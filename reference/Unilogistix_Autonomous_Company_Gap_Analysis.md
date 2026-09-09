# Unilogistix: autonomous-company gap analysis and implementation backlog

**Review date:** September 9, 2026  
**Repository:** `turkyildiz/Unilogistix`  
**Final reviewed commit:** `1f77d908f424afffecd556d7244f5c44e655e89d`  
**Status:** Analysis and proposed work only; no repository writes, account changes, production actions or new mandates performed.

## Executive assessment

Unilogistix has an explicit operating philosophy and broad company coverage, but the reviewed evidence supports **a governance and architecture foundation with partial infrastructure implementation**, not a fully operating autonomous company. The decisive gap is executable, connected business operations with independent enforcement and recovery—not more department names. The runtime, business operations and evolution books explicitly identify themselves as unimplemented initial specifications. [R03, R12, R14, R20, R27]

The target should be defined as **zero routine internal human work within an explicitly delegated, tested operating scope**, while founder/board governance remains authentic. Customer choices and external provider services must be recorded honestly. Safe pauses, abandoned tickets and unresolved tasks are not successful autonomy. This matches the existing autonomy policy. [R02]

Do not claim permanent autonomy from a repository audit, a happy-path demo, or a quiet period with no transactions. Autonomy, reliability, security and commercial viability need separate evidence.

## Scope and evidence limits

The review read the core governance and activation documents; runtime, organization, engineering, business, memory and evolution specifications; customer/security/financial policies; dashboards and Safe Goes brief; setup/validation scripts; GitHub workflow requirements; and vault bootstrap/refresh implementation. GitHub branch, ruleset and workflow-run APIs were also inspected.

The initial baseline was `ff1a69f6511f8ecf7111613db501d5f037c0d7ef`. The branch advanced during review. Both intervening commits were inspected through `1f77d908f424afffecd556d7244f5c44e655e89d`: one adds `credential-refresh.py`, and one updates the vault evidence. Older claims that audit logging or automatic canary delivery are entirely missing have therefore been superseded.

Live servers, production deployments, account grants, revenue and customer interactions were **not independently tested**. Statements about deployed vault tests are repository-reported evidence, not fresh live verification. One isolated Python validation-helper experiment was performed with mocked HTTP errors and no network or credentials; its results are in `assertion_regression.json`.

## Current-state findings

| Area | Evidence at review | What remains |
|---|---|---|
| Governance | Founder direction and zero-human target recorded | Adopted concrete standing mandates, authenticated board channel, limits and first-product activation [R01, R26] |
| Runtime | Durable task/execution design; interactive legacy launcher | A supervised, persistent company operating runtime [R03, R08] |
| CI/CD | `main` reports unprotected and no required checks; ruleset API returned `[]`; Actions runs API returned zero | Enforced automated tests, independent verification, machine-triggered CI and deployment/rollback [R04, R11] |
| Vault | Canary isolation, audit rotation, a renewing issuer and automated canary credential delivery reported tested | Production identities, recovery after issuer expiry, scheduled backup, full unseal/read restore, remote durable audit and action gateway [R05, R07] |
| Marketing/sales/support/finance | Broad contracts, policy and acceptance expectations | Connected business services and executable end-to-end workflows [R09, R12, R16, R18] |
| Feedback/learning | Provenance, experiments, canaries and rollback specified | Operational ingestion, prioritization, evaluation, release and measured customer follow-up [R13, R14] |
| Reporting | Metric definitions and honest denominator rules | Source instrumentation, targets, dashboards and observed outcomes [R02, R15] |
| First business | Safe Goes candidate with location simulator acceptance | Validated narrow offer, authorized live product, customer lifecycle and viability evidence [R19] |

## Concrete engineering findings

### 1. CI is not presently enforced

The workflow directory describes planned checks rather than active workflow execution. GitHub's observed branch response reports protection disabled and no required status checks; ruleset and run lists were empty. This demonstrates missing GitHub-side gates at inspection, not proof that no external CI system exists anywhere. [R04, R11]

A particularly important implementation trap: current GitHub documentation says certain PR events created using `GITHUB_TOKEN` produce approval-required workflow runs. A scoped GitHub App installation token is the better default for UNI-created PRs that must start CI without a routine human click. Keep protected verification, safe triggers and least privilege; do not remove review or execute untrusted PR code in a privileged context to eliminate approval friction. [S01, S02]

### 2. Vault work has progressed, but recovery remains incomplete

The latest vault record reports file audit and rotation, automatic bootstrap credentials, short-outage behavior and an off-host snapshot accepted by a disposable vault. Those are useful partial controls. The same record says the restored vault was not fully unsealed; backups remain session-driven rather than scheduled; the issuer needs administrator re-issuance after a 24-hour renewal outage; and the broker serves only a non-sensitive canary. [R05]

Require complete restore-and-read evidence and workload re-bootstrap after prolonged outage. Do not solve recovery by consolidating all privileged recovery material into the ordinary agent's trust domain. Test disk/audit failure too: OpenBao documents request availability dependence on audit-device behavior. [S03]

### 3. Security verification can misreport success under Python optimization

`bootstrap.py` uses `assert exc.code == 403` to validate expected denials. The isolated experiment showed that a mocked HTTP 500 is rejected under ordinary compilation but accepted as an expected denial with optimization enabled. Canary calls inside `assert` in both bootstrap and credential refresh can also be omitted entirely. Python explicitly removes assertion statements under optimization. [R06, R07, S04]

