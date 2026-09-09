# Integrations & Infrastructure

Version: 0.2 | Updated: 2026-09-09 | Status: Initial specification; runtime not implemented

## Modular reference design

Provide replaceable interfaces for source control, CI/CD, models, orchestration, memory, CRM, billing, accounting, identity, notifications, databases, search, storage, events, monitoring, and secrets.

Use the founder-reported Cloudflare, GitHub, Vercel, Supabase, Fireworks.ai, on-prem, and Hetzner pool first. Choose workload placements after capacity, costs, requirements, and account authority are known. Avoid coupling the company's governance to one model or cloud provider.

## Tool registry

Each integration records owner, environment, purpose, API/action allowlist, credential reference, data classification, approval requirements, spend/rate/concurrency caps, timeout, idempotency behavior, retry/reconciliation rules, audit format, health check, revocation procedure, and recovery dependency.

See [integration template](../../templates/integration.md). A tool appearing in a model's tool list does not prove write permission or board authorization.

## Infrastructure boundaries

Separate development, staging, and production identities and data. Use least privilege, secret rotation, network and tenant isolation, authenticated service interfaces, encrypted transport, and access-controlled storage.

Instrument orchestration, tool calls, model usage, queues, customer workloads, and payment effects. Redact logs while retaining useful correlation IDs. Define event delivery and deduplication semantics.

Version infrastructure configuration, dependency identities, and deployment artifacts. Back up authoritative stores and test restoration. Document recovery objectives and supplier failure alternatives.

## Product expansion

Provision isolated product identities, quotas, and accounting boundaries. Sharing a model endpoint or database service does not justify sharing customer access. Replication follows the product handover gate.

Physical integrations require validated devices, approved action limits, interlocks, and local safe states.

## Acceptance

Prove tool denial with insufficient privileges, secret isolation, quota enforcement, duplicate-event handling, gateway revocation, and restore from backup. Verify a replacement implementation can satisfy the same contract.

Current GitHub read access was observed; contents-write returned a permissions error during the initial upload. Do not describe repository write capability as operational until a successful write is verified.

## Autonomous operation requirement

Every operational human ask is a failure. Apply [the founder-directed autonomy policy](../../policies/autonomy.md), with AI recovery, honest failure accounting, and no authority bypass. Routine escalations go to AI functions; reserved board decisions remain explicit.

## Chapter coverage

1. Infrastructure Vision
2. Reference Architecture
3. Cloud Strategy
4. Environments
5. Networking
6. Source Control
7. GitHub
8. CI/CD
9. AI Platform
10. Model Registry
11. Orchestrator Runtime
12. Tool Registry
13. Prompt Management
14. Memory Services
15. CRM
16. Accounting
17. Billing
18. Identity / Access
19. Email
20. Calendar
21. Notifications
22. Document Management
23. API Gateway
24. Authentication
25. Databases
26. Object Storage
27. Search
28. Event Bus
29. Messaging
30. Monitoring
31. Logging
32. Secrets
33. Security
34. Backups
35. Disaster Recovery
36. Infrastructure as Code
37. Deployment Strategies
38. Scaling
39. Vendor Management
40. Multi-Product Infrastructure
41. Future Expansion

These chapter headings preserve the blueprint's expansion plan. This initial book establishes its operating contract; dedicated chapter specifications will be developed with the corresponding roadmap phase.

## Cost and existing capacity

Apply [cost-efficiency policy](../../policies/cost-efficiency.md): reuse suitable existing resources, measure total cost per verified outcome, preserve reliability and zero-human operations, and reserve new purchases beyond delegated limits for the board. Provider availability is not a spending cap.

## Change history

- 0.2 — 2026-09-09: Added the initial operating contract and retained the blueprint chapter coverage.
