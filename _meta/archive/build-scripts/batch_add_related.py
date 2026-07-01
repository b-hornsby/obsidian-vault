#!/usr/bin/env python3
"""Batch-append a '## Related' section to processed chat files.
Targets ~300 highest-value conversations (major projects, recent, diverse sources).
"""

import json
import random
from pathlib import Path

VAULT = Path("/vault")
MAPPING = json.loads((VAULT / "_meta" / "enrichment_mapping.json").read_text())

# Major projects we want to surface
MAJOR_PROJECTS = {
    "homelab-stack": "Homelab Stack",
    "private-ai-consulting": "Private AI Consulting",
    "operation-immortal-agent": "Operation Immortal Agent",
    "it-certification": "IT Certification",
    "second-brain-vault": "Second Brain Vault",
}

# Tag → topic node mapping (best effort from top tags)
TAG_TO_TOPIC = {
    "coding": "coding",
    "ai": "ai-tools",
    "ai-tools": "ai-tools",
    "homelab": "homelab",
    "career": "career",
    "crypto": "crypto-web3",
    "trading": "crypto-web3",
    "llm": "ai-tools",
    "docker": "homelab",
    "linux": "homelab",
}


def pick_target_files(limit=300):
    """Pick the most valuable files to enrich.
    Priority: major-project-linked, recent, then random fill."""
    major_linked = []
    for entry in MAPPING:
        projects = entry.get("enriched_frontmatter", {}).get("linked_projects", [])
        if any(p in MAJOR_PROJECTS for p in projects):
            major_linked.append(entry)
    # Sort by date desc
    def date_key(e):
        try:
            return e.get("file", "").split("_")[0].replace("processed/", "")
        except Exception:
            return ""
    major_linked.sort(key=date_key, reverse=True)
    return major_linked[:limit]


def build_related_section(entry):
    """Build a markdown Related section with wikilinks."""
    ef = entry.get("enriched_frontmatter", {})
    projects = ef.get("linked_projects", [])
    tags = ef.get("tags", [])
    category = ef.get("category", "")

    lines = ["\n\n## Related\n"]

    # Project links
    project_links = []
    for proj in projects:
        if proj in MAJOR_PROJECTS:
            project_links.append(
                f"- [[nodes/projects/{proj}|{MAJOR_PROJECTS[proj]}]]"
            )
    if project_links:
        lines.append("### Projects\n")
        lines.extend(project_links)
        lines.append("")

    # Topic links from tags
    topic_links = []
    seen_topics = set()
    for tag in tags:
        topic = TAG_TO_TOPIC.get(tag)
        if topic and topic not in seen_topics:
            topic_links.append(f"- [[nodes/topics/{topic}|{topic.replace('-', ' ').title()}]]")
            seen_topics.add(topic)
    if category and category not in seen_topics:
        topic_links.append(
            f"- [[nodes/topics/{category}|{category.replace('-', ' ').title()}]]"
        )
    if topic_links:
        lines.append("### Topics\n")
        lines.extend(topic_links)
        lines.append("")

    return "\n".join(lines)


def append_related(entry):
    """Append the Related section to the physical file if it doesn't already have one."""
    rel_path = entry.get("file", "")
    if not rel_path:
        return False
    # The file field already starts with "processed/..."
    filepath = VAULT / rel_path
    if not filepath.exists():
        return False

    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception:
        return False

    # Skip if already has a Related section
    if "## Related" in content:
        return False

    section = build_related_section(entry)
    filepath.write_text(content + section, encoding="utf-8")
    return True


def main():
    targets = pick_target_files(300)
    updated = 0
    skipped = 0
    for entry in targets:
        if append_related(entry):
            updated += 1
        else:
            skipped += 1
    print(f"Targets: {len(targets)}")
    print(f"Updated: {updated}")
    print(f"Skipped (already had Related or missing file): {skipped}")


if __name__ == "__main__":
    main()
