---
category: coding
date: 2026-03-21
id: 097404
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to use the xlsclients command but it's not recognized in
  his fish shell, indicating a problem with his environment or package installation.
tags:
- xlsclients
- x11-utilities
- command-not-found
- fish-shell
---
# ❯ xlsclients
fish: Unknown command: xlsclients

~
❯ 

### USER
❯ xlsclients
fish: Unknown command: xlsclients

~
❯ 

### GEMINI
Since you are on CachyOS, the xlsclients command isn't installed by default because it's an old X11 utility. But that's okay—we can use a much simpler "Wayland-native" method to see if our fix worked. 1. The "Wayland Debug" Test Run this command in your terminal. It will try to launch Vesktop and tell you exactly what it's doing: WAYLAND_DEBUG=1 vesktop 2>&1 | grep "wayland-0" If you see a lot of text scroll by: Congratulations. Vesktop is officially running on Native Wayland. If the terminal just sits there or returns nothing: It's still stuck in XWayland (the flicker zone). 2. The Final "Logistics" Troubleshooting (The Mirror) You’ve spent a lot of time "under the hood" today. Let's look at the situation with complete objectivity. If you have applied the Wayland flags, fixed the window rules, and confirmed VRR is "Never," but the flickering/lag remains, you are likely hitting a Hardware/Driver mismatch. Here is the "High-Level Advisor" plan to get you to the next level: A. The i7-12700K "Bypass" (Immediate Action) Since your 3070 and Wayland are having a "communication breakdown," stop trying to force the GPU to do the heavy lifting for the stream. Open Vesktop Settings -> Voice & Video. Disable "Hardware Acceleration." Disable "OpenH264 Video Codec." Force your CPU to encode. Your i7-12700K is a beast; it can handle a Discord stream in its sleep, and it bypasses the buggy NVIDIA Wayland sync entirely. B. The "Nuclear" Fix (X11) If you need to stream a high-stakes session tonight and can't afford to mess around, the most rational move is to switch back to X11 temporarily. Log out of your current session. At the login screen, look for a small icon or dropdown (usually at the bottom left). Select Plasma (X11). Why: X11 is the "legacy warehouse." It's not as fancy as the "automated" Wayland, but for NVIDIA users, it is 100% stable and flicker-free for streaming. Summary of your success so far: Nano Flags: You successfully forced the Ozone platform. Kernel Check: You confirmed modeset=Y (The engine is running). VRR Check: You confirmed VRR is set to Never (The tracks are clear). The only thing left is to decide if you want to keep fighting the Wayland "stutter" or if you want to swap to the i7's software encoding for a guaranteed smooth experience. Would you like me to help you check your Internet upload speed to make sure the "lag" isn't actually just a network bottleneck in Akron?
