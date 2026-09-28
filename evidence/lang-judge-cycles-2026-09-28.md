# F-149 bounded judge cycles: release evidence

Version: 1.4 | Updated: 2026-09-28 | Status: repairs deployed and D013 active; challenge completion pending

The founder authorized three total cycles, each at most eight repair exchanges
plus one final judge call. Only an explicit final return with actionable findings
may open the next cycle. Prior clarification remains separate. This evidence
records implementation and assisted maintenance, not complete autonomy.

PR [263](https://github.com/turkyildiz/unilogistix-corporate-os/pull/263) merged and
deployed as `fd865520048f06163e9fabb6cb8c7f3d24635e08`. Its reviewed head was
`062d88a78d5c84cc131a2d8dd38fde7ad8164582`; the merged and reviewed Git trees matched.
Native Cindy accepted and Garry cleared that head after review findings were
resolved. CI run `36446297737` passed. Local validation passed 3,310 tests plus
207 subtests, with three skipped and two expected failures; Ruff and Bandit passed.

An installed-code test using a disposable ledger and injected test authority
verified unsigned renewal holds at eight, authentic-return-shaped progression
through three cycles, cumulative 24 exchanges, three final calls, no fourth cycle,
and no replay after reopening the ledger. These simulated seats and authority
are not evidence of a live signed grant. Live readback confirmed the original
D-010 active, zero D-013 grant rows, and identical activation/read registry paths.

The supported migration sent the original challenge toward its unused final
judge call while preserving all eight spent exchanges. It exposed another defect:
accumulated review text exceeded the packet ceiling before an external call.
The runtime incorrectly recorded a consumed synthetic HOLD. Exact installed-code
reproduction and the original state/claim/receipt and verified audit evidence were
retained. The challenge had remained held at this checkpoint; it had not autonomously passed.

Follow-up PR [264](https://github.com/turkyildiz/unilogistix-corporate-os/pull/264)
bounds superseded history, prepares an immutable packet before claiming a call,
and proposes a one-incident, audited correction of the proven non-call. Local
validation passed 3,349 tests plus 207 subtests, three skipped and two expected
failures. Native Cindy accepted and Garry cleared reviewed head
`aa35830ab2ca44e480c9e3fe62cebd306e181111`; CI run `36450412214` passed.
It merged and deployed as `20e39764ef8358cfd5efd3c444d5f79cc8ee8ba5`, with the
reviewed and deployed Git trees identical. Ruff and Bandit passed.

A disposable backup of the real ledger was rehearsed against the installed code,
with synthetic seats and injected test authority only. It proved that the exact
incident could be reconciled while preserving the original claim and receipt,
that unsigned work still held at eight, and that a test grant allowed 24 total
exchanges and three actual-shaped judge calls with no fourth or restart replay.
No live ledger writes or external calls occurred in that rehearsal.

The root-only supported correction then ran once under stopped Lang/recovery
services against the pinned proof and unchanged live state. It preserved all
eight spent exchanges, cycle one, and the original failure event/effect/receipt.
Lang restarted successfully with zero automatic restarts and the real Judy process
started on the corrected final opportunity. Judy returned REWORK with actionable
findings for the tenant/product budget checker. Lang then held at
`judge_cycle_authority_required`, cycle one, 8/8 spent and lifetime eight, with
one completed final ruling. D013 remains inactive; no new exchange was taken.
Subsequent autonomous repair and challenge completion remain unproven. No repair counter
was reset, no actual judge call refunded, and no cycle advanced by reconciliation.

The owner subsequently supplied signed D013 approval
`684f9aae-a731-4700-8ced-0af8b2c5e2a6`. The existing administrator delivery route
staged only the public action and signed envelope. Runtime verified the signature
and activated the amendment at 2026-09-28T16:46:35Z without a restart, bound to the
original D010 approval. Readback showed cycle two opened from the existing REWORK
receipt, 0/8 current-cycle exchanges, eight lifetime exchanges and one completed
final ruling. No final ruling was replayed. Lang remained active with the same PID
and zero automatic restarts. Cody subsequently requested clarification of the
new authority through the existing question path; that question is distinct from
a final exhausted-cycle ruling. Judy rejected that question because the worker pack
omitted the already verified approval. The task held at cycle two, 0/8, lifetime eight.

Follow-up [PR265](https://github.com/turkyildiz/unilogistix-corporate-os/pull/265)
repairs the authority context, question/final distinction, and retained ruling guidance.
Candidate `991a84dd05f869239e640bd231b358d54a34bffd` passes 3,375 tests and 207
subtests, with three skipped and two expected failures. Read-only real-grant packet
preparation and a disposable real-ledger-copy resume rehearsal pass, preserving
budgets, judge receipts and effects. Native Cindy's revised review accepts the change;
native Garry also returned CLEAR on the same revision. Exact-head CI36456739192
passed. The merge/deployed revision is `a8e5eb8bfdc29963356c61f7270945fd7936faa7`,
with its tree verified equal to the reviewed head. Installed checks prepared all
four worker packets using the real signed authority (maximum 107,878 bytes under
the unchanged limit), and the installed disposable-ledger resume proof retained
the eight-exchange budget and original judge receipts/effects. Both made zero
external calls and zero live ledger writes.
The founder explicitly instructed continuation and testing. The existing D012
recovery cap is already exhausted for this task; the supported zero-extra founder
resume was then executed and recorded as assisted maintenance. It advanced the
round to nine, retained cycle two with 0/8 spent and lifetime eight, and preserved
all existing final receipts and effects. Native Cody started; Lang was active with
zero automatic restarts. This is not an autonomous recovery or a new judge ruling.
Challenge completion is not established.

No production Board private key or passphrase was read by the agent. The signing
kit was tested only with an unenrolled disposable key; the production signature
was supplied by the owner. The old D010 mandate, expiry, revocation and emergency
stops continue to constrain every renewed operation.

## Change history

- 1.4 — 2026-09-28: PR265 qualified deployment, installed proofs and assisted live continuation.

- 1.3 — 2026-09-28: Authentic D013 activation and cycle-two opening verified.

- 1.2 — 2026-09-28: Live Judy REWORK and correct unsigned-renewal hold observed; challenge completion pending.

- 1.1 — 2026-09-28: PR264 qualified deployment, installed incident rehearsal and live audited correction; signature and challenge outcome pending.

- 1.0 — 2026-09-28: Records PR263 release and the discovered preflight incident;
PR264 and D013 activation remain explicitly pending.
