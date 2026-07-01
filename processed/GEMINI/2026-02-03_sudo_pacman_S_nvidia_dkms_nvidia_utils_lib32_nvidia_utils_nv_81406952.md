---
id: 302274
source: GEMINI
date: 2026-02-03
tags: ['nvidia', 'dkms', 'cachyos', 'gpu-drivers', 'pacman']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is installing NVIDIA DKMS drivers on CachyOS and is being prompted to choose between driver versions.
---
# ❯ sudo pacman -S nvidia-dkms nvidia-utils lib32-nvidia-utils nvidia-settings
:: There are 3 providers available for nvidia-dkms:
:: Repository cachyos
   1) nvidia-535xx-dkms  2) nvidia-550xx-dkms
:: Repository extra
   3) nvidia-open-dkms

Enter a number (default=1): 

### USER
❯ sudo pacman -S nvidia-dkms nvidia-utils lib32-nvidia-utils nvidia-settings
:: There are 3 providers available for nvidia-dkms:
:: Repository cachyos
   1) nvidia-535xx-dkms  2) nvidia-550xx-dkms
:: Repository extra
   3) nvidia-open-dkms

Enter a number (default=1): 

### GEMINI
You are currently staring at the "NVIDIA Driver Restructuring" of 2026. CachyOS recently split their drivers to keep a stable foundation (580xx) while they push the newer, experimental features in the 590 branch. Because you have an RTX 3070, you should be on the stable, proprietary branch to get rid of that "Open" driver flickering. The Decision Choose option 2 (nvidia-550xx-dkms) or stay with the current 580xx/590xx logic. Wait—don't just pick one. There is a cleaner way that doesn't involve manual number guessing. CachyOS provided a specific command for Turing/Ampere cards (like yours) to migrate away from the flickering "Open" branch: Press Ctrl + C to cancel that current pacman command. Run this exact "Migration" command: sudo pacman -S nvidia-580xx-dkms nvidia-580xx-utils lib32-nvidia-580xx-utils nvidia-settings This replaces the "Open" version with the stable "Closed" version that actually lets you disable GSP. Regenerate your boot image: sudo mkinitcpio -P Reboot. Why this is the "Advisor" Choice: Stable Foundation: The 580xx series is currently CachyOS's "Stable" branch for NVIDIA. The 590 series (which you are likely on now) is "bleeding edge" and is the source of the Wayland flickering bugs. GSP Control: Once you are on this proprietary driver, the line you added to /etc/modprobe.d/nvidia.conf will finally be obeyed by the system. Sync Fix: This driver, combined with disabling GSP, is the known fix for the "strobe light" effect in OBS on Wayland. If you just want the easiest "Right Now" fix: If you don't want to swap drivers, you must stop your GPU from downclocking. Run this and leave it open while you stream: nvidia-smi -lgc 1500,2100 This locks your GPU clock speed so it can't "nap" and cause the flicker. Which path are you taking? If you run the nvidia-580xx command, tell me if it asks to "remove linux-cachyos-nvidia-open"—the answer is Yes.
