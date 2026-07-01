---
category: general
date: 2026-01-21
id: 982926
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is indicating that previous troubleshooting attempts have not resolved
  the issue.
tags:
- troubleshooting
- linux-gaming
- steam-deck
- emulation
---
# None of these are the problem

### USER
None of these are the problem

### GEMINI
If none of those are the problem, then we are looking at a file system lock or a zombie process. If the paths are perfect, the quotes are correct, and Proton is disabled, but Steam still hangs on "Launching," it means the operating system thinks the emulator is already running or the file is "in use" by another process. This is common when a previous "brick" or crash didn't close the emulator properly. 1. The "Zombie" Process Steam won't launch a second instance of a shortcut if it thinks the first one is still alive. The Action: In Desktop Mode, open System Monitor (search for it in the start menu). Look for any process named yuzu, ryujinx, or AppImage. Kill them all. Why: If a background process is hung, Steam sends the "launch" command, it hits the hung process, and just sits there waiting for a "ready" signal that never comes. 2. The "NAND" Lock (The most likely candidate) When you use SAK-merged files, the emulator sometimes tries to create a virtual filesystem entry for it. If you previously had the update installed via the emulator's NAND (the "Update Manager"), there might be a lock file or a corrupted metadata entry in the emulator's internal folder that is conflicting with your new "all-in-one" file. The Action: 1. Open the emulator (Yuzu/Ryujinx) directly in Desktop Mode. 2. Does the game appear in the list? If so, does it show the correct version number? 3. Right-click the game -> Open Transferable Pipeline Cache. Delete everything in that folder. 4. Right-click the game -> Open Mod Data Location (check if there's anything old there and move it out). 3. The SD Card "Mount" Permission Since your file is on a linked folder on the SD card: The Problem: SteamOS sometimes mounts SD cards with "noexec" permissions or the symlink has lost its "execute" bit during the reparse/initialization. The Test: In Desktop Mode, navigate to the actual file on the SD card (not the link). Right-click it -> Properties -> Permissions. Is "Is Executable" checked? If not, check it. The Reality: If Steam can't "execute" the path because the SD card is acting as "read-only" or "storage-only," it will hang at "Launching" forever. 4. The "AppImage" vs. "Script" Conflict Did you point Steam ROM Manager to the AppImage or to a .sh script? If you pointed it to the AppImage, it might be missing the environment variables EmuDeck sets up to make the SD card readable. The Fix: Ensure the Target points to the EmuDeck launch script (usually in ~/Emulation/tools/launchers/) rather than the raw emulator file. The Advisor's Bottom Line If you are 100% certain the paths and syntax are correct, then the file itself is failing a checksum or a permission check. Try this: Move that one game file from the SD card to the Steam Deck's internal SSD (the home/deck/Emulation/roms/nswitch folder). If it launches from the SSD, your SD card's symlink or file system is the bottleneck. If it still doesn't launch from the SSD, the SAK-merged file is internally corrupted in a way that the emulator's command-line interface can't handle. Which emulator are you using, and did you point the "Target" to the AppImage or a script?
