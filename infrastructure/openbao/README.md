# Unilogistix OpenBao foundation

Version: 0.6 | Updated: 2026-09-10 | Status: Backup hardening deployed and delivered-copy recovery verified; live upgrade pending

## Current verification

On September 10 the configured HTTPS health endpoint returned initialized,
unsealed and active. Secondary-host metadata showed six-hourly snapshot delivery,
with the latest observed copy less than four hours old. These checks establish
current health and delivery. A separately captured current snapshot subsequently
passed the isolated restore and upgrade checks described below.

The workstation recovery timer had no next run scheduled. An independently
reviewed calendar timer is now installed and repeated scheduling was observed.
The founder completed account authentication; host-state access and a subsequent
scheduled service run succeeded. Scheduling is repaired. This did not require
unsealing the live vault and does not qualify a future authentication expiry or
full host-loss recovery.

The deployed version requires security upgrade review against the current
[OpenBao advisory](https://github.com/openbao/openbao/security/advisories/GHSA-rh46-vc3j-w2w3).
The local 2.6.2 binary was installed from the official release and its archive
checksum verified. Synthetic integration tests passed. A current encrypted
snapshot also passed restoration with original custody on 2.4.4, followed by an
upgrade of the restored data to 2.6.2. Both stages verified cluster identity,
the nonsecret health canary and scoped access denials; the mount contract stayed
unchanged. The disposable test had no external network or source data volume and
was removed afterward. Private evidence retains the exact snapshot digest,
reviewed harness and earlier failed attempts. This qualifies the tested snapshot
and controls, not every credential, future backup or provider integration. The
live vault has not been upgraded, restarted, sealed or restored in this work.

Backup review found that the existing receiver's archive-name check and rolling
retention do not prove recoverability or preserve a separately verified recovery
checkpoint. Hardened sender/receiver code is now deployed with a dedicated
restricted upload account. The delivered archive's exact digest and receipt were
independently compared, then that received copy passed the isolated restore and
upgrade checks. The verified copy is pinned in a separate root-controlled
checkpoint directory outside candidate retention. The upload account cannot
traverse that directory or modify backup code/configuration.

The new six-hour snapshot timer and five-minute delivery-status timer are active
with future deadlines. The legacy snapshot timer is disabled; its definition and
archives are retained. Health and backup-status checks passed after cutover.
Monitoring distinguishes fresh delivery from separately qualified recovery;
local success does not establish continuing remote existence, external outage
notification or an immutable checkpoint against a compromised root administrator.

See [ADR-0002](../../decisions/ADR-0002-secrets-and-project-recovery.md) for the
founder's framework/project recovery scope. The existing shared cluster is one
backup source covering multiple projects, not separate project vault instances.

## Placement

Reuse the existing fleet OpenBao service. Unilogistix has a separate KV v2 mount,
`unilogistix/`, and separate AppRole auth mount, `unilogistix-approle/`.
This is policy isolation inside a shared service, not a separate security domain
against a compromised vault administrator. No additional server was purchased.

## Implemented basics

- KV v2 with required compare-and-set writes and ten retained versions.
- `bootstrap-reader` AppRole can read only the non-sensitive health canary.
- Explicit denial of the existing projects' `secret/` mount.
- Five-minute access tokens with a fifteen-minute maximum lifetime.
- Single-use SecretIDs expire after five minutes.
- Test credentials were revoked; no provider credentials were imported.

Live verification passed: allowed canary read; denied cross-project read,
unrelated Unilogistix read, write, administration and anonymous access;
rejected reused SecretID; denied access after token revocation.

## Reproduction

Run `bootstrap.py` on the trusted vault host with `BAO_ADDR` and
`BAO_ADMIN_TOKEN_FILE` set to its existing endpoint and protected operational
token file. The script reads credentials internally and prints only test results.
It creates or reconciles only the named Unilogistix mount, policy and role.
Do not supply token values as command arguments or publish them.

## Operational controls verified

- File audit logging enabled by configuration reload without sealing the shared vault; rotation and sampled raw-token absence checks passed.
- Four restricted provider AppRoles read only their assigned existing credential. Cross-provider access tests returned denial. The fixed read-only checker revokes each two-minute token after use and returns status only. It rejects arbitrary provider choices and follows no HTTP redirects.
- Cloudflare, Vercel, Supabase and Fireworks checks passed through those roles. Provider credentials remain in their existing source paths; they are not duplicated into Unilogistix.
- Bootstrap credentials refresh every two minutes; provider checks and issuer renewal run every six hours.
- HTTPS with certificate verification is provided by Tailscale Serve inside the tailnet. Unilogistix services use that endpoint; existing fleet HTTP consumers were not changed.
- A disposable same-version vault accepted a snapshot, unsealed using three distributed shares in memory, and successfully read the restored canary. The live vault was never sealed or restored during this drill.
- Snapshot capture and transfer run every six hours with a separate snapshot-only vault identity. The secondary receiver retains 28 snapshots, validates archive structure, and rejects uploads over 64 MiB.
- The secondary SSH key is restricted to the receiver. An arbitrary-command denial test passed. NAS forced-command enforcement failed testing, so that backup key was removed from NAS and delivery moved to Shield.
- A minute-based health timer checks vault health, credential age, successful secondary backup age, audit freshness and disk capacity. Failures produce nonzero systemd status and structured journal output.
- A workstation watcher can unseal the known cluster after an observed process restart. It preserves same-process manual seals, requires prior healthy-cluster evidence, and honors the operator pause marker. Four simulated safety tests passed; the live healthy check passed. No deliberate production restart was performed to test it.

## Operator pause

On the vault host, create `/var/lib/unilogistix/PAUSED` to stop the provider checker and prevent automatic unseal. Removing it restores eligibility for those operations. Snapshot and health checks continue. This is a technical control; the authenticated board interface is not implemented.

## Explicit remaining limits

- Full restore was tested, but replacement-host provisioning and traffic cutover are not automatic. This is not high availability.
- The watcher depends on this workstation being available. It does not initialize unknown vaults or recover without three reachable custodians.
- Administrative tokens remain under existing fleet custody. A workstation authorized to SSH to all three share holders is a common trust point; distributed share files do not make those permissions an independent security quorum.
- Issuers have renewable 24-hour leases; the backup identity has a renewable 48-hour lease. Longer outages require authorized re-issuance. The fixed checker does not autonomously create new provider accounts or rotate provider keys.
- Audit logs remain local to the vault host, with fourteen rotations. Remote immutable audit retention and external alert delivery are not configured. A local health timer cannot report its own host's total failure.
- Dedicated OpenBao roles are implemented; dedicated provider-side credentials are not. Existing source credentials retain their original provider permissions. The checker constrains its own operations to approved read endpoints; it is not a production deployment or spending gateway.
- No inference spending, infrastructure purchases, customer writes, deployments or payment actions were enabled.

The completed controls support bounded read-only credential use. Production write access requires a concrete workflow, resource scope, rotation method, budget where relevant, and evidence for its additional controls.

The older lab installer and test scripts in the local workspace are unfinished
experiments; this deployment did not use them.

## Change history

- 0.6 — 2026-09-10: Deployed restricted backup delivery, verified recovery from the delivered copy, pinned its checkpoint and switched monitoring/scheduling with legacy archives preserved.
- 0.5 — 2026-09-10: Recorded restored host access and successful current-snapshot restore/upgrade rehearsal; preserved live upgrade, backup cutover and recovery limits.
- 0.4 — 2026-09-10: Reverified current health and backup delivery, corrected recovery scheduling, and recorded upgrade/authentication/backup-integrity work still required.

- 0.3 — 2026-09-09: Verified full recovery, HTTPS, scoped provider access, scheduled backups and monitoring; documented residual limits.
- 0.2 — 2026-09-09: Added audit, rotation, automatic bootstrap delivery, outage tests, and partial restore evidence.
- 0.1 — 2026-09-09: Created isolated mount and role; passed live authorization tests.
