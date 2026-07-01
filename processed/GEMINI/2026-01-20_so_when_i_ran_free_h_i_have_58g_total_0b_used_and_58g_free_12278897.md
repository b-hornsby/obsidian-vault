---
id: 246053
source: GEMINI
date: 2026-01-20
tags: ['linux-memory', 'free-command', 'system-resources']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is sharing memory stats (5.8GB total, all free) to help diagnose an issue.
---
# so when i ran free -h i have 5.8g total, 0b used and 5.8g free

### USER
so when i ran free -h i have 5.8g total, 0b used and 5.8g free

### GEMINI
The 5.8G result you're seeing in free -h confirms that you are running a newer version of SteamOS (3.6 or higher). Valve replaced the old swap file with ZRAM, which is a compressed RAM partition. The "Unknown" error in CryoUtilities happens because the tool wasn't built for ZRAM. But more importantly: 5.8GB is not enough for Tears of the Kingdom with an update. You are crashing in Game Mode because you've hit the RAM ceiling. Here is the brutal truth: You cannot "force" CryoUtilities to work right now because it's fighting SteamOS's new architecture. We have to bypass it and fix your specific TotK configuration manually. 1. The "Launch Option" Reality Check (Why it's actually crashing) SRM likely set your shortcut to launch with specific flags. If the update changed the internal file ID, the shortcut is trying to load a configuration that no longer exists. In Desktop Mode, open Steam and right-click TotK > Properties. Look at Launch Options. It should look like this: -f -g "/home/internal_games/Zelda.nsp" The Secret Killer: If there are any other flags there (like --width or --height or specific GPU IDs), delete them. Keep it simple: -f -g "path". 2. Manual ZRAM "Emergency" Fix Since you can't use CryoUtilities, we will manually increase your swapiness. This tells the Deck to be more aggressive about offloading memory to the SSD so the game doesn't crash. Open Konsole. Run this command: sudo sysctl -w vm.swappiness=100 Note: This is temporary until you reboot, but it will let us test if memory is the culprit. 3. Citron "Handshake" Fix If it works in Desktop but not Game Mode, the emulator is failing to "fullscreen" correctly, which Game Mode sees as a crash. Open Citron (Desktop). Emulation > Configure > Graphics. Set Fullscreen Mode to "Exclusive Fullscreen" (not Borderless). Set Aspect Ratio to "Force 16:10" (The Deck's native ratio). Important: Go to Advanced Graphics and turn OFF "Enable Compute Pipelines." This setting is notorious for crashing TotK updates on SteamOS 3.6+. 4. The SRM "Clean Sweep" Even if you think SRM is fine, it likely cached the 1.0.0 metadata. Close Steam completely. Open Steam ROM Manager. Click Settings (bottom left) > Remove all added app entries. Go back to Parsers, click Parse, and then Save to Steam. This forces Steam to rebuild the shortcut specifically for the version that is currently "live" in your Citron NAND. The Precision Plan Apply the UMA 4G BIOS fix (Volume Up + Power). If you haven't done this yet, none of the other steps will matter for TotK. Run the swappiness=100 command in Konsole. Use SRM to Remove and Re-add the games to Steam. Launch in Game Mode. If it still returns to the home screen: It means your NAND update file is "orphaned." In Citron (Desktop), right-click the game > Properties > Add-ons. Uncheck the update, click OK, then go back and Re-check it. This forces the emulator to re-index the file path. Does it still show the spinning Steam logo forever, or does it kick you back to the home screen within 5 seconds? (This timing tells me if it's a "Path" error or a "Memory" error).
