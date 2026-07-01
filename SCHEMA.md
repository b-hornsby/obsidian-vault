# Wiki Schema

## Domain
Bryan's second brain — personal knowledge management covering:
- Career (job search, IT certs, professional development)
- Technical (AI/ML, coding, homelab, security)
- Personal (crypto, streaming, life goals)
- Projects (garage flipping, second brain, homelab, AI consulting)

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `garage-flipping.md`)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- Every new page must be added to `MOC.md` under the correct section
- Entity pages go in `nodes/people/`, `nodes/projects/`, `nodes/topics/`
- Raw sources go in `raw/` or `processed/`
- Insights and daily notes go in `insights/`

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
Tw1n/                    # Wiki root (WIKI_PATH)
├── MOC.md               # Map of Content (main index)
├── nodes/               # Entity and concept pages
│   ├── people/          # People Bryan interacts with
│   ├── projects/        # Active and archived projects
│   └── topics/          # Topic hubs (career, tech, personal)
├── insights/            # Daily notes, thinking patterns, reports
│   ├── daily-notes/
│   ├── thinking-patterns/
│   └── weekly-report/
├── processed/           # AI conversation outputs by model
├── hermes-memories/     # My memory exports
├── raw/                 # Raw source material
└── _meta/               # Templates, scripts, archive
```
