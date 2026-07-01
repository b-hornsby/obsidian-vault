---
category: homelab
date: 2026-01-21
id: 769258
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is emphasizing that the setup was working perfectly before he re-parsed
  it, even with the update.
tags:
- steam-rom-manager
- srm-configuration
- reparse-issue
- game-updates
- emulation-station
---
# THIS WAS ALL WORKING LITERALLY RIGHT BEFORE I REPARSED, even with the update

### USER
THIS WAS ALL WORKING LITERALLY RIGHT BEFORE I REPARSED, even with the update

### GEMINI
I understand the frustration. It’s infuriating when a system that was working perfectly breaks purely because you refreshed the list. If it worked literally seconds before the reparse, then the emulator, the file, and the update are fine. The only thing that changed is the handshake between the Steam UI and the file. Since you've already verified the pathing syntax, here is exactly what happened: When you reparsed, Steam created a brand new shortcut entry in your library. Even if it looks identical to the old one, Steam treats it as a different entity with different "Cloud" and "Shader" states. 1. The "Hidden Window" Hang This is the #1 cause of infinite "Launching" screens on the Deck. When Steam launches a non-Steam game, it looks for the first window the application opens. Because you merged the update with SAK, the emulator might be throwing a tiny "Verifying File" or "Shader Migration" popup that you can't see in Game Mode. Steam waits for that popup to close before it shows the game, but since you can't see it, you can't close it. The Fix: Go to Desktop Mode and launch the game via the Steam Shortcut there. If a little box pops up saying "Update detected" or "Integrity check," click "OK" or "Don't show again." Once that's cleared in Desktop, Game Mode will work. 2. The "Double-Quote" SRM Bug Steam ROM Manager (SRM) has a persistent bug where it occasionally adds an extra set of quotation marks to the "Target" or "Start In" fields during a reparse. Check this specifically: In the shortcut properties, look at the Start In field. It should look like /home/deck/Applications/ (no quotes). If SRM put "/home/deck/Applications/" (with quotes), the launch will hang on "Launching" forever. Target Field: Ensure it doesn't have "nested" quotes like ""/path/to/game"". 3. The "Compatibility" Ghost When SRM creates a new shortcut, Steam sometimes tries to be "helpful" and assigns a Proton version to it automatically (especially if it's an .xci or .nsp which Steam doesn't recognize as native). The Fix: Go to the game in Steam -> Properties -> Compatibility. Ensure "Force the use of a specific Steam Play compatibility tool" is UNCHECKED. If it's checked, Steam is trying to run a Nintendo Switch file through a Windows translator, which results in an infinite launch loop. 4. The Steam Cloud/Shader "Stuck" State Steam often gets stuck "Checking for Updates" or "Downloading Shaders" for non-Steam shortcuts after a reparse. The Fix: In Game Mode, while it's saying "Launching," press the Steam Button -> Home. Look at the top of your screen. Is there a download icon or a "Shader Pre-Caching" bar moving? If so, cancel it or let it finish. Steam won't open the game until its background check (which is useless for an emulator) is done. The Advisor's Precision Strategy You said it was working right before the reparse. That means the issue is 100% within the Steam Shortcut settings. Delete the shortcut manually from your Steam library (Right-click -> Manage -> Remove non-steam game). Reparse one more time, but first, go into SRM settings and ensure the "Steam Directory" and "User Accounts" are correctly selected. The "Manual Test": Before doing anything else, go to Desktop Mode, open a terminal (Konsole), and paste your "Target" line there. If the game starts, then the issue is the Compatibility tab or Start In field in Steam. Does the "Start In" field currently have quotes in it? This is the most common silent killer after an SRM reparse.
