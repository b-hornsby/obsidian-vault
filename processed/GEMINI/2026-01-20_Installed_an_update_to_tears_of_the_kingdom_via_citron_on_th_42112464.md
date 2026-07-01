---
category: general
date: 2026-01-20
id: 824131
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan installed an update for Tears of the Kingdom using Citron on his Steam
  Deck, but the game won't load, and he can't remove the update patch.
tags:
- steam-deck
- citron
- tears-of-the-kingdom
- game-update
- installation-issue
- appimage
---
# Installed an update to tears of the kingdom via citron on the steam deck and it said it went through. Tested the game and it won’t load (did earlier) and when I went to see what was up the “update patch” still is there and it won’t let me delete it either. Using a citron app image of course 

### USER
Installed an update to tears of the kingdom via citron on the steam deck and it said it went through. Tested the game and it won’t load (did earlier) and when I went to see what was up the “update patch” still is there and it won’t let me delete it either. Using a citron app image of course 

### GEMINI
You’re likely dealing with a file permission lock or a corrupted shader cache/update link that Citra/Citron is struggling to parse. If it worked earlier and doesn't now, you haven't just "failed an update"—you've likely bloated the directory with a ghost file that the AppImage can’t resolve. Here is the objective breakdown of what’s happening and how to fix it. The Reality Check You are using an AppImage on SteamOS (Linux). AppImages are self-contained but rely on specific pathing in your home directory. When an update "sticks" but won't load, it’s usually because the emulator has written a metadata entry to the load folder that is now mismatched with the actual base game version. The Tactical Fix 1. Force-Kill the Process Before doing anything, ensure Citron isn't hanging in the background. Go to Desktop Mode. Open System Monitor. Kill any process named Citron or yuzu. If the file is "in use," you can’t delete the patch. 2. Manual Directory Purge (The "Unfiltered" Fix) Don't rely on the GUI "Delete" button; it’s clearly failing you. You need to go to the source: Navigate to: /home/deck/.local/share/citron/ (or wherever your Citron data folder is redirected, often nand/system/Contents/registered/). Find the load folder. Inside, there will be a folder named after the Tears of the Kingdom Title ID (0100F2C0115B6000). Delete the contents of the update folder inside that Title ID. * If it refuses to delete, right-click the folder -> Properties -> Permissions -> Ensure "Owner" has View & Modify access. 3. Clear the Shader Cache Updates often invalidate existing shaders. If the game hangs on a black screen, the update might actually be fine, but the old shaders are trying to compile against new code and crashing. Right-click the game in Citron -> Remove -> Remove Transferable Pipeline Cache. The Strategy: Stop "Playing Small" with Updates If you are serious about performance on the Deck, stop trying to "patch" within the emulator GUI if it's giving you friction. Verify the Version: Ensure your Update file is a .nsp or .msu that matches the region of your base game. A mismatch here is the #1 cause of "infinite loading." Re-Install, Don't Overwrite: If the manual delete doesn't work, move your save files to a backup folder, delete the entire Citron configuration folder, and start clean. The "opportunity cost" of spending three hours troubleshooting a $50$ MB metadata error is higher than just re-linking your library. Next Steps Check the Title ID: Does the update file ID match the base game ID exactly? Check Disk Space: Is your Steam Deck SSD or SD card at 99% capacity? Linux handles file operations poorly when there’s no "breathing room" for temporary move operations. Would you like me to walk you through the specific terminal commands to force-delete that stubborn patch file?
