---
category: general
date: 2026-01-20
id: 997137
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan followed all the steps, but the game (Tears of the Kingdom) still gets
  stuck on the launching screen in game mode, even after building shaders.
tags:
- steam-deck
- citron
- tears-of-the-kingdom
- game-mode
- launching-issue
- shaders
---
# I did all of those steps and when I go to game mode and launch it still stays stuck on launching even though it built shaders this time

### USER
I did all of those steps and when I go to game mode and launch it still stays stuck on launching even though it built shaders this time

### GEMINI
The fact that it built shaders and still won't hand off to the screen means you are dealing with a Display Handshake Failure. The emulator is running, the game is technically "on," but the Steam Deck's Game Mode compositor (Gamescope) is stuck looking at the "Launching" transition because it doesn't recognize the Citron window as the active display. Here is how you force the image to appear. 1. The "Window Switcher" Force (The Most Likely Fix) SteamOS sometimes gets confused when an AppImage opens multiple background processes (like shader builders) and doesn't know which one to show. While stuck on the "Launching" screen, hold the Steam Button and press Left on the D-Pad. This is the "Alt-Tab" for the Steam Deck. If you see two Citron windows or a "Citron" and a "The Legend of Zelda" window, select the game window. 2. Disable the "Steam Overlay" for this Game The Steam Overlay often conflicts with Vulkan-based emulators during heavy load, causing the "Launching" screen to stay pinned on top even though the game is running behind it. Go to the game in your Steam Library (Game Mode). Select the Gear Icon -> Properties -> General. Toggle "Enable the Steam Overlay while in-game" to OFF. 3. Check the "Target" Path in Steam If you added this game to Steam manually, or if EmuDeck did it, the "Launch Options" might be pointing to an old configuration or a specific file that is causing a hang during the transition. Go to Properties -> Shortcut. Look at the Target. It should point to the Citron AppImage. Look at Launch Options. If there is a bunch of text there, clear it entirely and try launching again. Sometimes old "arguments" (like forcing a specific resolution) break after an update. 4. The "Vsync/Refresh" Lock If your Steam Deck is set to a refresh rate other than 60Hz, or if you have Allow Variable Refresh Rate on, the emulator can "deadlock" during the transition from the loading screen to the game. Press the (...) button -> Performance (Battery icon). Set Frame Limit to OFF. Set Refresh Rate to 60. Set Allow Screen Tearing to ON. The Unfiltered Advice You’ve proven the game works in Desktop Mode, so the emulator, the update, and the keys are 100% fine. The problem is purely Steam's UI acting as a wall. If the steps above don't work, the "brutally honest" strategic move is to delete the Steam shortcut entirely and re-add it. Use Steam ROM Manager (if you have EmuDeck) or manually add the Citron AppImage as a Non-Steam game again. A fresh shortcut will reset the "Launching" handshake. Try the Steam Button + D-Pad Left shortcut while it's stuck. Does it show a second window you can switch to?
