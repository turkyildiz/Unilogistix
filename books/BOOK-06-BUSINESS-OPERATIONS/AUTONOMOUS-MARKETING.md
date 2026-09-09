# UNI / Unilogistix — Autonomous Marketing & Growth Operating Model

**Business-instance marketing operating model — discussion draft**

Version: 0.2  
Updated: 2026-09-09  
Status: Proposed documentation update; not adopted or activated  
Prepared for: Founder governing Unilogistix and authorized business-instance governance  
Scope: Autonomous marketing and its connections to sales, onboarding, support, finance, engineering, and customer-feedback learning  
Repository baseline reviewed: `a23534e1ffa280adb94221b4c5353f8819a92dc6`

## Current identity and document status

Unilogistix is the reusable AI operating framework and will never be an actual
company. This marketing function runs inside each actual business's dedicated
instance, under that business's identity and mandate. LondonRue, a towel business,
is the founder's example. References below to company finance, customer accounts,
board decisions and operations refer to the relevant business, not an incorporated
Unilogistix parent.

The founder has confirmed the business-instance model and the learning loop from
business outcomes into Unilogistix upgrades and future businesses. Detailed marketing
rules, numerical limits and activation settings below remain proposals. Today is
documentation only. Future implementation backlogs describe intended capabilities,
not work authorized for today or evidence of live operation.

This version adapts the [supplied discussion draft](../../reference/Unilogistix_Autonomous_Marketing_Board_Proposal.md).
Its repository observations remain historical observations at the cited commit.
See the [system model](../../governance/SYSTEM_AND_BUSINESS_MODEL.md) and
[business-to-framework CI/CD workflow](../../workflows/business-to-framework-learning.md).

## Executive recommendation

Build marketing as an AI-operated acquisition and retention function, not a content-generation queue. Its job is to identify suitable customers, communicate verified value, attract and convert prospects, and improve results using customer and business outcomes.

The proposed operating loop is:

**Research → positioning → campaign → independent verification → distribution → sales → onboarding → customer outcomes → learning → improved campaign or product.**

The founder and board determine business direction, capital authority, material commitments, and reserved decisions. Within an adopted mandate, UNI performs ordinary marketing work without asking the founder to write content, choose every headline, approve every post, adjust campaigns, or repair routine integrations.

Start with one product, one defined audience, and one primary acquisition channel. Establish the customer journey, spending controls, support connection, and measurement before adding channels. A useful first milestone is not “100 posts published.” It is one auditable customer journey from acquisition through payment, support, and an evidence-backed improvement.

## 1. Current foundation and scope of this proposal

The reviewed Business Operations book already connects research, acquisition, sales, onboarding, service, support, and renewal. It assigns marketing responsibility for substantiated positioning and directs the business to pause acquisition when service or funded obligations cannot support growth. It identifies its runtime as not implemented. [S1]

The reviewed product-and-customer policy covers truthful marketing, approved budgets and markets, customer identity checks, support remedies, and restrictions on customer-data reuse. These are documented requirements, not proof of connected operational systems. [S2]

The reviewed integration inventory lists CRM, support, marketing, billing, and accounting as workflow requirements whose providers/accounts are not selected. That is the documented status in the inspected file; this proposal does not independently certify every external account or deployment. [S3]

The evolution book specifies measured experiments, independent evaluation, controlled rollout, and rollback. The autonomy policy requires honest accounting of human asks, human execution, blocked work, and verified completion. [S4] [S5]

This proposal turns those principles into a concrete marketing operating contract. It does not repeat the previous company-wide audit, claim that missing infrastructure has been deployed, or assume that an earlier infrastructure finding still applies.

Unless a paragraph explicitly describes the reviewed repository and cites a source, the designs, controls, milestones, and acceptance criteria below are **recommendations for board consideration**.

## 2. Definition of successful autonomous marketing

Marketing succeeds when it brings in customers the company can serve, helps them reach meaningful product outcomes, and contributes to sustainable economics within authorized limits.

Autonomy means ordinary internal marketing operations complete without human diagnosis, decision-making, execution, or repair. It does not mean suppressing questions while leaving work unfinished. The existing autonomy policy treats safe pauses as unresolved or failed operations rather than successes. [S5]

