---
category: homelab
date: 2026-02-19
id: 836730
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was troubleshooting why Lutris appeared in search but not in the application
  menu's games section.
tags:
- lutris
- application-menu
- cachyos
- troubleshooting
- games-section
---
# when i look in lost and found nothing is there and its not in the games section either 

### USER
when i look in lost and found nothing is there and its not in the games section either 

### GEMINI
Since it’s not in "Lost & Found" and not in "Games," your application menu has explicitly excluded the entry from its view, likely due to a bug in how KDE Plasma 6 (the default for CachyOS) handles menu updates. Because search works, the system knows the app exists. The menu is just being stubborn. Here is the direct, manual way to force it back: 1. The "Kick the Tires" Method (KMenuEdit Force-Save) KDE's menu often needs a manual "Save" action to re-scan the directories properly. Open KMenuEdit (right-click the Start Menu icon > Edit Applications). Click on the Games category. Click New Item at the top. Give it a temporary name like "Test." Click Save in the top left corner. Check your menu now. Often, saving any change forces the menu to realize Lutris was missing and it will suddenly pop back into the Games category. If Lutris appears, you can delete the "Test" item and save again. 2. Manual Re-Insertion If the step above didn't work, we will manually tell the menu exactly where Lutris is. In KMenuEdit, go to the Games category. Click New Item. Name: Lutris Description: Video Game Preservation Platform Command: lutris %U Icon: Click the icon box, search for lutris, and select it. Click Save. 3. Clear the Global Menu Cache If you want to fix the root cause rather than just adding a manual entry, you need to wipe the specific files Plasma uses to build the "grid" view. Run this block of commands in your terminal: # Wipe the service caches rm -rf ~/.cache/ksycoca6* rm -rf ~/.cache/plasma-svgelements* # Force the system to re-index desktop files sudo update-desktop-database /usr/share/applications # Restart the Shell (Your screen will flicker) kbuildsycoca6 --noincremental plasmashell --replace & disown Why is this happening? On CachyOS/Arch, when packages update, they sometimes change the "MimeType" or "Categories" in the .desktop file. If your local menu configuration (~/.config/menus/applications-kmenuedit.menu) has a "memory" of the old file, it might conflict and hide the new one because it doesn't know where to put it. Does it show up in the "Games" category now after you added a "Test" item and saved?
