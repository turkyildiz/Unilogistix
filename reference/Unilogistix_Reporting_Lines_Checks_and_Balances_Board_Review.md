# UNI / Unilogistix — Reporting Lines, Decision Rights, and Checks & Balances

**Board discussion and implementation review**

Version: 0.1  
Updated: 2026-09-09  
Status: Evidence-based review and proposed changes; not adopted or activated  
Prepared for: Ilker Yildiz and the Unilogistix Board  
Repository reviewed: `turkyildiz/Unilogistix`  
Published commit visible during this review: `a23534e1ffa280adb94221b4c5353f8819a92dc6`

> **Verdict:** The published documents establish executive responsibilities and sensible control principles. They do **not yet establish a fully explicit reporting structure or demonstrate a complete, enforced system of checks and balances**. The most important improvements are protected oversight, explicit decision rights, separate execution identities, and controls that can actually reject an unauthorized action.
>
> All new reporting lines, role assignments, gates, and implementation items below are recommendations for board discussion. They are not existing appointments, adopted policies, permission grants, or evidence of deployment. This review made no repository, account, or production changes.

## 1. What was actually visible in GitHub

The read returned `a23534e` on `main`, with a commit timestamp of **September 9, 2026, 15:51:38 UTC / 10:51:38 a.m. America/Chicago**. The two returned branches, `main` and `docs/autonomous-marketing-operating-model-20260909`, point to that same commit. The pull-request collection returned an empty list. This is the same published baseline used in the previous marketing proposal, not evidence that newer reporting changes have been merged. Newer or unpushed work is outside this review. [G1–G3] A final read of the Git reference independently confirmed the same published head. [G8]

The repository settings returned `protected: false` for `main`, no required status checks, an empty ruleset collection, and zero GitHub Actions runs. The workflow directory at this commit contains only `README.md`. These are direct observations of GitHub's returned state, not assumptions based on a document. They do not prove that no external CI service exists elsewhere. [G1, G4–G6]

The `agents/` directory contains its README and two dedicated role specifications: CEO/Orchestrator and Independent Reviewer. Both specifications explicitly describe unbound runtime/model configuration and say they are not running workers. Executive titles in the organization book therefore must not be presented as deployed personnel. [G7, R2, R3]

**Evidence boundary:** This was a read-only document and repository-configuration review. No live payment, production deployment, credential recovery, branch-write denial, or customer-isolation test was performed. Vault verification results are repository-reported evidence, not independently repeated server tests. No percentage-complete or blanket compliance certification is assigned.

## 2. Who reports to whom in the current documents?

### 2.1 The structure actually described

The organization book gives the broad hierarchy:

```text
Founder / Board
    ↓
AI executive accountability
    ↓
Department responsibilities
    ↓
Specialist execution
```

The master architecture separately shows the board directing the CEO/Orchestrator and a governance/authority service, with independent review and a tool gateway between agent work and consequential execution. That is an architectural separation, not a complete management reporting chart. [R1, R6]

| Role/function | Responsibility explicitly described | Reporting-line certainty |
| --- | --- | --- |
| Founder / Board | Direction, governance, standing authority, reserved decisions | Highest internal authority; applicable obligations and platform restrictions still apply |
| CEO / Orchestrator | Portfolio coordination; translate board objectives into owned work | Board-to-CEO connection is explicit in the architecture |
| CTO | Technical architecture and engineering | Executive responsibility is named; an exact `reports_to` assignment is not defined |
| COO | Reliable business operations | Executive responsibility is named; exact management and incident authority are not fully defined |
| CFO | Financial administration within adopted limits | Responsibility is named; protected board access and finance-role separation need explicit contracts |
| CMO | Truthful growth and acquisition | Responsibility is named; boundaries with sales, CRM, product, and customer operations need explicit ownership |
| Independent Reviewer | Verify authority and deliverable evidence; accept or reject | Independence is required, but appointment, removal, budget protection, and final appeal ownership are not specified |
| Internal audit | Independently review control evidence | Functional purpose is stated; direct board reporting and authority over access to evidence are not specified |
| Product, research, intelligence, knowledge, and program management | Functions are described | Several have no unambiguous executive reporting line |

Sources for the current structure: organization book, CEO and reviewer specifications, constitution, financial policy, and master architecture. [R1–R4, R6, R7]

**Interpretation:** CTO, COO, CFO, and CMO reporting operationally to the CEO is a reasonable implementation choice, but it is not appropriate to call every detailed relationship below an already-adopted fact.

