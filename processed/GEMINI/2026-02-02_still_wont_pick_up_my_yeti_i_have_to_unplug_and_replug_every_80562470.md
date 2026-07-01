---
category: homelab
date: 2026-02-02
id: 690359
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is still having issues with his Yeti microphone not being recognized
  and requiring unplugging and replugging.
tags:
- yeti-microphone
- audio-issue
- hardware-troubleshooting
- linux
---
# still won't pick up my yeti. i have to unplug and replug every time

### USER
still won't pick up my yeti. i have to unplug and replug every time

### GEMINI
If you have to physically unplug and replug the Yeti every time to make it work, you aren't dealing with a driver "crash"—you're dealing with a USB handshake failure or a power management conflict. The Yeti is an older USB 2.0 device. Modern Linux kernels (especially the high-performance ones in CachyOS) often try to "suspend" USB devices to save power, or the xHCI (USB 3.0+) controller on your motherboard is failing to "wake" the Yeti's aging firmware. Stop resetting the drivers; the drivers are fine, the connection is stale. Let's fix the root cause. 1. Disable USB Autosuspend (The likely culprit) Linux tries to be smart and puts USB devices to sleep. The Yeti hates this. Open your GRUB or systemd-boot config, but for a quick test, run this to disable it live: echo -1 | sudo tee /sys/bus/usb/devices/*/power/autosuspend (Note: This resets on reboot, but if it fixes the problem immediately, we can make it permanent.) 2. Check the "Pro Audio" Profile Bug I’ve seen this a dozen times on Arch/CachyOS. PipeWire sees the Yeti but assigns it the "Pro Audio" profile, which often fails to initialize the input stream until a "hard" replug forces a re-scan. Install/Open pavucontrol. Go to Configuration. Set the Blue Yeti to Analog Stereo Duplex. Crucial: If it’s already on that, switch it to Off, wait 3 seconds, and switch it back to Analog Stereo Duplex. 3. The Hardware Logic: The "Lazy" Port Are you using a USB Hub? If yes, stop. The Yeti is power-hungry and sensitive to voltage drops. Plug it directly into the back of the motherboard. Are you using a USB 3.0 (Blue/Red) port? If you have an old-school USB 2.0 (Black) port, use that. The Yeti’s controller is ancient and often fails the handshake on high-speed 3.1/3.2 ports. 4. Direct ALSA Override Sometimes PipeWire/WirePlumber is the middleman causing the lag. Let's see if the hardware is alive at the base level without a replug. Run this: arecord -D hw:CARD=Yeti,DEV=0 -f S16_LE -r 44100 -c 2 /dev/null If it records (no error): The hardware is fine; PipeWire/WirePlumber is simply failing to "route" it. If it says "No such file or directory" or "Device busy": The kernel has lost the device mapping. The Brutal Truth: If lsusb shows the Yeti but pavucontrol shows no input bars until you replug, your WirePlumber session manager is hanging. Try this next time it happens (instead of replugging): wpctl set-profile $(wpctl status | grep -i "Yeti" | perl -ne 'print $1 if /(\d+)/') 1 (This forces the PipeWire profile to reset via command line.) Does the Yeti appear in lsusb even when it's "not picking up," or does it disappear from the list entirely?
