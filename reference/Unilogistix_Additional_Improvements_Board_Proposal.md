# UNI / Unilogistix — Additional Company-Wide Improvements

**Board discussion draft | Supplement to the autonomous-company gap analysis and marketing proposal**

Version: 0.1  
Updated: 2026-09-09  
Status: Recommendations for discussion; not adopted, funded, implemented, or activated by this document  
Prepared for: Ilker Yildiz and the Unilogistix Board  
Repository baseline checked: `a23534e1ffa280adb94221b4c5353f8819a92dc6`  
Scope: Company-wide improvements beyond the marketing operating model

> **Decision boundary:** This document proposes what to improve and how to test it. It does not approve spending, select providers, grant credentials, authorize customer contact, amend company policy, or permit production changes. Board discussion and receipt of the file are not adoption. No repository or live infrastructure changes were made to prepare this document.

## Executive recommendation

**The next improvement is to make UNI behave as one accountable business, not a collection of individually convincing agents.**

The earlier proposals already cover marketing, sales, support, engineering, finance, recovery, and customer-feedback learning. This supplement strengthens the connections between those functions and adds more explicit customer self-service, procurement, economic, and decision-management requirements. It is not another request to create dozens of departments.

The most valuable additions are:

- **Provable outcomes:** The company knows what actually happened, which capabilities are currently verified, and which claims have become stale.
- **Consistent customer treatment:** Sales, marketing, support, billing, and engineering cannot make contradictory decisions about the same customer or commitment.
- **Measured expansion of autonomy:** Each action earns operational eligibility through evidence, while its authority still comes from an authentic mandate.
- **Commercial completeness:** Customers can buy, activate, administer, renew, and leave through supported workflows; attractive revenue is evaluated alongside delivery cost and retained value.
- **Resilience and accountability:** Compound failures are rehearsed, the founder's workstation is not the hidden recovery dependency, and the board receives decisions supported by current evidence.

**Recommended first engineering slice:** one customer lifecycle with a verified outcome record, enforceable cross-department rules, duplicate-event handling, and an independent failure test. Keep the previously proposed durable runtime, action gateway, scoped identities, protected CI/CD, and spending controls as prerequisites—not optional work displaced by this supplement.

## 1. What this review does—and does not—establish

The checked `main` branch points to the baseline above. Its response still reports `protected: false` and no required status checks. This is a GitHub setting observed during this review, not a statement about every possible external build system. [R1]

The AI Operating System book still labels the company runtime an initial specification rather than an implemented service. The dashboard contract similarly defines metrics without claiming live instrumentation or values. [R2] [R3]

The OpenBao document has advanced beyond the older audit: it now reports a disposable restored vault that unsealed and returned the canary, scheduled backups, HTTPS, and scoped read-only provider checks. **Those achievements should not continue to be listed as wholly missing.** However, that same record identifies unfinished replacement-host provisioning and traffic cutover, workstation-dependent recovery, longer-outage re-issuance dependencies, local-only audit retention, and missing external alert delivery. These are repository-reported results and limitations; no live server tests were repeated for this supplement. [R4]

The previous company analysis and marketing proposal were both read for comparison. Their references appear as [P1] and [P2]. The proposals below distinguish deeper implementation detail from additional business requirements. An item described here is **not automatically a newly discovered defect**, and no missing capability is asserted solely because a filename is absent.

Unless explicitly labeled as a repository observation or external technical fact, the following content is a recommendation for board consideration.

## 2. Prioritized improvement map

P0 means a prerequisite for the relevant consequential unattended workflow. P1 means a first-business operating requirement. Priorities are dependency-based, not delivery dates. Proposed roles are responsibilities, not a claim that those AI workers exist.

