#!/usr/bin/env python3
"""
fix_enrichment_issues.py -- Fix all three minor enrichment quality issues.

1. Add missing source/id to 367 files from second pass
2. Normalize resolution values (unresolved->partial, resolved->resolved)
3. Cap over-tagged files at 6 tags max

Usage: python3 fix_enrichment_issues.py
"""

import os
import re
import yaml
import glob
import random
import string

VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
PROCESSED_DIR = os.path.join(VAULT_PATH, "processed")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "enrichment-final-fixes.log")

# Provider folder mapping
PROVIDER_FOLDERS = {
    "CLAUDE": "CLAUDE",
    "GEMINI": "GEMINI",
    "GPT": "GPT",
    "GROK": "GROK",
}

# Resolution normalization map
RESOLUTION_MAP = {
    "unresolved": "partial",
    "resolved": "resolved",
    # Keep existing values as-is
    "partial": "partial",
    "abandoned": "abandoned",
}

generated_ids = set()


def gen_id():
    """Generate a unique synthetic ID."""
    while True:
        new_id = "v3-" + "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
        if new_id not in generated_ids:
            generated_ids.add(new_id)
            return new_id


def read_frontmatter(filepath):
    """Read YAML frontmatter from a markdown file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1)), content
        except yaml.YAMLError:
            return None, content
    return None, content


def write_frontmatter(filepath, fm, content):
    """Write YAML frontmatter back to a markdown file."""
    body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, flags=re.DOTALL)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(yaml.dump(fm, default_flow_style=False, allow_unicode=True))
        f.write("---\n")
        f.write(body)


def get_provider_from_path(filepath):
    """Infer provider from directory structure."""
    rel = os.path.relpath(filepath, PROCESSED_DIR)
    top_dir = rel.split(os.sep)[0]
    return top_dir.upper() if top_dir.upper() in PROVIDER_FOLDERS else "UNKNOWN"


def main():
    log = []
    stats = {
        "source_id_fixed": 0,
        "resolution_normalized": 0,
        "tags_trimmed": 0,
        "unchanged": 0,
        "errors": 0,
    }

    files = sorted(glob.glob(os.path.join(PROCESSED_DIR, "**", "*.md"), recursive=True))
    # Exclude CONVERSATION-HUB
    files = [f for f in files if "CONVERSATION-HUB" not in f]

    log.append(f"Processing {len(files)} files...")

    for filepath in files:
        filename = os.path.basename(filepath)
        try:
            fm, content = read_frontmatter(filepath)
            if not fm:
                stats["unchanged"] += 1
                continue

            changed = False

            # Fix 1: Add missing source/id
            if "source" not in fm or "id" not in fm:
                if "source" not in fm:
                    provider = get_provider_from_path(filepath)
                    fm["source"] = provider
                    log.append(f"  SOURCE: {filename} -> added source={provider}")
                if "id" not in fm:
                    fm["id"] = gen_id()
                    log.append(f"  ID: {filename} -> added id={fm['id']}")
                stats["source_id_fixed"] += 1
                changed = True

            # Fix 2: Normalize resolution values
            old_resolution = fm.get("resolution", "")
            if old_resolution in RESOLUTION_MAP:
                new_resolution = RESOLUTION_MAP[old_resolution]
                if new_resolution != old_resolution:
                    fm["resolution"] = new_resolution
                    log.append(f"  RESOLUTION: {filename}: '{old_resolution}' -> '{new_resolution}'")
                    stats["resolution_normalized"] += 1
                    changed = True

            # Fix 3: Cap tags at 6 max
            tags = fm.get("tags", [])
            if isinstance(tags, list) and len(tags) > 6:
                fm["tags"] = tags[:6]
                log.append(f"  TAGS: {filename}: {len(tags)} tags -> trimmed to 6")
                stats["tags_trimmed"] += 1
                changed = True

            if changed:
                write_frontmatter(filepath, fm, content)
            else:
                stats["unchanged"] += 1

        except Exception as e:
            log.append(f"  ERROR: {filename}: {e}")
            stats["errors"] += 1

    # Summary
    log.append(f"\n{'='*60}")
    log.append(f"Final Fixes Complete")
    log.append(f"{'='*60}")
    log.append(f"Files with source/id added: {stats['source_id_fixed']}")
    log.append(f"Resolutions normalized:     {stats['resolution_normalized']}")
    log.append(f"Tags trimmed (6 max):      {stats['tags_trimmed']}")
    log.append(f"Files unchanged:           {stats['unchanged']}")
    log.append(f"Errors:                    {stats['errors']}")

    # Write log
    with open(LOG_PATH, "w") as f:
        f.write("\n".join(log))

    # Print summary
    for line in log[-10:]:
        print(line)
    print(f"\nFull log: {LOG_PATH}")


if __name__ == "__main__":
    main()
