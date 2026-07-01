---
category: homelab
date: 2026-01-20
id: 638270
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated that the Citron emulator isn't auto-starting the selected
  game in game mode, even though it's the Linux version.
tags:
- citron-emulator
- linux-gaming
- auto-start
- game-mode
- steam-deck
---
# this citron version is literally for linux and it still doesn't auto start the game i selected in game mode?

### USER
this citron version is literally for linux and it still doesn't auto start the game i selected in game mode?

### GEMINI
The reason it isn't auto-starting is that the AppImage is not passing the instructions to the actual emulator "inside." On Linux, when you wrap an AppImage in a command like ~/lsfg, the AppImage often thinks the -f -g flags are meant for it (the container) rather than the game. Since you're using a native Linux version of Citron, we have to use the "Argument Pass-through" syntax. 1. The Correct "Pass-through" Command Try this exact string in your Launch Options. I have added a -- (double dash). In Linux, this tells the first program (the AppImage) to stop looking at flags and pass everything following it directly to the emulator engine. ~/lsfg %command% -- -f -g "/home/internal_games/ZeldaTotK_1.4.1.xci" 2. The "Target" Check (Brutally Important) If the above doesn't work, look at your Target box in Steam. Is it pointing directly to the .AppImage file? If it is pointing to a shell script (like citron.sh), the -f -g flags will never reach the game. The Fix: Ensure the Target is the absolute path to the Citron.AppImage itself. 3. The "Portable User" trick (The Citron Ghost) Citron sometimes ignores launch flags if it doesn't have a local configuration it "trusts." In Desktop Mode, go to the folder where your Citron.AppImage is. Create a folder right next to it named user. Open Citron once. It will now be in "Portable Mode." Close it and try launching from Game Mode again with the command in Step 1. 4. The "SRM" Permanent Solution If you want to stop fighting the Steam UI, do this in Steam ROM Manager (Desktop Mode): Go to your Citron Parser. In the Executable Arguments box, make sure it is exactly: ${fullscreenArgument} -g "${filePath}" Then, in the Steam Launch Options (within SRM), add the ~/lsfg %command% part. Save and Parse. This forces SRM to bake the path into the shortcut properly. The Advisor's Verdict If you add the -- and it still shows the menu, then your specific build of Citron has a broken CLI (Command Line Interface). This happens often with "nightly" or community builds of Citron. Test this: Change your Target to a different emulator (like Ryujinx) just for a second and use the same -g command. If Ryujinx starts the game immediately, then you know for a fact your Citron AppImage is the problem. Try the -- trick now. Does the game finally bypass that annoying menu?
