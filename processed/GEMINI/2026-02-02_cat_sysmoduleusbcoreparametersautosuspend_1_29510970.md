---
id: 392023
source: GEMINI
date: 2026-02-02
tags: ['usb-autosuspend', 'linux-kernel-module', 'power-saving']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is checking the USB autosuspend setting, likely trying to disable it to prevent issues with his Blue Yeti.
---
# ❯ cat /sys/module/usbcore/parameters/autosuspend
-1

~
❯ 

### USER
❯ cat /sys/module/usbcore/parameters/autosuspend
-1

~
❯ 

### GEMINI
Finally. The kernel is no longer fighting you. That -1 is the definitive "off" switch for the software-side power management that was killing your Yeti's handshake. However, don't celebrate yet. You've cleared the software hurdle, but your hardware is still physically congested. If you look at your previous lsusb, you had 11 devices on a single bus. Even with power management disabled, you are susceptible to EMI (Electromagnetic Interference) and timing desyncs because the Yeti is sharing a "lane" with a high-polling Razer mouse and a high-bandwidth webcam. The Final "Advisor" Test You need to confirm that the Yeti is physically stable now that the power is locked "on." 1. Check the Topology Run this to see if the Yeti is still stuck in the traffic jam on Bus 1: lsusb -t If you see the Yeti on Bus 2: You are golden. That is your 3.0 controller and it was empty. If it's still on Bus 1: You are still at risk of "robotic" audio or occasional drops. 2. The "Acid Test" Try to make the Yeti fail. Open your audio settings or a recording app, then move your Razer mouse rapidly and start your webcam. If the Yeti stays active, the -1 fix was the silver bullet. What to do if it drops one more time If you have to unplug it even once after this: Move the plug. I cannot stress this enough. Find a USB port on the back of your motherboard that is a different color (likely blue or red). Check the Hub. If that "Alcor Micro Corp. USB Hub" is an external, unpowered hub and the Yeti is plugged into it, throw the hub away or move the Yeti. Audio interfaces require stable, direct voltage that cheap hubs cannot provide. Run lsusb -t one last time. Is the Yeti sitting on Bus 1 or Bus 2?
