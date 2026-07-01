#!/usr/bin/env python3
"""Check files with no user turns."""
import sys
sys.path.insert(0, '/mnt/c/Users/toastedmel0n/Obsidian/Tw1n/_meta/scripts')
from fix_gpt_enrichment import *
import glob, os

VAULT = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
files = sorted(glob.glob(os.path.join(VAULT, "processed/GPT/*.md")))

no_user = 0
has_user = 0
for f in files:
    with open(f) as fh:
        content = fh.read()
    user_turns = extract_user_turns(content)
    if not user_turns.strip():
        no_user += 1
        if no_user <= 5:
            print(f"No user turns: {os.path.basename(f)}")
    else:
        has_user += 1

print(f"\nTotal: {len(files)}, has user turns: {has_user}, no user turns: {no_user}")
