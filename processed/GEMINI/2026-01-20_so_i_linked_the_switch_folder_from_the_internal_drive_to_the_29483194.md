---
id: 012324
source: GEMINI
date: 2026-01-20
tags: ['steam-rom-manager', 'symlink', 'rom-path', 'reparse-steam']
category: homelab
sentiment: building
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan needs help unparsing and re-parsing Steam ROM Manager entries after moving Switch ROMs from SD card to internal drive via symlink.
---
# so i linked the switch folder from the internal drive to the sd card for switch games only. how do i unparse the ones i had in steam when they were on the sd card and how do i reparse them so they are pointed at the new location

### USER
so i linked the switch folder from the internal drive to the sd card for switch games only. how do i unparse the ones i had in steam when they were on the sd card and how do i reparse them so they are pointed at the new location

### GEMINI
To fix your Steam Library, you need to flush the old "ghost" paths and re-scan so the shortcuts point to your new internal drive locations. If you don't do this, clicking a game in Steam will result in an error because it’s still looking for the file on the SD card. Here is the exact process to "unparse" and "reparse" without affecting your other games. 1. The "Unparse" (Removing Old Entries) Steam ROM Manager (SRM) has a built-in "Nuclear Option" for specific parsers. This is the cleanest way to wipe the old Switch links from Steam. Close Steam entirely. If Steam is open, SRM cannot modify your library. Open Steam ROM Manager (via EmuDeck or Desktop Mode). On the left-hand list, ensure only the Switch parser (e.g., Yuzu or Ryujinx) is toggled ON (green). Toggle all others OFF for now so you don't accidentally mess with your other systems. Click Preview at the top. Click Parse. This will show your Switch games. Look for a button at the bottom labeled "Remove from Steam". Click it. Note: This only deletes the shortcuts in Steam; it does NOT delete your ROMs. Check the "Event Log" tab. It should say "Done removing entries." 2. The "Reparse" (Adding the New Paths) Now you need to tell SRM where the games moved to. Stay in Steam ROM Manager. Go back to the Parsers tab on the left. Select your Switch parser (Yuzu/Ryujinx). Look for the field labeled "ROMs Directory". Click the folder icon and navigate to your Internal Drive folder where you moved the games (e.g., /home/deck/Internal_Games/switch/). Click Save at the bottom of the parser settings. Go back to Preview, click Parse, and verify the games show up. Click Save to Steam (or "Add Games"). Pro-Tip: The "Exception" Safety Net If you have some games on the SD card and some on the internal drive, and you want SRM to see both, you have two choices: The Symlink Method (Recommended): Since you already made a symlink, you can actually keep the SRM path pointed to the SD card folder. Because of the symlink, SRM will follow that "shortcut" into your internal drive and find the games automatically. The Manual Method: If the symlink isn't working for SRM, you can duplicate the Switch parser in SRM, naming one "Switch Internal" and one "Switch SD," each pointing to their respective folders. What about EmulationStation? You don't need to do anything for EmulationStation. Since you created a symlink (the shortcut folder) on the SD card, ES-DE will open that folder, follow the link to your internal drive, and display the games exactly as it did before. Would you like me to help you verify the folder paths in the Linux terminal to ensure your symlink is correctly "handshaking" with the internal drive? Cleaning up Steam ROM Manager entries This video is useful because it demonstrates how to troubleshoot and reset parsers in Steam ROM Manager when games aren't appearing or paths have changed.
