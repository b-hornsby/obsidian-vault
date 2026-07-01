---
id: 618668
source: GEMINI
date: 2026-02-19
tags: ['lutris', 'desktop-entry', 'visibility', 'grep', 'cachyos']
category: homelab
sentiment: exploratory
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was checking whether the Lutris .desktop file had any hidden or display-restricting flags set.
---
# ❯ grep -E "NoDisplay|Hidden|OnlyShowIn" /usr/share/applications/net.lutris.Lutris.desktop

~
❯  

### USER
❯ grep -E "NoDisplay|Hidden|OnlyShowIn" /usr/share/applications/net.lutris.Lutris.desktop

~
❯  

### GEMINI
Empty results from grep mean the file itself isn't telling the system to hide it. This confirms your problem isn't a "hidden" flag—it’s a cache or pathing failure in how your Application Menu (the GUI) reads the desktop database compared to how your Search (the indexer) reads it. Since you're on CachyOS, you're likely using KDE Plasma or GNOME. Stop poking the file and force the environment to acknowledge the reality of your disk. 1. The Nuclear Cache Refresh (KDE Plasma) If you are on KDE (standard for Cachy), the ksycoca (KService Desktop Config Cache) is likely corrupted or stale. Search uses a different indexing service (KRunner/Baloo), which is why it works there but not in the menu. Run this: kbuildsycoca6 --noincremental Note: If you get "command not found," try kbuildsycoca5—though CachyOS has moved to Plasma 6. 2. The Global Refresh (GNOME/Other) If the above doesn't work or you aren't on KDE: sudo update-desktop-database /usr/share/applications 3. The Pathing Reality Check Check if you have a duplicate, broken entry in your local user folder that is overriding the system-wide one you just found. The local one always wins, and if it's broken, the icon vanishes. Run this: ls ~/.local/share/applications/net.lutris.Lutris.desktop If this file exists: Delete it. It’s likely a leftover or a broken manual entry. If it doesn't exist: Move to step 4. 4. The Last Resort: Manual Menu Audit If you are on KDE, right-click your Application Launcher (Start button) -> Edit Applications... Navigate to the Games category. Look for Lutris. If it’s there but "Hidden" is checked in the GUI, uncheck it and hit Save. You're searching for a ghost in the machine. If kbuildsycoca6 doesn't bring it back, you have a broken XDG path. Run echo $XDG_DATA_DIRS and paste the output here. I want to see if your system even knows where to look for desktop files.