Customer choices, such as selecting a plan or declining an offer, remain customer inputs. Genuine account-owner authorization or external-provider dependencies must be recorded. Do not hide routine human work by labeling it a board decision or outsourcing it to an undisclosed human operator.

Measure both outcome quality and independence. A functioning publishing bot with no customer conversion is not a complete marketing department. An apparently successful campaign that depends on the founder manually handling every prospect is not an autonomous customer lifecycle.

## 3. Board authority and standing operating mandates

### 3.1 Proposed division of decisions

| Decision | Proposed owner | Boundary |
| --- | --- | --- |
| Mission, material market expansion, total capital authority | Founder/board | Recorded governance decision |
| First product and customer segment | Board adopts scope; AI research proposes evidence | No launch inferred from a candidate brief |
| Messaging, headlines, scheduling, ordinary experiments | AI growth lead | Within adopted product claims, channel scope, and budget |
| Campaign publication | Distribution service after verification | No routine founder approval inside valid delegation |
| Budget reallocation | AI growth and finance | Only within explicitly delegated campaign and period limits |
| Discounts and offers | AI sales/growth | Approved pricing and commitment rules |
| Containment of harmful or broken campaigns | AI operations/growth | Preauthorized pause and withdrawal controls |
| Increased spending authority or materially broader commitments | Founder/board | No self-issued mandate or implicit approval |

A mandate should remain valid long enough for ordinary operations to proceed, while defining expiry, revocation, renewal, and funded continuity. Board unavailability never expands agent authority.

### 3.2 Illustrative mandate template

The following is a configuration sketch, not an executable authorization or a signed resolution. Missing required values must block live activation.

```yaml
mandate:
  id: null
  status: proposed
  adopted_resolution_id: null
  authenticated_approval_reference: null
  product_id: null
  objective: Acquire and retain suitable customers within adopted limits
  customer_segments: []
  permitted_markets: []
  permitted_channels: []
  permitted_account_ids: []
  approved_claim_set_version: null
  approved_offer_policy_version: null
  budget:
    currency: null
    period: null
    total_cap: null
    per_campaign_cap: null
    per_action_cap: null
    reporting_delay_reserve: null
    essential_continuity_reserve: null
  measurement:
    activation_definition: null
    cohort_window: null
    target_metrics: {}
    guardrail_thresholds: {}
    minimum_evidence_rule: null
  valid_from: null
  expires_at: null
  revocation_reference: null
  operational_recovery_policy: null
  data_and_communication_policy_reference: null
  live_activation: false
```

The implementation must validate the authenticated approval, exact policy version, account scope, remaining funds, and revocation state when an action executes—not just when an agent plans it.

## 4. Department responsibilities and independence

Use the smallest set of workers that covers the required responsibilities. These are roles, not a requirement for a permanently running model instance per title.

| Function | Accountable responsibility | Required output |
| --- | --- | --- |
| AI growth lead | Acquisition strategy, prioritization, campaign portfolio | Bounded plans and measured decisions |
| Research | Customer problems, alternatives, channel evidence | Dated findings, uncertainty, and counterevidence |
| Brand and creative | Positioning, copy, visuals, demonstrations | Versioned assets linked to substantiated claims |
| Independent assurance | Claims, offers, audience rules, privacy, quality | Evidence-backed acceptance or rejection |
| Distribution operations | Publication, scheduling, delivery reconciliation | External receipts and verified live assets |
| Sales and customer success | Qualification, approved offers, activation | Accepted handoffs and customer outcomes |
| Support and product | Resolve problems and identify improvement needs | Tickets, evidence, priorities, verified fixes |
| Finance | Budget reservations, spending reconciliation, economics | Authoritative exposure and cost records |
| Analytics | Attribution, cohorts, experiments, reporting | Reproducible metrics with limitations |
| Engineering and operations | Reliable integrations, deployment, recovery | Tested releases and service evidence |

The creator cannot approve its own material claims or change protected verification rules to get a campaign released. Reviewers need distinct execution contexts and appropriately separated permissions. Deterministic controls enforce authority and spending; an AI review alone is not authorization.

## 5. The complete campaign lifecycle

### 5.1 Research and positioning

