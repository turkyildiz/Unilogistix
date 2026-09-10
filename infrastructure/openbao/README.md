# Unilogistix OpenBao foundation

Version: 0.7 | Updated: 2026-09-10 | Status: Inspected fleet upgraded to 2.6.2; delivered post-upgrade snapshot restored and checkpoint verified

## Current verification

On September 10 the inspected fleet service was upgraded to OpenBao 2.6.2 using
an independently reviewed maintenance procedure and a pinned official image.
Verified HTTPS health reports the expected cluster, initialized, unsealed and
active; Docker health also passes. The upgrade addresses the version finding in
[the OpenBao advisory](https://github.com/openbao/openbao/security/advisories/GHSA-rh46-vc3j-w2w3).

The original container and storage remain preserved and stopped. Production uses
a separately copied and qualified data volume, selected durably by the default
Compose configuration under a new project name. The old binary was never run
against upgraded storage. Once production traffic could resume, automatic
rollback was forbidden; reverting older authority would require reconciliation
of any accepted writes, revocations and credentials.

A snapshot delivered after the upgrade passed an isolated 2.6.2 restore with
original custody, expected cluster identity, the nonsecret canary and scoped
access denials. The test had no external network or production data volume;
owned-container removal and cleanup were confirmed. That exact received archive
was pinned separately under root control and its digest and permissions rechecked.
Earlier verified checkpoints and legacy archives remain preserved. Private
records retain exact source identifiers, image and archive digests, reviews,
execution evidence and failed attempts without publishing credentials.

Health, delivery-status, credential-refresh and fixed provider checks passed.
Health and rotation configuration now point to the active audit file rather than
preserved rollback storage; the updated rotation rule passed a debug-only parse.
The workstation watcher returned to its prior enabled/active state and passed;
only the maintenance-owned pause marker was removed. The six-hour snapshot and
five-minute delivery-status timers remain active. The legacy snapshot timer is
disabled, with its definition and archives retained.

Current development credentials for Truxon and Freightex were separately verified
against this inspected fleet service, with their distinct existing policies
preserved. This confirms development policy separation on one observed cluster;
it does not establish every hosted endpoint override, absence of independent
external vaults, or complete recovery coverage for either company. No company
credentials, policies or vaults were merged.

The dedicated backup upload account cannot traverse the separately protected
checkpoint directory or modify backup code/configuration. Delivery receipts are
verified independently against actual stored bytes. Fresh delivery is distinct
from a qualified restore; local monitoring does not prove continuing remote
existence, external outage notification or immutability against a root compromise.

See [ADR-0002](../../decisions/ADR-0002-secrets-and-project-recovery.md) for the
framework and project recovery contract. Completion here is limited to this
inspected fleet and the tested snapshots and controls. Broader company readiness,
financial repairs and future independent project vaults remain separate work.

## Placement

Reuse the existing fleet OpenBao service. Unilogistix has a separate KV v2 mount,
`unilogistix/`, and separate AppRole auth mount, `unilogistix-approle/`.
This is policy isolation inside a shared service, not a separate security domain
against a compromised vault administrator. No additional server was purchased. Current consumer coverage is limited to the verified development credentials and named operational checks above.

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

- File audit logging is enabled; rotation and sampled raw-token absence checks passed.
- Four restricted provider AppRoles read only their assigned existing credential. Cross-provider access tests returned denial. The fixed read-only checker revokes each two-minute token after use and returns status only. It rejects arbitrary provider choices and follows no HTTP redirects.
- Cloudflare, Vercel, Supabase and Fireworks checks passed through those roles. Provider credentials remain in their existing source paths; they are not duplicated into Unilogistix.
- Bootstrap credentials refresh every two minutes; provider checks and issuer renewal run every six hours.
- HTTPS with certificate verification is provided by Tailscale Serve inside the tailnet. Unilogistix services use that endpoint; existing fleet HTTP consumers were not changed.
- An earlier isolated same-version drill accepted a snapshot, unsealed using three distributed shares in memory, and successfully read the restored canary. That drill did not seal or restore the live vault.
- Snapshot capture and transfer run every six hours with a separate snapshot-only vault identity. The secondary receiver retains 28 unverified candidates, validates bounded archive structure/internal checksums, and rejects uploads over 64 MiB. Restore-qualified checkpoints are protected separately from candidate pruning.
- The secondary SSH key is restricted to the receiver. An arbitrary-command denial test passed. An earlier receiver failed forced-command testing; its backup key was removed and delivery moved to the verified secondary receiver.
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
- No general inference-spending, infrastructure-purchase, customer-write, application-deployment or payment gateway was enabled by these credential controls. The bounded vault maintenance described above was separately authorized and completed.

The completed controls support bounded read-only credential use. Production write access requires a concrete workflow, resource scope, rotation method, budget where relevant, and evidence for its additional controls.

Synthetic tests and current-data restore rehearsals provide different evidence.
Neither substitutes for the measured production and delivered-copy checks above.

## Change history

- 0.7 — 2026-09-10: Recorded completed fleet security upgrade, durable storage cutover, verified post-upgrade delivered-copy recovery, restored monitoring and current development-policy separation; retained broader coverage limits.

- 0.6 — 2026-09-10: Deployed restricted backup delivery, verified recovery from the delivered copy, pinned its checkpoint and switched monitoring/scheduling with legacy archives preserved.
- 0.5 — 2026-09-10: Recorded restored host access and successful current-snapshot restore/upgrade rehearsal; preserved live upgrade, backup cutover and recovery limits.
- 0.4 — 2026-09-10: Reverified current health and backup delivery, corrected recovery scheduling, and recorded upgrade/authentication/backup-integrity work still required.

- 0.3 — 2026-09-09: Verified full recovery, HTTPS, scoped provider access, scheduled backups and monitoring; documented residual limits.
- 0.2 — 2026-09-09: Added audit, rotation, automatic bootstrap delivery, outage tests, and partial restore evidence.
- 0.1 — 2026-09-09: Created isolated mount and role; passed live authorization tests.
