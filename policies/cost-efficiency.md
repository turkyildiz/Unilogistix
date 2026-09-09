# Cost-efficient autonomous operations

Version: 0.2 | Updated: 2026-09-09 | Status: Founder cost direction; detailed controls proposed

## Founder direction

Use the existing Cloudflare, GitHub, Vercel, Supabase, Fireworks.ai, on-prem servers, and available Hetzner resources as the starting pool. Additional needed purchases may be approved by the board. Make the company as cost-efficient as possible.

This is a selection and optimization requirement. It is not an unlimited spending authorization or proof of unused capacity, active credits, paid plans, or access to every account.

## Objective and accounting

Minimize total cost per verified business outcome while meeting customer, security, reliability, and autonomy requirements. Report both incremental cash cost and fully allocated cost.

Include inference, failed attempts, review, compute, idle capacity, storage, egress, backups, monitoring, licenses, power, maintenance, replacement, and expected failure/recovery cost. Do not treat owned hardware as free or managed infrastructure as automatically cheaper.

Attribute cost by parent, venture, workflow, and agent. Avoid counting the same shared cost twice. Use measured usage and dated prices or invoices; mark unknown costs rather than inventing estimates.

## Placement procedure

1. Inventory existing capacity, account plans, quotas, commitments, data locality, and operational reliability.
2. Reuse a suitable existing service or idle resource if it meets requirements at lower incremental cost.
3. Compare on-prem, existing Hetzner capacity, and current managed-service allocations for the workload.
4. Account for latency, cross-provider traffic, backup and recovery, and coordination complexity.
5. Prefer one clear home for each workload and authoritative data type.
6. Record a placement decision, expected monthly and marginal costs, limits, and a review trigger.
7. Migrate only when savings or reliability benefits exceed migration cost and risk.

Do not deploy one service to every provider merely because those providers are available.

## Model routing

Use deterministic code for parsing, arithmetic, validation, and straightforward transformations when appropriate. Use retrieval and bounded context to avoid repeatedly sending whole repositories or books.

Choose the least expensive evaluated model that meets the task's accuracy, latency, security, and reliability requirements. Fireworks.ai is an available inference option; local inference is a candidate only after GPU/CPU capacity, power, throughput, and quality are measured.

Reserve stronger models for hard reasoning, failed bounded attempts, or required independent review. Track total cost per accepted result, including retries. Use batching, caching, and prompt reuse where supported and compatible with data isolation. Cached authority checks must not hide revocation.

Do not reduce review or required tests just to lower model cost.

## Operating controls

Use per-task, per-venture, period, recurring, and portfolio budgets with enforced limits. Right-size workers, queue background work, reclaim expired previews and temporary resources, and avoid always-on idle agents.

Before stopping resources, verify ownership, customer dependencies, backups, and retention. Cost optimization must not delete required records or undermine service obligations.

Monitor usage against forecast and quotas. Trigger automated optimization inside existing authority; pause new discretionary commitments at caps. Do not upgrade plans or make new purchases silently.

## Purchase decisions

Prepare a board decision only when a purchase or commitment exceeds existing delegation. Include the unmet requirement, existing-resource alternatives, measured utilization, current price source/date, one-time and recurring cost, payback or benefit, cancellation terms, and the consequence of doing nothing.

A genuinely new capital or budget decision belongs to the board. Repeated approval of ordinary spending inside an existing mandate is an autonomy failure. Capture recurring needs in bounded standing mandates rather than repeatedly asking.

## Required evidence

A workload is cost-ready when usage is attributable, caps are configured, cost estimates are traceable, and degraded/retry behavior is bounded. Financial sustainability and zero operational human asks remain simultaneous goals.

## Change history

- 0.2 — 2026-09-09: Recorded the founder's existing infrastructure and cost-efficiency direction.
