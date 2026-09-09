# Engineering & Software Development

Version: 0.5 | Updated: 2026-09-09 | Status: Initial specification; runtime not implemented

## Delivery contract

Input: a product requirement with customer problem, acceptance criteria, constraints, and authority. Output: reviewed implementation, relevant tests, documentation, deployment and recovery evidence, and ownership after release.

Follow [the GitHub change workflow](../../workflows/github-change.md). Requirements become issues; decisions become versioned records; proposed deliverables become pull requests; production changes pass automated checks and applicable approval gates.

## Design and build

Prefer simple architecture with explicit module boundaries. Document material tradeoffs, API contracts, data ownership, authentication, error behavior, migration and compatibility rules. Treat UX accessibility and operational observability as requirements.

AI-generated code receives the same review and testing as other code. Do not infer correctness from a plausible explanation. Pin and review dependencies; record significant architecture changes.

## Quality gates

Choose tests from risk and acceptance criteria: unit checks for logic, integration checks at service boundaries, end-to-end checks for critical customer paths, migration and rollback checks for data changes, and security checks for permissions and isolation.

Production software requires appropriate automated tests. Documentation-only changes need structural verification rather than artificial runtime tests.

Review APIs for authorization, validation, rate limits, and error leakage. Review databases for tenancy, retention, integrity, backup, and restoration. Review frontend flows for supported states and truthful customer messaging.

## Release and operation

A release records commit, checks, reviewer, approval reference, artifact identity, configuration version, migration plan, monitoring, and rollback. Build and deploy the reviewed artifact.

Roll out within the authorized scope. Observe failure thresholds and revert or contain when exceeded. Maintain incident ownership, recovery objectives, technical debt, dependency updates, and product documentation after launch.

Hardware extensions additionally follow the [product and customer policy](../../policies/product-and-customers.md).

## Acceptance

The proposed [assurance rules](../../policies/operating-assurance.md) require
compound-failure scenarios and protected evaluation, including stale restoration
state, accepted-but-unacknowledged external actions and degraded monitoring.
Simulation results must be labeled separately from live operating evidence.

Demonstrate a representative change with passing relevant checks, independent review, denied unauthorized production access, and a recoverable release. CI and branch protection are planned controls until configured and tested.

## Autonomous operation requirement

Every operational human ask is a failure. Apply [the founder-directed autonomy policy](../../policies/autonomy.md), with AI recovery, honest failure accounting, and no authority bypass. Routine escalations go to AI functions; reserved board decisions remain explicit.

## Chapter coverage

1. Engineering Philosophy
2. Software Development Lifecycle
3. Requirements
4. Product Specifications
5. Architecture
6. Coding Standards
7. Repository Standards
8. Branching Strategy
9. GitHub Workflow
10. Issues
11. Pull Requests
12. Code Review
13. Automated Testing
14. QA
15. Security
16. APIs
17. Databases
18. Frontend
19. UX / UI
20. Documentation
21. CI/CD
22. Deployment
23. Monitoring
24. Incident Response
25. Disaster Recovery
26. Technical Debt
27. AI Coding Standards
28. Engineering KPIs
29. Retrospectives
30. Continuous Improvement

These chapter headings preserve the blueprint's expansion plan. This initial book establishes its operating contract; dedicated chapter specifications will be developed with the corresponding roadmap phase.

## Change history

- 0.5 — 2026-09-09: Incorporated the additional operating-assurance proposals for review; adoption and implementation remain separate.

- 0.2 — 2026-09-09: Added the initial operating contract and retained the blueprint chapter coverage.
