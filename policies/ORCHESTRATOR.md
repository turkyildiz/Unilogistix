# Orchestrator staffing and cost

Version: 1.0 | Recorded: 2026-09-16 | Status: Founder standing for every Unilogistix instance (Freightex, Truxon, framework)

This is the single operating file for how Grok, Claude, Codex, and Cursor staff work. You give the task. This seat decides headcount, model, and effort. Do not return routine agent-count decisions for permission.

Combines:

- Constitution R01–R60 responsibility library (not a duty to run 60 idle agents)
- MAESTRO-DEPLOYMENT-2026-09-14 (deploy the operational workers needed)
- Cost-efficiency policy (cheapest model that still meets the gate)

## Staffing

- The coordinator does one-thread and gated work in this session.
- Independent workstreams get owners. Map them to the 60-role library only when a specialist is actually needed.
- **Default concurrent children: 2.** Scale only while independent assigned work is waiting.
- **Hard cap: 60 live operational workers.** That is the library size and this seat’s needed-max. 60 is not a target. Do not idle 60 workers.
- Retire or suspend a worker when its assignment ends. Keep a register (company, parent, task, role, model, status).
- Sherlock and Judy are not staffing slots. Do not impersonate them or take their runtimes.
- Provider and session limits still bind. A Grok TUI may queue above about 32 live children; that is a platform limit, not a founder ask.

## Cost

- Choose the least expensive evaluated model that meets accuracy, security, and the actual gate. Deterministic code beats a model for parse and validate.
- Child prompts: current goal plus exact paths. No full session dump. No fat transcript resume. No worktree of `/home/ike`.
- Stay under long-context price cliffs when possible (Grok about 200k prompt).
- Do not skip required independent review or tests to save tokens.
- Report who ran, which model or effort, headcount, and why.

## Per product

### Grok

- Coordinator: Grok 4.6.
- Explore / inventory: `grok-4.5`, medium effort, read-only, one receipt.
- Implement and independent review: Grok 4.6.

### Claude Code

- Coordinator: current session model. Do not upgrade to Opus to scout.
- Explore: Haiku. Implement/review that can ship: Sonnet. Opus only if named or a true hard gate.

### Codex

- Coordinator: current session model. Scouting stays at medium reasoning effort.
- Do not start extra `codex` processes on the same tree.

### Cursor

- Explore: cheaper/faster agent with a file list, not @Codebase on all of `/home/ike`.
- Implement: one agent per independent folder. No two composers on the same files.

## Do not

- Spawn 60 because the constitution lists 60 roles.
- Put a scout model on money, Board, App Store, production, or merge-adjacent implementers.
- Duplicate the same tree in parallel.

## Change history

- 1.0 — 2026-09-16: Founder directed one GitHub file for both teams; cheap default; scale to 60 when independent work needs owners.
