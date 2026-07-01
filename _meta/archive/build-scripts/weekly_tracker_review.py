#!/usr/bin/env python3
"""
weekly_tracker_review.py
Runs every Sunday evening (or manually) to:
  1. Scan q2-2026-action-tracker.md
  2. Look for signals of progress in vault work directories (excluding rebuild artifacts)
  3. Auto-update Status where signal detected
  4. Flag slipping / past-due items
  5. Write timestamped summary to tracker + update Active-Dashboard.md

Safety rules:
  - Ignore files modified only during the rebuild window (Apr 29 14:00-16:00)
  - Prefer frontmatter date over filesystem mtime
  - Never auto-mark Done; only promote Not Started -> In Progress
  - Never scan raw/, archive/, _meta/, or backup folders
"""

import hashlib
import os
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

VAULT = Path(os.environ.get("VAULT_ROOT", "/vault"))
TRACKER = VAULT / "insights" / "q2-2026-action-tracker.md"
DASHBOARD = VAULT / "Active-Dashboard.md"
LOG_DIR = VAULT / "_meta" / "weekly_review_logs"
HASH_STORE = VAULT / "_meta" / ".weekly_tracker_hashes.json"

# Days back to scan for activity fallback
LOOKBACK_DAYS = 7

# Known rebuild window — anything touched ONLY in this window is suspect
REBUILD_START = datetime(2026, 4, 29, 14, 0, 0)
REBUILD_END = datetime(2026, 4, 29, 16, 0, 0)

# Keyword crosswalk: action -> [signals]
SIGNAL_MAP = {
    "operation-immortal-agent": [
        "solana", "dlmm", "immortal", "bot", "trade", "phantom", "jupiter",
        "meteora", "raydium", "liquidity", "swap", "rust", "anchor"
    ],
    "ai-security-convergence": [
        "security+", "security plus", "comptia security", "cybersecurity",
        "ai security", "security ai"
    ],
    "private-ai-consulting": [
        "consulting", "$500", "package", "clinic", "dentist", "private ai",
        "prospect", "pitch", "client", "invoice", "small business"
    ],
    "it-certification": [
        "comptia", "a+", "network+", "network plus", "certification",
        "exam", "study", "anki", "practice test", "test date", "sec+"
    ],
    "homelab-stack": [
        "demo", "screenshot", "screencast", "homelab", "self-host",
        "proxmox", "docker", "kubernetes", "k3s", "ansible", "terraform",
        "open webui", "ollama", "local ai"
    ],
    "streaming": [
        "youtube", "stream", "video", "content plan", "recording",
        "obs", "twitch"
    ],
    "blockchain-analysis": [
        "coinbase", "binance", "api", "exchange", "on-chain", "data analysis"
    ],
    "vault-meta": [
        "weekly review", "hermes", "check-in", "tracker"
    ],
}

EXCLUDED_NAMES = {
    "q2-2026-action-tracker.md",
    "concrete-action-plan-Q2-2026.md",
    "goal-alignment-2026-Q2.md",
    "active-dashboard.md",
}

SCAN_DIRS = [
    VAULT / "processed",
    VAULT / "nodes",
    VAULT / "insights",
    VAULT / "goals",
]

EXCLUDED_FRAGMENTS = ["/raw/", "/archive/", "_meta"]


# ─── Helpers ────────────────────────────────────────────────────────────────

def _now():
    return datetime.now()


def parse_frontmatter_date(text):
    """Extract created or updated timestamp from YAML frontmatter."""
    if not text.startswith("---"):
        return None
    try:
        fm_end = text.index("---", 3)
        fm = text[:fm_end]
    except ValueError:
        return None
    for key in ("updated", "created", "date", "modified"):
        m = re.search(rf"^{key}\s*:\s*(.+)$", fm, re.IGNORECASE | re.MULTILINE)
        if m:
            val = m.group(1).strip()
            for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%dT%H:%M", "%Y-%m-%d"):
                try:
                    return datetime.strptime(val, fmt)
                except ValueError:
                    continue
    return None


def file_mtime(path):
    try:
        return datetime.fromtimestamp(path.stat().st_mtime)
    except Exception:
        return datetime.min


