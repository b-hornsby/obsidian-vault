---
id: 440736
source: GEMINI
date: 2026-01-20
tags: ['citron-emulator', 'zelda-totk', 'game-update']
category: homelab
sentiment: frustrated
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is clarifying that he only updated the Zelda TOTK game file, not the Citron emulator itself, while troubleshooting an issue.
---
# i didn't update citron i only updated totk 

### USER
i didn't update citron i only updated totk 

### GEMINI
If you didn't update Citron, then the issue is that Version 1.4.1 changed the game's internal Title ID or metadata, and the emulator's "Game List" logic is now getting stuck trying to reconcile your old cache with the new file structure. When you launch a game via command line (-g), the emulator performs a quick check. If it sees a conflict (like an update that doesn't perfectly match the base game's recorded Title ID in its cache), it aborts the auto-launch and drops you into the menu so you can "manually" resolve it. Here is the prioritized plan to force that auto-launch back into gear: 1. The "NAND Cache" Purge (Most Likely Fix) Even though you merged the files with SAK, Citron still has a "memory" of the old 1.0.0 or 1.2.1 version in its internal folders. Go to Desktop Mode and open Citron. Right-click Tears of the Kingdom and select Remove > Remove All Pipeline Caches. Then select Remove > Remove All Installed Contents. Why: This clears the metadata "ghosts." Since your 1.4.1 is now baked into the .xci, Citron will see it as a "fresh" 1.4.1 game and won't hang on the version check. 2. The "Start Screen" Logic Kill Citron has a setting that forces the menu to stay open if it detects any configuration change (which the 1.4.1 update triggered). In Citron, go to Emulation > Configure > General. Uncheck "Confirm exit when emulation is running." Uncheck "Pause emulation when in background." Go to the Interface tab and ensure "Show title bar" and "Show status bar" are Unchecked. 3. The Absolute Launch Option Syntax If the above two didn't work, we need to use the "Double-Dash" escape. Linux sometimes gets confused between the LSFG command and the Citron flags. Change your Launch Options to this exact string: ~/lsfg %command% -- -f -g "/home/internal_games/ZeldaTotK_1.4.1.xci" Note the --: This tells the system: "Everything after this dash belongs to the emulator, not the LSFG wrapper." 4. The "Direct Path" Reality Check Since SRM worked before, go into Desktop Mode Steam and look at the "Target" box for the game. If the Target box has quotes, the Launch Options path must also have quotes. If you have a space in your filename (e.g., Zelda TotK.xci), rename it to ZeldaTotK.xci and update the launch option. Spaces are the #1 cause of the "drops to menu" bug on Linux. Strategy for the Next Level You're playing a high-level game with 1.4.1 and LSFG. If the menu still appears, it’s because Citron is detecting a "Configuration Mismatch" created by the update. One final trick: Open Citron in Desktop Mode, double-click the game to start it, then immediately close it using File > Exit. This "registers" the 1.4.1 version in the emulator's recent history. Often, Citron will only auto-launch a game that it has "successfully" launched manually at least once. Try Step 1 (Purging the NAND cache) first. It’s the most direct way to stop the emulator from second-guessing your 1.4.1 file. Does it boot straight to the Nintendo logo now?
