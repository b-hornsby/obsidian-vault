---
id: 807393
source: GEMINI
date: 2026-02-19
tags: ['lutris', 'desktop-file', 'system-applications', 'cachyos', 'file-inspection']
category: homelab
sentiment: exploratory
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was verifying the existence and permissions of the system-level Lutris .desktop file.
---
# ❯ ls /usr/share/applications/net.lutris.Lutris.desktop
.rw-r--r-- 2.0k root  3 Feb 04:04  /usr/share/applications/net.lutris.Lutris.desktop

~
❯  

### USER
❯ ls /usr/share/applications/net.lutris.Lutris.desktop
.rw-r--r-- 2.0k root  3 Feb 04:04  /usr/share/applications/net.lutris.Lutris.desktop

~
❯  

### GEMINI
The file exists, which means the "Search" tool can see it, but your application menu is ignoring it. Since you're on CachyOS (likely running KDE Plasma or GNOME), there is a high probability of a metadata conflict or a NoDisplay flag hiding it from the grid. Stop guessing and look inside the file. 1. The Direct Audit Run this command to see if it’s intentionally hiding from you: grep -E "NoDisplay|Hidden|OnlyShowIn" /usr/share/applications/net.lutris.Lutris.desktop If you see NoDisplay=true: You found the culprit. The system is told to index it for search but hide the icon. If you see OnlyShowIn=GNOME (and you're on KDE): It’s being filtered out by desktop environment rules. 2. The Brutal Fix: Force the Refresh If the grep returns nothing, your application database is stale. CachyOS is fast, but sometimes the cache gets "lazy." Force a rebuild of the system configuration cache: # Force rebuild of the service configuration cache (KDE specific) kbuildsycoca6 --noincremental # Update the desktop database system-wide sudo update-desktop-database /usr/share/applications 3. The "CachyOS Specific" Check CachyOS often uses fish or zsh with specific pathing. If you installed Lutris via the CachyOS Package Installer (the GUI one), it sometimes places entries in a way that requires a shell restart or a logout/login to sync the XDG environment variables. The Strategy: Check the file contents with the grep command above. Edit the file (using sudo nano) to remove any NoDisplay=true line if it exists. Log out and log back in. If it shows up in search, the path is indexed; if it's missing from the menu, the desktop entry is being filtered. Stop wasting time clicking through menus—did the grep command return a NoDisplay=true or Hidden=true result?