def is_rebuild_artifact(mtime):
    """Return True if file was modified only inside the known rebuild window."""
    return REBUILD_START <= mtime <= REBUILD_END


def content_hash(path):
    try:
        return hashlib.md5(path.read_bytes()).hexdigest()
    except Exception:
        return None


def load_hash_store():
    if not HASH_STORE.exists():
        return {}
    try:
        import json
        return json.loads(HASH_STORE.read_text())
    except Exception:
        return {}


def save_hash_store(store):
    HASH_STORE.parent.mkdir(parents=True, exist_ok=True)
    import json
    HASH_STORE.write_text(json.dumps(store, indent=2))


def is_excluded_path(path):
    s = str(path.resolve()).lower()
    return any(frag.lower() in s for frag in EXCLUDED_FRAGMENTS)


# ─── Scan logic ─────────────────────────────────────────────────────────────

def scan_for_genuine_activity(since):
    """
    Returns list of Path objects representing REAL USER WORK since `since`.
    Filters out:
      - Rebuild artifacts (mtime within Apr 29 14:00-16:00)
      - Files with no content change since last review
      - Files seen for the very first time (baseline capture)
    """
    candidates = []
    for directory in SCAN_DIRS:
        if not directory.exists():
            continue
        for root, _, files in os.walk(directory):
            for f in files:
                if not f.endswith(".md"):
                    continue
                if f.lower() in EXCLUDED_NAMES:
                    continue
                p = Path(root) / f
                if is_excluded_path(p):
                    continue
                candidates.append(p)

    previous_hashes = load_hash_store()
    genuine = []
    current_hashes = {}

    for p in candidates:
        mtime = file_mtime(p)
        # Quick reject: mtime too old
        if mtime < since and mtime != datetime.min:
            current_hashes[str(p.resolve())] = content_hash(p)
            continue

        h = content_hash(p)
        canonical = str(p.resolve())
        current_hashes[canonical] = h

        # First time seeing this file? Record baseline, don't treat as new.
        if canonical not in previous_hashes:
            continue

        # If hash unchanged since last review → no real work
        if previous_hashes.get(canonical) == h:
            continue

        # Hash changed! But was it a rebuild artifact?
        if is_rebuild_artifact(mtime):
            # Still exclude if mtime is ONLY in rebuild window and we have no other signal
            # For safety, we check frontmatter
            fm_date = parse_frontmatter_date(p.read_text(encoding="utf-8"))
            if fm_date:
                if fm_date < since:
                    continue
            else:
                continue  # rebuild window + no frontmater = skip

        genuine.append(p)

    save_hash_store(current_hashes)
    return genuine


def detect_signals(files):
    hits = {k: 0 for k in SIGNAL_MAP}
    for f in files:
        try:
            content = f.read_text(encoding="utf-8").lower()
        except Exception:
            continue
        for project, keywords in SIGNAL_MAP.items():
            for kw in keywords:
                if kw in content:
                    hits[project] += content.count(kw)
                    break
    return hits


# ─── Tracker parsing / updating ─────────────────────────────────────────────

def parse_tracker():
    text = TRACKER.read_text(encoding="utf-8")
    lines = text.splitlines()
    header, footer = [], []
    rows = []
    table_started = False
    sep_seen = False
    for line in lines:
        s = line.strip()
        if s.startswith("| Action #"):
            table_started = True
            continue
        if table_started and not sep_seen and re.match(r"^\|[\s\-|\:]+\|$", s):
            sep_seen = True
            continue
        if table_started and s.startswith("|"):
            parts = [p.strip() for p in s.split("|")
                     if p.strip()]  # drop empty edges
            if len(parts) == 7:
                rows.append(tuple(parts))
            continue
        if table_started and not s.startswith("|") and sep_seen:
            footer.append(line)
            continue
        if not table_started:
            header.append(line)
    return header, footer, rows


def update_status(rows, signals):
    updated = []
    changes = []
    for r in rows:
        action, project, desc, prio, due, status, notes = r
        new_status = status
        sig = signals.get(project.lower(), 0)

        # Only auto-promote Not Started -> In Progress
        if status.lower() == "not started" and sig > 0:
            new_status = "In Progress"
            changes.append(
                f"Action {action}: {project} → In Progress (signal: {sig})")

        updated.append((action, project, desc, prio, due, new_status, notes))
    return updated, changes