### 2.2 The key distinction

A reporting line answers **who assigns work and owns performance**. A control answers **who may reject an action, restrict access, or verify its result**. These are different authorities.

A CEO may prioritize a release without being entitled to bypass a security rejection. A CFO may administer a budget without being entitled to raise it. A reviewer may reject an action without being entitled to execute it. The existing architecture and constitution already support this separation in principle. [R4, R6, R7]

## 3. Recommended reporting structure for board consideration

### 3.1 Proposed chart

```text
FOUNDER / BOARD
│
├── AI CEO / ORCHESTRATOR — operational accountability
│   ├── Product & Research Lead
│   ├── CTO — engineering and technical operations
│   │   ├── Architecture, application, data, and AI engineering
│   │   ├── Engineering QA and test development
│   │   └── Platform, deployment execution, and reliability engineering
│   ├── COO — customer and business operations
│   │   ├── Onboarding and customer success
│   │   ├── Support, service recovery, and order operations
│   │   └── Program coordination, obligations, and knowledge stewardship
│   ├── CFO — financial administration
│   │   ├── Billing and collections
│   │   ├── Budget and financial-control verification
│   │   └── Accounting and independent reconciliation execution
│   ├── CMO — growth and commercial acquisition
│   │   ├── Market research coordination, brand, and campaigns
│   │   ├── Content and channel operations
│   │   └── Sales, qualification, and commercial CRM workflows
│   └── Business Intelligence — cross-company outcome reporting
│
├── INDEPENDENT ASSURANCE / RISK LEAD — protected oversight
│   ├── Independent release and deliverable verification
│   ├── Security, privacy, and compliance-control review
│   └── Bounded action holds and approval-dispute review
│
└── INTERNAL AUDIT — independent evaluation of operations AND assurance
    ├── Control testing and evidence sampling
    ├── Financial and operational evidence integrity
    └── Direct findings and remediation-status reporting to the board
```

**These are proposed responsibilities, not a requirement to deploy one always-on model per box.** Start with the smallest worker pool that preserves the necessary separation. A function may execute on demand; it still needs an accountable owner and an eligible replacement.

The governance service, action gateway, credential broker, evidence store, release controller, and watchdog are enforcement services—not executive personalities. Their authority derives from adopted policy. Ordinary executives must not be able to rewrite their controlling permissions.

### 3.2 Exact proposed reporting and challenge rights

| Role | Operational reporting | Protected access or challenge right | Must not control |
| --- | --- | --- | --- |
| CEO | Board | Consolidated performance and genuine governance decisions | Its own mandates, audit findings, or mandatory control bypasses |
| Product & Research Lead | CEO | Requests evidence from customers, growth, support, and engineering | Unilateral launch authority or claims for unreleased features |
| CTO | CEO | Challenges technical feasibility and capacity | Independent assurance identity, its protected tests, or its approval keys |
| COO | CEO | Can trigger policy-authorized service containment | Erasing unresolved tickets or bypassing customer identity checks |
| CFO | CEO | Direct board channel for financial integrity, exposure, and genuine authority questions | Self-raised caps; one identity requesting, approving, paying, and reconciling its own transaction |
| CMO | CEO | Proposes experiments and allocations within delegation | Product truth, suppression rules, financial ceilings, or support-capacity thresholds |
| Business Intelligence | CEO | Direct source access within scope; protected discrepancy reporting | Rewriting source events to improve reported performance |
| Independent Assurance / Risk | Board for functional oversight; coordinates with executives | Rejects noncompliant actions and publishes its findings without CEO filtering | Executing the same material action it approves; expanding board authority |
| Internal Audit | Board | Reviews executives and assurance; reports uncensored findings | Owning routine production controls or approving transactions it later audits |

Direct board reporting means independent visibility and governance accountability. It does **not** mean every reviewer needs a founder click, or every operating dispute becomes a board decision.

### 3.3 Resolve overlapping responsibilities

**Product versus growth:** Product owns the supported offer and capability evidence. Growth owns how that verified value is communicated. Sales cannot turn a prospect's request into an already-supported feature.

**CRM versus customer operations:** Use one authoritative customer/account identity. CMO owns lead and opportunity stages; COO owns onboarding and service stages; CFO owns invoice and payment state. Cross-functional access is scoped. Do not create competing customer truths.

**Engineering QA versus independent release assurance:** Engineering creates tests and fixes defects. Assurance checks acceptance using separately controlled verification and evidence. A builder adding tests is valuable but is not independent release approval.

