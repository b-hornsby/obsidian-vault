---
id: 053345
source: GEMINI
date: 2026-01-20
tags: ['citron-emulator', 'steam-deck', 'game-testing', 'troubleshooting']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was asking whether to retry a game after running a fix command for Citron on Steam Deck.
---
# So now that I ran the command should I try the game again?

### USER
So now that I ran the command should I try the game again?

### GEMINI
Running that command was the right "brutal" move to clear the pipes. Since it returned nothing (silent success), the "ghost" records in that specific directory are gone. Yes, try the game now—but only in Desktop Mode first. Testing it in Desktop Mode isolates whether the emulator is fixed. If it works there but still fails in Game Mode, we have successfully moved the problem from "corrupted files" to "Game Mode configuration," which is much easier to solve. Before you hit "Play," check these 3 things: 1. The Firmware/Keys Reality Check By nuking that folder, you likely cleared your registered Firmware. If TotK fails to launch or gives an encryption error, you need to: Re-install your Firmware (Tools -> Install Firmware). Ensure your prod.keys are version 16.0.3 or higher. TotK updates literally won't trigger on old keys. 2. The "Add-on" Verification Right-click the game in Citron (Desktop Mode) -> Properties. Look at the Add-ons tab. If the update is gone, re-install it once using "Install Files to NAND." If it’s there but unchecked, check it. 3. The Shader Wipe (Crucial) Since the update was causing hangs, your existing shader cache is likely "poisoned" with bad data from the failed launch. Right-click the game -> Remove -> Remove All Pipeline Caches. Warning: The next boot will be slow as it rebuilds them. The "Game Mode" Strategy If it works in Desktop but hangs in Game Mode: The Frame Limit Trap: Press the (…) button in Game Mode. Ensure "Frame Limit" is OFF and "Refresh Rate" is 60. If you have it set to 30 or 45, the emulator will often hang on the TotK loading screen because it can't "handshake" with the SteamOS compositor. The "Wait" Rule: On the first launch after a wipe, TotK can sit on a black screen or a "Launching" logo for up to 3 minutes while it pre-compiles. Do not force-close it. Try launching in Desktop Mode now. Does it reach the main menu?
