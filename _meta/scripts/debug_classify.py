#!/usr/bin/env python3
"""Debug the Internet Technician classification."""
import sys
sys.path.insert(0, '/mnt/c/Users/toastedmel0n/Obsidian/Tw1n/_meta/scripts')

import importlib
import fix_gpt_enrichment
importlib.reload(fix_gpt_enrichment)

from fix_gpt_enrichment import classify_category, extract_user_turns, ALL_CATEGORY_KEYWORDS, STREAMING_KEYWORDS, CAREER_KEYWORDS
from fix_gpt_enrichment import _keyword_matches

filepath = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n/processed/GPT/2024-03-18_Internet_Technician_Installer_66949181.md"
with open(filepath) as f:
    content = f.read()

user_turns = extract_user_turns(content)
title = "Internet Technician Installer"
text = (title + " " + user_turns).lower()

print("Text:", repr(text[:200]))
print()

for kw, weight in STREAMING_KEYWORDS:
    if _keyword_matches(kw, text):
        print(f"  STREAMING match: '{kw}' (weight {weight})")

for kw, weight in CAREER_KEYWORDS:
    if _keyword_matches(kw, text):
        print(f"  CAREER match: '{kw}' (weight {weight})")

cat, conf = classify_category(title, user_turns)
print(f"\nResult: {cat} ({conf})")
