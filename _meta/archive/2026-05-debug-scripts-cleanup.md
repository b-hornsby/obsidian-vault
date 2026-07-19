---
type: archive
tags: [meta, cleanup, scripts]
---

# 2026-05 Debug Scripts Cleanup

Removed 21 one-off enrichment/debug Python scripts from `_meta/scripts/` on 2026-07-19.
These were created during the May 2026 enrichment debugging cycle
(fix_* / enrich_semantic* / spot_check* variants) and superseded by
the canonical `enrich_semantic_v3.py` workflow kept in project history.
