#!/usr/bin/env python3
"""Enrich 5 major project nodes with real content from enrichment mapping + Q2 plan context."""

import json
from pathlib import Path

VAULT = Path("/vault")
MAPPING = json.loads((VAULT / "_meta" / "enrichment_mapping.json").read_text())

# Q2 plan context per project
Q2_CONTEXT = {
    "homelab-stack": {
        "priority": "P1",
        "actions": [
            "Day 14: Demo notes + README written in vault",
            "Day 21: Pick and build ONE demo MVP (working code + screenshot/screencast)",
            "Day 30: Share demo somewhere for external signal",
            "Day 60: Demo generates inbound interest",
        ],
        "definition_of_done": "Working demo with README, shared publicly, producing inbound signal.",
        "blockers": ["1,614 conversations but no shipped artifact yet", "Analysis paralysis on which project to demo"],
        "focus_question": "Am I building something I can show, or just maintaining the lab?",
    },
    "private-ai-consulting": {
        "priority": "P1",
        "actions": [
            "Day 5: Define the $500 'Private AI Stack' package details",
            "Day 14: Reach out to 3 prospects; log conversations in vault",
            "Day 60: Close first paid engagement OR pivot package",
        ],
        "definition_of_done": "$500 package defined, 3 prospects contacted, first engagement closed or pivoted.",
        "blockers": ["No conversations since Nov 2025", "No concrete offer documented"],
        "focus_question": "Who am I helping and what do they pay for?",
    },
    "operation-immortal-agent": {
        "priority": "P0",
        "actions": [
            "Day 1: Move all code to one execution folder",
            "Day 3: One test trade OR log why not",
            "Day 14: Go live with real trade OR write archive note",
            "Day 60: 7-day stable uptime OR clean exit archived",
        ],
        "definition_of_done": "Live trade running OR clean archive note with lessons learned.",
        "blockers": ["Funding constraint (self-identified Apr 7)", "Code scattered across folders"],
        "focus_question": "Ship or kill — no more research mode.",
    },
    "it-certification": {
        "priority": "P1",
        "actions": [
            "Day 3: Decide: CompTIA A+, Network+, or Security+? One cert only",
            "Day 10: Book the exam with real non-refundable date",
            "Day 21: Study system live (Anki / practice tests)",
            "Day 60: Practice test 80%+ readiness",
            "Day 90: Exam taken; result documented",
        ],
        "definition_of_done": "Exam booked, studied 4x/week, result logged pass or fail.",
        "blockers": ["No conversations since June 2025", "Spread over 17 months, no concentrated push"],
        "focus_question": "Book the exam first; the deadline forces the schedule.",
    },
    "second-brain-vault": {
        "priority": "P1 (enabling)",
        "actions": [
            "Ongoing: Import all chat exports into processed/",
            "Ongoing: Enrich with tags, category, sentiment, linked projects",
            "Ongoing: Build topic hubs and project nodes",
            "Weekly: Hermes review on priority progress",
        ],
        "definition_of_done": "All 3,400 chats processed, graph-connected, actively producing insights.",
        "blockers": ["Raw files still need full enrichment", "Topic hubs mostly empty"],
        "focus_question": "Is the vault producing decisions, or just storing conversations?",
    },
}


def extract_project_data(project_name):
    entries = []
    for e in MAPPING:
        projects = e.get("enriched_frontmatter", {}).get("linked_projects", [])
        if project_name in projects:
            entries.append(e)
    return entries


def strongest_conversations(entries, limit=10):
    """Return the most recent + most substantial conversations."""
    def date_key(e):
        fname = e.get("file", "")
        try:
            return fname.split("_")[0]
        except Exception:
            return ""
    entries.sort(key=date_key, reverse=True)
    return entries[:limit]


def extract_date_from_file(fname):
    """Pull YYYY-MM-DD from filename like processed/CLAUDE/2025-02-17_Title.md"""
    try:
        base = fname.split("_")[0]
        # strip any subfolders, get last part
        parts = base.replace("\\", "/").split("/")
        for p in parts:
            if len(p) == 10 and p[4] == "-" and p[7] == "-":
                return p
    except Exception:
        pass
    return "?"


