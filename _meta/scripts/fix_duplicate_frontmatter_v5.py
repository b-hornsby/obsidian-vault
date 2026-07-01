#!/usr/bin/env python3
"""
fix_duplicate_frontmatter_v5.py -- Nuclear option: remove ALL duplicate frontmatter.
Strategy: Find the last frontmatter block before the actual body (markdown # header or ### USER/ASSISTANT).
Keep only that one block.
"""

import os
import re
import glob

VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
PROCESSED_DIR = os.path.join(VAULT_PATH, "processed")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "fix-duplicate-frontmatter-v5.log")


def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the body start: first # header or ### USER/HUMAN/ASSISTANT/GEMINI/GPT/GROK
    body_pattern = r'(^|\n)(#+\s|###\s*(?:USER|HUMAN|ASSISTANT|GEMINI|GPT|GROK))'
    body_match = re.search(body_pattern, content)

    if not body_match:
        return False  # Can't find body, skip

    body_start = body_match.start()
    if body_start == 0:
        body_start = body_match.end() - 1  # Skip the newline before #

    # Everything before the body is frontmatter blocks
    before_body = content[:body_start]

    # Count how many --- blocks are in before_body
    fm_count = before_body.count('---')

    if fm_count <= 2:
        return False  # Only one frontmatter block (normal)

    # Find the LAST complete frontmatter block before the body
    # Work backwards from body_start
    last_fm_start = before_body.rfind('---')
    if last_fm_start == -1:
        return False

    # Find the --- that starts this last block
    # Look for ---\n before last_fm_start
    prev_dash = before_body.rfind('---', 0, last_fm_start)
    if prev_dash == -1:
        prev_dash = 0

    # The last frontmatter block
    last_fm = before_body[prev_dash:].strip()

    # The body
    body = content[body_start:].strip()

    # Reconstruct
    new_content = last_fm + "\n" + body

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