Research begins with a customer problem, not a publishing quota. Record the audience, purchasing role, problem, alternatives, source dates, likely objections, and confidence. Separate observations from assumptions.

Use permitted customer feedback and aggregated product outcomes to refine the audience. Do not reuse confidential information from another venture or customer merely because it is accessible to a model.

Maintain an approved product-and-brand library containing released capabilities, supported use cases, current pricing, service commitments, demonstration assets, and permitted brand materials. Unsupported future features remain proposals and must not be advertised as available.

### 5.2 Experiment and asset creation

Each campaign defines a hypothesis, audience, offer, channel, primary metric, guardrails, budget, observation window, and stopping rule before launch. Record why the experiment is worth running and what uncertainty it addresses.

Generate the required landing page, copy, visuals, email, or demonstration. Assets carry versions and dependencies on claim, pricing, and product-release records. A changed product claim should identify every affected live asset.

### 5.3 Verification and activation

Check factual support, offer validity, working links, form behavior, accessibility, audience eligibility, permitted tracking, and customer communication preferences. Confirm that the destination product and support service are operational.

Publication requires a valid mandate, accepted asset version, healthy connector, sufficient reserved budget, and current service-capacity signal. Stale mandatory checks block new activation.

### 5.4 Distribution and follow-through

Create a stable external-action identity before publishing or sending. Store the provider receipt and confirm the result. When a timeout leaves success uncertain, reconcile before retrying.

A lead enters CRM with its permitted contact preferences and source. Sales qualifies and uses approved offers. Customer success owns onboarding. Support receives problems. Finance reconciles payments. Marketing receives permitted outcome events, not unrestricted access to private conversations or financial accounts.

### 5.5 Evaluation and retirement

Evaluate mature outcomes against the declared hypothesis. Continue, revise, stop, or scale within existing authority. Preserve unsuccessful experiments and costs.

Retiring a campaign includes stopping schedules and spend, handling already-received inquiries, correcting obsolete public assets where possible, and retaining required evidence. Irreversible actions, such as an email already sent, require truthful correction or remediation rather than a fictitious rollback.

Proposed state progression:

`draft → research-ready → planned → assets-ready → verification → authorized → scheduled → live → evaluating → continued / revised / paused / retired`

Rejected, blocked, failed, and cancelled outcomes remain visible. A pause does not count as completed customer acquisition.

## 6. Channel operating requirements

Do not assume that a configured tool proves account authorization, permissible automation, or reliable publishing. Before activation, verify the selected provider's current official requirements and the actual granted permissions. This document deliberately does not select vendors or prescribe unverified platform-specific settings.

### Owned website and search content

Produce useful product pages, explanations, comparisons, and documentation grounded in actual capabilities. Website changes pass through testing and controlled deployment. Validate forms, campaign tags, permitted analytics, mobile behavior, and truthful error states.

Avoid volume targets that reward repetitive or low-value pages. Maintain ownership, freshness dates, and retirement triggers for live content. Search discovery and commercial success are not guaranteed by publication.

### Social channels

Use approved company accounts and supported interfaces. Adapt assets to each channel, verify publication, monitor relevant responses, and route customer issues to support. Do not fabricate identities, endorsements, conversations, engagement, or partnerships.

Failed authorization should pause the affected channel and open remediation. Do not evade provider restrictions with substitute accounts, concealed automation, or access-control bypasses.

### Email and lifecycle communication

Implement authenticated sending, permitted audience selection, purpose-specific communication preferences, unsubscribe processing, suppression, bounce handling, complaint monitoring, and delivery reconciliation.

Recheck eligibility at send time, including queued messages. Keep essential service communication separate from promotional communication. Do not add promotion to an essential notice to evade a customer's preferences.

Before activation, establish the applicable market and provider requirements. A prospect submitting a support request does not automatically become eligible for marketing.

### Paid acquisition

Use a separately scoped advertising identity and an adopted budget. Account for delayed reporting, taxes, fees, and uncertain committed spend. Stop new exposure when financial data is unreliable or the remaining authority cannot cover worst-case authorized commitments.

Provider budget controls are a second layer, not a substitute for the company's ledger and reconciliation. Where a provider does not support a true hard cap, document the exposure and adopt a conservative limit or exclude that channel.

