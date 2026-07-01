---
id: 414090
source: GEMINI
date: 2026-01-19
tags: ['citron-emulator', 'emulation-station', 'steam-rom-manager', 'steam-deck-game-mode']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan confirmed Citron worked in Emulation Station and wanted to get it recognized by Steam ROM Manager for game mode.
---
# i want to also say that within emulation station it already has the option to switch to the citron (standalone) emulator. my goal though is to be able to have citron to be picked up by steam rom manager as well so that i can add those games to my steam game mode 

### USER
i want to also say that within emulation station it already has the option to switch to the citron (standalone) emulator. my goal though is to be able to have citron to be picked up by steam rom manager as well so that i can add those games to my steam game mode 

### GEMINI
Since ES-DE already has the Citron option, you’ve done the easy part. To get those same games into Steam Game Mode, you have to tell Steam ROM Manager (SRM) exactly how to "talk" to Citron. SRM doesn't "know" Citron exists by default, so we’re going to clone a working parser and swap the guts. Follow these steps exactly. Don’t cut corners or you’ll end up with broken shortcuts that launch nothing. 1. The Prep Work Make sure you are in Desktop Mode. Ensure Steam is completely closed (check the system tray). SRM cannot write to Steam if it's running. Note the exact path of your Citron AppImage (e.g., /home/deck/Applications/citron.AppImage). 2. Configure Steam ROM Manager Open EmuDeck and launch Steam ROM Manager. Unlock the "Create" Mode: * Click Settings on the left. Change the Theme to "Classic". (The default EmuDeck theme hides the advanced "Clone" and "Create" features you need). Clone a Working Parser: Look at the list of parsers on the left. Find Nintendo Switch - Yuzu or Nintendo Switch - Ryujinx. Select it, scroll to the bottom of the right pane, and click Clone. A new entry will appear at the bottom of the list. Click it to edit. 3. Swap the Details (The "Surgery") Update these specific fields in your new cloned parser: Parser Title: Change to Nintendo Switch - Citron. Steam Collections: Change to Nintendo Switch - Citron. Executable: Click the browse button and select your citron.AppImage. Command line arguments: This is the most common place people fail. It should look like this (copy/paste it): -f -g "${filePath}" Note: If you were cloning from Yuzu, remove any extra flags like --fullscreen if they cause issues, but -f -g (fullscreen/start game) usually works for Citron. ROMs Directory: Make sure this points to your Switch ROMs folder (usually /run/media/mmcblk0p1/Emulation/roms/switch/ if on SD card). 4. Finalize and Parse Click Save at the bottom left. Go to the Preview tab (or "Add Games" in some versions). Click Parse. You should see your Switch games pop up with Citron icons. Click Save to Steam. Wait for the notification that says "Done adding/removing entries." Why this is better than the "Renaming" trick Renaming your AppImage to yuzu.AppImage is for people who want to be lazy. By creating a dedicated Citron Parser, you can have both Ryujinx and Citron entries for the same game in Steam if you want to test performance, and you won't get confused about which emulator is actually running. Next step: Go back into Game Mode and try launching a game. If it opens but stays in a window, did you remember to keep the -f in the command line arguments?
