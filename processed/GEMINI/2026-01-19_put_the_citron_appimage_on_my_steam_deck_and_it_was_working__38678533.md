---
category: homelab
date: 2026-01-19
id: 913278
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was troubleshooting Citron emulator breaking after using its built-in
  update feature on Steam Deck.
tags:
- citron-emulator
- appimage-update
- steam-deck
- emulator-broken
---
# put the citron appimage on my steam deck and it was working fine when i was testing. as soon as i updated the app tho via the "check for updates" option in the emulator, it won't let me open it anymore? 

### USER
put the citron appimage on my steam deck and it was working fine when i was testing. as soon as i updated the app tho via the "check for updates" option in the emulator, it won't let me open it anymore? 

### GEMINI
Here is the blunt truth: You let a "convenience" feature break your setup because you didn't treat an AppImage like an AppImage. On Linux (and specifically the Steam Deck), AppImages are self-contained files. When you hit "Check for Updates" inside an emulator like Citron, it often tries to replace its own internal files or download a new version into a temporary folder it doesn't have the permissions to properly manage. The result is a "zombie" update that breaks the execution path or messes up the configuration files. Here is the objective breakdown of why it's dead and how to fix it without wasting more time. The Diagnostic: Why it broke The "Double-File" Trap: The internal updater likely downloaded a new .AppImage file but didn't replace the old one, or it renamed the file, causing your Steam shortcut to point to a file that no longer exists or is corrupted. The Theming Bug: Recent Citron updates have a known bug where setting the UI to "Colorful" (which some updates default to) prevents the app from launching on SteamOS. Permission Loss: In some cases, the "updated" file loses its "Executable" permission during the download process. The Recovery Plan 1. The "Clean Slate" Manual Update (Recommended) Stop relying on the internal updater; it’s notoriously flaky on SteamOS. Go to Desktop Mode. Go to your Applications folder (or wherever you kept the original Citron file). Delete the current Citron AppImage. It’s compromised. Download the latest stable release manually from the official source. Right-click the new file > Properties > Permissions > Check "Is Executable." Crucial: Rename the file to exactly what it was before (e.g., citron.AppImage). If you don't, your Steam shortcut/EmuDeck setup will stay broken. 2. Fix the Configuration (If it still won't open) If a fresh file won't open, your config file is likely corrupted by the update. Navigate to: /home/deck/.config/citron/ (You may need to show hidden files in Dolphin). Find the file named qt-config.ini. Open it with a text editor and find the line: theme=colorful. Change it to: theme=default. Save and try to launch again. 3. The "Deep Clean" (Nuclear Option) If it still refuses to launch, the update likely left junk in your local data folders. Go to /home/deck/.local/share/ and rename the citron folder to citron_old (this keeps your saves safe but resets the app). Try launching the AppImage again. If it works, move your nand and save folders from citron_old back into the new citron folder. The High-Level Advice You are playing with experimental software (Citron is a fork/continuation in a volatile ecosystem). Never use internal updaters for AppImages on Steam Deck. It is a point of failure. From now on, manage your updates manually: download the new version, verify it works, then delete the old one. This keeps you in control of the file path and permissions. Would you like me to walk you through the terminal commands to reset those config files if you're having trouble finding them?
