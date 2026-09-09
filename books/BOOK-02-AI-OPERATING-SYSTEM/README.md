# AI Operating System

Version: 0.5 | Updated: 2026-09-09 | Status: Initial specification; runtime not implemented

## Runtime responsibilities

The CEO/orchestrator translates objectives into durable tasks, resolves dependencies, routes to qualified role versions, schedules bounded execution, and assembles evidence for review. It is not a privileged all-purpose tool executor.

Input: an authenticated objective and mandate. Output: verified deliverables, audit records, status, cost, and follow-up tasks. See the [architecture](../../MASTER_ARCHITECTURE.md).

## Task and handoff contract

Each task stores ID, parent objective, product, owner, required role, policy and agent versions, status, acceptance criteria, dependencies, deadline, attempt count, cost reservation, sensitivity, and evidence references.

Every significant handoff contains objective, context, constraints, expected deliverable, dependencies, assumptions, risks, confidence with rationale, acceptance criteria, and next action. Use [the handoff template](../../templates/handoff.md).

## Durable state machine

Intake → planned → ready → running → review → completed. Review may route to awaiting-approval and back to ready after valid approval, or to running for revisions. Any nonterminal task may become failed or cancelled with a reason. Dependency failure blocks dependents; it does not silently remove the dependency.

Workers claim renewable leases. Each external action has a stable idempotency key. Persist the result before task completion. On lease loss or restart, reconcile uncertain external effects before retrying. Apply bounded retry, timeout, queue concurrency, and cost limits.

## Routing and controls

Apply the proposed [connected operating rules](../../policies/operating-assurance.md)
for evidence-based task closure, consistent customer state, action-specific
qualification and scheduling under a shared operation budget. Qualification is
distinct from role title and authority; child tasks cannot expand the envelope.

Route by capability, permissions, data sensitivity, evaluation results, and available budget. Escalation to a more capable model still uses the same authority. Gate tools outside the model and recheck revocations at execution.

GitHub stores work definitions and deliverables; runtime state belongs in a durable operational store with linked IDs. Memory retrieval must enforce product boundaries.

## Acceptance

A sandbox objective must survive a worker crash and duplicate delivery without duplicate external effects. Invalid permissions must be denied, missing approvals queued, and board suspension propagated. Report verified completion rate, wait time, failure recovery, model cost, and unsupported claims.

The current repository specifies this runtime; it does not implement it.

## Autonomous operation requirement

Every operational human ask is a failure. Apply [the founder-directed autonomy policy](../../policies/autonomy.md), with AI recovery, honest failure accounting, and no authority bypass. Routine escalations go to AI functions; reserved board decisions remain explicit.

## Chapter coverage

1. Executive Summary
2. AIOS Architecture
3. CEO / Orchestrator
4. Agent Routing
5. Department Hierarchy
6. Task Management
7. Planning and Decomposition
8. Agent Communication Protocol
9. GitHub Integration
10. Memory Integration
11. Knowledge Integration
12. Decision Frameworks
13. Human Approval Gates
14. Risk Controls
15. Monitoring
16. Metrics
17. Failure Recovery
18. Continuous Improvement
19. Version Control
20. Appendices

These chapter headings preserve the blueprint's expansion plan. This initial book establishes its operating contract; dedicated chapter specifications will be developed with the corresponding roadmap phase.

## Change history

- 0.5 — 2026-09-09: Incorporated the additional operating-assurance proposals for review; adoption and implementation remain separate.

- 0.2 — 2026-09-09: Added the initial operating contract and retained the blueprint chapter coverage.
