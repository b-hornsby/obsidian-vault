---
id: 099093
source: GEMINI
date: 2026-02-02
tags: ['pipewire', 'wpctl', 'audio-device', 'linux-audio', 'grep']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is using `wpctl status` and `grep` to find information about a device named 'Yeti' in his PipeWire audio setup.
---
# ❯ wpctl status | grep -i "Yeti"

~
❯ 

### USER
❯ wpctl status | grep -i "Yeti"

~
❯ 

### GEMINI
Total silence from wpctl. This confirms the hardware is there (kernel level) but the audio server (PipeWire/WirePlumber) is completely blind to it. Since we've already cleaned up the udev rules, we are now down to the CachyOS audio stack failing to bind the driver. 1. The "Resuscitation" Script Let's skip the small talk and force the system to re-bind the Yeti to the ALSA driver. Run this entire block: # Force the kernel to 'unbind' and 'rebind' the Yeti without unplugging it DEV_BUS=$(lsusb -d 046d:0ab7 | awk '{print $2":"$4}' | sed 's/://') echo "$DEV_BUS" | sudo tee /sys/bus/usb/drivers/usb/unbind sleep 1 echo "$DEV_BUS" | sudo tee /sys/bus/usb/drivers/usb/bind # Now kick PipeWire to see the 'new' device systemctl --user restart pipewire pipewire-pulse wireplumber 2. Check the "Zombie" logs If the command above doesn't work, we need to see why PipeWire is rejecting it. Run this and look for red text: journalctl --user -u pipewire -u wireplumber --since "5 minutes ago" Look for lines like: failed to open ALSA device Device or resource busy (This means another app is hogging the mic) Protocol error 3. The "Pro Audio" Profile Wipe Sometimes a corrupted config file in your user directory tells PipeWire to "ignore" the Yeti. Run: mv ~/.config/pulse ~/.config/pulse.old 2>/dev/null rm -rf ~/.local/state/pipewire/* systemctl --user restart pipewire The Brutal Reality Check: If lsusb shows the device but wpctl status remains empty even after the unbind/bind trick, your Yeti is likely failing the USB Descriptor request. This is a hardware-level "stutter" where the mic says "I'm a Yeti" but fails to provide the list of audio formats it supports. Run the unbind/bind block in Step 1. Does wpctl status | grep -i "Yeti" return anything now?