This is a **test/evidence integrity defect**, not evidence that OpenBao's ACLs are bypassed. Replace these assertions with always-executed conditions and negative tests for normal and optimized execution.

### 4. Documentation checks are not operational checks

`validate_foundation.py` checks root files, links, metadata, chapter coverage and the autonomy phrase. The setup tests check mocked configuration and preservation behavior. Neither demonstrates a working refund, support resolution, production release or recovered company operation. Keep these useful checks, but do not use their passing result as an autonomy certificate. [R21, R22]

## The operating design to implement

Use a small number of shared services, not dozens of permanently running executive personas. A coordinator routes work; specialist workers create deliverables; independent verification checks evidence; a deterministic action gateway authorizes side effects. Identity, budgets and board control remain outside ordinary model authority. [R03, R17, R20]

The proposed company has eight accountable functions: coordination; product/research; engineering; independent assurance; growth/sales; customer operations; finance; and reliability/security. These are responsibilities, not a requirement for eight always-on model instances. Work must also cover knowledge stewardship and recurring obligations.

### Reuse the existing infrastructure deliberately

The founder-reported pool is Cloudflare, GitHub, Vercel, Supabase, Fireworks.ai, on-prem servers and Hetzner; account scope, capacity and total cost still require verification. [R10]

Proposed placement: GitHub for source and verified delivery; Supabase/Postgres for authoritative company/customer records with explicit tenancy; suitable existing compute for isolated workers and reliability services; OpenBao for machine secrets; Cloudflare/Vercel for appropriate edge/frontend functions; Fireworks for evaluated inference tasks. Do not provision all providers simply because they are available.

Choose one durable orchestration implementation. Cloudflare Workflows is an existing-provider candidate because it supports persisted multi-step execution, retries and external-event waits. Benchmark fit, limits, data boundaries, failure behavior and total cost before adopting it. Do not equate managed retries with exactly-once external payments or emails. [S09]

Do not give an agent a Supabase administrative/service-role credential and assume row policies will contain it: privileged roles can bypass RLS. Route business actions through scoped identities and explicit server-side authorization. [S06]

### One mandatory transaction spine

For every important action preserve: customer/tenant ID, business-operation ID, task ID, mandate/policy version, actor identity, idempotency key, review record, external receipt, cost allocation and verified outcome. Keep raw personal, location and financial data in private operational systems; public GitHub gets sanitized work and evidence references. [R03, R13, R16, R18]

## Four closed business loops

### Marketing and acquisition

Research a specific customer segment; form an evidence-backed offer; produce and verify content; publish through an approved channel; capture qualified leads; attribute activation and revenue; compare cost and retention; then improve or stop the campaign. Add deliverability, consent, unsubscribe, bounce and complaint handling—not just copy generation. Adopt SPF, DKIM and DMARC plus one-click unsubscribe for marketing as a sensible baseline; Gmail has explicit sender requirements, with additional bulk-sender requirements. [R12, R16, S05]

Pause acquisition automatically when support backlog, service reliability, capacity or cash guardrails are exceeded. Optimize retained customer value and contribution, not impressions or content volume.

### Sales, onboarding, billing and retention

Qualification leads to an approved offer, terms, payment, entitlement, onboarding and a measured first useful outcome. Recover stalled onboarding. Process renewal, failed payment, cancellation, refunds and disputes through the same identities and obligation ledger. A transaction timeout must trigger reconciliation, not a blind second charge. Stripe's documentation is an example of why integrations must handle duplicate/out-of-order webhooks and explicit idempotency; it is not a claim Stripe is selected for UNI. [R12, R18, S07, S08]

### Support and service recovery

Authenticate; classify; inspect trusted telemetry and knowledge; perform a permitted remedy; verify the result; communicate; close or reopen; and send genuine product gaps to engineering. A chatbot response is not a resolved customer problem. Use SLA clocks, severity-based queues and aging detection. Normal escalation goes to another qualified AI function or an authorized recovery workflow—not the founder acting as help desk. [R02, R16]

### Feedback to measurable improvement

Customer evidence → privacy filtering and deduplication → diagnosis and reproducible case → prioritized hypothesis → protected regression test → proposed product/prompt/workflow change → independent evaluation → canary release → measured outcome → customer follow-up → curated knowledge.

Separate knowledge learning, operating-process learning and product learning. Start with versioned retrieval, SOPs, prompts and experiments; do not treat arbitrary customer text as trusted model-training data or permission to modify the company. Preserve held-out cases and record negative results. A before/after improvement alone does not establish causality; use suitable experiments and report small-sample uncertainty. [R13, R14]

## Implementation sequence: gates, not calendar promises

| Gate | Deliverable | Required evidence |
|---|---|---|
| A — Trusted foundation | Standing mandates, scoped identity, vault recovery, action gateway, protected CI and immutable enforcement | Over-limit and forged actions denied; ordinary authorized actions and AI-created PRs proceed without routine approval |
| B — Durable operating slice | Objective → durable task → worker → independent review → tested PR → sandbox release → audit | Crash, replay, retry, revocation and rollback tests pass |
| C — Complete first business | One product plus acquisition, sale, onboarding, billing, support, cancellation and obligation handling | One integrated sandbox customer lifecycle; then authorized live evidence |
| D — Learning and resilience | Feedback-to-release loop, autonomous incidents, recurring maintenance and meaningful dashboards | A customer problem leads to a verified fix and measured outcome; prolonged dependency failures are handled honestly |
| E — Autonomy graduation | Sustained representative workload under adopted thresholds | Zero ordinary human asks/work, no hidden stalled obligations, and passing reliability/security/financial gates |
| F — Replication | Second isolated venture, transfer and retirement | Isolation, budgets, customer obligations and board revocation survive handover |

