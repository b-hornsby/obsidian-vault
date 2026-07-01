---
category: homelab
date: 2026-03-21
id: 348089
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to disable adaptive sync, likely to troubleshoot display
  issues or for specific application requirements.
tags:
- adaptive-sync
- display-settings
- monitor-configuration
---
# how do i turn off adaptive sync 

### USER
how do i turn off adaptive sync 

### GEMINI
If you can't find it in the menus, it's likely because your monitor and NVIDIA driver are "auto-negotiating" the refresh rate behind the scenes, and KDE 6 has hidden the toggle to be "helpful." Since the UI is failing you, we’re going to use the Terminal to force it off. This is the only way to be 100% sure it’s dead. 1. The Terminal "Force Quit" for VRR Open your terminal and run this command: kscreen-doctor output.1.vrrpolicy.never What this does: It bypasses the System Settings menu and tells the display server (KWin) to strictly disable Variable Refresh Rate for your primary monitor. If you have two monitors: Run kscreen-doctor -o first to see which one is output.1 and which is output.2, then apply the command to both. 2. The Physical "Kill Switch" If the terminal command doesn't stop the flickering, your monitor's internal hardware is likely forcing it. Reach under/behind your monitor and open its OSD (On-Screen Display) Menu using the physical buttons. Look for "FreeSync," "G-Sync," or "Adaptive Sync." Set it to OFF. Why: If the monitor tells Linux "I am a G-Sync monitor," Linux will try to use it even if you told the software not to. Turning it off at the source is the only "brutally honest" way to ensure it's gone. 3. Check the "NVIDIA Settings" (The Linux Catch-22) Even though you're on Wayland, the nvidia-settings panel still controls some hardware behaviors. Open NVIDIA X Server Settings (it might be in your app menu). Look for "Allow G-SYNC/G-SYNC Compatible" under the OpenGL or Display sections. Uncheck it. The Verdict: Why we are doing this In a high-volume logistics environment (your 3070 streaming to your friends), Adaptive Sync is a bottleneck. It tries to match your monitor's refresh rate to your game's FPS. When you start a stream, the "capture" tool (PipeWire) gets confused because the refresh rate is constantly jumping around (e.g., from 144Hz to 132Hz to 140Hz). This creates the flicker and lag. By setting a "Fixed" refresh rate (e.g., a solid 144Hz), you give the streaming software a stable target to capture. Once you've run that kscreen-doctor command, does the flickering stop when you open Vesktop?
