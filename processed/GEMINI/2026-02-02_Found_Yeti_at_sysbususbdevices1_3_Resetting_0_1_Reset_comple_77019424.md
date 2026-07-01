---
id: 204369
source: GEMINI
date: 2026-02-02
tags: ['blue-yeti', 'usb', 'linux', 'device-reset', 'troubleshooting']
category: streaming
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is observing the system resetting his Blue Yeti microphone at a specific USB device path, likely as part of a troubleshooting process.
---
# Found Yeti at /sys/bus/usb/devices/1-3. Resetting...
0
1
Reset complete.

~
❯ 

### USER
Found Yeti at /sys/bus/usb/devices/1-3. Resetting...
0
1
Reset complete.

~
❯ 

### GEMINI
That "Reset complete" confirms the logic works. You’ve just successfully "replugged" the mic without moving. Now, we need to see if the audio server finally grabbed the handshake. Run this command right now: wpctl status | grep -i "Yeti" 1. If it appears: We’ve identified the problem: your Yeti is too slow for the CachyOS boot speed. It needs a "kick" after the system is already up. To automate this so you never run that script again, we should add that logic to a startup script. 2. If it STILL doesn't appear: We need to check if the kernel is throwing an error during that reset. Run: dmesg | tail -n 20 Look for New USB device found or any lines in red. 3. The Permanent "Next Level" Fix Since you mentioned you had a command that ran every boot, this is likely what you were doing. Instead of a manual script, we can bake a delay into your PipeWire configuration or create a simple systemd service that runs that "Reset" loop 5 seconds after you log in. Is the Yeti appearing in wpctl status or pavucontrol now? If it is, would you like me to help you turn that "Electronic Replug" into a permanent startup service so this problem dies forever?
