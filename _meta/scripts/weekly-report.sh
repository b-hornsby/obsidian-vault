#!/usr/bin/env bash
set -euo pipefail

VAULT="/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
INSIGHTS="$VAULT/insights"
WEEKLY_DIR="$INSIGHTS/weekly-report"
DAILY_DIR="$INSIGHTS/daily-notes"
GOALS_DIR="$INSIGHTS/goals"
DASHBOARD="$VAULT/Active-Dashboard.md"

TODAY="$(date +%F)"
REPORT="$WEEKLY_DIR/$TODAY-weekly.md"

mkdir -p "$WEEKLY_DIR" "$DAILY_DIR" "$GOALS_DIR"

# Try to discover last weekly report by mtime under weekly-report/.
LAST_WEEKLY="$(find "$WEEKLY_DIR" -maxdepth 1 -type f -name '*-weekly.md' -printf '%T@ %p\n' 2>/dev/null | sort -nr | head -n1 | awk '{print $2}' || true)"
LAST_WEEKLY="${LAST_WEEKLY:-none}"

# Latest daily note by mtime.
LAST_DAILY="$(find "$DAILY_DIR" -maxdepth 1 -type f \( -name '*.md' -o -name '[0-9]*' \) -printf '%T@ %p\n' 2>/dev/null | sort -nr | head -n1 | awk '{print $2}' || true)"
LAST_DAILY="${LAST_DAILY:-none}"
LAST_DAILY_DATE="$(basename "$LAST_DAILY" .md)"
LAST_DAILY_DATE="${LAST_DAILY_DATE:-unknown}"

# Latest goals file by mtime.
LAST_GOALS="$(find "$GOALS_DIR" -maxdepth 1 -type f -name '*.md' -printf '%T@ %p\n' 2>/dev/null | sort -nr | head -n1 | awk '{print $2}' || true)"
LAST_GOALS="${LAST_GOALS:-none}"

cat > "$REPORT" <<EOF
---
type: weekly-report
period: weekly
created_at: $(date -u +%Y-%m-%dT%H:%M:%SZ)
---

# Weekly Report — $TODAY

This is an auto-generated minimum viable weekly report. No manual review required.

## Goto-Forward

- Last weekly report: $LAST_WEEKLY
- Last daily note: $LAST_DAILY_DATE ($LAST_DAILY)
- Last goals update: $LAST_GOALS
- Dashboard review: see [[Active-Dashboard.md]]

## Notes

- Cron restored on $TODAY. If this file exists and the timestamp is current, the weekly automation is live.
- Review goals in [[insights/goals/goals-overall|Goals Overview]].
- If cadence stalls for more than 2 weeks, investigate `_meta/scripts/weekly-report.sh` and active scheduler entries.
EOF

echo "Wrote $REPORT"