| ID | Improvement | Priority | Relationship to earlier work | Proposed accountable function |
| --- | --- | --- | --- | --- |
| IMP-01 | Verified capability and outcome records | P0 | Makes UNI-020/027 and MKT-14 evidence rules executable | Assurance / Data |
| IMP-02 | Consistent customer state and enforceable commitments | P0 | Deepens UNI-003/012/014/015/024 beyond handoff records | Customer Operations / Engineering |
| IMP-03 | Action-specific autonomy eligibility | P0 | Refines UNI-001/009/026; separates permission from demonstrated competence | Governance / Assurance |
| IMP-04 | Compound-failure simulation and protected evaluation | P0 | Extends UNI-017/018/026/030 with adversarial lifecycle tests | Independent Assurance |
| IMP-05 | Customer self-service and verified first value | P1 | Expands onboarding and support into a complete customer-controlled experience | Product / Customer Success |
| IMP-06 | Evidence-backed buying and procurement workflow | P1 | Adds a concrete enterprise-purchasing path to the sales proposal | Sales / Assurance |
| IMP-07 | Customer- and product-level economics | P1 | Turns UNI-028 and MKT-10 into pricing, packaging, and cost decisions | Finance / Product |
| IMP-08 | Business-aware work scheduling | P0 | Makes runtime priorities, resource limits, and cost policy enforceable | Operations / AI Platform |
| IMP-09 | Independent end-to-end recovery | P0 | Updates UNI-005/006/019/023 to the newer infrastructure evidence | Reliability / Security |
| IMP-10 | Board decision and operating-evidence system | P1; authority records are P0 | Extends governance/reporting into decision tracking and measurable follow-through | Governance / Intelligence |

Do not open ten new disconnected projects. Attach refinements to existing backlog items, maintain one accountable owner per outcome, and implement the shared primitives once.

## 3. IMP-01 — Require evidence before declaring a capability ready or work complete

### Improvement

Create one capability registry and one business-outcome record format. The registry answers **“What is UNI currently permitted and proven to do?”** The outcome record answers **“What happened in this particular customer operation?”**

The existing dashboard and runtime specifications establish acceptance and evidence requirements, but they do not yet provide live proof. The earlier backlog already proposed capability records; this recommendation defines their use in release eligibility, reporting, and task closure. [R2] [R3] [P1: UNI-020, UNI-027]

### Implementation proposal

A capability record should identify the exact action, product, environment, software/prompt/tool versions, required mandate, test suite, evidence location, verification date, expiry or invalidation triggers, and responsible function. Keep adoption, implementation, deployment, testing, operational eligibility, and observed performance as separate fields. A passing sandbox test must not imply production permission.

A consequential operation should retain its customer scope, state version, authorized intent, external action IDs, receipts, acceptance checks, reconciliation state, cost, and remaining obligations. Preserve auditable decision summaries and source evidence; do not require private model reasoning or put credentials and raw customer records in public GitHub.

Only an independent acceptance path may move the operation to verified completion. An agent's written assertion, a green process exit, or a hash without trusted provenance is insufficient. A hash detects content changes; it does not establish that an event really occurred.

### Example and acceptance

An account setup is not complete because a welcome email was sent. Completion requires the intended account, correct access, and a verified first-use condition. A refund has separate requested, provider-accepted, and reconciled states. A file-delivery task cannot close without a readable artifact at the promised location.

**Test:** Report success without producing the artifact or external receipt. The operation remains unverified. Change a tool version or revoke the mandate; the affected readiness checks invalidate according to policy while historical evidence remains intact. Unrelated capabilities do not lose eligibility merely because an unrelated document changed.

**Tradeoff:** Evidence has storage and execution cost. Apply strong checks to consequential outcomes and lighter validation to reversible internal drafts; do not demand expensive independent model review for every trivial transformation.

## 4. IMP-02 — Give departments one consistent customer lifecycle

### Improvement

A CRM record and a handoff are not enough. Define what must remain true while marketing, support, billing, and engineering operate concurrently.

Use separate but linked dimensions for commercial status, payment state, service entitlement, support incidents, communication preferences, and data obligations. Do not compress them into one vague “active/inactive” field: a customer can cancel renewal while retaining paid service, or request deletion while some records remain subject to an adopted retention rule.

### Implementation proposal

Maintain versioned customer and commitment records with deterministic transition rules. Enforce a single owner for each authoritative entity, transactional updates within the chosen database, and explicit continuation or compensation for external multi-step operations. A compensation is a new corrective action, not a claim that an already-sent email or completed service can be erased.

AWS's saga guidance describes coordination and compensation across services and specifically notes that sagas do not themselves supply transaction isolation. Use this as a design reference, not a recommendation to add AWS or split UNI into many microservices. Keep one transactional store where practical and address external effects separately. [E1]

Proposed invariants include:

