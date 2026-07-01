---
id: 132553
source: GEMINI
date: 2026-02-19
tags: ['kbuildsycoca6', 'kde', 'desktop-cache', 'cachyos', 'application-menu']
category: homelab
sentiment: executing
resolution: resolved
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was rebuilding the KDE system cache to refresh the application menu entries.
---
# ❯ kbuildsycoca6 --noincremental
kbuildsycoca6 running...

~
❯ 

### USER
❯ kbuildsycoca6 --noincremental
kbuildsycoca6 running...

~
❯ 

### GEMINI
If kbuildsycoca6 finished and the icon still isn't in your menu, the cache is clean, but the logic is still broken. Search works because it indexes the file name, but the Application Menu is a snob—it won't show the icon if it thinks the Exec path or the Icon is invalid. Let's look at the "hidden" logic the system uses to reject a desktop file. Run this to see the guts of the file: grep -E "Exec|Icon|Categories|Terminal" /usr/share/applications/net.lutris.Lutris.desktop The Three Likely Culprits: Broken Path: If Exec= points to a location that doesn't exist (e.g., /usr/bin/lutris vs /usr/local/bin/lutris), the menu will silently discard the entry while Search (which just looks at the filename) still shows it. Missing Icon: If the Icon= field points to a theme icon that isn't installed in your current icon pack, some launchers hide the entry entirely rather than showing a "broken" image. The "TryExec" Guard: Many desktop files have a TryExec line. If the file pointed to by TryExec isn't found, the entry is ignored. Do this now: Check if the binary actually exists where the desktop file thinks it does. Run: which lutris If which lutris returns nothing: You have a ghost desktop file from a previous installation and the app isn't actually installed. If it returns a path: Compare that path to what you see in the Exec= line from the grep command above. Paste the output of the grep and the which lutris command. Let's see where the mismatch is.
