-- ============================================================================
-- Unilogistix Supabase house-cleaning audit — generic READ-ONLY catalog queries
-- ============================================================================
-- Safe to run against ANY Supabase/Postgres project (Truxon, Freightex, or any
-- future Unilogistix project). Every statement is read-only and the whole
-- script runs inside a READ ONLY transaction that is always rolled back, so it
-- cannot modify data, schema, or catalog state under any circumstance.
--
-- Run it with the Supabase SQL editor, or with psql:
--   psql "$DATABASE_URL" -f db-audit.sql
-- (see README.md in this same folder for how to get a DATABASE_URL without
-- exposing it in shell history / logs).
--
-- Each section is labelled with the checklist item it answers. Sections are
-- independent SELECTs — run the whole file, or copy out one section at a time
-- into the Supabase Studio SQL editor.
-- ============================================================================

begin transaction read only;

-- ----------------------------------------------------------------------------
-- 0. Context: which database / project am I looking at?
-- ----------------------------------------------------------------------------
select current_database() as database,
       current_setting('server_version') as pg_version,
       now() as run_at;

-- ----------------------------------------------------------------------------
-- 2. RLS enabled with effectively-`true` policies
-- ----------------------------------------------------------------------------
-- 2a. Tables with RLS disabled entirely (in public schema; adjust schema list
--     as needed). An exposed-to-PostgREST table with RLS off and a `grant` to
--     anon/authenticated is a wide-open table.
select n.nspname as schema, c.relname as table,
       c.relrowsecurity as rls_enabled,
       c.relforcerowsecurity as rls_forced
from pg_class c
join pg_namespace n on n.oid = c.relnamespace
where c.relkind = 'r'
  and n.nspname in ('public')
  and c.relrowsecurity = false
order by 1, 2;

-- 2b. Policies whose USING/WITH CHECK expression is a bare `true` (or missing,
--     which PostgREST treats as unrestricted for the given command). These are
--     the classic "RLS is on but does nothing" trap.
select schemaname, tablename, policyname, cmd, roles,
       qual as using_expr, with_check as check_expr
from pg_policies
where schemaname = 'public'
  and (
        qual is null or trim(both '()' from qual) = 'true'
        or with_check is null or trim(both '()' from with_check) = 'true'
      )
order by 1, 2, 3;

-- 2c. All policies, for manual review of anything not caught by 2b (e.g.
--     `auth.role() = 'authenticated'` with no tenant/user_id scoping is also
--     effectively-true across tenants).
select schemaname, tablename, policyname, permissive, roles, cmd,
       qual as using_expr, with_check as check_expr
from pg_policies
where schemaname = 'public'
order by 1, 2, 3;

