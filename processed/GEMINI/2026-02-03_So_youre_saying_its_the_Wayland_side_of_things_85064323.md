---
id: 663596
source: GEMINI
date: 2026-02-03
tags: ['wayland', 'display-server', 'troubleshooting', 'linux-desktop']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is confirming that a problem he's experiencing is related to the Wayland display server.
---
# So you’re saying it’s the Wayland side of things?

### USER
So you’re saying it’s the Wayland side of things?

### GEMINI
Yes, Wayland is the root cause of the specific flickering and capture behavior you are experiencing with an NVIDIA card. Because you are using an NVIDIA RTX 3070 on Wayland, you are dealing with a known protocol conflict between how NVIDIA's drivers handle "syncing" frames and how the Wayland compositor displays them. Why Wayland is the Problem Right Now The Flickering: This is caused by a lack of "Explicit Sync" support in older driver/compositor combinations, leading to frames being displayed out of order. The Browser Source: Chromium (which powers the OBS Browser Source) is notoriously unstable on Wayland when Hardware Acceleration is enabled. The Capture Method: On Wayland, "Window Capture (PipeWire)" is required to see any windows at all, but it adds a layer of permission pop-ups that you don't have to deal with on Xorg. Why the "Gearbox" is Missing The reason you don't see the option to switch to Xorg (X11) on your login screen is often because GNOME's display manager (GDM) hides it when it detects certain NVIDIA configurations. It effectively "locks" you into Wayland unless you manually force the config file to show the alternative. How to Fix the "Now Playing" Issue on Wayland If you stay on Wayland, you must change how you use OBS to avoid the flicker: Stop capturing a browser window. Instead, use the Browser Source directly in OBS. Kill the acceleration. Go to Settings > Advanced and uncheck "Enable Browser Source Hardware Acceleration." This forces the CPU to render the music info, which bypasses the NVIDIA/Wayland flickering bug entirely. Would you like the terminal command to force your login screen to show the Xorg (X11) option so you can leave Wayland behind? This is usually the most stable path for NVIDIA streamers on Linux.
