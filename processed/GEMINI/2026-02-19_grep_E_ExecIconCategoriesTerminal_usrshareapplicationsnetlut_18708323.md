---
id: 424166
source: GEMINI
date: 2026-02-19
tags: ['lutris', 'desktop-entry', 'grep', 'cachyos', 'application-config']
category: homelab
sentiment: exploratory
resolution: resolved
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was inspecting the Lutris .desktop file to understand its Exec command, icon, and category settings.
---
# ❯ grep -E "Exec|Icon|Categories|Terminal" /usr/share/applications/net.lutris.Lutris.desktop
Categories=Game;
Exec=lutris %U
Icon=net.lutris.Lutris
Terminal=false

~
❯ 

### USER
❯ grep -E "Exec|Icon|Categories|Terminal" /usr/share/applications/net.lutris.Lutris.desktop
Categories=Game;
Exec=lutris %U
Icon=net.lutris.Lutris
Terminal=false

~
❯ 

### GEMINI
The desktop file is structurally perfect. There are no "hide" flags, the category is standard, and the execution command is clean. If kbuildsycoca6 didn't fix it, we are dealing with a Category Filter or a Local Override issue. Your application menu is intentionally ignoring this file because it thinks it doesn't belong or it's being superseded by a broken local version. Run these two commands and give me the output: 1. The Local Override Check Check if there is a "dead" version of this file in your user directory that is masking the system one: ls -l ~/.local/share/applications/net.lutris.Lutris.desktop (If this returns a file, delete it immediately: rm ~/.local/share/applications/net.lutris.Lutris.desktop then restart your menu.) 2. The Binary Verification Search works because it sees the .desktop file. The menu fails because it validates the Exec line. Does the system actually know where lutris is? which lutris The "Brutally Honest" Reality Check: If which lutris returns a valid path and there is no local override, you are likely looking in the wrong place. Check the "Games" category specifically. * Check "Lost & Found" or "Other." * Right-click your Application Launcher -> Edit Applications. Look for Lutris in the tree. If it’s there but greyed out or unchecked, your menu editor has manually disabled it. Is which lutris returning a path, or are you chasing a ghost entry for an app that isn't actually installed?
