---
type: project
status: current
priority: P0
first_seen: 2025-01-01
tags: [vault, second-brain, obsidian, pkm, obsidian-tools, knowledge-management]
aliases: [Second Brain, The Vault, Knowledge Base]
---

# Second Brain Vault

> The infrastructure behind every other project — entity layer, processed conversations, topic index, thinking patterns, daily/weekly cadence. Currently in maintenance mode with real gaps.

## What This Is

It's the operational memory for every project. The homelab tools, the job search, the OIA research, the consulting notes — they land here first. Without it, I would be relitigating old decisions with nothing to point at.

## What's Currently Working

- Entity pages (people, projects, topics) — ~20 pages cross-linked
- Processed export bucket — large repository of conversations with frontmatter, tags, linked_projects
- Topic index — navigable view by real tags and categories
- Thinking patterns analysis — data-driven portrait of decision-making
- Weekly report generation artifacts / reports index
- Daily note template and start of cadence

## What Didn't Ship / Known Gaps

- Weekly reports pipeline stalled since 2026-05-19; cron/automation needs restoration
- No remote/offsite backup: drift, corruption, or hardware loss = single-machine risk
- Some unresolved wikilinks still present after maintenance passes
- Conversation-topic-index exists on disk but should be re-verified after writes
- Daily notes backlog: no live entries 2026-05-27 through 2026-07-18
- No CI/reporting validation step; enrichment quality is manual

## Current Backup Strategy (honest state)

- Local filesystem only, plus whatever manual copies exist outside Git
- Git initialized but remote not configured in this state; recovery is local-first

## Last Verified Sweep

- Enrichment quality verified at ~93% (manual spot-checks, not automated)
- Entity pages rebuilt after a small set of deletions; backlinks should be checked
- Vault health dashboard is alive but shows stalled cadence

## Next Actions

1. Restore weekly report cron/automation
2. Add remote backup configuration (Git remote or automated sync)
3. Rebuild topic-index verification after any new enrichment writes
4. Backfill or intentionally skip the 2026-05-27 to 2026-07-18 daily notes gap

## Linked Conversations

Browse via: [[insights/conversation-topic-index.md|Conversation Topic Index]] — maintained at `insights/conversation-topic-index.md`.

---
*This is a working document, not a marketing page. Update when state changes, especially when weeks stall.*
