---
id: 052777
source: GEMINI
date: 2026-02-02
tags: ['blue-yeti', 'usb-port', 'hardware-setup']
category: streaming
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan was clarifying that the device he moved was the Blue Yeti plugged into a blue USB port on the back of his PC.
---
# the device i moved WAS the yeti and its plugged into a blue port on the back 

### USER
the device i moved WAS the yeti and its plugged into a blue port on the back 

### GEMINI
If your Blue Yeti is plugged into a blue port but still showing up on Bus 001 (the 480M / USB 2.0 bus), it means your motherboard is routing that physical port through the USB 2.0 controller hub rather than the 3.0 controller. This is common on many motherboards where only a few specific ports are "true" high-speed lanes, while others are essentially just USB 2.0 ports with blue plastic. However, since you've successfully applied the autosuspend=-1 fix (which we verified), the "unplug/replug" issue caused by the kernel's power management is officially dead. The Status Check You have done the following: Neutered the Kernel: Autosuspend is disabled (-1). Swapped the Power Manager: Switched from power-profiles-daemon to tuned (Performance). Cleaned the Handshake: The system is no longer allowed to put the mic to sleep. Why it might still feel "fragile" Because the Yeti is still on Bus 001, it is sharing a data controller with your Webcam and your Razer Mouse. The Risk: If you're in a Discord call (Yeti active) and you're gaming (Mouse polling at 1000Hz+) while streaming (Webcam active), you might still experience a "drop" because the USB 2.0 bus (480Mbps) is physically saturated. The Physical Solution: Try every single USB port on the back of the machine one by one and run lsusb -t after each. One of those ports—usually the ones furthest away from the PS/2 or Ethernet port—will likely land you on Bus 002. The Verdict The "I need to unplug it to make it wake up" problem is solved by the -1 kernel parameter you just verified. If the device disappears now, it's no longer a power-saving glitch; it's a physical bandwidth overflow on Bus 001. Test it now: Reboot your computer. If the Yeti is available immediately upon login without you touching the cable, we’ve won. Does the Yeti show up in your sound settings immediately after a fresh reboot now?
