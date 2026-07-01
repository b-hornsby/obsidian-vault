---
id: 172554
source: GEMINI
date: 2026-01-20
tags: ['citron-emulator', 'game-update', 'version-1.4.1']
category: homelab
sentiment: frustrated
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is clarifying that the update version he is trying to apply is 1.4.1.
---
# i never said which update. the update is 1.4.1

### USER
i never said which update. the update is 1.4.1

### GEMINI
Actually, knowing it's Version 1.4.1 changes the entire diagnostic. As of late 2025 and early 2026, version 1.4.0 and 1.4.1 of Tears of the Kingdom were released primarily to support the "Switch 2" and higher-end localization. These specific updates changed the game's memory management and file structure in a way that is highly unstable on older Citron/Yuzu-based forks when running in Game Mode. If it works in Desktop but fails in Game Mode, you are hitting a Title ID vs. Metadata conflict that Game Mode cannot resolve on its own. The Brutal Solution: The "XCI" Pivot If you are using a .nsp update file on top of an .nsp base game, Citron is trying to "patch" the game live during the Game Mode launch. This is failing. The fix used by the community: Obtain a "Superdeck" or "Update Integrated" .xci file of version 1.4.1. Why: By using a single file where the update is already baked into the ROM, you bypass the "NAND check" that is currently causing your Game Mode crash. When you use an integrated file, Steam ROM Manager points to one single solid file, and the emulator doesn't have to look for patches in the NAND, which is where the Game Mode "handshake" is failing. If you want to keep your current files, do this EXACT manual fix: 1. The "Apostrophe" and Naming Check Steam ROM Manager (SRM) often fails if there are special characters in the title after an update. Rename your Base ROM file to exactly: ZeldaTotK.nsp (No spaces, no symbols). Re-parse in SRM. If the shortcut name in Steam has a : or ', it can cause an instant "Poof" back to home. 2. Force the "Portable" Home The reason it works in Desktop but not Game Mode is often a "Configuration Ghost." Go to your Citron folder in Desktop Mode. Create a new folder next to the Citron AppImage named user. This forces Citron to use a "Portable" configuration. You will have to move your nand, keys, and load folders from ~/.local/share/citron/ into this new user folder. Why this works: It centralizes everything so Steam doesn't have to look through hidden Linux directories to find your update. 3. The Version 1.4.1 "Handshake" Tweak In Citron (Desktop) > Properties for TotK > Graphics: Resolution: Set it to 1x (720p/1080p). Do not use 0.75x or any mods yet. Window-Adapting Filter: Set to Bilinear. Anti-Aliasing: None. TotK 1.4.1 has a high initial VRAM draw. If you have any scaling or AA turned on, the Game Mode session will kill the app before the screen turns on. The Reality Check You are trying to run the most recent, most demanding version of the game on a "Legacy" style setup. If it's an instant "poof" back to home: Your SRM shortcut is pointing to a file path that the Steam Deck's Game Mode doesn't have permission to see. If it's a 10-second spin then crash: The game is running out of memory because 1.4.1 is optimized for the Switch 2's larger RAM pool. The most "Direct Advisor" move here: Go back to Version 1.2.1. Version 1.4.1 offers almost zero performance benefits for the Steam Deck—it was mostly for Brazilian Portuguese support and Switch 2 compatibility. You are fighting a war for an update that gives you nothing but crashes. Would you like me to show you how to safely "Roll Back" to 1.2.1 without losing your 1.4.1 save data?
