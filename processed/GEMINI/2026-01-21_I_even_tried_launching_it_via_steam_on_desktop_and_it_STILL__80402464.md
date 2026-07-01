---
category: homelab
date: 2026-01-21
id: 838217
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated that a game is not launching, even when launched via
  Steam on desktop mode.
tags:
- steam-launching
- linux-gaming
- steam-deck
- troubleshooting
---
# I even tried launching it via steam on desktop and it STILL says launching like this

### USER
I even tried launching it via steam on desktop and it STILL says launching like this

### GEMINI
If it's hanging on "Launching" even in Desktop Mode, the handoff between Steam and the emulator is physically broken. Steam thinks it’s doing its job, but the command it's sending is hitting a dead end. Since you confirmed this happened immediately after a reparse, SRM likely messed up the executable permissions or the syntax of the link itself. The "Brutally Honest" Fixes You need to stop trusting Steam ROM Manager for a second and verify the actual chain of command. Check the Executable Bit: When SRM creates a new shortcut, it sometimes points to an AppImage or script that lost its "permission to run" during the file shuffle. Go to the emulator file (the .AppImage) in your file manager. Right-click > Properties > Permissions. Ensure "Is executable" is checked. If it isn't, Steam will say "Launching" forever because it doesn't have permission to start the program. The "Target" syntax check: Open the shortcut properties in Steam. If the "Target" looks like this: "/path/to/yuzu.AppImage" -f -g "/path/to/game.xci" ...try removing the -f. Sometimes a specific update to an emulator makes the "fullscreen" flag hang the launch if the shader cache is being rebuilt. The "Start In" Field: Look at your "Start In" field. If it is blank, or if it points to the SD card but the emulator is on the SSD, it will hang. It should point to the folder containing the emulator. The Ultimate Diagnostic To find out exactly why it's hanging, we have to bypass the Steam UI: Open Konsole (Terminal) in Desktop Mode. Copy the entire text from the "Target" box in your Steam shortcut. Paste it into Konsole and hit Enter. What happens? If it launches: The problem is a Steam UI glitch (likely a "Compatibility" tool or "Steam Play" setting being forced). If it says "No such file or directory": Your reparse used an old or slightly incorrect path. If it says "Permission denied": You need to right-click the AppImage and make it executable. Which error did the Konsole (terminal) give you when you pasted the target line?
