---
type: weekly-index
status: active
priority: P1
tags: [weekly-report, index, q2-2026, q3-2026]
aliases: [Weekly Reports Index, Reports]
---

# Weekly Reports Index

> Auto-generated index of weekly review reports.

```dataview
TABLE created_at AS "Created", week_ending AS "Week Ending"
FROM "insights/weekly-report"
WHERE file.name != "weekly-reports-index.md"
SORT week_ending DESC
LIMIT 50
```

---
## Status

- Cadence: active
- Script: `_meta/scripts/weekly-report.sh`
- Schedule: Sunday 08:00 WSL cron

---
## Related

- [[insights/goals/goals-overall.md|Goals Overview]]
- [[nodes/projects/second-brain-vault.md|Second Brain Vault]]
