---
source: hermes
date: 2026-05-20
session: fix-duplicate-queries
tags: [hermes, vault, maintenance, cleanup]
---

# Fixed Duplicate Queries Directory

Found duplicate `queries/` directories:
- Original: insights/queries/ (created during vault enrichment)
- Duplicate: queries/ at vault root (created during final sweep)

Actions taken:
1. Updated MOC.md to point to insights/queries/ for all 6 dataview links
2. Updated Active-Dashboard.md to reference insights/queries/
3. Removed duplicate queries/ directory at vault root
4. Verified all links now point correctly to insights/queries/

Result: Single source of truth for query files, no broken links.