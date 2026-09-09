# UNI / Unilogistix

Version: 0.4 | Updated: 2026-09-09 | Status: Foundation draft; blueprint standard selected

**A reusable AI operating system that develops and operates businesses through dedicated business instances.**

UNI / Unilogistix is the master operating framework and repository identity. It will never be an actual company. Actual businesses receive their own configured instances; LondonRue, the founder's example towel business, would develop and operate through its LondonRue instance. See the [system and business model](governance/SYSTEM_AND_BUSINESS_MODEL.md).

The founder supplies direction. AI functions research, design, build, test, launch, market, sell, support, administer finances, maintain, and improve products. A business can receive its dedicated, governed instance during discovery and development. Viability is evaluated later; the master framework remains reusable for further businesses.

Business outcomes continuously improve Unilogistix through [versioned learning and CI/CD](workflows/business-to-framework-learning.md). The next business inherits the improved framework; existing instances receive compatible evaluated upgrades.

## Repository standard

The founder selected the [Master Blueprint v1.0](reference/UNI_Master_Blueprint.md) as the documentation and architecture standard. This foundation implements its eleven root documents, ten books, and operating areas.

The framework supports software, physical-goods businesses such as the LondonRue towel example, and hardware where authorized. The earlier software-first implementation proposal does not restrict the business model. The [alignment decision](decisions/ADR-0001-blueprint-alignment.md) explains how the two sources fit together.

## Start here

- [Review all agent responsibilities in the constitution](CONSTITUTION.md#constitutional-agent-responsibility-schedule): 60 drafted contracts with shared rules, handoffs, separation and LondonRue scenarios.

- Current work: [complete the company documents and agree their scope](governance/DOCUMENT_SCOPE.md), using the confirmed US/Illinois legal baseline. Runtime implementation is outside today's scope.
- [Vision](VISION.md), [manifesto](MANIFESTO.md), and [founder](FOUNDER.md).
- [Constitution](CONSTITUTION.md) and [rulebook](RULEBOOK.md).
- [Master architecture](MASTER_ARCHITECTURE.md) and [complete index](MASTER_INDEX.md).
- [Roadmap](ROADMAP.md), [changelog](CHANGELOG.md), and [glossary](GLOSSARY.md).
- [Board decision and activation register](governance/BOARD_REGISTER.md).

## Tool setup and autonomy evidence

See [MCP configuration and setup scripts](integrations/README.md) and [the autonomy failure register](governance/AUTONOMY_REGISTER.md). Six UNI MCP entries are configured. The GitHub connected app can read the existing private projects. Tailscale connectivity, OpenBao health, and SSH to its host have been verified; other provider and server access remains partly unverified.

## What exists

A versioned documentation foundation, ten initial book specifications, operating contracts, policy references, templates, and a proposed Safe Goes product brief. Department names and agent specifications describe responsibilities; they do not represent deployed workers.

A [local sandbox task store](services/foundation/README.md) now implements persistent tasks, leases, bounded retries and atomic audit records. Its deterministic CLI records draft tasks; real AI execution, independent review and unattended deployment remain incomplete. See [local implementation evidence](evidence/implementation-2026-09-09.md).

No live dashboard, connected billing system, production product, CI enforcement, or autonomous company has been established by this local increment. GitHub publication requires separate verification.

## Authority

Selection of the blueprint authorizes this documentation alignment. Detailed operational policies remain proposals until adopted. No budget, live customer operation, account mandate, or product launch is inferred from this foundation.

Work follows the [GitHub operating model](workflows/github-change.md). The public repository holds code, policies, and sanitized decision records; private systems hold secrets, customer data, and detailed financial records.

## Founder-directed autonomy requirement

**Every operational human ask is a failure.** Ordinary work must use autonomous resolution and recovery. Count unavoidable asks, actual human execution, and unresolved operations honestly. Reserved board authority does not permit relabeling routine operational decisions. See [the autonomy policy](policies/autonomy.md).

## Existing infrastructure and cost direction

Build on Cloudflare, GitHub, Vercel, Supabase, Fireworks.ai, multiple on-prem servers, and Hetzner as reported available by the founder. Reuse suitable capacity, minimize cost per verified outcome, and bring genuinely new purchases outside delegation to the board. See [the stack plan](integrations/EXISTING_STACK.md) and [cost-efficiency policy](policies/cost-efficiency.md).

## Change history

- 0.4 — 2026-09-09: Linked the constitutional agent responsibility schedule and recorded its draft review status.

- 0.3 — 2026-09-09: Linked business-instance scope, marketing and the founder-confirmed framework learning loop.

- 0.3 — 2026-09-09: Applied the founder's reusable-framework/business-instance model; Unilogistix is not an actual company.

- 0.2 local increment — 2026-09-09: Linked the tested sandbox task store and security verification evidence.
- 0.2 — 2026-09-09: Established the master-blueprint structure and reconciled the original company vision.
