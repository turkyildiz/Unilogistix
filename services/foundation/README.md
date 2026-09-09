# Local task execution foundation

Version: 0.1 | Updated: 2026-09-09 | Status: Local sandbox implementation; production incomplete

The SQLite task store persists submissions, attempt limits, deadlines, leases,
results and ordered audit events. State and audit updates share a transaction.
Expired leases are recovered when a worker next claims work. A unique lease
token prevents a previous worker from completing a reclaimed task. Duplicate
submission IDs must bind the same input and limits.

Run a deterministic local draft task with a database outside the repository:

```bash
python3 services/foundation/sandbox.py --db /tmp/uni-sandbox.sqlite submit demo "Prepare a sandbox deliverable"
python3 services/foundation/sandbox.py --db /tmp/uni-sandbox.sqlite step
python3 services/foundation/sandbox.py --db /tmp/uni-sandbox.sqlite status demo
python3 scripts/check_runtime.py
```

The step command records a placeholder deliverable. Completion means that local
step completed; independent review remains pending. It does not execute the
objective through an AI worker. Caller processes are trusted and must use the
same concurrency configuration. Lease tokens are coordination tokens, not
authenticated workload identities. Use a private local database directory;
customer records and secrets do not belong in this sandbox.

## Publication boundary

This records an earlier local experiment. Its runtime source and tests are not part
of the documentation-only GitHub publication; commands above describe that local
workspace experiment, not a runnable feature delivered by this document commit.

## Remaining operational requirements

UNI-002 remains partial: service supervision, workflow checkpoints, recurring
schedules, authorization checks, AI execution and failure-queue operations are
not implemented. The queue recovers after a process exits, but does not prove
safe retry after an external provider succeeds. External effects require a
separate authorized gateway with idempotency and reconciliation. SQLite audit
rows are transactional, not tamper-proof against a database administrator.
Deployment, independent review and host-loss restore testing remain pending.

## Change history

- 0.1 — 2026-09-09: Added sandbox persistence and failure-recovery acceptance tests.
