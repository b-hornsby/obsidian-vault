---
id: 441237
source: GEMINI
date: 2026-02-02
tags: ['pavucontrol', 'pulseaudio', 'audio-control', 'cachyos', 'missing-package']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan discovered he didn't have pavucontrol installed and needed it for audio management on CachyOS.
---
# i dont have pavucontrol

### USER
i dont have pavucontrol

### GEMINI
If you're on CachyOS, you're likely using a modern Desktop Environment like KDE Plasma or GNOME, which has its own built-in sound settings. However, without pavucontrol, you are flying blind—you can't see the internal routing conflicts that are causing this. Install it now. It is the "gold standard" for troubleshooting PipeWire. sudo pacman -S pavucontrol Once installed, open it (pavucontrol) and go to the Input Devices tab. If the Yeti is there but the bar isn't moving, check the Configuration tab and ensure the Yeti is set to "Analog Stereo Duplex" and not "Pro Audio." The "Brutal" Summary of Your Situation: The Handshake: Your Yeti is failing to initialize during the boot sequence because CachyOS is too fast. The Fix: The "Electronic Replug" script we ran earlier proved that the hardware works if you "kick" the USB port after the OS has loaded. The Conflict: You have multiple nodes (47, 75, 77) because PipeWire keeps trying to find the Yeti and failing. Your Final, Bulletproof Plan: Since you don't want to unplug/replug every time, you need to automate the "kick." Add this to your Startup Applications (Autostart) as a script or command: sh -c "sleep 5; wpctl set-mute (wpctl status | grep -i 'Yeti' | grep -oP '\d+' | head -n 1) 0; wpctl set-volume @DEFAULT_AUDIO_SOURCE@ 0.6" If that doesn't work after a reboot, do you want me to write a one-click "Yeti Fix" desktop icon for you that you can just double-click whenever it acts up?