def build_project_node(project_name, display_name, entries):
    ctx = Q2_CONTEXT[project_name]
    q2_tracker = VAULT / "insights" / "q2-2026-action-tracker.md"
    
    # Build strongest recent conversations list
    recent = strongest_conversations(entries, 8)
    convo_links = []
    for e in recent:
        fpath = e.get("file", "")
        title = e.get("title", "Untitled")
        # Don't double-prefix: file field already starts with "processed/..."
        convo_links.append(f"- [[{fpath}|{title}]]")

    # Dates
    dates = [extract_date_from_file(e.get("file", "")) for e in entries if e.get("file")]
    dates = [d for d in dates if d != "?"]
    first = min(dates) if dates else "?"
    last = max(dates) if dates else "?"
    total = len(entries)

    blockers_md = "".join(f"  - {b}\n" for b in ctx['blockers'])

    body = f"""---
type: project
status: active
first_seen: {first}
last_seen: {last}
conversation_count: {total}
priority: {ctx['priority']}
tags: [project, synthesis, q2-2026]
---

# {display_name}

> {ctx['focus_question']}

## Summary

Project tracked across **{total} conversation(s)**. First seen {first}. Last active {last}.

This is a **{ctx['priority']}** priority in the Q2 2026 action plan.

## Current Status

_What actually matters right now:_

- **Next deadline:** {ctx['actions'][0]}
- **Definition of done:** {ctx['definition_of_done']}
- **Known blockers:**
{blockers_md}
## Q2-2026 Actions

| Due | Action | Status |
|-----|--------|--------|
"""
    for action in ctx["actions"]:
        due, desc = action.split(": ", 1)
        body += f"| {due} | {desc} | Not Started |\n"

    body += f"""
## Key Decisions & Themes

_Extracted from {total} conversations:_

"""
    # Extract a few decision/principle notes if available
    decisions = []
    for e in entries:
        ef = e.get("enriched_frontmatter", {})
        if ef.get("type") == "Decision":
            decisions.append(e.get("title", "Untitled"))
    if decisions:
        body += "### Decisions Made\n"
        for d in decisions[:5]:
            body += f"- {d}\n"
        body += "\n"
    else:
        body += "_No explicit decision-type notes yet. Review strongest conversations below to surface key calls._\n\n"

    # Themes from tags
    tag_counts = {}
    for e in entries:
        for t in e.get("enriched_frontmatter", {}).get("tags", []):
            tag_counts[t] = tag_counts.get(t, 0) + 1
    top_tags = sorted(tag_counts.items(), key=lambda x: -x[1])[:5]
    if top_tags:
        body += "### Top Tags\n"
        for t, c in top_tags:
            body += f"- #{t} ({c})\n"
        body += "\n"

    body += f"""## Strongest Recent Conversations

_These have the most signal for current work:_

{chr(10).join(convo_links)}

## All Conversations

_See full timeline below or query the enrichment mapping for complete list._

## Open Questions / Unresolved Threads

- [ ] {ctx['actions'][0].split(': ', 1)[1]}
- [ ] {ctx['actions'][1].split(': ', 1)[1]}

## Related

- [[../topics/ai-tools|AI Tools]]
- [[../../insights/q2-2026-action-tracker|Q2 Action Tracker]]
- [[../../insights/concrete-action-plan-Q2-2026|Concrete Action Plan]]
"""

    return body


# Generate all 5 nodes
PROJECTS = [
    ("homelab-stack", "Homelab Stack"),
    ("private-ai-consulting", "Private AI Consulting"),
    ("operation-immortal-agent", "Operation Immortal Agent"),
    ("it-certification", "IT Certification"),
    ("second-brain-vault", "Second Brain Vault"),
]

for slug, display in PROJECTS:
    entries = extract_project_data(slug)
    node_path = VAULT / "nodes" / "projects" / f"{slug}.md"
    node_path.write_text(build_project_node(slug, display, entries), encoding="utf-8")
    print(f"Written: {node_path} ({len(entries)} conversations)")

print("\nAll 5 project nodes enriched.")
