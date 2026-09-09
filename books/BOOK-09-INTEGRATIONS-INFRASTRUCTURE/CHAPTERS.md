# Integrations & Infrastructure — Complete Chapter Manual

Version: 1.0 | Updated: 2026-09-09 | Status: Complete draft manuscript; adoption and operational activation pending

## Reading and authority

This manual supplies substantive procedures for every chapter in the selected blueprint. The [constitution](../../CONSTITUTION.md) is canonical for all 60 roles, reporting, authority and protected oversight. “Company” means the relevant actual business; Unilogistix itself is the reusable framework. LondonRue towels is an example, not an inferred formation or launch.

Each chapter names its owner and trigger, required procedure, and acceptance/failure evidence. All work inherits the constitutional mandate, independent review, privacy, bounded recovery and truthful outcome requirements. Numeric limits and real account/entity identities belong to the [business profile](../../templates/business-instance.md); missing required authority restricts the affected action. Documentary completeness does not claim adopted rules or implemented controls. Every operational human ask is a failure and must be recorded without concealing unresolved work.

Follow [operating assurance](../../policies/operating-assurance.md), [watchdog escalation](../../policies/watchdogs-and-repair-alerts.md), [decision rights](../../governance/DECISION_RIGHTS.md) and [business-to-framework learning](../../workflows/business-to-framework-learning.md) where applicable. A real legal/provider requirement is verified for its exact business, action and current source before use; no illustrative company cadence is a statutory deadline.

## Chapter directory

