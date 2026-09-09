# Knowledge, Memory & Intelligence

Version: 1.0 | Updated: 2026-09-09 | Status: Complete draft chapter manuscript; adoption and runtime activation pending

## Sources of truth

GitHub holds source code, policies, versioned specifications, prompts, and sanitized decisions. Operational stores hold tasks and audit events. Financial systems hold transaction and accounting records. Product stores hold customer and device records. Search indexes and model context are derived views.

A retrieval result never overrides its authoritative source or grants action permission.

## Memory layers

Working memory: bounded context for a current task. Project memory: requirements, decisions, dependencies, and outcomes for one product. Company memory: reusable methods, approved policies, and nonconfidential lessons. Long-term knowledge: attributed and reviewed evidence with explicit retention.

Knowledge records include ID, source, author or importer, observation date, version, owner, sensitivity, product scope, fact/assumption/recommendation/question classification, review date, expiry, and supersession links.

## Ingestion and retrieval

Validate source and sensitivity before ingestion. Enforce access before indexing and at retrieval. Keep private product data isolated; a shared lesson must be sanitized and authorized for reuse.

Retrieval returns provenance, date, and version alongside content. Mark stale or conflicting records and consult the source for consequential decisions. A copied prompt is not an approved prompt release.

## Master and business memory

Keep each business's operational memory separate from reusable Unilogistix framework knowledge. Every meaningful business outcome is considered for learning; record the disposition and promote validated reusable lessons through [business-to-framework CI/CD](../../workflows/business-to-framework-learning.md). "Company memory" below means the relevant actual business context, not an incorporated Unilogistix parent.

## Decision history and learning

Link decisions to evidence and alternatives. Record failed experiments and incidents. Curate reusable lessons rather than copying raw customer conversations into company memory.

Retire knowledge through supersession or deletion according to adopted retention rules. Propagate permission changes and deletion to derived indexes, caches, and backups according to the applicable retention design.

## Acceptance

Verify retrieval does not cross product boundaries, stale policy is detected, superseded documents do not govern actions, and an injected instruction in a retrieved document cannot change permissions.

Measure grounded-answer quality, freshness coverage, retrieval failures, and unauthorized disclosure attempts. Intelligence proposals remain recommendations until authorized through ordinary gates.

## Autonomous operation requirement

Every operational human ask is a failure. Apply [the founder-directed autonomy policy](../../policies/autonomy.md), with AI recovery, honest failure accounting, and no authority bypass. Routine escalations go to AI functions; reserved board decisions remain explicit.

## Chapter coverage

1. Purpose
2. Knowledge Architecture
3. Sources of Truth
4. Memory Architecture
5. Working Memory
6. Project Memory
7. Company Memory
8. Long-Term Knowledge
9. Retrieval
10. Knowledge Validation
11. Decision History
12. Prompt Library
13. SOP Library
14. Lessons Learned
15. Knowledge Governance
16. Knowledge Security
17. Knowledge Versioning
18. Intelligence Layer
19. Cross-Project Learning
20. Avoiding Stale Knowledge
21. Knowledge Retirement
22. Continuous Learning
23. Appendices

Every listed chapter is expanded in the [complete chapter manual](CHAPTERS.md). The manuscript specifies responsibilities, procedures, acceptance evidence and failure handling; operating controls require separate activation proof.

## Change history

- 1.0 — 2026-09-09: Completed all listed chapters and linked the manuscript; implementation remains outside today’s scope.

- 0.3 — 2026-09-09: Linked business-instance scope, marketing and the founder-confirmed framework learning loop.

- 0.2 — 2026-09-09: Added the initial operating contract and retained the blueprint chapter coverage.
