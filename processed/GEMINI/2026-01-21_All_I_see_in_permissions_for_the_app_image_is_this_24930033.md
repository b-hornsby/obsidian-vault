---
id: 102114
source: GEMINI
date: 2026-01-21
tags: ['appimage', 'permissions', 'linux', 'troubleshooting']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is investigating the permissions of an AppImage file.
---
# All I see in permissions for the app image is this

### USER
All I see in permissions for the app image is this

### GEMINI
If you are seeing the "Launching..." bar stay frozen like that even in Desktop Mode, then Steam is sending a command that the operating system is physically unable to execute. Your permission screen shows the "Execute" box is checked, so the file itself is allowed to run, but the Target path is likely pointing to the wrong place or using broken syntax after the reparse. The "Surgical" Diagnostic To fix this, we need to see the error message that Steam is hiding from you. Open Konsole (the terminal app) in Desktop Mode. Open Steam in Desktop Mode, right-click your game, and select Properties. Copy everything in the Target box. It should look like: "/home/deck/Applications/citron.AppImage" -f -g "/path/to/your/game.xci" Paste that entire line into the Konsole window and press Enter. What to Look For in the Error: "No such file or directory": Your reparse used a path that doesn't actually exist on your SD card or SSD. Check for a missing letter or a wrong folder name. "Permission denied": Even if that box is checked in the UI, sometimes the SD card is "locked" in read-only mode. A "NAND" or "Keys" error: If the emulator opens but the game doesn't, your SAK merger likely corrupted the file's header, or it's looking for firmware that was wiped during your "reinitialization". Two Immediate Fixes to Try: Remove the -f: In the Steam "Target" box, delete the -f but leave the -g. Sometimes "Fullscreen" mode causes a hang on the first launch after a reparse. Clear the "Start In" field: Ensure the "Start In" box in Steam Properties is completely empty or points only to the folder containing the .AppImage without any quotes. Tell me exactly what the Konsole says when you try to run that command. That is the only way to see past the "Launching..." lie.
