---
category: general
date: 2026-01-20
id: 073148
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan describes the game crashing and returning to the home screen after
  waiting for it to load in game mode.
tags:
- steam-deck
- citron
- tears-of-the-kingdom
- game-mode
- crashing
- troubleshooting
---
# I waited it out and eventually it force stopped the game and went back to the Home Screen

### USER
I waited it out and eventually it force stopped the game and went back to the Home Screen

### GEMINI
The "Force Stop" is SteamOS's safety valve. It saw the emulator taking too long to respond, assumed it had crashed, and killed the process to "save" your system. This confirms that the initial shader/update processing is too heavy for the Steam Deck's Game Mode compositor to handle on the first run. Since it worked in Desktop Mode, we know the files are good. Now we just have to trick Game Mode into letting it run. 1. The "Desktop-to-Game" Bridge (The Guaranteed Fix) We need to "pre-warm" the game files so they are ready for the strict environment of Game Mode. Go to Desktop Mode. Open Citron and launch Tears of the Kingdom. Perform a manual save. Walk around for a few seconds, open the map, and save the game. Close Citron properly (don't just hit the 'X', use File > Exit). This forces the emulator to write the updated metadata and shader headers to the disk. Go back to Game Mode and try again. Now that the "first time" tasks are done, it should bypass the delay that caused the force-stop. 2. Disable "Steam Linux Runtime" Sometimes Steam tries to force a compatibility layer on top of your AppImage, which causes a conflict during heavy loading. In Game Mode, go to the game’s page (before hitting Play). Select the Gear Icon -> Properties -> Compatibility. Ensure "Force the use of a specific Steam Play compatibility tool" is UNCHECKED. If it is checked, it might be trying to run your Linux AppImage through Proton, which will fail every single time. 3. Change the Graphics API If it still crashes, Desktop Mode might be defaulting to OpenGL while Game Mode is struggling with Vulkan (or vice versa). In Desktop Mode, open Citron. Go to Emulation -> Configure -> Graphics. Switch the API (If it's on Vulkan, try OpenGL. If it's on OpenGL, switch to Vulkan). Vulkan is generally better for the Deck, but OpenGL is sometimes more stable for the initial "handshake" after a big update. The Brutal Reality You are fighting Gamescope. It has a timer; if the game doesn't show a frame in ~60-90 seconds, it kills it. Pro Tip: While the game is "Launching," keep moving the joysticks or tapping the screen. Sometimes input activity prevents the "Force Stop" timer from triggering. Perform Step 1 (The Desktop Save) and then try Game Mode again. Does it still force-stop, or does it finally break through?
