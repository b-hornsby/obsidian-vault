---
id: 835468
source: GEMINI
date: 2026-01-20
tags: ['rom-filename', 'naming-convention', 'switch-roms']
category: homelab
sentiment: curious
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is asking about the meaning of '1g+1u' in a ROM filename.
---
# in the filename it says 1g+1u?

### USER
in the filename it says 1g+1u?

### GEMINI
In the world of Switch scene tools, "1G+1U" is shorthand for "1 Game + 1 Update." It is SAK's way of confirming that the merge was successful. It has taken your base game (1G) and fused it with your update (1U) into a single container. You might also see "1G+1U+1D" if you had included a DLC. What this means for your Steam Deck This is the "Golden File" you’ve been trying to create. Because the game and update are now one single entity, you have eliminated the "handshake" lag that was causing Game Mode to crash. The Final Setup (Do not skip these steps) To ensure this actually works when you switch back to Game Mode, you must "clean the house" first: 1. Eliminate the "Ghost" Update Citron is likely still trying to load the old .nsp update from its internal memory (NAND), which will conflict with your new merged file. Open Citron in Desktop Mode. Right-click Tears of the Kingdom > Remove > Remove All Installed Contents. Note: This does NOT delete your save games. It only wipes the update files from the emulator's internal folders. 2. Swap the Files Move your old, unpatched .xci and the .nsp update file out of /home/internal_games and into a backup folder (or delete them). Place your new "1G+1U" file into /home/internal_games. Rename it to something clean like ZeldaTotK_1.4.1.xci. (Avoid symbols like + in the filename, as Steam ROM Manager sometimes chokes on them). 3. Refresh Steam ROM Manager Since you have a new file with a new name, the old Steam shortcut is now pointing to a dead link. Open Steam ROM Manager. Click Settings > Remove all added app entries. Go to Parsers, click Parse, and then Save to Steam. 4. The "Exclusive Fullscreen" Check Before you leave Desktop Mode, open Citron one last time and ensure the game boots to the title screen. Check the Version column in Citron. It should say 1.4.1. In Emulation > Configure > Graphics, ensure it is set to "Exclusive Fullscreen". The Moment of Truth Go back to Game Mode and launch the game. Why this should finally work: Previously, Game Mode was timing out because the CPU was trying to do three things at once: launch the emulator, find the update in the NAND, and apply it to the base ROM. By using the 1G+1U file, you've done all that work ahead of time. The Deck now only has to do one thing: open one file. If it launches and you see "1.4.1" on the game's title screen, you've won. Would you like me to show you how to check your save file compatibility, or are you ready to jump back into Hyrule?
