# Autonomy failure and dependency register

Version: 0.2 | Updated: 2026-09-09 | Status: Observed bootstrap record

This register records observed foundation-stage failures and manual dependencies. It is not a claim about a production runtime.

| ID | Observation | Classification | State / corrective action |
| --- | --- | --- | --- |
| AF-001 | Initial GitHub upload returned 403; the assistant requested the founder change integration access | Operational human ask during bootstrap | Open: direct MCP configured; authenticated repository write remains unverified |
| AF-002 | MCP configuration write was blocked by the protected configuration directory; platform escalation required | Bootstrap approval dependency / operational human ask | Configuration completed through approved execution; eliminate recurring setup asks through provisioned environment |
| AF-003 | Registering additional provider MCP entries required protected-config platform escalation | Bootstrap approval dependency / operational human ask | Configuration completed; account OAuth remains a bootstrap dependency |
| DEP-001 | Direct GitHub MCP requires an account-authorized credential not present in this session | Bootstrap credential dependency | Open: terminal launcher prepared; future machine identity and managed rotation needed |
| DEP-002 | Chrome DevTools configuration references npx, unavailable in this environment | Observed capability gap; no human ask issued | Deferred until browser workflow; automate compatible runtime provisioning then |

## Counting

AF-001, AF-002, and AF-003 describe issued asks and remain historical failures even after remediation. DEP entries describe unmet dependencies; count a distinct issued human ask when one occurs. Do not infer that configuring MCP removes the GitHub publication failure.

Production instrumentation will use individual action events, timestamps, eligible-operation denominators, human execution time, and recurrence evidence as specified in [the autonomy policy](../policies/autonomy.md). Do not manufacture precise timing or live operational metrics for this documentation session.

## Change history

- 0.2 — 2026-09-09: Added to the blueprint-aligned foundation.
