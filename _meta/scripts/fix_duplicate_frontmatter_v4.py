#!/usr/bin/env python3
"""
fix_duplicate_frontmatter_v4.py -- Fix duplicate frontmatter blocks.
Split on --- delimiters, keep only the first block + body text.
"""

import os
import re
import glob

VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
PROCESSED_DIR = os.path.join(VAULT_PATH, "processed")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "fix-duplicate-frontmatter-v4.log")


def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split on --- lines
    parts = re.split(r'\n---\n', content)

    # parts[0] is the first line "---"
    # parts[1] is the first frontmatter content
    # parts[2] is either the body OR the second frontmatter content
    # We need to find where the actual body starts

    if len(parts) <= 2:
        return False  # Only one frontmatter block

    # The first frontmatter block is parts[0] + "---\n" + parts[1] + "\n---"
    first_fm_content = parts[1].strip()

    # Everything after the first frontmatter block
    remaining = "\n---\n".join(parts[2:])

    # Remove any subsequent frontmatter blocks from remaining
    # A frontmatter block looks like: key: value\nkey: value\n...
    # The body starts with # (markdown header) or ### (conversation turn)
    # Find the first # or ### that's not inside frontmatter
    body_match = re.search(r'\n(#+\s|###\s*(?:USER|HUMAN|ASSISTANT|GEMINI|GPT|GROK))', remaining)
    if body_match:
        body = remaining[body_match.start():].lstrip('\n')
    else:
        # Fallback: just use everything after the second ---
        body = remaining

    # Reconstruct
    new_content = "---\n" + first_fm_content + "\n---\n" + body

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def main():
    log = []
    fixed = 0
    errors = 0

    files = sorted(glob.glob(os.path.join(PROCESSED_DIR, "**", "*.md"), recursive=True))
    files = [f for f in files if "CONVERSATION-HUB" not in f]

    log.append(f"Scanning {len(files)} files...")

    for filepath in files:
        filename = os.path.basename(filepath)
        try:
            if fix_file(filepath):
                log.append(f"  FIXED: {filename}")
                fixed += 1
        except Exception as e:
            log.append(f"  ERROR: {filename}: {e}")
            errors += 1

    log.append(f"\nDone! {fixed} files fixed, {errors} errors")

    with open(LOG_PATH, "w") as f:
        f.write("\n".join(log))

    for line in log[-5:]:
        print(line)
    print(f"\nFull log: {LOG_PATH}")


if __name__ == "__main__":
    main()
