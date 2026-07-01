---
category: streaming
date: 2026-02-03
id: 741253
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is experiencing OBS window capture flickering when playing a game with
  OBS on a second monitor.
tags:
- obs-studio
- window-capture
- flickering
- gaming
- multi-monitor
---
# im talking on obs, the window capture flickers when im playing a game and i have obs running on my other monitor 

### USER
im talking on obs, the window capture flickers when im playing a game and i have obs running on my other monitor 

### GEMINI
This is the classic "Dual Monitor Desync" on NVIDIA Wayland. Because your primary monitor is likely running a game at high refresh (165Hz) and your second monitor is trying to draw OBS, the Wayland compositor (Mutter) is getting confused about which monitor to "sync" the frames to. When you capture a window from one monitor while a game is "owning" the GPU's attention on the other, the frames in OBS flicker because they are being delivered out of order. The Precision Fixes for Dual-Monitor Flickering 1. The "Explicit Sync" Kill-Switch (Most Likely Fix) Even if your drivers are new, OBS's integration with "Explicit Sync" is currently buggy on GNOME. You can force OBS to use the older, more stable sync method. Close OBS completely. Open your terminal and launch OBS with this exact prefix: __NV_DISABLE_EXPLICIT_SYNC=1 obs Check the capture: If the flickering stops, you can make this permanent by editing your OBS shortcut or adding export __NV_DISABLE_EXPLICIT_SYNC=1 to your ~/.bashrc or ~/.config/fish/config.fish. 2. The Match-Refresh-Rate Rule NVIDIA on Wayland hates mismatched refresh rates. If your 27" is 165Hz and your 32" is 165Hz, you're fine—but if one is set to 144Hz or 60Hz in your GNOME settings, it will cause the other to flicker. Go to Settings > Displays. Ensure both monitors are set to exactly the same refresh rate (e.g., both 165Hz or both 60Hz). 3. VRR (G-Sync) is Your Enemy Variable Refresh Rate (G-Sync) often causes flickering in secondary windows like OBS because the game’s FPS is fluctuating while OBS is trying to capture at a constant 60 FPS. Go to Settings > Displays. Select your gaming monitor and Turn off "Variable Refresh Rate." Restart OBS and test. 4. Use "Screen Capture" Instead of "Window Capture" Individual "Window Capture (PipeWire)" is notoriously more prone to flickering than capturing the entire display. Delete your Window Capture. Add a Screen Capture (PipeWire). Select the monitor your game is on. If you only want a specific part of the screen, hold the Alt key and drag the red edges of the source in OBS to crop it. The Reality Check You're playing a high-end game on an RTX 3070 while asking OBS to record/stream on a second monitor—all on a display protocol (Wayland) that NVIDIA only started "fixing" a few months ago. Try this first: Run the terminal command __NV_DISABLE_EXPLICIT_SYNC=1 obs. Does that command stop the flickering in the OBS preview while your game is active?
