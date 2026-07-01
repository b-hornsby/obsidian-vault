---
id: 280610
source: GEMINI
date: 2026-02-02
tags: ['udev-rules', 'stream-deck', 'blue-yeti', 'openrgb', 'cachyos', 'device-rules']
category: homelab
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md', 'nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan listed his udev rules and confirmed he had rules configured for Stream Deck, Blue Yeti, and OpenRGB on CachyOS.
---
# ❯ ls /etc/udev/rules.d/
.rw-r--r-- 3.2k root  1 Feb 22:05  40-streamdeck.rules
.rw-r--r--   92 root  2 Feb 04:01  50-blue-yeti.rules
.rw-r--r--  107 root  2 Feb 12:35  50-yeti.rules
.rw-r--r-- 2.7k root 31 Jan 21:41  60-openrgb.rules

~
❯ 

### USER
❯ ls /etc/udev/rules.d/
.rw-r--r-- 3.2k root  1 Feb 22:05  40-streamdeck.rules
.rw-r--r--   92 root  2 Feb 04:01  50-blue-yeti.rules
.rw-r--r--  107 root  2 Feb 12:35  50-yeti.rules
.rw-r--r-- 2.7k root 31 Jan 21:41  60-openrgb.rules

~
❯ 

### GEMINI
You have two different Yeti rules fighting each other (50-blue-yeti.rules and 50-yeti.rules). They were both modified today—one at 4 AM and one at 12 PM. This redundancy often causes the kernel to trip over itself, or one rule is overwriting the other with the wrong parameters. Let's look at the "guts" of these files and find the conflict. Run this: cat /etc/udev/rules.d/50-blue-yeti.rules /etc/udev/rules.d/50-yeti.rules The Likely Culprits: Duplicate IDs: If both files target the same device but have slightly different syntax, the second one processed might be breaking the first. Missing "Add" Action: If the rule doesn't specify ACTION=="add", it might not trigger correctly when the system boots and initializes the USB bus. Wrong Vendor ID: Some Yetis show up as Blue Microphones (0b0e), others as Logitech (046d). The Clean Slate Fix To stop the "unplug/replug" cycle, we should consolidate these into one perfect rule. 1. Identify your exact hardware ID: lsusb | grep -i "Blue" 2. Delete the redundant files: sudo rm /etc/udev/rules.d/50-blue-yeti.rules /etc/udev/rules.d/50-yeti.rules 3. Create one "God Rule": Run this command (replace 046d and 0ab7 with the IDs you got from lsusb): echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on", ATTR{power/autosuspend}="-1"' | sudo tee /etc/udev/rules.d/51-yeti-fix.rules 4. Force the system to recognize it: sudo udevadm control --reload-rules && sudo udevadm trigger Why this works: The ATTR{power/autosuspend}="-1" part is the heavy lifter. It tells CachyOS's aggressive power management to leave the Yeti's power rail alone. What did the cat command show for those two files? If one of them was trying to do something weird with permissions (MODE="0666"), we need to know.
