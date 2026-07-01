---
category: general
date: 2026-01-20
id: 130192
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan followed initial setup steps for Citron on his Steam Deck, but is now
  encountering an unexpected file structure.
tags:
- steam-deck
- citron
- setup
- file-system
- troubleshooting
---
# Did steps one and two but now when I look in the main citron folder this is all I see

### USER
Did steps one and two but now when I look in the main citron folder this is all I see

### GEMINI
Based on the image you provided, you are looking at the correct root folder for Citron. If nand/user/Contents/registered is empty, the update isn't actually installed there, despite what the emulator UI says. Here is the objective reality: You aren't fighting a "file" anymore; you're fighting a corrupted database entry that is telling the emulator to look for an update that doesn't exist. This is why it hangs in Game Mode—it's trying to call data from a void. 1. Kill the "Index" (The Direct Fix) The reason the update still shows in your game properties is a file called records.bin. This file is a list of everything Citron thinks it has installed. In the citron folder shown in your picture, look for any file ending in .bin (likely in a system subfolder inside nand). Delete records.bin. This forces Citron to rebuild its list of installed content from scratch when you next open it. 2. Flush the "Poisoned" Shaders Since you are in the main folder now, look at the shader folder in your image. Open that folder and delete everything inside. The Opportunity Cost: You will have some minor stuttering when you first start playing as the Deck rebuilds shaders. The Benefit: This is the most common reason for the "infinite loading" in Game Mode after a failed update. 3. The "Nuclear" Option (Strategic Reset) If you want to be 100% sure the update is gone so you can play today: Go back one folder in Dolphin so you see the citron folder itself. Rename citron to citron_OLD. Open the Citron AppImage. It will create a brand-new, clean citron folder. Copy only your keys and nand/system/Contents/registered (your firmware) from citron_OLD to the new folder. Do not copy the load or shader folders. Why Game Mode specifically fails Desktop Mode is more "forgiving" of minor configuration errors. Game Mode uses a very strict environment called Gamescope. If the emulator is trying to load a "ghost" update, Game Mode will just hang indefinitely while Desktop Mode might just ignore it and boot the base game. Try renaming the folder (Step 3). It is the only way to be absolutely sure you've stripped out whatever garbage that update left behind. Would you like to know where your save files are located so you can move them to the new folder?
