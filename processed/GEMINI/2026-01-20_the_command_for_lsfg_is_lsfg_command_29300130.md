---
id: 162152
source: GEMINI
date: 2026-01-20
tags: ['lsfg-command', 'linux-gaming', 'steam-deck', 'game-launching']
category: homelab
sentiment: executing
resolution: resolved
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is noting the correct command for launching a game using lsfg.
---
# the command for lsfg is ~/lsfg %command%

### USER
the command for lsfg is ~/lsfg %command%

### GEMINI
To combine the LSFG command with your direct-launch game path, you have to be careful about the order. In Steam, %command% acts as a placeholder for the "Target" you've already set (the Citron AppImage). Here is exactly how your Launch Options box should look for everything to work (direct launch + fullscreen + frame gen): The Exact Command Copy and paste this into the Launch Options for Tears of the Kingdom: ~/lsfg %command% -f -g "/home/internal_games/ZeldaTotK_1.4.1.xci" Why this works: ~/lsfg: This tells the system to start the LSFG-VK Vulkan layer first. %command%: This tells Steam to run your "Target" (Citron) inside that layer. -f -g: These are the instructions for Citron. They tell the emulator to launch in fullscreen and go straight to the game file at that specific path. Critical Tuning for TotK 1.4.1 Since you're using Frame Gen on a heavy game, you must set these specific limits in the Steam Deck's "..." Performance menu to avoid stuttering or "jitter": Frame Limit: Set to 30 FPS. (LSFG will double this to a smooth 60). Refresh Rate: Set to 60Hz. Allow Tearing: ON. (Frame Gen requires this to reduce latency). In the Decky LSFG Plugin: Multiplier: 2x. Performance Mode: ON. WSI (Vulkan): ON. The "Advisor" Troubleshooting If the game crashes instantly with this command, it usually means there is a space in your filename or path that isn't wrapped in quotes. Ensure your path looks like "/home/.../ZeldaTotK_1.4.1.xci" with those quotation marks included. Next Step: Try launching with that combined command. Does the game start immediately with the LSFG "Active" message in the corner?
