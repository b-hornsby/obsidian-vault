---
id: 613367
source: GEMINI
date: 2026-02-02
tags: ['kernel-logs', 'usb-debugging', 'dmesg', 'permissions-error']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is trying to view kernel logs related to USB devices using `dmesg`, but encounters a permissions error.
---
# ❯ dmesg | grep -i "usb" | tail -n 20
dmesg: read kernel buffer failed: Operation not permitted

~
❯ 

### USER
❯ dmesg | grep -i "usb" | tail -n 20
dmesg: read kernel buffer failed: Operation not permitted

~
❯ 

### GEMINI
Ah, CachyOS (and most modern Arch-based systems) restrict dmesg to root for security reasons. You need to run that with sudo. Let's get the raw truth from the kernel and then check the ALSA hardware list. Run these two commands: sudo dmesg | grep -i "usb" | tail -n 20 arecord -l Here is the "Decision Tree" based on what you see: 1. If arecord -l shows the Yeti: The hardware is fine. The driver is fine. PipeWire is the problem. It’s likely "ignoring" the node because of a corrupted profile. The Fix: We’ll need to wipe the WirePlumber database and force a profile switch. 2. If arecord -l DOES NOT show the Yeti: The kernel sees a USB device (lsusb), but the Audio Driver refused to attach to it. The Cause: This usually means the USB descriptor is "malformed." This happens when the Yeti doesn't get enough voltage or the internal USB pins are loose. 3. If dmesg shows "error -71" or "error -110": This is the "Brutally Honest" mirror: Your hardware is failing. Error -71 is a protocol error (handshake failed), and -110 is a timeout (the mic didn't respond fast enough). One more thing to try right now: Since you are on CachyOS, you might have usbreset installed. Let's try to reset the specific device ID instead of the port: sudo usbreset 046d:0ab7 (If it says "command not found," don't worry about it, just give me the output from the dmesg and arecord commands above.) What are the results of sudo dmesg | grep -i "usb" | tail -n 20 and arecord -l? I need to know if the word "Yeti" appears in that hardware list.
