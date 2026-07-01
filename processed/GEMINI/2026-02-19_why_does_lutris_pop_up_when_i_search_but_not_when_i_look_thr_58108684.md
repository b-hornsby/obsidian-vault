---
category: homelab
date: 2026-02-19
id: 827798
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was trying to understand why Lutris appeared in KDE search but not
  in the categorized application menu.
tags:
- lutris
- application-menu
- cachyos
- kde-menu
- desktop-entry
---
# why does lutris pop up when i search but not when i look through my applications? on cachyos

### USER
why does lutris pop up when i search but not when i look through my applications? on cachyos

### GEMINI
This usually happens because your application launcher (like the KDE Plasma or GNOME menu) hasn't refreshed its database, or the desktop entry file for Lutris is marked with a property that hides it from the grid. Since you're on CachyOS, follow these steps to force it to show up: 1. The Quickest Fix: Refresh the Database Your search engine (KRunner or GNOME Search) often looks at different metadata than the "All Applications" grid. Force a refresh by running this in your terminal: sudo update-desktop-database If you are using KDE Plasma, also try: kbuildsycoca6 --noincremental 2. Check for "NoDisplay" or "Hidden" Status Sometimes Lutris (especially if installed via Flatpak or a specific AUR version) includes a flag in its configuration that hides it from menus. Locate the Lutris desktop file: ls /usr/share/applications/net.lutris.Lutris.desktop # OR if Flatpak: ls /var/lib/flatpak/exports/share/applications/net.lutris.Lutris.desktop Open the file (e.g., nano /usr/share/applications/net.lutris.Lutris.desktop) and look for these lines: NoDisplay=true Hidden=true If they exist, change them to false or delete the lines entirely. Save and exit. 3. Verify the Installation Method CachyOS users sometimes accidentally install "add-ons" instead of the main app. The Problem: You might have installed a context menu extension (like lutris-git-ext or a specific runner) instead of the full package. The Solution: Ensure you have the meta-package that CachyOS recommends for gaming. Run: sudo pacman -S cachyos-gaming-applications This ensures lutris is properly installed alongside all necessary dependencies and desktop files. 4. Categorization Glitch If Lutris is in your "Games" category but you are looking in "All Applications" or "Office," it might be filtered out depending on your launcher's settings. Right-click your Start Menu/Launcher icon -> Edit Applications. Search for Lutris in the editor. If it's there but unchecked, check it. If it's in a weird category, move it to "Games." Would you like me to show you how to manually create a desktop entry if the file is completely missing?
