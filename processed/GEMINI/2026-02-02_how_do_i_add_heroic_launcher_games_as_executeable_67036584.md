---
id: 216984
source: GEMINI
date: 2026-02-02
tags: ['heroic-launcher', 'game-shortcuts', 'cachyos', 'linux-gaming']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was trying to add Heroic Launcher games as executable shortcuts on CachyOS.
---
# how do i add heroic launcher games as executeable

### USER
how do i add heroic launcher games as executeable

### GEMINI
If you're trying to add Heroic Launcher games as standalone executables (likely for Steam, a desktop shortcut, or a custom launcher), you don't actually want the raw .exe file. Pointing directly to the game's executable usually bypasses the Wine/Proton prefix Heroic set up, causing the game to crash or fail to find its save files. Here is the direct, no-nonsense way to do it. 1. The "Official" Way (Easiest) Heroic has a built-in feature to export games so they behave like native executables in your library or on your desktop. To Steam: 1. Open Heroic and go to your Library. 2. Click the three vertical dots (or right-click) on the game tile. 3. Select Add to Steam. (Note: Restart Steam afterward to see it in your "Non-Steam" category). To Desktop/Application Menu: Go to the game's page in Heroic. Click the three dots in the top right. Select Add Shortcut (this creates a .desktop file on Linux or a shortcut on Windows). 2. The "True" Executable Command (For Advanced Launchers) If you need a specific command to put into a script or a specialized front-end (like Pegasus or EmulationStation), you should use Heroic’s URI scheme. This ensures the game launches with the correct Wine version and prefixes. The command format is: heroic://launch/<provider>/<game-id> Example: heroic://launch/epic/66033 How to find your Game ID: Go to the game’s Settings inside Heroic. In the "General" or "Advanced" tab, look for App Name or ID. Alternatively, right-click the game and select "Copy Game ID" if available in your version. 3. The Manual Linux Script (The "Pro" Way) If you want a physical file that acts as an executable, create a simple bash script: Create a file named launch_game.sh. Paste this inside: #!/bin/bash flatpak run com.heroicgameslauncher.hgl heroic://launch/epic/YOUR_GAME_ID_HERE (Remove flatpak run com.heroicgameslauncher.hgl and replace with just heroic if you installed via .deb/.rpm/AppImage). Run chmod +x launch_game.sh. Why you shouldn't just point to the .exe: If you browse to the game folder and select game.exe, you are stripping away the Wine Prefix (the fake "C: drive") and the compatibility layer (Proton/Wine-GE) that Heroic manages. The game will try to run as a native Windows app on Linux (failing immediately) or lose access to your saves and cloud sync. What's your end goal for these executables? If you're trying to set up a specific handheld UI or a mod manager, I can give you the exact path syntax for that.
