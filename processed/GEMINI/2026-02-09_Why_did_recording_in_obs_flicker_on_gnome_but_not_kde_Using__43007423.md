---
category: streaming
date: 2026-02-09
id: 378138
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was trying to understand why OBS recording flickered on GNOME but not
  KDE on CachyOS.
tags:
- obs
- flicker
- gnome
- kde
- wayland
- cachyos
---
# Why did recording in obs flicker on gnome but not kde? Using cachyos 

### USER
Why did recording in obs flicker on gnome but not kde? Using cachyos 

### GEMINI
The reason you're seeing flicker on GNOME but not KDE while using CachyOS typically comes down to how each desktop environment (DE) handles Explicit Sync and PipeWire buffer management, especially if you are on an NVIDIA GPU. Since CachyOS is aggressive with kernel and driver updates (often running the latest 6.x kernels and NVIDIA 555+ drivers), you are likely caught between two different implementations of Wayland protocols. 1. The Explicit Sync Gap The most common cause of "flicker" on Linux right now is the transition to Explicit Sync. KDE Plasma (6.1+): KDE was the first to fully implement the linux-drm-syncobj-v1 protocol. This allows the GPU to tell the compositor exactly when a frame is ready. Without this, frames can appear out of order, leading to the "stroboscopic" flickering you see in OBS. GNOME (Mutter): GNOME's implementation of explicit sync has historically lagged slightly behind KDE's or handled "legacy" (implicit) syncing differently. If GNOME is falling back to implicit sync while your CachyOS kernel/NVIDIA driver is expecting explicit, you get flickering in the screen-share buffer (PipeWire). 2. Mutter vs. KWin (The Compositors) Mutter (GNOME): GNOME’s compositor is known for being more restrictive. It often forces a specific "damage tracking" method. If a window doesn't update its entire surface, Mutter might only send partial "dirty" regions to OBS. On some drivers, this results in flickering between the new frame and a black or old frame. KWin (KDE): KWin is generally more "gamers-first" and has more toggles for direct scan-out and tearing. On CachyOS, KWin often defaults to settings that bypass the issues Mutter still struggles with regarding PipeWire stream consistency. 3. Wayland vs. XWayland If you are recording a game: In GNOME, games often run through XWayland. If GNOME's XWayland implementation isn't perfectly synced with its Wayland compositor, the "bridge" to OBS (via PipeWire) will flicker. KDE has specific optimizations for XWayland (like "Allow applications to block compositing") that often stabilize the frame delivery to OBS. How to Fix it on GNOME If you want to stay on GNOME but lose the flicker, try these steps in order: Check for NVIDIA Explicit Sync: Ensure you are on NVIDIA driver 555 or newer. Then, ensure your GNOME version is 46.1+, which contains the necessary Mutter patches. Use "Screen Capture (PipeWire)" specifically: In OBS, do not use "Window Capture (X11/GDI)". Ensure you are using the PipeWire source. Disable "Allow Flipping" (NVIDIA users): Sometimes the "Flip Queue" causes the flicker. You can try disabling "Allow Flipping" in the NVIDIA Settings (though this is harder on Wayland). Use GPU Screen Recorder: If OBS remains broken, try gpu-screen-recorder. It’s available in the CachyOS repos and often bypasses desktop compositor flickering by capturing directly from the GPU buffer. Would you like me to help you check your current driver and GNOME versions to see if you're missing a specific sync patch?