| Situation | Invariant to enforce |
| --- | --- |
| Cancellation effective before renewal | No new renewal charge is intentionally initiated under the superseded instruction; reconcile already-started external charges |
| Customer declines promotional contact | Queued promotional sends recheck current eligibility at execution |
| Refund and dispute processes overlap | Reservations and reconciliation prevent disbursements beyond the available eligible amount; conflicts remain visible |
| Sales offers a service level | The offer references an adopted service and pricing version with a responsible fulfillment owner |
| A feature is suspended | New offers and promotions cannot represent it as currently available |
| A customer has multiple open tickets | One root incident can coordinate remedies without deleting individual customer obligations |

Customer requests and agent-generated text are proposed inputs. They do not directly overwrite contractual terms, account authority, or financial state.

### Example and acceptance

**Test:** Deliver a cancellation event, delayed payment webhook, scheduled renewal, and promotional message in different orders, with worker restarts between steps. Each ordering must converge to the correct permitted commercial state, preserve paid entitlements, and retain any unresolved refund or notice obligation.

**Tradeoff:** Some provider actions cannot be stopped after acceptance. Document the cancellation cutoff and reconciliation route. Do not promise instantaneous consistency across all external systems.

## 5. IMP-03 — Grant operational eligibility per action, not per impressive agent title

### Improvement

A worker that can write accurate articles has not demonstrated that it can issue refunds, change pricing, or deploy software. Maintain a capability-level eligibility matrix alongside the authority matrix.

### Implementation proposal

Use the following evidence stages. A board-adopted mandate may preauthorize advancement inside a fixed envelope after independent gates pass; otherwise a wider envelope needs authentic new authority.

| Stage | Permitted behavior under the applicable mandate | Evidence needed to advance |
| --- | --- | --- |
| Observe | Read scoped data and make internal recommendations | Grounded outputs and access-denial tests |
| Simulate | Execute in an isolated environment with test records | Happy-path and failure-path acceptance |
| Bounded live operation | Perform a narrow real action within explicit limits | Verified outcomes, costs, and incident behavior |
| Established operation | Repeat that specific action within its adopted envelope | Representative current evidence and continuing guardrails |
| Suspended or restricted | Stop new affected actions; retain authorized containment | Remediation and requalification under the governing policy |

The effective permission is the intersection of **mandate, identity, resource scope, demonstrated eligibility, current service health, and remaining budget**. None of these creates the others. Self-reported model confidence is not an authorization signal.

A prompt, model, tool schema, permission, or relevant policy change triggers risk-proportionate retesting. Automatic restriction is allowed only through the adopted control design; automatic expansion cannot exceed preauthorized boundaries.

### Example and acceptance

Support might be eligible to provide account-scoped troubleshooting while its refund capability remains in simulation. An engineering worker may build changes but lack release authority. A new model can run as a challenger without becoming the production executor.

**Test:** Attempt to reuse an article-publication qualification to issue a credit. Deny it. Then demonstrate an already-authorized, qualified routine action completing without an extra founder approval. A restricted action stays visibly blocked rather than being silently rerouted to a more privileged worker.

**Tradeoff:** More stages can become bureaucracy. Start with a small set of consequential action classes, not a permission ceremony around every internal sentence.

## 6. IMP-04 — Rehearse compound failures and protect evaluation from the workers being evaluated

### Improvement

Single-component checks do not exercise the hardest company situations: a payment succeeds just as the worker dies, the customer cancels, the model provider fails, and the restored database contains stale pending work.

Build a reusable company test environment with fake customers, test payments, disposable services, controlled faults, and a virtual clock for expiry and recurring obligations. Its scenario runner must not hold production credentials or send real customer messages.

### Implementation proposal

Start with the scenarios below. Preserve event order, timestamps, actions attempted, accounting changes, customer-visible results, and invariant violations so a failure can be reproduced.

| Scenario | Required observable result |
| --- | --- |
| Payment accepted, response lost, worker restarted | Reconciliation finds the original result; no duplicate collection |
| Cancellation races renewal and queued outreach | IMP-02 lifecycle rules hold for each event order |
| Provider token expires during an incident | Authorized recovery or an explicit contained failure; no privilege escalation |
| A bad release also degrades internal monitoring | Independent customer-path checks detect the impact |
| Restored state predates completed external actions | Recovery reconciles external effects before resuming execution |
| Malicious content enters a ticket or retrieved document | No change to authority, recipients, secrets, or protected tests |
| Acquisition load increases while support falls behind | Bounded admission and resource policy preserve existing obligations |
| Work continues after a mandate is revoked | New consequential actions are blocked, including queued actions |

