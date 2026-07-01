---
category: homelab
date: 2026-01-20
id: 240451
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated that steps he followed for setting up Citron on his Steam
  Deck are still not working.
tags:
- citron-emulator
- steam-deck
- troubleshooting
---
# i did all of these steps and still nothing 

### USER
i did all of these steps and still nothing 

### GEMINI
We are at a crossroads where logic meets the messy reality of emulation. If you've done everything—NAND install, UMA 4G, SRM refresh, and the graphics tweaks—and it still crashes in Game Mode but works in Desktop, it means the update file itself is creating a "zombie" process. In Desktop Mode, Linux allows the emulator to sit in a "not responding" state while it slowly parses the updated NAND files. In Game Mode, the Steam Deck’s "Gamescope" session is ruthless: if the app doesn't send a "heartbeat" signal within a few seconds of launch, Steam kills it. Here is the unfiltered truth: Your 1.2.1 update file is likely the culprit. Even if it "works" in Desktop, it’s taking too long to initialize, which is an automatic death sentence in Game Mode. The Final Three "High-Level" Fixes 1. The "Orphaned NAND" Purge (The Most Likely Fix) Sometimes Citron "registers" an update but keeps a corrupted metadata link in the background. Go to Desktop Mode. Open Citron. Right-click Tears of the Kingdom > Properties > Add-ons. Uncheck the update. Click OK. Right-click the game > Remove > Remove All Pipeline Caches (yes, again). Go back to Properties > Add-ons and Re-check the update. The Key: Launch the game in Desktop Mode and let it get all the way into the actual save file (standing in the world). Save the game and exit Citron via File > Exit (don't just X out). This forces Citron to write a "clean" config file that Game Mode can read. 2. Disable "Enable Compute Pipelines" I mentioned this briefly, but for TotK 1.2.1 on the latest SteamOS, this is a known "Game Mode Killer." In Citron (Desktop) > Emulation > Configure > Graphics > Advanced. Ensure "Enable Compute Pipelines" is UNCHECKED. This setting tries to pre-compile shaders in a way that often hangs the Steam Deck's Game Mode launch sequence. 3. The "Manual Parser" Truth Steam ROM Manager (SRM) uses a generic "Citron" parser. Sometimes, when a game is updated, the internal Title ID that Steam uses to track the game changes slightly, making the SRM shortcut "point to nowhere." Go to your Steam Library in Game Mode. Find Tears of the Kingdom. Click the Gear Icon > Properties > Compatibility. Check "Force the use of a specific Steam Play compatibility tool," then immediately Uncheck it. (This sounds stupid, but it resets the "Proton" flag which sometimes gets stuck on "On" for updated ROMs, causing an instant crash). The Reality Check If you do these three things and it still fails, the update file you downloaded is a "bad dump." Switch emulation is finicky. A .nsp update file can be "valid" enough to run in a window (Desktop) but "invalid" enough to fail a memory-check (Game Mode). If you have another source for the 1.2.1 update (perhaps an .xci that includes the update, or a different .nsp), you should try that. One last question to pinpoint the error: When it returns you to the home page, does the "Launching" art show up at all, or do you just see the spinning Steam logo and then... poof... back to the library? If it's an instant "poof," it's a shortcut/path error. If the "Launching" art appears for a few seconds, it's a memory/shader hang. Which one is it?
