# Provider credential readiness

Version: 0.1 | Updated: 2026-09-09 | Status: Existing credential inventory and read-only verification

## Method

Queried the existing OpenBao metadata and project policies. A process on the trusted vault host read selected credential values into memory and sent them only to their corresponding provider API. Tool output contained status fields only. No credentials were copied into Unilogistix, and no provider login, purchase, deployment, inference request, or account mutation was performed.

## Results

| Provider | Evidence | Remaining requirement |
| --- | --- | --- |
| GitHub | Connected app has verified private reads and Unilogistix writes | Prefer this existing connection; do not duplicate personal tokens |
| Cloudflare | Existing token verification returned HTTP 200 and active status | Verify resource scope and provision dedicated access when recovery is ready |
| Supabase | Existing management token listed organizations successfully | Dedicated Unilogistix project and scoped credentials; no use of customer service-role keys |
| Vercel | Existing infrastructure and Freightex credentials authenticated; primary credential returned HTTP 404 | Use a verified provisioning route; determine dedicated project/team scope; do not revoke an existing key based on this single check |
| Fireworks | Existing credential listed its account successfully (HTTP 200) | Dedicated service identity, permitted models, and enforced budget before inference |
| Hetzner | No matching credential found in the enumerated OpenBao secret paths | Locate the existing account's authorized provisioning path when compute is needed |

## Boundaries and next work

Authentication success does not prove least privilege, rotation authority, quota, billing readiness, or production readiness. Existing deployment policies include broad path wildcards; do not copy them as Unilogistix's access design.

Dedicated provider credential issuance/import remains gated on recovery verification in the [OpenBao status](../infrastructure/openbao/README.md). Complete distributed-share access and a full restored-vault unseal; then define the exact resource scope and issue credentials directly into the secret store. Use interactive account login only if the existing authorized route cannot provide that scope.

Provider API checks follow the official [Cloudflare token verification](https://developers.cloudflare.com/api/resources/user/subresources/tokens/methods/verify/), [Vercel user endpoint](https://vercel.com/docs/rest-api/user/get-the-user), [Supabase organizations endpoint](https://supabase.com/docs/reference/api/v1-list-all-organizations), and [Fireworks accounts endpoint](https://docs.fireworks.ai/api-reference/list-accounts).

## Change history

- 0.1 — 2026-09-09: Inventoried existing provider credentials without publishing values or copying production keys.
