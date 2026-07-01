---
id: 624737
source: GEMINI
date: 2026-02-02
tags: ['arch-linux', 'package-management', 'pacman', 'xdg-desktop-portal']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is listing installed xdg-desktop-portal packages, likely as part of troubleshooting a screen sharing or permissions issue.
---
# ❯ pacman -Qs xdg-desktop-portal
local/xdg-desktop-portal 1.20.3-2.1
    Desktop integration portals for sandboxed apps
local/xdg-desktop-portal-gnome 49.0-1.1 (gnome)
    Backend implementation for xdg-desktop-portal for the GNOME desktop environment
local/xdg-desktop-portal-gtk 1.15.3-1.1
    A backend implementation for xdg-desktop-portal using GTK

~
❯ 

### USER
❯ pacman -Qs xdg-desktop-portal
local/xdg-desktop-portal 1.20.3-2.1
    Desktop integration portals for sandboxed apps
local/xdg-desktop-portal-gnome 49.0-1.1 (gnome)
    Backend implementation for xdg-desktop-portal for the GNOME desktop environment
local/xdg-desktop-portal-gtk 1.15.3-1.1
    A backend implementation for xdg-desktop-portal using GTK

~
❯ 

### GEMINI
Your pacman output confirms you have a clean setup: no conflicting portals from other desktop environments (like -wlr or -kde). You are using the standard GNOME and GTK backends, which is exactly where you want to be. The fact that a reboot fixed it confirms my suspicion: GNOME 49’s PipeWire state was likely hung. On rolling-release distros like CachyOS, if you update your kernel or Mesa drivers and don't reboot, the portal's communication with the GPU gets "noisy," leading to that rapid flickering. One Final Strategic Tweak Since you are on CachyOS (which pushes updates frequently), the flicker will eventually come back after a heavy update. Instead of rebooting every time, you can "kick" the portal back into gear manually. Add this to your .bashrc or .zshrc as an alias: alias fix-stream="systemctl --user restart xdg-desktop-portal-gnome xdg-desktop-portal-gtk xdg-desktop-portal" Next time it flickers, just run fix-stream in your terminal. It’s faster than a reboot and clears the "ghost" capture sessions that cause the flicker. Advisor's Final Mirror You solved it by cycling the system state, which is fine for now. But remember: your settings.json is currently bare-bones. You’ve disabled Hardware Acceleration, which fixes the flicker but increases your CPU load during streams. If you start seeing performance drops or lag in your games while streaming, it’s because your CPU is doing the work your GPU should be doing. Once you’re confident the system is stable, you might try re-enabling Hardware Acceleration in the JSON, but keep that fix-stream alias ready. Would you like me to show you how to check if your stream is actually using your GPU's encoder (VA-API) to save your CPU some stress?
