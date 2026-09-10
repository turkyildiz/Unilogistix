# ADR-0002: Framework secrets and project vault recovery

Version: 0.1 | Updated: 2026-09-10 | Status: Founder requested implementation; existing deployment being reverified

## Direction and purpose

The founder requested OpenBao for Unilogistix to track secrets and support recovery of each project's OpenBao. The founder also extended the Truxon/Freightex repair deadline without setting a replacement date. This instruction authorizes implementation using existing resources; it does not establish completed recovery or authorize additional purchases.

Unilogistix remains a reusable framework. Secrets belong to the actual business or infrastructure owner. A new business inherits policies, deployment tooling and empty configuration templates, never another business's credentials, tokens, recovery shares or snapshots.

## Existing deployment versus intended capability

The workspace contains an existing [OpenBao foundation](../infrastructure/openbao/README.md) with a dedicated Unilogistix KV mount and AppRole mount inside the fleet service. Existing Truxon and Freightex deployment documentation describes separate secret trees in that same service. These are access-policy boundaries, not separate vault clusters or isolation against a compromised fleet administrator. The September 9 implementation claims require current verification before reuse.

Reuse a qualified existing installation before creating a duplicate. An independent project vault must have its own cluster identity, storage, seal configuration and workload identities. Placing another mount on the same cluster does not create independent disaster recovery.

## Secrets management

- Record business, environment, provider resource, credential purpose, authoritative location, issuer, expiry, rotation procedure and recovery reference. Keep actual values and sensitive infrastructure identifiers out of the public repository.
- Give each workload the minimum paths and operations it needs, with short-lived authentication where supported. Backup identities may capture snapshots but must not receive restore, seal, policy-administration or general secret-read privileges.
- Keep one authoritative writer for each credential. A secret copy is not evidence that the provider still accepts it. Rotation must track provider activation and consumer adoption, including uncertain outcomes.
- Test cross-business access denial, revocation and expiration. A central administrator's broad authority remains an explicit trust boundary; role names alone do not provide independent custody.

## Project recovery

The proposed default is for Unilogistix to track and orchestrate encrypted project snapshots in separately controlled backup storage. Secret-by-secret mirroring is optional and must not be presented as complete vault recovery.

1. Bind every backup job and restore record to the exact source cluster and covered businesses. A snapshot of the current shared fleet vault covers that cluster; it is not a Freightex-only or Truxon-only export.
2. Capture a consistent Raft snapshot, record its byte count, digest, capture time, source version and cluster identity, and verify durable receipt independently of the source host.
3. Keep recovery custody independent of the snapshot store. Do not put all required unseal shares beside the snapshot or inside the only vault they unlock. For auto-unseal, preserve the actual seal service/key dependency; recovery shares alone cannot replace it.
4. Use separate per-source destinations and upload identities. One project's uploader must not overwrite, list or prune another project's backups. Central retention must preserve a last-known restorable copy when new verification fails.
5. Restore only into a newly created isolated target during drills. Unseal the isolated restored target using source-cluster custody, verify scoped canary reads, then destroy the disposable target. Never restore a project snapshot into the live central vault to "import" that project. Before any real cutover, reconcile revocations, policies and current provider credential state; an old snapshot can restore obsolete internal credentials and permissions. Keep consumers and scheduled jobs disabled until that reconciliation passes.
6. Record recovery-point and recovery-time measurements, snapshot age, custody availability, tested version and unresolved cutover steps. Alert delivery must be observable outside the primary host; a local timer cannot report total host loss by itself.

Automatic failover, high availability and safe restoration of every future business are not established by an installed vault or a successful snapshot upload. Each project must pass its own onboarding and restore qualification.

## Completion evidence

The installation is usable when current health, authenticated scoped access, negative authorization checks, audit behavior and credential renewal pass. The backup function is qualified only after independently stored snapshots, recovery custody and an isolated restore have been verified for the named source. Pending controls remain explicit in the operational record.

## References

- [OpenBao integrated storage](https://openbao.org/docs/concepts/integrated-storage/) describes Raft-backed storage and cluster behavior.
- [Raft snapshot API](https://openbao.org/docs/2.4.x/api/system/storage/raft/) documents snapshot capture and whole-cluster restore, including force-restore seal checks.
- [Seal and unseal](https://openbao.org/docs/concepts/seal/) explains Shamir custody and why auto-unseal recovery depends on the seal mechanism.

## Change history

- 0.1 — 2026-09-10: Recorded founder direction, existing shared-vault topology and proposed project recovery contract; current implementation verification remains in progress.
