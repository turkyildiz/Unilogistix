# Unilogistix OpenBao foundation

Version: 0.1 | Updated: 2026-09-09 | Status: Bootstrap deployed and access-tested

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

## Outstanding before production credentials

The inspected shared service has no audit device. Audit logging and retention,
backup/restore verification for the new data, independent recovery, operational
admin custody, and automatic workload identity delivery remain unfinished.
The existing transport is HTTP inside Tailscale; direct TLS is not configured.
This bootstrap does not implement a secret-handling action gateway, rotation,
or unattended role credential delivery. Those controls need their own evidence.

The older lab installer and test scripts in the local workspace are unfinished
experiments; this deployment did not use them.

## Change history

- 0.1 — 2026-09-09: Created isolated mount and role; passed live authorization tests.
