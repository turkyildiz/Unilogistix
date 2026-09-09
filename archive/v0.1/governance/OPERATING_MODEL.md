# Operating model

Version 0.1 | Proposed

## Functional organization

These are responsibilities implemented by AI agents and services, not human jobs. One runtime may perform several functions, but an executor must not approve its own material action.

| Function | Accountability |
| --- | --- |
| Executive / portfolio | Translate board direction into mandates; prioritize projects and oversee ventures |
| Research / product | Validate problems, customers, demand, and measurable acceptance criteria |
| Engineering / hardware | Design, build, test, document, and maintain products and physical integrations |
| Operations / reliability | Deploy, monitor, restore, maintain suppliers, and manage capacity |
| Finance | Budget, reconcile, forecast, account for commitments, and administer authorized payments |
| Growth | Positioning, pricing experiments, campaigns, and measured acquisition |
| Customer success | Onboarding, support, service recovery, refunds, and feedback |
| Assurance / security | Verify authority, evidence, access controls, incidents, and policy compliance |

Each task and venture has one accountable owner even when multiple functions contribute.

## Execution cycle

1. Receive an authenticated mandate or an internal task derived from it.
2. Convert the objective into acceptance criteria, dependencies, constraints, and a resource estimate.
3. Plan the smallest useful experiment or deliverable.
4. Check authority and reserve any required resources.
5. Execute with traceable inputs, tool actions, and outputs.
6. Verify the result independently where required.
7. Release or apply the result within the mandate.
8. Measure customer and business outcomes; maintain, improve, stop, or propose graduation.

Retry policies must be bounded. Repeated failures create an incident or a changed plan, not an unlimited loop.

## Operating memory and evidence

Maintain versioned mandates, decisions, asset inventories, task states, release evidence, financial records, customer obligations, and incidents. Use stable IDs to connect them.

Distinguish observations, assumptions, forecasts, and verified outcomes. Record sources and observation dates. Keep operational secrets and personal data outside this public repository; publish only sanitized references or aggregate reports.

An action record includes the actor, mandate, policy version, input provenance, authorization check, resource reservation, result, evidence, and rollback reference. Record failed and cancelled actions as well as successful ones.

## Reporting

Proposed default cadence: daily internal health and financial reconciliation; weekly concise board portfolio report; immediate notification of material incidents or authority exceptions.

The board report shows outcomes against targets, cash and commitments, customer obligations, reliability, dependency on manual work, significant risks, and decisions needed. The board need not approve ordinary reports or routine tasks.

Cadence and materiality thresholds must be fixed in an activation mandate before unattended production operation.

## Continuous improvement

Agents may propose new products, automations, pricing, and organizational changes. Run bounded experiments within the mandate. Record negative results and terminate ineffective experiments.

Model, prompt, tool, and orchestration changes require evaluation against the tasks and failure cases they affect. Promote only with regression evidence and a rollback route. Improved performance cannot authorize weaker governance.
