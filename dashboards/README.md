# Dashboard and KPI contract

Version: 0.2 | Updated: 2026-09-09 | Status: Draft specification

Initial definitions below require source instrumentation and adopted windows. No live values are claimed.

| Metric | Formula / source | Decision |
| --- | --- | --- |
| Operational human asks | Count issued routine-operation requests for human action; action log | Every event opens autonomy remediation |
| Human ask rate | 100 × asks / eligible ordinary operations started in the window | Target zero; include failed and blocked operations |
| Human execution minutes | Sum recorded human work time for ordinary operations | Target zero; remove recurring manual dependencies |
| Autonomous verified completion | Tasks accepted without human asks or execution / eligible tasks in cohort | Improve success, not just suppress asks |
| Blocked operations | Count blocked tasks by age and root cause | Repair capability gaps |
| Customer retention | Retained eligible customers / starting eligible customer cohort | Reassess customer value |
| Contribution | Revenue minus defined attributable delivery and operating costs | Evaluate viability with cash and obligations |
| Cash available | Reconciled cash minus reserved commitments and required reserve | Limit new commitments |
| Service availability | Successful eligible service events / eligible service events | Trigger incident or reliability work |
| AI cost per accepted outcome | Attributed model/tool costs / accepted outcomes | Improve routing and quality |
| Support resolution time | Resolution timestamp minus creation, by severity and percentile | Address backlog and service failures |

Owner and source mappings: COO for task/support/availability; CFO for financial ledgers; CTO for model and engineering events; product owner for customer cohorts. Review daily internally and weekly with the portfolio by default.

Each product mandate supplies windows, freshness, targets, exclusions, and incident thresholds. Missing data or zero denominators must display unavailable. Show stale timestamps and unfinished cohorts. Never improve autonomy metrics by dropping failed work or disguising operational asks as strategy.

## Change history

- 0.2 — 2026-09-09: Added to the blueprint-aligned foundation.
