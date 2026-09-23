# D-008 — Lang closed loop: seat identities, standing merge mandate, deploy register

Status: DRAFT for Board signature. Prepared by Maestro (Gram) on 2026-09-22 from founder direction F-076 ("i actually wated lang to write the code , deploy test and merge. not me sitting here"). Sherlock review required. Takes effect when the founder signs the action envelope in `~/board-sign/d008/` and the runtime consumes it (PR by Codex).

Scope: `turkyildiz/unilogistix-corporate-os` only. Nothing here touches company repositories (F-069/F-070 stay read-only), OpenBao secrets other than the seat paths named below, or the §9 reserved list.

## A. Seat identities (F-036, F-037, contract §10, §11.5)

| Seat | GitHub identity | CLI / API credential | OpenBao path (kv v2) | Used for |
|---|---|---|---|---|
| Cody | App `unilogistix-corporate-os-ci` (id 5017230, installation 163403482) — existing | Codex CLI login token | `unilogistix/corporate-os/seats/cody/codex-token` | push branches, open PRs (author) |
| Cindy | **new** App `unilogistix-corporate-os-cindy` — founder creates; permissions: pull_requests: write, contents: read, metadata: read; this repo only | Claude CLI login token | `unilogistix/corporate-os/seats/cindy/github-app.pem`, `…/cindy/claude-token` | review and approve PRs (approver ≠ author) |
| Garry | none (comments via Cody's App as "security review by Garry") | Grok CLI token | `unilogistix/corporate-os/seats/garry/grok-token` | security review |
| Owen | none | local llama-server, no credential | — | deploy via the deploy script |
| Maestro | appointed by the Board; not staffed by this decision | — | — | — |

Controller policy amendment (same shape as F-066): `read` on `unilogistix/data/corporate-os/seats/*`; everything else under `corporate-os/*` stays denied. Tokens are written by the founder with `-cas`, never printed; the service reads them at seat-invoke time and never persists them in the ledger (secret scan on every seat output stays).

Per-seat OS users remain a later gate (§11.5). All seats run as `corporate-os` under the Lang unit's cgroup, each with its own `$HOME` under `/var/lib/unilogistix/corporate-os/seats/<seat>/` (mode 0700), its own session id (uuid5 of the seat name) and prompt source.

## B. Standing merge mandate (replaces per-PR founder approval of F-055 inside this repository)

A pull request to `main` of `unilogistix-corporate-os` merges **without founder action** when all of the following are true, verified by the runtime before it calls merge:

1. Author is the Cody App. Head is on a branch Lang created for a task with a `task_id` in the ledger.
2. Cindy approval: a review with state APPROVED posted by the Cindy App, on the exact head SHA, with the first line `VERDICT: ACCEPT` and the task_id.
3. Garry security verdict on the exact head SHA with no CHANGES_REQUIRED.
4. `foundation` check green on the head; head up to date with `main`.
5. The diff touches none of the reserved paths: `governance/**`, `infrastructure/**`, `.github/**`, `pyproject.toml`, `uv.lock`, `scripts/deploy_main_to_oryx.sh`, `orchestrator/board_*.py`, `orchestrator/approvals.py`, `orchestrator/pr_executor.py`, any OpenBao policy file. A diff touching any of these parks the task to the Board (`hold_board`).
6. Rule of Four honoured: `exchange_count ≤ 4` on the task; at 4 it parked for Judy instead.
7. Merge method: merge commit. Merge commit body cites task_id, Cindy review id, Garry verdict id.

The founder keeps approval for everything in 5, for contract edits (F-060 §9), OpenBao policy, spend beyond F-057, identity, first launch, new company, store publication, `thaw`, and for anything Lang parks.

Branch protection stays as it is (1 approval, dismiss stale, last-push approval, `foundation` required, admins enforced). The Cindy App is the approver; the founder is not removed from anything.

## C. Deploy register (§8, §13.5) — first rows

| Unit | Deploy command | Runs as | Trigger | Rollback |
|---|---|---|---|---|
| `corporate-os-ui.service` | `scripts/deploy_main_to_oryx.sh` | root via a fixed sudoers rule for the Owen step (`corporate-os ALL=(root) NOPASSWD: /opt/unilogistix/corporate-os/scripts/deploy_main_to_oryx.sh`) | after a mandate merge (B) | re-run the script pinned to the previous `.deployed-origin-main-sha` |
| `corporate-os-lang.service` | same script (restarts both units) | same | same | same |

Owen deploys only after B is satisfied and only what B merged. Deploy evidence: the script output line and the post-deploy `systemctl is-active` of both units, appended to the task's audit.

## D. Duration and revocation

Valid 30 days from signature (expires 2026-10-22), renewable by a new signature. Revocable at any time by the founder (`freeze` per §9 stops new merges immediately; a signed revoke, as in D-007, removes the mandate). Every mandate merge is an audit event with the envelope's approval_id.

## E. What Codex builds (one PR, reviewed as usual, founder-approved because it touches reserved paths)

1. Seat credential reads from OpenBao at invoke time; per-seat `$HOME`; uuid5 session ids; CLIs installed system-wide; Owen over HTTP. (Closes PR #76's items.)
2. `mandate_merge()` in the executor: checks B.1–B.7 against GitHub and the ledger, then merges as the Cody App; audit event with approval_id.
3. Cindy review posting: the Cindy seat's verdict posted as a GitHub review by the Cindy App on the exact SHA.
4. Owen deploy step per C, with the sudoers rule shipped in `infrastructure/`.
5. Consumes the signed envelope from `~/board-approvals/` the way D-007's override is consumed; refuses when expired or revoked.

## F. Founder's steps today

1. Create the Cindy GitHub App (name, permissions above, install on this repo only); download its PEM.
2. Write the four credentials into OpenBao (Maestro gives the exact `bao kv put -cas=0` commands; values never shown).
3. Sign: `cd ~/board-sign/d008 && ./sign.sh` — then `./deliver.sh` to oryx.
4. Approve Codex's PR from E (it touches reserved paths — the last per-PR approval for this repo).
