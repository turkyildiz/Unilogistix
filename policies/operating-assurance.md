# Connected business operation and assurance

Version: 0.1 | Updated: 2026-09-09 | Status: Proposed rules incorporated for document review; not adopted or activated

## Source, scope and relationship to the constitution

This policy incorporates all ten improvements from the founder-supplied
[additional improvements proposal](../reference/Unilogistix_Additional_Improvements_Board_Proposal.md)
into the existing [constitutional responsibilities](../CONSTITUTION.md#constitutional-agent-responsibility-schedule).
It creates no additional agent roles. One listed role is accountable for each
cross-department outcome; other roles retain their specialist responsibilities.

Unilogistix is a reusable operating framework, never an actual company. These rules
apply in the relevant actual-business instance, or to framework work where specified.
LondonRue towels is the example. References to the board mean the actual authorized
governance scope, not an incorporated Unilogistix board.

The supplied proposal's GitHub and OpenBao observations are historical claims at
its stated baseline, including its reported infrastructure progress and remaining
dependencies. They were not independently reverified during this documentation work.
They neither overwrite newer evidence nor establish current operational readiness.
Its technical references remain source references, not selected vendors or claims
of compliance. Today's work is documentation only.

## Improvement ownership and disposition

All entries are incorporated as proposed document requirements. Existing UNI/MKT
backlog references remain historical traceability, not newly authorized projects.

| ID | Required improvement | Accountable role | Supporting roles | Relationship to current rules |
| --- | --- | --- | --- | --- |
| IMP-01 | Capability evidence and verified outcome records | R57 | R53, R54, R07, relevant verifier | Makes existing completion/evidence rules precise |
| IMP-02 | Consistent customer state and commitments | R02 | R18, R33, R35, R41, R46–R48 | Adds shared invariants across existing handoffs |
| IMP-03 | Action-specific operating eligibility | R07 | R56, R57, R60 | Separates permission from demonstrated capability |
| IMP-04 | Compound-failure and protected evaluation | R21 | R22, R23, R26, R57, R59 | Expands existing independent testing requirements |
| IMP-05 | Customer self-service and first value | R06 | R11, R12, R15, R17, R34–R37 | Makes customer-controlled journeys explicit |
| IMP-06 | Evidence-backed customer buying process | R32 | R13, R23, R44, R50, R51 | Adds quotes, assurance answers and contract deviations; distinct from supplier procurement R38 |
| IMP-07 | Customer/product economics | R04 | R43, R44, R48, R54, R06 | Connects cost evidence to sustainable offers and growth |
| IMP-08 | Business-aware scheduling | R01 | R02, R08, R26, R43, R56 | Adds capacity reserves, fairness and shared child-task limits |
| IMP-09 | Independent end-to-end recovery | R26 | R24, R48, R58–R60 | Extends backup requirements to restored customer operation |
| IMP-10 | Decisions connected to current evidence | R07 | R01, R04, R52–R54 | Connects authentic decisions to execution and measured results |

## IMP-01 — Evidence before readiness or completion

Maintain scoped capability records containing action class, business, environment,
artifact/model/prompt/tool versions, authority reference, applicable tests, evidence
provenance, verification date, invalidation conditions and owner. Record adoption,
implementation, deployment, qualification and observed outcomes separately.

An operation record contains its authorized intent, relevant business/customer
scope and state version, external action IDs, receipts, checks, reconciliation,
cost and remaining obligations. Consequential completion requires independent
acceptance appropriate to its risk. Reversible internal drafting may use lightweight
artifact validation; it does not require a separate expensive model review for
every transformation. Do not require private model reasoning as evidence.

An assertion, green exit or content hash alone cannot establish that an external
event occurred. Hashes bind reviewed content; provenance and outcome evidence
establish what is known. Preserve historical evidence when a relevant version,
mandate or condition changes, but invalidate the affected current eligibility.
Unrelated changes do not invalidate unrelated capabilities.

**Review case:** A promised file is absent, or a refund has only been requested.
R57/relevant acceptance role rejects verified completion; the accountable executor
retains the missing deliverable or settlement obligation.

## IMP-02 — Consistent customer state across departments

Maintain separate linked dimensions for order/commercial state, payment, entitlement,
support, contact preferences and data obligations. R33 owns canonical relationship
records; R37 order state; R46 billing/receivables; R35 support; R51 data-use rules.
R18 specifies versioned updates and integrity controls. R02 owns resolution of
cross-department inconsistency; one vague active/inactive field is insufficient.

Required invariants include:

- An effective cancellation stops initiation of affected future renewals; already-started external actions are reconciled under the applicable terms.
- Promotional sends recheck current eligibility, including queued sends.
- Refunds and disputes share eligible-amount/exposure checks so concurrent paths do not over-disburse; conflicts remain visible.
- An offer references current permitted product, price and service commitments with a fulfillment owner.
- Suspended or unavailable capabilities cannot remain advertised as presently available.
- Combining related tickets into one incident does not erase individual remedies or deadlines.
- Cancellation does not automatically erase paid entitlements, financial records or unresolved obligations.

Updates within the authoritative store require integrity and concurrency controls.
External multi-step actions require explicit continuation or corrective actions.
A corrective action is not a claim that a shipment, service or sent email was erased.

**Review case:** Apply cancellation, delayed payment, return and promotional events
in different orders with restarts. The documentary expected result must preserve
the permitted customer outcome, money state and open obligations in every ordering.
R02 assigns any conflict; departments cannot each invent their own final state.

## IMP-03 — Qualify actions, not titles

An enabled role needs action-specific qualification as well as authority. Proposed
stages are observe, simulate, bounded live, established operation and restricted/
suspended. Each stage is scoped to action, business, environment and configuration.

Execution requires the intersection of valid mandate, scoped identity/resources,
current action qualification, service conditions and remaining authorized resources.
None supplies the others. Confidence, a job title or success at another action
cannot expand permission. A model/tool/prompt or relevant rule change triggers
risk-proportionate reassessment of affected actions.

R57 independently verifies qualification; R07 maintains authentic authority;
R60 enforces the resulting scope. Automated promotion may proceed only within an
already-adopted envelope and its evidence gates. Restriction does not authorize
rerouting to a more privileged worker to bypass the failure.

**Review case:** An agent qualified to publish content attempts a refund. Reject
the unsupported action; allow an independently qualified, already-authorized refund
path without manufacturing a new founder approval requirement.

## IMP-04 — Compound failures and protected evaluation

R21 defines representative compound-failure scenarios; R22 executes future tests
with isolated synthetic records, controlled clocks/faults and no production
credentials or real customer communications. Include response loss after payment,
cancellation races, credential expiry during an incident, degraded monitoring,
restored stale state, malicious retrieved content, capacity overload and revocation
of queued work.

Protect evaluation criteria and independent results from the change author. Keep
reproduction inputs, event order, attempted actions, state changes and observable
customer/financial outcomes. Test fixtures may be maintained, but changes to their
meaning need independent review. No author can create the only tests, redefine
passing, grade the result and approve its own consequential release.

Label simulation as simulation. Check important assumptions against permitted
provider sandboxes and contract evidence before relying on them. A simulated month
is not a month of observed business operation or proof of demand.

**Review case:** Inject false success, duplicate actions and an attempted evaluator
change. The protected acceptance process detects the violation and assigns a fix;
the false success cannot enter readiness evidence.

## IMP-05 — Direct customer controls and verified value

Standard customer actions must have understandable direct controls appropriate to
the product, with AI help as an additional route. Cover discovery/comparison,
purchase, identity/account management where needed, transaction history, service
or delivery status, support, cancellation/returns and applicable data requests.
Do not impose unnecessary account creation on a business that supports guest buying.

R06 defines first value; R11/R12 specify success, failure and accessibility behavior.
For LondonRue, payment or a welcome email does not prove satisfactory delivery of
towels. Use available evidence of correct fulfillment and customer outcome without
inventing satisfaction for customers who do not respond.

Measure abandonment, time to useful outcome and unresolved steps using permitted
data. Show honest partial states and route failures to an accepted R34/R35/R37
owner. Buttons that cannot perform a supported action must not suggest completion.

**Review case:** A customer can buy, inspect order status and request a permitted
remedy without the founder operating the interface. The remedy follows its real
terms and verification steps rather than an invented chatbot workaround.

## IMP-06 — Evidence-backed quotes and buying support

R32 maintains a versioned commercial packet suitable for the target customer:
verified product facts, approved prices/terms, supported delivery/service boundaries
and relevant assurance evidence. For LondonRue wholesale buyers, this may include
verified dimensions/materials, quantity availability, lead times and standard quotes.
An enterprise security portal is not required unless the business need justifies it.

Each consequential answer distinguishes verified fact, adopted commitment, proposal
and unknown, with source and current scope. Restrict private supporting records to
authorized recipients. A planned control, supplier credential or another business's
certification must not be represented as the seller's demonstrated certification.

Standard offers proceed inside delegation. Requested deviations in liability,
service, data, geography or money go to R50 and the actual required authority.
Unfamiliar wording does not become authorized because a model sounds confident.

**Review case:** A buying questionnaire mixes supported facts, a planned capability
and an unauthorized guarantee. Supply accurate answers, identify the gap and keep
the guarantee proposed while supporting the authorized purchasing path.

## IMP-07 — Explainable customer and product economics

R04 defines decision-oriented views with R44's accounting policies and R54's metric
definitions. Separate actual receipts, recognized revenue under the adopted method,
direct cash outlays, allocated costs, reserves and remaining obligations. Include
goods, freight, fulfillment, returns, support, inference, retries, infrastructure
and recovery where relevant, without double counting shared allocations.

Disclose allocation assumptions and timing. Missing costs imply uncertainty, not
zero expense. Use the simplest detail that supports a meaningful decision. Compare
product and mature customer cohorts; do not expose unnecessary personal financial
profiles to marketing or other businesses.

Pricing/packaging changes stay within existing authority and commitments. A costly
customer is still owed their contracted service and permitted remedies. Restrict
new unviable exposure within mandate rather than abandoning existing obligations.

**Review case:** A campaign raises sales but loses money after returns and support.
R04/R05/R06 use reconciled evidence to change future targeting or propose a revised
offer, while R02 continues owed service.

## IMP-08 — Scheduling that preserves business obligations

R01 and R08 enforce hard authority, safety and obligation constraints before
optimizing throughput. Prioritize incidents and funded customer obligations,
time-critical duties, ordinary service and then discretionary experiments, with
reserved capacity and aging rules that prevent indefinite starvation.

Each operation has an owner lease, deadline, total budget/tool-call limits,
concurrency bound and recovery route. Child work consumes the same authorized
envelope; additional workers do not create additional funds. Deduplicate shared
investigations while preserving distinct customer cases and deadlines. Stale
workers must not overwrite accepted work after ownership changes.

Use deterministic checks for straightforward validation/calculation and evaluated
models where reasoning is needed. Never remove mandatory independent checks to
improve cost or speed figures. Repeated repair failure triggers bounded alternate
recovery or an owned unresolved state, not unlimited looping.

**Review case:** Research demand floods the queue while checkout fails and a funded
renewal is due. Essential work receives capacity, experiments remain within their
shared limit and all unfinished work retains an owner.

## IMP-09 — Recover the business, independently

R26 owns the recovery outcome; R24/R60 recover infrastructure/identity and R59
detects loss independently of the failed service. Record actual failure domains
and permitted recovery resources privately. Existing resources are not assumed to
have spare capacity or independent power/network dependencies.

The acceptance target is restored, reconciled customer operation after loss of
the normal host and founder workstation. Cover identity recovery, restoration,
external-action reconciliation, customer-path checks, cutover and authorized
resumption. Test prolonged credential expiry. Preserve intentional suspension;
recovery must not undo board revocation or place all recovery authority inside
ordinary worker access.

Backups, off-host evidence and external detection need verified outcomes. SLOs and
recovery targets belong to each business profile. A reliability error allowance is
not money or permission to violate data/security rules. Undelegable steps remain
visible dependencies, not hidden claims of autonomy.

**Review case:** In an isolated exercise, lose both host and workstation after an
external payment. Detect, restore and reconcile without repeating the payment;
compare measured recovery and potential data loss to the adopted targets.

## IMP-10 — Decisions, evidence and follow-through

R07 owns authentic decision records; R54 assembles current facts and R01 owns
follow-through. A material packet includes the problem, recommendation, alternatives
including no action, evidence, uncertainty, one-time/recurring costs, obligations,
expected benefit, genuine decision deadline and exact requested authority.

Record the real decision, exact adopted version/scope, effective period, conditions,
supersession and follow-through owner. A pending, rejected or overdue proposal is
not approved. Report authority, capability, operations, economics and learning as
separate dimensions, with changed facts, negative outcomes and forecast/actual
differences. Do not combine them into a single misleading autonomy score.

Routine support remains operating work inside delegated authority. New capital or
other reserved decisions receive concrete packets without premature execution.
Governance reporting must not become a queue of routine approvals for the founder.

**Review case:** Process one ordinary support issue and one new-capital proposal.
The former follows autonomous recovery; the latter remains unexecuted until its
actual authority exists. Both have truthful status and accountable follow-through.

## Adoption and remaining configuration

The ten rules are proposed additions to the manuscript, not ten newly approved
implementation projects. Specific action matrices, permitted transactions, service
targets, budgets, retention values, recovery placement and first-value definitions
belong to business adoption schedules. Changes to protected control requirements
use the constitutional amendment/review procedure.

The supplied proposal's eight board items remain undecided unless separately
resolved by an authentic instruction. Its suggested engineering sequence is future
work; it does not override today's documentation-only scope. The original proposal
is preserved unchanged; this policy is the current adapted rule text.

## Change history

- 0.1 — 2026-09-09: Incorporated IMP-01–IMP-10 into existing role ownership, adapted the examples to business instances and LondonRue, and retained adoption and historical-evidence boundaries.
