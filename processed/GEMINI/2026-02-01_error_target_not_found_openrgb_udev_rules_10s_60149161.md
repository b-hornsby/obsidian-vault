---
category: homelab
date: 2026-02-01
id: 233266
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to install openrgb-udev-rules on CachyOS but is encountering
  a 'target not found' error, indicating a problem with package availability or configuration.
tags:
- cachyos
- openrgb
- udev-rules
- package-manager
- arch-linux
---
# error: target not found: openrgb-udev-rules

~ 10s
❯ 

### USER
error: target not found: openrgb-udev-rules

~ 10s
❯ 

### GEMINI
This is exactly where "playing it safe" with standard repositories fails you. You are on CachyOS, an Arch-based powerhouse, yet you're acting like you're on a restricted ecosystem. The openrgb-udev-rules package isn't in the main Arch repos; it’s in the AUR (Arch User Repository) or bundled within the OpenRGB package itself. If you just installed the binary and ignored the configuration, you’ve built a car and forgotten the keys. 1. The Direct Fix (The AUR) You need to use an AUR helper like paru (standard on CachyOS) or yay. Action: Run paru -S openrgb-udev-rules Alternative: If you prefer the all-in-one package, run paru -S openrgb. The AUR version usually handles the udev rules during installation. 2. The Manual "No Excuses" Fix If you don't want to mess with the AUR, do it manually. This takes 30 seconds and removes the dependency on a package manager: Create the file: sudo nano /etc/udev/rules.d/99-openrgb.rules Paste the rules: Go to the official OpenRGB udev file and paste the content in. Reload the system: sudo udevadm control --reload-rules sudo udevadm trigger 3. Identify Your Blind Spot: Is the hardware even visible? You're trying to fix the detection of the device, but you haven't confirmed if the OS can even see the bus. Run this command right now: ls /dev/i2c-* If it says "No such file or directory": Your modprobe didn't stick or failed silently. Your kernel doesn't even know I2C exists. If it lists devices (/dev/i2c-0, etc.): The driver is fine; it's a permission/rules issue. Next Step: Run ls /dev/i2c-* and tell me the result. If it's empty, we need to look at your kernel logs (dmesg | grep i2c) to see why the hardware is rejecting the driver. Which one is it?
