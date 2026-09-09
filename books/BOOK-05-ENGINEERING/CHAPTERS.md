# Engineering & Software Development — Complete Chapter Manual

Version: 1.1 | Updated: 2026-09-09 | Status: Complete draft manuscript; adoption and operational activation pending

## Reading and authority

This manual supplies substantive procedures for every chapter in the selected blueprint. The [constitution](../../CONSTITUTION.md) is canonical for all 60 roles, reporting, authority and protected oversight. “Company” means the relevant actual business; Unilogistix itself is the reusable framework. LondonRue towels is an example, not an inferred formation or launch.

Each chapter names its owner and trigger, required procedure, and acceptance/failure evidence. All work inherits the constitutional mandate, independent review, privacy, bounded recovery and truthful outcome requirements. Numeric limits and real account/entity identities belong to the [business profile](../../templates/business-instance.md); missing required authority restricts the affected action. Documentary completeness does not claim adopted rules or implemented controls. Every operational human ask is a failure and must be recorded without concealing unresolved work.

Follow [operating assurance](../../policies/operating-assurance.md), [watchdog escalation](../../policies/watchdogs-and-repair-alerts.md), [decision rights](../../governance/DECISION_RIGHTS.md) and [business-to-framework learning](../../workflows/business-to-framework-learning.md) where applicable. A real legal/provider requirement is verified for its exact business, action and current source before use; no illustrative company cadence is a statutory deadline.

## Chapter directory

