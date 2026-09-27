# D-012 — Lang self-recovery: automatic restarts, and Judy's limited recovery rulings

Status: DRAFT for Board signature. Prepared by Maestro (Gram) on 2026-09-27 from founder direction
("should we give judy the judge power to inspect/restart lang if the watchdog alert is received?", then
"lets try it" on Maestro's proposal). Takes effect when the founder signs the action envelope in
`~/board-sign/d012/`. It amends D-010 only where section C says so; D-008, D-010 (otherwise) and D-011
stay in force.

## A. Why

On 2026-09-26/27 every Lang stop needed the founder, even when the answer was obvious:

- SH-21 and SH-27 parked `seat_unavailable` after a one-off seat failure. The seats were healthy again
  within minutes; the founder had to resume each task.
- SH-30 parked `cody_blocked_prerequisite_missing` twice. Both times the answer was a scope clarification
  inside the plan (build the gates; take the four signals as caller-supplied evidence). Lang sat idle
  from 00:40 until the founder woke.

The stuck-task watchdog (PR #232) now detects these within minutes. D-012 lets them be resolved without
the founder when the fix is mechanical or a narrow judgement inside the plan, and keeps every decision
that changes budget, plan, guardrails, money or law with the founder.

## B. Scope

Repository `turkyildiz/unilogistix-corporate-os` and the Lang runtime on oryx. Nothing else.

## C. What changes

### C.1 Mechanical recovery — automatic, no AI

When the heartbeat watchdog finds one of these, Lang fixes it by fixed code and reports it:

1. `corporate-os-lang.service` inactive → start it (at most 3 times per hour; after that, page the Board).
2. A seat claim older than `STALE_CLAIM_SECONDS` with no matching collect → release it through the
   existing F-108 path (no change in behaviour, only no longer waiting for the next dispatcher pass).
3. A task parked `seat_unavailable` whose seat passes a health probe → retry once at the same budget.
   A second `seat_unavailable` on the same task stays parked for the Board.

### C.2 Judy's recovery rulings

When the watchdog pages a parked build task (IT lane) or a frozen backlog caused by one, Judy inspects
the task (its requirement, the plan item, the blocker text, the diff so far, the review history) and
returns exactly one ruling:

- **RESUME** — send the task back to Cody **at its current exchange budget** (0 extra), with a
  clarifying instruction of at most 500 characters that stays inside the plan item's own wording; and,
  when the backlog is frozen only because of this task, thaw that backlog.
- **HOLD** — leave it parked for the founder, with her reasoning.

This amends D-010 for this case only: a RESUME ruling by Judy counts as an authorised resume and thaw
under the limits below. Every other resume and thaw stays the founder's.

### C.3 Limits on Judy (hard, enforced in code)

Judy may never:

- raise any exchange budget, or resume a task that has spent its budget;
- make more than **2** rulings per task (the third stop is the founder's);
- thaw a backlog frozen for any reason other than the task she resumed;
- change a plan, a backlog file, a guardrail, a Board decision, or anything reserved by D-010 or
  section D of D-011 (contracts, OpenBao policy, spend, identity, first launch, new company, store
  publication, money, legal);
- merge anything, or skip a reviewer: Cindy, Garry, CI and the D-008 mandate still decide every merge;
- act on a governance-lane or business-lane task, a Sherlock finding, or a watchdog alert about Lang's
  own units (those are C.1 or the founder's).

Her instruction text passes the secret scanner; one that fails is refused and the task stays parked.

## D. Visibility and veto

Every C.1 action and every Judy ruling is written to the ledger (`lang.recovery_*` / `lang.judy_ruling`)
and paged to the founder through the watchdog channel within one minute, with the task, the blocker, the
ruling and her instruction. The founder can undo a RESUME at any time by freezing the backlog; "revoke
D-012" stops C.1 and C.2 at once. Sherlock's register reviews sample Judy's rulings.

## E. Duration and revocation

Valid 30 days from signature, renewable by a new signature. Revocable at any time: the founder says
"revoke D-012" (Maestro disables it at once and records it), or signs a revocation. The runtime checks for
an active signed D-012 envelope before any C.1 or C.2 action and does nothing without one.

## F. How it is built

Once signed, Maestro builds it as a founder release (it touches resume/thaw authority, so D-011 does not
apply): Garry review, tests for every limit in C.3, a switch that turns C.1 and C.2 off independently.
Until that release is deployed, nothing in this decision is active.

## G. Founder's steps

1. Read this document.
2. Sign: `cd ~/board-sign/d012 && ./sign.sh` (Board key; passphrase in your terminal only).
3. Tell Maestro "d012 signed". Maestro records it in the Board register and builds the release.
