# Unilogistix OpenBao foundation

Version: 0.2 | Updated: 2026-09-09 | Status: Bootstrap deployed and access-tested

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

- Declarative file audit enabled through SIGHUP without sealing the shared vault.
- Audit rotation tested; canary request logged; sampled issuer and runtime token values absent from raw logs.
- Logrotate retains fourteen rotations, with daily rotation and a 50 MB size condition evaluated when logrotate runs. This is not a hard disk-usage cap.
- Restricted issuer identity renews its 24-hour periodic lease and issues single-use AppRole credentials. A systemd timer runs every two minutes.
- Runtime canary tokens are stored root-only in `/run/unilogistix/bootstrap.token`, mode 0600. Bootstrap issuer custody is a root-only persistent file, not distributed trust.
- Simulated endpoint failure removes the runtime credential; the next successful service execution restores delivery.
- Raft snapshot saved and copied to a second host in protected storage. A disposable same-version vault accepted the snapshot and recovered its original 3-of-5 sealed state. The live vault was not sealed or restored.

## Outstanding before production credentials

Full restored-vault unseal is **not tested**: access to the distributed shares remains incomplete. Snapshot capture and transfer are currently manual execution by the agent, not scheduled recovery automation. The snapshot predates the last credential renewal and is not a substitute for ongoing backups.

The issuer expires if it cannot renew for 24 hours; recovery after that requires re-issuance by an authorized administrator. Shared operational-admin custody remains unchanged. Remote durable audit collection, disk-capacity monitoring, autonomous recovery, an action gateway, and provider-key rotation remain unfinished.

The transport is HTTP inside Tailscale; direct TLS is not configured. No provider credentials have been imported. The credential broker serves only the non-sensitive bootstrap canary, not production workloads.

The older lab installer and test scripts in the local workspace are unfinished
experiments; this deployment did not use them.

## Change history

- 0.2 — 2026-09-09: Added audit, rotation, automatic bootstrap delivery, outage tests, and partial restore evidence.
- 0.1 — 2026-09-09: Created isolated mount and role; passed live authorization tests.