Marketing and support specifications can be developed during foundation work, but live outbound messages, spending and production access remain gated by their actual permissions. A GitHub automation demonstration is not yet an operating company.

## Suggested graduation protocol — not yet adopted

A proposed initial evidence window is 30 consecutive operating days **and at least one complete applicable billing/renewal cycle**, with a meaningful customer-operation mix and workload volume determined for the product. Include low-frequency failure tests even when live traffic does not naturally produce them. Synthetic tests prove technical behavior, not market demand or real retention.

Measure operational human asks, human minutes, verified autonomous completion, aged unresolved work, reopened tickets, SLO compliance, billing reconciliation, losses/refunds, acquisition-to-retention outcomes and fully allocated cost. Count human asks when issued, even unanswered. Keep zero-traffic denominators unavailable, not perfect. Count at a stable business-operation level rather than inflating the denominator with artificial subtasks. [R02, R15]

At minimum, test: worker death; duplicate and reordered events; model outage; a failed canary release; a database migration failure; vault host loss; issuer expiry beyond 24 hours; blocked audit output; a full disk; concurrent spending; payment timeout; forged customer identity; cross-tenant retrieval; poisoned feedback; a missed maintenance deadline; board suspension; customer cancellation; and a support case reopened after false resolution.

A routine founder repair invalidates the clean autonomy claim for that observation cohort. Reserved board decisions remain governance, but ordinary decisions cannot be relabeled to hide dependence. A failed operation may safely stop; it must stay visible as failed or blocked.

## Issue-ready implementation backlog

All paths below are proposed locations unless they name an already inspected file. These items have **not** been created in GitHub. P0 means prerequisite for consequential unattended operation; P1 means necessary to call the first business fully operating; P2 means scale/physical-scope work that must precede activating those capabilities. Items are dependency-linked, not a claim of linear execution order.

### UNI-001 — Activate bounded standing mandates

**Priority:** P0 · **Accountable AI function:** Governance  
**Dependencies:** None  
**Evidence:** R01, R02, R26

**Gap:** Budget, production authority, first-product mandate, authenticated board channel, and detailed adoption are not activated in the register.

**Implement:** Implement authenticated board resolutions with exact scope, version, expiry, revocation and immutable evidence. Compile mandates into enforceable per-action, daily, recurring and portfolio limits. Cover routine releases, marketing, support remedies, approved vendor use and continuity explicitly.

**Acceptance:** An in-scope release/refund executes after automated gates without a new founder ask. An expired mandate, forged board message, or missing monetary cap denies execution and creates a truthful blocked record.

**Proposed paths:** `governance/mandates/`, `schemas/mandate.schema.json`, `services/governance/`

### UNI-002 — Run an unattended durable orchestrator

**Priority:** P0 · **Accountable AI function:** Operations / Engineering  
**Dependencies:** UNI-001  
**Evidence:** R03, R08

**Gap:** The operating layer is a specification; start_uni.py is an interactive bootstrap launcher, explicitly not the selected unattended design.

**Implement:** Deploy supervised durable workflows with leases, checkpoints, deadlines, bounded retries, concurrency quotas and failure queues. Keep operational state outside chat context; separate company workflow execution from customer product uptime.

**Acceptance:** Kill a worker after an external action; restart and reconcile without repeating the effect. Missed scheduled work is recovered after downtime and no task becomes ownerless.

**Proposed paths:** `services/orchestrator/`, `workers/`, `tests/recovery/`

### UNI-003 — Create authoritative records and reliable events

**Priority:** P0 · **Accountable AI function:** Data / Engineering  
**Dependencies:** UNI-002  
**Evidence:** R03, R13

**Gap:** Task, customer, payment and knowledge contracts exist in prose, not as a demonstrated integrated operational store.

**Implement:** Implement versioned schemas and migrations for tenants, mandates, tasks, tool actions, reviews, customers, tickets, feedback, experiments, releases and obligations. Use a transactional outbox/inbox, signature validation, deduplication, replay handling and correlation IDs; assign exactly one source of truth per entity.

**Acceptance:** Duplicated, delayed and out-of-order events converge to the correct business state. A database commit followed by process loss does not lose its outbound event.

**Proposed paths:** `schemas/`, `db/migrations/`, `services/events/`

### UNI-004 — Enforce tool actions outside the model

**Priority:** P0 · **Accountable AI function:** Security / Platform  
**Dependencies:** UNI-001, UNI-003, UNI-030  
**Evidence:** R25, R17, R18

**Gap:** The tool gateway, live authorization and atomic spending enforcement are not implemented.

**Implement:** Expose typed business actions rather than unrestricted shell, SQL or payment tools. Check identity, tenant, mandate, limits, resource, recipient, policy version and revocation on execution. Reserve budget atomically; bind approval and idempotency to the exact action; reconcile uncertain provider success before retrying.

**Acceptance:** Concurrent individually valid requests cannot exceed their combined budget. Injected customer instructions cannot change a destination, read another tenant, obtain secrets or expand permissions.

**Proposed paths:** `services/action-gateway/`, `tests/authorization/`, `tests/idempotency/`