### Partnerships, referrals, and direct outreach

Treat these as optional later workflows. Approved terms, contact eligibility, attribution, and fulfillment ownership must exist before activation. A negotiated commercial commitment outside delegated terms goes to the board. No commission, referral promise, affiliate relationship, or data sharing is implied by this proposal.

## 7. Customer journey and departmental handoffs

Use a connected journey:

**Campaign → prospect → qualified opportunity → offer → signup → activation → payment → continued value → renewal, cancellation, or recovery.**

Every handoff needs a receiving owner, acceptance criteria, deadline, status, and evidence. A sent message does not prove the receiving function accepted the work.

| Handoff | Information passed | Verified result |
| --- | --- | --- |
| Marketing to sales | Product, source, permitted contact details, need, consent/preferences | Qualification completed or an explicit disqualification |
| Sales to onboarding | Accepted terms, product scope, account identity, first-value objective | Customer reaches the defined activation event |
| Customer to support | Ticket, identity, product context, severity | Appropriate verified remedy or visible unresolved obligation |
| Support to product | Reproduced defect or documented unmet need | Prioritization decision with rationale |
| Product to engineering | Requirement, scope, acceptance test, authority | Reviewed and tested change |
| Engineering to marketing | Verified release and supported claim changes | Accurate updated assets and eligible customer follow-up |
| Finance to analytics | Reconciled payment, refund, cost, and liability events | Reproducible economic reporting |

Marketing must pause or narrow acquisition when it would send customers into a broken signup flow, unavailable feature, unsafe service condition, unmanageable support backlog, or unfunded obligation. The adopted mandate supplies numeric thresholds and recovery conditions.

## 8. Support-driven learning and CI/CD

### 8.1 Diagnose the right problem

A complaint may reveal misleading messaging, confusing onboarding, a product defect, an unsupported use case, or misuse. These require different remedies.

Marketing corrects inaccurate expectations. Customer success improves onboarding. Support handles the affected customer. Product and engineering own supported product changes. No department may solve the appearance of a problem by hiding tickets, deleting criticism, or promising an unreleased fix.

### 8.2 Three controlled learning paths

| Learning path | What changes | Required gate |
| --- | --- | --- |
| Knowledge | FAQs, product explanations, troubleshooting guidance | Verified source, scope, freshness, retrieval tests |
| Operating process | Prompts, model routing, campaign procedures | Held-out evaluations, cost and safety comparison, controlled rollout |
| Product | Features, usability, performance, reliability | Reproduction, acceptance tests, independent review, release verification |

Feedback is evidence, not authority. Customer text cannot change budgets, access rights, protected tests, or board identity. Do not train on raw customer messages or share them across ventures without the required authorization and data controls.

### 8.3 Feedback-to-release workflow

`intake → privacy filtering → deduplication → diagnosis → hypothesis → prioritization → test → implementation → independent evaluation → controlled release → outcome measurement → customer follow-up`

Prioritization considers affected customers, severity, reproducibility, expected benefit, effort, cost, and strategic scope. Urgent security or service failures take an incident route rather than waiting for a marketing experiment.

Code and website changes should move through issue, branch, checks, independent verification, immutable artifact, staging, controlled release, and monitoring. Builders must not modify trusted release gates to approve themselves. Verify that automated work can trigger the required checks without routine human approval while preserving protected boundaries.

A released fix becomes a marketing claim only after the actual capability is verified. Marketing cannot announce a planned improvement as completed.

## 9. Data, integrations, and reliable execution

### 9.1 Minimum authoritative records

| Record | Minimum useful fields |
| --- | --- |
| Campaign | ID, product, owner, hypothesis, audience, mandate, budget, state, dates |
| Asset | ID, version, type, claims, product release, reviewer, publication destinations |
| Claim | Statement, evidence, permitted scope, source date, expiry, supersession |
| Contact eligibility | Identity, purpose, source, preferences, effective time, suppression state |
| Customer journey | Customer/account ID, permitted source association, activation and outcome references |
| External action | ID, idempotency key, authority, payload hash, attempt, receipt, reconciliation state |
| Experiment | Hypothesis, cohort, baseline, primary/guardrail metrics, decision rule, results |
| Feedback | Sanitized evidence, product scope, classification, issue, disposition, follow-up |
| Obligation | Owner, due date, dependency, authority, funding, completion evidence |