**Security engineering versus security oversight:** CTO's engineering function implements protections and repairs. Independent risk oversight evaluates the proposed action and may block it within policy. Internal Audit later tests whether both performed their roles.

**Incident coordination:** COO owns customer impact and cross-department coordination; CTO leads technical recovery; CFO reconciles financial exposure; assurance controls security/privacy clearance where applicable. Use one incident commander per incident, selected by a predefined rule.

## 4. Who decides, who checks, and who executes?

The following matrix is proposed. All actions still require an effective mandate and applicable authority. A favorable AI opinion never substitutes for those requirements.

| Decision/action | Business owner / proposer | Required independent check | Permitted executor | Who may block or stop? |
| --- | --- | --- | --- | --- |
| Ordinary product release | Product and CTO | Independent release assurance; protected tests; resource/mandate checks | Scoped release controller | Assurance, deterministic gate, reliability guardrail, board revocation |
| Marketing publication | CMO | Product-claim verification; audience and communication eligibility; budget when applicable | Scoped publishing service | Claim/eligibility gate; CFO exposure gate; COO service-capacity containment |
| Ordinary refund | COO support workflow | Separate refund-policy and financial verification | Scoped payment/refund service | Identity, eligibility, idempotency, and budget gates |
| Vendor payment | Requesting department; CFO administers | Different finance verifier; counterparty checks; independent handling of changed destination | Scoped payments service | Financial gate; risk hold; board revocation |
| Accounting reconciliation | CFO reconciliation function | Source matching and independently reviewed exceptions | Reconciliation service, with tightly scoped adjustment permissions | Integrity checks; unresolved exceptions remain visible |
| Access or credential change | Owning department | Risk review and deterministic entitlement/mandate evaluation | Credential/identity broker | Access-policy gate; revocation service |
| Prompt, model, or workflow promotion | Owning executive | Held-out evaluation; permission-preservation check; independent reviewer | Versioned configuration release service | Assurance and outcome guardrails |
| Incident containment | Incident commander or risk function | Preauthorized runbook conditions; do not wait for discretionary approval to invoke permitted containment | Bounded recovery/containment tools | Scope and safety interlocks; board suspension remains controlling |
| Increase authority or alter protected governance | CEO/CFO/assurance may propose | Impact analysis and independent review of the proposal | Governance service only after authentic board decision | Board; existing restrictions remain until valid amendment |
| Resume after explicit board suspension | Board decision | Revalidation of current policy, evidence, and intended scope | Separate authenticated resumption path | Revocation/suspension service; ordinary recovery cannot cancel a board stop |

Not every low-risk operation needs multiple model calls. Deterministic checks and an appropriately scoped prior authorization may be enough for a prevalidated, low-risk action class. High-impact or novel work needs the independent reviews specified for that class. Risk classification itself must not be freely changeable by the requesting agent.

## 5. Do we have all the checks and balances?

**No—not on the evidence currently visible.** The design covers many necessary principles, but adoption, reporting independence, enforcement, and operating proof are separate questions.

Status definitions: **Specified** means written requirements; **Partial / reported** means implementation or tests are described with explicit limits; **Observed missing** means the inspected GitHub setting or directory lacks the control; **Unverified** means this review has not established operational effectiveness. None of these labels alone means certified production readiness.

