#!/usr/bin/env python3
"""
fix_duplicate_frontmatter.py -- Fix files with duplicate frontmatter blocks.
The enrichment script's write function didn't always strip the old frontmatter properly.
This script keeps only the first frontmatter block and removes duplicates.
"""

import os
import re
import glob

VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
PROCESSED_DIR = os.path.join(VAULT_PATH, "processed")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "fix-duplicate-frontmatter.log")


def fix_file(filepath):
    """Fix a file with duplicate frontmatter blocks."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all frontmatter blocks
    pattern = r'^---\s*\n(.*?)\n---'
    matches = list(re.finditer(pattern, content, re.DOTALL | re.MULTILINE))

    if len(matches) <= 1:
        return False  # No duplicates

    # Keep only the first frontmatter block
    first_fm = matches[0]
    # Remove everything from the second frontmatter onward
    # Find where the body starts (after the first ---)
    body_start = first_fm.end()
    # The body is everything after the first frontmatter block
    body = content[body_start:].strip()

    # Remove any remaining --- blocks from the body
    body = re.sub(r'^---\s*\n.*?\n---\s*\n?', '', body, flags=re.DOTALL | re.MULTILINE)

    # Reconstruct the file
    new_content = "---\n" + first_fm.group(1).strip() + "\n---\n" + body

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def main():
    log = []
    fixed = 0
    errors = 0

    files = sorted(glob.glob(os.path.join(PROCESSED_DIR, "**", "*.md"), recursive=True))
    files = [f for f in files if "CONVERSATION-HUB" not in f]

    log.append(f"Scanning {len(files)} files for duplicate frontmatter...")

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
