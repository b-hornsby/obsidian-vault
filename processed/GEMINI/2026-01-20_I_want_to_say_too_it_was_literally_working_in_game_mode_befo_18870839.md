---
category: general
date: 2026-01-20
id: 538609
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan emphasizes that the game was working in game mode before the update
  issue occurred.
tags:
- steam-deck
- citron
- tears-of-the-kingdom
- game-mode
- regression
- update-issue
---
# I want to say too it was literally working in game mode before the update issue

### USER
I want to say too it was literally working in game mode before the update issue

### GEMINI
This is the classic "Desync" trap between Desktop Mode and Game Mode on the Steam Deck. If it works in Desktop but not Game Mode, the problem isn't the file itself—it's how the Deck handles the environment when you launch a shortcut. Here is why you are seeing "No update installed" and why the game won't load in Game Mode: 1. The Metadata Desync (The "No Update" Lie) When you install an update in Desktop Mode, Citron updates its local database. However, Game Mode sometimes launches the AppImage with a different set of "argument flags" or environment variables. The Ghost Entry: The "properties" window is showing you what the emulator sees in the folder, but the game engine itself isn't registering it because the pathing for the NAND (where the update lives) is perceived differently in Game Mode. The Fix: Go to Desktop Mode, open Citron, right-click the game, and "Remove All Installed Contents." Then, instead of using the "Install to NAND" menu, try this: Place the update .nsp file in the same folder as your game. Right-click the game -> Properties -> Add-ons. If it’s not there, re-install it via the menu one last time, but ensure you are clicking "Save" and not just closing the window. 2. The Gamescope Hang (Why it won't load) Game Mode uses Gamescope (the micro-compositor), while Desktop Mode uses X11/KDE. TotK is notorious for hanging on launch in Game Mode if the VRAM or Clock Speed is being throttled by Steam's overlay. Action: While the game is "loading" (and hanging) in Game Mode: Press the (...) button on the right of the Deck. Go to the Performance (Battery) tab. Set Manual GPU Clock Frequency to OFF (or set it manually to 1600 to force it to wake up). Ensure Frame Limit is set to OFF. If it's set to 30 or 60, the emulator's internal clock can desync during the "Update check" phase of the TotK boot sequence, causing an infinite loop. 3. The "Force Launch" Test If the shortcut you're using in Game Mode was created before the update, the shortcut's "Target" might be pointing to a specific version or cached file that is now invalid. The Move: In Game Mode, don't launch the game directly. Launch the Citron AppImage itself first. Once the emulator GUI opens inside Game Mode, launch TotK from there. If it works this way, your Steam shortcut is broken. You need to delete the shortcut and re-add the game via Steam ROM Manager or EmuDeck to refresh the launch arguments. The Advisor's Cold Truth You're treating the symptom, not the disease. The "Update Patch" you can't delete is a permission-locked file caused by the AppImage crash. Stop using the UI to delete it. 2. Open Konsole in Desktop Mode. Type: rm -rf ~/.local/share/citron/nand/system/Contents/registered/* This nukes every update and firmware file. It is a clean slate. Re-install your Firmware, then re-install the TotK update. If you do this and it still won't load in Game Mode, the issue is your "keys" file—TotK updates require newer keys than the base game. Do you know what version your prod.keys are?
