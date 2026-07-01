---
id: 528118
source: GEMINI
date: 2026-02-19
tags: ['lutris', 'which', 'binary-path', 'cachyos', 'terminal']
category: homelab
sentiment: exploratory
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was verifying the installed location of the Lutris binary on CachyOS.
---
# ❯ which lutris
/usr/bin/lutris

~
❯ 

### USER
❯ which lutris
/usr/bin/lutris

~
❯ 

### GEMINI
The binary exists, the desktop file is valid, and there are no "hide" flags. Since you're on CachyOS (KDE Plasma), this is officially a Menu Indexing failure or a Categorization conflict. Your search tool (KRunner) works because it scans the filesystem directly. Your Application Launcher (the "Start" menu) is failing because its internal database is ignoring the entry. Stop playing defense and force the menu to see it. Follow this sequence exactly: 1. The Manual Menu Audit (The Most Likely Culprit) KDE has a habit of "disabling" entries in the GUI without touching the .desktop file. Run kmenuedit in your terminal. Expand the Games category in the left sidebar. Look for Lutris. If it's there but the text is greyed out: It is manually disabled. Check the box and click Save (top left). If it's NOT there: Look in the "Lost & Found" or "Other" categories at the bottom of the list. 2. The "Nuclear" Cache Purge Your local user cache is likely stuck on an old version of the menu state. Wipe the cache files that Plasma uses to build the app list: rm ~/.cache/ksycoca6* rm ~/.cache/plasma_theme_cache_* kbuildsycoca6 --noincremental Note: Your screen might flicker for a second; that’s normal. 3. The Symlink Power Move If it still won't show up, force a local copy of the desktop file. Sometimes the system-wide folder (/usr/share/applications) gets its permissions or indexing wonky on Arch-based distros like Cachy. cp /usr/share/applications/net.lutris.Lutris.desktop ~/.local/share/applications/ update-desktop-database ~/.local/share/applications Now check your menu again. The Reality Check If you do all three and it still doesn't show up in the menu but does show up in search: Are you using a custom Application Launcher widget? (e.g., "Minimalist Menu" or "Tiled Menu"?) Some third-party widgets have their own internal filters or bugs. Switch back to the "Application Launcher" (default) to test. Go run kmenuedit now—did you find Lutris sitting in a different category or unchecked?
