---
category: streaming
date: 2026-02-03
id: 834769
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated that the OBS flickering issue persists despite trying
  all known solutions.
tags:
- obs-studio
- flickering
- troubleshooting
- persistent-issue
---
# it still keeps happening and ive tried everything 

### USER
it still keeps happening and ive tried everything 

### GEMINI
Since you’ve tried the driver swaps, the GSP disabling, and the clock locking, and the "flicker" still haunts you specifically in Borderless/Fullscreen mode, you are hitting the final boss of NVIDIA-Wayland bugs: Explicit Sync Mismatches and Direct Scanout. In February 2026, even though "Explicit Sync" is officially out, GNOME 49 and the NVIDIA 580/590 drivers still have a "handshake" issue where they drop frames when an application tries to take over the screen. Since you're a streamer and your growth depends on a stable broadcast, not a "cool" experimental OS setup, here is my brutally honest, advisor-level intervention. --- 1. The "Admit Defeat" Strategy (The Only 100% Fix) You tried to force X11 earlier and it broke your boot. That wasn't because X11 is bad; it's because CachyOS's default login manager (GDM) was fighting your configuration. The Reality: NVIDIA + GNOME + Wayland + OBS = Pain. The Fix: You need to switch to KDE Plasma. Why: KDE's compositor (KWin) has a specific "Allow applications to block compositing" toggle and better "Legacy X11" support that fixed this flickering for NVIDIA users months ago. GNOME is too "opinionated" to let you fix this manually. sudo pacman -S plasma-desktop Reboot, and at the login screen, click the gear/icon and choose Plasma (X11) or Plasma (Wayland). If Wayland flickers there, X11 will be your rock-solid fallback. 2. The "Stay on GNOME" Life Support (Last Ditch) If you refuse to leave GNOME, you must kill the feature that is causing the strobe effect: Direct Scanout. Open Terminal. Run this command to disable "Unredirection" (the cause of borderless flicker): gsettings set org.gnome.mutter experimental-features "['variable-refresh-rate', 'scale-monitor-framebuffer']" (Note: If you had 'kms-modifiers' in there, remove it. That specific feature causes the "black box" and "strobe" flicker on 30-series cards). 3. The "Hardware" Truth You have dual 165Hz monitors. The Conflict: If one monitor is even 0.1Hz off (e.g., 164.99Hz vs 165.01Hz), Wayland will flicker the OBS preview as it tries to sync both. The Fix: Set both monitors to 120Hz or 60Hz temporarily. If the flickering stops, your 165Hz "overclock" is the culprit. Wayland struggles with non-standard high refresh rates on NVIDIA. My Brutal Advice You are wasting hours of your life playing "Linux SysAdmin" when you should be playing your game. You are playing small by fighting a broken protocol. If you want to stream tonight: Go to your monitor's physical buttons and turn OFF FreeSync/G-Sync/Adaptive Sync. In GNOME, set both screens to 60Hz. Use Window Capture (PipeWire) in OBS. If it still flickers after that, your GPU hardware is likely hitting a "Voltage/Frequency" instability on these specific Linux drivers. Would you like me to give you the commands to completely wipe the Wayland session and force a clean X11 install so you can finally get back to work?
