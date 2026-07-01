#!/usr/bin/env python3
"""
fix_missing_enrichment.py -- Restore new enrichment for files that lost it.
Some files had their new enrichment block deleted by the v5 frontmatter fix.
This script reads the enrichment logs and restores the correct frontmatter.
"""

import os
import re
import glob
import yaml

VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
PROCESSED_DIR = os.path.join(VAULT_PATH, "processed")
V2_LOG = os.path.join(VAULT_PATH, "_meta", "enrichment-log-v2.md")
V3_LOG = os.path.join(VAULT_PATH, "_meta", "enrichment-log-v3.md")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "fix-missing-enrichment.log")


def parse_enrichment_log(log_path):
    """Parse an enrichment log and return a dict of filename -> enrichment data."""
    entries = {}
    if not os.path.exists(log_path):
        return entries

    with open(log_path, "r") as f:
        content = f.read()

    # Parse each file entry
    # Format: ### FILENAME (PROVIDER)
    # - **Category:** ...
    # - **Tags:** [...]
    # etc.
    pattern = r'###\s+(.+?)\s+\((.+?)\)\n(.*?)(?=###|\Z)'
    for match in re.finditer(pattern, content, re.DOTALL):
        filename = match.group(1).strip()
        provider = match.group(2).strip()
        fields_text = match.group(3)

        entry = {"source": provider}

        # Extract fields
        cat_match = re.search(r'\*\*Category:\*\*\s*(.+)', fields_text)
        if cat_match:
            entry["category"] = cat_match.group(1).strip()

        tags_match = re.search(r'\*\*Tags:\*\*\s*(\[.+?\])', fields_text, re.DOTALL)
        if tags_match:
            try:
                entry["tags"] = yaml.safe_load(tags_match.group(1))
            except:
                pass

        sent_match = re.search(r'\*\*Sentiment:\*\*\s*(.+)', fields_text)
        if sent_match:
            entry["sentiment"] = sent_match.group(1).strip()

        res_match = re.search(r'\*\*Resolution:\*\*\s*(.+)', fields_text)
        if res_match:
            entry["resolution"] = res_match.group(1).strip()

        proj_match = re.search(r'\*\*Linked Projects:\*\*\s*(\[.+?\])', fields_text, re.DOTALL)
        if proj_match:
            try:
                entry["linked_projects"] = yaml.safe_load(proj_match.group(1))
            except:
                pass

        nodes_match = re.search(r'\*\*Linked Nodes:\*\*\s*(\[.+?\])', fields_text, re.DOTALL)
        if nodes_match:
            try:
                entry["linked_nodes"] = yaml.safe_load(nodes_match.group(1))
            except:
                pass

        summary_match = re.search(r'\*\*Summary:\*\*\s*(.+?)(?=\n-|\Z)', fields_text, re.DOTALL)
        if summary_match:
            entry["summary"] = summary_match.group(1).strip()

        entries[filename] = entry

    return entries


def read_frontmatter(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1)), content
        except:
            pass
    return None, content


def write_frontmatter(filepath, fm, body):
    yaml_str = yaml.dump(fm, default_flow_style=False, allow_unicode=True).strip()
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n" + yaml_str + "\n---\n" + body)


def get_body(content):
    """Extract body from content (everything after first frontmatter block)."""
    match = re.match(r'^---\s*\n.*?\n---\s*\n', content, re.DOTALL)
    if match:
        return content[match.end():]
    return content


def main():
    log = []
    fixed = 0
    skipped = 0
    errors = 0

    # Load enrichment data from logs
    enrichment = {}
    enrichment.update(parse_enrichment_log(V2_LOG))
    enrichment.update(parse_enrichment_log(V3_LOG))
    log.append(f"Loaded {len(enrichment)} enrichment entries from logs")

    # Find files that need fixing
    files = sorted(glob.glob(os.path.join(PROCESSED_DIR, "**", "*.md"), recursive=True))
    files = [f for f in files if "CONVERSATION-HUB" not in f]

    for filepath in files:
        filename = os.path.basename(filepath)
        try:
            fm, content = read_frontmatter(filepath)
            if not fm:
                continue

            # Check if file is missing new enrichment (no summary field)
            if "summary" in fm:
                skipped += 1
                continue

            # File has old enrichment only -- try to restore from log
            if filename in enrichment:
                new_fm = enrichment[filename]
                body = get_body(content)

                # Preserve the original id and date
                if "id" in fm:
                    new_fm["id"] = fm["id"]
                if "date" in fm:
                    new_fm["date"] = fm["date"]

                write_frontmatter(filepath, new_fm, body)
                log.append(f"  RESTORED: {filename} (category: {new_fm.get('category', '?')})")
                fixed += 1
            else:
                skipped += 1

        except Exception as e:
            log.append(f"  ERROR: {filename}: {e}")
            errors += 1

    log.append(f"\nDone! {fixed} restored, {skipped} skipped, {errors} errors")

    with open(LOG_PATH, "w") as f:
        f.write("\n".join(log))

    for line in log[-10:]:
        print(line)
    print(f"\nFull log: {LOG_PATH}")


if __name__ == "__main__":
    main()
