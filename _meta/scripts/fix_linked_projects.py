#!/usr/bin/env python3
"""
Fix linked_projects across all enriched files that are missing project references.

Reads each enriched file's content and existing frontmatter, searches for project
name mentions in the conversation text, and adds missing project references.
"""

import os
import re
import glob
import logging
from datetime import datetime

VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
PROCESSED_DIR = os.path.join(VAULT_PATH, "processed")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "enrichment-projects-fix.log")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH, mode="w"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger(__name__)

# Project detection rules: project_id -> list of (pattern, required_context)
# Patterns are matched case-insensitive. For common words like "vault" or "streaming",
# we require additional context to avoid false positives.
PROJECT_RULES = {
    "operation-immortal-agent": [
        # Direct references
        r"\boperation\s*immortal\s*agent\b",
        r"\bimmortal\s*agent\b",
        r"\bOIA\b",
        # Solana trading / fund manager references
        r"\bjupiter\s*perp",
        r"\bperp[s]?\b.*\b(trad|fund|solana)",
        r"\bsolana\b.*\b(trad|fund|agent|perp)",
        r"\bfund\s*manager\b.*\b(solana|crypto|agent)",
        r"\bmemecoin\b.*\b(fund|trad|agent)",
        r"\bdefi\b.*\b(agent|fund|trad)",
    ],
    "homelab-stack": [
        r"\bhomelab\b",
        r"\bhome\s*lab\b",
        r"\bproxmox\b",
        r"\bplex\b.*\b(server|media)",
        r"\bmedia\s*server\b",
        r"\bNAS\b",
        r"\bunraid\b",
        r"\bdocker\b.*\b(server|host|lab)",
        r"\bvm[s]?\b.*\b(server|host|lab)",
        r"\bvirtual\s*machin",
        r"\bpi[\s-]?hole\b",
        r"\bnetwork\s*attached\b",
    ],
    "private-ai-consulting": [
        r"\bprivate\s*AI\s*consult",
        r"\bAI\s*consult",
        r"\bconsulting\b.*\b(AI|machine\s*learning|LLM|tech)",
        r"\bAI\s*business\b",
        r"\bAI\s*service\b",
        r"\bconsultant\b.*\b(AI|tech|LLM)",
    ],
    "second-brain-vault": [
        # "vault" alone is too common; require Obsidian/second-brain context
        r"\bobsidian\b.*\bvault\b",
        r"\bvault\b.*\bobsidian\b",
        r"\bsecond\s*brain\b",
        r"\bknowledge\s*base\b.*\b(obsidian|vault|personal)",
        r"\bpersonal\s*knowledge\b",
        r"\bPKM\b",
        r"\bnote[\s-]*taking\b.*\b(system|obsidian|vault)",
        r"\bzettelkasten\b",
    ],
    "streaming-rig": [
        r"\bstreaming\s*rig\b",
        r"\bstream\b.*\b(setup|rig|PC|pc|hardware)",
        r"\bOBS\b",
        r"\bopen\s*broadcaster\b",
        r"\bstreaming\b.*\b(software|hardware|setup|equipment)",
        r"\bTwitch\b.*\b(setup|stream|broadcast)",
        r"\bYouTube\b.*\b(stream|broadcast|live)",
    ],
    "it-certification": [
        r"\bIT\s*certif",
        r"\bcertif\b.*\b(IT|CompTIA|AWS|Azure|Google|cloud)",
        r"\bCompTIA\b",
        r"\bSecurity\+\b",
        r"\bSecurity\s+Plus\b",
        r"\bNetwork\+\b",
        r"\bAWS\s*(cert|Solutions|Cloud)",
        r"\bAzure\s*cert",
        r"\bcertification\b.*\b(exam|study|prep|test)",
        r"\bstudying\b.*\b(certif|exam)",
        r"\bcert\b.*\b(exam|prep|study)",
    ],
    "flappy-meme-bird": [
        r"\bflappy\s*meme\s*bird\b",
        r"\bflappy\s*bird\b",
        r"\bflappy\b.*\b(game|meme|bird)",
    ],
}


