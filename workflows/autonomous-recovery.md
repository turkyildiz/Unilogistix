# Autonomous recovery workflow

Version: 0.7 | Updated: 2026-09-09 | Status: Draft specification

Trigger: a blocked or failed operation, including tool failure, missing context, reviewer rejection, or uncertain external result.

Owner: the task owner; COO owns recurring operational defects.

Failures detected by [independent watchdogs](../policies/watchdogs-and-repair-alerts.md)
become durable incident/repair work with severity, accepted AI ownership, delivery
and progress deadlines. R26 coordinates incidents; R59 independently checks recovery.
Missed acknowledgment or progress escalates through operational fallback channels.
Repair does not wait for founder acknowledgment when already authorized.

Diagnose → reconcile state → bounded retry → permitted repair → approved alternate → scope-preserving redesign → rollback/queue/safe state. Follow [the autonomy policy](../policies/autonomy.md).

After each attempt record the hypothesis, evidence, cost, result, and next scheduled step. Do not loop indefinitely. Resolve a blocker when new evidence supports a useful action; elapsed time alone does not authorize anything.

If an unavoidable human ask occurs, record it immediately as a failure and produce a reusable remediation artifact. Complete independent work while the affected action remains blocked.

Acceptance: the formerly failing scenario completes without human help; uncertain external effects are not duplicated; permission-denial cases remain denied. Repeated defects create prioritized improvement work.

## Change history

- 0.7 — 2026-09-09: Specified independent failure detection, urgent repeat/fallback alerts and verified repair; operating thresholds and channel activation remain proposed.

- 0.2 — 2026-09-09: Added to the blueprint-aligned foundation.
