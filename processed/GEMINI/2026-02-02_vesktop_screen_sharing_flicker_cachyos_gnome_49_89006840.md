---
category: homelab
date: 2026-02-02
id: 538438
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was experiencing screen sharing flicker in Vesktop on CachyOS with
  GNOME 49.
tags:
- vesktop
- screen-sharing
- flickering
- gnome-49
- wayland
---
# vesktop screen sharing flicker cachyos gnome 49

### USER
vesktop screen sharing flicker cachyos gnome 49

### GEMINI
The flickering you're experiencing on Vesktop (CachyOS/GNOME) is a classic symptom of the Wayland-XWayland bridge conflict, likely exacerbated by GNOME 49’s frame scheduling or NVIDIA drivers if you’re using them. You’re likely trying to run a performance-heavy OS but letting a basic Electron configuration bottleneck your workflow. Here is the cold reality of the fix. 1. The XWayland Problem Vesktop, being an Electron app, often defaults to XWayland. When you share a Wayland screen through an XWayland window, the buffer swap causes the flicker. The Fix: Force Vesktop to run natively on Wayland. Close Vesktop completely. Launch it from the terminal with these flags to see if the flicker stops: vesktop --enable-features=UseOzonePlatform --ozone-platform=wayland If this works, edit your .desktop file or use Flatseal (if using Flatpak) to make these environment variables permanent. 2. PipeWire & Portal Check CachyOS is bleeding edge. If your xdg-desktop-portal-gnome is misconfigured or clashing with xdg-desktop-portal-gtk, the screen capture stream will stutter. The Fix: Ensure only one backend is primary. For GNOME, you need xdg-desktop-portal-gnome. Verify PipeWire is handling the stream correctly: systemctl --user status pipewire wireplumber In Vesktop Settings, go to Vencord > Settings > Screen Share and toggle "Use Electron Screen Capture" OFF. You want to use the WebRTC PipeWire stream. 3. Hardware Acceleration & NVIDIA If you are on an NVIDIA GPU, GNOME 49 and Wayland still have "Explicit Sync" nuances. Flickering is often the result of the app and the compositor disagreeing on when a frame is ready. The Fix: Disable Hardware Acceleration in Vesktop’s general settings as a test. If the flickering stops, the issue is your driver's interaction with Electron’s GPU cache. Clear the Cache: rm -rf ~/.config/vesktop/GPUCache. Corrupt shaders from a CachyOS update frequently cause flickering. Comparison of Solutions MethodEffortLikely SuccessDownsideWayland FlagsLowHighPotential cursor offset issuesDisable HW AccelLowMediumHigher CPU usagePortal ResetMediumHighAffects all screen-sharing apps The Advisor's Verdict You are running CachyOS—a distro optimized for performance—yet you're letting a standard Discord wrapper stutter. If you haven't enabled Explicit Sync (available in recent Mutter/NVIDIA updates), you are leaving stability on the table. Your next step: Run the terminal command in Step 1. Does the flickering persist in the terminal output, or does the UI stabilize? Once you confirm, I can give you the specific configuration lines to hardcode into your system.
