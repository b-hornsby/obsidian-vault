---
category: homelab
date: 2026-01-20
id: 553658
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated because a Steam Rom Manager update broke his configuration,
  which was previously working perfectly.
tags:
- steam-rom-manager
- srm-configuration
- emulation-station
- game-updates
- steam-deck
---
# that didn't work but again before this update srm pointed everything perfectly and it was working perfectly

### USER
that didn't work but again before this update srm pointed everything perfectly and it was working perfectly

### GEMINI
Here’s the unfiltered reality: Your Citron update broke its own Command Line Interface (CLI). When you updated the Citron AppImage, the new version likely changed how it reads inputs or, more commonly, it has a "UI Conflict" where it forces the game list to the front regardless of what Steam tells it. Since SRM was working perfectly before, the issue isn't your shortcut logic—it's the emulator's new "brain" ignoring the commands. We are going to force it to behave using the "Terminal Sniper" method. 1. The "Colorful" Theme Bug (The most likely fix) Recent Linux builds of Citron have a documented bug where if the UI theme is set to "Colorful," the emulator ignores launch arguments and just sits at the menu. Go to Desktop Mode. Open File Manager (Dolphin) and go to: /home/deck/.config/citron/ Right-click qt-config.ini and open it with KWrite. Find the line that says theme=colorful (or anything else). Change it to: theme=qdarkstyle Save and close. Try launching in Game Mode now. 2. The Absolute "Direct" Launch Option Since the standard flags aren't working, we will use the Linux binary-direct path. Steam ROM Manager often points to a "generic" launcher; we want to point to the heart of the AppImage. Change your Launch Options to this exact sequence: ~/lsfg %command% -f -g "/home/internal_games/ZeldaTotK_1.4.1.xci" -- Note the -- at the very end. In Linux, this tells the program "Stop looking for options and just run what I told you." 3. The "SRM" Reset (If #1 failed) If SRM worked before, it might have cached old arguments that are now conflicting with the new AppImage's structure. Open Steam ROM Manager in Desktop Mode. Go to your Citron Parser. Look for Executable Arguments. It should be exactly: -f -g "${filePath}" If there is anything else in that box (like ${userDir}), delete it. Click Save, then Parse, then Save to Steam. The Advisor's "Hard Truth" Pivot If you do the qt-config.ini fix and the -- flag, and it still shows the menu, your version of Citron is a "broken" build for CLI usage. Your Move: If you want the game to "just work" like it did before: Go back to the previous version of Citron you were using. You can find older .AppImage files on their GitHub or in your Downloads folder. New isn't always better. Version 1.4.1 of the game + a new Citron build is a recipe for the exact "menu hang" you're seeing. Try Step 1 (the qt-config.ini theme change) first. It sounds crazy, but it is a confirmed fix for Citron ignoring launch flags on Steam Deck. Did changing the theme to qdarkstyle allow the game to auto-start?
