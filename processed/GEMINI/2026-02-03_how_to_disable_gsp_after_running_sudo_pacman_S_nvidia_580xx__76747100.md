---
category: homelab
date: 2026-02-03
id: 205399
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking how to disable the GPU System Processor (GSP) after installing
  NVIDIA drivers, indicating he wants to configure his GPU settings.
tags:
- nvidia
- gsp
- gpu-firmware
- linux-drivers
- cachyos
---
# how to disable gsp after running sudo pacman -S nvidia-580xx-dkms nvidia-580xx-utils lib32-nvidia-580xx-utils nvidia-settings

### USER
how to disable gsp after running sudo pacman -S nvidia-580xx-dkms nvidia-580xx-utils lib32-nvidia-580xx-utils nvidia-settings

### GEMINI
Now that you have installed the proprietary (closed) drivers, the "GSP handshake" is finally under your control. On the "Open" drivers you were using before, the system would have ignored your request to disable it. Step 1: Confirm the GSP Fix Since you already created the file earlier, let's make sure it's active. Open the file one last time: sudo nano /etc/modprobe.d/nvidia.conf Ensure it contains exactly this line: options nvidia NVreg_EnableGpuFirmware=0 Save and Exit: (Ctrl+O, Enter, Ctrl+X). REGENERATE the boot image: (This is the step most people miss). sudo mkinitcpio -P Reboot your PC. Step 2: Verify it Worked After you reboot, run the command you used earlier: nvidia-smi -q | grep "GSP Firmware" If it says N/A: Success. The flickering in OBS should now be dead because the GPU is no longer "napping" or using the buggy firmware sync. If it still shows a version number: CachyOS might be loading the nvidia_drm module too early. We’ll need to add the parameter to your Kernel Boot Line instead (let me know if this happens). Step 3: The "Finish Line" Strategy If GSP is finally N/A but you see even a tiny flicker, it's down to your dual 165Hz monitors. Do these two things in your GNOME settings to lock it in: Disable VRR: Go to Settings > Displays and turn off Variable Refresh Rate. Force Performance: Open a terminal and run: nvidia-settings -a "[gpu:0]/GPUPowerMizerMode=1" (This keeps the RTX 3070 at full power while OBS is open so the frames don't drift). What does nvidia-smi -q | grep "GSP Firmware" say now? If it says N/A, open OBS and tell me if that strobe-light effect has finally stopped.