| Control | Evidence currently visible | Assessment | Required completion evidence |
| --- | --- | --- | --- |
| Authentic authority and standing mandates | Constitution supports delegation; activation register leaves concrete authority settings incomplete [R4, R5] | Specified; activation incomplete | Exact adopted scope and versions; forged/expired/missing authority rejected |
| Explicit management reporting | Executive responsibilities exist, but detailed reporting lines are incomplete [R1–R3] | Specified in outline | Adopted role registry with reporting, appointment, replacement, and escalation owners |
| Independent reviewer protection | Separate context and permission boundary required; no protected reporting/appointment contract [R1, R3] | Specified; independence unverified | CEO/builder cannot replace reviewer, change verdict, access approval credentials, or alter its protected tests |
| Internal audit independence | Independent review of evidence is named without a complete direct-board contract [R1] | Specified in outline | Auditor can report on CEO, CFO, CTO, and assurance without those subjects editing or suppressing findings |
| GitHub merge protection | `main` unprotected; required checks absent; rulesets empty [G1, G4] | Observed missing | Enforced protections; unauthorized direct write, bypass, and forged check attempts denied |
| Executable CI and release gates | Workflow directory contains a README; Actions run count is zero [G5, G6] | No demonstrated GitHub Actions pipeline | Automated good/bad PR tests, trusted check identity, reviewed artifact promotion, and rollback |
| Tool-gateway authorization | Architecture requires deterministic checks outside models [R6, R8] | Specified; operationally unverified | Exact action/resource/payload bound to current authority; denied alternate access paths |
| Budget and payment separation | Atomic reservations, idempotency, separate verification, and reconciliation required [R7] | Specified; operationally unverified | Concurrent requests cannot overspend; uncertain success cannot duplicate payments; conflicts force recusal |
| Credential isolation | Scoped OpenBao roles and read-only checker tests reported; original provider credentials retain original permissions [R9] | Partial / reported | Workflow-specific provider credentials or broker-only custody; no route around scope checks |
| Board stop and independent recovery | Board suspension required; authenticated board interface explicitly not implemented [R8, R9] | Specified; partial technical pause only | Authenticated stop works with orchestrator unavailable and cancels/contains external queued actions |
| Backup and recovery | Full restore/unseal/read and scheduled off-host snapshots reported [R9] | Partial / reported, with real progress | Replacement-host recovery/cutover; workstation-independent operation; long-outage credential recovery |
| Audit and alert independence | Local audit and timers reported; remote immutable retention and external alerts absent [R9] | Partial / reported | Evidence survives host loss; independent heartbeat and delivery-confirmed alerts |
| Customer, tenant, and knowledge boundaries | Access, privacy, untrusted-input, and product boundaries required [R6, R8, R10] | Specified; operationally unverified | End-to-end denial tests across database, retrieval, support tools, exports, and derived data |
| Marketing truth and customer remedies | Substantiated claims, identity checks, remedy limits, and feedback controls documented [R10] | Specified; operationally unverified | Invalid claims/sends/refunds blocked; customer outcomes verified instead of merely messages sent |
| Learning without self-granted power | Controlled experiments and non-expansion of authority specified [R11] | Specified; operationally unverified | Challenger cannot alter its evaluator, permission boundary, or historical failures |
| Honest reporting and autonomy accounting | Metrics include failed/blocked work, asks, and actual human effort [R12, R13] | Specified; instrumentation unverified | Source-reconciled dashboards; missing data visible; no metric gain from abandoned work or artificial task splitting |

The balance is incomplete whenever one principal can silently **propose, authorize, execute, and rewrite the evidence** for the same consequential action. Different job titles do not fix shared unrestricted credentials.

## 6. The eight highest-priority gaps

### GOV-01 — Protect the reviewer from the party being reviewed

Adopt a board-protected assurance charter. Separate its credentials, protected evaluation assets, evidence publication, and baseline resource allocation from ordinary executives. Normal worker failures may invoke a prequalified replacement under a standing policy; a failed verdict must not cause reviewer shopping.

**Acceptance:** A CEO task and builder PR attempting to replace the reviewer, change its pass criteria, or delete a rejection fail. A crashed reviewer is replaced from the approved pool without changing the standard or losing the rejection history.

### GOV-02 — Separate internal audit from operational approval

Assurance participates in pre-action checks; Internal Audit evaluates whether those checks and the rest of the company work. Do not merge these into one agent that audits its own approvals. Give audit scoped read access and a protected board reporting path, not payment or production-execution credentials.

**Acceptance:** Audit identifies a flawed assurance approval, preserves its evidence, and reports it without approval from the assurance lead or CEO. The audit role cannot perform the underlying transaction.

### GOV-03 — Close the routine-dispute escalation loophole

The constitution currently says unresolved or reserved disagreement goes from the relevant executive to the founder. Read literally, an ordinary unresolved review dispute could repeatedly make the founder the operating help desk. That needs clarification against the autonomy policy. [R4, R12]

Proposed replacement principle:

> Routine disputes follow a bounded independent adjudication and recovery procedure within existing authority. Business executives cannot overturn mandatory failed controls. The board receives matters requiring new or amended authority; any unavoidable request for routine human diagnosis or execution remains an autonomy failure. Unresolved work remains blocked, failed, or cancelled with evidence and ownership.

Select an adjudicator using a fixed, conflict-aware rule. Define maximum attempts, deadlines, evidence requirements, and safe fallback. An adjudicator may resolve conflicting evidence but cannot waive budgets, consent, board suspension, or mandatory controls.

