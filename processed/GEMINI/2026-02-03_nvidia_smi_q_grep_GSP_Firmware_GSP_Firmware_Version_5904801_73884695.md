---
id: 094402
source: GEMINI
date: 2026-02-03
tags: ['nvidia-smi', 'gsp-firmware', 'gpu-information']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is checking the GSP Firmware version using nvidia-smi, likely for troubleshooting or information gathering.
---
# ❯ nvidia-smi -q | grep "GSP Firmware"
    GSP Firmware Version                               : 590.48.01

~
❯ 

### USER
❯ nvidia-smi -q | grep "GSP Firmware"
    GSP Firmware Version                               : 590.48.01

~
❯ 

### GEMINI
The fact that you see a GSP Firmware Version means you are currently using the nvidia-open drivers (NVIDIA's open-source kernel modules). Here is the "advisor" level truth: On the nvidia-open driver, GSP firmware is mandatory. You cannot disable it. Your "empty file" trick will be ignored by the system as long as you're on this driver. The flickering you see is the GSP firmware "sleeping" and "waking up" because your music overlay is too "light" for it to stay in a high-performance state. The Brutal Final Plan (3 Paths) Path A: The "Switch Drivers" Move (Most Technical) To actually disable GSP, you have to switch from the "Open" driver to the "Proprietary" one. On CachyOS, this is a single command, but it carries a risk of breaking your boot again if not done right. Run: sudo pacman -S linux-cachyos-nvidia It will ask to remove linux-cachyos-nvidia-open. Say Yes. After it finishes, do not reboot yet. Run: sudo mkinitcpio -P Now reboot. Once you've done this, the NVreg_EnableGpuFirmware=0 line you put in that empty file will finally work. Path B: The "Power Mizer" Move (Easiest) If you don't want to risk the driver switch, force your card to stop "napping." Open your terminal. Run: nvidia-settings Go to GPU 0 -> PowerMizer. Change "Preferred Mode" to "Prefer Maximum Performance." Keep the nvidia-settings window open in the background while you stream. Path C: The "Dual Monitor" Sanity Check Since you have two 165Hz monitors, GNOME Wayland is likely struggling with the sync timing between them. Go to Settings > Displays. Turn OFF Variable Refresh Rate (VRR/G-Sync) on both. Set both monitors to 144Hz (just slightly below the max). My Recommendation Stop trying to "fix" Wayland for 30-series NVIDIA cards. It is currently a mess for OBS users. If Path B (Maximum Performance) doesn't stop the flicker, your system is fundamentally struggling with how Wayland handles frame "flipping" on NVIDIA. Try Path B first (it takes 5 seconds). Does "Prefer Maximum Performance" stop the strobe-light effect in OBS?
