# D-010 — Standing merge mandate, renewed: per-task exchange budget

Status: DRAFT for Board signature. Prepared by Maestro (Gram) on 2026-09-23 from founder direction ("this plan makes more sense lets do set per task", after FC11a merged at exchange 4 of 4 with two exchanges spent on formatting). Takes effect when the founder signs the action envelope in `~/board-sign/d010/` and the runtime consumes it; the D-008 mandate is revoked in the same release.

Scope: `turkyildiz/unilogistix-corporate-os` only, as D-008. D-008 sections A (seat identities), C (deploy register) and E/F (history) are unchanged and remain in force. This document replaces D-008 section B (the merge conditions) and section D (duration) as one signed packet.

## B. Standing merge mandate

A pull request to `main` of `unilogistix-corporate-os` merges **without founder action** when all of the following are true, verified by the runtime before it calls merge:

1. Author is the Cody App. Head is on a branch Lang created for a task with a `task_id` in the ledger.
2. Cindy approval: a review with state APPROVED posted by the Cindy App, on the exact head SHA, with the first line `VERDICT: ACCEPT` and the task_id.
3. Garry security verdict on the exact head SHA with no CHANGES_REQUIRED.
4. `foundation` check green on the head; head up to date with `main`.
5. The diff touches none of the reserved paths (unchanged from D-008 B.5). A diff touching any of them parks the task to the Board (`hold_board`).
6. **Exchange budget honoured: `exchange_count ≤ exchange_budget` on the task, and `exchange_budget ≤ 8`.**
   - The budget is fixed **once, when the task enters the ledger**: set by Maestro when forwarding a Board item (`maestro_inbox forward --exchange-budget N`), or by the founder. Default 4 (the Rule of Four). Allowed values 4 to 8.
   - No seat can set or change it. It is stored on the intake record; the merge gate reads it from there, not from the task state the runtime writes.
   - At the budget, the task parks for Judy instead (as at 4 under D-008).
   - Raising the ceiling of 8 needs a new Board signature.
   - Maestro uses more than 4 only for large multi-file work (for example a Forest Shield build task), and records the budget in the task text.
7. Merge method: merge commit. Merge commit body cites task_id, Cindy review id, Garry verdict id.

The founder keeps approval for everything in 5, for contract edits (F-060 §9), OpenBao policy, spend beyond F-057, identity, first launch, new company, store publication, `thaw`, and for anything Lang parks.

## D. Duration and revocation

Valid 30 days from signature, renewable by a new signature. Revocable at any time by the founder (`freeze` per §9 stops new merges immediately; a signed revoke removes the mandate). Every mandate merge is an audit event with the envelope's approval_id. On activation of this mandate the D-008 mandate is revoked (reason: "superseded by D-010").

## E. What changes in code (Maestro's PR, Garry review, founder release — touches reserved paths)

1. `lang_intake_queue.exchange_budget` (nullable integer; null means 4). Validated 4..8 on insert; `forward_maestro` and `maestro_inbox forward --exchange-budget` set it.
2. The dispatcher copies it into the task's first state; the runtime uses it in place of the literal 4 (the Rule-of-Four park and the three rework checks).
3. `mandate_merge` refuses unless `exchange_count ≤` the intake record's budget `≤ 8`, and the task state's budget equals the intake record's.
4. `d008.py`: merge condition `exchange_count_le_task_budget_max_8`; packet digest = SHA-256 of this file.

## F. Founder's steps

1. Sign: `cd ~/board-sign/d010 && ./sign.sh` (Board key, passphrase in your terminal only).
2. Run the founder-steps script Maestro provides: it merges the code PR (after Garry CLEAR), releases and deploys it, installs and activates this mandate, and revokes D-008, in that order.
