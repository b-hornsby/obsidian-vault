---
id: 840655
source: GEMINI
date: 2026-01-21
tags: ['appimage', 'game-pathing', 'command-line-arguments', 'linux-gaming', 'steam-deck']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is describing the target path, which includes the AppImage location and the game path with specific arguments.
---
# The target it just shows where the app image is and then where the game is for that particular game with -f -g in between those two paths

### USER
The target it just shows where the app image is and then where the game is for that particular game with -f -g in between those two paths

### GEMINI
The "-f -g" arguments stand for fullscreen and game path. Since Steam is hanging on "Launching," it means the terminal command is essentially yelling at a wall. Because you manually merged the files with SAK, Steam ROM Manager is likely creating a command string that the Linux shell can't parse—usually because of a single missing quotation mark or a hidden character in the filename. The "Surgical" Fix Don't re-parse again. We’re going to fix the shortcut manually to prove it works. Go to Desktop Mode. Open Steam and find your Tears of the Kingdom shortcut. Right-click it -> Properties. Look at the Target field. It should look something like this: "/path/to/yuzu.AppImage" -f -g "/path/to/game.xci" Check for these 3 specific "Silent Killers": The Triple Quote: If your path looks like ""/path/to/game"" (double quotes on both ends), Steam will hang forever. It must be exactly one set of quotes. The "Start In" Field: This should only be the folder path of the emulator, without quotes. If there are quotes in "Start In," the launch will fail. The SAK Suffix: If SAK named your file something like TOTK (Update 1.2.0).xci, the parentheses often break the Linux command line if not perfectly quoted. Action: Rename the file to totk.xci. Update the "Target" path in Steam to match. If that doesn't work: The "Proton" Trap Check the Compatibility tab in that shortcut's properties. Is "Force the use of a specific Steam Play compatibility tool" checked? * UNCHECK IT. * Because you are launching a Linux AppImage, trying to run it through Proton (which is for Windows apps) will cause an infinite "Launching" loop because Proton is trying to "translate" a file that's already native to Linux. The Advisor's Cold Truth You're treating the symptom (the infinite launch) instead of the disease (the messy file pathing). By using SAK and manual parsing, you've created a "custom" setup that EmuDeck's automation no longer understands. Try this test: Inside the Steam Shortcut properties in Desktop Mode, copy the entire Target line. Open a terminal (Konsole) and paste it there, then hit Enter. If the game launches, the problem is a Steam UI bug. If the terminal says "File not found" or "Command not found," you have a typo in your path. Should I show you exactly what the "Target" and "Start In" lines should look like based on your specific file paths?
