---
category: homelab
date: 2026-01-20
id: 908210
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was frustrated that a specific game worked in desktop mode but not
  game mode on Steam Deck after an update.
tags:
- citron-emulator
- game-mode
- desktop-mode
- steam-deck
- update-issue
---
# This literally doesn’t happen with any other game and it’s only because of this update issue. I’m just not sure why it works in desktop and not in game mode and how to fix it

### USER
This literally doesn’t happen with any other game and it’s only because of this update issue. I’m just not sure why it works in desktop and not in game mode and how to fix it

### GEMINI
It is frustrating, but the reason this is only happening with Tears of the Kingdom and only after the update is simple: TotK is the most resource-heavy game you can emulate, and the update changed the "memory map" of the game. Desktop Mode works because it's a standard Linux environment. Game Mode is a specialized "micro-compositor" called Gamescope. Gamescope has a very short fuse—if a game doesn't "check in" within a certain timeframe because it's busy loading a massive update or building complex shaders, Gamescope assumes it's dead and refuses to show the window. Here is the precise, prioritized plan to fix the bridge between Desktop and Game Mode. 1. The "Vulkan Pipeline" Reset Updates often change how shaders are handled. If your Desktop Mode is using one setting and Game Mode is trying to use another, it will hang forever. Go to Desktop Mode. Open Citron -> Emulation -> Configure -> Graphics. Check "Use Disk Shader Cache" and "Use Asynchronous Shader Building". Set "Vsync Mode" to Mailbox or FIFO. Important: Under the Advanced tab of Graphics, ensure "Enable Reactive Flushing" is ON. This is often required for TotK to "wake up" the display driver in Game Mode. 2. Force the "Internal" Resolution Game Mode tries to force the Steam Deck's 800p resolution, but the TotK update might be trying to launch at a different internal scale, causing a resolution "handshake" loop. In Citron (Desktop), right-click TotK -> Properties -> Graphics. Ensure Resolution is set to 1x (720p/1080p). Set Window Adapting Filter to Bilinear. Close Citron and try Game Mode again. 3. Use "Full Screen" instead of "Borderless" Sometimes the TotK update forces the game into a windowed mode that Game Mode can't "grab." In Citron -> Configure -> General. Change Full Screen Mode from "Borderless Window" to "Exclusive Fullscreen" (or vice versa). Test which one allows the "handshake" to happen in Game Mode. 4. The "Launcher" Shortcut Audit Since you said this is only happening with this game/update, your Steam shortcut might be pointing to a specific version of the game that no longer "exists" in the same way after the NAND update. Delete the Steam shortcut for Tears of the Kingdom in your Steam Library. Go to Desktop Mode. If you use EmuDeck, run Steam ROM Manager and re-parse your games. This creates a fresh shortcut with the correct "arguments" for the updated game. If you added it manually, right-click the Citron AppImage in Dolphin -> Add to Steam, then manually add the launch arguments again. The Reality Check If it works in Desktop but not Game Mode, the game is running. You just can't see it. Next time it stays on "Launching," try tapping the Steam Button twice quickly. * Or, try holding the Power Button for 1 second to bring up the power menu, then hit B to go back. Sometimes forcing a UI overlay to pop up "wakes up" the game screen underneath. Would you like me to walk you through how to check the Steam "Launch Options" to make sure they aren't pointing to the wrong file?
