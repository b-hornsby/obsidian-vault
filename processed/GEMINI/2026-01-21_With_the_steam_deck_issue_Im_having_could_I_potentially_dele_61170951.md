---
category: homelab
date: 2026-01-21
id: 223583
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan is asking if deleting a file and having it rewritten upon launching
  Tears of the Kingdom could resolve his Steam Deck issue.
tags:
- steam-deck
- file-rewriting
- tears-of-the-kingdom
- troubleshooting
- game-launching
---
# With the steam deck issue I’m having, could I potentially delete the file from the linked folder in the sd card and have it rewrite the file when I launch tears of the kingdom? 

### USER
With the steam deck issue I’m having, could I potentially delete the file from the linked folder in the sd card and have it rewrite the file when I launch tears of the kingdom? 

### GEMINI
Stop looking for a "soft" fix. You’re asking if you can delete a file and hope the system fixes itself—that's reactive, not strategic. If you're dealing with a symlinked folder (likely set up via EmuDeck or manual storage management), the answer depends entirely on which file you’re talking about. Here is the objective breakdown of what happens when you hit delete: 1. The "Safe" Deletions (Regenerative) If the file is a Shader Cache or Pipeline Cache, yes, you can delete it. The Result: The game will launch, but it will be a stuttering mess for the first 15–30 minutes as it "rewrites" (recompiles) those shaders in real-time. The Opportunity Cost: You trade a clean file for immediate performance degradation. If your issue is crashing during shader compilation, this is a valid troubleshooting step. 2. The "Dangerous" Deletions (Non-Regenerative) If the file is a Save File or Firmware/Keys component: The Result: It will not rewrite itself. You will simply lose your progress or the game will fail to boot (providing a "Keys not found" or "NCA header" error). The Symlink Risk: Because it's a symlink, deleting the file in the "linked" folder on your SD card deletes the only copy of that file. There is no "original" hidden on your SSD; the link is just a shortcut. If you delete it, it’s gone. 3. The "Configuration" Deletions If it's a config.ini or a settings file: The Result: The emulator (Yuzu/Ryujinx) will usually rewrite a default version. This is useful if you’ve borked your settings and can’t get the game to display correctly. The Advisor's Verdict You are likely avoiding the real issue: SD Card instability or a corrupted Symlink. If you are seeing "Read/Write" errors or the game is "disappearing," deleting one file is a band-aid on a bullet wound. Linux (SteamOS) treats symlinks as transparent—if the link is broken or the SD card is unmounting itself due to heat or age, the "rewrite" will fail anyway because the system can't find the destination. Your Strategic Plan: Identify the File: If it's shader_cache, delete it and suffer the stutter. If it's in the save folder, do not touch it without a backup. Verify the Path: Go to Desktop Mode. Open the folder. Right-click the folder and ensure the "Link" isn't showing a "Broken" icon (red X). Test the Hardware: If the "rewrite" fails, your SD card is likely failing or formatted in a way (like NTFS) that Linux permissions are rejecting. Move the folder back to internal storage temporarily. If it works there, your SD card is the culprit. Would you like me to walk you through how to verify if that specific symlink is actually broken before you start deleting data?
