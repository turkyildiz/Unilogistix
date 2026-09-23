# Lang boot knowledge (Board-authored, status: accepted)

Loaded into Lang's §14 knowledge store at boot as `company_scope=framework`, `author_seat=board`, `status=accepted`, `proof_ref=BOARD_REGISTER.md`. Lang reads these before its first assign. Lang may not edit this file.

| id | fact | source |
|---|---|---|
| K-001 | Every machine the group operates is Unilogistix hardware and may host any Unilogistix workload — Gram, VMAI, Homedev, Deskdev, the UGREEN NAS, Lynx, the Hetzner hosts, oryx. Contained so it never disturbs another company's production service. | F-047 (2026-09-18), restated by the founder for Lang on 2026-09-22 (F-072) |
| K-002 | Hardware is shared; credentials, accounts, authority, customer data and money are not. Each company keeps its own (F-036). Secrets live in OpenBao (F-037); Lang references paths, never values. | F-036, F-037 |
| K-003 | Aida, AOL, Truxon and Freightex are Unilogistix companies. DQFile is Team DQF. Puralba is the first non-trucking toolbox instance; Truxon and Freightex names never appear in Puralba outputs. | F-047, F-039, F-038 |
| K-004 | Lang runs on oryx today. If oryx is off, Lang is off; tasks resume from checkpoint when it returns. Continuity elsewhere (R59) is a Board decision queued after Lang is operational. | F-071 discussion, 2026-09-22 |
| K-005 | Lang may live on any Unilogistix machine only as a co-tenant: no conflicts with, and no performance reduction of, the services already there. Concretely: run under its own user and cgroup with CPU and memory limits, its own ports and directories, no shared secrets, no changes to another service's config; if a measurement shows an existing service slowed, Lang yields first. The existing service has priority on its host. | founder, 2026-09-22 (F-073), extends K-001 |
