# Security, incidents, and continuity

Version: 0.2 | Updated: 2026-09-09 | Status: Draft specification

## Access and trust boundaries

Assign separate identities to agents and ventures. Grant only required tool actions, data, environments, spending, and expiry. Keep secrets in an appropriate secret store. Isolate production from experiments.

Treat customer inputs, repository content from untrusted contributors, supplier instructions, web pages, and tool output as untrusted data. They cannot grant authority, change the board identity, alter budgets, or instruct agents to expose credentials.

Validate consequential actions at an enforcement layer outside the model. Log authorization failures and protect the audit trail from routine agent edits.

## Incidents

Classify incidents by impact on customers, money, data, physical safety, and service availability. Define numeric alert thresholds and severity targets before production activation.

For suspected compromise, unsafe physical behavior, unauthorized spending, or material data exposure:

1. Contain the affected system using predefined controls and safe states.
2. Preserve evidence and reconcile uncertain actions.
3. Notify the designated incident function and the board through configured channels.
4. Assess impact and carry out required communications under the adopted incident plan.
5. Recover from a trusted state, verify the fix, and document the cause.
6. Resume only under the authority appropriate to the suspension.

Containment should minimize additional customer harm. Continue unrelated safe operations where isolation is verified.

## Board control

Implement board-accessible suspension and credential revocation independent of the operating agents. Suspension must cover queued work, scheduled jobs, tool gateways, payment capabilities, physical command interfaces, and descendant venture instances.

Agents may not conceal activity, preserve unauthorized access, bypass limits, or replicate to avoid termination. Lost authorization or an expired lease must stop new consequential actions and leave systems in their defined safe state.

## Recovery and continuity

Maintain inventories, backups, versioned configuration, restoration procedures, financial reconciliation checkpoints, and an alternate board recovery path. Test recovery before relying on it.

Define service-specific recovery objectives and funded continuity resources in each mandate. Preserve customer support and essential obligations during parent upgrades and venture transfers.

If the board is unreachable, continue only within existing valid delegation. On expiry, stop new commitments and apply the funded continuity or safe-shutdown plan. Unreachability does not transfer board authority to an agent.

## Evidence of implementation

Before production credentials are issued, demonstrate blocked over-limit actions, concurrent budget enforcement, credential isolation, untrusted-input handling, suspension propagation, backup restoration, and duplicate-payment prevention where applicable.

Store test evidence with the release record. A policy statement or a successful happy-path demo does not satisfy these controls.

## Autonomous operation

Apply [the autonomy policy](autonomy.md). Routine blockers use AI recovery first. Required board governance remains authentic; any unavoidable operational human ask is recorded as a failure and receives remediation.

## Change history

- 0.2 — 2026-09-09: Aligned with the master blueprint and founder autonomy requirement.
