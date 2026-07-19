# PC Dashboard Session Recap — 2026-06-27

## Work completed
- Scrub sensitive scripts from git history
  - Removed from every commit: `wazuh-ntfy-formatted.py`, `injection-alert-relay.py`, `injection-alert-relay.sh`
  - Used `git filter-repo` on a fresh clone and force-pushed rewritten `master`
- Clean up runtime files
  - Untracked: `alerts.json`, `data.json`, `update-data.log`, `alerts.json.bak`, `nul`
  - Added exact ignore rules to `.gitignore`
- Added repo docs
  - `README.md` — grounded overview, how to run, caveats, hygiene note
  - `about.md` — goals, non-goals, file inventory, data flow summary

## Repo state at end of session
- Branch: `master`
- Latest: `230dd33 Add README and about`
- Working dir clean aside from ignored runtime cache files
- Verified: no sensitive scripts in tracking or history; `.gitignore` final

## Notes for next time
- If future runtime files re-appear as untracked, `.gitignore` already covers them.
- If this triggers GitHub security alerts from the old history, a GitHub support ticket is the fastest way to invalidate cached refs.


## Related
- [[MOC.md|Map of Content]]
- [[nodes/topics/tech/pc-security|PC Security]]
