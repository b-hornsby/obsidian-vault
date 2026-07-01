---
category: homelab
date: 2026-01-20
id: 947992
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was trying to manage installed game contents in Citron's NAND and encountered
  confusing messages about base game installation.
tags:
- citron-emulator
- nand
- game-contents
- switch-game-management
---
# When I remove all installed contents from the game it says the base game isn’t installed in the nand and can’t be removed, there is no update installed for this title and there is no dlc installed for this title

### USER
When I remove all installed contents from the game it says the base game isn’t installed in the nand and can’t be removed, there is no update installed for this title and there is no dlc installed for this title

### GEMINI
When Citron tells you "the base game isn't installed in the NAND," it reveals exactly what's wrong: You are running a "Split Library." Your base game is in one folder (likely your SD card or home downloads), but you tried to install the update to the internal NAND (the emulator's "virtual" memory). Because the update "sticks" to the NAND but doesn't see a base game next to it, it has nothing to patch. Here is the brutal, prioritized path to fix this. Stop trying to use the "Remove" menu; it's looking for files in the wrong place. 1. The "Clean Slate" Terminal Command You need to manually wipe the corrupted update records that the UI can't see. Open Konsole in Desktop Mode. Copy and paste this exactly: rm -rf ~/.local/share/citron/nand/system/Contents/registered/* (If that path doesn't exist, use: rm -rf ~/.var/app/org.citron_emu.citron/data/citron/nand/system/Contents/registered/*) This will delete the "ghost" update. 2. The "Unified Library" Strategy The reason it works in Desktop but not Game Mode is that Game Mode is likely launching the game via a shortcut that points directly to the .nsp/.xci file, bypassing the NAND update you installed in Desktop Mode. The Fix: Do not "Install to NAND." Create a folder called TotK on your Steam Deck. Put the Base Game AND the Update File in that same folder. In Citron (Desktop Mode), right-click the game -> Properties -> Add-ons. If the update is in the same folder, Citron should see it automatically without "installing" it. This is much more stable for the Steam Deck. 3. Fixing Game Mode (The "Short" Launch) If it still won't load in Game Mode after the cleanup: Go to your Steam Library in Desktop Mode. Right-click the TotK shortcut -> Properties. Look at the Target. If it points to TotK_Update.nsp, it will never load. It must point to the Citron AppImage. The Launch Options should look something like: "/path/to/citron.AppImage" -g "/path/to/TotK_BaseGame.nsp" The "Shaders" Trap: If the screen stays black for 2–3 minutes in Game Mode, don't touch it. It is rebuilding the shaders for the new update. If you force-close it, you corrupt the cache again. 4. Why it says "No Update Installed" If you see it in the properties list but it says "No update installed," it means your prod.keys are too old. Tears of the Kingdom updates (like 1.2.1 or higher) require Firmware/Keys version 16.0.3 or newer. If your keys are old, Citron sees the update file but can't "decrypt" it to apply it to the game. What to do next: Clear the registered folder using the command in Step 1. Then, tell me: What is the version number of your prod.keys? (If you don't know, tell me the last time you updated them).
