#!/usr/bin/env python3
"""Scan processed/ folder and output a markdown summary of recent conversations.

Reads markdown files from processed/ subfolders (CLAUDE/, GEMINI/, GPT/, GROK/),
extracts date from filenames matching YYYY-MM-DD format, and writes a sorted
table to insights/recent-conversations.md.
"""

import os
import re
import sys
from pathlib import Path

VAULT_ROOT = Path(os.environ.get("VAULT_ROOT", "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"))
PROCESSED_DIR = VAULT_ROOT / "processed"
OUTPUT_DIR = VAULT_ROOT / "insights"
OUTPUT_FILE = OUTPUT_DIR / "recent-conversations.md"

# Regex to match YYYY-MM-DD in a filename (before .md extension)
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def scan_files():
    """Walk all provider subfolders and collect file info."""
    entries = []

    if not PROCESSED_DIR.is_dir():
        print(f"Error: {PROCESSED_DIR} does not exist.", file=sys.stderr)
        sys.exit(1)

    for provider_folder in sorted(PROCESSED_DIR.iterdir()):
        if not provider_folder.is_dir():
            continue
        provider = provider_folder.name  # CLAUDE, GEMINI, GPT, GROK

        for md_file in provider_folder.iterdir():
            if not md_file.suffix == ".md":
                continue

            # Extract date from filename
            stem = md_file.stem  # filename without .md
            date_match = DATE_RE.search(stem)
            date_str = date_match.group(1) if date_match else None

            # File size as approximate word count (roughly 1 word per 5 chars)
            size_bytes = md_file.stat().st_size if md_file.stat().st_size is not None else 0
            word_count = max(1, size_bytes // 5) if size_bytes > 0 else 0

            entries.append({
                "date": date_str,
                "provider": provider,
                "filename": md_file.name,
                "word_count": word_count,
                "sort_key": date_str if date_str else "9999-99-99",
            })

    return entries


def pick_top_50(entries):
    """Return the 50 most recent files by date descending."""
    # Sort: files with a date go first (descending), then dateless entries
    entries.sort(key=lambda e: e["sort_key"], reverse=True)
    return entries[:50]


def write_table(entries):
    """Write markdown table to output file."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    header = "| Date | Provider | Filename | Word Count |\n|---|---|---|---|"

    lines = []
    for e in entries:
        date_col = e["date"] if e["date"] else "N/A"
        # Make filename a wikilink
        filename_link = f"[{e['filename']}]({e['filename'].replace(' ', '%20')})"
        lines.append(f"| {date_col} | {e['provider']} | {filename_link} | {e['word_count']:,} |")

    table_body = "\n".join(lines)
    content = f"""# Recent Conversations

Summary of the 50 most recent processed conversations, sorted by date (newest first).

{header}
{table_body}
"""

    OUTPUT_FILE.write_text(content)
    print(f"Wrote {len(entries)} entries to {OUTPUT_FILE}")


def main():
    entries = scan_files()
    print(f"Found {len(entries)} markdown files across {PROCESSED_DIR.name}/")
    top = pick_top_50(entries)
    write_table(top)


if __name__ == "__main__":
    main()
