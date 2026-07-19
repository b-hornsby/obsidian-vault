#!/bin/bash
set -euo pipefail
VAULT="/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
SRC="$HOME/.hermes/memories"
DST="$VAULT/hermes-memories"
mkdir -p "$DST"

for f in MEMORY.md USER.md export-*.md; do
  [ -f "$SRC/$f" ] || continue
  cp -f "$SRC/$f" "$DST/$(basename "$f")"
done

cd "$VAULT"
git add -A
if git diff --cached --quiet; then
  echo "[memory-export] no changes"
else
  git commit -m "auto: export hermes memories to vault backup"
  git push origin master
  echo "[memory-export] committed and pushed"
fi