### UNI-005 — Deliver and recover production workload identities

**Priority:** P0 · **Accountable AI function:** Platform / Security  
**Dependencies:** UNI-001  
**Evidence:** R05, R07, R09, R10

**Gap:** Automated credentials now serve the bootstrap canary only; a 24-hour issuer-renewal outage still needs administrator re-issuance.

**Implement:** Bind short-lived identities to actual services and environments, with scoped permissions and audited credential delivery. Implement board-authorized re-bootstrap after issuer expiry, host loss and machine replacement without exposing recovery authority to normal workers.

**Acceptance:** A canary-authorized identity cannot become a production workload identity. A simulated outage longer than the issuer period and subsequent host replacement recover under the same standing authority without a person repairing credentials.

**Proposed paths:** `infrastructure/identity/`, `infrastructure/openbao/`, `tests/identity/`

### UNI-006 — Finish vault audit, backup and recovery

**Priority:** P0 · **Accountable AI function:** Security / Reliability  
**Dependencies:** UNI-005  
**Evidence:** R05, S03

**Gap:** File audit and rotation are reported verified, but remote durable audit, capacity monitoring, scheduled backups and full restored-vault unseal/read remain unfinished.

**Implement:** Schedule protected backups with retention and independent off-site storage; test complete restoration and application reads. Monitor disk, audit health and credential age; validate failure behavior with the actual deployed OpenBao version. Review direct TLS and the shared-administrator trust boundary.

**Acceptance:** A disposable replacement vault unseals and serves the expected recovered records, not merely accepts a snapshot. Disk exhaustion, audit sink blockage and backup failure produce bounded recovery or explicit safe failure without silent loss.

**Proposed paths:** `infrastructure/openbao/`, `infrastructure/backups/`, `tests/disaster-recovery/`

### UNI-007 — Install enforced and unattended CI

**Priority:** P0 · **Accountable AI function:** Engineering  
**Dependencies:** UNI-001, UNI-005  
**Evidence:** R04, R11, R23, S01, S02

**Gap:** GitHub reported main unprotected, no required checks, an empty ruleset list and zero Actions runs at inspection.

**Implement:** Add real workflows for foundation checks, setup tests, runtime tests, dependency/security review and acceptance evidence. Enforce required checks from trusted identities, prevent routine direct pushes and force pushes, pin actions and isolate untrusted builds. Use a scoped GitHub App for autonomous PR creation where GITHUB_TOKEN would require workflow approval.

**Acceptance:** A broken change and an unauthorized direct push are rejected by the provider configuration. An AI-created PR automatically starts required CI and passes or fails without a human approval click.

**Proposed paths:** `.github/workflows/ci.yml`, `.github/workflows/security.yml`, `infrastructure/github/`

### UNI-008 — Replace assertion-dependent security verification

**Priority:** P0 · **Accountable AI function:** Engineering / Security  
**Dependencies:** None  
**Evidence:** R06, R07, S04

**Gap:** Bootstrap denial validation and canary calls use assert; optimized Python can remove those checks and even the canary request.

**Implement:** Replace security-relevant assertions with explicit checks that always execute and raise typed errors. Refactor scripts behind callable entry points; mock provider failures and test normal and optimized execution. Keep outcome evidence distinct from PASS text.

**Acceptance:** HTTP 403 is accepted as an expected denial; 401, 404, 429 and 500 are not mislabeled as a passing denial. A failed canary never produces PASS or publishes a runtime credential under normal Python, -O or PYTHONOPTIMIZE.

**Proposed paths:** `infrastructure/openbao/bootstrap.py`, `infrastructure/openbao/credential-refresh.py`, `tests/openbao/`

### UNI-009 — Make AI roles executable and evaluable

**Priority:** P0 · **Accountable AI function:** AI Platform  
**Dependencies:** UNI-002, UNI-004  
**Evidence:** R03, R20, R14

**Gap:** Departments and roles specify accountability but do not provide deployed workers or measured agent capability.

**Implement:** Create a versioned registry for model, prompt, tool schema, permissions, data access, cost limits and evaluation results. Start with coordinator, product/research, builder, independent verifier, growth, customer operations, finance and reliability/security responsibilities; instantiate workers only when needed.

**Acceptance:** A worker cannot claim a role without passing that role's required evaluations and receiving its scoped identity. Verifier credentials and protected checks are inaccessible to the author of the change being verified.

**Proposed paths:** `agents/registry/`, `evaluations/`, `workers/`

### UNI-010 — Automate reviewed release and rollback

**Priority:** P0 · **Accountable AI function:** Engineering / Reliability  
**Dependencies:** UNI-007, UNI-009, UNI-023  
**Evidence:** R11, R23, S02

**Gap:** An executable build-review-release-observe-rollback path is not demonstrated.

**Implement:** Build immutable artifacts and promote the same digest through staging and production after independent checks and standing-mandate validation. Add preview tests, migration compatibility tests, canary/feature-flag rollout, business guardrails, autonomous rollback and post-release evidence.

**Acceptance:** A staged regression triggers rollback and preserves customer data and outstanding obligations. The builder cannot replace a reviewed artifact, approve itself or disable the trusted release gate.

**Proposed paths:** `.github/workflows/release.yml`, `services/release-controller/`, `tests/releases/`

### UNI-011 — Implement customer identity, CRM and consent

**Priority:** P1 · **Accountable AI function:** Customer Operations / Data  
**Dependencies:** UNI-003, UNI-004, UNI-021  
**Evidence:** R12, R16