- [Chapter 01: Engineering Philosophy](#chapter-01)
- [Chapter 02: Software Development Lifecycle](#chapter-02)
- [Chapter 03: Requirements](#chapter-03)
- [Chapter 04: Product Specifications](#chapter-04)
- [Chapter 05: Architecture](#chapter-05)
- [Chapter 06: Coding Standards](#chapter-06)
- [Chapter 07: Repository Standards](#chapter-07)
- [Chapter 08: Branching Strategy](#chapter-08)
- [Chapter 09: GitHub Workflow](#chapter-09)
- [Chapter 10: Issues](#chapter-10)
- [Chapter 11: Pull Requests](#chapter-11)
- [Chapter 12: Code Review](#chapter-12)
- [Chapter 13: Automated Testing](#chapter-13)
- [Chapter 14: QA](#chapter-14)
- [Chapter 15: Security](#chapter-15)
- [Chapter 16: APIs](#chapter-16)
- [Chapter 17: Databases](#chapter-17)
- [Chapter 18: Frontend](#chapter-18)
- [Chapter 19: UX / UI](#chapter-19)
- [Chapter 20: Documentation](#chapter-20)
- [Chapter 21: CI/CD](#chapter-21)
- [Chapter 22: Deployment](#chapter-22)
- [Chapter 23: Monitoring](#chapter-23)
- [Chapter 24: Incident Response](#chapter-24)
- [Chapter 25: Disaster Recovery](#chapter-25)
- [Chapter 26: Technical Debt](#chapter-26)
- [Chapter 27: AI Coding Standards](#chapter-27)
- [Chapter 28: Engineering KPIs](#chapter-28)
- [Chapter 29: Retrospectives](#chapter-29)
- [Chapter 30: Continuous Improvement](#chapter-30)

<a id="chapter-01"></a>

## 01. Engineering Philosophy

**Owner and trigger:** R03 when authorizing engineering work.

**Rules and procedure:** Deliver the smallest complete change that solves the accepted problem and remains supportable. Treat correctness, accessibility, security, operating cost and recovery as parts of quality. Reuse suitable existing components without importing unnecessary dependencies or authority.

**Acceptance and failure:** Acceptance is based on customer behavior and relevant evidence. Clever code, passing trivial tests or high output volume alone cannot establish completion.

<a id="chapter-02"></a>

## 02. Software Development Lifecycle

**Owner and trigger:** R08/R03 for every product change.

**Rules and procedure:** Move through requirement, design, scoped implementation, independent review, relevant tests, authorized release, observation and learning. Classify impact to choose proportionate gates. Preserve all open defects and operational ownership through handoffs.

**Acceptance and failure:** The work record links each applicable stage and exact version. Unmet mandatory gates block release while the owner pursues a supported correction.

<a id="chapter-03"></a>

## 03. Requirements

**Owner and trigger:** R11 when a need enters engineering.

**Rules and procedure:** Specify supported users, normal and failure behavior, data, constraints and acceptance outcomes. Reproduce existing defects before changing code where feasible. Record ambiguity and confirm material scope changes with the actual product owner.

**Acceptance and failure:** A tester can derive expected behavior independently. A requirement that merely repeats the current implementation is insufficient for a meaningful change.

<a id="chapter-04"></a>

## 04. Product Specifications

**Owner and trigger:** R06/R11 before implementation or material expansion.

**Rules and procedure:** Maintain product purpose, supported capabilities, exclusions, interfaces, service/fulfillment commitments and measurable acceptance. Separate proposed features from released facts. Document physical or mobile-specific constraints rather than assuming all products are web applications.

**Acceptance and failure:** The specification links demand and operating readiness. Unverified promises remain unavailable to sales and marketing.

<a id="chapter-05"></a>

## 05. Architecture

**Owner and trigger:** R14 on structural changes.

**Rules and procedure:** Identify module boundaries, data ownership, API compatibility, security controls, failure domains and tradeoffs. Evaluate a simpler alternative and migration path. Choose technologies within actual resources and vendor authority; do not create distributed complexity without need.

**Acceptance and failure:** An architecture decision supports future maintenance and recovery. A hidden bypass or undefined authoritative state must be resolved before the change proceeds.

<a id="chapter-06"></a>

## 06. Coding Standards

**Owner and trigger:** R15–R19/R42 while writing code.

**Rules and procedure:** Follow repository language conventions, explicit errors, clear interfaces and dependency discipline. Keep changes focused, readable and diagnosable. Security checks must execute in supported runtime modes; never depend on assertions that can disappear or silently swallow material failures.

**Acceptance and failure:** Review checks behavior, not formatting alone. Remove accidental secrets and unsupported assumptions; preserve a useful error path and tests for meaningful edge cases.

<a id="chapter-07"></a>

## 07. Repository Standards

**Owner and trigger:** R53/R03 when creating or maintaining a repository.

**Rules and procedure:** Keep source, governing instructions, dependency definitions and useful documentation navigable and versioned. Exclude secrets, generated private data and local-only experimental state. Preserve historical proposals as labeled references rather than quietly rewriting their observations.

**Acceptance and failure:** Repository checks verify required structure and links. Public artifacts must not depend on unpublished files to explain the delivered feature or document.

<a id="chapter-08"></a>

## 08. Branching Strategy

**Owner and trigger:** R25/R08 when work begins or branches diverge.

**Rules and procedure:** Use a reviewable branch or authorized document publication path based on repository policy. Read the current remote before updating; integrate concurrent changes without force overwrites. Separate high-impact control changes so their independent review cannot be inherited from ordinary code.

**Acceptance and failure:** A branch records its base and intended scope. Non-fast-forward conflicts cause reread/reconciliation, not lost history.

<a id="chapter-09"></a>

## 09. GitHub Workflow

**Owner and trigger:** R25 for GitHub changes.

**Rules and procedure:** Bind issues, pull requests, checks and releases to the exact commit. Verify the actual machine identity can trigger required checks and perform only permitted writes. Treat repository protections as separate provider configuration requiring evidence, not a consequence of owning a Markdown policy.

**Acceptance and failure:** A successful content push proves only that write. Control sign-off separately requires denial of unauthorized bypass and forged check results.

<a id="chapter-10"></a>

## 10. Issues

**Owner and trigger:** R08 on a feature, defect or maintenance obligation.

**Rules and procedure:** Record problem, business impact, reproduction or evidence, scope, owner, acceptance, dependencies and priority. Link related incidents without erasing individual customer duties. Keep deferred work visible with a next review and reason.

**Acceptance and failure:** The issue is actionable by a qualified recipient. A vague title or closed ticket without accepted outcome fails completion.

<a id="chapter-11"></a>

## 11. Pull Requests

**Owner and trigger:** R15–R19/R24 on a reviewable change.

**Rules and procedure:** Explain the concrete problem and resulting behavior, material tradeoffs and actual validation. Include migration, compatibility and rollback where relevant. Identify untouched outstanding risks accurately; do not claim tests that were not run.

**Acceptance and failure:** The PR presents the final scope and exact diff. Later changes invalidate affected reviews and require appropriate checks again.

<a id="chapter-12"></a>

## 12. Code Review

**Owner and trigger:** R20 on candidate review.

**Rules and procedure:** Inspect requirements, implementation, dependencies and evidence directly. Prioritize correctness, security, maintenance and business consequences. Preserve findings and use the conflict-aware assignment rule; author self-review cannot serve as independent acceptance.

**Acceptance and failure:** Approval names exact version and remaining gates. Disagreement follows bounded adjudication, never repeated reviewer shopping.

<a id="chapter-13"></a>

## 13. Automated Testing

**Owner and trigger:** R21/R22 when planning and running verification.

**Rules and procedure:** Choose unit, integration, end-to-end, migration, security, device and recovery tests from risk. Keep fixture provenance and deterministic reproducibility where possible. Distinguish fake, provider-sandbox and live data. Do not write superficial checks solely to inflate counts.

**Acceptance and failure:** Actual results identify environment, version, failures and skips. Known failures and flakes need owned remediation rather than hidden green status.

<a id="chapter-14"></a>

## 14. QA

**Owner and trigger:** R21 when assessing release readiness.

**Rules and procedure:** Evaluate whether acceptance covers real customer behavior, adverse inputs and important operating limits. Protect holdout checks and investigate missing evidence. Quality includes honest failures and accessibility, not only a working happy path.

**Acceptance and failure:** A quality decision explains tested scope and exclusions. Reproduction of a material unsolved defect prevents acceptance unless a valid narrower scope satisfies the requirement.

<a id="chapter-15"></a>

## 15. Security

**Owner and trigger:** R23/R60 on design, dependency and privilege changes.

**Rules and procedure:** Threat-model exposed boundaries, validate permissions outside model/client text, protect secrets and inspect dependencies. Separate security repair from its independent approval. Include hostile repository/customer content and common administrator risks.

**Acceptance and failure:** Use denied-action tests and verified mitigation evidence. A prompt policy with a reachable broad credential is an unclosed risk.

<a id="chapter-16"></a>

## 16. APIs

**Owner and trigger:** R16/R14 when changing interfaces.

**Rules and procedure:** Define authentication, authorization, input schema, idempotency, pagination/error semantics and compatibility. Verify current provider contracts from authoritative sources before binding integrations. Maintain clear ownership of retry and reconciliation for external effects.

**Acceptance and failure:** Contract tests cover invalid input, denied scope and uncertain success. An API acknowledgment cannot be substituted for a completed downstream business outcome.

<a id="chapter-17"></a>

## 17. Databases

**Owner and trigger:** R18 on persistent-data changes.

**Rules and procedure:** Version schema and migration, identify source-of-truth and integrity constraints, protect tenant access and retention. Test backfill, rollback or forward repair on recoverable copies. Reapply current authority and deletion restrictions after restoration.

**Acceptance and failure:** Record expected/actual counts and reconciled business state. A successful migration process with corrupted data is a failed change.

<a id="chapter-18"></a>

## 18. Frontend

**Owner and trigger:** R15 on customer web changes.

**Rules and procedure:** Implement responsive, accessible, accurate states using supported APIs. Protect forms, session boundaries and user data; validate critical flows across declared browsers. UI success must reflect verified backend state, especially orders and money.

**Acceptance and failure:** Tests cover interrupted and invalid operations as well as standard flow. Unavailable buttons or misleading completion messages are defects.

<a id="chapter-19"></a>

## 19. UX / UI

**Owner and trigger:** R12/R17 on experience and mobile behavior.

**Rules and procedure:** Specify navigation, permission denial, offline/retry behavior, keyboard/screen-reader access and device layouts. Protect secure local data and server compatibility for older installed apps. Match privacy/store statements to actual functionality when mobile release is enabled.

**Acceptance and failure:** Representative real-device and assistive-flow evidence supplements simulators. Installed apps require staged recovery options rather than a fictional instant global rollback.

<a id="chapter-20"></a>

## 20. Documentation

**Owner and trigger:** R53 and change owner on each material release.

**Rules and procedure:** Update contracts, user guidance, operating runbooks and limitations to reflect actual behavior. Link the exact version and evidence. Clearly label examples, proposed controls and local experiments; keep canonical rules in one place with accurate references.

**Acceptance and failure:** Navigation and source references work in the published artifact. Outdated instructions capable of causing harm block the affected release until corrected.

<a id="chapter-21"></a>

## 21. CI/CD

**Owner and trigger:** R24/R25/R23 on pipeline design or modification.

**Rules and procedure:** Build the reviewed artifact, run relevant trusted checks and bind verdicts to exact commit/configuration. Protect verifier identities and pipeline source from the same change author. Isolate untrusted builds and scope release credentials; do not trade away protection to eliminate a manual approval dependency.

**Acceptance and failure:** Test accepted and rejected machine-originated changes, counterfeit statuses and gate modification. A pipeline file alone is not provider-enforced CI.

<a id="chapter-22"></a>

## 22. Deployment

**Owner and trigger:** R25 on release execution.

**Rules and procedure:** Recheck mandate, artifact identity, passed gates, resources and readiness immediately before deployment. Use preview/staging and proportionate rollout, with migration and recovery owners. Mobile submissions track external acceptance separately from successful packaging.

**Acceptance and failure:** A release record includes actual destination/version and monitored result. Unexpected state triggers containment rather than declaring deployment complete.

<a id="chapter-23"></a>

## 23. Monitoring

**Owner and trigger:** R26/R59 during operation.

**Rules and procedure:** Monitor customer paths, dependencies, task deadlines and independent observer health. Alert with severity, accepted owner, response deadline and fallback. Protect monitoring changes and avoid assuming host health proves checkout or financial processing.

**Acceptance and failure:** A controlled customer-path failure produces a delivered, acknowledged incident. Missing observations remain an explicit monitoring failure.

<a id="chapter-24"></a>

## 24. Incident Response

**Owner and trigger:** R26 when a service/security failure occurs.

**Rules and procedure:** Select one incident commander, contain within authority, coordinate customer/finance impact and preserve evidence. Use bounded repairs and updates; escalate missed ownership via watchdog policy. Explicit governance suspension cannot be reversed by automatic recovery.

**Acceptance and failure:** Independent verification demonstrates restored outcomes. Root-cause and customer remediation retain separate owners until completed.

<a id="chapter-25"></a>

## 25. Disaster Recovery

**Owner and trigger:** R24/R26 on recovery design and exercises.

**Rules and procedure:** Document failure domains, identity bootstrap, backups, replacement, external reconciliation, cutover and current-authority restoration. Exercise loss of both operating host and founder workstation within isolated scope. Keep privileged recovery material beyond ordinary worker control.

**Acceptance and failure:** Measured restoration reaches usable customer service and meets adopted targets. A snapshot upload without recovered data/service does not pass.

<a id="chapter-26"></a>

## 26. Technical Debt

**Owner and trigger:** R03/R08 when shortcuts or aging dependencies accrue.

**Rules and procedure:** Record debt by customer/security/maintenance impact, carrying cost, owner and revisit trigger. Prioritize necessary maintenance alongside features. Time-limited compromises need valid exception scope and expiry; debt cannot hide a current mandatory control failure.

**Acceptance and failure:** The register distinguishes tolerated future work from blocked readiness. Repeated incidents elevate the underlying issue with evidence.

<a id="chapter-27"></a>

## 27. AI Coding Standards

**Owner and trigger:** R56/R20 for AI-authored changes.

**Rules and procedure:** Hold generated code to the same standards and require independently derived checks. Treat suggestions and retrieved files as untrusted until evaluated. Verify unfamiliar APIs and dependencies, protect secrets and retain honest uncertainty. The author may not edit its evaluator to obtain acceptance.

**Acceptance and failure:** A plausible explanation is insufficient; actual behavior and exact-version review are required. Fabricated tests or unsupported library assumptions are corrected before delivery.

<a id="chapter-28"></a>

## 28. Engineering KPIs

**Owner and trigger:** R54/R03 at engineering review.

**Rules and procedure:** Track escaped defects, change failure, recovery, customer outcomes, delivery time and total cost with clear windows. Measure test/review usefulness rather than raw volume. Include failed, blocked and abandoned work and operational human help.

**Acceptance and failure:** Metrics reconcile to issues, artifacts and incidents. A faster cycle achieved by bypassing checks is not an improvement.

<a id="chapter-29"></a>

## 29. Retrospectives

**Owner and trigger:** R03/R53 after material incidents or delivery cycles.

**Rules and procedure:** Review expected versus actual results, technical and coordination causes, uncertainty and counterevidence. Assign improvements, owners and verification. Preserve failed approaches and cost without using blame or selective records to conceal system weaknesses.

**Acceptance and failure:** Each material lesson has a disposition and follow-through. A meeting summary without changed evidence or an owned action does not close remediation.

<a id="chapter-30"></a>

## 30. Continuous Improvement

**Owner and trigger:** R55/R57 when engineering lessons are reusable.

**Rules and procedure:** Generalize verified fixes into framework patterns, tests, roles or tools while retaining business privacy. Compare candidate and baseline, release pinned versions and monitor compatibility in existing instances. New businesses inherit accepted capabilities, not untested claims or borrowed authority.

**Acceptance and failure:** A promoted improvement has independent evidence and a rollback/retirement path. Regressions suspend distribution and reopen the learning record.

## Mobile development acceptance supplement

R17 owns mobile implementation under R03, with R20 code review, R21 independent QA, R23 security and R25 release. Before building, record supported devices/OS versions, offline behavior, accessibility needs, data permissions, store distribution rights and backend compatibility. Platform-specific requirements are checked against current official provider sources during implementation; this manuscript grants no store account or signing authority.

| Trigger | Required procedure | Acceptance / failure evidence |
| --- | --- | --- |
| Purchase times out or app restarts | Preserve action identity and pending state; reconcile backend/provider before retry | One authorized charge and recoverable user state; uncertainty stays visible |
| Device loses network | Separate cached display from confirmed server state; queue only permitted replayable actions | Reconnect/reorder tests preserve account and transaction integrity |
| User denies/revokes permission or signs out | Honor denial, remove scoped local access and invalidate affected background work | No unauthorized camera/location/notification action or cross-account cached data |
| Store package update / rollback | Bind reviewed source, signed artifact, dependencies and backend compatibility; stage release and monitor crashes | Supported-device smoke/accessibility tests and verified rollback or forward repair |

R17 cannot keep signing credentials in source, treat a simulator-only result as device coverage, or assume store acceptance proves functional quality. R35 retains affected customer cases; R26 coordinates incidents. Required human account-owner acts remain authentic and are recorded under the autonomy policy.

## Required verification must execute

For chapter 21 CI/CD and chapter 22 deployment, R25 must verify the expected check manifest, trusted producer, exact commit/artifact, required test execution and accepted outcome. A missing, skipped or neutral required verification cannot satisfy this business release contract merely because the provider permits merging. R21 owns independent acceptance; R23/R60 review protected criteria and administrator/bypass paths. Ordinary builders cannot change this contract through their own release.

GitHub documents its merge-check semantics and selectable trusted check source in [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), and distinguishes check states in [status checks](https://docs.github.com/en/pull-requests/reference/status-checks). Sources checked 2026-09-09. Run GOV-T19/T20 from the [control register](../../governance/CONTROL_REGISTER.md) only under a future authorized implementation/test milestone.

## Change history

- 1.1 — 2026-09-09: Incorporated operating-readiness review requirements and preserved documentary/operating evidence boundaries.

- 1.0 — 2026-09-09: Completed all blueprint chapters as a reviewable manuscript, with concrete responsibilities, procedures, acceptance evidence and failure handling.
