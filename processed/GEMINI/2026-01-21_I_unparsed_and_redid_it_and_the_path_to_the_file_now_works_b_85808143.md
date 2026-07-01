---
category: homelab
date: 2026-01-21
id: 693167
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated because after fixing the file path, the game is now stuck
  in an infinite loading loop, which wasn't happening before.
tags:
- steam-rom-manager
- srm-configuration
- pathing-issues
- infinite-loading
- emulation-station
---
# I unparsed and redid it and the path to the file now works but now it’s doing that infinitely loading thing and it wasn’t doing that a second ago when I was having to manually select it a second time?

### USER
I unparsed and redid it and the path to the file now works but now it’s doing that infinitely loading thing and it wasn’t doing that a second ago when I was having to manually select it a second time?

### GEMINI
The infinite loading screen you're seeing now is the final hurdle in your "franken-file" strategy. Because you used SAK to merge the update, the file's internal structure has changed. When you launch it via Steam/EmulationStation, the emulator is trying to apply its own logic (like looking for shaders or verifying the file hash) while Steam is simultaneously trying to overlay its "Game Mode" wrapper. Here is the brutal, objective reality: The reason it worked when you "manually selected it" but fails when "auto-launched" is that the manual selection gives the emulator time to initialize, whereas the auto-launch command is slamming into a wall of metadata it doesn't expect. 1. The Most Likely Culprit: Shader Cache Conflict When you merged the update into the base file, you technically created a "new" game in the eyes of the emulator. It is likely trying to build a brand new shader cache from scratch. In Game Mode, this often looks like an infinite spinning logo because the "Shaders Compiling" window is hidden behind the Steam UI. The Fix: Go to Desktop Mode, open your emulator directly, and launch the game. Let it sit on that loading screen. If it's shaders, you'll see a progress bar. Wait for it to reach the menu. Once it has booted once in Desktop Mode, it should bypass the "infinite" load in Game Mode. 2. The "NAND" Ghost Issue You mentioned that the original issue was the "Update Manager" bricking things. This happens because the emulator stores update data in a specific folder (the nand). Even though you've now merged the update into the .xci or .nsp, the emulator might still be trying to look in its nand folder for the old update info, causing a logic loop. The Action: 1. Open the emulator in Desktop Mode. 2. Right-click Tears of the Kingdom. 3. Select "Remove" -> "Remove All Pipeline Caches" (This is safe). 4. Select "Manage Title Updates" and make sure nothing is checked. Since it’s merged, you don't want the emulator trying to "double-patch" it. 3. Disable the "Steam Wake Movie" (Odd but frequent Deck Bug) There is a known bug where custom "Wake Movies" or "Boot Animations" cause non-Steam shortcuts (like your Switch games) to hang on an infinite loading screen. The Action: Go to Settings -> Customization and turn off "Use as Wake Movie" if you have it on. 4. The "Pathing" Double-Check If it still won't load, look at the file name you created with SAK. If it has brackets, parentheses, or spaces (e.g., TOTK [Update 1.2.0].xci), the Steam launch argument might be breaking at the first special character. The Action: Rename the file to TOTK.xci. Re-parse in Steam ROM Manager. Try again. The Advisor’s Bottom Line You've spent a lot of time "working around" the system with SAK. Every time you add a layer of manual merging, you move further away from the "standard" EmuDeck setup, which is why your automation is breaking. Would you like me to show you how to find the specific log file for your emulator so we can see the exact line of code where it's hanging?
