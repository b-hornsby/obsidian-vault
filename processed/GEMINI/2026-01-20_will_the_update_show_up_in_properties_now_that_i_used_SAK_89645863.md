---
category: homelab
date: 2026-01-20
id: 652760
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking if using Switch Army Knife (SAK) to apply an update will
  make the update visible in the game's properties.
tags:
- switch-army-knife
- sak
- game-updates
- rom-properties
- emulation
---
# will the update show up in properties now that i used SAK?

### USER
will the update show up in properties now that i used SAK?

### GEMINI
When you use SAK to merge an update into a base file, the behavior in Citron changes. Here is the direct, technical breakdown of what you will see. 1. Will it show in Properties? No, not as an "Add-on" or "Patch" checkbox. When you install an update to the NAND, Citron sees the base game and a separate patch file, allowing you to toggle the update on and off in the properties menu. Once merged with SAK, the Base Game IS the Update. Citron will see the file and display the Game Version (e.g., 1.4.1) directly next to the game title or in the "Version" column of the main list. If you right-click > Properties, the "Add-ons" tab will be empty because the update is no longer an "added" file—it's part of the core .xci. 2. How to Verify It Worked Before you waste time in Game Mode, verify the merge in Desktop Mode: Open Citron. Look at the Tears of the Kingdom entry in your list. Check the Version column. It should explicitly state 1.4.1. If it still says 1.0.0, the merge failed or you are still pointing Citron to your old, unpatched file. 3. The Clean Up (Crucial Step) If you don't do this, Citron might get confused by "ghost" files: Delete the old NAND update: Right-click the game > Remove > Remove All Installed Contents. This wipes the old .nsp update you installed to the NAND earlier. Why? If you have a merged 1.4.1 file AND a 1.4.1 patch in your NAND, the emulator will try to patch a patch. This is exactly the kind of resource loop that causes the Steam Deck's Game Mode to crash. 4. Steam ROM Manager Refresh Since the filename of your merged file is likely different (or the internal metadata has changed), you must re-run SRM: Move the old .xci and the .nsp update file out of your internal_games folder (put them in a backup folder elsewhere). Put only your newly patched .xci in the internal_games folder. Run Steam ROM Manager > Parse > Save. The Advisor's Final Strategy By merging the files, you have removed the "NAND bottleneck." When you hit "Play" in Game Mode, the Deck now only has to open one single file. If it boots in Desktop and shows "1.4.1" in the version column, but still crashes in Game Mode, then we have 100% confirmed it is a Graphics/Resource hang. At that point, your next move is to go into the Steam "..." Performance menu while the game is "launching" and ensure your Manual GPU Clock is set to 1200MHz to give the CPU the power it needs to decompress that merged 1.4.1 file. Would you like me to wait while you run the SAK merge, or do you need the specific terminal command to check if your Citron configuration is still looking for the old NAND files?