Operational records belong in controlled stores. Public GitHub content should contain code, specifications, schemas, and sanitized evidence—not contact lists, credentials, raw tickets, or detailed financial records.

### 9.2 Proposed technical boundaries

Use a durable workflow runtime with persisted state, deadlines, bounded retries, worker leases, scheduled jobs, and failure ownership. A chat session is not the runtime.

Expose narrow actions such as `publish_verified_asset`, `send_eligible_message`, `pause_campaign`, and `reserve_campaign_budget` through an action gateway. Workers receive only necessary scoped access. Production credentials should not enter model prompts.

Event envelopes should carry `event_id`, `event_type`, `occurred_at`, `received_at`, `schema_version`, `product_id`, relevant subject IDs, a correlation ID, and provenance. Validate incoming authenticity; deduplicate and handle late or out-of-order delivery. Do not assume external systems provide exactly-once execution.

Test credential renewal, revocation, outage behavior, quota handling, and a real permitted action for each connector. Recurring manual login is an unresolved autonomy dependency, not an operational connector.

## 10. Finance, attribution, and business metrics

### 10.1 Spending and commitments

Reserve authorized funds before external commitments and use atomic accounting so concurrent campaigns cannot spend the same balance. Reconcile actual spend and release only confirmed unused reservations. Unknown spend remains exposure until reconciled.

Track advertising, creative production, AI inference, tools, sales activity, discounts, delivery costs, and shared costs under an adopted allocation method. Do not call advertising spend alone the total cost of acquiring a customer.

### 10.2 Metric definitions

| Metric | Proposed definition and limitation |
| --- | --- |
| Qualified conversion | Qualified prospects divided by eligible prospects in a defined cohort |
| Activation rate | Customers reaching a predeclared first-value event divided by eligible signups |
| Advertising cost per new paying customer | Attributed advertising spend divided by attributed new paying customers; not fully loaded acquisition cost |
| Fully loaded acquisition cost | Defined acquisition costs allocated to a cohort divided by its new paying customers; disclose timing and allocation assumptions |
| Cohort contribution | Recognized net revenue less defined attributable delivery, service, and operating costs; report acquisition cost separately and combined without double counting |
| Retention | Retained eligible customers divided by the starting eligible cohort, using an explicit retention definition |
| Refund and complaint rates | Applicable cases divided by the relevant customer/order cohort, with reporting delays |
| Autonomous verified completion | Accepted operations with no human ask or human execution divided by all eligible started operations in the cohort |
| Operational human asks | Raw asks, asks per 100 eligible operations, and recorded human execution time |
| Blocked work | Open count, age, impact, owner, and root cause |

No denominator means “unavailable,” not zero or perfect performance. Keep test accounts, bots, internal activity, incomplete cohorts, late conversions, cancellations, and attribution uncertainty visible.

Attribution describes an association under a chosen model; it does not prove a campaign caused a purchase. Use controlled comparisons or holdouts where practical. Do not add up overlapping channel claims as if each independently acquired the same customer.

### 10.3 Experiment discipline

Predeclare the success rule, observation period, guardrails, resource cap, and conditions for early stopping. A large number of impressions does not compensate for poor activation or expensive support.

For low-volume products, retain uncertainty and combine quantitative outcomes with documented customer evidence. Avoid continuously selecting a winner from tiny samples. Scaling must remain within authority and preserve reliability, privacy, and economics.

## 11. Operating cadence, recovery, and maintenance

Use event-driven operations alongside scheduled reviews.

| Trigger | Proposed autonomous response |
| --- | --- |
| Eligible prospect arrives | Route, qualify, and start permitted follow-up |
| Unsubscribe or preference change | Update suppression and invalidate ineligible queued sends |
| Broken landing page or signup | Pause affected spend; open incident; recover and verify |
| Support or refund spike | Diagnose message/product mismatch; contain affected acquisition |
| Product release | Revalidate dependent claims; update eligible assets and follow-ups |
| Expiring credential or integration error | Renew or recover through approved methods; pause safely when necessary |
| Delayed spend report | Reconcile exposure; constrain new commitments |
| Scheduled performance review | Compare mature cohorts and decide within the mandate |

