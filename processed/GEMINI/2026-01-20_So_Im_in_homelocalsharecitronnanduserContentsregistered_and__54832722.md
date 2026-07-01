---
category: general
date: 2026-01-20
id: 805182
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is exploring a specific directory in the Citron file structure and
  finds it to be empty, which is unexpected.
tags:
- steam-deck
- citron
- file-system
- directory-structure
- troubleshooting
---
# So I’m in home/.local/share/citron/nand/user/Contents/registered and all I see is a “citron_meta” folder and it’s empty?

### USER
So I’m in home/.local/share/citron/nand/user/Contents/registered and all I see is a “citron_meta” folder and it’s empty?

### GEMINI
If that folder is empty, the "ghost" is living in your System NAND, not your User NAND. This happens because Citron (like its predecessor Yuzu) splits data between where it stores "System" files (Firmware) and "User" files (Updates/DLC). The update is currently registered in a database that says it exists, but the file system is either permission-locked or the AppImage has mapped the path elsewhere. 1. The "Kill the Database" Move Since you can't find the file in user, it’s likely in the system side or the database file is lying to the UI. Navigate to: /home/deck/.local/share/citron/nand/system/Contents/registered/ If you see folders with long hex names here (e.g., 000000...), delete them all. Crucial: Go back to the main citron folder and look for a file called records.bin. Delete it. This is the "index" that tells Citron what is installed. If you don't kill this file, the UI will keep showing the update. 2. Force-Reset the AppImage (The "Nuclear" Option) If you just want the update gone so you can play in Game Mode, stop being surgical. In Desktop Mode, rename your folder from /home/deck/.local/share/citron to /home/deck/.local/share/citron_OLD. Open Citron. It will be completely fresh (no keys, no games). Copy your keys folder from the citron_OLD to the new citron folder. Add your game directory. DO NOT install the update. Try Game Mode now. 3. Why Game Mode is still hanging If you delete the update and it still won't load in Game Mode, the problem is Poisoned Shaders. Right-click the game in Citron -> Remove -> Remove All Pipeline Caches. Game Mode often hangs on TotK because it tries to compile 5,000+ shaders at once on a fresh launch and the Steam Deck's "Gamescope" compositor thinks the app has crashed and kills it. The Brutal Truth You're seeing an empty folder because the AppImage likely doesn't have "write" permissions to that specific directory in SteamOS, so it "simulated" the install into a temporary memory cache that it can't clear. Rename the folder as suggested in Step 2. It takes 2 minutes and is the only way to guarantee that "ghost" update isn't being called by the emulator during the Game Mode boot sequence. Do you want the exact path to where your save files are so you don't lose your TotK progress when you reset the folder?