Maintain a protected evaluation set separate from the builder's ordinary fixtures. Do not let the same actor generate the only tests, edit the pass criteria, grade the result, and approve deployment. A second model can contribute diversity of review, but a different model name alone does not establish independent permissions or a trustworthy test oracle.

OWASP recommends scoped tools, separation of decisions from irreversible execution, bounded tool chains, and structured adversarial testing. It also recommends human oversight for high-impact actions. This proposal does not claim OWASP endorses a blanket no-human design: preserve genuinely reserved board actions and exclude activities whose required oversight cannot be satisfied. [E2]

### Acceptance and limitations

**Test:** Insert known failures, false success messages, and an attempt to weaken the evaluator. The protected suite rejects the result and preserves evidence. A simulated thirty-day cycle must be labeled simulated; it is not thirty days of observed customer operation.

Use real provider sandboxes and contract checks to validate important simulator assumptions. Simulation can expose defects; it cannot establish real demand, certification, permanent reliability, or compatibility with every future provider change.

## 7. IMP-05 — Give customers a complete self-service experience and measure first value

### Improvement

Do not make a conversation with an AI the only way to buy, change settings, understand a charge, or obtain support. Provide direct, understandable controls for standard customer actions, with AI assistance as an additional path.

The marketing proposal already links acquisition to activation. This addition specifies the customer-facing product experience and the evidence needed to distinguish activity from value. [P2: sections 7–8]

### Implementation proposal

The first supported product should have a coherent journey for plan comparison, purchase or trial, account setup, supported data/device connection, first useful outcome, account administration, billing history, support, renewal, cancellation, and appropriate export or deletion requests. Use clear transaction status and identity checks for sensitive operations. Test keyboard access, error recovery, mobile behavior, and authorization—not just the happy-path screenshot.

Define first value per product. For a future authorized tracking offering, it could be receipt and correct account-scoped display of an enrolled test device's fresh position. Login or receipt of a welcome email would not be enough. Any live device, location collection, or installation remains subject to its own mandate and physical dependencies.

Measure time to first value, completion by onboarding step, recurring useful activity, and the reasons a customer stalls or leaves. Offer permitted in-product guidance, a reversible repair, or a supported alternative. Customers who do not submit tickets must not disappear from the learning process; use permitted telemetry and voluntary feedback, not intrusive profiling or fabricated interviews.

### Acceptance and tradeoff

**Test:** A new customer can reach the declared first-value event and later cancel renewal without UNI's founder, a manual sales representative, or an AI inventing an unsupported workaround. Broken setup is visible as incomplete and triggers bounded recovery.

Keep the first portal narrow. A technically honest product with a few excellent workflows is preferable to a broad dashboard filled with inactive buttons or inaccurate success states.

## 8. IMP-06 — Automate evidence-backed buying and procurement, not just lead generation

### Improvement

Extend sales beyond answering product questions. Support the practical buying steps an approved target customer may require: quotations, security questions, standard terms, billing arrangements, product demonstrations, and implementation scope.

This is an additional operating specification; the review did not inspect actual customer procurement requests or determine which requirements apply to UNI's first market.

### Implementation proposal

Build a versioned commercial and assurance packet from authoritative records: released capabilities, supported interfaces, data handling, service boundaries, incident communication, pricing, approved contract templates, and any legitimately applicable certifications or attestations.

Every answer to a procurement question should carry its supporting source, scope, version, review date, and confidence category: verified fact, adopted commitment, proposal, or unknown. Restrict non-public evidence to authenticated recipients. The commercial agent must not answer “yes” to controls that are merely planned or reuse another company’s certifications as UNI’s own.

Use a contract-deviation workflow. Matching an adopted standard offer can be routine. Changes outside approved liability, service, geography, data, or financial boundaries remain proposals. An unfamiliar legal clause is not resolved simply because a model sounds confident. Determine the applicable professional or account-owner requirements for the specific action before activation; record nondelegable dependencies honestly.

### Acceptance and tradeoff

