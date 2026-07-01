#!/usr/bin/env python3
"""
Strict rebuild of all node pages with accurate project/person detection.
"""
import os, re, json, glob
from pathlib import Path
from collections import defaultdict, Counter

VAULT = Path("/vault")
PROCESSED = VAULT / "processed"
NODES = VAULT / "nodes"

SOURCES = ["CLAUDE", "GEMINI", "GPT", "GROK"]

# STRICT project detection: must match specific phrase combos, not single words
PROJECT_RULES = {
    "flappy-meme-bird": {
        "phrases": ["flappy bird", "meme bird", "flappy meme", "flappy game", "pygame bird", "game dev bird"],
        "require_any": ["flappy", "pygame", "game dev"],
    },
    "homelab-stack": {
        "phrases": ["homelab stack", "home lab", "server stack", "proxmox", "nas setup", "router config", "network lab"],
        "require_any": ["homelab", "server rack", "unraid", "truenas", "pfsense", "opnsense"],
    },
    "it-certification": {
        "phrases": ["it certification", "comptia", "security+", "network+", "a+ exam", "a+ cert", "it cert", "help desk cert", "it job cert", "tiffin cert", "tiffin university", "secai cert"],
        "require_any": ["comptia", "security+", "network+", "tiffin", "secai", "certification exam", "it certification"],
        "forbid": ["ssl cert", "tls cert", "https cert", "root cert", "ca cert"],  # must NOT contain these
    },
    "operation-immortal-agent": {
        "phrases": ["operation immortal", "immortal agent", "dlmm bot", "meteora bot", "solana bot", "liquidity bot", "yield bot", "autonomous fund", "agent trade", "agent fund", "immortal fund"],
        "require_any": ["meteora", "dlmm", "operation immortal", "immortal agent", "jupiter perp", "autonomous solana"],
    },
    "private-ai-consulting": {
        "phrases": ["private ai", "ai consulting", "local ai consulting", "ai business", "ai service business", "ai solution business", "custom ai", "client ai", "business ai"],
        "require_any": ["private ai", "ai consulting", "ai implementation", "ai business", "client ai"],
    },
    "second-brain-vault": {
        "phrases": ["second brain", "obsidian vault", "knowledge base", "pkm", "personal knowledge", "zettelkasten", "vault setup", "obsidian graph"],
        "require_any": ["second brain", "obsidian vault", "knowledge management", "zettelkasten", "pkm"],
    },
    "streaming-rig": {
        "phrases": ["streaming rig", "stream setup", "obs setup", "twitch setup", "youtube stream", "multistream", "streaming hardware", "stream deck", "capture card"],
        "require_any": ["obs studio", "streaming rig", "twitch stream", "youtube stream", "multistream", "elgato", "stream deck", "voicemeeter"],
    },
}

def load_mapping():
    path = VAULT / "_meta" / "enrichment_mapping.json"
    return json.loads(path.read_text(encoding="utf-8"))

def detect_projects(title, body_text):
    """Strict phrase-based project detection."""
    combined = (title + " " + body_text).lower()
    found = []
    for proj_name, rules in PROJECT_RULES.items():
        # Check forbid list first
        if any(forbid in combined for forbid in rules.get("forbid", [])):
            # But only skip if the forbid is in a strong context, not just the word
            # Skip this project if ANY forbid phrase is present
            pass  # Actually, let Require_any override
        # Check phrases (exact multi-word matches)
        if any(phrase in combined for phrase in rules.get("phrases", [])):
            found.append(proj_name)
            continue
        # Check required terms with context (must have at least one)
        if any(term in combined for term in rules.get("require_any", [])):
            found.append(proj_name)
    return list(set(found))  # dedupe

