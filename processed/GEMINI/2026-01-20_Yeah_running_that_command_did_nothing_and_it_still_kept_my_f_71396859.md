---
category: homelab
date: 2026-01-20
id: 078713
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan found that a command meant to manage firmware in Citron's NAND did
  not remove the firmware as expected.
tags:
- citron-emulator
- firmware
- nand
- switch-emulation
---
# Yeah running that command did nothing and it still kept my firmware

### USER
Yeah running that command did nothing and it still kept my firmware

### GEMINI
If that command "did nothing" and your firmware is still there, it confirms my suspicion: The path we targeted is the wrong one. The AppImage is storing its data in a different hidden directory, which is exactly why the GUI "Remove" button isn't working—it's trying to delete files from a path it no longer "owns" or can't find. Here is the unfiltered reality: You are chasing a ghost because the emulator is looking at Folder A, but your files are in Folder B. 1. Locate the REAL Data Folder We need to find where the firmware actually lives so we can kill that corrupted update record. Run this command in Konsole: find ~ -name "registered" -type d 2>/dev/null Look at the results. * If you see a path with .var/app/org.citron_emu.citron, that’s the one. If you see a path in Documents or Applications, that’s it. Once you find the real path, run the rm -rf command on that specific directory. 2. The "Game Mode" Fix (The 60Hz Trap) You said it works in Desktop but not Game Mode. This is almost always a Refresh Rate mismatch. Switch to Game Mode. Open the game. When it starts loading, press the (...) button. Go to the Performance (Battery) tab. Look at Frame Limit and Refresh Rate. Crucial: Set Frame Limit to OFF and Refresh Rate to 60. If the Deck is set to 30Hz or 45Hz, the emulator's internal clock for TotK will freeze during the "Checking for Updates" phase, causing an infinite loading screen. 3. Why the "No Update" Error Persists The reason it says "No update installed" in properties despite being there is that you likely have mismatched Regions. Is your base game USA and the update EUR? Or vice versa? If the Title IDs don't match exactly, the emulator will show the file in the "Add-ons" list but will report "No update installed" because it can't link them. The Solution: Right-click the game in Citron -> Properties. Check the Title ID (it's a long string of numbers). Ensure your update file has the same Title ID. Your Strategic Move Stop being surgical. If you want to play today, do this: In Desktop Mode, rename the folder /home/deck/.local/share/citron to /home/deck/.local/share/citron_old. Open Citron. It will be like a brand new install. Add your keys, install the firmware, and point it to your game. Do not "Install to NAND." Just put the update file in the same folder as the game. Citron should pick it up automatically. Run that find command in Step 1 and tell me what paths it spits out. I'll tell you exactly which one to nuke.