**Test:** Submit a procurement questionnaire mixing supported controls, planned controls, and one requested guarantee outside delegation. Produce evidence-backed answers, label gaps accurately, and decline to create the unauthorized commitment. A standard authorized buyer should still complete the standard purchasing path without the founder acting as a salesperson.

Do not build a large compliance portal before confirming the target market needs it. Start with an accurate reusable evidence packet and one standard quote-to-order workflow.

## 9. IMP-07 — Manage economics by product, customer cohort, and service obligation

### Improvement

Revenue and low token prices are not sufficient operating measures. Extend the cost policy into product packaging, account-level resource economics, and decisions about what to scale.

The repository already calls for total cost per verified outcome, including retries, review, infrastructure, and recovery. This proposal operationalizes that requirement rather than claiming it is absent. [R5]

### Implementation proposal

Track costs by product and business operation, then allocate shared costs consistently. Show direct cash expenditure, allocated operating cost, revenue assumptions, actual receipts, and outstanding obligations separately. Include support, refunds, model calls, repeated attempts, data transfer, storage, and the relevant delivery or hardware costs.

For internal product decisions, use a clearly defined contribution view:

```text
Cohort contribution before acquisition
  = defined net revenue for the cohort
  - attributable delivery and service costs

Cohort contribution after acquisition
  = contribution before acquisition
  - consistently allocated acquisition costs
```

These are proposed management metrics, not a selected jurisdiction-specific accounting treatment. Publish the definition, time window, allocation basis, and immature-cohort limitations. Do not count the same shared expense twice or present a projected lifetime value as collected cash.

Evaluate plan limits, packages, supported use cases, and new-customer offers against observed cost and value. Pricing experiments require adopted boundaries, customer notice where appropriate, and stable existing commitments. Do not silently reprice existing customers or deny owed support because a cost model labels them unprofitable.

### Acceptance and tradeoff

**Test:** A campaign generates revenue but attracts high-cost, low-retention customers. The business identifies the loss-making pattern, constrains new exposure inside its mandate, and proposes a better offer or target segment while continuing existing obligations.

Initially use a few explainable cost categories. Excessively detailed allocation can cost more than the decision it improves. Missing cost data should show uncertainty, not fictional margins.

## 10. IMP-08 — Schedule work by business urgency and customer impact

### Improvement

Implement an operational scheduler, not just a list of tasks routed to executive personas. It should prevent unlimited retries, duplicate research, resource starvation, and several agents simultaneously “fixing” the same incident.

### Implementation proposal

Within adopted safety and authority rules, prioritize active incidents and funded customer obligations, then deadlines and renewals, ordinary service, and bounded discretionary experiments. Provide reserved capacity and aging rules so lower-volume customers and routine work are not indefinitely starved.

Each workflow should have an execution deadline, cost and tool-call limit, maximum concurrent attempts, owner lease, and a defined recovery route. Propagate a shared operation budget through child tasks: spawning more workers must not create more spending authority.

Deduplicate shared investigations while preserving distinct tickets and deadlines. A new worker can take an expired lease, but its writes should use a version or fencing check so an old worker cannot later overwrite the new result. Cache only permitted, appropriately scoped content; never rely on cached authority when revocation must be current.

Use deterministic code for straightforward validation and calculations, and evaluated models for tasks that need language or reasoning. The cost policy already advocates that division. Do not remove independent checks to make a cost dashboard look better. [R5]

### Acceptance and tradeoff

**Test:** Flood the system with a bounded research campaign while an existing customer's service fails and a funded renewal becomes due. Essential work gets capacity, the research operation stays within its total budget, and no task disappears. A repeated repair failure terminates or changes strategy according to policy instead of looping forever.

Avoid an opaque single “business value” score that can trade away privacy, mandatory duties, or promised service. Hard constraints are enforced first; optimization operates inside them.

## 11. IMP-09 — Recover the customer service independently of the founder's workstation

### Improvement

Move from “a vault snapshot restored successfully” to “the approved business service can recover, reconcile, and resume after losing its normal host and control environment.”

The latest vault record reports valuable progress but explicitly leaves host replacement and cutover unautomated, identifies a workstation recovery dependency, and notes that a local health timer cannot report complete failure of its own host. It also says provider credentials retain their original provider-side scope: a read-only checker is not a production write gateway. [R4]

### Implementation proposal