**Gap:** Customer lifecycle responsibilities exist, but CRM, identity and communication-provider operation are not verified.

**Implement:** Build canonical customer/organization records, entitlements, consent, lifecycle states, approved terms, promises and contact history. Connect company-owned email/chat channels with delivery receipts, threading, suppression lists and idempotent sends.

**Acceptance:** The same customer remains linked across lead, purchase, onboarding, support and renewal. Unsubscribing suppresses pending marketing sends while necessary service notices follow their separate permitted policy.

**Proposed paths:** `services/customers/`, `services/crm/`, `integrations/communications/`

### UNI-012 — Implement billing and finance administration

**Priority:** P1 · **Accountable AI function:** Finance  
**Dependencies:** UNI-003, UNI-004, UNI-005, UNI-011  
**Evidence:** R18, R12, S07, S08

**Gap:** Billing, accounting and payment integrations are unselected/unverified; financial control requirements are prose.

**Implement:** Implement product catalog, entitlements, orders/subscriptions, invoices, collections, credits, cancellations, refunds, chargeback handling and reconciliation. Separate collected cash, revenue, reservations, fees, liabilities and forecasts; enforce counterparty and account-change controls.

**Acceptance:** A duplicated webhook and a timeout after a successful charge cannot produce duplicate charges, refunds or entitlements. Cancellation, failed renewal and disputes reconcile correctly and do not silently erase obligations.

**Proposed paths:** `services/billing/`, `services/finance/`, `integrations/payments/`, `tests/finance/`

### UNI-013 — Operate a measured marketing function

**Priority:** P1 · **Accountable AI function:** Growth  
**Dependencies:** UNI-010, UNI-011, UNI-012, UNI-015, UNI-020  
**Evidence:** R12, R16, S05

**Gap:** Marketing is described but no connected campaign execution or acquisition-outcome loop is demonstrated.

**Implement:** Implement segment research, evidence-backed positioning, content production, claim checking, website publication and one approved acquisition channel first. Track campaign/cohort attribution through activation and contribution; enforce spending, consent, sender authentication, unsubscribe, bounce and complaint policies; pause acquisition when support or reliability guardrails breach.

**Acceptance:** An authorized campaign is planned, published, attributed, evaluated and paused or adjusted without routine founder approval. A claim without evidence and a send to a suppressed recipient are blocked before publication.

**Proposed paths:** `services/growth/`, `workflows/business/campaign/`, `tests/growth/`

### UNI-014 — Close sales and onboarding loops

**Priority:** P1 · **Accountable AI function:** Sales / Customer Success  
**Dependencies:** UNI-011, UNI-012, UNI-022  
**Evidence:** R12, R16

**Gap:** A customer can be discussed in the blueprint without an implemented offer-to-activated-service workflow.

**Implement:** Implement qualification, approved offers/discounts, terms acceptance, checkout handoff, onboarding, activation checks and stalled-onboarding recovery. Persist commitments and service entitlements; never allow sales text to create an unsupported feature or service guarantee.

**Acceptance:** An eligible customer completes purchase and reaches the first useful product outcome automatically. A failed payment, unsupported requirement or stalled setup triggers a bounded alternative rather than a false completed sale.

**Proposed paths:** `services/sales/`, `workflows/business/onboarding/`

### UNI-015 — Resolve customer issues, not merely answer

**Priority:** P1 · **Accountable AI function:** Customer Operations  
**Dependencies:** UNI-009, UNI-011, UNI-012, UNI-022  
**Evidence:** R12, R16

**Gap:** Support policies define ownership and identity checks but there is no demonstrated ticket-to-resolution runtime.

**Implement:** Implement authenticated ticket intake, severity, SLA clocks, telemetry-backed diagnosis, approved remedies, service recovery and engineering handoff. Require evidence of resolution, customer follow-up, reopen handling and backlog monitoring; route ordinary escalation to qualified AI functions.

**Acceptance:** A routine issue reaches a verified remedy, appropriate communication and an auditable closure without human operational work. A social-engineering request for another account or an excessive refund fails, and an unanswered ticket cannot age silently.

**Proposed paths:** `services/support/`, `workflows/business/support-resolution/`, `tests/support/`

### UNI-016 — Turn customer feedback into evidence

**Priority:** P1 · **Accountable AI function:** Product / Customer Success  
**Dependencies:** UNI-003, UNI-015, UNI-020  
**Evidence:** R13, R14

**Gap:** Feedback is a chapter and an improvement input, not an operational evidence pipeline.

**Implement:** Ingest tickets, surveys, churn, lost sales, reviews and permitted product telemetry into provenance-bearing feedback records. Redact private data, identify duplicates, distinguish defect/request/confusion/abuse, reproduce where possible, and prioritize by severity, affected cohorts, expected impact and cost.

**Acceptance:** Repeated reports of one defect create one linked root issue while retaining each customer's history. A malicious instruction in feedback cannot become policy, a secret request or an authorized code change.

**Proposed paths:** `services/feedback/`, `schemas/feedback.schema.json`, `tests/feedback/`

### UNI-017 — Release learning through controlled experiments

**Priority:** P1 · **Accountable AI function:** Product / AI Quality  
**Dependencies:** UNI-009, UNI-010, UNI-016  
**Evidence:** R13, R14

**Gap:** Baseline/challenger evaluation, canary adoption and rollback are specified but not implemented.