def build_tracker_text(header, footer, rows):
    lines = list(header)
    lines.append("| Action # | Project | Description | Priority | Due | Status | Notes |")
    lines.append(
        "|----------|---------|-------------|----------|-----|--------|-------|")
    for r in rows:
        lines.append(
            f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} |")
    lines.extend(footer)
    return "\n".join(lines) + "\n"


# ─── Dashboard update ───────────────────────────────────────────────────────

def update_dashboard(rows):
    if not DASHBOARD.exists():
        return
    text = DASHBOARD.read_text(encoding="utf-8")
    total = len(rows)
    p0_t = sum(1 for r in rows if r[3].upper() == "P0")
    p1_t = sum(1 for r in rows if r[3].upper() == "P1")
    p2_t = sum(1 for r in rows if r[3].upper() == "P2")
    p0_d = sum(1 for r in rows if r[3].upper() == "P0" and r[5].lower() == "done")
    p1_d = sum(1 for r in rows if r[3].upper() == "P1" and r[5].lower() == "done")
    p2_d = sum(1 for r in rows if r[3].upper() == "P2" and r[5].lower() == "done")

    new_block = (
        f"- **P0 Items:** {p0_d}/{p0_t} done\n"
        f"- **P1 Items:** {p1_d}/{p1_t} done\n"
        f"- **P2 Items:** {p2_d}/{p2_t} done\n"
        f"- **Overall Progress:** {p0_d + p1_d + p2_d}/{total}"
    )
    old = re.search(
        r"(- \*\*P0 Items:\*\* .*\n- \*\*P1 Items:\*\* .*\n- \*\*P2 Items:\*\* .*\n- \*\*Overall Progress:\*\* .*)",
        text, re.DOTALL)
    if old:
        text = text.replace(old.group(1), new_block)
    else:
        text = text.replace("## Quick Status\n\n",
                            f"## Quick Status\n\n{new_block}\n")
    text = re.sub(
        r"\*\*Last Review:\*\* .*",
        f"**Last Review:** {_now().strftime('%Y-%m-%d %H:%M')}",
        text)
    DASHBOARD.write_text(text, encoding="utf-8")


# ─── Main ───────────────────────────────────────────────────────────────────

def main():
    since = _now() - timedelta(days=LOOKBACK_DAYS)

    files = scan_for_genuine_activity(since)
    signals = detect_signals(files)

    header, footer, rows = parse_tracker()
    updated_rows, changes = update_status(rows, signals)

    # Build summary block
    summary = ["---", f"## Weekly Review — {_now().strftime('%Y-%m-%d %H:%M')}", "", "### This Week"]
    if changes:
        summary.append("**Auto-detected changes:**")
        for c in changes:
            summary.append(f"- {c}")
    else:
        summary.append("No auto-detected status changes this week.")

    # Flag blocked / slipping
    blocked = [r for r in updated_rows if r[5].lower() == "blocked"]
    if blocked:
        summary.append("\n**Flagged as blocked:**")
        for r in blocked:
            summary.append(f"- Action {r[0]} ({r[1]}): {r[2]}")

    p0_nst = [r for r in updated_rows if r[3].upper() == "P0"
              and r[5].lower() == "not started"]
    if p0_nst:
        summary.append("\n**P0 items still not started:**")
        for r in p0_nst:
            summary.append(f"- Action {r[0]}: {r[1]} — {r[2]}")

    clean_footer = []
    for line in footer:
        if line.startswith("## Weekly Review"):
            break
        clean_footer.append(line)

    output = build_tracker_text(header, clean_footer, updated_rows)
    TRACKER.write_text(output + "\n".join(summary) + "\n", encoding="utf-8")
    update_dashboard(updated_rows)

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / f"weekly_review_{_now().strftime('%Y%m%d_%H%M')}.md"
    log_path.write_text("\n".join(summary) + "\n", encoding="utf-8")

    print("Weekly review complete.")
    print(f"Genuine files scanned: {len(files)}")
    print(f"Status changes: {len(changes)}")
    print(f"Blocked: {len(blocked)}")
    print(f"Log: {log_path}")


if __name__ == "__main__":
    main()
