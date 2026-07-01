#!/usr/bin/env python3
"""
fix_all_frontmatter.py -- One script to fix ALL frontmatter issues.

Handles:
1. Duplicate frontmatter blocks (keep the NEW one with summary/linked_nodes)
2. Files where v5 kept the wrong (old) block
3. Ensures every file has exactly one clean frontmatter block

Strategy:
- Find the body (starts with # or ### USER/HUMAN/ASSISTANT/GEMINI/GPT/GROK)
- Find ALL frontmatter blocks before the body
- Keep the one that has 'summary' field (new enrichment)
- If none has summary, keep the first one
- Reconstruct the file
"""

import os
import re
import glob
import yaml

VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
PROCESSED_DIR = os.path.join(VAULT_PATH, "processed")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "fix-all-frontmatter.log")


def find_body_start(content):
    """Find where the actual body starts (markdown header or conversation turn)."""
    patterns = [
        r'\n# ',           # Markdown header
        r'\n### USER',     # Conversation turn
        r'\n### HUMAN',
        r'\n### ASSISTANT',
        r'\n### GEMINI',
        r'\n### GPT',
        r'\n### GROK',
    ]
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            return match.start() + 1  # Skip the newline
    return None


def parse_frontmatter_blocks(content, body_start):
    """Extract all frontmatter blocks before the body."""
    before = content[:body_start]
    # Split on --- delimiters
    parts = before.split('---')
    # parts[0] is empty (before first ---)
    # parts[1] is first FM content
    # parts[2] is either empty or second FM content
    # etc.
    blocks = []
    for i in range(1, len(parts), 2):
        if i < len(parts):
            fm_text = parts[i].strip()
            if fm_text:
                try:
                    fm = yaml.safe_load(fm_text)
                    if fm:
                        blocks.append(fm)
                except yaml.YAMLError:
                    pass
    return blocks


def choose_best_block(blocks):
    """Choose the best frontmatter block. Prefer the one with 'summary'."""
    if not blocks:
        return None
    if len(blocks) == 1:
        return blocks[0]
    # Prefer block with 'summary' (new enrichment)
    for block in blocks:
        if 'summary' in block:
            return block
    # Fallback: first block
    return blocks[0]


def fm_to_yaml(fm):
    """Convert frontmatter dict to YAML string."""
    return yaml.dump(fm, default_flow_style=False, allow_unicode=True).strip()


def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    body_start = find_body_start(content)
    if body_start is None:
        return False, "no_body"

    body = content[body_start:].strip()

    blocks = parse_frontmatter_blocks(content, body_start)
    if len(blocks) <= 1:
        return False, "single_block"

    best = choose_best_block(blocks)
    if best is None:
        return False, "no_fm"

    new_content = "---\n" + fm_to_yaml(best) + "\n---\n" + body

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True, f"fixed ({len(blocks)} blocks -> 1)"


def main():
    log = []
    fixed = 0
    skipped = 0
    errors = 0

    files = sorted(glob.glob(os.path.join(PROCESSED_DIR, "**", "*.md"), recursive=True))
    files = [f for f in files if "CONVERSATION-HUB" not in f]

    log.append(f"Scanning {len(files)} files...")

    for filepath in files:
        filename = os.path.basename(filepath)
        try:
            was_fixed, reason = fix_file(filepath)
            if was_fixed:
                log.append(f"  FIXED: {filename} ({reason})")
                fixed += 1
            else:
                if reason != "single_block":
                    log.append(f"  SKIP: {filename} ({reason})")
                skipped += 1
        except Exception as e:
            log.append(f"  ERROR: {filename}: {e}")
            errors += 1

    log.append(f"\nDone! {fixed} fixed, {skipped} skipped, {errors} errors")

    with open(LOG_PATH, "w") as f:
        f.write("\n".join(log))

    for line in log[-10:]:
        print(line)
    print(f"\nFull log: {LOG_PATH}")


if __name__ == "__main__":
    main()
