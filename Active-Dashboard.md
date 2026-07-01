# Active Dashboard — Q2 2026

**Last Review:** 2026-06-02
**Current Focus:** Garage Flipping — Tech-Enabled Scavenger

---

## Quick Status

- **Sprint Items Complete:** 0 / 6
- **P0 Items:** 2 in progress (posting + outreach logging)
- **Active Project:** garage-flipping
- **Daemon:** lead-scraper running (PASS)
- **Infrastructure:** Craigslist daemon + ntfy alerts + vault auto-logging live

---

## Active Projects

```dataview
TABLE conversation_count AS "Conversations", status AS "Status"
FROM "nodes/projects"
WHERE type = "project"
SORT conversation_count DESC
```

## Active Topics

```dataview
TABLE file.mtime AS "Last Updated"
FROM "nodes/topics"
WHERE type = "topic"
SORT file.mtime DESC
```

---

## Recent Daily Notes

```dataview
TABLE file.mtime AS "Last Modified"
FROM "insights/daily-notes"
SORT file.name DESC
LIMIT 7
```

---

## Upcoming Deadlines (Q2 Tracker)

For the latest tracked actions, see:
- [[insights/goals/concrete-action-plan-Q2-2026|Concrete Action Plan]]
- [[insights/goals/goal-alignment-2026-Q2|Goal Alignment Report]]
- [[insights/goals/q2-2026-action-tracker|Q2 Action Tracker]]

---

## Quick Links

- [[MOC.md|Map of Content]] — central navigation hub for the second brain
- [[nodes/topics/thinking-patterns.md|Thinking Patterns]] — how Bryan thinks, decides, and builds
- [[insights/goals/goals-overall|Goals Overview]] — master goals document
- [[weekly-reports-index|Weekly Reports]] — 10 reports, auto-generated Sundays
- [[insights/blind-spots/2026-04-blind-spots.md|Blind Spots Report]]
- [[insights/daily-notes/2026-05-26|Today's Daily Note]]

---

## Second Brain Status

| Metric | Value |
|--------|-------|
| Total enriched conversations | 3,400 |
| Entity pages with narrative | 20 |
| Thinking patterns analysis | [[insights/thinking-patterns/2026-05-18-patterns-raw-data.md|May 18 Patterns (raw data)]] |
| Cross-link coverage | 100% (3,400/3,400 files) |
| Metadata coverage | 100% (source + id on all files) |
| Weekly reports | [[weekly-reports-index|10 reports]] (Apr 4 – May 19) |
| Daily notes | [[insights/daily-notes/2026-05-26|Active]] (started May 20) |
| Query system | 6 dataview files in `insights/queries/` |
| Goals tracking | [[goals-index|4 files]] — all cross-linked |
| Last enrichment run | 2026-05-19 |
| Vault health | **Alive** — all systems operational |

---

## Phase 3 + Enrichment Fixes — Kanban Tasks

| ID | Title | Status |
|----|-------|--------|
| T1 | Enrich processed files with frontmatter (Phase 3) | Done |
| T2 | Build entity pages from enriched data | Done |
| T3 | Generate thinking patterns report | Done |
| T4 | Update Active Dashboard | Done |
| T5 | Recreate weekly check-in cron job | Done |
| Fix T1 | Second pass enrichment on 2,000 missed files | Done |
| Fix T2 | Fix GPT enrichment quality (wrong categories) | Done |
| Fix T3 | Fix linked_projects across all enriched files | Done |
| Fix T4 | Verify enrichment quality and update dashboard | Done |
| Fix T5 | Wire living layer — daily notes, weekly nav, goals links | Done |

---

## How to Use This Vault

This vault is the second-brain execution layer. It's not just an archive — it's supposed to drive action. When talking to Hermes:

- **"Check tracker"** — Hermes reviews Q2 action items and flags what's slipping
- **"Weekly review"** — Hermes scans recent activity, updates the tracker, writes a weekly insight report
- **"What's my P0?"** — Hermes tells you the highest-priority action right now
- **"Daily note"** — Hermes writes today's daily note with what happened, key takeaways, and related links

The rule: if it doesn't help get Bryan out of warehouse or generate revenue, it's maintenance. Do it later.

---

*Dashboard maintained by Hermes. Last updated 2026-05-26 (Daily check-in).*
