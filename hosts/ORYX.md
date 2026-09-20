# Oryx — host readiness

Version: 1.0 | Prepared: 2026-09-19 | Status: ready for container workloads

Unilogistix hardware (F-047). Prepared by Maestro (Gram) at the founder's
request so Team Truxon can deploy Forest Shield workers here; the services
themselves are Team Truxon's to deploy and operate.

## What it is

| | |
| --- | --- |
| Tailnet | `oryx` / 100.80.248.46, SSH as `ike` (key `~/.ssh/bao/oryx_id_ed25519`) |
| OS | Ubuntu 26.04.1 LTS, kernel 7.0.0-31-generic |
| CPU / RAM | 32 cores / 60 GB (58 GB free) |
| Disk | 915 GB, 847 GB free (same filesystem holds `/var/lib/docker`) |
| Swap | 8 GB |
| Docker | 29.8.1, Compose v5.5.1, service enabled, `ike` in the `docker` group |
| Runtime limits | cgroup v2; memory, PID and CPU limits verified working |

## Prepared on 2026-09-19

- `apt-get upgrade` applied (4 mutter packages); 0 pending, no reboot required.
- Unattended upgrades: already enabled. UFW: already active. Time: synced.
- `/etc/docker/daemon.json` created: json-file logs capped at 10 MB × 3 (an
  attachment parser can otherwise fill a disk with logs), `live-restore` so
  containers survive a daemon restart, and a 4096/8192 `nofile` default.
- Verified: `docker run --memory=256m --pids-limit=64 --cpus=1 --network=none`
  starts and the limit lands (`memory.max` = 268435456).

## Caveats for whoever deploys here

1. **Not a detonation host.** `deploy/shield-detonate`'s own README says "Not
   the NAS. Not Supabase. Not the office." Oryx is on the tailnet with SSH
   reach across the estate, so fetching hostile URLs here would put lateral
   movement one exploit away. Detonation belongs on a disposable, non-tailnet
   host. `shield-attach` (parses hostile bytes in a sandboxed container) and
   `shield-visual` are a good fit, with explicit limits.
2. **UFW does not filter Docker-published ports.** Anything published with
   `-p` bypasses UFW rules. Bind to `127.0.0.1:` or use the `DOCKER-USER`
   chain; do not assume the firewall covers a container.
3. **Containers can reach the tailnet** (including OpenBao on `vmai`). That is
   what lets a worker fetch its own secrets, and also what makes egress rules
   worth writing per compose file rather than host-wide.
4. **Per-container limits are not set for you.** Give every worker that parses
   untrusted input `--memory`, `--pids-limit`, `--cpus`, `--read-only` and
   `--cap-drop=ALL`; the host will honour them.

## Change history

- 1.0 — 2026-09-19: Host surveyed, updated and prepared for container
  workloads; deployment of Forest Shield workers left to Team Truxon.
