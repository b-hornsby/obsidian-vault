---
category: coding
date: 2026-03-21
id: 753961
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to read the nvidia_drm modeset parameter but is getting a
  permission denied error, indicating a troubleshooting step for display issues.
tags:
- nvidia-driver
- modeset-parameter
- permission-denied
---
# ❯ cat /sys/module/nvidia_drm/parameters/modeset
cat: /sys/module/nvidia_drm/parameters/modeset: Permission denied

~
❯ 

### USER
❯ cat /sys/module/nvidia_drm/parameters/modeset
cat: /sys/module/nvidia_drm/parameters/modeset: Permission denied

~
❯ 

### GEMINI
That "Permission denied" is actually a good sign. It means the file exists and the system is protecting it, which is standard for kernel parameters. On CachyOS, modeset is almost certainly enabled by default, but let's confirm it the "unfiltered" way without needing root permissions. Run this instead: sudo cat /sys/module/nvidia_drm/parameters/modeset If it returns Y: Your kernel is correctly set up for Wayland. If it returns N: This is why you’re flickering. We’ll need to add it to your bootloader (which is likely Limine or systemd-boot on a 2026 CachyOS install). The Final "Logistics" Troubleshooting (The Mirror) You’ve spent a lot of time "under the hood" today. Let's look at the situation with complete objectivity. If you have applied the Wayland flags, fixed the window rules, and disabled VRR, but the flickering/lag remains, you are likely hitting a Hardware/Driver mismatch. Here is the "High-Level Advisor" plan to get you to the next level: 1. The i7-12700K "Bypass" (Immediate Action) Since your 3070 and Wayland are having a "communication breakdown," stop trying to force the GPU to do the heavy lifting for the stream. Open Vesktop Settings -> Voice & Video. Disable "Hardware Acceleration." Disable "OpenH264 Video Codec." Force your CPU to encode. Your i7-12700K is a beast; it can handle a Discord stream in its sleep, and it bypasses the buggy NVIDIA Wayland sync entirely. 2. Verify the Handshake Open your terminal and run xlsclients. If Vesktop is in that list, you are still running on XWayland (the flicker zone). If it is NOT in the list, the flags worked and you are on Native Wayland. 3. The "Opportunity Cost" Reality Check If you’ve done all this and your friends still see a slideshow: Check your Upload Speed: Akron internet can be spotty. If you aren't hitting at least 15Mbps upload while gaming, the software fixes won't matter. The X11 Nuclear Option: If you need to stream a high-stakes session tonight and can't afford to mess around, log out, click the session menu at the bottom left, and select Plasma (X11). It solves the NVIDIA flicker issue instantly at the cost of being "old tech." Try the sudo cat command first—what did it return?