**Implement:** Separate learning into reviewed knowledge/SOP updates, workflow/prompt/model updates and product changes; do not train directly on arbitrary raw tickets. Use held-out regression cases, cost/quality/safety guardrails, versioned experiments, appropriately designed customer measurement and rollback. Close the loop by notifying affected customers.

**Acceptance:** A change that improves one score but leaks data, worsens resolution or exceeds cost is rejected. A released improvement traces back to feedback, test evidence, deployment and measured customer outcome; a bad challenger rolls back.

**Proposed paths:** `services/experiments/`, `evaluations/holdout/`, `workflows/business/feedback-to-release/`

### UNI-018 — Recover from incidents autonomously

**Priority:** P0 · **Accountable AI function:** Reliability / Operations  
**Dependencies:** UNI-002, UNI-004, UNI-006, UNI-010  
**Evidence:** R17, R03

**Gap:** No demonstrated executable incident-response and recovery operating loop covers the company.

**Implement:** Implement SLO-based alerts, incident ownership, bounded retries, provider failover within mandate, rollback, circuit breakers and financial reconciliation. Add runbooks for queue stalls, model outage, provider changes, expired credentials, disk pressure, failed migrations and compromised workloads.

**Acceptance:** A model/provider outage invokes an approved alternative within the same data and spending boundaries. A failed repair does not recurse indefinitely, exceed budget, or relabel a safe pause as successful completion.

**Proposed paths:** `services/reliability/`, `runbooks/`, `tests/chaos/`

### UNI-019 — Monitor and stop the company independently

**Priority:** P0 · **Accountable AI function:** Security / Governance  
**Dependencies:** UNI-001, UNI-004, UNI-005  
**Evidence:** R17, R26

**Gap:** Board shutdown, independent monitoring and descendant revocation remain specifications.

**Implement:** Deploy a watchdog outside the orchestrator's failure and permission domain; use independent heartbeat, queue-age and customer-path checks. Give the board an authenticated suspension/revocation path covering scheduled jobs, gateways, deployment, payments and descendants. Define funded continuity and expiry behavior.

**Acceptance:** Killing or compromising the orchestrator does not disable board suspension or monitoring. Revocation stops queued consequential actions and later descendants; routine service recovery follows valid runbooks without inventing authority.

**Proposed paths:** `services/watchdog/`, `services/board-control/`, `tests/revocation/`

### UNI-020 — Instrument truthful operating outcomes

**Priority:** P0 · **Accountable AI function:** Operations / Intelligence  
**Dependencies:** UNI-003  
**Evidence:** R02, R15

**Gap:** KPI definitions exist without live source instrumentation or adopted thresholds.

**Implement:** Connect source events to dashboards for autonomy, aged backlog, SLA, uptime, acquisition, activation, retention, money and cost per accepted outcome. Use fixed business-operation definitions, include failed and blocked cases, keep retries separate and reconcile unfinished cohorts.

**Acceptance:** Zero traffic shows unavailable rather than 100% autonomy. An unanswered human ask, a blocked operation and a later reopened ticket remain visible and cannot be excluded to improve results.

**Proposed paths:** `services/observability/`, `dashboards/`, `tests/metrics/`

### UNI-021 — Enforce tenant privacy and knowledge boundaries

**Priority:** P0 · **Accountable AI function:** Security / Data  
**Dependencies:** UNI-003, UNI-005  
**Evidence:** R13, R16, S06

**Gap:** Data isolation and retention are specified but not demonstrated against deployed stores and retrieval.

**Implement:** Implement database grants and row policies, storage/search access checks, scoped service actions and data classification. Keep raw customer/location/financial data out of public GitHub; propagate deletion, supersession and access revocation to derived indexes and caches under adopted retention rules.

**Acceptance:** An authenticated customer and a support worker cannot retrieve another tenant's data through tables, views, storage or search. A revoked/deleted or superseded knowledge record cannot continue guiding consequential work through a stale index.

**Proposed paths:** `db/policies/`, `services/knowledge/`, `tests/tenancy/`

### UNI-022 — Build one bounded, supported first product

**Priority:** P1 · **Accountable AI function:** Product  
**Dependencies:** UNI-001, UNI-010, UNI-021  
**Evidence:** R19, R12

**Gap:** Safe Goes is a GPS-tracking candidate, not an activated product mandate or supported service.

**Implement:** Fix a narrow initial customer, supported use case, value proposition, acceptance criteria, price assumptions and support obligation. Use simulated devices/test identities first; graduate real location/device use only after authorization, retention, misuse and isolation tests.

**Acceptance:** A test account receives and views authorized location, gets an auditable geofence event and loses access after revocation. A customer can reach a useful outcome; a successful demo alone cannot activate live tracking, buying or launch.

**Proposed paths:** `products/safe-goes/`, `tests/product-acceptance/`

### UNI-023 — Reproduce infrastructure and recover deployments

**Priority:** P0 · **Accountable AI function:** Platform  
**Dependencies:** UNI-006, UNI-007  
**Evidence:** R05, R10, R11

**Gap:** Scripts and live setup reports do not yet demonstrate a complete rebuildable environment and service recovery system.

**Implement:** Commit sanitized infrastructure configuration, service units, timer configuration and deployment dependencies; retain secrets separately. Record artifact/configuration digests, backup inventories, resource placement, capacity and recovery objectives; test reconstruction on a replacement environment.

**Acceptance:** A replacement environment can be rebuilt from reviewed code and authorized secrets without undocumented workstation state. The restored service passes its customer-path tests within the board-adopted recovery objectives.

