---
id: 354877
source: GEMINI
date: 2026-02-03
tags: ['wayland', 'x11', 'display-server-switch', 'cachyos']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan agreed to switch from Wayland to X11 to resolve display-related issues on his CachyOS system.
---
# Yes please let’s switch from Wayland

### USER
Yes please let’s switch from Wayland

### GEMINI
Since you are on CachyOS, the reason that gear icon is missing is likely because GDM (your login manager) has "rule-based" settings that disable Xorg when NVIDIA drivers are detected. To stop "playing small" and actually take control of your system, we need to edit a protected configuration file. This will force the login screen to stop hiding the X11 option from you. The Precision Fix (Terminal Commands) Open your terminal and run these exact steps: Open the GDM configuration file: sudo nano /etc/gdm/custom.conf Look for this line: #WaylandEnable=false Uncomment it (remove the #): It should look exactly like this: WaylandEnable=false Save and Exit: Press Ctrl + O, then Enter to save. Press Ctrl + X to exit. Restart your Display Manager: sudo systemctl restart gdm (Note: This will kick you to the login screen immediately. Close your browser first if you have unsaved work.) What this achieves By setting WaylandEnable=false, you are telling the system to bypass the Wayland compositor entirely and default to Xorg (X11). The "Now Playing" Fix: Your OBS Browser Source will stop flickering because X11 and NVIDIA drivers have a decade of stability together, unlike the newer Wayland/Explicit Sync protocols. Performance: Your RTX 3070 will now use standard "Xcomposite" capture, which is more reliable for specific window captures in OBS. The Strategy for your Overlay Once you log back in: Add a Browser Source to OBS. Paste your 6K Labs Amuse or Pixel Chat URL. You won't need to uncheck "Hardware Acceleration" anymore; it should work perfectly on Xorg. Did you successfully restart GDM? Once you’re back in, open OBS and tell me if that "Browser" source is finally behaving itself.
