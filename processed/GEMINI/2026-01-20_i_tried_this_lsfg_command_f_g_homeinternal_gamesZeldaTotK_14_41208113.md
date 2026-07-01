---
category: homelab
date: 2026-01-20
id: 225548
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan tried a launch command with lsfp flags for Zelda TOTK 1.4.1 but it
  still requires manual game selection.
tags:
- citron-emulator
- lsfg-command
- zelda-totk
- launch-arguments
---
# i tried this ~/lsfg %command% -f -g "/home/internal_games/ZeldaTotK_1.4.1.xci" and it didnt work i still have to choose it 

### USER
i tried this ~/lsfg %command% -f -g "/home/internal_games/ZeldaTotK_1.4.1.xci" and it didnt work i still have to choose it 

### GEMINI
If Citron is still showing the game list despite the -f -g command, it means the emulator isn't correctly parsing the path we gave it. This usually happens on Linux because of how AppImages handle file permissions or because of a tiny syntax error with the quotes. Since we are acting with "brutal honesty" and "precision," let's stop guessing and use the absolute definitive path that Linux requires. 1. The "Double Quote" Fix (Most Likely Culprit) Sometimes the Steam Deck's launch options need the path to be wrapped in both single and double quotes to ensure the AppImage doesn't drop the command. Try this exact string in your Launch Options: ~/lsfg %command% -f -g "'/home/internal_games/ZeldaTotK_1.4.1.xci'" Notice the difference: I put a single quote ' inside the double quotes ". 2. The "Z-Drive" Logic Because Citron is a Windows-based architecture running on Linux, it sometimes doesn't recognize /home/ as a valid starting point—it wants to see it as a mapped drive. Try this version: ~/lsfg %command% -f -g "Z:/home/internal_games/ZeldaTotK_1.4.1.xci" 3. Verify the "Target" Path If those don't work, we need to make sure your "Target" box (above the Launch Options) is actually pointing to the Citron AppImage and not a script. Target: Should be the path to Citron.AppImage. Start In: Should be the folder where that AppImage lives. The "I'm Done With This" Alternative If you have tried the quotes and it still opens the menu, it means the version of Citron you have is ignoring command-line arguments (this happens in some "canary" or experimental builds). Do this instead: Open Citron in Desktop Mode. Go to Emulation > Configure > General. Look for a checkbox that says "Exit Citron when emulation stops" and "Confirm exit" — check the first, uncheck the second. There is sometimes a setting under Interface or UI called "Start games in Fullscreen" or "Hide game list on launch". If you see those, toggle them. Final Check on LSFG If you see the Citron menu, is the LSFG-VK plugin showing "Active"? * If YES: The ~/lsfg part is working perfectly. The only issue is Citron being stubborn about the -g flag. If NO: The ~/lsfg part is failing and we need to fix the Decky plugin first. Try the 'single inside double' quote trick first. If that doesn't bypass the menu, tell me: what is the EXACT text in your "Target" box?