Maintain recurring obligations for domain and certificate expiry, sender health, account permissions, connector changes, stale claims, pricing updates, retention jobs, and reporting. Assign owners and due dates.

The recovery sequence is diagnosis, reconciliation, bounded retry, permitted repair, approved alternative, and containment when necessary. A failure should create owned remediation and a recurrence test. Do not disguise silent abandonment as autonomy.

An independent watchdog should detect missing scheduled work and unavailable operating agents. Board suspension must cover queued sends, publishing, paid campaigns, and descendant workflows. Externally running campaigns require provider-side pause confirmation; stopping a local worker does not prove external spend has stopped.

## 12. Security, privacy, and customer trust

Implement tenant and venture isolation at storage, retrieval, action, and reporting boundaries. Treat web pages, customer messages, and third-party content as untrusted evidence. They cannot grant permission or instruct credential disclosure.

Keep personal data minimized, purpose-limited, and subject to adopted correction, retention, export, and deletion procedures. Propagate restrictions to derived indexes and caches. Preserve legally required records according to the adopted retention design rather than promising indiscriminate deletion.

Maintain evidence for claims and rights to creative assets. Do not fabricate testimonials, customer logos, performance statistics, partnerships, or certifications. AI company representation should be truthful and clear where material to customer understanding.

Each product and market needs an applicable-requirements review before activation, including communication practices, privacy, advertising claims, and provider restrictions. This proposal is not a determination of legal compliance for a particular jurisdiction.

## 13. LondonRue towel-business example

LondonRue is the founder's example, not a recorded launch authorization. Its
instance develops the towel business and operates its marketing, storefront,
supplier interfaces, orders, support and financial administration within mandate.

An illustrative campaign compares two verified presentations of a towel collection.
Before publication, growth checks the material, dimensions, care instructions,
images, price and delivery claims against product and supplier evidence. Operations
confirms stock or a supported fulfillment arrangement. The campaign must not promise
inventory, certifications, delivery or product performance without support.

Track the journey from permitted acquisition to order, payment, shipment, receipt,
returns or continued customer value. For physical goods, checkout or account signup
alone is not proof that the customer received a useful product. Include fulfillment,
shipping, returns and support in economic evaluation.

If customers report unclear dimensions, support handles their actual cases while
product and growth correct verified product information. Measure later outcomes;
do not invent a causal improvement from a small or immature cohort. Supplier or
quality failures also reach procurement and operations, not just engineering.

LondonRue-specific improvements follow its business release process. Validated
reusable lessons improve the Unilogistix framework through independent evaluation
and versioned CI/CD. Future businesses inherit the improved product-information,
marketing and support workflows in their applicable business profiles. Existing
instances can receive compatible upgrades without copying private customer data.


## 14. Implementation backlog and acceptance gates

Priorities indicate a proposed sequence, not approved work or a delivery-time commitment. Owners below are proposed AI responsibilities, not claims that those workers are deployed.