def extract_user_turns(body, source):
    user_markers = {
        "CLAUDE": ["### HUMAN"],
        "GEMINI": ["### USER"],
        "GPT": ["### USER", "### HUMAN"],
        "GROK": ["### USER", "### HUMAN"],
    }
    ai_markers = {
        "CLAUDE": ["### ASSISTANT"],
        "GEMINI": ["### GEMINI"],
        "GPT": ["### ASSISTANT", "### GPT"],
        "GROK": ["### ASSISTANT", "### GROK"],
    }
    markers = user_markers.get(source, ["### HUMAN", "### USER"])
    ai_ms = ai_markers.get(source, ["### ASSISTANT"])
    lines = []
    in_user = False
    for line in body_text.splitlines():
        stripped = line.strip()
        if any(stripped.startswith(m) for m in markers):
            in_user = True
            continue
        if any(stripped.startswith(m) for m in ai_ms):
            in_user = False
            continue
        if in_user and stripped:
            lines.append(stripped)
    return " ".join(lines)

def rebuild_topic_pages(mapping):
    topics_dir = NODES / "topics"
    topics_dir.mkdir(parents=True, exist_ok=True)
    topic_data = defaultdict(lambda: {"conversations": [], "tags": Counter(), "projects": set(), "people": set()})

    for item in mapping:
        fm = item["enriched_frontmatter"]
        cat = fm["category"]
        rel = item["file"]
        date = fm.get("date", "")
        title = item["title"]
        source = item["source"]

        topic_data[cat]["conversations"].append({"path": rel, "title": title, "date": date, "source": source})
        for t in fm.get("tags", []):
            topic_data[cat]["tags"][t] += 1
        # Skip project detection here, do it separately
        for person in fm.get("linked_nodes", []):
            topic_data[cat]["people"].add(person)

    for cat, data in topic_data.items():
        fpath = topics_dir / f"{cat}.md"
        convs = sorted(data["conversations"], key=lambda x: x["date"] or "")
        top_tags = data["tags"].most_common(10)
        people_list = sorted(data["people"])

        src_counts = Counter(c["source"] for c in convs)
        date_range = ""
        if convs:
            dates = [c["date"] for c in convs if c["date"]]
            if dates:
                date_range = f"{min(dates)} to {max(dates)}"

        md = f"""---
type: topic
tags: [topic, moc]
aliases: [{cat.replace('-', ' ')}]
---

# {cat.replace('-', ' ').title()}

> 🧠 Topic hub for **{cat.replace('-', ' ').title()}**.

## Stats
- **Total conversations**: {len(convs)}
- **Date range**: {date_range or 'N/A'}
- **By source**: {', '.join([f'{s}={c}' for s,c in src_counts.most_common()])}
- **Top tags**: {', '.join([t for t,_ in top_tags[:8]])}
- **Linked people**: {', '.join([f"[[nodes/people/{p}|{p.title()}]]" for p in people_list]) if people_list else 'None'}

## Conversations
"""
        for c in convs:
            md += f"- [[{c['path']}|{c['title'][:80]}]] — {c['date']} ({c['source']})\n"

        md += "\n## Connected Topics\n"
        for other in sorted(topic_data.keys()):
            if other != cat:
                md += f"- [[nodes/topics/{other}.md|{other.replace('-',' ').title()}]]\n"

        md += "\n## Patterns Noticed\n_What questions does Bryan keep asking? What does he seem to understand vs not?_\n\n"

        fpath.write_text(md, encoding="utf-8")
        print(f"  Topic: {fpath} ({len(convs)} convs, {len(md)//1024}KB)")

    return topic_data