**Proposed paths:** `infrastructure/`, `deploy/`, `tests/rebuild/`

### UNI-024 — Schedule all recurring business obligations

**Priority:** P1 · **Accountable AI function:** Operations / Finance  
**Dependencies:** UNI-003, UNI-012, UNI-015  
**Evidence:** R12, R17, R18

**Gap:** The repository does not demonstrate a durable calendar of operational commitments and their completion evidence.

**Implement:** Track renewals, subscription cancellations, domain/certificate expiry, provider deprecations, vulnerability patches, monthly close, retention jobs and adopted compliance deadlines. Assign owner, authority, funding, due date, retry policy and proof of completion to each obligation.

**Acceptance:** A missed execution after downtime is caught up without duplicating a payment or filing. Product closure or parent downtime cannot silently discard support, cancellation, data-retention or funded customer obligations.

**Proposed paths:** `services/obligations/`, `workflows/business/scheduled-operations/`

### UNI-025 — Graduate, replicate and retire ventures safely

**Priority:** P2 · **Accountable AI function:** Portfolio  
**Dependencies:** UNI-018, UNI-019, UNI-022, UNI-024, UNI-028  
**Evidence:** R14, R17

**Gap:** Controlled venture replication is a future lifecycle specification, not evidence of repeatable independent operation.

**Implement:** Template an isolated product instance with scoped identity, budget, data, support and metrics only after a first venture meets graduation gates. Test handover and retirement, preserve liabilities and revocation, and prevent uncontrolled self-replication.

**Acceptance:** A second venture cannot access the first venture's private records or exceed the portfolio cap. A transfer or shutdown preserves obligations and parent/board control.

**Proposed paths:** `services/portfolio/`, `templates/product-runtime/`, `tests/venture-lifecycle/`

### UNI-026 — Certify autonomy with representative evidence

**Priority:** P1 · **Accountable AI function:** Independent Assurance  
**Dependencies:** UNI-013, UNI-014, UNI-015, UNI-017, UNI-018, UNI-019, UNI-020, UNI-021, UNI-024, UNI-028  
**Evidence:** R02, R15, R17

**Gap:** No adopted observation window and no demonstrated real-business autonomy evidence support graduation.

**Implement:** Build an acceptance suite covering business, reliability, security, finance and autonomy failures, plus a sustained observation run. Require zero ordinary human asks/work, business/reliability thresholds, a representative scenario mix and at least one complete applicable customer billing lifecycle. Proposed numeric thresholds require board adoption.

**Acceptance:** Simulated customers are labeled synthetic and cannot establish real demand, retention or financial viability. A routine founder repair resets the clean observation window; a safety pause remains blocked/failed rather than autonomous success.

**Proposed paths:** `tests/company-acceptance/`, `evidence/autonomy/`, `dashboards/autonomy/`

### UNI-027 — Generate status from current evidence

**Priority:** P1 · **Accountable AI function:** Knowledge / Assurance  
**Dependencies:** UNI-007, UNI-020  
**Evidence:** R21, R24, R01, R05

**Gap:** Older overview/activation language lags newer publication and vault work; the validator checks documentation structure, not live capability.

**Implement:** Add capability records linking specification, implementation, deployed artifact, test run, environment, freshness and accountable owner. Generate status summaries and detect stale claims; distinguish configured, authenticated, tested, deployed and autonomous.

**Acceptance:** A changed implementation or expired test invalidates its prior ready status. A Markdown heading or configured MCP entry can never alone mark a business capability operational.

**Proposed paths:** `schemas/capability.schema.json`, `services/evidence/`, `scripts/validate_capabilities.py`

### UNI-028 — Prove business viability as well as automation

**Priority:** P1 · **Accountable AI function:** Product / Finance  
**Dependencies:** UNI-012, UNI-020, UNI-022  
**Evidence:** R12, R15, R18

**Gap:** There are no activated demand, margin, retention, reserve or stop thresholds for the initial venture.

**Implement:** Tie product experiments to observed customer value, acquisition, activation, renewal, support cost and fully allocated operating cost. Keep technical autonomy and commercial viability as separate scorecards; set stop/pivot rules and funded service-continuity obligations.

**Acceptance:** High content output or many closed tickets cannot substitute for customer value and retained revenue. An unprofitable or harmful acquisition experiment stops within its mandate while existing commitments remain serviced.

**Proposed paths:** `services/business-intelligence/`, `products/metrics/`, `tests/business-guardrails/`

### UNI-029 — Account for physical and external dependencies

**Priority:** P2 · **Accountable AI function:** Operations / Product  
**Dependencies:** UNI-022, UNI-024  
**Evidence:** R02, R16, R19

**Gap:** Hardware manufacture, installation, return and physical repair are not demonstrated autonomous capabilities.

**Implement:** Record supplier/customer/account-owner dependencies explicitly; use auditable authorized interfaces and permitted device actions. Keep software simulation separate from physical validation; do not count outsourcing routine internal work to people as autonomous execution.

**Acceptance:** An unavailable installation or repair capability blocks the relevant operation instead of claiming completion. A device action outside authorized scope is denied independently of the planner.

**Proposed paths:** `integrations/suppliers/`, `products/device-contracts/`, `tests/hardware-boundaries/`

### UNI-030 — Protect the enforcement trust boundary

**Priority:** P0 · **Accountable AI function:** Security / Governance  
**Dependencies:** UNI-001, UNI-005  
**Evidence:** R17, R20, R25

