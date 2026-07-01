---
category: homelab
date: 2026-01-20
id: 6297
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan removed all pipeline caches and now the game infinitely loads and returns
  to the home screen.
tags:
- pipeline-cache
- citron-emulator
- infinite-loading
- steam-rom-manager
---
# so i removed all pipeline caches and now its just "launching" forever. like i said it was just working after a fresh steam rom manager instance and everything. its literally this update but again i installed it in the nand this time with that option. it just now returned me to the home page 

### USER
so i removed all pipeline caches and now its just "launching" forever. like i said it was just working after a fresh steam rom manager instance and everything. its literally this update but again i installed it in the nand this time with that option. it just now returned me to the home page 

### GEMINI
This is the final hurdle. If it works in Desktop but crashes in Game Mode with a black screen or an "infinite loading" loop, it means the emulator is hanging while trying to initialize the game within Steam's Gamescope environment. Since you've already purged the shaders and confirmed the NAND installation is correct, the issue is down to a Resource Conflict or a Launch Path error. 1. The "Mod/Cheat" Ghost (Most Likely) When you update Tears of the Kingdom (e.g., to 1.2.1), any mods or cheats you had for the previous version become "poison." Even if they are disabled, Citron sometimes tries to parse the load directory and chokes. Action: In Desktop Mode, right-click the game > Open Mod Data Location. The Move: Move everything inside that folder to a temporary "Backup" folder on your desktop. Try to launch in Game Mode with an entirely empty mod folder. If it boots, one of your "60fps" or "DynamicFPS" mods was crashing the Game Mode initialization. 2. Force the Vulkan Reset Game Mode is much pickier about Vulkan "handshakes" than Desktop Mode. Action: In Citron (Desktop), go to Emulation > Configure > Graphics. Settings: * Graphics API: Vulkan. Device: Ensure it explicitly says "AMD Custom GPU (RADV VANGOGH)". V-Sync Mode: Change this to Mailbox (this is the most stable for the Deck's Game Mode). Disk Shader Cache: Ensure this is Checked. 3. Check the Steam ROM Manager Shortcut (The "Target" Error) SRM sometimes creates a shortcut that doesn't play nice with updates. Go to the game in your Steam Library (Game Mode) > Properties > Shortcut. Check the Target field. It should look like this: "/home/deck/Applications/citron.AppImage" Check the Launch Options. It should look like this: -f -g "/home/deck/internal_games/ZeldaTotK.nsp" The Truth: If the "Launch Options" is pointing to the Update file instead of the Base ROM, it will crash. Because you installed the update to the NAND, the shortcut must point to the base ROM. Citron will see the ROM, check the NAND, and apply the update automatically. 4. The "Internal Memory" Pressure Tears of the Kingdom + a large update + Game Mode's overhead = a massive RAM spike. Action: If you haven't already, increase your Swap File size to 16GB (using CryoUtilities) or ensure you have at least 15-20GB of free space on your internal SSD. If the SSD is full, the shader cache has nowhere to write during that initial Game Mode boot, causing the crash you're seeing. The Final "Nuke" Option If it still won't boot in Game Mode, the SRM shortcut is likely corrupted. Delete the non-steam game shortcut from Steam. Open Steam ROM Manager in Desktop Mode. Re-parse and Save to Steam. This forces Steam to rebuild the launch string with the correct environment variables. What to do next: If you look at the Shortcut tab in Steam (Step 3), can you paste exactly what is in your Target and Launch Options fields? I can tell you instantly if the syntax is wrong.