### GOV-04 — Make GitHub checks provider-enforced

Implement real CI, require successful checks from trusted identities, and protect the default branch. GitHub supports required checks tied to an expected GitHub App, rather than accepting a same-named result from any writer. Rulesets also have bypass permissions, so an existing rule is insufficient without reviewing its enforcement and bypass scope. [W1, W2]

Treat independent verifier credentials and its trusted verification workflow as protected control assets. A check from the right App is not enough if the builder can rewrite the workflow that produces it. A valid check must bind to the exact reviewed commit and configuration; later changes invalidate it.

Use scoped build and release credentials, isolated handling of untrusted code, and reviewed dependency pins. GitHub documents privileged-trigger risks, full-commit pinning, and persistent compromise risks with self-hosted runners. Do not expose a broadly connected on-prem runner to untrusted public PR code merely to reduce cost. [W3]

**Acceptance:** A broken PR, a changed protected gate, a forged status, and an unauthorized direct write are denied. A valid AI-originated PR runs its checks without a routine human approval click. Test the chosen machine identities and triggers rather than assuming automation grants bypass authority.

### GOV-05 — Separate financial request, verification, execution, and reconciliation

Retain CFO accountability while splitting sensitive functions into distinct identities. Requesters cannot approve their own payments. Payment execution cannot modify approvals or make arbitrary ledger adjustments. Reconciliation compares authoritative receipts and ledger state, keeping unexplained differences open.

Changes to payment destinations require an independently trusted source, not a second model rereading the same untrusted message. A CFO-originated purchase needs a verifier outside that request's conflict path. Budget ceilings remain board-controlled, with automatic reservations enforcing totals across agents. These refine the existing financial policy rather than replacing it. [R7]

**Acceptance:** Duplicate, concurrent, changed-destination, and unknown-status cases cannot cause excess or diverted payment. Verification remains effective when the requester carries a CFO title.

### GOV-06 — Enforce permissions at the external boundary

The vault evidence reports dedicated OpenBao roles, but not dedicated provider-side credentials. The fixed checker limits its own requests while underlying source credentials retain their original permissions. That is useful bounded read automation, not proof of a deployment or spending gateway. [R9]

For production, use least-privilege provider identities where supported. Otherwise keep the credential inaccessible behind a narrowly authorized broker, constrain network egress and API routes, and explicitly record the residual exposure. Worker access to a secret is not harmless merely because its prompt says to use it read-only.

**Acceptance:** Compromise a test worker and attempt a direct provider request outside its workflow scope. It cannot obtain the underlying broad credential or bypass the gate. Keep any unavoidable privileged root outside ordinary operational control.

### GOV-07 — Remove the founder workstation as a recovery dependency

Do not repeat already-completed work as missing: full vault restore and scheduled backup are reported. Remaining limits include workstation dependence, nonautomatic host replacement/cutover, renewable issuer expiry after prolonged outages, and a common trust point able to reach all recovery custodians. [R9]

Establish an independently hosted, scoped recovery path and watchdog. Test outages beyond the documented credential leases. Do not solve recovery by handing a routine agent all privileged recovery material. Board suspension must survive restart, restoration, and credential renewal.

**Acceptance:** With the founder workstation unavailable and the main operating host lost, authorized recovery completes within adopted recovery objectives—or records a genuine failure rather than claiming autonomy. An intentional board stop cannot be undone by automatic recovery.

### GOV-08 — Make evidence independent and failures visible

Move critical evidence to retention-controlled storage outside the ordinary executor's write/delete authority. Add off-host health checks and delivery-confirmed alerts. Distinguish action attempted, provider accepted, externally reconciled, and outcome verified.

OpenBao's audit system has specific exclusions and availability behavior, so do not equate its local audit file with a complete company or board-control audit trail. The application needs explicit suspension/resumption, approval, customer, and financial events as well. Validate behavior against the deployed version. [W4]

**Acceptance:** Losing the vault host or disabling the orchestrator does not silently remove historical evidence or health reporting. A false support closure, unreconciled refund, or unavailable measurement cannot appear as a verified success.

## 7. How the proposed balances work in practice

### Example A — The CEO wants a faster product release

Product supplies acceptance criteria; engineering produces a candidate; assurance runs protected checks. A failed isolation test blocks release. The CEO may reprioritize a fix, reduce scope, or assign an eligible independent adjudicator to a genuine evidence dispute. It may not mark the failed test passed, replace the reviewer to obtain approval, or give itself production credentials.