**Gap:** There is no demonstrated boundary preventing ordinary builders or self-improvement from rewriting their own safety and approval controls.

**Implement:** Separate builder, reviewer, release, finance, governance and recovery identities; use protected policy/verification artifacts with a distinct release path. Prevent operational roles from editing board identity, increasing budgets, replacing required tests, spoofing trusted check results or disabling audit.

**Acceptance:** A malicious PR that changes its acceptance test, disables a guard or forges a reviewer cannot pass the independently protected gate. Changing models or prompts cannot increase tool permissions or erase evidence.

**Proposed paths:** `services/policy-enforcement/`, `infrastructure/trust-boundaries/`, `tests/control-integrity/`

## Evidence references

Repository file URLs are pinned to the final reviewed commit. Live API observations describe the inspection only and can change. Source URLs are supplied as code text for reproducibility.

- **R01** — `governance/BOARD_REGISTER.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/governance/BOARD_REGISTER.md`
- **R02** — `policies/autonomy.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/policies/autonomy.md`
- **R03** — `books/BOOK-02-AI-OPERATING-SYSTEM/README.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/books/BOOK-02-AI-OPERATING-SYSTEM/README.md`
- **R04** — `.github/workflows/README.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/.github/workflows/README.md`
- **R05** — `infrastructure/openbao/README.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/infrastructure/openbao/README.md`
- **R06** — `infrastructure/openbao/bootstrap.py`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/infrastructure/openbao/bootstrap.py`
- **R07** — `infrastructure/openbao/credential-refresh.py`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/infrastructure/openbao/credential-refresh.py`
- **R08** — `scripts/start_uni.py`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/scripts/start_uni.py`
- **R09** — `integrations/README.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/integrations/README.md`
- **R10** — `integrations/EXISTING_STACK.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/integrations/EXISTING_STACK.md`
- **R11** — `books/BOOK-05-ENGINEERING/README.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/books/BOOK-05-ENGINEERING/README.md`
- **R12** — `books/BOOK-06-BUSINESS-OPERATIONS/README.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/books/BOOK-06-BUSINESS-OPERATIONS/README.md`
- **R13** — `books/BOOK-07-KNOWLEDGE-MEMORY-INTELLIGENCE/README.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/books/BOOK-07-KNOWLEDGE-MEMORY-INTELLIGENCE/README.md`
- **R14** — `books/BOOK-10-EVOLUTION/README.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/books/BOOK-10-EVOLUTION/README.md`
- **R15** — `dashboards/README.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/dashboards/README.md`
- **R16** — `policies/product-and-customers.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/policies/product-and-customers.md`
- **R17** — `policies/security-and-continuity.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/policies/security-and-continuity.md`
- **R18** — `policies/financial-policy.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/policies/financial-policy.md`
- **R19** — `products/safe-goes/README.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/products/safe-goes/README.md`
- **R20** — `books/BOOK-03-ORGANIZATION/README.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/books/BOOK-03-ORGANIZATION/README.md`
- **R21** — `scripts/validate_foundation.py`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/scripts/validate_foundation.py`
- **R22** — `scripts/test_setup_mcp.py`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/scripts/test_setup_mcp.py`
- **R23** — `workflows/github-change.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/workflows/github-change.md`
- **R24** — `ROADMAP.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/ROADMAP.md`
- **R25** — `RULEBOOK.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/RULEBOOK.md`
- **R26** — `CONSTITUTION.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/CONSTITUTION.md`
- **R27** — `README.md`: `https://github.com/turkyildiz/Unilogistix/blob/1f77d908f424afffecd556d7244f5c44e655e89d/README.md`

### GitHub live-setting observations

- **Branch:** Final observed head 1f77d908f424afffecd556d7244f5c44e655e89d; protected=false; required checks empty. Endpoint: `https://api.github.com/repos/turkyildiz/Unilogistix/branches/main`
- **Rulesets:** Observed response []. Endpoint: `https://api.github.com/repos/turkyildiz/Unilogistix/rulesets`
- **Actions runs:** Observed total_count=0. Endpoint: `https://api.github.com/repos/turkyildiz/Unilogistix/actions/runs?per_page=5`

### Official technical documentation consulted September 9, 2026

- **S01** — GitHub — GITHUB_TOKEN, workflow-trigger and approval behavior: `https://docs.github.com/en/actions/concepts/security/github_token`
- **S02** — GitHub — Secure use reference: `https://docs.github.com/en/actions/reference/security/secure-use`
- **S03** — OpenBao — Audit devices: `https://openbao.org/docs/audit/`
- **S04** — Python — The assert statement: `https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement`
- **S05** — Google — Email sender guidelines: `https://support.google.com/mail/answer/81126?hl=en`
- **S06** — Supabase — Row Level Security: `https://supabase.com/docs/guides/database/postgres/row-level-security`
- **S07** — Stripe — Webhooks: `https://docs.stripe.com/webhooks`
- **S08** — Stripe — Idempotent requests: `https://docs.stripe.com/api/idempotent_requests`
- **S09** — Cloudflare — Workflows: `https://developers.cloudflare.com/workflows/`

## Bottom line

Build the smallest complete company that can acquire, sell, onboard, serve, bill, support, improve and recover—not the largest agent organization. Every repeated operational dependency needs either an automated, authorized completion path or an explicit unresolved status. Founder/board control must stay independent of the systems executing the work.
