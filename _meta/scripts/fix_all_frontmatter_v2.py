#!/usr/bin/env python3
"""
fix_all_frontmatter_v2.py -- Nuclear option using regex to find all FM blocks.
"""

import os
import re
import glob
import yaml

VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
PROCESSED_DIR = os.path.join(VAULT_PATH, "processed")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "fix-all-frontmatter-v2.log")


def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find body start
    body_match = re.search(r'(?:^|\n)(#+\s|###\s*(?:USER|HUMAN|ASSISTANT|GEMINI|GPT|GROK))', content)
    if not body_match:
        return False, "no_body"

    body_start = body_match.start()
    if content[body_start] == '\n':
        body_start += 1

    before_body = content[:body_start]
    body = content[body_start:].strip()

    # Find ALL frontmatter blocks in before_body
    # Pattern: ---\n(content)\n---
    fm_pattern = r'---\s*\n(.*?)\n---'
    matches = list(re.finditer(fm_pattern, before_body, re.DOTALL))

    if len(matches) <= 1:
        return False, "single_block"

    # Parse all blocks
    blocks = []
    for m in matches:
        try:
            fm = yaml.safe_load(m.group(1))
            if fm:
                blocks.append(fm)
        except yaml.YAMLError:
            pass

    if not blocks:
        return False, "no_valid_fm"

    # Choose best: prefer block with 'summary'
    best = None
    for b in blocks:
        if 'summary' in b:
            best = b
            break
    if best is None:
        best = blocks[0]

    # Reconstruct
    yaml_str = yaml.dump(best, default_flow_style=False, allow_unicode=True).strip()
    new_content = "---\n" + yaml_str + "\n---\n" + body

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
                if reason not in ("single_block",):
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
