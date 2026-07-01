---
category: homelab
date: 2026-03-21
id: 758432
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan wants to ensure Vesktop always launches with forced native Wayland
  and is seeking instructions on how to configure this.
tags:
- vesktop
- wayland
- forced-launch
- application-configuration
---
# How do I make sure vesktop launches each time with forced native Wayland

### USER
How do I make sure vesktop launches each time with forced native Wayland

### GEMINI
To make these changes permanent, you need to modify the Desktop Entry file for Vesktop. On CachyOS (and Arch-based systems), system updates will overwrite files in /usr/share/applications/, so the "Pro" way to do this is to create a local override. Here is the exact process to "Full Send" these flags permanently: 1. Create a Local Override Copy the system's Vesktop shortcut to your local user folder. This ensures your changes stay even after a system update. mkdir -p ~/.local/share/applications/ cp /usr/share/applications/vesktop.desktop ~/.local/share/applications/ 2. Edit the File Open the file in a text editor (I'll use nano here, but you can use kate if you prefer a GUI): nano ~/.local/share/applications/vesktop.desktop 3. Modify the Exec Line Find the line that starts with Exec=. It likely just says Exec=vesktop %U. You need to change it to include the Wayland and GPU flags. Change it to exactly this: Exec=vesktop --enable-features=UseOzonePlatform,WaylandWindowDecorations --ozone-platform=wayland --enable-gpu-rasterization --enable-zero-copy %U (Note: Keep the %U at the end if it was there; it allows the app to open Discord links from your browser). To save in Nano: Press Ctrl + O, then Enter, then Ctrl + X. 4. Refresh the Database Tell KDE to look at your new local file instead of the system one: update-desktop-database ~/.local/share/applications/ Verification: How to know it worked? Once you launch Vesktop from your application menu: Open your terminal. Run: xlsclients The Goal: If Vesktop is NOT listed in the output of that command, it is running natively on Wayland. If it is listed, it's still stuck in XWayland. Why this is the "Best" way: Persistent: It won't break when you run pacman -Syu. Native: It forces Chromium (the engine) to stop using the X11 translation layer, which is the root cause of the flickering you described. Performance: The --enable-gpu-rasterization and --enable-zero-copy flags reduce the CPU overhead, which helps eliminate that lag your friends are seeing. Since you're on CachyOS, would you like me to show you how to check if your NVIDIA drivers are correctly using "Explicit Sync" to further kill that flickering?
