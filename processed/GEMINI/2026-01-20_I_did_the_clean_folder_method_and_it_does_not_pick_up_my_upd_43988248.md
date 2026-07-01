---
category: general
date: 2026-01-20
id: 209124
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan tried the 'clean folder method' for updating the game, but the update
  is not being recognized.
tags:
- steam-deck
- citron
- tears-of-the-kingdom
- clean-folder-method
- update-issue
---
# I did the clean folder method and it does not pick up my update?

### USER
I did the clean folder method and it does not pick up my update?

### GEMINI
If the "clean folder" method didn't work, it's because Citron is more rigid than other emulators like Ryujinx—it often refuses to "auto-scan" updates unless they are merged into the file or manually indexed. Since we already cleared your corrupted NAND, we can now do a "clean" install without the ghost files interfering. Here is how you get that update working correctly without breaking Game Mode again. 1. The "Right" Way to Install to NAND Since the folder scan failed, you have to use the internal installer, but you must do it in a specific order to prevent the database from desyncing again: Open Citron in Desktop Mode. Go to File -> Install Files to NAND... Select your TotK Update .nsp file. Crucial Step: Once it finishes, Right-click Tears of the Kingdom -> Properties. Go to the Add-ons tab. You should now see the update listed. Ensure the box next to it is checked. Launch the game in Desktop Mode first. Let it reach the title screen. This "bakes" the update into the emulator's launch settings. 2. If it still doesn't show up (The Key Check) If you install the file and it still says "no update" or doesn't show in Add-ons, your prod.keys are likely outdated. Tears of the Kingdom updates (like v1.2.0 or 1.2.1) use a newer encryption than the base game. If your keys are from the base game release (v16.0.0), Citron will "install" the update file but can't read it, so it acts like it's not there. The Fix: Ensure you have prod.keys version 16.0.3 or higher in your keys folder. 3. Preventing the Game Mode Hang (The "Timeout" Fix) The reason Game Mode hangs while Desktop works is usually because the Steam Deck thinks the app is "stuck" while it's actually just processing the update for the first time. Wipe Shaders Again: Right-click the game -> Remove -> Remove All Pipeline Caches. (New updates need new shaders). Game Mode Launch: When you switch to Game Mode and launch, do not touch the controller for at least 3 minutes. * The "30FPS" Deadlock: Open the (...) menu -> Performance. Make sure your Frame Limit is OFF. If it's set to 30, the emulator's "update check" logic can sometimes hang indefinitely during the boot sequence. Strategy: The "Unfiltered" Move If you keep having trouble with .nsp updates, the most stable way to play TotK on Steam Deck is to merge the update into the game file itself (creating a single .xci or .nsp that includes the update). Use a tool called SAK (Switch Army Knife) on a PC to merge your base game and update. Transfer the new, single file back to your Deck. Benefit: No more "Install to NAND," no more database corruption, and it will work in Game Mode 100% of the time. Try Step 1 (Install to NAND in Desktop) now. Does the update finally show up in the "Add-ons" tab?
