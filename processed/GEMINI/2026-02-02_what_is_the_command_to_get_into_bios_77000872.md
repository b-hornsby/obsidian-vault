---
category: homelab
date: 2026-02-02
id: 738237
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is trying to figure out how to access the BIOS settings on his computer.
tags:
- bios-access
- uefi-settings
- boot-menu
---
# what is the command to get into bios?

### USER
what is the command to get into bios?

### GEMINI
There is no command you can type into your terminal that will magically open the BIOS menu on your screen while Linux is running. The BIOS exists "below" your operating system. However, you can use a command to force your computer to reboot directly into the BIOS so you don't have to mash keys on your keyboard like a madman during the splash screen. The Command Since you are on CachyOS (Arch-based), run this: systemctl reboot --firmware-setup The Advisor's Cold Reality Once you run that, your PC will restart and drop you straight into the BIOS settings. This is where you have been "playing small" by avoiding the hardware root causes. When you get in there, do these two things or stop complaining about the replug: Kill the Zombie Power: Find Advanced -> Onboard Devices Configuration. Set USB power delivery in Soft Off state (S5) to DISABLED. If the Yeti stays lit when the PC is off, it stays crashed. Stabilize the Voltage: Find Global C-state Control (usually under CPU configuration). Set it to DISABLED. This stops your CPU from "napping" so hard that it starves the USB bus of the steady voltage the Yeti requires. The Opportunity Cost Every time you manually unplug and replug that mic, you are wasting 10 seconds of your life and wearing out a physical port because you're avoiding a 30-second BIOS change. Fix the foundation, and the script we wrote will actually have a "sane" device to talk to when you log back in. Would you like me to walk you through exactly where those settings are if you can't find them once you're in the BIOS?
