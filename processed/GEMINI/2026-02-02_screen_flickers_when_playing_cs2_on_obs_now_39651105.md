---
category: streaming
date: 2026-02-02
id: 330167
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is experiencing screen flickering in OBS while playing CS2.
tags:
- obs-studio
- screen-flickering
- cs2
- game-streaming
- performance-issues
---
# screen flickers when playing cs2 on obs now

### USER
screen flickers when playing cs2 on obs now

### GEMINI
Screen flickering in CS2 while using OBS is a notorious issue, usually caused by a conflict between how the game renders and how OBS hooks into the GPU. Since you just set up the Replay Buffer, the added strain on your GPU's encoder is likely exposing a settings mismatch. Here is the "advisor" move: Don't just try random things. Follow this prioritized sequence to kill the flicker. 1. The "G-Sync/FreeSync" Conflict (Most Likely) If you have a high-refresh-rate monitor, G-Sync/FreeSync often causes flickering when OBS is "hooked" into the game. The Fix: Open your NVIDIA Control Panel (or AMD Software) and disable G-Sync/FreeSync specifically for CS2, or set it to "Fixed Refresh". Alternative: Ensure your in-game FPS is capped. If your monitor is 144Hz, cap CS2 at 141 FPS (3 below max). Uncapped frames cause massive sync issues with OBS. 2. Swap Capture Methods "Game Capture" is usually the gold standard, but CS2’s anti-cheat and "Trusted Mode" can make it act up. The Test: If you are using Game Capture, try switching to Window Capture. The Settings: In Window Capture settings, change the "Capture Method" to Windows 10 (1903 and up). This uses a newer API that handles CS2 much better than the legacy bitblt method. 3. Disable "Hardware-Accelerated GPU Scheduling" (HAGS) Windows has a feature called HAGS that tries to give games more control over the GPU, but it often "starves" OBS of resources, leading to frame drops and flickering. The Fix: Go to Windows Settings > System > Display > Graphics Settings. Action: Toggle Hardware-Accelerated GPU Scheduling to OFF. Note: You must restart your PC for this to take effect. 4. Run OBS as Administrator If you don't run OBS as an admin, Windows treats it as a background task. When CS2 demands 99% of your GPU, Windows will literally stop giving OBS the resources it needs to render the preview/buffer, causing a flicker. The Fix: Right-click your OBS shortcut > Properties > Compatibility > Check "Run this program as an administrator." The Reality Check If you are recording at a higher resolution/FPS than your hardware can handle, the Replay Buffer is effectively a constant recording loop. Check your Stats dock in OBS (View > Stats). If you see "Frames missed due to rendering lag," your GPU is maxed out. You’ll need to lower your CS2 graphics settings or drop your OBS output to 1080p/60fps. Would you like me to walk you through how to check that Stats dock to see if your hardware is actually the bottleneck?
