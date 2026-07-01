#!/usr/bin/env python3
"""Spot-check specific category changes."""
import sys
sys.path.insert(0, '/mnt/c/Users/toastedmel0n/Obsidian/Tw1n/_meta/scripts')

import importlib
import fix_gpt_enrichment
importlib.reload(fix_gpt_enrichment)

from fix_gpt_enrichment import *
import glob, os

VAULT = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
files = sorted(glob.glob(os.path.join(VAULT, "processed/GPT/*.md")))

check_transitions = [
    ("career", "crypto-web3"),
    ("crypto-web3", "general"),
    ("streaming", "general"),
    ("homelab", "general"),
    ("coding", "crypto-web3"),
]

for f in files:
    filename = os.path.basename(f)
    with open(f, 'r') as fh:
        content = fh.read()
    old_fm, body = parse_frontmatter(content)
    if not old_fm:
        continue
    old_cat = old_fm.get("category", "")
    user_turns = extract_user_turns(content)
    if not user_turns.strip():
        continue
    title = filename.replace('.md', '').replace('_', ' ')
    new_cat, conf = classify_category(title, user_turns)

    for from_cat, to_cat in check_transitions:
        if old_cat == from_cat and new_cat == to_cat:
            print(f"{filename}")
            print(f"  {old_cat} -> {new_cat} ({conf})")
            print(f"  User: {user_turns[:200]}")
            print()
            break
