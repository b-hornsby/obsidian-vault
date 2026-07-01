#!/usr/bin/env python3
"""Quick test of the enrichment fix logic on 20 sample files."""
import sys
sys.path.insert(0, '/mnt/c/Users/toastedmel0n/Obsidian/Tw1n/_meta/scripts')
from fix_gpt_enrichment import *
import glob, os

VAULT = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
files = sorted(glob.glob(os.path.join(VAULT, "processed/GPT/*.md")))[:20]

for f in files:
    filename = os.path.basename(f)
    with open(f) as fh:
        content = fh.read()
    old_fm, body = parse_frontmatter(content)
    if not old_fm:
        print(f"{filename}: NO FRONTMATTER")
        continue
    user_turns = extract_user_turns(content)
    title = filename.replace('.md', '').replace('_', ' ')
    cat, conf = classify_category(title, user_turns)
    tags = generate_tags(title, user_turns, cat)
    projects = detect_projects(user_turns)
    old_cat = old_fm.get('category', '?')
    old_tags = old_fm.get('tags', [])
    old_proj = old_fm.get('linked_projects', [])
    marker = ' *** CHANGED' if old_cat != cat else ''
    print(f"{filename}")
    print(f"  {old_cat} -> {cat} ({conf}){marker}")
    print(f"  tags: {old_tags}")
    print(f"    -> {tags}")
    print(f"  proj: {old_proj} -> {projects}")
    print()
