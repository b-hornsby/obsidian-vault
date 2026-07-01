---
id: 688177
source: GEMINI
date: 2026-01-20
tags: ['citron-emulator', 'nand-update', 'tears-of-the-kingdom', 'steam-deck', 'switch-emulation']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan applied a game update to Citron's NAND and confirmed Tears of the Kingdom ran in desktop mode on Steam Deck.
---
# i applied the update to the nand, tested it in desktop and confirmed it ran. the game is tears of the kingdom 

### USER
i applied the update to the nand, tested it in desktop and confirmed it ran. the game is tears of the kingdom 

### GEMINI
Since it runs in Desktop Mode but crashes in Game Mode, the problem is no longer your file setup—it’s the handshake between Steam and the emulator. Tears of the Kingdom is notorious for this because it pushes the Deck’s hardware to its absolute limit, and Game Mode (Gamescope) is much more aggressive about killing apps that don't respond "correctly" during launch. Here is the strategic fix to stop the crashing in Game Mode: 1. The "Clean Slate" Strategy (Critical) Updates often change how the game handles shaders. If you have old shaders from the previous version, Game Mode will try to load them, hit a conflict, and crash before you even see a Nintendo logo. In Desktop Mode, open Citron. Right-click Tears of the Kingdom. Select Remove > Remove All Pipeline Caches. Note: Your first launch after this will have some stuttering while it rebuilds, but it will actually boot. 2. Check the Steam Shortcut Path When you used Steam ROM Manager, it created a shortcut. If that shortcut is pointed at an old version or a specific file path that changed, it will fail. In Game Mode, go to the game's Properties > Shortcut. Look at the "Target." It should point to your Citron AppImage. Look at "Launch Options." It should end with the path to your Base ROM (the one in /home/internal_games). Crucial: Ensure the path is in quotes if there are spaces. If SRM pointed it to the update file by mistake, it will crash every time. It must point to the base game; Citron handles the update internally via the NAND you just set up. 3. The "Gamescope" Conflict Settings Game Mode applies its own V-Sync and frame limits which can conflict with Citron’s internal settings for TotK. Inside Citron (Desktop Mode): Right-click game > Properties > Graphics. API: Vulkan (Mandatory for Deck). V-Sync Mode: Mailbox or Off (Let Steam Deck handle V-Sync). In Game Mode (Right Sidebar / "..." Button): Set the Refresh Rate to 60. Disable "Allow Tearing." Ensure "Enable Unified Frame Limit Management" is Off. 4. The "Long Initial Boot" The first time you launch TotK with a new update in Game Mode, it has to verify the NAND contents and re-cache. If you see the Steam spinning logo for more than 2 minutes, don't force quit it yet. * If it returns to the home screen instantly, it's a pathing error (see Step 2). If it hangs, it's a shader/memory issue (see Step 1). The Brutal Truth You are emulating one of the most demanding games ever made for the Switch on a handheld. If you don't Remove All Pipeline Caches after an update, you are effectively trying to build a house on a crumbling foundation. One final check: Open Citron in Desktop Mode, right-click the game, and go to Properties > Add-ons. Is the update checked? If it’s unchecked, Citron is trying to launch Version 1.0.0 with the shader cache of a newer version, which is an instant crash. Would you like me to give you the exact "Launch Options" string you should use in Steam to make sure it's launching via the AppImage correctly? (I just need to know the exact name of your AppImage file).
