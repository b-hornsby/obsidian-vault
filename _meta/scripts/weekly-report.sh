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

# Friday-anchored week ending
WEEKDAY="$(date +%u)"
if [ "$WEEKDAY" -ge 5 ]; then
  DAYS_TO_FRIDAY=0
else
  DAYS_TO_FRIDAY=$((5 - WEEKDAY))
fi
WEEK_END="$(date -d "+$DAYS_TO_FRIDAY days" +%F 2>/dev/null || date -d "+$DAYS_TO_FRIDAY day" +%F)"
[ -z "$WEEK_END" ] && WEEK_END="$TODAY"

# Last weekly report excluding today
LAST_WEEKLY="$(find "$WEEKLY_DIR" -maxdepth 1 -type f -name '*-weekly.md' ! -name "$TODAY-weekly.md" -printf '%T@ %p\n' 2>/dev/null | sort -nr | head -n1 | awk '{print $2}' || true)"
LAST_WEEKLY="${LAST_WEEKLY:-none}"
LAST_WEEKLY_BASENAME="$(basename "$LAST_WEEKLY" .md)"
[ "$LAST_WEEKLY_BASENAME" = "none" ] && LAST_WEEKLY_BASENAME="none"

# Latest daily note
LAST_DAILY="$(find "$DAILY_DIR" -maxdepth 1 -type f -name '*.md' -printf '%T@ %p\n' 2>/dev/null | sort -nr | head -n1 | awk '{print $2}' || true)"
LAST_DAILY="${LAST_DAILY:-none}"
LAST_DAILY_DATE="$(basename "$LAST_DAILY" .md)"
LAST_DAILY_DATE="${LAST_DAILY_DATE:-unknown}"

# Latest goals file
LAST_GOALS="$(find "$GOALS_DIR" -maxdepth 1 -type f -name '*.md' -printf '%T@ %p\n' 2>/dev/null | sort -nr | head -n1 | awk '{print $2}' || true)"
LAST_GOALS="${LAST_GOALS:-none}"
LAST_GOALS_BASENAME="$(basename "$LAST_GOALS" .md)"
[ "$LAST_GOALS_BASENAME" = "none" ] && LAST_GOALS_BASENAME="none"

cat > "$REPORT" <<EOF
---
type: weekly-report
period: weekly
created_at: $(date -u +%Y-%m-%dT%H:%M:%SZ)
week_ending: "$WEEK_END"
generated: "$TODAY"
source_last_weekly: "$LAST_WEEKLY"
source_last_daily: "$LAST_DAILY"
source_last_daily_date: "$LAST_DAILY_DATE"
source_last_goals: "$LAST_GOALS"
dashboard: "$DASHBOARD"
---

# Weekly Report — $TODAY

> Auto-generated weekly review skeleton. Complete each section during Sunday review.

## Week at a Glance

- Last weekly report: $LAST_WEEKLY
- Last daily note: $LAST_DAILY_DATE
- Goals context: $LAST_GOALS
- Dashboard: [[Active-Dashboard.md]]

## Top Projects

- [ ] Project / outcome with highest completion this week:
- [ ] Runner-up project / outcome:
- [ ] Under-performer that needs attention:

## Decisions

- [ ] Decisions made this week:
- [ ] Decisions deferred / parked:

## Blockers

- [ ] Active blockers / dependencies:
- [ ] External factors / distractions:

## Next Week Focus

- [ ] Top priority outcome:
- [ ] Second priority:

## Review Notes

- Anything to carry forward from last weekly:
EOF

echo "Wrote $REPORT"
