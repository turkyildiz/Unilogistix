# Supabase house-cleaning audit — 2026-09-19

Static, read-only audit of the Supabase usage in the Truxon and Freightex
repos, against the founder's house-cleaning checklist. This audit was done
**without any live database access** — no credentials were read, printed, or
used. Everything in `truxon.md` / `freightex.md` marked `NEEDS LIVE CHECK` or
`UNKNOWN` requires the owning team (Team Truxon / Team Freightex) to actually
run `db-audit.sql` against their own project, and/or check their hosted
Supabase dashboard settings directly.

## Files in this folder

- `truxon.md` — 12-item checklist findings for the Truxon Supabase project(s), with repo evidence and severity-ranked recommended fixes.
- `freightex.md` — same, for the Freightex Supabase project (ref `wbfonwbwodhisfszzeyo`).
- `db-audit.sql` — a generic, read-only SQL script (wrapped in `begin transaction read only; ... rollback;`) that answers the DB-side (live) parts of the checklist: RLS/FORCE status, FK-without-index, public buckets, `cron.job`, triggers, SECURITY DEFINER functions without a pinned `search_path`, BYPASSRLS roles, grants to `anon`, and the migration ledger.
- This `README.md`.

## How the founder runs `db-audit.sql` — without exposing credentials

The goal is: run the script against a project's Postgres connection, without
that connection string ever landing in shell history, a log file, a repo, or
this chat. Three options, cheapest/safest first.

### Option A — Supabase Studio SQL Editor (recommended, zero credential handling)

1. Log in to the Supabase dashboard for the project (Truxon or Freightex — each team owns its own project's dashboard access).
2. Open **SQL Editor**.
3. Paste the contents of `db-audit.sql` in as-is (it's already wrapped in a read-only transaction, so even a partial paste/run is inert against writes).
4. Run it, review results section by section, save/export as needed.

No connection string is ever typed or copied — the dashboard is already
authenticated. This is the option to hand to a non-technical stakeholder.

### Option B — `psql` with the DB URL read from the owning team's vault, never persisted

Each team keeps its own project's connection string in its own vault, not in
this audit's repo:

- **Truxon**: `truxon/deploy/secrets/INVENTORY.md` — "Truxon/Supabase" section (service_role, CRON_SECRET, DB password, anon key → KeePassXC vault). The canonical prod project ref (`okoeeyxxvzypjiumraxq`) is currently scattered across ~12 deploy scripts rather than named once in INVENTORY.md — see `truxon.md` item 1 for the full list of paths, and consider fixing that as part of this house-cleaning pass.
- **Freightex**: `freightex/deploy/secrets/INVENTORY.md` (mother project ref `wbfonwbwodhisfszzeyo`, per its header) and the machine-readable copy `freightex/deploy/secrets/inventory.json`.

In both cases this audit references the *path* only — no secret value was read or printed.

A wrapper that never writes the secret to disk or shell history:

```bash
#!/usr/bin/env bash
set -euo pipefail
# Example only — substitute the owning team's actual vault read command.
# The key property: the URL lives only in this subshell's memory, is never
# echoed, exported to a file, or passed as a CLI arg (which would land in
# `ps`/shell history) — read it via a var from a command substitution and
# feed it to psql's -f, not a here-string with the URL in it.
DB_URL="$(vault kv get -field=database_url secret/<team>/<project>/db)"
psql "$DB_URL" -f db-audit.sql
unset DB_URL
```

Notes:
- Use `vault kv get` (or whatever the owning team's actual secret store CLI is — OpenBao is referenced in Truxon's `deploy/openbao/` for their infra secrets; confirm whether the Supabase DB URL itself lives there or in Supabase's own project settings) rather than pasting the URL by hand.
- Never put `$DB_URL` in a script argument that shows up in `ps aux` on a shared box — the `psql "$DB_URL"` invocation above is fine on a single-user machine; on a shared host prefer a `~/.pgpass` line (mode 0600) or `PGSERVICEFILE` instead so the password never appears in argv at all.
- `unset DB_URL` afterward, and don't leave the shell's history file capturing the command if `HISTCONTROL=ignorespace` isn't set — prefix the command with a space, or just use Option A.

### Option C — Supabase CLI, project-linked, using its own credential store

If the team already has `supabase login` + `supabase link --project-ref <ref>`
set up locally, they can run:

```bash
supabase db execute --file db-audit.sql
```

(or the current CLI's equivalent flag — check `supabase db --help` for the
installed version) which uses the CLI's own stored session rather than a
manually-typed connection string.

## Which "live checks" to run, per project

The per-project `truxon.md` / `freightex.md` files each end with a bullet
list of every checklist item this static audit could not resolve from the
repo alone (Auth rate-limit settings, actual restore-test history, live
`cron.job` contents, live RLS FORCE/BYPASSRLS state, live row counts across
candidate duplicate-concept tables, live connection/pooling behavior under
load). Run `db-audit.sql` first — it answers most of them in one pass — then
use the dashboard for the couple of settings (Auth rate limits, restore-test
evidence) that aren't Postgres catalog objects at all.

## Scope / limitations of this audit

- Read-only, static analysis of the Truxon (`/home/ike/work/truxon`, branch
  `main`) and Freightex (`/home/ike/work/freightex`, branch `main`) repos as
  checked out at audit time. No `git fetch`/`pull` was run, so if Truxon's
  local `main` was behind `origin/main` at audit time, that gap is noted in
  `truxon.md`.
- `truxon-wt/` contains ~19 separate git worktrees on `claude/*` feature
  branches (not `main`) — these were not audited in depth; they're
  in-flight work, not the shipped default branch.
- No secret values were read or printed anywhere in this audit — only
  variable names, file paths, and vault/dashboard path references.
- No frontend deploy, no `supabase link`/deploy, no live DB queries were run.