-- ----------------------------------------------------------------------------
-- 2b. RLS enabled but NOT forced — table owner (and any BYPASSRLS role)
--     silently skips the policy
-- ----------------------------------------------------------------------------
-- Postgres/Supabase fact: RLS policies never apply to the table owner unless
-- `ALTER TABLE ... FORCE ROW LEVEL SECURITY` is also set, and never apply to
-- any role with the BYPASSRLS attribute (Supabase's `service_role` has
-- BYPASSRLS by design — that's expected and FORCE does not change it).
-- The risk is everything else that quietly runs as the table owner: a
-- migration script, a `pg_cron` job, or dashboard SQL executed by the
-- `postgres` role all bypass a correct policy if FORCE isn't set. Before
-- flipping FORCE on, note that any SECURITY DEFINER function *owned by that
-- same table owner* becomes subject to RLS the moment FORCE is enabled, so
-- each such function must be retested (or repoliced / given its own
-- appropriately-scoped role) first.

-- 2b-i. Per RLS-enabled table: is FORCE set, and who owns it?
select
  n.nspname as schema,
  c.relname as table,
  c.relrowsecurity as rls_enabled,
  c.relforcerowsecurity as rls_forced,
  own.rolname as table_owner,
  own.rolbypassrls as owner_has_bypassrls
from pg_class c
join pg_namespace n on n.oid = c.relnamespace
join pg_roles own on own.oid = c.relowner
where c.relkind = 'r'
  and n.nspname = 'public'
  and c.relrowsecurity = true
order by (c.relforcerowsecurity = false) desc, 1, 2; -- not-forced tables first

-- 2b-ii. Every role with BYPASSRLS (service_role should be the expected one;
--        flag anything else, e.g. a role used by an ORM/migration runner).
select rolname, rolbypassrls, rolsuper, rolcanlogin
from pg_roles
where rolbypassrls = true
order by rolname;

-- 2b-iii. pg_cron job owners — a cron job's SQL runs as this role. If it's the
--         table owner (commonly `postgres`) and FORCE isn't set on tables it
--         touches, the job silently bypasses RLS today (harmless until FORCE
--         is added — then it must be re-verified against policies, or run as
--         a role scoped with its own policy/grants instead).
select jobid, schedule, command, username as runs_as_role, active
from cron.job
order by jobid;

-- 2b-iv. SECURITY DEFINER functions with their owning role — cross-reference
--        against 2b-i: a SECURITY DEFINER function owned by a table's owner
--        will start being subject to that table's RLS once FORCE is enabled
--        on it, which can silently break the function's own writes/reads if
--        no policy permits the definer's implicit role context.
select
  n.nspname as schema,
  p.proname as function_name,
  pg_get_function_identity_arguments(p.oid) as args,
  p.prosecdef as security_definer,
  own.rolname as function_owner,
  own.rolbypassrls as owner_has_bypassrls
from pg_proc p
join pg_namespace n on n.oid = p.pronamespace
join pg_roles own on own.oid = p.proowner
where n.nspname = 'public'
  and p.prosecdef = true
order by 1, 2;

-- ----------------------------------------------------------------------------
-- 3. FK columns without a supporting index
-- ----------------------------------------------------------------------------
-- Postgres does NOT auto-index the referencing side of a foreign key. A FK
-- column with no index means every parent-row UPDATE/DELETE does a seq scan
-- of the child table to check/cascade, and joins on the FK are slow.
with fkeys as (
  select
    con.conname as constraint_name,
    con.conrelid as child_table_oid,
    ns.nspname as child_schema,
    cl.relname as child_table,
    con.confrelid as parent_table_oid,
    array_agg(att.attname order by u.ord) as fk_columns,
    array_agg(att.attnum order by u.ord) as fk_attnums
  from pg_constraint con
  join pg_class cl on cl.oid = con.conrelid
  join pg_namespace ns on ns.oid = cl.relnamespace
  join unnest(con.conkey) with ordinality as u(attnum, ord) on true
  join pg_attribute att on att.attrelid = con.conrelid and att.attnum = u.attnum
  where con.contype = 'f'
    and ns.nspname = 'public'
  group by 1,2,3,4,5
),
indexed as (
  select
    i.indrelid as table_oid,
    array_agg(a.attname order by k.ord) as index_columns
  from pg_index i
  join unnest(i.indkey::int2[]) with ordinality as k(attnum, ord) on true
  join pg_attribute a on a.attrelid = i.indrelid and a.attnum = k.attnum
  group by i.indexrelid, i.indrelid
)
select
  f.child_schema,
  f.child_table,
  f.constraint_name,
  f.fk_columns
from fkeys f
where not exists (
  select 1
  from indexed idx
  where idx.table_oid = f.child_table_oid
    -- the FK columns must be a *prefix* of some index's columns
    and idx.index_columns[1:array_length(f.fk_columns,1)] = f.fk_columns
)
order by 1, 2;

-- ----------------------------------------------------------------------------
-- 4. Public storage buckets
-- ----------------------------------------------------------------------------
select id as bucket_id, name, public, file_size_limit, allowed_mime_types,
       created_at
from storage.buckets
order by public desc, name;

-- 4b. Storage RLS policies on storage.objects (bucket-scoped access rules) —
--     review any bucket above with public=true alongside its object policies.
select policyname, permissive, roles, cmd, qual as using_expr, with_check
from pg_policies
where schemaname = 'storage' and tablename = 'objects'
order by policyname;

-- ----------------------------------------------------------------------------
-- 5. Triggers — inventory for manual review of single-row assumptions
-- ----------------------------------------------------------------------------
-- Lists every trigger and its level (ROW vs STATEMENT) and timing. A ROW-level
-- trigger whose function reads/writes exactly one NEW/OLD record is fine for
-- single-row DML but silently only fires once per row even under a bulk
-- UPDATE ... WHERE matching many rows (that's expected), whereas STATEMENT
-- triggers that assume a single affected row (e.g. via `SELECT ... INTO`
-- without aggregation) are the risky pattern. Function source is included so
-- you can eyeball for `NEW`/`OLD` single-row logic vs bulk-safe FOR EACH ROW.
select
  t.tgname as trigger_name,
  n.nspname as schema,
  c.relname as table,
  case t.tgtype::int & 1 when 1 then 'ROW' else 'STATEMENT' end as level,
  case
    when t.tgtype::int & 66 = 2 then 'BEFORE'
    when t.tgtype::int & 66 = 64 then 'INSTEAD OF'
    else 'AFTER'
  end as timing,
  p.proname as function_name,
  pg_get_functiondef(p.oid) as function_source
from pg_trigger t
join pg_class c on c.oid = t.tgrelid
join pg_namespace n on n.oid = c.relnamespace
join pg_proc p on p.oid = t.tgfoid
where not t.tgisinternal
  and n.nspname = 'public'
order by 2, 3, 1;

-- ----------------------------------------------------------------------------
-- 6. Migration drift — objects present in the catalog vs recorded migrations
-- ----------------------------------------------------------------------------
-- 6a. Supabase CLI's migration ledger — compare this list against the
--     `supabase/migrations/*.sql` filenames in the repo. Any DB row with no
--     matching file (or vice versa) is drift.
select version, name
from supabase_migrations.schema_migrations
order by version;

-- 6b. All user-defined functions/procedures, with their definitions, so you
--     can grep for ones never introduced by a migration file (dashboard-authored
--     functions are legal but must be reconciled back into a migration).
select n.nspname as schema, p.proname as function_name,
       pg_get_function_identity_arguments(p.oid) as args,
       l.lanname as language
from pg_proc p
join pg_namespace n on n.oid = p.pronamespace
join pg_language l on l.oid = p.prolang
where n.nspname = 'public'
order by 1, 2;

-- 6c. All tables + approximate row counts, for cross-checking against models
--     used in app code / duplicate-concept review (item 11).
select schemaname, relname as table, n_live_tup as approx_row_count
from pg_stat_user_tables
where schemaname = 'public'
order by relname;

-- ----------------------------------------------------------------------------
-- 7. anon key -> Supabase Auth directly (bypassing app rate limiting)
-- ----------------------------------------------------------------------------
-- This is not fully answerable from SQL (Auth rate limits are a project-level
-- dashboard/API setting, not a DB object) — see README.md "live checks" list.
-- What SQL *can* show: whether public self-signup is enabled at the DB/Auth
-- config level is outside pg_catalog; check supabase/config.toml `[auth]`
-- `enable_signup` in-repo, and confirm the *hosted* project's Auth settings
-- (Dashboard > Authentication > Rate Limits, and > Providers > Email
-- "Allow new users to sign up") match what the repo assumes.
select 'See README.md live-check list — Auth rate limits are not pg_catalog objects' as note;

-- ----------------------------------------------------------------------------
-- 8. Backups — never fully verifiable from inside the DB
-- ----------------------------------------------------------------------------
-- Whether a restore has ever been *tested* is an operational fact, not a DB
-- object. What SQL can show: WAL/replication and extension state that backups
-- may depend on.
select name, setting from pg_settings
where name in ('wal_level', 'archive_mode', 'max_wal_senders');

select extname, extversion from pg_extension order by extname;

-- ----------------------------------------------------------------------------
-- 9. Connection pooling fit
-- ----------------------------------------------------------------------------
-- 9a. Current connection count and mode, by application_name / backend type —
--     helps see if edge functions are using many direct (non-pooled)
--     connections instead of PgBouncer/Supavisor.
select application_name, count(*) as connections,
       count(*) filter (where state = 'active') as active,
       count(*) filter (where state = 'idle') as idle
from pg_stat_activity
where pid <> pg_backend_pid()
group by 1
order by connections desc;

-- 9b. Prepared statements currently held open per session — a prepared
--     statement surviving across pooled "transactions" is the classic
--     PgBouncer-transaction-mode incompatibility signal (should normally be
--     empty/near-empty on a well-behaved transaction-mode pooled connection).
select count(*) as open_prepared_statements
from pg_prepared_statements;

-- ----------------------------------------------------------------------------
-- 10. Cron jobs (pg_cron) — compare against supabase/functions/* and docs
-- ----------------------------------------------------------------------------
select jobid, schedule, command, nodename, database, active
from cron.job
order by jobid;

-- 10b. Recent run history (if pg_cron's job_run_details is available) to see
--      which schedules are actually firing / failing.
select jobid, status, return_message, start_time, end_time
from cron.job_run_details
order by start_time desc
limit 50;

-- ----------------------------------------------------------------------------
-- 11. Multiple tables/views claiming the same concept
-- ----------------------------------------------------------------------------
-- Naive but useful: table/view names that share a normalized "stem" (strip
-- common prefixes/suffixes) often indicate parallel/duplicate concepts
-- (e.g. drivers vs driver_profiles vs active_drivers). Manual review required
-- — this just surfaces candidates.
select
  regexp_replace(relname, '^(active_|all_|v_|mv_)|(_view|_v2|_legacy|_old)$', '', 'g') as normalized_stem,
  array_agg(relname order by relname) as candidate_tables_or_views
from pg_class c
join pg_namespace n on n.oid = c.relnamespace
where n.nspname = 'public'
  and c.relkind in ('r', 'v', 'm')
group by 1
having count(*) > 1
order by 1;

-- ----------------------------------------------------------------------------
-- 12. Auth triggers — coverage across signup methods (password/OAuth/magic
--     link/phone)
-- ----------------------------------------------------------------------------
-- Lists every trigger on auth.users (Supabase fires the same `auth.users`
-- INSERT regardless of signup method, so a single well-written trigger DOES
-- cover all methods — but many hand-rolled ones read provider-specific
-- metadata (e.g. raw_user_meta_data->>'full_name' only ever set by the
-- password/OAuth flow) and silently produce incomplete profile rows for
-- other methods. Inspect function_source below for provider-specific field
-- reads that aren't null-guarded.
select
  t.tgname as trigger_name,
  case t.tgtype::int & 1 when 1 then 'ROW' else 'STATEMENT' end as level,
  case
    when t.tgtype::int & 66 = 2 then 'BEFORE'
    when t.tgtype::int & 66 = 64 then 'INSTEAD OF'
    else 'AFTER'
  end as timing,
  p.proname as function_name,
  pg_get_functiondef(p.oid) as function_source
from pg_trigger t
join pg_class c on c.oid = t.tgrelid
join pg_namespace n on n.oid = c.relnamespace
join pg_proc p on p.oid = t.tgfoid
where not t.tgisinternal
  and n.nspname = 'auth'
  and c.relname = 'users'
order by t.tgname;

-- ----------------------------------------------------------------------------
-- Extra: SECURITY DEFINER functions without a pinned search_path
-- ----------------------------------------------------------------------------
-- A SECURITY DEFINER function with no explicit `search_path` setting is
-- vulnerable to search_path hijacking (a caller-controlled schema earlier in
-- the path can shadow a table/function the definer-owner intended to hit).
select
  n.nspname as schema,
  p.proname as function_name,
  pg_get_function_identity_arguments(p.oid) as args,
  p.prosecdef as security_definer,
  p.proconfig as proconfig -- look for 'search_path=...' entries; NULL/absent = not pinned
from pg_proc p
join pg_namespace n on n.oid = p.pronamespace
where n.nspname = 'public'
  and p.prosecdef = true
  and (p.proconfig is null
       or not exists (
         select 1 from unnest(p.proconfig) cfg where cfg like 'search_path=%'
       ))
order by 1, 2;

-- ----------------------------------------------------------------------------
-- Extra: grants to `anon` / `authenticated` roles (PostgREST-exposed surface)
-- ----------------------------------------------------------------------------
select grantee, table_schema, table_name,
       array_agg(privilege_type order by privilege_type) as privileges
from information_schema.role_table_grants
where table_schema = 'public'
  and grantee in ('anon', 'authenticated')
group by 1, 2, 3
order by 1, 2, 3;

-- Column-level grants (rarer, but a table-level REVOKE + column-level GRANT
-- pattern can hide a privileged column from this summary if you only check
-- table grants elsewhere).
select grantee, table_schema, table_name, column_name,
       array_agg(privilege_type order by privilege_type) as privileges
from information_schema.role_column_grants
where table_schema = 'public'
  and grantee in ('anon', 'authenticated')
group by 1, 2, 3, 4
order by 1, 2, 3, 4;

-- ----------------------------------------------------------------------------
-- Extra: schema_migrations ledger, full list (supports item 6 cross-check)
-- ----------------------------------------------------------------------------
select version, name, statements is not null as has_statements
from supabase_migrations.schema_migrations
order by version;

rollback;

-- ============================================================================
-- End of script. `rollback` above guarantees nothing done in this session —
-- including anything accidentally destructive pasted in by hand — is
-- committed, as long as you run the whole file (or at minimum keep the
-- `begin transaction read only; ... rollback;` wrapper around whatever subset
-- you copy out).
-- ============================================================================
