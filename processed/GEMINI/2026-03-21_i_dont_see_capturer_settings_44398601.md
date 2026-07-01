---
category: streaming
date: 2026-03-21
id: 589240
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is having trouble finding capturer settings, likely within OBS Studio,
  indicating a problem with his streaming setup.
tags:
- obs-studio
- capturer-settings
- streaming-configuration
---
# i dont see capturer settings

### USER
i dont see capturer settings

### GEMINI
Since you're on a cutting-edge CachyOS build (March 2026), the menus in Vesktop have shifted. "Capturer Settings" has been integrated directly into the streaming interface itself rather than the main settings menu. Here is the "brutally honest" breakdown of where those final buttons are hiding and how to finish this. 1. Where the "Capturer Settings" are hiding In modern Vesktop, you won't find a dedicated tab in the main settings. Instead: Join a voice channel. Click the Screen Share icon. Before you click "Share": Look at the bottom of the window that pops up (where you pick which screen/app to stream). You will see a dropdown or a "Settings" gear inside that specific popup. The Fix: Ensure "Use PipeWire" is selected. If you see an option for "Audio Source," set it to the specific application, not "System Audio," to prevent lag. 2. The Vencord "Plugin" Fix Vesktop has Vencord built-in. If the stream is still buggy, a specific plugin might be fighting your NVIDIA driver. Go to User Settings (the main gear icon). Scroll down to the Vencord section on the left sidebar. Click Plugins. Search for "WebRTC" or "Screenshare." The Fix: If "WebRTC Tweaks" is on, turn it OFF. It often tries to force settings that your NVIDIA 3070's Wayland driver doesn't support yet. 3. The "CachyOS" Power Move (Task Manager) Since you couldn't find the "Priority" rule in KDE, we’ll do it at the OS level to ensure your i7-12700K doesn't "park" the stream cores. Open your terminal and run: renice -n -5 $(pgrep vesktop) Why: This tells the Linux kernel to prioritize Vesktop's data over other background tasks. In a logistics sense, you're putting this package on the "Express" truck. Final Summary: The Complete Fix To recap, you have now: Forced Wayland: Saved the nano file with the Ozone flags. (Kills the flicker). Window Rules: Set "Accept Focus" and "Focus Stealing Prevention." (Kills the lag). Adaptive Sync: Turned it OFF in KDE settings. (Kills the stutter). The Result: Your stream should now be a smooth 60 FPS. If your friends still say it’s laggy, the bottleneck is likely your Upload Speed or a PipeWire buffer issue. Would you like me to show you the command to check if your internet is actually the one "bottlenecking" the stream?
