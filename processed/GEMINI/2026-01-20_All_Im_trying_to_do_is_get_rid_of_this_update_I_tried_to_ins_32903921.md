---
category: general
date: 2026-01-20
id: 656910
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is trying to remove a faulty update for Tears of the Kingdom on his
  Steam Deck so he can play it in game mode.
tags:
- steam-deck
- citron
- tears-of-the-kingdom
- game-update
- rollback
- game-mode
---
# All I’m trying to do is get rid of this update I tried to install for tears of the kingdom so I can play it in game mode

### USER
All I’m trying to do is get rid of this update I tried to install for tears of the kingdom so I can play it in game mode

### GEMINI
The reason my command "did nothing" is exactly why your update is still there: the AppImage is using a different data path than the standard one. On Linux, if you run a "delete" command on a folder that doesn't exist, it just stays silent. Since your firmware is still there, we haven't touched the actual folder Citron is using. Here is the "no-nonsense" way to find and kill that update once and for all. 1. Find the REAL folder We need to find where your firmware is actually stored. Run this command in Konsole: find ~ -name "registered" -type d 2>/dev/null Look at the results. You will likely see a path that looks like one of these: /home/deck/Applications/citron... /home/deck/.var/app/org.citron_emu.citron/... /home/deck/Emulation/storage/citron/... 2. The Manual Wipe Once you see the path from that command, do not use the terminal. Use the Dolphin File Manager so you can see what you're doing: Open Dolphin. Click the three-line menu (top right) and check "Show Hidden Files". Navigate to the path you found in Step 1. Go into the registered folder. Delete everything inside. (This is where the "ghost" update files live). Go back one level to the citron folder, find the shader folder, and delete everything inside there too. Corrupted shaders from a failed update are the #1 cause of Game Mode hangs. 3. Why Game Mode is still failing If it works in Desktop but not Game Mode, it’s a Refresh Rate/Clock issue. Game Mode tries to "optimize" the Deck, which breaks emulators. Do this in Game Mode right now: Launch the game. While it's "loading," press the (...) button on the right. Go to Performance (the battery icon). Set Frame Limit to OFF (Slide it all the way to the left). Set Refresh Rate to 60. Turn OFF "Manual GPU Clock." Wait. After an update/wipe, TotK can take up to 3 minutes on a black screen to rebuild the launch cache. The Strategic "Cheat Code" If you just want the update gone and the game working: Don't "Install to NAND." Delete the update file from your Deck entirely. If the emulator still thinks it's there, rename your citron folder to citron_backup. Open the emulator—it will be clean. Put your keys back in. If it works now, the problem was the corrupted database in that folder. What was the output of that find command? Copy and paste the path here if you want me to give you the exact "delete" command.
