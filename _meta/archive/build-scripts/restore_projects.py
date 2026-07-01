#!/usr/bin/env python3
"""
Restore homelab-stack and private-ai-consulting projects with balanced matching.
"""
import json
from pathlib import Path
from collections import defaultdict

VAULT = Path("/vault")
m = json.loads((VAULT / "_meta" / "enrichment_mapping.json").read_text(encoding="utf-8"))

HOMELAB_KEYWORDS = [
    "4090", "rtx", "7700", "ryzen", "pfsense", "opnsense", "unraid", "truenas",
    "proxmox", "nas", "server rack", "home server", "gpu cooling",
    "nvidia-smi", "dual boot", "cachyos install", "cachyos setup",
    "hardware", "build", "desktop-n", "steam deck",
]

def is_homelab(item):
    title = item["title"].lower()
    body = item.get("body", "").lower()
    combined = title + " " + body
    tags = item["enriched_frontmatter"].get("tags", [])
    cat = item["enriched_frontmatter"].get("category", "")
    count = 0
    for kw in HOMELAB_KEYWORDS:
        if kw in combined:
            count += 1
    # Also count if in homelab category + has hardware tags
    if cat == "homelab" and count >= 2:
        return True
    if cat == "homelab" and any(t in ["hardware", "nvidia", "linux", "cachyos", "windows"] for t in tags):
        return True
    if count >= 3:
        return True
    return False

CONSULT_KEYWORDS = [
    "private ai", "ai consulting", "ai business", "ai for business",
    "client ai", "custom ai", "sell ai", "ai service", "local ai",
    "ai solution", "implement ai", "offer ai", "ai product",
    "profitab", "revenue", "business name", "pc repair", "custom build",
    "tech service", "tech support business", "freelance ai",
]

def is_consulting(item):
    title = item["title"].lower()
    body = item.get("body", "").lower()
    combined = title + " " + body
    count = 0
    for kw in CONSULT_KEYWORDS:
        if kw in combined:
            count += 1
    if count >= 2:
        return True
    # Check for goals-related signals
    if "resume" in combined and "ai" in combined and "linkedin" in combined:
        return True
    if "business" in combined and "ai" in combined and "build" in combined:
        return True
    return False

# Build project data
project_data = defaultdict(lambda: {"conversations": [], "first": None, "last": None, "topic": set()})

for item in m:
    fm = item["enriched_frontmatter"]
    rel = item["file"]
    date = fm.get("date", "")
    title = item["title"]
    cat = fm.get("category", "general")
    source = item["source"]

    # Add to existing projects from mapping
    for proj in fm.get("linked_projects", []):
        project_data[proj]["conversations"].append({"path": rel, "title": title, "date": date, "category": cat, "source": source})
        project_data[proj]["topic"].add(cat)
        if date:
            if project_data[proj]["first"] is None or date < project_data[proj]["first"]:
                project_data[proj]["first"] = date
            if project_data[proj]["last"] is None or date > project_data[proj]["last"]:
                project_data[proj]["last"] = date

    # Check homelab-stack
    if is_homelab(item):
        proj = "homelab-stack"
        project_data[proj]["conversations"].append({"path": rel, "title": title, "date": date, "category": cat, "source": source})
        project_data[proj]["topic"].add(cat)
        if date:
            if project_data[proj]["first"] is None or date < project_data[proj]["first"]:
                project_data[proj]["first"] = date
            if project_data[proj]["last"] is None or date > project_data[proj]["last"]:
                project_data[proj]["last"] = date

    # Check private-ai-consulting
    if is_consulting(item):
        proj = "private-ai-consulting"
        project_data[proj]["conversations"].append({"path": rel, "title": title, "date": date, "category": cat, "source": source})
        project_data[proj]["topic"].add(cat)
        if date:
            if project_data[proj]["first"] is None or date < project_data[proj]["first"]:
                project_data[proj]["first"] = date
            if project_data[proj]["last"] is None or date > project_data[proj]["last"]:
                project_data[proj]["last"] = date

# Write all project files
projects_dir = VAULT / "nodes" / "projects"
projects_dir.mkdir(parents=True, exist_ok=True)

for proj, data in project_data.items():
    fpath = projects_dir / f"{proj}.md"
    convs = sorted(data["conversations"], key=lambda x: x["date"] or "")

    # Deduplicate conversations by path
    seen_paths = set()
    unique_convs = []
    for c in convs:
        if c["path"] not in seen_paths:
            seen_paths.add(c["path"])
            unique_convs.append(c)
    convs = unique_convs

    md = f"""---
type: project
status: active
first_seen: {data['first'] or 'unknown'}
last_seen: {data['last'] or 'unknown'}
tags: [project, synthesis]
---

# {proj.replace('-', ' ').title()}

> Evergreen notes on {proj.replace('-', ' ')}.

## What It Is
Project identified across {len(convs)} conversation(s). First seen {data['first'] or '?'}. Last seen {data['last'] or '?'}.\n
## Conversation Timeline
"""
    for c in convs:
        md += f"- [[{c['path']}|{c['title'][:80]}]] — {c['date']} ({c['source']})\n"

    md += "\n## Related Topics\n"
    for t in sorted(data["topic"]):
        md += f"- [[nodes/topics/{t}.md|{t.replace('-',' ').title()}]]\n"

    md += "\n## Current State\n_What was the last thing Bryan was working on?_\n\n"
    md += "\n## Open Questions / Unresolved Threads\n_Things he asked about but didn't resolve._\n\n"

    fpath.write_text(md, encoding="utf-8")
    print(f"  Project: {proj} ({len(convs)} convs)")

# Summary
print("\n=== PROJECT DISTRIBUTION ===")
for proj, data in sorted(project_data.items(), key=lambda x: -len(x[1]["conversations"])):
    convs = data["conversations"]
    seen = len(set(c["path"] for c in convs))
    print(f"  {proj}: {seen} conversations")
