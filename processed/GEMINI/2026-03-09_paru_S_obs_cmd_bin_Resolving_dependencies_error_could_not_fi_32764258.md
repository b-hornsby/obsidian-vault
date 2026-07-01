---
category: streaming
date: 2026-03-09
id: 825814
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is encountering an error while trying to install obs-cmd-bin using
  the paru package manager because the package cannot be found.
tags:
- paru
- package-manager
- obs-cmd
- dependency-error
- cachyos
---
# ❯ paru -S obs-cmd-bin
:: Resolving dependencies...
error: could not find all required packages:
    obs-cmd-bin (target)

~
❯ 

### USER
❯ paru -S obs-cmd-bin
:: Resolving dependencies...
error: could not find all required packages:
    obs-cmd-bin (target)

~
❯ 

### GEMINI
Ah, that's because you were looking for obs-cmd-bin. In the AUR, it is simply named obs-cmd. Try this: paru -S obs-cmd Why paru couldn't find it: The -bin suffix is common in the AUR for pre-compiled packages, but this specific tool is small enough that the maintainer just named it obs-cmd. It will download and compile the Rust source code for you automatically. If it still fails (The "Brutal Advisor" Backup): If for some reason you don't want to wait for Rust to compile, or if paru gives you more lip, you can use the official OBS wayland-hotkeys plugin. It’s arguably more "native" to your CachyOS/KDE setup: Install the Plugin: paru -S obs-wayland-hotkeys-git Launch OBS: You’ll see a prompt asking to register global shortcuts. Map the Keys: Go to System Settings → Shortcuts → Global Shortcuts. You will see a new entry for "OBS Studio" there. Map your Replay Buffer Save key in the System Settings, not inside OBS. Strategic Advice: You're a Linux enthusiast on CachyOS; don't settle for the X11 "Legacy" band-aid. It’s a performance tax you shouldn't pay. Using obs-cmd or the wayland-hotkeys plugin keeps your recording pipeline clean and your framerates high for Apex and Fortnite. Once you get obs-cmd installed, would you like me to give you the exact command to test your connection to the OBS WebSocket?
