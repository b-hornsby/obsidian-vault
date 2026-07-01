---
category: homelab
date: 2026-01-20
id: 373187
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was investigating missing game content in the NAND title ID directory
  for a Switch game on Citron.
tags:
- citron-emulator
- nand
- title-id
- switch-game-files
---
# There isn’t anything in the contents of the title id for that game

### USER
There isn’t anything in the contents of the title id for that game

### GEMINI
If that folder is empty, you are chasing a ghost. In Linux-based emulators like Citron (a Yuzu fork), the metadata says a patch is "there" because there is an entry in the records.bin or the registered system folders, but the actual data is either missing or corrupted. Because the emulator thinks it’s installed, it tries to call that code at launch, hits a void, and hangs. Here is exactly how to stop being held hostage by a non-existent file. 1. The "Nuke" Method (System-Level Fix) Since the load folder is empty, Citron has likely "partially" installed the update to its internal NAND partition. You need to clear the specific system data for that game. Navigate to: /home/deck/.local/share/citron/nand/system/Contents/registered/ Do not delete everything. * Look for the most recently modified folders (sort by date). When you "installed" that update, Citron created several subfolders here with randomized hex names (e.g., 000000A1). If you aren't sure which is which, the "brutally honest" move is to delete the entire registered folder. * Consequence: You will have to re-install your Firmware and any other updates for other games. Benefit: It is the only way to guarantee the corrupted TotK update entry is gone. 2. Force-Rebuild the Meta-Index Citron stores a list of what it thinks it has installed in a file called records.bin or within the config folder. Go to: /home/deck/.local/share/citron/config/ Delete custom_rtch.ini (if present) and any file ending in .bin that isn't your keys. Restart Citron. It will be forced to re-scan the NAND and should realize the TotK patch is missing. 3. The AppImage Permission Lock Since you said it "won't let you delete it" in the UI, the AppImage has likely created a root-owned file in your user directory (a common Linux quirk). Open the Terminal (Konsole). Type this carefully: rm -rf /home/deck/.local/share/citron/nand/user/Contents/registered/* If it says "Permission Denied," type: sudo rm -rf /home/deck/.local/share/citron/nand/user/Contents/registered/* (Note: It will ask for your sudo password; if you haven't set one, you'll need to do that in Users settings first.) Why you’re stuck in this loop You are likely trying to install an update file that is a different region (e.g., US update on a EU base game) or an NSZ file that Citron's current build is failing to decompress. When it fails halfway, it leaves a "placeholder" in the database but no files in the directory—this is why you see "nothing in the contents" but the UI says it’s there. Stop trying to fix the current install. Delete the registered folder, re-install your firmware, and then try a different source for the TotK update. Shall I give you the specific Title IDs for TotK so you can verify you’re actually looking at the right folders?