Maintain a private dependency and failure-domain inventory for identity, orchestration, databases, networking, monitoring, and customer service. Choose approved recovery placement from suitable existing resources; “already owned” does not establish spare capacity or independent failure domains.

Provide external missing-heartbeat and customer-path checks, protected off-host evidence, and a tested replacement-and-cutover runbook. Map each alert to an accountable response rather than merely producing journal output. Preserve an authenticated board suspension route and ensure automated recovery does not undo an intentional suspension.

Use service-level objectives to decide urgency and growth/release restrictions. An error budget is an adopted allowance for service failures, not money and not permission for privacy or security violations. Google's SRE guidance discusses burn-rate alerting and the special care needed for low-traffic services; calibrate targets to UNI's actual product rather than copying arbitrary thresholds. [E3]

The recovery proof should cover identity re-establishment, restore, external-action reconciliation, customer-path verification, traffic cutover, and resumption inside the same mandate. Test prolonged credential expiry. Do not achieve apparent independence by putting all recovery shares and administrator credentials inside an ordinary agent's trust domain.

### Acceptance and tradeoff

**Test:** In an isolated exercise, make the normal host and founder workstation unavailable. Independent monitoring detects the failure. The authorized recovery path rebuilds the needed environment, verifies customer service, and does not repeat an already completed payment or notification. Record recovery time and potential data loss against adopted objectives.

Redundancy increases cost and operational complexity. Start with one tested recovery path, not active deployment to every available provider. Where a step remains nondelegable, expose the dependency and do not claim that workflow is fully autonomous.

## 12. IMP-10 — Give the board decisions and evidence, not a stream of agent narration

### Improvement

Make governance an authentic decision system with measurable follow-through. The board should receive strategic choices and material exceptions, not routine tickets relabeled as governance or long summaries without verifiable results.

The existing venture policy already requires demand, economics, reliability, autonomy, and transfer evidence before graduation. This recommendation turns that into a usable decision packet and preserves the distinction between operating performance and business viability. [R6]

### Implementation proposal

For each material proposal, produce a concise record of the problem, recommendation, alternatives including no action, supporting evidence, uncertainty, one-time and recurring cost, customer obligations, expected benefit, decision deadline, and exact requested scope. Do not invent deadlines or claims of urgency.

After an authenticated decision, store its adopted version, effective period, scope, conditions, and supersession links. Link implementation and outcome measurement to that decision. An agent-written summary of what it believes the board intended is not independent approval.

Maintain separate status for:

| Dimension | Board question |
| --- | --- |
| Authority | What is actually authorized, until when, and under what conditions? |
| Capability | What can the system currently perform, supported by which tests? |
| Operations | What succeeded, failed, or remains overdue? |
| Economics | What customer value, cost, cash exposure, and retention were observed? |
| Learning | Which changes improved results, failed, or remain uncertain? |

The periodic report should show changed facts, decisions made inside delegation, expiring authority, unresolved obligations, material risk, and proposals requiring genuine board action. Include negative results and forecast-versus-actual comparisons.

### Acceptance and tradeoff

**Test:** Give the system an ordinary in-scope support problem and a proposal requiring new capital authority. The first follows operational recovery without a board approval request; the second produces a bounded decision packet without spending. An overdue or rejected proposal must not be silently treated as approved.

Avoid a dashboard that aggregates everything into a misleading single “autonomy score.” A technically independent but unviable business and a profitable business needing daily founder repairs are different problems.

## 13. One integrated example

This is a hypothetical demonstration, not a released Safe Goes capability, current customer incident, or approved product launch.

An authorized customer starts a trial, connects a supported test device, and reaches the first-value event. The product records the outcome, and marketing receives only the permitted attribution event. Sales uses the current approved offer rather than generating a new service promise.

The customer later reports duplicated alerts. Support links the ticket to a reproduced issue; the scheduler gives the incident appropriate priority while preserving billing and other customer deadlines. Engineering proposes a fix, and independent tests check duplicate suppression, latency, and account isolation. The author cannot remove those checks to pass.

During the exercise, the worker crashes after the test payment provider accepts a transaction. Recovery reconciles the external result before retrying. Meanwhile, the customer cancels renewal. Billing, service entitlement, and queued messages apply the current customer state rather than separate departmental guesses.

