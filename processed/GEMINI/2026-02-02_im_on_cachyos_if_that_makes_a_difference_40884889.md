---
id: 084637
source: GEMINI
date: 2026-02-02
tags: ['cachyos', 'linux-distribution']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is stating that he is using the CachyOS Linux distribution, suggesting it might be relevant to the issue he's facing.
---
# im on cachyos if that makes a difference 

### USER
im on cachyos if that makes a difference 

### GEMINI
Being on CachyOS changes the game significantly. You aren't dealing with Windows "admin mode" issues; you are dealing with Wayland compositor conflicts and VRR (Variable Refresh Rate) bugs on Linux. Since CachyOS pushes the bleeding edge (likely running Plasma 6 on Wayland), CS2 and OBS are fighting over the same buffers. Here is how to kill the flicker on your specific setup. 1. The Nuclear Fix: Force CS2 to Native Wayland By default, CS2 often runs through XWayland (a translation layer), which is the #1 cause of flickering when OBS tries to "hook" the game. You want the game to talk directly to the compositor. In Steam, right-click CS2 > Properties. In the Launch Options, add: SDL_VIDEO_DRIVER=wayland %command% Why: This bypasses the X11 translation and usually eliminates the flickering caused by frame-pacing mismatches between the game and OBS. 2. Disable VRR / Adaptive Sync Linux Wayland is still "hit or miss" with Variable Refresh Rate (G-Sync/FreeSync) when multiple apps (like OBS) are pulling from the GPU. Go to your System Settings > Display and Monitor. Find Adaptive Sync (or VRR) and set it to Never. If the flicker stops, you’ve found the culprit. If you want to keep VRR on for the game but off for the desktop, you may need to use Gamescope. 3. Use "PipeWire" for Capture On CachyOS/Wayland, you should not be using "Game Capture" (which is an X11-based plugin). In OBS, delete your existing Game Capture source. Add a new source called Screen Capture (PipeWire) or Window Capture (PipeWire). Select the CS2 window. Why: PipeWire is the native Wayland way to share video buffers. It is significantly more stable and avoids the flickering "strobe" effect common with legacy capture methods. 4. Adjust the CachyOS Scheduler (Advanced) CachyOS is famous for its custom kernels and schedulers. Sometimes the "v3" or "v4" optimizations can cause micro-stutters in OBS's Replay Buffer threads. Open the CachyOS Hello app. Go to the Tweaks or Kernel Manager section. If you are using the bore or sched-ext schedulers, try switching to the standard Linux-CachyOS kernel to see if the flicker persists. Strategy Check: PipeWire is your priority. If you are still using the "Game Capture" source you used on Windows, that is exactly why it’s flickering. Wayland does not allow apps to "spy" on each other like Windows does; you must use the PipeWire portal to bridge them. Would you like me to show you the terminal command to check if your PipeWire portals are configured correctly for OBS?