def parse_frontmatter(content: str) -> tuple[dict | None, str]:
    """Parse YAML frontmatter from markdown content. Returns (frontmatter_dict, body)."""
    if not content.startswith("---"):
        return None, content

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return None, content

    fm_text = match.group(1)
    body = content[match.end() :]

    # Simple YAML parser for flat key-value pairs
    fm = {}
    for line in fm_text.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()

        # Parse list values like ['item1', 'item2']
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            if not inner:
                fm[key] = []
            else:
                items = re.findall(r"'([^']*)'", inner)
                fm[key] = items
        else:
            fm[key] = val

    return fm, body


def build_frontmatter(fm: dict) -> str:
    """Rebuild YAML frontmatter string from dict."""
    lines = ["---"]
    for key, val in fm.items():
        if isinstance(val, list):
            if not val:
                lines.append(f"{key}: []")
            else:
                items = ", ".join(f"'{v}'" for v in val)
                lines.append(f"{key}: [{items}]")
        else:
            lines.append(f"{key}: {val}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def detect_projects(body: str) -> list[str]:
    """Detect which projects are mentioned in the body text."""
    body_lower = body.lower()
    detected = []

    for project_id, patterns in PROJECT_RULES.items():
        for pattern in patterns:
            if re.search(pattern, body_lower, re.IGNORECASE):
                detected.append(project_id)
                break  # One match per project is enough

    return detected


def process_file(filepath: str) -> dict:
    """Process a single file. Returns info about changes made."""
    result = {"file": filepath, "changes": [], "errors": []}

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        result["errors"].append(f"Read error: {e}")
        return result

    fm, body = parse_frontmatter(content)
    if fm is None:
        result["errors"].append("No frontmatter found")
        return result

    existing = set(fm.get("linked_projects", []))
    if not isinstance(existing, list):
        existing = []

    detected = set(detect_projects(body))
    missing = detected - set(existing)

    if missing:
        new_projects = list(set(existing) | missing)
        # Sort for consistency
        new_projects.sort()
        fm["linked_projects"] = new_projects

        # Rebuild file
        new_fm_str = build_frontmatter(fm)
        new_content = new_fm_str + body

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            result["changes"] = sorted(missing)
            log.info(
                f"UPDATED: {os.path.basename(filepath)} -> added {sorted(missing)}"
            )
        except Exception as e:
            result["errors"].append(f"Write error: {e}")
    else:
        log.debug(f"SKIP: {os.path.basename(filepath)} (no changes needed)")

    return result


def main():
    log.info("=" * 60)
    log.info("Starting linked_projects fix")
    log.info(f"Processed dir: {PROCESSED_DIR}")
    log.info("=" * 60)

    # Find all markdown files in processed directory
    pattern = os.path.join(PROCESSED_DIR, "**", "*.md")
    files = sorted(glob.glob(pattern, recursive=True))

    log.info(f"Found {len(files)} markdown files to process")

    total_updated = 0
    total_unchanged = 0
    total_errors = 0
    project_additions = {}

    for i, filepath in enumerate(files):
        if i % 500 == 0 and i > 0:
            log.info(f"Progress: {i}/{len(files)} files processed...")

        result = process_file(filepath)

        if result["errors"]:
            total_errors += 1
            log.error(f"ERROR in {filepath}: {result['errors']}")
        elif result["changes"]:
            total_updated += 1
            for proj in result["changes"]:
                project_additions[proj] = project_additions.get(proj, 0) + 1
        else:
            total_unchanged += 1

    log.info("=" * 60)
    log.info("SUMMARY")
    log.info(f"  Total files:     {len(files)}")
    log.info(f"  Updated:         {total_updated}")
    log.info(f"  Unchanged:       {total_unchanged}")
    log.info(f"  Errors:          {total_errors}")
    log.info("")
    log.info("Projects added:")
    for proj, count in sorted(project_additions.items()):
        log.info(f"  {proj}: {count} files")
    log.info("=" * 60)


if __name__ == "__main__":
    main()
