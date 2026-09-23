# D-009 — Controller service token: periodic renewable token for the Lang service

Status: DRAFT for Board signature. Prepared by Maestro (Gram) 2026-09-22 after D-008 activation (F-086) showed the enrolled AppRole cannot feed a long-running service. Sherlock review required.

## Problem
`auth/unilogistix-approle/role/corporate-os-controller` (F-053/F-054): `token_ttl 5m`, `token_max_ttl 15m`, `token_period 0`, SecretID single-use, 5 min, CIDR-bound to the tunnel. Correct for a qualification ceremony; a service token dies within 15 minutes. `corporate-os-lang` reads `OPENBAO_CONTROLLER_TOKEN` from `/var/lib/unilogistix/corporate-os/controller.env`; today the file is empty, so every seat invocation parks `seat_unavailable`.

## Change (one role, three fields)
| field | now | after |
|---|---|---|
| `token_period` | 0s | **24h** (periodic token: renewable indefinitely while renewed; each renewal resets the 24h clock) |
| `token_ttl` / `token_max_ttl` | 5m / 15m | unchanged for non-periodic use; ignored for periodic tokens |
| `token_num_uses` | 0 | 0 (unchanged) |
| everything else | | **unchanged**: policies `corporate-os-controller` only, `token_bound_cidrs 100.118.119.6`, `secret_id_bound_cidrs 100.118.119.6/32`, `secret_id_num_uses 1`, `secret_id_ttl 5m`, service token type |

Renewal: a root-run systemd timer `corporate-os-token-renew.timer` every 6h runs `bao token renew-self` through the loopback tunnel with the token from `controller.env`; failure to renew → audit event `lang.controller_token_renew_failed` and the token expires within 24h → seats park. Revocation: `bao token revoke <accessor>` (accessor recorded at login in the register, not the token) kills the service token instantly; F-054 emergency stop unchanged.

## Login ceremony (founder, once per boot of the token)
1. On Gram: `bash ~/corp-os-enrol/enrol.sh issue` → role_id (not secret) + one wrapped SecretID (5 min, single use).
2. On oryx as root: `~/corp-os-enrol/d009-login.sh <role_id> <wrapping_token>` → unwraps through the loopback tunnel, logs in, writes `OPENBAO_CONTROLLER_TOKEN=<token>` to `controller.env` (0600 root:root), prints the **accessor** only, restarts `corporate-os-lang`.
3. Maestro records the accessor and issue time in the register.

## Not changed
No new policy paths. No new roles. Deny rules intact. Token never leaves oryx; Maestro never sees it.

## Duration
Standing (the role setting persists); the token itself lives while renewed. Board may revoke the token or reset `token_period` to 0 at any time.
