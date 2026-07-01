#!/usr/bin/env python3
"""
fix_duplicate_frontmatter_v3.py -- Fix duplicate frontmatter blocks.
The issue: some files have ---\n(fm1)\n---\n---\n(fm2)\n--- where the closing --- of block 1
is immediately followed by opening --- of block 2.
"""

import os
import re
import glob

VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
PROCESSED_DIR = os.path.join(VAULT_PATH, "processed")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "fix-duplicate-frontmatter-v3.log")


def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all frontmatter block positions
    # Match: ---\n...\n--- (non-greedy)
    pattern = r'^---\s*\n(.*?)\n---'
    matches = list(re.finditer(pattern, content, re.DOTALL | re.MULTILINE))

    if len(matches) <= 1:
        return False

    # Keep the first block, remove everything from the second block onward
    first_end = matches[0].end()
    second_start = matches[1].start()

    # The body is everything after the first frontmatter block
    # But we need to remove the duplicate frontmatter from the body
    body = content[first_end:]

    # Remove all subsequent frontmatter blocks from body
    body = re.sub(r'\n?---\s*\n.*?\n---', '', body, flags=re.DOTALL)

    # Also handle case where --- immediately follows (no newline)
    body = re.sub(r'---\s*\n.*?\n---', '', body, flags=re.DOTALL)

    body = body.strip()

    new_content = content[:first_end].rstrip() + "\n" + body

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
