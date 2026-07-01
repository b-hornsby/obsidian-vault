---
category: homelab
date: 2026-01-21
id: 282853
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is clarifying that the game is stuck on the 'launching' screen indefinitely
  after a reparse.
tags:
- game-launching
- infinite-launching
- steam-deck
- reparse-issue
- linux-gaming
---
# No I mean it will literally say “launching” for a LONG time and never actually launch. It wasn’t doing that before the reparse

### USER
No I mean it will literally say “launching” for a LONG time and never actually launch. It wasn’t doing that before the reparse

### GEMINI
When Steam sits on "Launching" indefinitely for a non-Steam shortcut, it means the Steam UI has handed the command to the OS, but the process has either crashed instantly or is hung waiting for a response that isn't coming. Since this started after the reparse, Steam ROM Manager likely created a shortcut with a broken "Target" or "Start In" path that doesn't match your manual SAK-merged file. 1. The "Pathing Trap" Check In Game Mode, go to your game -> Properties -> Shortcut. Look at the Target and Start In fields. The Problem: Steam ROM Manager often adds quotes incorrectly or misses a space when a file name changes. If you have any special characters (brackets, parentheses, or extra periods) in that SAK-merged filename, the launch argument is likely failing. The Fix: Rename your ROM to something incredibly simple like totk.xci. Reparse one last time. If there are no spaces or brackets, there's nothing for the terminal command to trip over. 2. The "Shaders are Background-Blocking" Issue When you launch a Switch game via a shortcut, the emulator often pops up a "Compiling Shaders" or "Verifying" window. In Game Mode, Steam tries to hide everything except the game window. If the emulator is waiting for you to click "OK" or is simply showing a progress bar, Steam will stay on the "Launching" screen forever because the actual game window hasn't appeared yet. The Test: Go to Desktop Mode and launch the game through Steam there. You will likely see an error message or a progress bar that was hidden in Game Mode. Once it clears in Desktop Mode, it will clear in Game Mode. 3. The Script Conflict (EmuDeck specific) EmuDeck shortcuts don't point to the game; they point to a script (like yuzu.sh) which then points to the game. If you manually moved or renamed files, that script might be pointing to the old location. The Fix: In Desktop Mode, open EmuDeck -> Manage Emulators -> [Your Emulator] -> Reset Configuration. This forces EmuDeck to rewrite the launch scripts to match the current file paths. 4. Storage "Ghosting" You mentioned a linked folder on an SD card. If the reparse happened while the SD card was even slightly unstable, Steam might have cached a "device ID" that is no longer matching. The Fix: Ensure your SD card is mounted. In Desktop Mode, open the folder where the ROM is. Right-click the ROM and select "Copy as Path." Go into Steam, find the shortcut properties, and paste that path into the Target field (make sure it's inside quotes). The Advisor's Verdict You're playing "Whack-A-Mole" because your file structure is non-standard. The "Launching" hang is almost certainly a syntax error in the Steam shortcut's target field. Check this now: In the Steam Shortcut properties for the game, does the "Target" path end exactly in .xci (or .nsp)? If there is any text after the extension, or if the path starts with /run/media/ but your SD card is mounted elsewhere, that is your "infinite launch." Would you like me to show you how to manually write the "Target" line so you can stop relying on the ROM Manager's broken parsing?