The product improvement rolls out under an existing valid mandate only after the relevant gates pass. Its cost and customer outcome appear in the operating record. The board receives a factual summary and any genuine strategic proposal—not a request to send the email, inspect the payment, deploy the fix, or repair the worker.

This scenario is successful only when the customer, financial, operational, security, and autonomy outcomes all meet their adopted criteria. A passing simulation demonstrates the scenario, not an entire permanently autonomous company.

## 14. Implementation sequence

The following are deliverable gates, not calendar promises or new authorizations.

| Gate | Deliverable | Exit evidence |
| --- | --- | --- |
| A — Define the contract | One selected customer lifecycle; outcome schema; state invariants; authority and eligibility rules | Missing authority and unsupported outcomes are rejected in local tests |
| B — Connect the operating slice | Durable workflow, scoped actions, authoritative records, protected CI, cost accounting | One complete sandbox lifecycle with consistent events and acceptance evidence |
| C — Break and recover it | Compound-failure runner and independent monitoring/recovery | Duplicate, reordered, expired, compromised-input, and host-loss cases meet defined criteria |
| D — Remove customer friction | Narrow self-service experience and approved commercial packet | Standard customers can activate and administer the product; answers and offers remain grounded |
| E — Observe a bounded business | An explicitly authorized live pilot with economic, service, and autonomy metrics | Representative live outcomes, visible unresolved work, and no hidden operational human execution |
| F — Improve and replicate selectively | Evaluated process/product improvements and reusable tested modules | Another workflow or venture inherits controls without inheriting private data or unjustified readiness |

Do not wait until every dashboard and commercial feature is built to test the operating slice. Conversely, do not activate paid acquisition, customer writes, or production releases merely because a sandbox flow works.

## 15. Proposed first acceptance contract

This is a **design sketch**, not an implemented schema, approved mandate, or production configuration. Its authority fields are deliberately unset and live execution is disabled.

```yaml
operation_contract:
  version: "0.1-proposed"
  status: proposed
  operation_type: customer_onboarding
  environment: sandbox
  product_id: null
  customer_scope: isolated_test_account
  authority:
    authenticated_mandate_reference: null
    adopted_policy_version: null
    live_execution_enabled: false
  required_evidence:
    - current_account_authorization
    - accepted_supported_offer_version
    - verified_first_value_event
    - reconciled_test_payment_state_if_applicable
    - remaining_obligations_record
  invariants:
    - customer_data_remains_account_scoped
    - repeated_delivery_does_not_repeat_external_effects
    - no_unsupported_offer_or_entitlement
    - revoked_authority_blocks_new_consequential_actions
  limits:
    total_operation_cost_cap: null
    execution_deadline: null
    maximum_attempts: null
  failure_policy:
    reconcile_unknown_external_results: true
    preserve_customer_obligations: true
    log_operational_human_asks: true
    treat_safe_pause_as_verified_success: false
  completion:
    independent_acceptance_required: true
    require_evidence_provenance: true
```

Before execution, replace unset values with genuinely adopted and validated configuration appropriate to the environment. Test the schema and enforcement in code. Copying this block into the repository does not create a control.

## 16. Decisions for board discussion

All entries below are **Not decided**. Approval of a general direction does not automatically approve every implementation, account, budget, or live-use setting.

| Decision | Recommendation | Outcome to record | Status |
| --- | --- | --- | --- |
| BD-IMP-01 — First integrated lifecycle | Choose one supported customer problem and the complete workflow to demonstrate | Product, scope, first-value definition, exclusions | Not decided |
| BD-IMP-02 — Evidence standard | Require current provenance and verified outcomes for consequential completion | Acceptance rules, owners, evidence retention and freshness | Not decided |
| BD-IMP-03 — Autonomy eligibility | Qualify specific action classes within standing mandates | Action matrix, promotion gates, restrictions and revocation | Not decided |
| BD-IMP-04 — Failure exercises | Adopt isolated compound-failure testing before broader live authority | Scenarios, isolation, resource limits and test ownership | Not decided |
| BD-IMP-05 — Customer and buying experience | Provide a narrow self-service journey and accurate standard commercial packet | Supported transactions, standard terms, customer controls | Not decided |
| BD-IMP-06 — Economic and scheduling limits | Protect existing obligations while bounding discretionary experiments | Cost definitions, capacity reserves, priorities and caps | Not decided |
| BD-IMP-07 — Independent recovery | Remove critical founder-workstation dependency in the approved recovery scope | Recovery objectives, resources, trust boundary and remaining exceptions | Not decided |
| BD-IMP-08 — Operating review and expansion | Keep authority, capability, performance and viability separate | Report cadence, observation criteria and expansion conditions | Not decided |

