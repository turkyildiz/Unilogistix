# Existing stack and workload placement

Version: 0.2 | Updated: 2026-09-09 | Status: Founder-reported resources; assignments proposed; MCP configuration verified

## Confirmed by the founder

The founder stated that Cloudflare, GitHub, Vercel, Supabase, Fireworks.ai, multiple on-prem servers, and Hetzner are available. Account access, project identities, specifications, remaining quotas, and current invoices have not yet been inspected.

## Proposed division of responsibility

| Available resource | Initial role to evaluate | Placement and cost constraint |
| --- | --- | --- |
| GitHub | Source, policies, review history, work items, CI | Use on-prem runners only after isolation and capacity are verified |
| On-prem servers | Durable orchestration, workers, builds, evaluation, internal services; possibly inference | Verify CPU/GPU, RAM, storage, power, network, isolation, backups, and uptime; owned capacity is not free |
| Hetzner | Public services, stable workers, or off-site recovery where suitable | Reuse existing allocations first; new provisioned capacity must fit a budget |
| Cloudflare | DNS, edge access, caching, and selected edge workloads | Avoid duplicating application hosting; measure requests, traffic, and storage |
| Vercel | Frontend previews and production web delivery where justified | Control preview lifetime and metered usage; compare requirements and total cost |
| Supabase | Existing managed database/auth/storage where suitable | Decide product boundaries and data locality; avoid duplicate authoritative databases |
| Fireworks.ai | Hosted inference option for evaluated task classes | Measure quality-adjusted inference cost, retries, concurrency, and latency |

These are architecture proposals, not deployed assignments. Product requirements may justify a different placement.

## Inventory required before provisioning

Record asset ID, owner, environment, CPU/GPU/RAM, storage and free capacity, network limits, region, isolation, reliability, backup/restore, current commitments, usage quotas, marginal cost, fully allocated cost, access method, and expiry.

Keep hostnames, network addresses, account details, and credentials in private operational inventory. This public repository should hold only sanitized capability summaries and decision references.

The initial inventory can be read-only. No server access should be guessed and no new resource purchased to avoid discovering existing capacity.

## Provider access plan

Cloudflare and Vercel have official remote MCP servers; Supabase provides an official remote MCP with scoping and tool-group options. Configuration has been registered, but account authorization and tool tests are pending. Sources: [Cloudflare](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/), [Vercel](https://vercel.com/docs/agent-resources/vercel-mcp), [Supabase](https://supabase.com/docs/guides/ai-tools/mcp).

Fireworks inference uses its provider API when the runtime is built; adding an MCP wrapper is unnecessary unless it fills a concrete management gap. Hetzner can be integrated through its official API or an evaluated client. On-prem automation should use an authenticated, least-privilege management interface within the adopted network boundary. No unverified community server is installed for these providers. Sources: [Fireworks](https://docs.fireworks.ai/getting-started/introduction), [Hetzner API](https://docs.hetzner.cloud/).

## Configuration and login

The stack script registered four entries: Cloudflare docs, Cloudflare API, Vercel, and Supabase. The Supabase entry initially exposes only allowlisted metadata/documentation reads; database access awaits a selected project and scope.

Reproduce configuration:

```bash
python3 /home/ike/Unilogistix/scripts/setup_stack_mcp.py --apply
```

Authenticate those account connections in your local terminal:

```bash
python3 /home/ike/Unilogistix/scripts/setup_stack_mcp.py --apply --login
```

The login flow runs provider OAuth through Codex. Grant only the intended accounts and capabilities. The script does not create resources, deploy, purchase services, or guarantee an account's permissions. Cloudflare and Vercel permissions are determined by the actual provider grants; they are not made read-only by this document.

Recurring manual login is not an acceptable final operating design. Machine access, renewal, revocation, and safe expiry need implementation before unattended operations.

Apply [cost-efficiency policy](../policies/cost-efficiency.md) to every placement and purchase decision.

## Change history

- 0.2 — 2026-09-09: Recorded the founder's existing infrastructure and cost-efficiency direction.
