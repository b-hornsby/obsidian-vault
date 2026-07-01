---
id: 204835
source: GEMINI
date: 2026-02-03
tags: ['obs-capture', 'window-capture', 'screen-capture']
category: streaming
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan was asking whether a capture method would allow capturing any window rather than a specific one in OBS.
---
# Will this allow me to use any window rather than a specific one?

### USER
Will this allow me to use any window rather than a specific one?

### GEMINI
In short: Yes, but it depends on the "Capture Method" you choose. Since you are on GNOME (Wayland) with an NVIDIA card, you have two distinct ways to capture windows, and they behave very differently: 1. Window Capture (PipeWire) — The "Flexible" Way On Wayland, this is the default. When you add a "Window Capture (PipeWire)" source and click "Select Window": The behavior: A system pop-up (the portal) will appear. You can click on any window currently open on your desktop to share it. The benefit: You aren't locked into a specific app until you actually click it in that pop-up. 2. Window Capture (Xcomposite) — The "Fixed" Way This is primarily for apps running through XWayland. The behavior: You choose a specific window from a dropdown menu inside OBS. The catch: If you close that specific window, the source goes black. It will not automatically pick up a different window unless it matches the title or class you previously set. Why this matters for your "Now Playing" Overlay If you are using a tool like Amuse or Pixel Chat, you shouldn't be using "Window Capture" at all. Use a Browser Source: This is a dedicated source inside OBS that only shows the music info. It doesn't require you to have a browser window visible on your monitor. The "Flicker" fix: If you use a Browser Source and it flickers, go to Settings > Advanced and uncheck "Enable Browser Source Hardware Acceleration." This is the most direct fix for your NVIDIA/Wayland setup. A Note on the "Missing Gear Icon" The reason you can't see the gear icon to switch to Xorg is often because GDM (your login screen) automatically hides it if it detects NVIDIA drivers that it thinks are incompatible with certain sessions. Would you like me to show you the terminal command to force your login screen to show that Xorg option? It requires editing a single config file (/etc/gdm/custom.conf).
