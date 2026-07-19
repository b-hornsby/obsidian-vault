#!/usr/bin/env bash
set -euo pipefail

APP_JSON="$VAULT/.obsidian/app.json"
if [ ! -f "$APP_JSON" ]; then
  echo "Missing $APP_JSON — nothing to sync."
  exit 1
fi

# Run in WSL Linux path context
VAULT="/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
APP_JSON="$VAULT/.obsidian/app.json"

tmp="$(mktemp)"

# Known corrections:
# - typo "Attatchments" -> "Attachments"
# - Notes/Insights folder path should mirror vault layout
sed -e 's/Attatchments/Attachments/g' "$APP_JSON" > "$tmp"

diff -u "$APP_JSON" "$tmp" || true

read -r -p "Apply these changes to $APP_JSON? [y/N] " ans
if [ "${ans:-N}" = "y" ] || [ "${ans:-N}" = "Y" ]; then
  cp "$tmp" "$APP_JSON"
  echo "Updated $APP_JSON"
else
  echo "No changes applied."
fi

rm -f "$tmp"
