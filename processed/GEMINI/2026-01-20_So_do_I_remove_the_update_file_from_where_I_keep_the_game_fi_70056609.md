---
category: general
date: 2026-01-20
id: 481559
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking whether he should remove the update file from the location
  where he keeps the game files when using the 'clean folder method'.
tags:
- steam-deck
- citron
- tears-of-the-kingdom
- game-update
- clean-folder-method
- file-management
---
# So do I remove the update file from where I keep the game file from the clean folder method?

### USER
So do I remove the update file from where I keep the game file from the clean folder method?

### GEMINI
Yes, you can move it or delete it once the installation is successful. Once you use the "Install Files to NAND" option, Citron makes a copy of that update and stores it inside its own internal folder structure (the nand folder we were looking at earlier). It no longer needs the original .nsp file to run the game with the update. The Tactical Move Do not delete it yet. Move it to a backup folder (like a "Downloads" or "Archive" folder) just until you verify the game works in Game Mode. Here is the exact sequence to finish this without a headache: Install to NAND (In Desktop Mode). Verify the Add-on: Right-click the game -> Properties -> Add-ons. Make sure the update is checked. The "Golden Boot": Launch the game in Desktop Mode. Look for the version number on the title screen (e.g., Ver. 1.2.1). Exit Citron. Move the original Update File: Take that .nsp file out of your game folder and put it somewhere else. Why? If it stays in the game folder, some versions of Citron/Yuzu forks might try to "double-load" it or get confused by the duplicate data, which can lead to—you guessed it—the loading hang you've been fighting. Switch to Game Mode and launch. Why you shouldn't leave it in the game folder Keeping the update file in the same folder as the base game while also having it installed to NAND is messy. It creates redundant paths. If Citron tries to read both at once, it can cause a metadata conflict that triggers the "infinite loading" screen in the Steam Deck's more restrictive Game Mode. A Warning on "Game Mode" Performance If you launch in Game Mode and see a black screen, be patient. Since you wiped the folder earlier, Citron has zero shaders. It has to build them from scratch for the updated version of the game. This can take 2 to 5 minutes on the first launch. If you kill the app because you think it's frozen, you might corrupt the database again. Try the "Golden Boot" in Desktop Mode now. Does the game show the updated version number on the title screen?
