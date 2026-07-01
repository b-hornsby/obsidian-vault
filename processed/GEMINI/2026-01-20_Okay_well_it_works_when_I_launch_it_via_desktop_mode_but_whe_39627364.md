---
category: general
date: 2026-01-20
id: 487518
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan reports that the game works in desktop mode, but not in game mode,
  and the system still indicates that no update is installed despite it being visible
  in the properties.
tags:
- steam-deck
- citron
- tears-of-the-kingdom
- game-mode
- desktop-mode
- update-issue
---
# Okay well it works when I launch it via desktop mode but when I tried to play it via game mode it just kept loading. It still says “there is no update installed for this title” even tho I clearly see it in properties for the game

### USER
Okay well it works when I launch it via desktop mode but when I tried to play it via game mode it just kept loading. It still says “there is no update installed for this title” even tho I clearly see it in properties for the game

### GEMINI
The fact that it works in Desktop Mode but hangs in Game Mode is the "smoking gun." It proves the files are there, but your Steam Deck's Game Mode environment is choking on a configuration mismatch or a performance limiter. Here is the cold, hard reality of why this is happening and how to stop the infinite loading screen. 1. The "60Hz/60FPS" Trap (The Most Likely Culprit) In Game Mode, the Steam Deck applies a system-wide Frame Limit. Emulators like Citron/Yuzu/Ryujinx tie their internal logic to the refresh rate. The Problem: If your Steam Deck "Performance" menu (the three-dot button) is set to 30FPS or 45FPS, or if you have Allow Variable Refresh Rate toggled on with a low limit, the emulator will wait forever for the next frame to "sync." The Fix: While in Game Mode, open the Performance Menu (…), go to the battery icon, and ensure: Frame Limit: Set to Off or 60. Refresh Rate: Set to 60Hz. Allow Screen Tearing: On (to ensure SteamOS doesn't force a laggy V-Sync). 2. The "Pathing" Conflict Desktop Mode and Game Mode handle "Non-Steam Game" shortcuts differently. If you added the game itself to Steam instead of adding the Citron AppImage, Steam might be trying to launch the game without the correct environment variables. The Fix: Ensure your Steam shortcut points to the Citron AppImage, not the .nsp file directly. If you use EmuDeck or Steam ROM Manager, re-run the parser. If you added it manually, make sure the "Target" in Steam properties is the AppImage and the "Start In" directory is the folder where the AppImage lives. 3. Clear the "Ghost" Cache The reason it says "no update installed" in properties despite being there is a Shaders/Cache mismatch between the two modes. Game Mode uses a different display compositor (Gamescope). In Desktop Mode, open Citron. Right-click Tears of the Kingdom. Select Remove -> Remove All Pipeline Caches. Now, try launching in Game Mode. It will take a long time to build shaders (black screen for 1-2 minutes), but it should eventually move past the loading screen. 4. Why it says "No update installed" The "Properties" window in the emulator often shows "No update" if the patch is disabled. In Desktop Mode, right-click the game -> Properties. Look at the Add-ons tab. Is the Update checked? If it’s unchecked, the emulator sees it in the folder but ignores it. Check it, click OK, and then switch to Game Mode. Strategy for Success You are likely experiencing a Shader Compilation Hang. Because Tears of the Kingdom is massive, Game Mode sometimes times out before the shaders finish compiling on the first run after an update. Do this right now: Set your Steam Deck to 60Hz/60FPS in the (...) menu. Launch the game in Game Mode. Wait for 5 full minutes. If the Steam loading logo is spinning, it’s working in the background. If it's a black screen, it’s compiling shaders. If it still doesn't load after 5 minutes, tell me: Is the screen black, or is it the Steam logo spinning?