def rebuild_project_pages(mapping, topic_data):
    projects_dir = NODES / "projects"
    projects_dir.mkdir(parents=True, exist_ok=True)

    project_data = defaultdict(lambda: {"conversations": [], "first": None, "last": None, "topic": set()})

    for item in mapping:
        # Use STRICT project detection
        projects = detect_projects(item["title"], item.get("body", ""))
        if not projects:
            continue

        fm = item["enriched_frontmatter"]
        rel = item["file"]
        date = fm.get("date", "")
        title = item["title"]
        cat = fm.get("category", "general")

        for proj in projects:
            project_data[proj]["conversations"].append({"path": rel, "title": title, "date": date, "category": cat})
            project_data[proj]["topic"].add(cat)
            if date:
                if project_data[proj]["first"] is None or date < project_data[proj]["first"]:
                    project_data[proj]["first"] = date
                if project_data[proj]["last"] is None or date > project_data[proj]["last"]:
                    project_data[proj]["last"] = date

    for proj, data in project_data.items():
        fpath = projects_dir / f"{proj}.md"
        convs = sorted(data["conversations"], key=lambda x: x["date"] or "")

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
            md += f"- [[{c['path']}|{c['title'][:80]}]] — {c['date']}\n"

        md += "\n## Related Topics\n"
        for t in sorted(data["topic"]):
            md += f"- [[nodes/topics/{t}.md|{t.replace('-',' ').title()}]]\n"

        md += "\n## Current State\n_What was the last thing Bryan was working on?_\n\n"
        md += "\n## Open Questions / Unresolved Threads\n_Things he asked about but didn't resolve._\n\n"

        fpath.write_text(md, encoding="utf-8")
        print(f"  Project: {fpath} ({len(convs)} convs)")

    # Clean up old project files not in current set
    for old in projects_dir.glob("*.md"):
        if old.stem not in project_data:
            print(f"  Removing stale project: {old}")
            old.unlink()

    return project_data

def rebuild_people_pages(mapping):
    people_dir = NODES / "people"
    people_dir.mkdir(parents=True, exist_ok=True)

    person_data = defaultdict(lambda: {"conversations": [], "mentions": 0})

    for item in mapping:
        fm = item["enriched_frontmatter"]
        for person in fm.get("linked_nodes", []):
            rel = item["file"]
            date = fm.get("date", "")
            title = item["title"]
            source = item["source"]
            person_data[person]["conversations"].append({"path": rel, "title": title, "date": date, "source": source})
            person_data[person]["mentions"] += 1

    for person, data in person_data.items():
        fpath = people_dir / f"{person}.md"
        convs = sorted(data["conversations"], key=lambda x: x["date"] or "")
        sources = sorted(set(c["source"] for c in convs))

        md = f"""---
type: person
tags: [people]
---

# {person.title()}

## Mentioned In
{len(convs)} conversation(s) across {len(sources)} source(s): {', '.join(sources)}.\n
## Conversations
"""
        for c in convs:
            md += f"- [[{c['path']}|{c['title'][:80]}]] — {c['date']} ({c['source']})\n"

        md += "\n## Context\n_What role does this person play in Bryan's conversations?_\n\n"

        fpath.write_text(md, encoding="utf-8")
        print(f"  Person: {fpath} ({len(convs)} convs)")

    # Clean up stale people pages
    for old in people_dir.glob("*.md"):
        if old.stem not in person_data:
            print(f"  Removing stale person: {old}")
            old.unlink()

def update_mapping_with_projects(mapping):
    """Recompute linked_projects in the mapping itself."""
    for item in mapping:
        item["enriched_frontmatter"]["linked_projects"] = detect_projects(item["title"], item.get("body", ""))
    # Save back
    out = VAULT / "_meta" / "enrichment_mapping.json"
    out.write_text(json.dumps(mapping, indent=2), encoding="utf-8")
    counts = Counter()
    for item in mapping:
        for p in item["enriched_frontmatter"]["linked_projects"]:
            counts[p] += 1
    print("\nRecomputed project distribution:")
    for p, c in counts.most_common():
        print(f"  {p}: {c}")

def main():
    mapping = load_mapping()
    print(f"Loaded {len(mapping)} records.")

    # First: recompute projects with strict rules
    update_mapping_with_projects(mapping)
    # Reload after update
    mapping = load_mapping()

    topic_data = rebuild_topic_pages(mapping)
    project_data = rebuild_project_pages(mapping, topic_data)
    rebuild_people_pages(mapping)

    print(f"\n=== Done ===")
    print(f"Topics: {len(topic_data)}")
    print(f"Projects: {len(project_data)}")
    print(f"People: {len(person_data)}")

if __name__ == "__main__":
    main()
