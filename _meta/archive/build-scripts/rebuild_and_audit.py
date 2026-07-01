#!/usr/bin/env python3
"""
Rebuild all node pages WITHOUT conversation caps.
Then run comprehensive vault audit.
"""
import os, re, json, glob
from pathlib import Path
from collections import defaultdict, Counter

VAULT = Path("/vault")
PROCESSED = VAULT / "processed"
NODES = VAULT / "nodes"

SOURCES = ["CLAUDE", "GEMINI", "GPT", "GROK"]
PROJECT_NAMES = [
    "flappy-meme-bird", "homelab-stack", "it-certification",
    "operation-immortal-agent", "private-ai-consulting",
    "second-brain-vault", "streaming-rig"
]
PEOPLE = ["bryan", "dad", "girlfriend"]

def load_mapping():
    path = VAULT / "_meta" / "enrichment_mapping.json"
    return json.loads(path.read_text(encoding="utf-8"))

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

        topic_data[cat]["conversations"].append({"path": rel, "title": title, "date": date, "source": item["source"]})
        for t in fm.get("tags", []):
            topic_data[cat]["tags"][t] += 1
        for p in fm.get("linked_projects", []):
            topic_data[cat]["projects"].add(p)
        for person in fm.get("linked_nodes", []):
            topic_data[cat]["people"].add(person)

    for cat, data in topic_data.items():
        fpath = topics_dir / f"{cat}.md"
        convs = sorted(data["conversations"], key=lambda x: x["date"] or "")
        top_tags = data["tags"].most_common(10)
        projects_list = sorted(data["projects"])
        people_list = sorted(data["people"])

        # Cross-source breakdown
        src_counts = Counter(c["source"] for c in convs)

        md = f"""---
type: topic
tags: [topic, moc]
aliases: [{cat.replace('-', ' ')}]
---

# {cat.replace('-', ' ').title()}

> 🧠 Topic hub for **{cat.replace('-', ' ').title()}**.

## Stats
- **Total conversations**: {len(convs)}
- **By source**: {', '.join([f'{s}={c}' for s,c in src_counts.most_common()])}
- **Top tags**: {', '.join([t for t,_ in top_tags[:8]])}
- **Linked projects**: {', '.join([f"[[nodes/projects/{p}|{p.replace('-',' ').title()}]]" for p in projects_list]) if projects_list else 'None'}
- **Linked people**: {', '.join([f"[[nodes/people/{p}|{p.title()}]]" for p in people_list]) if people_list else 'None'}

## Conversations
"""
        for c in convs:
            md += f"- [[{c['path']}|{c['title'][:80]}]] — {c['date']} ({c['source']})\n"

        md += "\n## Connected Topics\n"
        for other in sorted(topic_data.keys()):
            if other != cat:
                md += f"- [[nodes/topics/{other}.md|{other.replace('-',' ').title()}]]\n"

        md += "\n## Patterns Noticed\n_What questions keep coming up? What does Bryan understand vs not?_\n\n"

        fpath.write_text(md, encoding="utf-8")
        print(f"  Rebuilt topic: {fpath} ({len(convs)} conversations, {len(md)} bytes)")

    return topic_data

def rebuild_project_pages(mapping, topic_data):
    projects_dir = NODES / "projects"
    projects_dir.mkdir(parents=True, exist_ok=True)

    project_data = defaultdict(lambda: {"conversations": [], "first": None, "last": None})

    for item in mapping:
        fm = item["enriched_frontmatter"]
        for p in fm.get("linked_projects", []):
            rel = item["file"]
            date = fm.get("date", "")
            title = item["title"]
            project_data[p]["conversations"].append({"path": rel, "title": title, "date": date})
            if date:
                if project_data[p]["first"] is None or date < project_data[p]["first"]:
                    project_data[p]["first"] = date
                if project_data[p]["last"] is None or date > project_data[p]["last"]:
                    project_data[p]["last"] = date

    for p, data in project_data.items():
        fpath = projects_dir / f"{p}.md"
        convs = sorted(data["conversations"], key=lambda x: x["date"] or "")

        md = f"""---
type: project
status: active
first_seen: {data['first'] or 'unknown'}
last_seen: {data['last'] or 'unknown'}
tags: [project, synthesis]
---

# {p.replace('-', ' ').title()}

> Evergreen notes on {p.replace('-', ' ')}.

## What It Is
Project identified across {len(convs)} conversation(s). First seen {data['first'] or '?'}. Last seen {data['last'] or '?'}.\n
## Conversation Timeline
"""
        for c in convs:
            md += f"- [[{c['path']}|{c['title'][:80]}]] — {c['date']}\n"

        md += "\n## Related Topics\n"
        for cat, tdata in topic_data.items():
            if p in tdata["projects"]:
                md += f"- [[nodes/topics/{cat}.md|{cat.replace('-',' ').title()}]]\n"

        md += "\n## Current State\n_What was the last thing Bryan was working on for this project?_\n\n"
        md += "\n## Open Questions / Unresolved Threads\n_Things he asked about but didn't resolve._\n\n"

        fpath.write_text(md, encoding="utf-8")
        print(f"  Rebuilt project: {fpath} ({len(convs)} conversations)")

    return project_data

