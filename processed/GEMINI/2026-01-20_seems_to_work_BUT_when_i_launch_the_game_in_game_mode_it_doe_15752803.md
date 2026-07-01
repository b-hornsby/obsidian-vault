---
category: homelab
date: 2026-01-20
id: 913482
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan's game update seems applied but the game doesn't auto-start in game
  mode, showing the Citron menu instead.
tags:
- citron-emulator
- game-mode
- auto-launch
- steam-deck
---
# seems to work BUT when i launch the game in game mode it doesn't automatically start it shows the citron menu and i have to manually start the game again

### USER
seems to work BUT when i launch the game in game mode it doesn't automatically start it shows the citron menu and i have to manually start the game again

### GEMINI
This happens because your Steam shortcut is only pointing to the emulator itself, not giving it the "Direct Launch" command for your specific game. It's an easy fix in the Steam settings. The Fix: Manual Launch Arguments You need to tell Citron two things: -f (Full screen) and -g (Game path). In Game Mode, go to Tears of the Kingdom in your Library. Click the Gear Icon > Properties. Look at the Launch Options box at the bottom. It needs to look exactly like this: -f -g "/home/deck/Emulation/roms/switch/ZeldaTotK_1.4.1.xci" Crucial Rule: If your file path has spaces (e.g., Zelda TotK.xci), you must use the quotation marks. If it doesn't have spaces, you can skip them, but keeping them is safer. Why Steam ROM Manager (SRM) "Forgot" This SRM is supposed to add these flags automatically, but when you renamed the file or moved it after using SAK, the "parser" link broke. To fix this permanently for the future: Go to Desktop Mode and open Steam ROM Manager. Select your Citron parser on the left. Look for a box labeled "Executable Arguments" or "Command Line Arguments". Ensure it says: ${fullscreenArgument} -g "${filePath}" Click Save Parser, then Parse and Save to Steam again. One Final Warning (The "Double Menu" Bug) If you add the -f -g flags and it still shows a menu, it means you have a "Start Screen" setting enabled inside Citron that overrides Steam. Open Citron in Desktop Mode. Go to Emulation > Configure > General. Uncheck "Confirm exit when emulation is running." Uncheck "Show title bar" (if available). Ensure "Pause emulation when in background" is OFF. The "Advisor" Performance Check Since you are finally in the game: Press the "..." button on your Deck. Set Manual GPU Clock to 1200MHz. Set TDP Limit to OFF (let it use the full 15W). Set Scaling Filter to FSR (with Sharpness at 5) for the best look on the Deck’s screen. Is it booting straight into the Nintendo logo now, or is it still stopping at the Citron game list?
