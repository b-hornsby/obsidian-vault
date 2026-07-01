---
category: homelab
date: 2026-02-03
id: 629392
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to install the linux-cachyos-nvidia kernel using pacman but
  the target is not found.
tags:
- pacman
- linux-cachyos-nvidia
- package-installation
- target-not-found
- kernel
---
# ❯ sudo pacman -S linux-cachyos-nvidia
error: target not found: linux-cachyos-nvidia

~
❯ 

### USER
❯ sudo pacman -S linux-cachyos-nvidia
error: target not found: linux-cachyos-nvidia

~
❯ 

### GEMINI
The reason that command failed is because CachyOS recently changed their package structure for the 590 driver series. You are "stuck" on the Open drivers because GSP is mandatory for them, which is exactly what is causing your flickering. If you want the proprietary driver (to finally disable GSP and stop the flickering), you have to use a different package name or the CachyOS Hardware Tool. The "Advisor" Plan to Kill the Flicker 1. The Direct Command Since linux-cachyos-nvidia was not found, try the DKMS version. This is the "Universal" proprietary driver for CachyOS. Run: sudo pacman -S nvidia-dkms nvidia-utils lib32-nvidia-utils nvidia-settings When it asks to remove nvidia-open-dkms or linux-cachyos-nvidia-open, say YES. Crucial: After it finishes, run sudo mkinitcpio -P to make sure your boot image is updated. 2. The "CachyOS Hello" Way (Safer) If the terminal is giving you a headache, CachyOS has a built-in tool for this: Open the CachyOS Hello app. Go to Driver Manager or Gaming Packages. Look for the toggle to switch from NVIDIA Open to NVIDIA Closed/Proprietary. Apply and reboot. Once you are on the Proprietary Driver: Now, that "empty" file you created earlier (/etc/modprobe.d/nvidia.conf) will finally work. Ensure it still has this line: options nvidia NVreg_EnableGpuFirmware=0 Reboot. Run nvidia-smi -q | grep "GSP Firmware". If it says N/A, the flickering in OBS will be gone. The "Right Now" Reality If you don't want to mess with drivers anymore today, your only flicker-free option is: Go to Settings -> Displays. Turn OFF Variable Refresh Rate (VRR). Set both monitors to 144Hz (Syncing them to the same speed). Do you want to try the nvidia-dkms command, or would you rather use the "CachyOS Hello" app to switch drivers?