The board may adopt, amend, reject, or defer each item. Record the authentic decision and exact version. A blank field means unresolved, not unlimited permission.

## 17. Documentation placement and maintenance

Suggested discussion-copy location, subject to the repository's review process:

`decisions/proposals/company-wide-improvements-2026-09-09.md`

After disposition, place adopted requirements in their canonical books or policies rather than maintaining several competing copies. Link implementation items and evidence from the roadmap and capability registry. Preserve the original blueprint and historical proposals without silently rewriting their past observations.

| Canonical area | Proposed addition |
| --- | --- |
| AI Operating System | Customer-state transitions, outcome contracts, eligibility checks and work scheduling |
| Business Operations | Self-service, buying workflow, commitments and customer economics |
| Knowledge / Evolution | Protected evaluation, provenance, experiment outcomes and change-triggered requalification |
| Engineering / Infrastructure | Compound-failure tests, independent monitoring and replacement recovery |
| Dashboards | Evidence freshness, outcome validity, lifecycle conflicts, customer value and cost |
| Governance / Venture lifecycle | Authentic decision packets, exact delegation and evidence-based expansion |

Document status should be derived from current evidence where possible. A test that expired, a revoked identity, or an uncompleted recovery drill must remain visible. The aim is fewer unsupported statements—not more documentation for its own sake.

## 18. Sources and evidence notes

### Prior discussion artifacts

**[P1]** *Unilogistix: autonomous-company gap analysis and implementation backlog*, September 9, 2026, supplied Markdown artifact `Unilogistix_Autonomous_Company_Gap_Analysis.md`. Its reviewed commit was `1f77d908f424afffecd556d7244f5c44e655e89d`. UNI identifiers in this supplement refer to that artifact; older infrastructure observations are superseded where the newer evidence states otherwise.

**[P2]** *UNI / Unilogistix — Autonomous Marketing & Growth Operating Model*, version 0.1, September 9, 2026, supplied Markdown artifact `Unilogistix_Autonomous_Marketing_Board_Proposal.md`, baseline `a23534e1ffa280adb94221b4c5353f8819a92dc6`. Its MKT identifiers and board decisions remain proposals, not assumed approvals.

### Repository sources

Sources R2–R6 are pinned to the checked baseline. They establish what the repository says, not independent live verification. R1 is the branch endpoint observed for this review and can subsequently change.

- **[R1] Main branch metadata:** https://api.github.com/repos/turkyildiz/Unilogistix/branches/main
- **[R2] AI Operating System:** https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/books/BOOK-02-AI-OPERATING-SYSTEM/README.md
- **[R3] Dashboard and KPI contract:** https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/dashboards/README.md
- **[R4] OpenBao foundation, version 0.3:** https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/infrastructure/openbao/README.md
- **[R5] Cost-efficient autonomous operations:** https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/policies/cost-efficiency.md
- **[R6] Venture lifecycle and replication:** https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/policies/venture-lifecycle.md

### External primary technical references

Consulted September 9, 2026. These support the specifically cited design principles; they do not certify UNI or establish that any proposed control is deployed. No provider selection is implied.

- **[E1] AWS Prescriptive Guidance — Saga orchestration pattern:** https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga-orchestration.html
- **[E2] OWASP Cheat Sheet Series — AI Agent Security:** https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
- **[E3] Google Site Reliability Engineering Workbook — Alerting on SLOs:** https://sre.google/workbook/alerting-on-slos/

## Change history

- **0.1 — 2026-09-09:** Prepared ten company-wide improvement proposals for board discussion, mapped them to the earlier company and marketing backlogs, updated the infrastructure baseline, and added implementation gates, acceptance criteria, a disabled example contract, and eight undecided board items. No live actions, repository modifications, or approvals were performed.

---

**Bottom line:** Build a company that can demonstrate a consistent customer outcome, detect when its own claims are wrong, recover within authentic authority, and learn which activities create durable value. More agents, more content, and more dashboards are useful only when they improve those results.
