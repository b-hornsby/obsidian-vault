---
category: homelab
date: 2026-02-02
id: 982029
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to run a command 'reutil' which is not recognized by his
  fish shell.
tags:
- fish-shell
- command-not-found
- shell-configuration
---
# ❯ reutil
fish: Unknown command: reutil

~
❯ 

### USER
❯ reutil
fish: Unknown command: reutil

~
❯ 

### GEMINI
It looks like I tried to give you a CachyOS-specific alias that didn't exist in your shell. Let's use the raw Linux commands that don't depend on aliases. Run this to get your motherboard info: cat /sys/devices/virtual/dmi/id/board_{vendor,name} (If that feels too messy, you can also try sudo dmidecode -s baseboard-product-name). Why this is the "Advisor" Move Since you're out of physical ports and don't have an adapter, we are in triage mode. Knowing the exact motherboard allows me to look at the block diagram of your chipset. I want to see if your "Blue" ports are being driven by the CPU or a secondary ASMedia/Realtek chip. Those secondary chips are notorious for "faking" USB 3.0 speeds while actually sharing a single tiny lane with things like your Ethernet or SATA controller. The Interim Plan Leave the edits. Your autosuspend=-1 is the only thing keeping that Yeti from being "soft-killed" by the OS. Musical Chairs: When you get a chance, move that Razer dongle to any other port. It is currently hogging the "cleanest" lane on your board (the USB-C one). The Mirror: You're frustrated that it "still won't work," but look at your dmesg. The system is recognizing the device now. The fact that it isn't "working" as an audio device points to a bandwidth collision. What motherboard are we dealing with? Give me that board_name and I'll find you a stable port.
