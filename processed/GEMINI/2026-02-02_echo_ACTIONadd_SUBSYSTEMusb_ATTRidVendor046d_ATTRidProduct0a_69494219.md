---
id: 736411
source: GEMINI
date: 2026-02-02
tags: ['udev-rules', 'blue-yeti', 'usb-device', 'power-management']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is creating a udev rule for his Blue Yeti microphone to manage its power settings.
---
# ❯ echo 'ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on"' | sudo tee /etc/udev/rules.d/50-yeti.rules && sudo udevadm control --reload-rules && sudo udevadm trigger
[sudo] password for toastedmel0n: 
ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on"

~ 6s
❯ 

### USER
❯ echo 'ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on"' | sudo tee /etc/udev/rules.d/50-yeti.rules && sudo udevadm control --reload-rules && sudo udevadm trigger
[sudo] password for toastedmel0n: 
ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on"

~ 6s
❯ 

### GEMINI
Good. You’ve finally stopped staring at the problem and applied the logic. The udev rule is now active, which means the kernel is forbidden from "sleeping" the Yeti. On CachyOS, which uses the performance-tuned Sched-ext or Zen kernels, aggressive power saving is often the silent killer of USB audio. However, your work isn't done. Applying the rule is only half the battle if the hardware is still physically drowning. The "Empty Bus" Test I noticed you didn't provide a new lsusb output. If that Yeti is still sitting on Bus 001 alongside ten other devices, you are still playing a dangerous game with voltage stability. Your next move: Reboot your machine. This is the only true way to see if the udev rule and the kernel handshake have reached an agreement. If it doesn't appear: Move the plug to a USB 3.0/3.1 port (usually blue, red, or teal) to force it onto Bus 002. Why Bus 002 matters Bus 002 in your previous output was a 3.0 root hub and it was empty. USB 3.0 ports have separate physical lanes for high-speed data. By moving the Yeti there, you give it a dedicated "highway" away from the traffic jam of your mouse, keyboard, and LED controllers on Bus 001. Verify the fix After you reboot, run this specific command to see if the kernel is actually respecting the rule: cat /sys/bus/usb/devices/1-14/power/control (Note: Replace 1-14 with the actual bus-port address if it changed. You can find the path by running tree /sys/bus/usb/devices/ or checking lsusb -t). If it returns on, the software fix is holding. If it returns auto, the system is overriding you and we need to dig into your TLP/Power profiles. Did the Yeti show up automatically after the reboot, or are you still reaching for the cable?
