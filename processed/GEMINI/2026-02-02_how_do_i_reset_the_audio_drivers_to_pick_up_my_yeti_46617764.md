---
id: 013501
source: GEMINI
date: 2026-02-02
tags: ['blue-yeti', 'audio-drivers', 'cachyos', 'pipewire', 'usb-audio']
category: homelab
sentiment: frustrated
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md', 'nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was trying to reset audio drivers to get his Blue Yeti microphone recognized on CachyOS.
---
# how do i reset the audio drivers to pick up my yeti

### USER
how do i reset the audio drivers to pick up my yeti

### GEMINI
On Linux (and specifically CachyOS), we don't "reinstall drivers" like on Windows because the drivers are baked into the kernel. Instead, we reset the audio state and force the PipeWire/WirePlumber stack to re-index your hardware. Follow this exact sequence to purge any hung configurations and force a fresh "handshake." 1. Wipe the PipeWire/WirePlumber Cache Sometimes WirePlumber (the session manager) "remembers" a corrupted state for a specific USB device. Clearing the state forces it to treat the Yeti as a brand-new device. Run this in your terminal: rm -rf ~/.local/state/wireplumber/* systemctl --user restart pipewire pipewire-pulse wireplumber 2. Force-Reload the Kernel Module If the kernel's USB audio driver is stuck in an error state, restarting the software won't help. You need to kick the driver itself. Unplug the Yeti. Run this to reload the driver: sudo modprobe -r snd_usb_audio && sudo modprobe snd_usb_audio Plug the Yeti back in. 3. Check for "Pro Audio" vs. "Analog Stereo" CachyOS/Arch often defaults to a "Pro Audio" profile for devices like the Yeti. While it sounds better, many apps can't handle the way "Pro Audio" maps channels, resulting in "no sound." Open pavucontrol (if you don't have it, sudo pacman -S pavucontrol). Go to the Configuration tab. Find your Yeti. Change the Profile to Analog Stereo Duplex. If it is already on that, toggle it to Off and then back to Analog Stereo Duplex. 4. The "Brutally Honest" Hardware Check If the steps above don't work, we need to stop blaming software. Run this command while the mic is plugged in: dmesg | tail -n 20 How to read the results: If you see "New USB device found": The drivers are fine. The issue is in your volume mixer (check if the input is muted in pavucontrol). If you see "device descriptor read/64, error -110" or "error -71": Your Yeti is dying. Those are physical communication errors. It means the USB port on the mic is loose or the cable isn't providing enough voltage. Run dmesg | tail -n 20 and tell me if you see any red text or "error" messages.
