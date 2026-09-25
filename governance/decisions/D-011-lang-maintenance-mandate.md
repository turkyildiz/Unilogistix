# D-011 — Lang maintenance mandate: Maestro releases Lang fixes

Status: DRAFT for Board signature. Prepared by Maestro (Gram) on 2026-09-24 from founder direction
("yes, draft D-011 and set build budgets to 8", after "it feels like Lang needs constant attention and
baby sitting"). Takes effect when the founder signs the action envelope in `~/board-sign/d011/`.
D-010 stays in force unchanged; D-011 adds to it and replaces nothing.

## A. Why

On 2026-09-24 the first real Lang project (Forest Shield) exposed six machinery gaps in one day (backlog
routing, a deploy race, a missing thaw, stale-branch rework, budget end, no resume). Each fix was
reviewed by Garry, fully tested and correct, and each still needed a founder release script, because the
files it touched are reserved paths. The founder's time went to releasing reviewed fixes, not to decisions.
D-011 lets Maestro release that class of fix, and only that class, while the guardrails stay with the Board.

## B. Scope

Repository `turkyildiz/unilogistix-corporate-os`, deployed to oryx by `scripts/deploy_main_to_oryx.sh`.
Nothing else: not Truxon, Freightex, DQFile, tenants, or any other repository.

## C. What Maestro may do without founder action

Maestro may merge a pull request to `main` and deploy it when **all** of the following are true:

1. **Purpose.** It fixes a defect seen in Lang's own behaviour (a live incident, a failed task, a test gap)
   or carries out a change the founder asked for in words recorded in the Board register. The PR body
   names the incident or the register entry.
2. **Author.** Written by Maestro as Cody's stand-in, by Cody through Lang, or by a Maestro subagent;
   never by an outside party.
3. **Security review.** Garry's verdict `GARRY_SECURITY: CLEAR` on the exact head SHA that merges, posted
   on the PR, from a review brief that describes every behavioural change.
4. **Checks.** The `foundation` CI check is green on that head and the head is up to date with `main`.
5. **Not a guardrail.** The diff changes none of the following (section D). A PR that does needs the
   founder's release as before, even when it also fixes a defect.
6. **Safe moment.** Deployed only when no seat is running and no Owen deploy is in progress; the
   post-deploy checks pass (units active, no traceback in 2 minutes, no deploy loop in 60 seconds).
7. **Notice.** Within one hour Maestro tells the founder in the Maestro session or channel: PR number,
   what it fixed, Garry's verdict, test counts, deployed revision. Each release gets a Board register line.

## D. What stays with the founder (outside D-011)

A change to any of these is never released under D-011:

- the merge and exchange rules: `orchestrator/mandate_merge.py` merge conditions, `orchestrator/d008.py`,
  and the exchange-budget limits (`EXCHANGE_BUDGET_*`, `BUDGET_MIN`/`BUDGET_MAX`, `CAP_MAX`), including any
  raise of the D-010 ceiling of 8;
- who may freeze, thaw, resume or arbitrate, and the emergency stop;
- the egress proxy allow-list (`scripts/egress_proxy.py`) and seat tools that reach the network
  (for example a new web tool for a reviewing seat);
- seat identities and credentials, GitHub App permissions, OpenBao policy and paths;
- the reserved-path list itself, `governance/**`, `.github/**`, `infrastructure/**`,
  `pyproject.toml`, `uv.lock`;
- D-008/D-010/D-011 and any other Board decision text.

Everything reserved to the founder by D-010 (contracts, OpenBao policy, spend, identity, first launch,
new company, store publication, thaw, anything Lang parks for the Board) stays with the founder.

## E. Duration and revocation

Valid 30 days from signature, renewable by a new signature. Revocable at any time: the founder says
"revoke D-011" (Maestro stops at once and records it), or signs a revocation. A D-011 release that later
proves wrong is rolled back by Maestro without waiting, and reported the same way.

## F. How it is enforced

D-011 is a mandate to Maestro, not to the runtime: no Lang code changes. Maestro releases with a fixed
script that refuses to merge unless conditions C.3 to C.6 hold and the diff avoids every path and
identifier in section D, and that writes the notice and the register line. Sherlock's register reviews
sample D-011 releases.

## G. Founder's steps

1. Read this document.
2. Sign: `cd ~/board-sign/d011 && ./sign.sh` (Board key; passphrase in your terminal only).
3. Tell Maestro "d011 signed". Maestro records it in the Board register and starts using it.
