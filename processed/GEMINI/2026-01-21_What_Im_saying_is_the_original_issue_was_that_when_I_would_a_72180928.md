---
category: homelab
date: 2026-01-21
id: 092135
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is explaining the history of his game update issues and how he used
  SAK as a workaround, but now he has to manually select the game each time.
tags:
- game-updates
- switch-army-knife
- sak
- emulation-station
- game-launching
- steam-deck
---
# What I’m saying is the original issue was that when I would apply an update to any switch game via the update manager it would brick the setup and I’d have to reinitialize everything. The work around was to use SAK to apply the update to the file itself and have the emulation station stuff read that file instead so it’s all in one. Now when I launch the game in game mode it launches but I have to manually pick the game again to play it. Before, I would just pick the game and it would launch it no issue. I haven’t changed anything pathing so I know that’s not the issue

### USER
What I’m saying is the original issue was that when I would apply an update to any switch game via the update manager it would brick the setup and I’d have to reinitialize everything. The work around was to use SAK to apply the update to the file itself and have the emulation station stuff read that file instead so it’s all in one. Now when I launch the game in game mode it launches but I have to manually pick the game again to play it. Before, I would just pick the game and it would launch it no issue. I haven’t changed anything pathing so I know that’s not the issue

### GEMINI
That context changes everything. You aren't dealing with a file corruption issue; you’re dealing with a launch argument mismatch caused by your manual SAK merger. When you use SAK to merge an update into a base file (creating a single .xci or .nsp), you change the file's identity and how the emulator handles it. The reason you're seeing the emulator menu instead of the game is that EmulationStation (ES) is sending a command to "Open [Old File Name]," but since you’ve replaced it with a merged file, the emulator doesn't recognize the direct path or the metadata has shifted. It defaults to the "Home" screen because the specific "Launch Game" command failed. Stop trying to delete files to "rewrite" them. That won't fix a logic error in your launcher. Here is the brutal truth: your "workaround" solved the update-brick issue but broke the automation. Why it's happening Metadata Change: SAK-merged files often have different internal headers. The emulator might see it as a new entry. File Extension/Pathing: If your SAK output has a different extension (e.g., you turned an .nsp into an .xci) or a slightly different name, ES is passing an invalid argument to Yuzu/Ryujinx. The "Launch" Command: ES-DE uses a script (usually yuzu.sh or ryujinx.sh) that tells the emulator: -g "path/to/game". If that path is even one character off or the file is "busy" being scanned as a new title, it drops you at the menu. The Precision Plan to Fix Automation 1. The "Clean Slate" Parse (Most Likely Fix) Since you changed the files themselves, EmulationStation’s cache is pointing to ghosts. Go to Desktop Mode. Open Steam ROM Manager. Remove all previously added Switch entries (Toggle them off or use the "Remove" option). Re-run the parser. Ensure it finds your new SAK-merged files. Save to Steam. This refreshes the launch arguments that ES-DE and Steam use to talk to the emulator. 2. Reset the Emulator Configuration in EmuDeck Since your updates were "bricking the setup," there’s a high chance your emulator config is bloated with conflicting paths for those updates. Open the EmuDeck app in Desktop Mode. Go to Manage Emulators. Select the emulator you’re using (Yuzu or Ryujinx) and click Reset Configuration. Note: This will not delete your saves, but it will wipe your custom graphics settings. You must do this to clear the pathing errors causing the "brick." 3. Check the "Alternative Emulator" Setting If you have both Yuzu and Ryujinx, ES-DE might be confused about which one should handle the new merged file. In EmulationStation, highlight Tears of the Kingdom. Press Menu (Start) -> Game Settings -> Per Game Settings. Check Alternative Emulator. Manually set it to the specific one you want (e.g., "YUZU (Standalone)" or "RYUJINX"). 4. The Nuclear Pathing Check If it still drops you into the menu, your file name has a character the Linux terminal hates (like brackets or special symbols from the SAK output). Rename the game file to something dead simple: TOTK_Merged.xci. Re-parse in Steam ROM Manager. Do you want me to show you how to check the launch logs in Desktop Mode to see exactly what error the emulator is throwing when it fails to auto-launch?
