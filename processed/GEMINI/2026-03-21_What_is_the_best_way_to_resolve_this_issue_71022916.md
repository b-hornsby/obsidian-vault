---
category: general
date: 2026-03-21
id: 629417
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is asking for the best way to resolve an unspecified issue.
tags:
- troubleshooting
- best-practice
- issue-resolution
---
# What is the best way to resolve this issue

### USER
What is the best way to resolve this issue

### GEMINI
The "best" way to resolve this is to stop fighting Wayland’s default limitations and force your apps to use the modern Explicit Sync and PipeWire protocols that your NVIDIA 3070 and CachyOS are designed to handle. Here is the exact, high-level plan to move from "laggy and buggy" to a professional-grade stream. 1. The "Protocol" Fix: Force Native Wayland By default, Vesktop (and Discord) often runs through XWayland, which is like trying to translate a conversation through a middleman who stutters. You need to force it to speak Wayland natively. The Action: Launch Vesktop with these precise flags. vesktop --enable-features=UseOzonePlatform,WaylandWindowDecorations --ozone-platform=wayland --enable-gpu-rasterization --enable-zero-copy Why this works: It bypasses the translation layer that causes the "black bar" flickering and utilizes your GPU directly for rendering the UI. 2. The "Performance" Fix: Disable KDE Power Management KDE Plasma is aggressively "green"—it tries to save power on background windows. When you're playing a game, it assumes Vesktop doesn't need resources, which is why your friends see a 5 FPS slideshow. The Action: Open System Settings > Window Management > Window Rules. Add a new rule for Vesktop. Add the property Focus stealing prevention and set it to None (Force). Add the property Lowered priority and set it to No (Force). Why this works: It tells CachyOS that Vesktop is a high-priority process that should never be "paused" or slowed down while you're focused on your game. 3. The "Sync" Fix: Disable Adaptive Sync (VRR) NVIDIA's Variable Refresh Rate (G-Sync) on Wayland is a known source of flicker during screen capture. The GPU gets confused between the game's refresh rate and the stream's capture rate. The Action: Go to System Settings > Display and Monitor. Set Adaptive Sync to Never. Why this works: It stabilizes the frame delivery, preventing the "flicker" that occurs when the monitor and GPU are rapidly switching frequencies. 4. The "Safety Net": XWayland Video Bridge If you still see glitches (especially when trying to share a specific window instead of the whole screen), you need the "bridge." The Action: sudo pacman -S xwaylandvideobridge Once installed, ensure it is running in your system tray. It acts as a specialized translator specifically for screen sharing. The Final "Brutally Honest" Check If you do all of this and it’s still laggy, turn OFF "Hardware Acceleration" inside the Vesktop settings. While it sounds counterintuitive, NVIDIA's Linux encoders can sometimes bottleneck during simultaneous gaming and streaming. Letting your CPU handle the stream encoding (which CachyOS is optimized for) often results in a smoother experience for your viewers. Would you like me to show you how to save these settings permanently so you never have to touch a terminal again to launch Discord?
