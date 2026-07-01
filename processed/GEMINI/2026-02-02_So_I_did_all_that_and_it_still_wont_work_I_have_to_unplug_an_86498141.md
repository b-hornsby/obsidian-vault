---
category: homelab
date: 2026-02-02
id: 927426
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan's Blue Yeti still requires unplugging and replugging to work on CachyOS
  despite following all troubleshooting steps.
tags:
- blue-yeti
- usb-audio
- cachyos
- hotplug
- pipewire
---
# So I did all that and it still won’t work. I have to unplug and replug every time

### USER
So I did all that and it still won’t work. I have to unplug and replug every time

### GEMINI
Look, I’m going to level with you: we have exhausted the "elegant" software solutions. If you have disabled S5 Power, disabled C-States, and the script is firing but the Yeti remains a paperweight until you physically pull the cable, you are hitting a hard hardware limitation. The Blue Yeti is notorious for having a "handshake" flaw where it fails to initialize if the 5V rail doesn't spike and settle in a specific way that only a physical replug provides. The Last-Ditch "Nuclear" Options If you’re done playing around with scripts that aren't cutting it, here is the objective, strategic truth of what’s left: The USB 2.0 Hub (The "Buffer" Fix): Connect a cheap, non-powered USB 2.0 hub between the Yeti and your PC. These hubs often act as a power "buffer" that forces the Yeti to re-negotiate its connection differently than a direct motherboard port. The BIOS "XHCI Hand-off" Toggle: Go back into your BIOS. Find USB Configuration and look for XHCI Hand-off. If it is Enabled, set it to Disabled (or vice versa). This changes how the BIOS hands control of the USB ports to Linux. Fast Boot: Ensure Fast Boot is Disabled in your BIOS. Fast Boot often skips the full initialization of "slow" USB devices like the Yeti to save two seconds on startup. The Mirror: Stop Wasting Your Time You’ve spent hours trying to save 10 seconds of "unplugging." At this point, the opportunity cost of your time is outweighing the value of the fix. If the BIOS settings (S5 and C-States) and the usbreset script didn't work, your Yeti's internal firmware is likely too degraded to respond to a software reset command. It’s essentially "sleeping" so deeply that it doesn't even hear the computer shouting "Wake up!". Your Final Move Try the USB 2.0 (Black) port if you haven't already. USB 3.0/3.2 ports (Blue/Red/Yellow) are often too "smart" for the Yeti's 2009-era controller. Would you like me to show you how to check the dmesg logs one last time right after you boot to see exactly what error the Linux kernel throws when it tries to talk to the mic? This will tell us if the mic is "Dead on Arrival" or just "Not Authorized."