| ID | Priority | Deliverable | Dependencies | Proposed owner | Acceptance evidence |
| --- | --- | --- | --- | --- | --- |
| MKT-01 | P0 | Adopted marketing mandate and launch criteria | Board decisions | Governance | Forged, expired, missing, and over-limit authority rejected |
| MKT-02 | P0 | Product, brand, claim, and offer registry | MKT-01 for live use | Product/assurance | Unsupported or expired claim blocks publication |
| MKT-03 | P0 | Durable workflow and action gateway | Shared company runtime | Engineering | Restart and duplicate delivery do not duplicate consequential effects |
| MKT-04 | P0 | Finance reservation and reconciliation interface | MKT-01, MKT-03 | Finance | Concurrent campaigns cannot exceed adopted exposure |
| MKT-05 | P0 | CRM, eligibility, and suppression records | MKT-03 | Customer operations | Preference change blocks a queued promotional send |
| MKT-06 | P0 | One verified publishing connector and destination | MKT-02–05 as applicable | Distribution | Actual allowed action, denial, receipt, retry, and revocation tests |
| MKT-07 | P1 | Research and campaign planner | MKT-01–02 | Growth | Hypothesis and evidence separated from assumptions |
| MKT-08 | P1 | Asset review and delivery pipeline | MKT-02–03, MKT-06 | Assurance/engineering | Builder cannot remove a protected check to publish |
| MKT-09 | P1 | Acquisition-to-activation journey | MKT-05–08, working product | Sales/customer success | Accepted handoffs and verified first-value event |
| MKT-10 | P1 | Attribution, costs, and cohort reporting | MKT-04, MKT-09 | Analytics | Dashboard reconciles to source events; no duplicate customer attribution |
| MKT-11 | P1 | Support, incident, and acquisition-stop interface | MKT-03, MKT-09 | Support/operations | Service failure pauses affected acquisition and recovery is verified |
| MKT-12 | P1 | Feedback-to-release-to-follow-up workflow | MKT-08–11 | Product/engineering | One real or sandbox issue traced through measured improvement |
| MKT-13 | P1 | Experiment evaluator and bounded optimization | MKT-10–12 | Growth/analytics | Weak evidence or guardrail failure prevents promotion |
| MKT-14 | P1 | Maintenance, watchdog, and board reporting | MKT-03–13 | Operations | Missed obligations and stale data are detected independently |
| MKT-15 | P2 | Additional channels and isolated venture reuse | First lifecycle graduation | Growth/platform | Isolation, permissions, economics, and recovery retested |

### Proposed rollout gates

**Gate A — Documented and authorized business scope.** The relevant business authority records its product, market, limits, review rules, and future implementation authority. Documentation approval alone does not activate live outreach.

**Gate B — Sandbox lifecycle.** A synthetic prospect travels through campaign, signup, onboarding, test payment, support, and feedback-driven change. No external customers or purchases are required to prove this technical flow.

**Gate C — Bounded live pilot.** Activate only the adopted product, audience, channel, and budget after security, support, and recovery tests pass. Show actual customer outcomes rather than treating simulations as market validation.

**Gate D — Marketing autonomy graduation.** Demonstrate representative operations over the adopted window with zero routine human asks or execution, acceptable customer outcomes, reconciled economics, and visible unresolved work. Low-frequency failures also require controlled exercises.

**Gate E — Expansion.** Add channels or products only when evidence supports the added complexity and authority covers it.

Do not call the entire company autonomous merely because the marketing subsystem passes. Sales, finance, support, engineering, maintenance, and other relevant obligations need their own end-to-end evidence.

## 15. Required acceptance and failure tests

| Test | Expected outcome |
| --- | --- |
| Publish an unsupported feature claim | Publication denied; correction task opened |
| Revoke a mandate after a post is scheduled | Queued publication blocked; affected live actions contained as authorized |
| Unsubscribe while an email waits in a queue | Promotional send rejected at execution |
| Timeout after provider accepts a campaign action | Reconcile before retry; no duplicate commitment |
| Concurrent budget requests | Atomic reservation prevents overspending |
| Spend data becomes stale | New exposure constrained; uncertain commitments remain reserved |
| Campaign directs users to failed signup | Affected acquisition paused and incident opened |
| Builder modifies verification rules in the same change | Protected review boundary prevents self-approval |
| Customer message contains tool instructions | Treated as untrusted content; no authority change |
| Cross-venture customer lookup | Access denied and logged |
| Restore runtime after a crash | Work resumes from durable state without duplicated sends or payments |
| Credential expires during unattended operation | Authorized recovery works, or failure is recorded and safely contained |
| Superficial conversion gain increases complaints | Guardrail rejects scaling or adoption |
| Customer defect is fixed | Release, customer outcome, and appropriate follow-up are linked |
| No customers or eligible operations occur | Metrics show unavailable; autonomy/business graduation not granted |
| Founder performs routine repair | Human work recorded; clean autonomy window not claimed |

## 16. Board discussion and proposed decision register

Every entry starts **Not decided**. Board discussion can accept, amend, reject, or defer individual items. No default outcome is inferred.

