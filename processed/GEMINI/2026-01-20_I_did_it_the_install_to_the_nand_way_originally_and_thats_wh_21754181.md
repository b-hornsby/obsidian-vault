---
category: general
date: 2026-01-20
id: 531841
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan mentions that installing the game to the NAND originally caused the
  current issues he's facing.
tags:
- steam-deck
- citron
- tears-of-the-kingdom
- nand-installation
- troubleshooting
---
# I did it the install to the nand way originally and that’s what got us in this mess

### USER
I did it the install to the nand way originally and that’s what got us in this mess

### GEMINI
I get it. You’re hesitant because the "official" way is what broke your setup. But here is the objective reason why it broke: Permissions and Database Corruption. When you installed it the first time, the AppImage likely created a file it didn't have full permission to modify later, or the "record" of the update got stuck in a loop. Since we just renamed/wiped the old Citron folder, we are starting with a clean database. To get the update working without repeating history, follow this risk-mitigated plan. 1. The "Safety First" Update Install We are going to use the NAND method again, but we are going to "seal" it in Desktop Mode so Game Mode doesn't have to do any heavy lifting. Open Citron in Desktop Mode. Go to File -> Install Files to NAND... Select your TotK Update .nsp. Immediately verify: Right-click the game -> Properties -> Add-ons. If the update is there and checked, proceed. If it still says "no update," stop. Your keys are too old for that specific update file. 2. The "Pre-Bake" Launch (Don't Skip This) This is where most people mess up. They install the update and immediately switch to Game Mode. Launch the game in Desktop Mode. Wait for it to reach the main menu. Check the bottom corner of the TotK title screen. Does it say Ver 1.2.1 (or whatever version you installed)? If yes, close the game normally. This ensures the emulator saves the "Update = ON" state to the configuration files properly. 3. Fixing the Game Mode "Handshake" Now that the update is verified in Desktop, we need to make sure Game Mode doesn't choke. Switch to Game Mode. Performance Settings (Critical): Press the (...) button -> Battery Icon. Frame Limit: OFF. Refresh Rate: 60. Why? If these are limited, the emulator’s internal clock during the "Checking for Add-on" phase can hang. The "3-Minute" Rule: Launch the game. The Steam logo might spin longer than usual, or you might see a black screen. Do not force close it. It is migrating the shaders to the new update version. Why this won't "break" it this time: The Folder is Clean: You aren't overwriting a corrupted entry; you're writing a fresh one. Permissions are Set: By launching in Desktop Mode first, the AppImage establishes "ownership" of those new NAND files before SteamOS's Game Mode tries to sandbox the application. The Advisor's Alternative If you are truly traumatized by the NAND method, use SAK (Switch Army Knife) on a PC to merge the update into the base game file (making one single .xci). Then you just put that one file on your Deck and never have to touch the "Install to NAND" button again. Try Step 1 and 2 in Desktop Mode now. Does the title screen of the game actually show the new version number?
