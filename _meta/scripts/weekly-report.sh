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

# Disambiguate current week ending using Friday anchor when possible.
NOW="$(date +%s)"
YEAR="$(date +%Y)"
WEEKDAY="$(date +%u)"
if [ "$WEEKDAY" -ge 5 ]; then
  DAYS_TO_FRIDAY=0
else
  DAYS_TO_FRIDAY=$((5 - WEEKDAY))
fi
WEEK_END="$(date -d "+$DAYS_TO_FRIDAY days" +%F 2>/dev/null || date -d "+$DAYS_TO_FRIDAY day" +%F)"
[ -z "$WEEK_END" ] && WEEK_END="$TODAY"

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
week_ending: "$WEEK_END"
generated: "$TODAY"
source_last_weekly: "$LAST_WEEKLY"
source_last_daily: "$LAST_DAILY"
source_last_daily_date: "$LAST_DAILY_DATE"
source_last_goals: "$LAST_GOALS"
dashboard: "$DASHBOARD"
---

# Weekly Report — $TODAY

> Auto-generated weekly summary skeleton. Fill in the sections below during weekly review.

## Goto-Forward

- Last weekly report: $LAST_WEEKLY
- Last daily note: $LAST_DAILY_DATE ($LAST_DAILY)
- Last goals update: $LAST_GOALS
- Dashboard review: see [[Active-Dashboard.md]]

## Week Ending

- \`$WEEK_END\`

## Top Projects

- [ ] Add project with highest completion This week:
- [ ] Add project with highest completion This week:
- [ ] Add project with highest completion This week:

## Decisions

- [ ] Add decisions made or deferred this week:
- [ ] Add decisions made or deferred this week:
- [ ] Add decisions made or deferred this week:

## Blockers

- [ ] Add blockers or dependencies blocking progress:
- [ ] Add blockers or dependencies blocking progress:
- [ ] Add blockers or dependencies blocking progress:

## Next Week Focus

- [ ] Add priority outcomes or deliverables:
- [ ] Add priority outcomes or deliverables:
- [ ] Add priority outcomes or deliverables:

## Links

- Last weekly report: \`$LAST_WEEKLY\`
- Last daily note: \`$LAST_DAILY_DATE\` (\`$LAST_DAILY\`)
- Last goals update: \`$LAST_GOALS\`
- Dashboard: \`$DASHBOARD\`

EOF

echo "Wrote $REPORT"