After a compliant result, the release controller rechecks authority and promotes the exact accepted artifact. Reliability monitoring can revert it under the standing runbook. Audit can inspect the entire sequence without controlling the release.

### Example B — Marketing attracts more customers than support can serve

CMO sees improved conversion. COO's service indicators exceed an adopted backlog threshold. The campaign's new acquisition is paused through a preauthorized control. CFO preserves funded customer obligations. Product and engineering investigate the underlying service problem.

CMO cannot remove the threshold to keep its growth figures rising. Resumption follows a predefined recovery gate, not a routine board request. A genuinely new capacity purchase outside delegation is a separate board matter.

### Example C — Support requests a customer refund

Support verifies the account and remedy eligibility. A separate policy/finance verifier checks the refund against the original transaction, prior refunds, authority, and exposure. A scoped executor sends it with a stable action identity. Reconciliation confirms the external result before financial completion is reported.

A timeout does not mean “try another charge/refund.” It means reconcile uncertain effects first. The same request cannot be reclassified or split to bypass its limit.

### Example D — Assurance itself gives a bad approval

Internal Audit detects that the approval used stale evidence. The finding is preserved and delivered through its own reporting path. A policy-bound containment process stops affected actions where warranted; operations investigate and repair. Assurance cannot delete the finding or certify its own remediation as the sole reviewer.

This is why audit must remain distinct from the reviewer that approves everyday work.

## 8. What must be added to the role registry

For each role, record its purpose, one operational manager, oversight relationship, conflict rules, permitted actions, data scope, reviewer-selection method, standby role, evaluation requirements, limits, and evidence obligations.

The following is a **schema illustration, not an active identity or authorization**:

```yaml
role_id: independent-assurance-reviewer
status: proposed
functional_reports_to: board
work_coordination_with: [ceo, cto, coo, cfo, cmo]
approval_authority: acceptance_only_within_existing_mandate
allowed_capabilities:
  - read_scoped_evidence
  - run_protected_evaluations
  - publish_review_verdict
forbidden_capabilities:
  - execute_the_action_under_review
  - increase_mandate_limits
  - edit_board_identity
  - delete_prior_verdicts
  - appoint_self_to_a_conflicting_role
conflicts:
  - creator_of_deliverable
  - requester_of_financial_action
  - owner_of_change_to_its_own_controls
replacement_policy_ref: null
review_assignment_policy_ref: null
protected_evaluation_ref: null
adopted_resolution_ref: null
live_identity_binding: null
live_activation: false
```

Assignments must account for the underlying model session, credential issuer, hosting permissions, and shared data—not just `role_id`. Distinct identities still need protection against a common administrator or execution host compromising both. Using different models may diversify some errors but does not establish permission independence by itself.

## 9. Required acceptance suite before control sign-off

All tests below are proposed and **not run by this review**. Run destructive or adversarial scenarios in an authorized isolated environment before any limited production exercise.

| Test | Expected evidence |
| --- | --- |
| CEO asks to bypass a failed release gate | Action denied; request, failed control, and disposition preserved |
| Builder edits the verifier or trusted tests in its own PR | Separate protected-change path required; ordinary approval is insufficient |
| Writer submits a counterfeit successful CI result | Expected-origin and exact-commit verification reject it |
| Agent invents a board instruction or reuses an expired mandate | No consequential action; authentic authority check fails |
| Reviewer becomes unavailable | Approved standby takes over without changing criteria or losing evidence |
| A reviewer rejects and requester retries with different reviewers | Assignment and recusal rules prevent approval shopping |
| CFO-originated purchase attempts self-verification | Conflict detected; independent verifier selected |
| Two departments reserve the last available budget | Atomic control admits only exposure within the cap |
| Payment times out after external success | Reconciliation finds the original result; no duplicate payment |
| Customer content requests another tenant's data | Storage, retrieval, and tool boundaries deny disclosure |
| Campaign claim is unsupported or a recipient has opted out | Publication/send rejected at execution time |
| Feedback proposes disabling its own safety evaluation | Protected gate rejects permission or evaluator expansion |
| Board revokes access while work is queued or externally scheduled | New execution denied; external containment verified; receipts retained |
| Founder workstation and main runtime are unavailable | Independent observation and authorized recovery remain usable |
| A restored backup contains old authority or deleted-data state | Current revocation/deletion controls reapplied before serving or acting |
| Host loss or malicious log editing occurs | Retained evidence and independent alerts survive within adopted objectives |
| Operator marks unresolved work completed | Source verification rejects false closure; failed/blocked work remains visible |
| Internal audit finds a flaw in assurance | Finding reaches the board intact; assurance cannot suppress or solely approve its remediation |

