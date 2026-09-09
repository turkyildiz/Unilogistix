# Operational playbooks

Version: 0.2 | Updated: 2026-09-09 | Status: Draft specification

Playbooks are execution procedures derived from adopted policies. The initial executable procedure is [autonomous recovery](../workflows/autonomous-recovery.md); incident containment and restoration are specified in [security and continuity](../policies/security-and-continuity.md).

Before live operation, develop and exercise provider-specific playbooks for deployment rollback, service outage, backup restore, credential rotation, failed payment, customer complaint, device loss, supplier failure, and venture handover.

Each playbook names a trigger, prerequisites, authorized commands, state checks, stop conditions, verification, rollback, owner, and evidence location. Do not invent production commands before selecting infrastructure.

## Change history

- 0.2 — 2026-09-09: Added to the blueprint-aligned foundation.
