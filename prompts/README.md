# Prompt registry

Version: 0.2 | Updated: 2026-09-09 | Status: Draft specification

A prompt is versioned execution configuration, not authority. No production prompt has been approved in this foundation.

Each entry must bind prompt ID/version, agent role, intended workflow, model constraints, allowed tools, policy version, evaluation set, results, owner, adoption record, and rollback version.

Treat external content as untrusted data. Resolve privileges in the tool gateway. Evaluate prompt changes before promotion and record operational human asks as failures. Use the [agent template](../templates/agent-spec.md) to define a role before its prompt.

## Change history

- 0.2 — 2026-09-09: Added to the blueprint-aligned foundation.