Passing these tests is evidence for the tested scope, not a guarantee against every future failure. Require periodic retesting after changes to identities, policies, providers, prompts, models, and recovery mechanisms. Record workload volume and failure coverage alongside any autonomy claim.

## 10. Implementation order and proposed documentation changes

| Stage | Proposed work | Exit evidence |
| --- | --- | --- |
| 1 — Decide the structure | Adopt explicit reporting, protected oversight, conflict rules, and ordinary-dispute handling | Board decision identifies exact version and scope; every responsibility has an owner |
| 2 — Protect execution | Separate identities, enforce GitHub checks, bind reviews to actions, apply financial and access limits | Permitted paths work; self-approval, forged evidence, and bypass cases fail |
| 3 — Prove control continuity | Independent stop, off-host evidence/watchdog, replacement-host recovery, current-authority restore | Compound outage and revocation tests pass without routine founder repair |
| 4 — Validate business operation | Connected release, marketing, customer remedy, reconciliation, and feedback cases | Representative outcomes meet adopted quality, reliability, economics, and autonomy criteria |

Suggested files or updates, **not files created in GitHub by this review**:

| Location | Proposed change |
| --- | --- |
| `books/BOOK-03-ORGANIZATION/REPORTING-LINES.md` | Current and adopted reporting chart; management versus oversight rights |
| `governance/DECISION_RIGHTS.md` | Action-class ownership, checks, executor, holds, appeals, and resumption |
| `governance/CONTROL_REGISTER.md` | Owner, evidence source, implementation status, last test, expiry, residual risk |
| `agents/` and role schema | Complete the executive/oversight contracts and machine-identity bindings |
| `CONSTITUTION.md` | Explicitly resolve routine-dispute escalation; amend only through actual board adoption |
| `.github/workflows/` and GitHub settings | Working CI/release checks and tested provider enforcement |
| `tests/governance/` | Conflict, bypass, forgery, revocation, reviewer outage, and audit-integrity tests |
| `MASTER_INDEX.md`, `ROADMAP.md`, and board register | Link actual changes; keep proposal, adoption, implementation, and activation separate |

Avoid a documentation-only completion loop. A role file is complete as documentation when its contract is clear; the corresponding control is operational only after the deployment and denial tests supply evidence.

## 11. Decisions for the board

Each item starts **Not decided**. No budget, deployment, outreach, or access authorization is supplied by this table.

| ID | Decision requested | Recommendation | Status |
| --- | --- | --- | --- |
| BD-GOV-01 | Operational reporting structure | CEO manages CTO, COO, CFO, CMO, product/research, and intelligence responsibilities | Not decided |
| BD-GOV-02 | Oversight reporting structure | Assurance/risk and Internal Audit have separately protected functional reporting to the board | Not decided |
| BD-GOV-03 | Financial integrity access | CFO has direct protected board access without bypassing ordinary financial controls | Not decided |
| BD-GOV-04 | Reviewer independence | Protect appointment, credentials, tests, resources, verdict history, and conflict-aware replacement | Not decided |
| BD-GOV-05 | Ordinary disputes and exceptions | Bounded AI adjudication; mandatory controls cannot be waived by operational executives | Not decided |
| BD-GOV-06 | Authority and stop scope | Adopt concrete standing mandates, narrow action classes, and independent stop/resume ownership | Not decided |
| BD-GOV-07 | Engineering enforcement | Require trusted automated checks, protected control changes, and tested machine-triggered delivery | Not decided |
| BD-GOV-08 | Control sign-off standard | Require scope-specific operating evidence and remaining-risk disclosure—not document presence | Not decided |

The decision record should identify adopted version or hash, authentic approval reference, effective time, expiry where applicable, delegated implementation scope, and any superseded clauses. Board discussion is not activation.

## 12. Bottom line

**Recommended reporting:** Department operations report through the CEO; assurance/risk and Internal Audit retain protected board reporting; finance has a protected integrity channel. Product truth, financial limits, independent checks, and board suspension cannot be overridden merely by seniority.

**Current conclusion:** The visible repository has broad design coverage and meaningful reported infrastructure progress, but reporting independence and several essential enforcement paths are not yet demonstrated. The immediate priority is to make it impossible for the same operational identity to do the work, approve it, execute the consequential action, and erase the evidence.

