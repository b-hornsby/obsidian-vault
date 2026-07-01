---
id: 864061
source: GEMINI
date: 2026-02-03
tags: ['kde', 'kwin', 'wayland', 'window-manager', 'cachyos']
category: homelab
sentiment: curious
resolution: resolved
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is confirming that KDE's KWin Wayland window manager is working correctly on his CachyOS setup.
---
# the wm for kde here is WM: KWin (Wayland) but it works?

### USER
the wm for kde here is WM: KWin (Wayland) but it works?

### GEMINI
In the world of NVIDIA Linux, you just transitioned from a "black box" (GNOME Mutter) to a "glass box" (KDE KWin). The reason KWin (Wayland) works for you while GNOME flickered like a strobe light is due to two massive technical advantages KDE integrated in late 2025 and early 2026: 1. The "Explicit Sync" Handshake GNOME 49 and the NVIDIA driver often have a "race condition" where they can't agree on when a frame is finished. GNOME: If the frame isn't ready at the exact microsecond requested, it sometimes shows the previous frame or a black frame, causing the flicker. KDE: KWin 6.2+ uses Explicit Sync. It tells the GPU, "Don't show this frame until I give you the 'Go' signal." This eliminates the out-of-order frames that cause flickering on your RTX 3070. 2. Smarter "Direct Scanout" As we discussed, "Fullscreen Windowed" mode was killing you on GNOME. The KDE Difference: KWin has a more mature implementation of Direct Scanout and Triple Buffering. If it detects that a borderless window is going to cause a sync error, it "fails gracefully" back to composited mode instead of letting the screen flicker. One Final "Advisor" Optimization Since you are on Wayland and it's working, do not touch the drivers again. You are in a stable state. However, to ensure your stream stays 100% smooth, do these three things inside KDE: Check for "Allow Tearing": Go to System Settings > Display & Monitor. Ensure "Allow legacy apps to scale themselves" is checked (this stops XWayland apps from looking blurry). Ensure "Adaptive Sync" is set to Never (unless you are actively gaming and not streaming). The OBS "PipeWire" Rule: In OBS, only use Screen Capture (PipeWire) or Window Capture (PipeWire). Since you are on Wayland, the old "Xcomposite" window capture won't work or will be laggy. The "Max Performance" Lock: Even though it's working now, run your power lock one last time to be safe: nvidia-settings -a "[gpu:0]/GPUPowerMizerMode=1" The Brutal Truth You didn't "lose" anything; you just upgraded your engine. GNOME's "minimalism" was actually hiding the settings you needed to stop the flicker. In KDE, you have the most advanced Wayland compositor for NVIDIA users currently in existence. Is your OBS "Now Playing" overlay and your game both visible and flicker-free now? If so, you are officially ready to go live.
