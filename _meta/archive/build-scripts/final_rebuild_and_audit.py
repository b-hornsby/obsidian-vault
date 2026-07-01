#!/usr/bin/env python3
"""
Final rebuild: topics get project links. Final audit. Ensure all cross-links work.
"""
import json, re
from pathlib import Path
from collections import defaultdict, Counter

VAULT = Path("/vault")
m = json.loads((VAULT / "_meta" / "enrichment_mapping.json").read_text(encoding="utf-8"))

def get_topic_projects():
    """Build cat -> projects mapping."""
    cat_projects = defaultdict(set)
    item_map = {i["file"]: i for i in m}
    for item in m:
        cat = item["enriched_frontmatter"]["category"]
        for proj in item["enriched_frontmatter"].get("linked_projects", []):
            cat_projects[cat].add(proj)
    return cat_projects

def rebuild_topics_with_projects():
    cat_data = defaultdict(lambda: {"conversations": [], "tags": Counter(), "people": set(), "projects": set()})
    for item in m:
        fm = item["enriched_frontmatter"]
        cat = fm["category"]
        cat_data[cat]["conversations"].append({
            "path": item["file"], "title": item["title"],
            "date": fm.get("date", ""), "source": item["source"]
        })
        for t in fm.get("tags", []):
            cat_data[cat]["tags"][t] += 1
        for p in fm.get("linked_projects", []):
            cat_data[cat]["projects"].add(p)
        for person in fm.get("linked_nodes", []):
            cat_data[cat]["people"].add(person)

    topics_dir = VAULT / "nodes" / "topics"
    for cat, data in cat_data.items():
        fpath = topics_dir / f"{cat}.md"
        convs = sorted(data["conversations"], key=lambda x: x["date"] or "")
        top_tags = data["tags"].most_common(8)
        people_list = sorted(data["people"])
        proj_list = sorted(data["projects"])
        src_counts = Counter(c["source"] for c in convs)
        dates = [c["date"] for c in convs if c["date"]]
        dr = f"{min(dates)} to {max(dates)}" if dates else "N/A"

        md = f"""---
type: topic
tags: [topic, moc]
aliases: [{cat.replace('-', ' ')}]
---

# {cat.replace('-', ' ').title()}

> 🧠 Topic hub for **{cat.replace('-', ' ').title()}**.

## Stats
- **Total conversations**: {len(convs)}
- **Date range**: {dr}
- **By source**: {', '.join([f'{s}={c}' for s,c in src_counts.most_common()])}
- **Top tags**: {', '.join([t for t,_ in top_tags])}
- **Linked projects**: {', '.join([f"[[nodes/projects/{p}|{p.replace('-',' ').title()}]]" for p in proj_list]) if proj_list else 'None'}
- **Linked people**: {', '.join([f"[[nodes/people/{p}|{p.title()}]]" for p in people_list]) if people_list else 'None'}

## Conversations
"""
        for c in convs:
            md += f"- [[{c['path']}|{c['title'][:80]}]] — {c['date']} ({c['source']})\n"

        md += "\n## Connected Topics\n"
        for other in sorted(cat_data.keys()):
            if other != cat:
                md += f"- [[nodes/topics/{other}.md|{other.replace('-',' ').title()}]]\n"

        md += "\n## Patterns Noticed\n_What questions does Bryan keep asking? What does he seem to understand vs not?_\n\n"
        fpath.write_text(md, encoding="utf-8")
        print(f"  Topic: {cat} ({len(convs)} convs)")

def final_audit():
    print("\n" + "="*60 + "\nFINAL AUDIT\n" + "="*60)

    # Counts
    dirs = [VAULT/"nodes"/"topics", VAULT/"nodes"/"projects", VAULT/"nodes"/"people",
            VAULT/"insights"/"weekly", VAULT/"insights"/"blind-spots"]
    for d in dirs:
        print(f"  {d}: {len(list(d.glob('*.md')))} files")

    # Wikilink sanity: check if targets resolve
    vault_files = {}
    for f in VAULT.rglob("*.md"):
        if '.obsidian' in str(f): continue
        rel = str(f.relative_to(VAULT))
        vault_files[rel] = f
        vault_files[f.stem] = f
        # Also register without .md for exact match
        vault_files[rel.replace('.md', '')] = f

    broken = Counter()
    total_links = 0
    for f in VAULT.rglob("*.md"):
        if '.obsidian' in str(f): continue
        content = f.read_text(encoding="utf-8", errors="ignore")
        for match in re.findall(r'\[\[([^\]|#\]]+)', content):
            total_links += 1
            target = match.strip().lstrip('/')
            if target not in vault_files and (target + '.md') not in vault_files:
                broken[f] += 1

    print(f"\n  Total link instances: {total_links}")
    print(f"  Files with potentially broken links: {len(broken)}")
    if broken:
        # Print 5 worst offenders
        for f, c in broken.most_common(5):
            print(f"    {f.relative_to(VAULT)}: {c} broken targets")

    # Distribution
    cats = Counter(i["enriched_frontmatter"]["category"] for i in m)
    print("\n  Category distribution:")
    for cat, c in cats.most_common():
        print(f"    {cat}: {c}")

    # Sentiment
    sents = Counter(i["enriched_frontmatter"]["sentiment"] for i in m)
    print("\n  Sentiment distribution:")
    for s, c in sents.most_common():
        print(f"    {s}: {c}")

    print("\n" + "="*60)

if __name__ == "__main__":
    rebuild_topics_with_projects()
    final_audit()
