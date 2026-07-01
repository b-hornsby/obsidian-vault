---
id: 083631
source: GEMINI
date: 2026-02-19
tags: ['lutris', 'desktop-file', 'local-applications', 'cachyos', 'troubleshooting']
category: homelab
sentiment: exploratory
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was checking if a local user-level Lutris .desktop file existed to troubleshoot application menu visibility.
---
# ❯ ls -l ~/.local/share/applications/net.lutris.Lutris.desktop
"/home/toastedmel0n/.local/share/applications/net.lutris.Lutris.desktop": No such file or directory (os error 2)

~
❯ 

### USER
❯ ls -l ~/.local/share/applications/net.lutris.Lutris.desktop
"/home/toastedmel0n/.local/share/applications/net.lutris.Lutris.desktop": No such file or directory (os error 2)

~
❯ 

### GEMINI
You've confirmed the file isn't being overridden locally, and it isn't explicitly hidden. Since you're on CachyOS, we’re down to the two most likely "invisible" blockers: Binary validation or Menu Editor exclusion. Stop poking the metadata and verify the executable itself. If the menu can't find the binary, it won't show the icon, even if the search indexer (which is just a file scraper) can see the .desktop file. 1. The Reality Check: Is it actually installed? Run this: which lutris If it says lutris not found: You have a "ghost" desktop file. You likely uninstalled Lutris but the .desktop file stayed behind. Search sees the file; the Menu sees a broken link and hides it. If it gives a path (e.g., /usr/bin/lutris): Proceed to step 2. 2. The Menu Editor Audit (KDE Plasma) On CachyOS/KDE, the Menu Editor (kmenuedit) has the power to "uncheck" an application, which keeps the file on disk but tells the Plasma drawer to ignore it. Open your terminal and run: kmenuedit Look under the Games category. Search for Lutris. Is it there? If it is, look at the checkbox next to it. If it’s unchecked, check it and hit Save (top left). 3. The "Cachy-Special" Cache Purge If which lutris works and kmenuedit shows it as active, your icon cache is lying to you. Force a hard reset of the icon and menu services: rm ~/.cache/ksycoca6* ~/.cache/icon-cache.kcache kbuildsycoca6 --noincremental What did which lutris return? If it returned nothing, you're chasing a ghost. If it returned a path, tell me—does it show up in kmenuedit?
