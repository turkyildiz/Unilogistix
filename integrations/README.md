# MCP and tool integration plan

Version: 0.2 | Updated: 2026-09-09 | Status: Six MCP entries configured; account authentication and live tool checks pending

## Current capability inventory

Observed 2026-09-09. Configuration is not proof of authentication, live tool availability, or permission.

| Capability | Implementation / state | Next verification |
| --- | --- | --- |
| Local file work and execution | Native tools available in this session | Use existing workspace permissions |
| Web research | Native web tool available | Verify sources for each task |
| GitHub connected app | Authenticated private repository reads work; initial 403 is historical | A real repository write must succeed before claiming write access |
| GitHub direct MCP | uni-github registered and configuration read back | Supply account-authorized token to the local host; verify tools and intended write |
| OpenAI technical documentation | uni-openai-docs registered and configuration read back | Verify search/page retrieval after MCP tools load |
| Browser testing | Local controller installed; existing-browser connection still unverified | Resolve Node/runtime dependency and test browser isolation when browser work begins |
| CRM, support, marketing, billing, accounting | Workflow requirements specified; providers/accounts not selected | Select and connect only when the relevant business workflow is implemented |
| Existing cloud and inference stack | Founder identified Cloudflare, Vercel, Supabase, Fireworks.ai, Hetzner, and on-prem capacity | Inspect existing allocation; see the stack plan |
| Hardware / GPS devices | No live integration | Product mandate, device protocol, simulator, and physical boundaries first |

MCP is one transport. Prefer an existing native tool, connector, or a reliable API when it meets the need. Do not install duplicate access or arbitrary servers just to increase the tool count.

## Setup provided

The script registers official remote GitHub and OpenAI documentation servers using the installed Codex CLI. It backs up existing configuration privately, preserves existing servers, checks conflicting entries, and verifies read-back. These transport and authentication settings follow [OpenAI's MCP documentation](https://learn.chatgpt.com/docs/extend/mcp?surface=cli) and [GitHub's Codex installation guide](https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-codex.md).

Run the dry check:

```bash
python3 /home/ike/Unilogistix/scripts/setup_mcp.py
```

To reproduce installation on this host:

```bash
python3 /home/ike/Unilogistix/scripts/setup_mcp.py --apply
```

The two foundation entries and four additional stack entries were configured successfully during foundation preparation. See [existing stack and provider login](EXISTING_STACK.md). Re-running is safe when their settings match. This does not change hosted connector permissions or authenticate GitHub.

## GitHub authentication and secrets

Use the authenticated GitHub connected app for publication. Private repository reads now work. The optional direct MCP token launcher is a legacy bootstrap utility, not the selected unattended credential design.

The founder selected OpenBao. Existing projects already document a shared deployment; its health endpoint is reachable and unsealed, and SSH to its host is verified. Recovery automation, privileged-token custody, consumer migration, and provider rotation require further verification. Do not infer those controls from a health check. No live secret values belong in this repository.

## Existing provider connections

See [the existing-stack plan](EXISTING_STACK.md) for configured Cloudflare, Vercel, and Supabase entries, Fireworks and Hetzner API plans, and the OAuth login script. Account existence is reported by the founder; live access has not been verified.

## Adding the next integration

Start from a workflow gap and complete [the integration contract](../templates/integration.md). Verify the provider's current official endpoint or pin a reviewed server release. Bind credentials to the appropriate product and environment. Test health, the required action, denial, retry/reconciliation, and revocation before marking operational.

Live payments, external messaging, production deployment, and device actions still require their own mandates; installing a tool does not authorize those activities.

The OpenAI documentation server provides documentation retrieval, not model inference or an API account. See [its official documentation](https://developers.openai.com/learn/docs-mcp).

## Change history

- 0.2 — 2026-09-09: Added to the blueprint-aligned foundation.