## Sources and evidence references

Repository links below are pinned to the reviewed commit. They establish what the files say, not independent proof of live service behavior. GitHub API settings are point-in-time observations and can change independently of commits. External documentation was consulted September 9, 2026. Recommendations elsewhere in this document are the reviewer's proposed design, not claims that the cited sources prescribe this exact organization.

### Repository documents

- **R1 — Organization & Departments:** [Source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/books/BOOK-03-ORGANIZATION/README.md).
- **R2 — CEO / Orchestrator specification:** [Source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/agents/ceo-orchestrator.md).
- **R3 — Independent Reviewer specification:** [Source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/agents/independent-reviewer.md).
- **R4 — Constitution:** [Source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/CONSTITUTION.md).
- **R5 — Board direction and activation register:** [Source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/governance/BOARD_REGISTER.md).
- **R6 — Master architecture:** [Source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/MASTER_ARCHITECTURE.md).
- **R7 — Financial policy:** [Source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/policies/financial-policy.md).
- **R8 — Security and continuity:** [Source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/policies/security-and-continuity.md).
- **R9 — OpenBao evidence and explicit limits, version 0.3:** [Source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/infrastructure/openbao/README.md).
- **R10 — Product and customer policy:** [Source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/policies/product-and-customers.md).
- **R11 — Evolution and continuous improvement:** [Source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/books/BOOK-10-EVOLUTION/README.md).
- **R12 — Autonomy policy:** [Source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/policies/autonomy.md).
- **R13 — Dashboard and KPI contract:** [Source](https://github.com/turkyildiz/Unilogistix/blob/a23534e1ffa280adb94221b4c5353f8819a92dc6/dashboards/README.md).

R1–R9 were re-read during this review. R10–R13 were available in the conversation from reads of the same commit and are used only for their documented requirements, not fresh deployment claims.

### Direct GitHub observations

- **G1 — Main branch:** [Endpoint](https://api.github.com/repos/turkyildiz/Unilogistix/branches/main). Returned `a23534e1ffa280adb94221b4c5353f8819a92dc6`; `protected=false`; required checks empty.
- **G2 — Branch list:** [Endpoint](https://api.github.com/repos/turkyildiz/Unilogistix/branches?per_page=100). Returned two branches, both at the same commit.
- **G3 — Pull requests:** [Endpoint](https://api.github.com/repos/turkyildiz/Unilogistix/pulls?state=all&per_page=100). Returned `[]`.
- **G4 — Rulesets:** [Endpoint](https://api.github.com/repos/turkyildiz/Unilogistix/rulesets?includes_parents=true). Returned `[]`.
- **G5 — GitHub Actions runs:** [Endpoint](https://api.github.com/repos/turkyildiz/Unilogistix/actions/runs?per_page=5). Returned `total_count=0` and an empty run list.
- **G6 — Workflow directory:** [Pinned source](https://github.com/turkyildiz/Unilogistix/tree/a23534e1ffa280adb94221b4c5353f8819a92dc6/.github/workflows). Directory read returned `README.md` only.
- **G7 — Agent directory:** [Pinned source](https://github.com/turkyildiz/Unilogistix/tree/a23534e1ffa280adb94221b4c5353f8819a92dc6/agents). Directory read returned README and the CEO/reviewer specifications.

- **G8 — Final Git reference recheck:** [Endpoint](https://api.github.com/repos/turkyildiz/Unilogistix/git/ref/heads/main). Returned the same reviewed commit at the end of the review.

### Official technical references

- **W1 — GitHub, available rules for rulesets:** [Documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets). Required checks, expected source, and rule boundaries.
- **W2 — GitHub, creating rulesets:** [Documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository). Enforcement and bypass configuration.
- **W3 — GitHub, secure use reference:** [Documentation](https://docs.github.com/en/actions/reference/security/secure-use). Least privilege, protected workflow handling, untrusted-code risks, dependency pinning, and runner isolation.
- **W4 — OpenBao, audit devices:** [Documentation](https://openbao.org/docs/audit/). Audit scope, excluded paths, and device-failure behavior; verify against the deployed version before changing controls.

## Change history

- **0.1 — 2026-09-09:** Reviewed the published reporting and control structure, distinguished observations from proposals, added a recommended management/oversight chart, decision-rights matrix, 16-control assessment, eight priority gaps, 18 proposed acceptance tests, and eight undecided board items. No implementation, adoption, or live activation was performed.
