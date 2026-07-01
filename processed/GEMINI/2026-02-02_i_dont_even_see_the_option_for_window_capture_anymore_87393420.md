---
id: 317936
source: GEMINI
date: 2026-02-02
tags: ['obs-studio', 'window-capture', 'source-missing', 'cachyos', 'streaming']
category: streaming
sentiment: frustrated
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/personal/streaming.md']
summary: Bryan couldn't find the window capture option in OBS Studio on CachyOS.
---
# i dont even see the option for window capture anymore

### USER
i dont even see the option for window capture anymore

### GEMINI
This is a classic "Wayland Portal" crash. When we enabled the VRR flag and rebooted, the communication between OBS and the GNOME desktop portal broke. In Wayland, the "Window Capture" option only exists if the xdg-desktop-portal service successfully handshakes with OBS at startup. If it's missing, OBS thinks it's running on a system that doesn't support PipeWire. 1. The "Resuscitation" Command We need to force-restart the services that provide those capture options. Run this in your terminal: systemctl --user restart xdg-desktop-portal-gnome xdg-desktop-portal Now, open OBS. Do you see "Screen Capture (PipeWire)" back in the + menu? 2. If it's still missing: Force the Wayland Platform Sometimes OBS on CachyOS defaults to "X11 mode" (XWayland) if the environment variables aren't set, which hides the Wayland-only PipeWire options. Launch OBS from the terminal with this specific flag: QT_QPA_PLATFORM=wayland obs 3. The "Permissions" reset If you still see nothing, GNOME might have "blacklisted" the capture request because of the previous flickering/crashing. Close OBS. Run: rm -rf ~/.config/obs-studio/plugin_config/linux-pipewire Restart OBS. The Advisor's Brutal Truth You are learning the hard way why "experimental" flags are called experimental. Enabling VRR on GNOME 49 with an NVIDIA card often causes the Portal to crash. If the portal crashes, OBS has no way to "see" your windows. The Strategy: If the capture options come back after Step 1 or 2, DO NOT turn VRR back on. Keep it off. If the options are still missing, the experimental flag we set earlier might have corrupted the Mutter (GNOME's window manager) state. We might need to revert it. Next step: Run the systemctl restart command above and then launch OBS with the QT_QPA_PLATFORM=wayland flag. Do the capture options (Screen/Window PipeWire) reappear in the list?
