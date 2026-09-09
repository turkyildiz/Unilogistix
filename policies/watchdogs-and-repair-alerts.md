# Independent watchdogs, urgent alerts and verified repair

Version: 0.1 | Updated: 2026-09-09 | Status: Proposed operating rule; no alert channels or watchdogs activated

## Purpose and ownership

Failures must become visible, owned repair work and remain visible until independently
verified recovery. R59 owns independent detection and alert follow-through; R26 owns
incident command and repair coordination. R02 owns affected business obligations.
R07 protects watchdog independence and R52 audits suppression, missed alerts and
unsupported closure. These are functions within the existing role library, not a
requirement for new permanent agents.

Use this policy for each actual business instance and the framework services on
which it depends. A healthy Unilogistix framework does not prove LondonRue checkout
works; each requires its own observable outcomes. All numeric values below are
proposed operating defaults for review, not current service guarantees or legal
deadlines. Business-specific safety and time-critical requirements take precedence.

## Required detection coverage

| Watch | Required signal | Repair/assessment owner |
| --- | --- | --- |
| Customer journeys | Broken checkout, unavailable service, failed order/fulfillment handoff, unexpected error rate | R26 with R03/R37/R35 |
| Tasks and agents | Missing heartbeats, expired leases, overdue work, stuck/repeated attempts, ownerless obligations | R01/R02/R08 |
| Finance | Suspected duplicate/unauthorized payments, uncertain settlements, unexplained differences, approaching limits | R48/R04, with R26 for incidents |
| Security and authority | Unexpected access, expired/revoked identity, denied-control anomalies, attempted protection changes | R23/R60/R07 |
| Infrastructure and maintenance | Capacity, expired certificates/credentials, missed jobs, failed backups and overdue restore exercises | R24/R26 |
| Business health | Inventory mismatch, delivery failures, support overload, refund/complaint surge, acquisition into broken service | R02/R06/R27 |
| Evidence and learning | Stale eligibility, missing acceptance evidence, repeated defects and unowned remediation | R57/R53 |
| Watchdog and alert delivery | Missing monitoring heartbeat, failed synthetic alert, unreachable primary channel or stale dashboard | Independent R59 observer, R07 and R26 |

Checks must measure absence as well as explicit errors. Proposed baseline for
critical continuously running services: heartbeat every 60 seconds, suspected
missing-service incident after two missed heartbeats, with separate corroborating
signals where available. This is a detection design target, not proof of uptime.
Physical safety controls must act independently at the required device timescale;
they cannot depend on this alert interval or an AI response.

## Severity and loudness

| Severity | Typical impact | AI-owner acknowledgment target | Repeat before acknowledgment | Required progress update |
| --- | --- | --- | --- | --- |
| SEV-0 Critical | Active material security/financial harm, physical danger or widespread destructive failure | 2 minutes | Every 2 minutes | Every 5 minutes |
| SEV-1 Major | Checkout/core service unavailable, many customer obligations at risk, critical control or recovery path unavailable | 5 minutes | Every 5 minutes | Every 15 minutes |
| SEV-2 Significant | Partial failure, repeated job/fulfillment errors or a recoverable control gap without current critical harm | 30 minutes | Every 30 minutes | Every 60 minutes while active |
| SEV-3 Routine | Low-impact defect, maintenance finding or improvement with no urgent obligation at risk | 1 business day | At missed assignment deadline | Each business day or the recorded earlier due date |

Classification uses actual impact and uncertainty. It cannot be downgraded merely
to avoid notifications or meet a metric. Severe known harm triggers authorized
containment immediately; acknowledgment is not a prerequisite. Record severity
changes and the supporting evidence.

“Loud” means a persistent severity banner, an actively routed incident alert,
deadline-based repeats and a working fallback—not only a log entry. Each alert
contains incident/business ID, severity, first/last observed times, customer/money/data
impact, concise evidence, assigned owner, authority limits, action required and the
next response deadline. Sensitive details stay behind scoped access; notifications
must not expose credentials or raw customer/financial records.

## Delivery, acknowledgment and escalation

1. Create a durable incident and repair task, then send to the assigned AI incident/operations destination through configured channels.
2. Record delivery attempts and receipts separately from acknowledgment. A provider accepting a notification does not prove the repair owner accepted the task.
3. Acknowledgment requires a qualified authorized owner to accept incident responsibility, name the next action and give the next update time. Reading the alert or posting “investigating” without ownership is insufficient.
4. For SEV-0/SEV-1, use an independently hosted fallback destination if primary delivery fails or acknowledgment misses its target. Alert R07 and the relevant executive at the same escalation point; R26 remains responsible unless a qualified replacement explicitly accepts.
5. Continue timer-based repeats to the operational response path until accepted. After acceptance, require progress updates; a missed update escalates immediately. Two update intervals without verifiable progress trigger an independent recovery assessment and alternate qualified assignment where authorized.
6. Failed notification delivery is itself an owned monitoring incident. Retain the original incident, attempt the permitted fallback and reconcile queued alerts when connectivity returns.

