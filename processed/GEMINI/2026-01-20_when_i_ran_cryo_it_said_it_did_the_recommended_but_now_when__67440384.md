---
category: homelab
date: 2026-01-20
id: 595018
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated because CryoUtilities reports incorrect swap size and
  swappiness, and he's getting errors when trying to manually resize it.
tags:
- cryoutilities
- swap-size
- swappiness
- steam-deck
- performance-tuning
---
# when i ran cryo it said it did the recommended but now when i check is says current swap size unknown and current swappiness 60. when i try to manually resize it gives me an error 

### USER
when i ran cryo it said it did the recommended but now when i check is says current swap size unknown and current swappiness 60. when i try to manually resize it gives me an error 

### GEMINI
The "Current Swap Size: Unknown" and manual resize errors are classic signs that your internal SSD is too full or your sudo permissions are desynced. If CryoUtilities cannot "see" or "resize" the swap file, it’s because it’s trying to carve out 16GB of space that isn't available or isn't writable. Because you're emulating Tears of the Kingdom—which already needs massive shader cache space—you've likely hit the wall. 1. The "Space" Reality Check CryoUtilities requires continuous free space on your internal SSD. The Math: If you want a 16GB swap file, you need at least 20-25GB of free space on your internal drive (/home) to be safe. The Fix: If you are under 20GB free, delete a game or move some ROMs to your SD card temporarily. CryoUtilities will continue to throw errors until it has enough "physical room" to build that 16GB file. 2. Force the System to "See" the Swap If you have the space but it still says "Unknown," your SteamOS might be holding onto a broken swap reference. Open Konsole in Desktop Mode. Type free -h and press Enter. Look at the "Swap" line. If it says 0B or a very small number (like 1.0Gi), the swap isn't active. Run this command to clear the "stuck" file: sudo swapoff -a Now, go back into CryoUtilities and try to set it to 16GB again. Removing the active swap lock often allows the tool to finally "see" the drive. 3. The "Manual Resize Error" (Sudo Fix) If it gives an error when you click "Set," it's usually because the sudo timeout happened or the password wasn't accepted. The Fix: Close CryoUtilities entirely. Open Konsole and type sudo ls. Enter your password. If it works, leave Konsole open (this keeps the sudo session "warm") and immediately open CryoUtilities and try again. 4. Storage Maintenance Task Valve added a "Trim" feature that can sometimes block CryoUtilities if it's running in the background. Go to Game Mode > Settings > System. Scroll to the bottom and click Run storage device maintenance tasks. Wait for it to finish (it can take 5-10 mins). Reboot the Deck and try CryoUtilities one more time. The Brutal Advice If you can't get CryoUtilities to work, Tears of the Kingdom will continue to crash in Game Mode. The update you installed increased the memory footprint of the game. Without that 16GB swap file, you are essentially trying to fit a gallon of water into a pint glass. Your Steam Deck is "spilling" (crashing) because the glass is full. Try this: Check your storage in the Steam Settings. How much free space do you have exactly on your "Internal Storage"? If it's less than 15GB, that is 100% why CryoUtilities is failing.
