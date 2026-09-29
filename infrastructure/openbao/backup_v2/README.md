# Snapshot sender v2: diagnostic and permission repair

Version: 1.1 | Updated: 2026-09-29 | Status: source preservation and reviewed repair candidate

These modules preserve the installed v2 snapshot sender and its shared protocol helper, previously described by the parent README but absent from this repository. The older hyphenated scripts remain historical v1 source and are not replaced. The sender imports `backup_common.py` from its installed directory. No credential files, receiver addresses, cluster identifiers, snapshots or deployment configuration are included.

The repair adds fixed failure stages and allowlisted error codes to the existing failure-status record. It rejects group/world-readable SSH identity files, nonregular files and non-root ownership before authentication. This guard runs inside the status-writing transaction boundary: a permission regression replaces a previous PASS with a fresh FAIL, rather than leaving stale success visible. It does not automatically relax or repair permissions. HTTP error objects are closed without reading/printing their response bodies.

The incident's cause was an administrative permission change to mode0640 on the sender SSH identity. OpenSSH correctly rejected that private key even though strict host identity verification and the offered public-key check succeeded. Restoring0600 on the exact existing root-owned file recovered delivery. Token renewal was working throughout; replacing the identity or changing known_hosts would not address the cause. Future operator access must use scoped service/status access rather than widening credential-file permissions.

Hard archive/expansion limits, exact source/version checks, pinned SSH host verification, candidate retention, receipt matching and checkpoint separation remain unchanged. The configured paths are resolved by the existing root-owned deployment file; this commit does not deploy code or authorize a new destination. Stage codes and status do not prove remote continuing existence or restoration.

## Qualification

```sh
python3 -W error::ResourceWarning -m unittest discover \
  -s infrastructure/openbao/backup_v2 -p test_diagnostics.py -v
python3 scripts/validate_foundation.py
```

Five tests cover nine injected failure stages, error redaction, receipt success, temporary cleanup, permission metadata and a real local invalid-mode file replacing previous PASS while preserving an archive. Synthetic tests mock token access and network/storage validation; they never read a live credential. Full archive parsing and restore qualification are separate existing controls, not newly established by these tests.

The deployed common helper is imported without behavioral changes. Preserve its installed filename and independently compare it before replacement. Apply sender updates only through reviewed fleet maintenance, then invoke the existing timer/service and verify an exact fresh durable receipt. Delivery recovery does not qualify a new archive for restore; perform the existing isolated same-version restore/unseal/canary/denial procedure on the exact received archive before pinning a checkpoint. Never restore into production or discard a previously qualified checkpoint.

## Restore source preservation

The [received-copy restore runbook](RESTORE.md) documents the generic isolated helper, exact audit configuration requirement, explicit historical application binding profiles and real synthetic qualification. Custody collectors, host topology, native credential loaders and exact received-copy identifiers remain private. This source addition does not deploy or schedule restores.

## Change history

- 1.1 — Preserve reusable restore helper/worker, explicit profile example, audit template and synthetic regressions; distinguish historical snapshot qualification from current credentials and continuous coverage.
- 1.0 — Preserve installed v2 sender/helper; add redacted stage diagnostics and fail-closed SSH identity permissions with regression tests. No source of provider authority or secrets is added.