def rebuild_people_pages(mapping):
    people_dir = NODES / "people"
    people_dir.mkdir(parents=True, exist_ok=True)

    person_data = defaultdict(lambda: {"conversations": [], "mentions": 0, "quotes": []})

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

        md = f"""---
type: person
tags: [people]
---

# {person.title()}

## Mentioned In
{len(convs)} conversation(s) across {len(set(c['source'] for c in convs))} source(s).\n
## Conversations
"""
        for c in convs:
            md += f"- [[{c['path']}|{c['title'][:80]}]] — {c['date']} ({c['source']})\n"

        md += "\n## Context\n_What role does this person play in Bryan's conversations?_\n\n"

        fpath.write_text(md, encoding="utf-8")
        print(f"  Rebuilt person: {fpath} ({len(convs)} conversations)")

def run_audit(mapping, topic_data):
    print("\n" + "="*60)
    print("VAULT AUDIT")
    print("="*60)

    # 1. Source directory integrity
    print("\n1. SOURCE DIRECTORY INTEGRITY")
    total_processed = len(mapping)
    print(f"   processed/ files: {total_processed}")
    print(f"   raw/ files: {len(list((VAULT/'raw').glob('*.md')))}")
    print(f"   Expected: 3400")

    # 2. Insight counts
    print("\n2. NODE COUNTS")
    dirs = {
        "nodes/topics": len(list((NODES/"topics").glob("*.md"))),
        "nodes/projects": len(list((NODES/"projects").glob("*.md"))),
        "nodes/people": len(list((NODES/"people").glob("*.md"))),
        "insights/weekly": len(list((VAULT/"insights"/"weekly").glob("*.md"))),
        "insights/blind-spots": len(list((VAULT/"insights"/"blind-spots").glob("*.md"))),
        "insights/patterns": len(list((VAULT/"insights"/"patterns").glob("*.md"))),
    }
    for d, c in dirs.items():
        print(f"   {d}: {c}")

    # 3. Wikilink sanity
    print("\n3. WIKILINK SANITY CHECK")
    all_files = set()
    all_links = defaultdict(list)
    for f in VAULT.rglob("*.md"):
        if '.obsidian' in str(f):
            continue
        all_files.add(f.stem)
        content = f.read_text(encoding="utf-8", errors="ignore")
        for link in re.findall(r'\[\[([^\]|#]+)', content):
            all_links[link].append(f.name)

    # Check for orphan links
    orphans = [l for l in all_links if l not in all_files]
    print(f"   Total unique links: {len(all_links)}")
    print(f"   Orphan links: {len(orphans)}")
    if orphans:
        short_orphans = [o for o in orphans if len(o) <= 30]
        print(f"   Sample orphans (up to 10): {short_orphans[:10]}")

    # 4. File size check (no huge files)
    print("\n4. FILE SIZE CHECK")
    huge = []
    for f in VAULT.rglob("*.md"):
        if '.obsidian' in str(f):
            continue
        size = f.stat().st_size
        if size > 500_000:
            huge.append((f.name, size))
    if huge:
        for n, s in huge[:5]:
            print(f"   WARN: {n} is {s//1024}KB")
    else:
        print("   All files under 500KB ✓")

    # 5. Distribution checks
    print("\n5. DISTRIBUTION CHECKS")
    cats = Counter(item["enriched_frontmatter"]["category"] for item in mapping)
    for cat, c in cats.most_common():
        print(f"   {cat}: {c}")

    # 6. Tag presence check
    print("\n6. ENRICHMENT FIELD CHECK")
    required_fields = ["tags", "category", "sentiment", "resolution", "linked_projects", "linked_nodes"]
    for field in required_fields:
        missing = sum(1 for item in mapping if field not in item["enriched_frontmatter"])
        print(f"   {field}: missing in {missing}/{len(mapping)} files")

    # 7. Graph connectivity
    print("\n7. GRAPH CONNECTIVITY PREVIEW")
    # Count how many topic pages link to processed files
    topic_wikilinks = 0
    for f in (NODES/"topics").glob("*.md"):
        content = f.read_text(encoding="utf-8", errors="ignore")
        topic_wikilinks += len(re.findall(r'\[\[processed/', content))
    print(f"   Topic pages -> processed: {topic_wikilinks} links")

    # Count how many processed files are NEVER linked from nodes
    linked_paths = set()
    for f in (NODES/"topics").glob("*.md"):
        content = f.read_text(encoding="utf-8", errors="ignore")
        for match in re.findall(r'\[\[(processed/[^\]|#]+)', content):
            linked_paths.add(match)
    print(f"   Unique processed files linked from topics: {len(linked_paths)}")
    print(f"   Total processed files: {total_processed}")
    print(f"   Coverage: {len(linked_paths)/total_processed*100:.1f}%")

    print("\n" + "="*60)
    print("AUDIT COMPLETE")
    print("="*60)

def main():
    mapping = load_mapping()
    print(f"Loaded {len(mapping)} enriched records from mapping.")

    topic_data = rebuild_topic_pages(mapping)
    project_data = rebuild_project_pages(mapping, topic_data)
    rebuild_people_pages(mapping)
    run_audit(mapping, topic_data)

if __name__ == "__main__":
    main()
