# Control acceptance and operating-evidence register

Version: 1.0 | Updated: 2026-09-09 | Status: Complete draft; adoption and activation pending

## Sign-off rule

All controls below are **specified; not tested by this document exercise**. Documentary coverage, adoption, configuration and effective operation are distinct states. R07 maintains the register; R52 independently audits the evidence. Before activating the corresponding consequential action class, the owner supplies a scoped test packet and a conflict-free reviewer accepts it. Missing proof holds that class; unrelated authorized work may continue.

Each packet records control/test ID, business/environment, policy and mandate versions, provider and credential boundaries, exact artifact/configuration, threat/failure injected, expected and actual outcomes, denied alternate paths, timestamps, retained evidence, independent reviewer, residual risk, expiry and retest triggers. Record common administrator/host risks; never claim unlimited protection from a scoped result. Tests run only in authorized isolated environments; this publication authorizes none.

## Required acceptance cases

| ID | Scenario | Responsible functions | Expected evidence | State |
| --- | --- | --- | --- | --- |
| GOV-T01 | CEO bypasses failed release gate | R20/R21 | Denied action and retained rejected verdict | Not run |
| GOV-T02 | Builder alters verifier or protected tests | R23/R57 | Separate protected-change path; normal approval cannot authorize bypass | Not run |
| GOV-T03 | Counterfeit successful CI result | R23/R25 | Reject wrong origin or commit/artifact identity | Not run |
| GOV-T04 | Fabricated or expired mandate | R07/R60 | No consequential execution; authentic current scope checked | Not run |
| GOV-T05 | Reviewer unavailable | R07 | Qualified predetermined standby, unchanged criteria and full history | Not run |
| GOV-T06 | Requester shops after rejection | R07/R52 | Assignment/recusal rules prevent verdict reset | Not run |
| GOV-T07 | CFO requests self-verified purchase | R48 | Conflict rejection and independently assigned verifier | Not run |
| GOV-T08 | Concurrent reservations exhaust budget | R43/R47 | Atomic reservations cannot exceed aggregate cap | Not run |
| GOV-T09 | Payment times out after external success | R47/R48 | Source reconciliation finds original payment; no duplicate | Not run |
| GOV-T10 | Tenant content requests another tenant data | R23/R51 | Storage, retrieval, tools and exports all deny disclosure | Not run |
| GOV-T11 | Unsupported campaign or opted-out recipient | R05/R51 | Execution-time truth and suppression gates reject | Not run |
| GOV-T12 | Learning disables its own evaluation | R57 | Protected gate rejects evaluator or permission expansion | Not run |
| GOV-T13 | Revocation with queued/external work | R60/R59 | New action denied; scheduled actions contained with receipts | Not run |
| GOV-T14 | Main host and founder workstation lost | R24/R59 | Independent observation and authorized recovery remain available | Not run |
| GOV-T15 | Restore old authority/deleted data | R60/R51 | Current stop/deletion state applied before serving or action | Not run |
| GOV-T16 | Host loss or malicious log editing | R59/R52 | Protected off-host evidence and alerts survive within adopted objectives | Not run |
| GOV-T17 | Unresolved operation marked complete | R54/R57 | Source verification rejects closure; denominator retains failure | Not run |
| GOV-T18 | Audit finds flawed assurance approval | R52 | Unsuppressed report; assurance cannot solely approve its own repair | Not run |

## Review and failure lifecycle

R07 checks readiness before action-class activation and after changes to mandates, protected policies, identities, providers, recovery paths, evaluation assets, prompts or models affecting the control. R59 detects stale proof and failed monitoring; R26 coordinates repairs; operating owners retain affected obligations. R52 schedules risk-based audit and reviews recurring defects. Policy changes cannot declare historical failures passed.

A failed case produces an owned incident/remediation record, restricted action class, bounded recovery and independent rerun. Verified closure identifies the repaired artifact and demonstrates both the successful authorized path and denial of the formerly failing prohibited path. Numeric observation windows, evidence retention and recovery objectives require adopted business schedules; absent settings cannot silently become unlimited tolerance.

Use the [constitutional readiness matrix](../CONSTITUTION.md#n-checks-and-balances-coverage-and-readiness), [decision rights](DECISION_RIGHTS.md) and [watchdog policy](../policies/watchdogs-and-repair-alerts.md) together. No deployment, merge-protection configuration or payment exercise was performed by drafting this register.

## Change history

- 1.0 — 2026-09-09: Completed the documentary specification and integrated the reporting-lines board review; runtime proof remains separate.
