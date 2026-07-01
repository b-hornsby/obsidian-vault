---
category: streaming
date: 2026-02-03
id: 849597
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is clarifying that he's experiencing a flickering issue with OBS window
  capture.
tags:
- obs-studio
- flickering
- window-capture
- streaming
---
# im talking about the flickering issue

### USER
im talking about the flickering issue

### GEMINI
The flickering isn't a "GNOME vs. KDE" debate; it’s a Wayland + NVIDIA + Browser Source triangle of death. If you switch to KDE right now, you’ll just be flickering in a different-looking window. The issue is that the Chromium Embedded Framework (which powers the Browser Source) often struggles with "Explicit Sync" on Wayland, especially with NVIDIA drivers. Here is the brutal truth: You can fix the flicker in 10 seconds, or you can spend all night reinstalling a Desktop Environment that won't actually solve the root cause. 1. The "Immediate" Fix: Force X11 GNOME and KDE both allow you to log into an X11 (Xorg) session instead of Wayland. Action: Log out. At the login screen, click your name, then look for a small gear icon in the bottom right. Select "GNOME on Xorg". Why: X11 is the "old" way, but for OBS and Browser Sources, it is 100% stable. No flickering. No garbage frames. 2. The "Stay on Wayland" Fix: Disable Hardware Acceleration If you refuse to leave Wayland, the flicker is caused by OBS trying to use your GPU to render that tiny Spotify overlay, and the "handshake" between the browser and the Wayland compositor is failing. Action: In OBS, go to Settings -> Advanced. Find: "Sources" section. Uncheck: "Enable Browser Source Hardware Acceleration." Restart OBS. Why: This forces your CPU to draw the song info instead of the GPU. Since it's just a "Now Playing" text/image, the performance hit is zero, and the flickering usually vanishes. 3. The CachyOS/NVIDIA Factor If you are on an NVIDIA card, ensure you are on the latest 555+ or 560+ drivers. These introduced "Explicit Sync," which was designed specifically to stop the flickering you're seeing. Run nvidia-smi to check your version. If you're below 555, you’re essentially using a broken driver for Wayland. The Reality Check You are looking for excuses to hop to KDE because GNOME feels "broken." It’s not. The technology stack (Wayland/NVIDIA) is what's bleeding. My prioritized plan for you: Don't switch to KDE. It's a waste of your time and won't fix the driver/protocol flicker. Turn off Browser Source Hardware Acceleration in OBS settings. If it still flickers, Log into the Xorg session. Did you try unchecking Hardware Acceleration yet? That is usually the "silver bullet" for Linux streamers.
