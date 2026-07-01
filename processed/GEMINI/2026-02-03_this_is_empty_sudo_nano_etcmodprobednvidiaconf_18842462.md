---
category: homelab
date: 2026-02-03
id: 883469
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan found the nvidia modprobe config file empty and was seeking guidance
  on what to do next for NVIDIA driver configuration.
tags:
- nvidia
- modprobe
- config-file
- cachyos
- driver-setup
---
#  this is empty? sudo nano /etc/modprobe.d/nvidia.conf

### USER
 this is empty? sudo nano /etc/modprobe.d/nvidia.conf

### GEMINI
It’s empty because you're creating the file for the first time. On Arch-based systems like CachyOS, if a configuration doesn't exist, the folder modprobe.d just stays empty or holds a few default files. You aren't "editing" a file; you are creating the override. However, there is a major catch with CachyOS: if you are using the nvidia-open drivers (which CachyOS often defaults to for newer cards), you cannot disable the GSP firmware. It will just ignore your file. Step 1: Check if you can even disable it Run this command: nvidia-smi -q | grep "GSP Firmware" If it says N/A, it’s already disabled. If it shows a Version Number, it’s active. If you are using nvidia-open (check with pacman -Qs nvidia-open), this firmware is mandatory. Step 2: If it's NOT N/A, do the "Nuclear" Fix If you want to try disabling it to stop the flickering: Open that empty file again: sudo nano /etc/modprobe.d/nvidia.conf Paste this exact line: options nvidia NVreg_EnableGpuFirmware=0 Save and Exit: (Ctrl+O, Enter, Ctrl+X). REGENERATE your boot image (Critical Step): sudo mkinitcpio -P Reboot. The Brutal Truth: Why you are still flickering If the screen still flickers after this, it is your dual 165Hz monitors + GNOME Wayland. When you have a high-refresh monitor, Wayland and NVIDIA often have "sync misses" where they can't decide who gets to draw the next frame. This is a known bug in GNOME 49's compositor. If the GSP fix fails, do this immediately: Open Settings -> Displays. Turn OFF Variable Refresh Rate (Adaptive Sync). Set both monitors to 120Hz or 144Hz (anything lower than the max 165Hz). Does nvidia-smi show a version number for GSP, or does it say N/A? That tells us if the "empty file" trick will even work.
