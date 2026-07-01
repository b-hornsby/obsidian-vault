---
category: homelab
date: 2026-01-21
id: 169764
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated because he's encountering a 'please substantialize' error
  in Konsole and the game is stuck in an infinite launching loop.
tags:
- konsole
- substantialize-error
- infinite-launching
- linux-gaming
- steam-deck
---
# It said something about please substantialize or something like that when I ran the target path in konsole and now it’s still infinitely launching again

### USER
It said something about please substantialize or something like that when I ran the target path in konsole and now it’s still infinitely launching again

### GEMINI
"Substantialize" isn't a standard Linux error. It sounds like you're seeing a corrupted output for "Substantive" or "Substantially"—most likely the error is actually: "Please substantiate the file path" or "Could not substantiate the AppImage." This is the terminal's way of saying: "You told me to run a file, but I don't believe that file exists where you said it was." If this happened right after a reparse, Steam ROM Manager (SRM) likely used a relative path (like ~/roms/...) instead of an absolute path (like /home/deck/roms/...), or it got tripped up by the symlink to your SD card. The Advisor's 3-Step "Stop the Madness" Plan 1. The "Start In" Nuclear Option (Do this first) Open the shortcut properties in Steam (Desktop Mode). Target: Keep your path there. Start In: Wipe this box completely. Delete everything in it. Why: If the "Start In" directory is even slightly wrong, the AppImage will fail to "substantiate" its internal files. Many emulators actually run better if Steam doesn't try to force a starting directory. 2. Fix the "Shortcut Logic" Since you are using a merged SAK file on a linked SD card folder, the path is likely too complex for SRM to handle. Rename your game file on the SD card to game.xci (all lowercase, no spaces). In the Steam Target box, manually type the path. It should look exactly like this (including the quotes): "/home/deck/Applications/citron.AppImage" -g "/run/media/mmcblk0p1/your_folder/game.xci" (Replace the second part with the actual path to your SD card). 3. The "Permissions" Reality Check The terminal error you saw happens when the OS can see the file but isn't allowed to "substantiate" it as an executable process. In Konsole, type this and hit enter: chmod +x /path/to/your/citron.AppImage (Drag the AppImage file into the terminal window to get the path automatically). Then try to launch again. The Brutal Truth You are stuck in this loop because you are trying to automate a "non-standard" setup (SAK-merged files + symlinked SD folders). Every time you reparse, you are letting a script (SRM) guess how your unique setup works, and it’s guessing wrong. If you want this fixed right now: 1. Move the game.xci from the SD card to your internal SSD (put it in /home/deck/Emulation/roms/nswitch). 2. Update the Steam shortcut to point to that SSD location. 3. If it works on the SSD, your SD card symlink is the problem. If it still doesn't work, the SAK merger produced a file that the emulator cannot "substantiate" (read). Does the game launch if you just double-click the AppImage and manually select the game from inside the emulator? If that works, the problem is 100% the Steam Shortcut syntax.