Channel profiles must name the primary incident system, an independent secondary
route and authenticated owner mappings before critical operation. SMS, push, email
or voice are optional delivery mechanisms chosen within actual account authority
and cost limits; this document configures none of them. If every channel fails,
no delivery can be claimed. The independent observer must still be able to detect
missing service/monitor signals through its own permitted route, or the business
must disclose that monitoring dependency as unready.

## Founder visibility without making the founder the repair operator

SEV-0/SEV-1 receive a prompt founder/governance visibility notice through the adopted
channel, with impact, AI owner and next update. Repeated paging targets AI repair
owners and fallback operations; founder updates follow the agreed severity cadence
and material changes, rather than a separate notification for every duplicate alert.

Normal repair continues under standing authority without waiting for the founder
to read, acknowledge or fix it. A genuinely reserved decision receives a separate
exact-scope decision packet. If human operational repair is unavoidable, record it
as an autonomy failure; do not hide the dependency behind an informational notice.

## Noise, maintenance and suppression

Group duplicate symptoms under a root incident while preserving affected customers,
cases and deadlines. Rate-limit duplicates, not material impact or escalation.
An outage affecting several businesses keeps each business's obligations visible
without disclosing their private data to each other.

Maintenance windows need recorded scope, owner, authority, start/end, expected
effects and expiration of suppression. They do not suppress unrelated failures or
erase incidents. Unexpected impact breaks the maintenance assumption and alerts.
Workers under investigation cannot mute their own watchdog, delete evidence,
silence a rejecting verifier or extend suppression indefinitely. Changes to alert
rules and routes require appropriate independent review and versioning.

## Repair and closure

Use `detected → routed → acknowledged → contained/repairing → verification → closed`,
with failed delivery, blocked repair and reopened states visible. Preserve one
accountable owner throughout. A containment action may reduce harm without resolving
the incident; externally running campaigns/payments need provider-state verification.

The repair owner records diagnosis, actual action, version/configuration, resource
use, result and remaining obligations. R59 and relevant independent specialists
verify the formerly failing customer/control path, observe stability for the
business-defined window and reconcile uncertain external effects. The repairer
cannot certify its own consequential recovery.

Close only when the affected outcome is verified and any remaining customer,
financial or preventive work has an accepted owner and deadline. Restoration and
permanent root-cause remediation may be separate linked records; neither may be
falsely labeled complete. Recurrence reopens or links the incident and feeds R53/R55
learning, with a regression case for the next Unilogistix version where reusable.

## Who watches the watchdog

The primary watchdog must not share every failure dependency, permission boundary
or mutable configuration path with the service it watches. A second observer
checks its heartbeat and the freshness of customer-path observations. R07/R52
receive evidence when monitoring or alert delivery itself fails.

Proposed exercises: daily harmless synthetic alert through the automated incident
path; monthly end-to-end delivery/fallback/owner-acceptance exercise, also after
material channel changes. Exercise records are labeled tests, cannot invoke real
payments/customer messages and do not count as real incidents or customer operation.
No test needs to page the founder unless that route is explicitly included in an
authorized notification test. Business activation must set scope and resource
limits for these checks and address correlated failures rather than assuming
another process on the same failed host is independent.

## Documentary acceptance cases

- Stop a worker silently: detect missed activity and assign repair without trusting a self-reported failure.
- Break checkout while host health stays green: the customer-path check raises the incident.
- Drop the primary alert: the fallback route receives and acknowledges the same incident within its adopted target.
- Accept an alert but do no work: the progress timer escalates and records reassignment without abandoning ownership.
- Let the repairer claim success while the path still fails: independent verification rejects closure.
- Stop the primary watchdog: the independent observer detects stale monitoring.
- Attempt indefinite maintenance suppression: reject the unauthorized extension and preserve visibility.
- Recover after a payment succeeded: reconcile first and prevent a repeated effect.
- Flood duplicate alerts: preserve the incident, deadlines and critical escalations without flooding unrelated recipients.

These are specifications for later tests. Measure detection, delivery, acknowledgment,
repair and verification times separately, plus missed alerts, false positives,
reopened incidents and operational human interventions. No live watchdog, external
notification or repair exercise is claimed by this document.

## Change history

- 0.1 — 2026-09-09: Defined watchdog coverage, proposed urgent-alert timers, fallback, ownership, independent closure and monitoring-of-monitoring for review.
