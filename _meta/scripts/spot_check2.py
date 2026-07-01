#!/usr/bin/env python3
"""Check specific files that might be misclassified."""
import sys
sys.path.insert(0, '/mnt/c/Users/toastedmel0n/Obsidian/Tw1n/_meta/scripts')

import importlib
import fix_gpt_enrichment
importlib.reload(fix_gpt_enrichment)

from fix_gpt_enrichment import *
import os

check_files = [
    # crypto-web3 -> general (should these stay crypto?)
    "2025-03-05_Coinbase_Wallet_XRP_Support_65463562.md",
    "2025-03-28_Best_XRP_Hot_Wallets_45495100.md",
    "2025-03-28_XRP_Wallet_Options_70265643.md",
    "2025-01-09_146_SOL_to_USD_58858547.md",
    # homelab -> general (should these stay homelab/career?)
    "2025-02-21_Explain_request_summary_58677744.md",
    "2025-03-06_Rib_cracking_explanation_42165405.md",
    # streaming -> general
    "2024-12-22_Weed_Themed_Banner_Request_92125664.md",
    "2024-12-29_Video_Creation_Assistance_87018827.md",
]

VAULT = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"

for fname in check_files:
    fpath = os.path.join(VAULT, "processed/GPT", fname)
    with open(fpath) as f:
        content = f.read()
    old_fm, body = parse_frontmatter(content)
    user_turns = extract_user_turns(content)
    title = fname.replace('.md', '').replace('_', ' ')
    cat, conf = classify_category(title, user_turns)
    tags = generate_tags(title, user_turns, cat)
    old_cat = old_fm.get('category', '?')

    print(f"{fname}")
    print(f"  {old_cat} -> {cat} ({conf})")
    print(f"  User: {user_turns[:300]}")
    print(f"  Tags: {tags}")
    print()
