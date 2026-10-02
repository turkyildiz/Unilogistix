# Exact received-copy restore qualification

Version: 1.0 | Updated: 2026-09-29 | Status: source preserved; generic profile variant qualified synthetically; operational execution requires independent review

`restore_qualification.py` runs a received snapshot in an owned, disposable OpenBao 2.6.2 container. It validates the trusted receipt, source cluster/version, archive basename, size and SHA256 before starting. Both container images are digest-pinned and must already be cached. The vault has no external network, published port, production volume or production container access. Its filesystem is read-only except new disposable tmpfs directories. The Python worker shares only that vault's isolated network namespace. Custody is passed through bounded stdin; no token/share files are opened by these modules.

This source contains no custody collector, native credential loader, host topology or received archive identifiers. The private reviewed operator wrapper must load the existing operator identity on its original vault host and keep it there. Root-token files must not be read. Do not improvise an SSH token-export pipeline or use the obsolete installed 2.4.4 restore script.

## Required inputs and review

1. Select a single received archive and its receiver receipt through the existing trusted delivery mechanism. Record their immutable hashes privately. Never select `latest` during execution.
2. Bind the exact source cluster/version and existing trusted deployment config. Add `qualification_bindings` using the structure in `restore-profile.example.json`. Each record states a scoped AppRole, own KV-v2 path, historical expected version, nonsecret binding fields, and three denied paths. Review these expectations against the selected snapshot's capture time. The profile is mandatory, bounded and rejects credential fields or arbitrary URLs; it does not grant access.
3. Review the source vault's declarative audit configuration. `audit-config.example.hcl` is the reviewed fleet template embedded as `AUDIT_CONFIG`. Description, type, locality and every option must match the persisted entry exactly. When the source uses a different configuration, change/review/test the template and helper together. Mount its sink only on new disposable tmpfs, never the live audit directory. Do not disable audit to pass qualification.
4. Independently review the helper/worker hashes and vault-local wrapper. Cache the pinned images before collecting custody. The wrapper must supply exactly three existing shares and the existing operator identity in memory/stdin on the original vault host. Neither custody nor native loader implementation belongs in this repository.
5. Run only the reviewed wrapper. Preserve the structured terminal result and exact input/helper hashes privately. A nonzero exit is failure. Do not convert a failed or partial run into a restored checkpoint.
6. Confirm ownership-guarded container cleanup, then dispose only that invocation's encrypted staging copies. Cleanup failure retains private inputs and must be resolved using exact run ownership, never a broad Docker prune. Preserve original receiver backups and prior qualified checkpoints.

The generic helper's CLI accepts `--archive`, `--receipt` and `--config`; its stdin protocol is reserved for the reviewed vault-local wrapper, not interactive secret entry. The config and receipt must be regular, owned by the invoking operator and not group/world writable. The wrapper must establish the stronger private source and operator identity bindings before invoking it.

## Checks and limitations

The worker initializes a fresh disposable target with 3-of-5 Shamir configuration, force-restores the exact snapshot, then unseals it with the original three shares. It checks source cluster identity and version, audit availability, the operator canary, and the existing bootstrap-reader policy. Bootstrap-reader intentionally lacks self-revoke: the test verifies this denial, revokes only its generated probe token using the restored operator, and verifies subsequent access is denied. Each application profile role must pass own-version/binding checks, cross-environment/admin/LIST denials and token revocation. No production policy is widened.

On failure, output includes fixed stages/codes, bounded seal metadata and allowlisted log categories. Raw Docker logs, response bodies, credential values and arbitrary exception strings are never emitted. Operator identity and shares stay within the original host and isolated driver memory/stdin. Docker access remains an operational privilege and must be held only by the reviewed host operator.

The received-copy qualification on 2026-09-29 passed the private exact-bound helper before this reusable profile refactoring: original 3-of-5 unseal, source cluster, audit, bootstrap checks and both Vakf application bindings at historical source version2. The staging API credential subsequently/currently has version4; the historical snapshot success does **not** prove restoration of version4. Preserve the exact capture/version in every result. This was an explicitly executed, fixed received-copy qualification, **not** continuously automated restore coverage. New snapshots need fresh qualification; this commit creates no timer or deployment.

The canonical generic profile variant is separately tested with synthetic credentials and actual pinned Docker images. Its deployment remains subject to independent review; preserving source is not a deployment or permission grant.

## Local qualification

```sh
python3 -W error::ResourceWarning -m unittest discover \
  -s infrastructure/openbao/backup_v2 -p 'test_*.py' -v
python3 infrastructure/openbao/backup_v2/test_real_restore.py
```

The second command is explicit and uses generated synthetic custody only. It creates an isolated source, captures its snapshot, then exercises three restore cases: omitted audit config fails, mismatched description/options fail after successful unseal with standby health, and exact audit config passes all scoped checks. Containers are label-owned and cleaned. Images must already be cached; the fixture never pulls or reads existing credentials.

The fixture models the real restrictive bootstrap policy and checks exact-probe operator revocation. Unit tests cover incorrect cluster/denials, cleanup ownership, redaction, prohibited profile fields and paths, in addition to the sender's permission/stale-status regressions.

## Sources

OpenBao's [pinned audit reconciliation implementation](https://github.com/openbao/openbao/blob/v2.6.2/vault/audit.go) requires exact configuration equality; [official audit documentation](https://openbao.org/docs/2.4.x/audit/) explains audit configuration and failure behavior.

## Change history

- 1.0 — Preserve reviewed isolated restore mechanics, exact audit template, explicit historical application binding profile, synthetic positive/negative qualification and policy-correct cleanup. Keep custody/operational identity loaders private.
