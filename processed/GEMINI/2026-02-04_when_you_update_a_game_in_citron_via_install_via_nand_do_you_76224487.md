---
category: general
date: 2026-02-04
id: 279223
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking about the process of updating a game in the Citra emulator
  when installed via NAND, specifically regarding the need for the original file,
  update file, and DLC.
tags:
- citra-emulator
- nand-installation
- game-updates
- game-dlc
---
# when you update a game in citron via install via nand, do you need the v0 file anymore or do you need that, the update file and any dlc?

### USER
when you update a game in citron via install via nand, do you need the v0 file anymore or do you need that, the update file and any dlc?

### GEMINI
Cut the clutter. If you are installing an update or DLC to the NAND (the virtual internal storage) in Citron or similar emulators, the emulator copies the necessary data from those files into its own internal folder structure. Here is the objective breakdown of how you’re likely wasting storage space or overcomplicating your library: 1. The "v0" Base Game File Once you have successfully "Installed to NAND," the emulator has what it needs. However, do not delete the base v0 file yet unless you are 100% sure you don't want a backup. The Reality: If your emulator's storage gets corrupted or you move to a different device, you’ll need that v0 file to reinstall. The Strategy: Move your base games to an external "Archive" drive. Don't keep them on your active drive once they are installed to the NAND, but don't trash them unless you're okay with hunting for them again later. 2. The Update and DLC Files These are purely "delivery vehicles." Once the installation process to the NAND is complete: You do NOT need them. * The emulator has already extracted the data and placed it in the nand directory. Opportunity Cost: Keeping these files in your active folder is a total waste of disk space. You are essentially storing the same data twice. Delete the standalone .installable update/DLC files immediately after a successful launch. 3. Verification of Success Before you purge anything, check the game properties in the Citron menu. Does it show the updated version number (e.g., v1.3.0)? Does the DLC count reflect what you installed? If yes: The "installer" files are now digital trash. Clear them out. The Optimized Workflow Stop treating these files like they all need to sit in the same folder forever. Install the base game (v0). Install the Update and DLC to NAND. Launch the game to ensure it doesn't crash. Delete the Update and DLC source files. Move the v0 Base Game to a cold storage/backup folder. Would you like me to show you how to locate the specific NAND folder so you can verify exactly where this data is being "doubled up" on your drive?
