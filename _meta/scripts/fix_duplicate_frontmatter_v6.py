#!/usr/bin/env python3
"""
fix_duplicate_frontmatter_v6.py -- Keep the FIRST frontmatter block, remove all duplicates.
The new enrichment (Phase 3) was written BEFORE the old enrichment (Phase 2).
So the first block is the one we want to keep.
"""

import os
import re
import glob

VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
PROCESSED_DIR = os.path.join(VAULT_PATH, "processed")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "fix-duplicate-frontmatter-v6.log")


def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the body start: first # header or ### USER/HUMAN/ASSISTANT/GEMINI/GPT/GROK
    body_pattern = r'(?:^|\n)(#+\s|###\s*(?:USER|HUMAN|ASSISTANT|GEMINI|GPT|GROK))'
    body_match = re.search(body_pattern, content)

    if not body_match:
        return False

    body_start = body_match.start()
    if content[body_start] == '\n':
        body_start += 1

    # Everything before the body
    before_body = content[:body_start]

    # Count --- blocks
    dashes = [m.start() for m in re.finditer(r'---', before_body)]

    if len(dashes) <= 2:
        return False  # Normal single frontmatter block

    # Keep only the first frontmatter block (chars 0 to dashes[1]+3)
    first_fm = content[:dashes[1] + 3].strip()

    # The body
    body = content[body_start:].strip()

    # Reconstruct
    new_content = first_fm + "\n" + body

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
