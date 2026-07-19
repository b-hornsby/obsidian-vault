# Wiki Schema

## Domain
Bryan's second brain — personal knowledge management covering:
- Career (job search, IT certs, professional development)
- Technical (AI/ML, coding, homelab, security)
- Personal (crypto, streaming, health, finance)
- Projects (garage flipping, second brain, homelab, AI consulting)

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `garage-flipping.md`)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- Every new page must be added to `MOC.md` under the correct section
- Entity pages go in `nodes/people/`, `nodes/projects/`, `nodes/topics/`
- Raw ingest/scraped material goes in `raw/`
- Refined author outputs go in `processed/<provider>/`
- Insights, reports, queries, daily notes go in `insights/`
- Ephemeral config/setup notes go in `Reference/`
- Canonical model state lives in `Reference/model-state.md`
- Vault automation scripts live in `_meta/scripts/`

## Frontmatter
Every wiki page should have:
```yaml
---
title: Page Title
type: entity | concept | project | insight | daily
tags: [relevant, tags]
---
```

## Tag Taxonomy
- Career: career, job-search, resume, interview, certification, it
- Technical: ai, coding, homelab, security, wazuh, linux, docker
- Personal: crypto, streaming, health, finance
- Projects: garage-flipping, second-brain, homelab, ai-consulting
- Meta: moc, index, template, archive

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions or minor details

## Update Policy
When new information conflicts with existing content:
1. Check dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates
3. Flag for user review

## Vault Structure
```
Tw1n/                               # Wiki root (WIKI_PATH)
├── MOC.md                          # Map of Content (main index)
├── SCHEMA.md                       # This file
├── nodes/                          # Entity and concept pages
│   ├── people/                     # People Bryan interacts with
│   ├── projects/                   # Active and archived projects
│   └── topics/                     # Topic hubs (career, tech, personal)
├── insights/                       # Derived outputs
│   ├── daily-notes/                # Chronological daily notes
│   ├── weekly-report/              # Sunday reflection reports
│   ├── thinking-patterns/          # Cognitive pattern studies
│   ├── goals/                      # Q2/Q3 goal docs and trackers
│   ├── queries/                    # Dataview queries
│   ├── blind-spots/                # Self audits
│   └── recent-conversations/       # Session-specific notes
├── processed/                      # AI conversation exports by model provider
│   ├── CLAUDE/
│   ├── GEMINI/
│   ├── GPT/
│   └── GROK/
├── hermes-memories/                # Hermes memory exports
├── raw/                            # Raw source material awaiting processing
├── Reference/                      # Ephemeral setup/config notes
│   └── model-state.md              # Canonical model runtime config
└── _meta/                          # Templates, scripts, archive
    └── scripts/                    # Automation: weekly report, config sync
```
