---
category: general
date: 2026-02-02
id: 500276
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is troubleshooting screen flickering in Vesktop, having tried one suggested
  solution related to XWayland without success.
tags:
- vesktop
- screen-flickering
- xwayland
- wayland
- electron-app
---
# did step one, still flickers 1. The XWayland Problem
Vesktop, being an Electron app, often defaults to XWayland. When you share a Wayland screen through an XWayland window, the buffer swap causes the flicker.
The Fix: Force Vesktop to run natively on Wayland.

Close Vesktop completely.
Launch it from the terminal with these flags to see if the flicker stops:vesktop --enable-features=UseOzonePlatform --ozone-platform=wayland
If this works, edit your .desktop file or use Flatseal (if using Flatpak) to make these environment variables permanent.

### USER
did step one, still flickers 1. The XWayland Problem
Vesktop, being an Electron app, often defaults to XWayland. When you share a Wayland screen through an XWayland window, the buffer swap causes the flicker.
The Fix: Force Vesktop to run natively on Wayland.

Close Vesktop completely.
Launch it from the terminal with these flags to see if the flicker stops:vesktop --enable-features=UseOzonePlatform --ozone-platform=wayland
If this works, edit your .desktop file or use Flatseal (if using Flatpak) to make these environment variables permanent.

### GEMINI
If native Wayland flags didn't kill the flicker, you’re likely dealing with a frame timing mismatch between GNOME’s compositor and Electron’s rendering engine. Since you're on CachyOS, you're likely on the latest kernel and drivers—which means "stable" defaults might actually be your enemy here. Stop poking at the surface and address the underlying pipe. 1. The "Experimental" Toggle (The Most Likely Culprit) Vesktop has its own internal handling for screen capture that often conflicts with GNOME’s PipeWire implementation. Open Vesktop Settings. Go to Vencord Settings (not the standard Discord settings). Find Plugins. Search for "FakeScreenShare" or "ScreenShare Settings". Disable "Use Electron Capturer". Enable "Experimental PipeWire Capturer" (if available). 2. Force Disable Hardware Acceleration I know you're on CachyOS for performance, but Electron's GPU acceleration is notorious for flickering on Wayland/GNOME when sharing buffers. Relaunch with: vesktop --disable-gpu The Logic: If this stops the flicker, the issue is Explicit Sync. Your GPU is pushing frames before the compositor is ready to draw them. If this works, you'll need to decide if you'd rather have a slightly laggier UI or a flickering stream. 3. Check for Portal Conflict GNOME 49 is strict. If you have xdg-desktop-portal-wlr or xdg-desktop-portal-kde installed alongside the GNOME portal, they will fight for the stream. Run: pacman -Qs xdg-desktop-portal If you see anything other than -gnome and -gtk, remove the others. Restart the portal: systemctl --user restart xdg-desktop-portal-gnome 4. XWayland Video Bridge (If all else fails) If you absolutely cannot get Native Wayland to behave, you may need the xwaylandvideobridge. While usually for KDE, some GNOME users on Arch-based systems use it to bridge the gap for Electron apps. Install: sudo pacman -S xwaylandvideobridge Reboot and try sharing again. The Reality Check You're trying to use a patched, third-party Discord client on a rolling-release, performance-tuned Arch derivative. Stability is not guaranteed. If the --disable-gpu flag works, your "high-performance" setup is actually the bottleneck because the drivers aren't syncing correctly with Electron. What to do now: Try the --disable-gpu flag. Tell me if the flicker remains. If it disappears, we need to look at your NVIDIA/AMD environment variables or your Mutter (GNOME's window manager) configuration. Which GPU are you currently running?