- [Chapter 01: Infrastructure Vision](#chapter-01)
- [Chapter 02: Reference Architecture](#chapter-02)
- [Chapter 03: Cloud Strategy](#chapter-03)
- [Chapter 04: Environments](#chapter-04)
- [Chapter 05: Networking](#chapter-05)
- [Chapter 06: Source Control](#chapter-06)
- [Chapter 07: GitHub](#chapter-07)
- [Chapter 08: CI/CD](#chapter-08)
- [Chapter 09: AI Platform](#chapter-09)
- [Chapter 10: Model Registry](#chapter-10)
- [Chapter 11: Orchestrator Runtime](#chapter-11)
- [Chapter 12: Tool Registry](#chapter-12)
- [Chapter 13: Prompt Management](#chapter-13)
- [Chapter 14: Memory Services](#chapter-14)
- [Chapter 15: CRM](#chapter-15)
- [Chapter 16: Accounting](#chapter-16)
- [Chapter 17: Billing](#chapter-17)
- [Chapter 18: Identity / Access](#chapter-18)
- [Chapter 19: Email](#chapter-19)
- [Chapter 20: Calendar](#chapter-20)
- [Chapter 21: Notifications](#chapter-21)
- [Chapter 22: Document Management](#chapter-22)
- [Chapter 23: API Gateway](#chapter-23)
- [Chapter 24: Authentication](#chapter-24)
- [Chapter 25: Databases](#chapter-25)
- [Chapter 26: Object Storage](#chapter-26)
- [Chapter 27: Search](#chapter-27)
- [Chapter 28: Event Bus](#chapter-28)
- [Chapter 29: Messaging](#chapter-29)
- [Chapter 30: Monitoring](#chapter-30)
- [Chapter 31: Logging](#chapter-31)
- [Chapter 32: Secrets](#chapter-32)
- [Chapter 33: Security](#chapter-33)
- [Chapter 34: Backups](#chapter-34)
- [Chapter 35: Disaster Recovery](#chapter-35)
- [Chapter 36: Infrastructure as Code](#chapter-36)
- [Chapter 37: Deployment Strategies](#chapter-37)
- [Chapter 38: Scaling](#chapter-38)
- [Chapter 39: Vendor Management](#chapter-39)
- [Chapter 40: Multi-Product Infrastructure](#chapter-40)
- [Chapter 41: Future Expansion](#chapter-41)

<a id="chapter-01"></a>

## 01. Infrastructure Vision

**Owner and trigger:** R24/R14 on infrastructure planning.

**Rules and procedure:** Support reliable business outcomes with replaceable, scoped services and explicit costs. Use suitable existing resources first, but verify capacity, commitments and failure domains. Unilogistix is the framework; infrastructure sharing does not merge business authority.

**Acceptance and failure:** A placement plan identifies purpose, owner, cost and recovery. Unverified spare capacity or a configured connector alone cannot establish readiness.

<a id="chapter-02"></a>

## 02. Reference Architecture

**Owner and trigger:** R14/R03 when defining service boundaries.

**Rules and procedure:** Map governance, workers, protected verification, action gateway, business state and independent evidence/monitoring. Identify direct provider paths and common administration risks. Keep the smallest architecture that meets actual isolation and recovery requirements.

**Acceptance and failure:** Trace permitted and denied actions end-to-end. A privileged alternate route or ownerless dependency remains an activation blocker.

<a id="chapter-03"></a>

## 03. Cloud Strategy

**Owner and trigger:** R24/R43 on workload placement.

**Rules and procedure:** Compare existing providers and on-prem resources by total cost, data needs, operating fit and recovery. Record assumptions and exit options. Do not provision new paid services or parallel redundancy without the appropriate authority.

**Acceptance and failure:** The decision includes capacity evidence and recurring exposure. A provider listed in the stack is not proof of an available budget or quota.

<a id="chapter-04"></a>

## 04. Environments

**Owner and trigger:** R24/R60 when creating development, test or production scope.

**Rules and procedure:** Separate identities, secrets, data and release permissions; use synthetic or explicitly permitted test data. Keep untrusted builds away from production credentials and private customer stores. Define safe teardown and evidence retention.

**Acceptance and failure:** Environment-boundary tests reject cross-access. Naming a directory staging does not establish isolation.

<a id="chapter-05"></a>

## 05. Networking

**Owner and trigger:** R24/R23 on connectivity and ingress/egress changes.

**Rules and procedure:** Document authenticated service paths, necessary ports/routes and external dependencies. Constrain worker egress where needed to prevent direct-provider bypass of narrow brokers. Preserve independent monitoring/recovery routes without distributing unrestricted administrator access.

**Acceptance and failure:** Connectivity and denied-route evidence matches the intended scope. Unknown exposure remains a tracked risk, not an implicit permission.

<a id="chapter-06"></a>

## 06. Source Control

**Owner and trigger:** R53/R25 on source changes.

**Rules and procedure:** Version code, policies, configuration and approved reusable assets; keep secrets/private data out. Preserve remote history and bind reviews to exact content. Distinguish source publication from operational deployment and control adoption.

**Acceptance and failure:** A commit readback verifies published content. Forced overwrite or missing dependencies is corrected before publication is reported complete.

<a id="chapter-07"></a>

## 07. GitHub

**Owner and trigger:** R25/R07 on GitHub publication and control sign-off.

**Rules and procedure:** Use actual repository permissions and reviewed machine identities. Define trusted required checks, bypass scope and protection of workflows that generate verdicts. Independently test behavior; a successful document push does not prove branch protection or a CI pipeline.

**Acceptance and failure:** Record exact branch/commit and permitted/denied operations. Historical access failures remain history rather than overriding newer verified writes.

<a id="chapter-08"></a>

## 08. CI/CD

**Owner and trigger:** R24/R25 on pipeline configuration.

**Rules and procedure:** Build exact accepted inputs, isolate untrusted work, protect verifier credentials and require applicable checks before promotion. Model-triggered work must run through supported authorization paths; remove manual dependency by proper design rather than disabling gates.

**Acceptance and failure:** A good/bad-change exercise includes forged status and protected-workflow modification. Configuration existence is not evidence of enforcement.

<a id="chapter-09"></a>

## 09. AI Platform

**Owner and trigger:** R19/R24 on inference service integration.

**Rules and procedure:** Record provider/model scope, privacy/data handling, rate/cost limits, availability and fallback. Separate model inference from action authority. Cache or batch only permitted data and charge retries to the original operation envelope.

**Acceptance and failure:** Representative quality/cost and outage evidence supports routing. A fallback cannot obtain additional tools or another business’s data.

<a id="chapter-10"></a>

## 10. Model Registry

**Owner and trigger:** R56/R57 on model adoption or update.

**Rules and procedure:** Register exact model/configuration, applicable roles/actions, evaluations, limitations, cost and expiry triggers. Distinguish proposed, qualified and active status. Protect qualification from the candidate and preserve prior adverse results.

**Acceptance and failure:** Promotion applies only to tested scope under existing authority. A changed identifier or provider behavior triggers appropriate reassessment.

<a id="chapter-11"></a>

## 11. Orchestrator Runtime

**Owner and trigger:** R01/R24 on durable worker deployment.

**Rules and procedure:** Persist task state, leases, deadlines, shared budgets and external action identities. Separate business uptime from conversational sessions. Specify recovery, fairness and concurrency; monitor missing activity independently.

**Acceptance and failure:** Restart and stale-worker exercises preserve ownership and do not duplicate effects. A bootstrap launcher is not automatically an unattended runtime.

<a id="chapter-12"></a>

## 12. Tool Registry

**Owner and trigger:** R60/R56 before exposing an integration.

**Rules and procedure:** Register purpose, allowed actions/resources, identity, data, spend/rate limits, evidence and revocation. Prefer narrow business actions over unrestricted shell/SQL/payment access. Verify provider semantics and the actual granted scope.

**Acceptance and failure:** A tool list entry without authenticated behavior remains unverified. Denial and bypass tests are required for consequential eligibility.

<a id="chapter-13"></a>

## 13. Prompt Management

**Owner and trigger:** R56/R53 on prompt configuration.

**Rules and procedure:** Version role instructions, tool contracts, evaluation bindings and governing references. Protect authority and evaluator instructions from retrieved/user content. Keep secrets out and requalify affected actions after material changes.

**Acceptance and failure:** A prompt diff has scoped review and evaluation. Increased confidence or persuasive text cannot justify additional permission.

<a id="chapter-14"></a>

## 14. Memory Services

**Owner and trigger:** R18/R53 on memory-service integration.

**Rules and procedure:** Define authoritative versus derived records, access filtering, freshness, retention and restore behavior. Keep business-private memory isolated and support permitted framework learning through explicit generalization.

**Acceptance and failure:** Cross-business and stale-policy retrieval tests fail safely. A shared database endpoint does not authorize shared records.

<a id="chapter-15"></a>

## 15. CRM

**Owner and trigger:** R33/R18 when connecting CRM.

**Rules and procedure:** Maintain canonical identity and linked commercial/service/financial dimensions with versioned updates. Propagate contact preferences and verified corrections. Restrict bulk export and cross-business access.

**Acceptance and failure:** Duplicate identity, cancellation and preference races preserve correct permitted state. Inconsistent departmental copies trigger owned reconciliation.

<a id="chapter-16"></a>

## 16. Accounting

**Owner and trigger:** R44/R18 on accounting integration.

**Rules and procedure:** Define ledger/subledger ownership, adopted accounting method, immutable source references and reviewed adjustments. Reconcile provider statements independently and keep private financial records outside public artifacts.

**Acceptance and failure:** A representative posting and correction traces to evidence. A successful API write does not establish a correct financial close.

<a id="chapter-17"></a>

## 17. Billing

**Owner and trigger:** R46/R47/R48 on payment and billing integration.

**Rules and procedure:** Separate invoice/entitlement state, execution and reconciliation. Bind exact amount, counterparty, authority and idempotency; handle delayed, duplicated and uncertain provider results. Preserve cancellations, refunds and remaining obligations.

**Acceptance and failure:** Payment-after-timeout scenarios yield one effect and correct balance. Broad payment credentials must not be reachable from ordinary workers.

<a id="chapter-18"></a>

## 18. Identity / Access

**Owner and trigger:** R60/R07 on role access.

**Rules and procedure:** Issue least-privilege, business/action-scoped identities only from authentic mandates and qualification. Record expiry, renewal, revocation and independent review for privileged changes. Protect administrator/recovery paths from ordinary agent control.

**Acceptance and failure:** Expired, forged and over-scope requests fail. No role title or successful login creates a mandate.

<a id="chapter-19"></a>

## 19. Email

**Owner and trigger:** R31/R24 on sending services.

**Rules and procedure:** Configure supported sender identity, purpose eligibility, suppression, delivery receipts and failure handling. Recheck queued recipients against current preferences. Verify current provider and applicable communication requirements before activation.

**Acceptance and failure:** An opt-out before send prevents promotion; an accepted provider request is distinguished from delivered/customer-read status.

<a id="chapter-20"></a>

## 20. Calendar

**Owner and trigger:** R08/R02 on recurring obligations.

**Rules and procedure:** Store owner, due rule, timezone, dependencies, scope, authority and escalation for renewals, reviews and maintenance. Preserve missed events after downtime and distinguish legal deadlines from company cadences.

**Acceptance and failure:** A clock-change/downtime exercise recovers due work without duplicating consequential actions. Unowned entries prevent calendar readiness.

<a id="chapter-21"></a>

## 21. Notifications

**Owner and trigger:** R59/R26 on alerts and notices.

**Rules and procedure:** Use durable incidents with delivery receipts, AI acknowledgment, repeat timers and independent fallback. Separate founder visibility from requests for repair. Protect sensitive details and avoid duplicate-alert noise without suppressing real obligations.

**Acceptance and failure:** A failed primary route and missing owner escalate within adopted targets. No channel delivery may be claimed without evidence.

<a id="chapter-22"></a>

## 22. Document Management

**Owner and trigger:** R53 on document storage and publication.

**Rules and procedure:** Maintain canonical versions, classifications, access, review dates and source provenance. Preserve supplied proposals unchanged and link adapted current policy. Public files exclude secrets and customer records; locally referenced artifacts must be labeled accurately.

**Acceptance and failure:** Readers can find exact controlling and historical versions. Broken links or misleading implementation status are repaired before completion.

<a id="chapter-23"></a>

## 23. API Gateway

**Owner and trigger:** R60/R16 on action-gateway design.

**Rules and procedure:** Validate exact identity, business, resource, payload, qualification, mandate, current conditions and reserved budget outside model text. Constrain direct-provider alternatives and protect underlying credentials. Record denial and uncertain execution without fabricating success.

**Acceptance and failure:** A compromised test worker cannot bypass the gateway or extract broader authority. Residual privileged paths require explicit protection and scope disclosure.

<a id="chapter-24"></a>

## 24. Authentication

**Owner and trigger:** R60/R07 on customer, workload or governance authentication.

**Rules and procedure:** Distinguish proof of identity from authorization to act. Validate session/revocation state and protect recovery and sensitive identity changes. Governance decisions require their actual trusted origin, not an agent-written interpretation.

**Acceptance and failure:** Forged approvals, stale sessions and changed-recipient requests fail. Recovery does not silently reset an intentional board stop.

<a id="chapter-25"></a>

## 25. Databases

**Owner and trigger:** R18/R24 on database provision and change.

**Rules and procedure:** Specify integrity, backups, access, capacity, migration and source ownership. Scope transactions and version checks so concurrent departments preserve consistent customer commitments. Keep restore restrictions current.

**Acceptance and failure:** Duplicate/out-of-order events and schema migration reconcile correctly. Data corruption or cross-business access blocks acceptance despite service availability.

<a id="chapter-26"></a>

## 26. Object Storage

**Owner and trigger:** R24/R51 on object/evidence storage.

**Rules and procedure:** Classify objects, restrict writes/deletes, set retention and protect critical evidence across failure domains. Separate public assets, private customer content and audit records. Preserve provenance and access on export and restore.

**Acceptance and failure:** An executor cannot delete its own adverse retained evidence. Unauthorized object URLs or lost metadata fail storage readiness.

<a id="chapter-27"></a>

## 27. Search

**Owner and trigger:** R18/R53 on search integration.

**Rules and procedure:** Index only permitted data and enforce scope before retrieval, not solely after generation. Track source freshness and retirement into indexes/caches. Evaluate relevance alongside denied-access behavior.

**Acceptance and failure:** An inaccessible source cannot leak through snippets or cached results. Stale authority or deleted records trigger restriction/reindexing.

<a id="chapter-28"></a>

## 28. Event Bus

**Owner and trigger:** R18/R16 on event delivery.

**Rules and procedure:** Define authenticated envelope, schema, occurrence/receipt time, correlation, ordering and deduplication. Tie outbound events to durable business commits and handle replay. Do not assume external systems supply exactly-once effects.

**Acceptance and failure:** Commit/crash and duplicate-delivery exercises preserve events without repeating payment or order actions. Lost provenance blocks trusted ingestion.

<a id="chapter-29"></a>

## 29. Messaging

**Owner and trigger:** R08/R16 on worker/service messages.

**Rules and procedure:** Use explicit accepted handoffs, bounded queues, owner leases and timeout policies. Separate command intent from verified outcomes. Preserve business scope and minimize sensitive content in payloads.

**Acceptance and failure:** A lost acknowledgment retains sender ownership. An expired worker cannot overwrite its replacement’s accepted result.

<a id="chapter-30"></a>

## 30. Monitoring

**Owner and trigger:** R59/R26 on service observation.

**Rules and procedure:** Measure real customer/control paths plus host, task and dependency signals. Observe missing heartbeats and stale data from an independent failure domain. Assign alert ownership and verify delivery/fallback.

**Acceptance and failure:** A green server with broken checkout still alerts. Monitoring failure is visible, not counted as successful service.

<a id="chapter-31"></a>

## 31. Logging

**Owner and trigger:** R53/R23 on operational logging.

**Rules and procedure:** Record significant action, authority, result, incident and reconciliation events with correlation and safe redaction. Keep protected evidence outside ordinary executor deletion authority. Avoid collecting credentials or unnecessary private reasoning.

**Acceptance and failure:** Audit can trace adverse events after a tested failure. Local logs alone cannot certify off-host retention or end-to-end business evidence.

<a id="chapter-32"></a>

## 32. Secrets

**Owner and trigger:** R60/R24 on credential delivery and renewal.

**Rules and procedure:** Keep secrets in protected custody with scoped workload grants, expiry and revocation. Verify renewal and long-outage recovery under actual authority. A read-only script does not narrow the source credential’s underlying provider rights.

**Acceptance and failure:** Workers cannot retrieve broad credentials or all recovery material. A canary read proves only its own scope, not production write eligibility.

<a id="chapter-33"></a>

## 33. Security

**Owner and trigger:** R23/R52 on infrastructure assurance.

**Rules and procedure:** Review threat model, identity/network boundaries, protected pipelines, backups and common-administrator exposure. Require independent review for control changes and direct audit visibility. Controls apply to administrators and executives within the tested boundary.

**Acceptance and failure:** A compromise/bypass exercise and residual-risk register support sign-off. Written restrictions without enforced denial remain specifications.

<a id="chapter-34"></a>

## 34. Backups

**Owner and trigger:** R24/R26 on backup schedules and retention.

**Rules and procedure:** Identify authoritative stores, frequency, encryption/access, retention, independent copies and restore validation. Confirm actual data can be recovered and reconciled, not merely that a backup file exists.

**Acceptance and failure:** Evidence includes a permitted restore/read test and missing-job detection. Failed backups become owned incidents; old snapshots cannot restore revoked authority.

<a id="chapter-35"></a>

## 35. Disaster Recovery

**Owner and trigger:** R26/R59 on disaster recovery exercises.

**Rules and procedure:** Recover identity, configuration, state, external effects and customer service after loss of normal host and founder workstation. Preserve intentional suspension and current privacy restrictions. Measure recovery against business-specific objectives.

**Acceptance and failure:** Replacement/cutover and service-path evidence distinguish complete recovery from vault-only restoration. Unavailable nondelegable steps remain explicit dependencies.

<a id="chapter-36"></a>

## 36. Infrastructure as Code

**Owner and trigger:** R24/R20 on infrastructure changes.

**Rules and procedure:** Version reproducible desired configuration, assumptions, migration and rollback. Review privileged/control changes independently and keep secrets outside code. Detect drift and reconcile actual state before applying new plans.

**Acceptance and failure:** A replacement environment can be reconstructed within scope. An unreviewed manual fix becomes recorded remediation, not hidden permanent configuration.

<a id="chapter-37"></a>

## 37. Deployment Strategies

**Owner and trigger:** R25/R58 when releasing services or framework upgrades.

**Rules and procedure:** Choose staged, compatible rollout proportional to consequence; preserve approved artifact identity and source evidence. Define health gates, rollback/forward repair and handling of irreversible effects. Existing businesses adopt within their own authority.

**Acceptance and failure:** An incompatible candidate is rejected before broad distribution. Partial failure preserves customer obligations and prior recoverable state.

<a id="chapter-38"></a>

## 38. Scaling

**Owner and trigger:** R24/R43 on load and capacity signals.

**Rules and procedure:** Scale inside adopted financial and technical bounds using verified demand and reserved essential capacity. Apply backpressure and queue fairness before uncontrolled expansion. Include storage, traffic, model and recovery costs.

**Acceptance and failure:** An overload test protects existing obligations and total operation budgets. More workers cannot create more spending authority.

<a id="chapter-39"></a>

## 39. Vendor Management

**Owner and trigger:** R38/R24/R50 on provider selection and renewal.

**Rules and procedure:** Assess capability, permissions, data terms, service limits, costs, exit and recovery dependencies from current official evidence. Reuse suitable existing resources while recording actual commitments. Contract deviations require their real approval.

**Acceptance and failure:** The vendor record includes tested scope and expiry/renewal ownership. A logo in the stack is not proof of authorized account access.

<a id="chapter-40"></a>

## 40. Multi-Product Infrastructure

**Owner and trigger:** R58/R60 on shared services and new business instances.

**Rules and procedure:** Allocate isolated identities, quotas, data and cost records; record any scoped shared service contract. Preserve independent control and revoke obsolete access after accepted handover. Initial discovery clones are distinct from graduation or legal formation.

**Acceptance and failure:** Cross-business read/write/payment attempts fail. Shared infrastructure does not justify copying credentials or obligations without actual transfer authority.

<a id="chapter-41"></a>

## 41. Future Expansion

**Owner and trigger:** R55/R10 when considering new technology or markets.

**Rules and procedure:** Treat roadmaps as hypotheses with evidence, cost, applicability and transition plans. Benchmark replacements against current capabilities and preserve business continuity. Defer unneeded complexity and recheck current vendor/legal constraints when scope becomes concrete.

**Acceptance and failure:** Expansion has a bounded mandate and tested applicable profile. Future possibilities are not current capability claims or purchase commitments.

## Change history

- 1.0 — 2026-09-09: Completed all blueprint chapters as a reviewable manuscript, with concrete responsibilities, procedures, acceptance evidence and failure handling.
