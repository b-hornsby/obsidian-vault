---
id: 182147
source: GEMINI
date: 2026-01-20
tags: ['sak', 'switch-army-knife', 'linux', 'steam-deck', 'tool-execution']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was asking how to run the Linux-based SAK (Switch Army Knife) tool on his Steam Deck.
---
# how do i run sak since its linux via the steam deck?

### USER
how do i run sak since its linux via the steam deck?

### GEMINI
Since SAK is a Windows application, you have to run it through Steam's Proton compatibility layer. Here is the no-nonsense, step-by-step guide to getting SAK running natively on your Deck. 1. The Preparation (Don't skip the Keys) SAK is just a interface; it uses hactool in the background. If you don't give it your keys, it will "run" but every operation will fail. Download SAK 64-bit from GitHub and extract the folder. Locate your prod.keys file (usually in /home/deck/.local/share/citron/keys/). Copy prod.keys into the bin folder inside your extracted SAK folder. Crucial: Rename that copy to keys.dat. SAK looks for that specific filename in the bin folder. 2. Adding SAK to Steam Open Steam in Desktop Mode. Bottom Left: Add a Game > Add a Non-Steam Game. Click Browse. Navigate to your extracted SAK folder and select SAK.exe. Find "SAK.exe" in your Steam Library. Right-click it > Properties > Compatibility. Check "Force the use of a specific Steam Play compatibility tool". Select Proton Experimental or Proton 9.0. 3. Running and Patching Hit Play on SAK in Steam. Once the window opens, click Update XCI with game update and dlc's. Step A: A file picker opens. Select your Base .xci file. Step B: Another file picker opens. Select your 1.4.1 .nsp update file. Click Update XCI and wait. Note: A terminal window might pop up. Leave it alone. It’s doing the heavy lifting. When it says "Success" or "Done," look in the SAK folder for a subfolder named patched. 4. The Final Clean Up Now that you have one single file that is Base + 1.4.1 Update, the "handshake" error in Game Mode will disappear. Move that new patched file to your /home/internal_games folder. Delete the old Zelda shortcut from Steam. Open Steam ROM Manager, parse your games again, and save. Why this is the "Final Boss" of fixes You've been struggling because Game Mode is timing out while Citron tries to look through your NAND for the 1.4.1 update. By merging them into one .xci, the emulator doesn't have to "think" during launch—it just loads the file. One warning: If SAK opens and then instantly closes, it means you're missing the Visual C++ Redistributable inside that Proton prefix. If it crashes on launch, would you like me to show you the command to install the missing "redist" files using Protontricks?
