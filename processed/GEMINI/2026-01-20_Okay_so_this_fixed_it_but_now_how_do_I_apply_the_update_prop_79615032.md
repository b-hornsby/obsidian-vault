---
id: 604150
source: GEMINI
date: 2026-01-20
tags: ['steam-deck', 'citron', 'tears-of-the-kingdom', 'game-update', 'game-mode', 'proper-installation']
category: general
sentiment: building
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
summary: Bryan has seemingly fixed an initial issue, but now needs guidance on how to properly apply the update to avoid breaking the game in game mode again.
---
# Okay so this fixed it but now how do I apply the update properly so it doesn’t break the game mode side of things again?

### USER
Okay so this fixed it but now how do I apply the update properly so it doesn’t break the game mode side of things again?

### GEMINI
To apply the update without bricking Game Mode again, you need to abandon the "Install to NAND" feature. That feature is notorious for permission locks and database corruption on the Steam Deck's Linux environment. Here is the professional, stable way to handle Tears of the Kingdom updates. 1. The "Clean Folder" Method (Recommended) Instead of "installing" the update into the emulator’s internal system, you are going to let Citron "discover" it. Put your Base Game (.nsp or .xci) and your Update file (.nsp) in the exact same folder on your Steam Deck. In Citron (Desktop Mode), right-click the game -> Properties. Go to the Add-ons tab. If the update file is in that folder, Citron often detects it automatically. If it's there, just check the box and hit OK. Why this is better: It doesn't write to the nand directory, which means there are no "ghost" files to get stuck later. 2. If you MUST use "Install to NAND" If you prefer the internal install, you must follow these rules to avoid another crash loop: Match the Region: Ensure your Update is the same region as the Base Game (e.g., both US). If they don't match, the emulator will "install" it, fail to link it, and hang on boot. Check your Keys: TotK updates usually require Firmware/Keys 16.0.3 or newer. If your keys are old, the update will install but the game will never load. Install in Desktop, Verify in Desktop: After installing, launch the game once in Desktop Mode. Let it reach the main menu. This allows the emulator to build the initial metadata without the Steam Deck’s "Game Mode" compositor (Gamescope) timing it out. 3. The Game Mode "First Boot" Protocol The most common reason for the infinite loading screen after a successful update is Shader Compilation. Switch to Game Mode. Launch the game. DO NOT TOUCH IT for 5 minutes. Even if the screen is black or the Steam logo is spinning. The Steam Deck is rebuilding the "Pipeline Cache" for the new update. If you force-close it during this, you corrupt the cache and have to start over. Performance Settings: Press the (…) button -> Performance. Ensure Frame Limit is OFF and Refresh Rate is 60. If you cap the deck at 30FPS during this first launch, the emulator often deadlocks. Summary Checklist ActionPurposeVerify RegionPrevents "No Update Installed" error.Delete old ShadersPrevents black screen hangs.Set Deck to 60HzEnsures the emulator doesn't freeze on boot.Wait 5 MinutesAllows first-time shader compilation. Would you like me to check the Title ID of your update file to make sure it actually matches your base game?
