---
category: homelab
date: 2026-02-02
id: 338843
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan tried to reload the snd_usb_audio kernel module but failed because
  the module was in use.
tags:
- snd-usb-audio
- kernel-module
- audio-driver-reload
---
# ❯ sudo modprobe -r snd_usb_audio && sudo modprobe snd_usb_audio
[sudo] password for toastedmel0n: 
modprobe: FATAL: Module snd_usb_audio is in use.

~
❯ 

### USER
❯ sudo modprobe -r snd_usb_audio && sudo modprobe snd_usb_audio
[sudo] password for toastedmel0n: 
modprobe: FATAL: Module snd_usb_audio is in use.

~
❯ 

### GEMINI
The module is "in use" because PipeWire is currently gripping it. It won't let go of the driver while the audio server is active. To force this reset, you have to kill the services first, swap the module, and then bring the services back up. Do exactly this, in this order: 1. The Nuclear Driver Reset Copy and paste this entire block to stop the audio stack, reload the kernel driver, and restart the stack: systemctl --user stop pipewire pipewire-pulse wireplumber && \ sudo modprobe -r snd_usb_audio && \ sudo modprobe snd_usb_audio && \ systemctl --user start pipewire pipewire-pulse wireplumber If the second line still says "In use": Something else (like a DAW, a browser with a mic open, or a game) is bypassing the standard audio stack. Close everything and try again. If it succeeds: Your Yeti should re-initialize. 2. Verify the Kernel's "Internal" View Once you've run the commands above, check if the kernel actually likes what it sees. Run: dmesg | grep -i "usb" | tail -n 15 Look for lines like New USB device found or Product: Blue Yeti. If you see "device not responding" or "error -110", no amount of driver resetting will fix a physically broken USB port. 3. The CachyOS Volume Check CachyOS often defaults new/reset devices to 0% volume or Muted at the hardware level (ALSA). Run: alsamixer Press F6 and select the Blue Yeti. Look for the "Capture" bar (press F4). If the bar says MM, it is muted. Press M to unmute. Use the arrow keys to crank the volume up to around 80. Where are we? Did the modprobe -r command finally go through after stopping the services? If so, check pavucontrol now—is the Yeti appearing in the Input Devices tab with a moving volume bar?
