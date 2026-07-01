---
id: 374054
source: GEMINI
date: 2026-01-20
tags: ['sak', 'switch-emulation', 'steam-deck', 'tool-installation']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was asking how to download SAK (Switch Army Knife) for use with Switch emulation on Steam Deck.
---
# how do i download sak?

### USER
how do i download sak?

### GEMINI
To merge your files using SAK (Switch Army Knife), you need to understand that this is a Windows-based utility. It doesn't have a native Linux installer, so we have to run it through Steam's translation layer (Proton) while in Desktop Mode. Since you've had issues with Game Mode "poofing" out, merging the update directly into the game file is the best way to ensure the Steam Deck only has one single thing to load. 1. Download and Prepare SAK Go to the official SAK GitHub on your Steam Deck's browser. Download the latest .zip file (usually SAK_vX.X.X.zip). In your File Manager (Dolphin), go to Downloads, right-click the zip, and Extract it to a folder (e.g., /home/deck/Applications/SAK/). Important: You need your prod.keys file for SAK to work. Copy your prod.keys (the same ones Citron uses) and paste them into the bin folder inside the SAK directory. Rename the copy to keys.dat if the app doesn't recognize them. 2. Run SAK on the Steam Deck Open Steam in Desktop Mode. Click Add a Game (bottom left) > Add a Non-Steam Game. Click Browse and navigate to the SAK folder you just extracted. Select SAK.exe and click Add Selected Programs. Find "SAK.exe" in your Steam Library, click the Gear Icon > Properties > Compatibility. Check "Force the use of a specific Steam Play compatibility tool" and select Proton Experimental. Click Play. 3. Merge the Update (1.4.1) into the Base Game (.xci) Once SAK opens: Click the button that says Update XCI with game update and dlc's. A window will pop up. Select your Base .xci file first. Another window will pop up. Select your 1.4.1 .nsp update file. Click Update XCI. Wait. The Steam Deck might look like it's doing nothing, but look at the SAK window—it will be processing. Once it finishes, it will create a new file in the SAK folder (usually in a subfolder called patched). Why this is the "Advisor" Move By doing this, you are creating a Version 1.4.1 XCI. You no longer need to "Install to NAND" in Citron. You no longer need to worry about the emulator "finding" the update in Game Mode. You just point Steam ROM Manager to this one new file. The Brutal Reality Check: If SAK gives you an error saying it can't find keys, you didn't put the prod.keys in the bin folder correctly. Without those keys, SAK cannot decrypt the game to merge the update. Would you like me to help you verify the file path for your keys so SAK doesn't fail on the first try?