| Decision | Recommendation for discussion | Required recorded outcome | Status |
| --- | --- | --- | --- |
| BD-MKT-01: Operating model | Adopt acquisition-to-retention ownership rather than content quotas | Accepted scope and accountable owner | Not decided |
| BD-MKT-02: First product and audience | One validated product, one audience, one primary channel | Product mandate, market, supported use cases | Not decided |
| BD-MKT-03: Delegation | Ordinary marketing decisions autonomous within standing limits | Reserved matters and permitted actions | Not decided |
| BD-MKT-04: Financial envelope | Capped pilot with explicit exposure and continuity reserves | Currency, amounts, periods, fees, allocation rules | Not decided |
| BD-MKT-05: Accounts and vendors | Reuse suitable existing resources; verify one channel first | Authorized accounts, procurement limits, identity design | Not decided |
| BD-MKT-06: Trust and customer policy | Evidence-backed claims and purpose-specific communication rules | Adopted policies and applicable-requirements review | Not decided |
| BD-MKT-07: Measurement | Activation, retention, contribution, and autonomy outcomes | Metric definitions, targets, windows, exclusions | Not decided |
| BD-MKT-08: Launch and stopping rules | Service-aware acquisition with automatic containment | Numeric guardrails and recovery conditions | Not decided |
| BD-MKT-09: Learning authority | Controlled knowledge/process/product improvement | Evaluation gates and protected boundaries | Not decided |
| BD-MKT-10: Graduation and expansion | Require representative evidence before adding complexity | Observation window, test coverage, expansion limits | Not decided |

After a decision, record its exact scope, adopted document version or hash, authenticated approval reference, effective date, expiry, amendments, and superseded decisions. Keep implementation completion and live activation separate from adoption.

## 17. Documentation placement and related work

Current adapted discussion location:

`books/BOOK-06-BUSINESS-OPERATIONS/AUTONOMOUS-MARKETING.md`

The supplied discussion copy is retained in reference/. Do not silently replace the existing constitution, autonomy policy, or customer policy with this proposal.

| Existing area | Proposed documentation change |
| --- | --- |
| Business Operations book | Link the marketing operating contract and customer-journey ownership |
| Evolution book | Link the marketing/customer-feedback experiment loop and evidence gates |
| Product-and-customer policy | Incorporate only explicitly adopted claims, communication, and growth controls |
| Integrations inventory | Add verified channel capability records, permissions, receipts, and renewal evidence |
| Workflows | Add campaign lifecycle, feedback-to-release, and acquisition containment workflows |
| Dashboards | Add adopted cohort, attribution, financial, and autonomy metric definitions |
| Roadmap | Insert acceptance-linked MKT backlog without claiming it is implemented |
| Board register | Record actual decisions and activation state, not the proposal as approval |
| Master index and changelog | Link adopted or clearly labeled proposed material and describe the update |

Keep customer data, account identifiers requiring protection, credentials, detailed financial records, and unsanitized operational evidence outside the public repository.

## 18. Evidence and source references

Repository statements in this proposal are based on the following files read at the pinned commit. Linked sources establish what the documents say, not independent proof that their described external systems are running. Provider-specific API behavior, legal requirements, and production readiness must be verified during implementation.

- **[S1] Business Operations:** [Pinned source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/books/BOOK-06-BUSINESS-OPERATIONS/README.md).
- **[S2] Product, hardware, marketing, and customer policy:** [Pinned source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/policies/product-and-customers.md).
- **[S3] MCP and tool integration plan:** [Pinned source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/integrations/README.md).
- **[S4] Evolution & Continuous Improvement:** [Pinned source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/books/BOOK-10-EVOLUTION/README.md).
- **[S5] Operational human intervention is a failure:** [Pinned source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/policies/autonomy.md).

## Change history

- **0.2 — 2026-09-09:** Adapted the supplied proposal to business-specific instances, replaced the illustrative scenario with LondonRue towels, and linked business-to-framework learning. Detailed policy adoption and all live activation remain pending.

- **0.1 — 2026-09-09:** Prepared a standalone marketing and growth operating-model proposal for founder/board discussion. Added authority boundaries, campaign operations, customer handoffs, support and CI/CD connections, feedback learning, metrics, controls, implementation backlog, acceptance tests, and undecided board resolutions. No adoption, deployment, spending, outreach, or repository write is implied.
