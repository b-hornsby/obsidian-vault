#!/usr/bin/env python3
"""
fix_duplicate_frontmatter_v2.py -- Properly fix ALL duplicate frontmatter blocks.
Keeps only the first frontmatter block, removes everything else that looks like frontmatter.
"""

import os
import re
import glob

VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
PROCESSED_DIR = os.path.join(VAULT_PATH, "processed")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "fix-duplicate-frontmatter-v2.log")


def fix_file(filepath):
    """Fix a file with duplicate frontmatter blocks."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split content by frontmatter delimiters
    # Pattern: ---\n...\n--- (possibly followed by more ---\n...\n---)
    parts = re.split(r'(^---\s*\n.*?\n---)', content, flags=re.DOTALL | re.MULTILINE)

    # Count frontmatter blocks
    fm_blocks = [p for p in parts if p.strip().startswith("---") and p.strip().endswith("---")]

    if len(fm_blocks) <= 1:
        return False  # No duplicates

    # Keep only the first frontmatter block
    first_fm = fm_blocks[0]

    # Find the body: everything after the first frontmatter block
    fm_end = content.find(first_fm) + len(first_fm)
    body = content[fm_end:]

    # Remove any remaining frontmatter blocks from the body
    body = re.sub(r'\n---\s*\n.*?\n---', '', body, flags=re.DOTALL)

    # Clean up leading whitespace
    body = body.strip()

    # Reconstruct
    new_content = first_fm.rstrip() + "\n" + body

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
