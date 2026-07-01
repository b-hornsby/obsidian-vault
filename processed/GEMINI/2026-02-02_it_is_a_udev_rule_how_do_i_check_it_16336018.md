---
category: homelab
date: 2026-02-02
id: 372253
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to check a udev rule, likely related to troubleshooting
  a hardware issue.
tags:
- udev-rules
- linux
- system-administration
---
# it is a udev rule. how do i check it?

### USER
it is a udev rule. how do i check it?

### GEMINI
To check your existing udev rules, you need to look in the directory where custom rules are stored. On CachyOS (and all Arch-based systems), that is /etc/udev/rules.d/. 1. List and Read the Rules Run this command to see every custom rule file you have: ls /etc/udev/rules.d/ Once you see the filenames (it's likely named something like 99-yeti.rules or audio.rules), read the contents with cat: cat /etc/udev/rules.d/[FILENAME_YOU_FOUND] 2. What you are looking for A functioning Yeti rule should look like this (the IDs might differ slightly depending on your specific Yeti model): SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on" If the file is empty or missing, that’s why it stopped working. You probably lost it during an update or a system migration. 3. How to verify the "ID" is still correct If the rule exists but isn't working, your Vendor or Product ID might be different. Run: lsusb | grep -i "Blue" You will see something like: Bus 001 Device 004: ID 046d:0ab7 Logitech, Inc. Blue Microphones Yeti 046d is the idVendor 0ab7 is the idProduct Check your rule file against those numbers. If they don't match, the rule is firing for a device that isn't there. 4. How to "Force Apply" the rule right now Instead of rebooting to see if the rule works, tell the system to reload and trigger them immediately: sudo udevadm control --reload-rules && sudo udevadm trigger What is inside that file? Paste the contents here, or if the directory is empty, tell me the ID from lsusb and I'll give you the exact command to recreate it in one shot.
