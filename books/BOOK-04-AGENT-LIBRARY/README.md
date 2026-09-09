# Agent Library

Version: 0.2 | Updated: 2026-09-09 | Status: Initial specification; runtime not implemented

## Specification and lifecycle

An agent is a versioned role plus executable runtime configuration. A Markdown role specification is not a deployed agent. Use the [agent specification template](../../templates/agent-spec.md) and register each version before activation.

The blueprint's executive, engineering, business, and meta-agent families define coverage. Begin with only the roles required by the first sandbox workflow.

## Required fields

Name, role, mission, responsibilities, non-responsibilities, inputs, outputs, tools, allowed actions, GitHub permissions, KPIs, quality standards, failure conditions, escalation, security, communication format, review frequency, version, and change history.

Also specify owner, mandate binding, model-selection constraints, context and cost limits, permitted data, prompt version, timeout, retry policy, evaluation set, revocation behavior, and retirement plan.

## Creation and promotion

Create a proposal with an unmet workflow need and alternatives. Check overlap with existing roles and expected operating cost. Define success and failure cases before selecting a model. Evaluate in a sandbox with realistic and adversarial inputs.

Promote only after capability, authority-denial, data-isolation, handoff, and recovery checks pass. Record the approved spec, prompt, model/runtime configuration, tool permissions, and evidence. Credentials remain in secret storage.

## Evaluation and retirement

Measure independently verified task quality, policy violations, unsupported claims, escalation accuracy, latency, and cost per accepted outcome. Do not reward task counts without quality.

Version material prompt, model, tool, and scope changes. Test a challenger against a pinned baseline before canary rollout. Roll back regressions.

Retirement prevents new assignments, resolves or transfers active work, revokes credentials, and preserves audit records. Agents may propose their own replacement but cannot silently deploy expanded authority.

## Initial library

[CEO/orchestrator](../../agents/ceo-orchestrator.md) and [independent reviewer](../../agents/independent-reviewer.md) are starter specifications. Other families remain explicit roadmap work, not falsely claimed deployed workers.

## Autonomous operation requirement

Every operational human ask is a failure. Apply [the founder-directed autonomy policy](../../policies/autonomy.md), with AI recovery, honest failure accounting, and no authority bypass. Routine escalations go to AI functions; reserved board decisions remain explicit.

## Chapter coverage

1. Agent Philosophy
2. Agent Classification
3. Standard Agent Specification
4. Executive Agents
5. Product Agents
6. Architecture Agents
7. Backend Agents
8. Frontend Agents
9. QA Agents
10. Security Agents
11. DevOps Agents
12. Data Agents
13. AI / ML Agents
14. UX / UI Agents
15. Research Agents
16. Marketing Agents
17. Social Media Agents
18. Advertising Agents
19. Sales Agents
20. Customer Success Agents
21. Customer Support Agents
22. Chatbot Agents
23. Finance Agents
24. Accounting Agents
25. Legal / Compliance Agents
26. Operations Agents
27. Business Intelligence Agents
28. Audit Agents
29. Knowledge Agents
30. Meta-Agents
31. Agent Creation
32. Agent Evaluation
33. Agent Promotion
34. Agent Retirement
35. Agent Security
36. Agent KPIs

These chapter headings preserve the blueprint's expansion plan. This initial book establishes its operating contract; dedicated chapter specifications will be developed with the corresponding roadmap phase.

## Change history

- 0.2 — 2026-09-09: Added the initial operating contract and retained the blueprint chapter coverage.
