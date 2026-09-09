# Reporting review disposition

Version: 1.0 | Updated: 2026-09-09 | Status: Complete draft; adoption and activation pending

## Source and baseline

The founder supplied [the reporting-lines board review](../reference/Unilogistix_Reporting_Lines_Checks_and_Balances_Board_Review.md). Its source is preserved unchanged. It inspected an earlier GitHub baseline, a23534e1ffa280adb94221b4c5353f8819a92dc6. The later document checkpoint edf006c17486cfcaf4e83c067d363a70d29f6f3d already added all-role reporting and watchdog rules. Historical observations about protection settings, workflow counts and infrastructure are attributed to that review; this document does not pretend they were freshly retested.

## Disposition of all eight gaps

| Gap | Draft resolution | Canonical home |
| --- | --- | --- |
| GOV-01 Reviewer independence | Protected pool, credentials, tests, capacity, verdict history and conflict-aware standby selection | [Decision rights](DECISION_RIGHTS.md#reviewer-appointment-and-replacement) |
| GOV-02 Audit versus assurance | R07 coordinates pre-action assurance; R52 audits both assurance and operators through protected founder reporting | [Constitution](../CONSTITUTION.md#m-reporting-lines-and-independent-oversight) and decision rights |
| GOV-03 Ordinary disputes | One appeal and independent adjudication, bounded defaults, restrictive timeout, preserved history; no routine founder help desk | [Decision rights](DECISION_RIGHTS.md#bounded-ordinary-dispute-resolution) |
| GOV-04 Trusted engineering gates | Trusted-origin/exact-artifact validation and separately protected control changes; future runtime acceptance cases | [Control register](CONTROL_REGISTER.md) |
| GOV-05 Finance conflicts | CFO protected integrity access plus action-level recusal, independent destination check, separate payment/reconciliation | [Decision rights](DECISION_RIGHTS.md#action-ownership) |
| GOV-06 External enforcement | Scoped provider rights or exclusive narrow broker custody; common-root risk disclosed | Decision rights and control register |
| GOV-07 Independent recovery | Observation/recovery independent of founder workstation; current stop/deletion state reapplied after restore | Decision rights and watchdog policy |
| GOV-08 Independent evidence | Off-host protected evidence, delivery-confirmed alerts, independently checked repair closure | Watchdog policy and control register |

The proposed “assurance/risk lead” function maps to existing R07; it does not add a 61st role. R22 remains assigned to independent QA R21 for verification tooling. Builders still write developer tests, and cannot grade their own material acceptance. Operating managers own repairs while independent reviewers own verdicts. The 60 role contracts remain canonical.

## Board proposals and adoption

BD-GOV-01 through BD-GOV-08 are included in the draft charter/control requirements for review: operating reporting, protected oversight, CFO integrity access, reviewer protection, bounded disputes, mandate/stop scope, engineering enforcement and scope-specific control sign-off. **All eight remain unadopted proposals.** Supplying a review and authorizing document publication do not constitute adoption, runtime authority or a budget.

The [adoption packet](ADOPTION_PACKET.md) identifies the completed manuscript and the exact remaining decisions. No alternative chart in the source silently overrides the constitution. All 18 source acceptance cases are retained as explicit unrun requirements in the control register.

## Change history

- 1.0 — 2026-09-09: Completed the documentary specification and integrated the reporting-lines board review; runtime proof remains separate.
