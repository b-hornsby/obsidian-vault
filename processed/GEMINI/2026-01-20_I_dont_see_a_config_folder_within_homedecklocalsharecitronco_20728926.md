---
category: general
date: 2026-01-20
id: 713084
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is unable to find the config folder within the specified Citron directory
  on his Steam Deck.
tags:
- steam-deck
- citron
- file-system
- configuration
- troubleshooting
---
# I don’t see a config folder within home/deck/.local/share/citron/config/

### USER
I don’t see a config folder within home/deck/.local/share/citron/config/

### GEMINI
If you don’t see a config folder, you’re either looking in the wrong root directory or the AppImage hasn't initialized its file structure where you expect it. Since you're on a Steam Deck, let's stop guessing and use the standard Linux paths. 1. Where the "Ghost" Files Actually Are On the Steam Deck, AppImages and Flatpaks often store their data in one of two places. Check these specific paths: Option A (Standard Home): /home/deck/.local/share/citron/ Option B (Flatpak/EmuDeck style): /home/deck/.var/app/org.citron_emu.citron/data/citron/ Crucial: If you don't see folders starting with a dot (like .local or .var), click the three-line menu in the top right of the File Browser (Dolphin) and check "Show Hidden Files". If you skip this, you are flying blind. 2. The "Forced" Clean Slate If the GUI says an update is there but the folder is empty, the Metadata Index is corrupted. To fix this without hunting for invisible files, do this: Open Konsole (the terminal). Copy and paste this command to find exactly where your Citron NAND is: find ~ -name "registered" -type d | grep citron Once you have that path, navigate to the folder one level up from registered (it should be called Contents). Delete the entire registered folder. > Why this works: This deletes the emulator's "memory" of all installed updates and firmware. It forces Citron to stop trying to load the "ghost" update that is crashing your game. You will have to re-install your Firmware and the Patch afterward, but it clears the blockage. 3. Check for "Read-Only" Locks If you found the file but "it won't let you delete it," the AppImage has locked the file permissions. In the terminal, type: sudo rm -rf [path to the stubborn folder] If you haven't set a password yet, type passwd first to create one. The Brutal Truth You are wasting time trying to surgicaly remove a patch that doesn't exist in the file system but exists in the emulator's database. The most efficient move is to delete the nand folder entirely. * Location: /home/deck/.local/share/citron/nand/ (or the .var equivalent). Action: Delete it. Cost: 5 minutes to re-install Firmware and the Patch. Gain: You actually get to play the game tonight. Would you like the exact Terminal command to wipe the NAND and reset the emulator's database so you can start fresh?
