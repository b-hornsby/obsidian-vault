---
category: homelab
date: 2026-02-02
id: 402424
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was clarifying that rebooting did not fix his USB device issue and
  he still has to physically unplug the device.
tags:
- usb-power
- device-persistence
- cachyos
---
# no i mean i rebooted and it still didnt work i still have to unplug

### USER
no i mean i rebooted and it still didnt work i still have to unplug

### GEMINI
If you rebooted and it still didn't work, we have officially moved past a "software configuration" issue and into a Hardware Power State issue. Because you are still seeing "Permission denied" when running the script, the script is not firing correctly during your startup sequence. But more importantly, the Yeti is staying in a "crashed" state during the reboot because of your BIOS settings. 1. The Critical BIOS Fix (Do this first) Look at the photos you sent me earlier. Your motherboard is keeping the Yeti in a "zombie" state. Go to BIOS -> Advanced -> Onboard Devices Configuration. Change "USB power delivery in Soft Off state (S5)" to DISABLED. Why? If the red light on your mic stays on when the PC is off, the mic never resets. It stays "stuck" in the error state it fell into during the last session. You need the mic to lose power completely so it can "cold boot" with the kernel quirk we added. 2. The "Permission Denied" Fix The script failed because visudo is very picky. If the path to usbreset is even slightly different, it will block the command. Run this: which usbreset If it returns /usr/bin/usbreset, then your visudo is correct, but your script needs to call it with sudo. Run this to fix the script once and for all: sudo printf "#!/bin/bash\nsleep 10\nsudo /usr/bin/usbreset 046d:0ab7\n" | sudo tee /usr/local/bin/reset_yeti.sh > /dev/null && sudo chmod 755 /usr/local/bin/reset_yeti.sh 3. The Advisor's Cold Reality If you refuse to change the S5 Power setting in the BIOS, you are wasting your time with the script. The script tries to "talk" to the mic, but if the mic is frozen due to a power-on crash, it won't respond to the reset command. Your Priority Plan: BIOS: Disable S5 USB Power and Global C-state Control. Physical: Move the Yeti to a USB 2.0 (Black) port if it's currently in a Blue/Red one. Reboot: After logging in, wait 15 seconds. Did you change the S5 Power setting to Disabled yet? That is the single most important step for this specific hardware.
