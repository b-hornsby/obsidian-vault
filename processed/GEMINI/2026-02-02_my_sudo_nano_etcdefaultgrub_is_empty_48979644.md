---
category: homelab
date: 2026-02-02
id: 284107
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan discovered his GRUB configuration file was empty and was seeking help
  understanding why.
tags:
- grub-config
- cachyos
- bootloader
---
# my sudo nano /etc/default/grub is empty

### USER
my sudo nano /etc/default/grub is empty

### GEMINI
If /etc/default/grub is empty, you are likely using systemd-boot or Limine, which CachyOS often uses as a modern alternative to GRUB. Editing a non-existent GRUB config is a waste of time and won't do a thing. We need to find where your kernel parameters are actually stored. 1. Identify the Bootloader Run this command to see what’s actually booting your system: ls /boot/loader/entries/ If you see .conf files there, you are using systemd-boot. 2. The systemd-boot Fix If you saw files in that directory, follow these steps: Find your active entry: ls /boot/loader/entries/ (Look for the one that likely corresponds to your current CachyOS kernel). Edit the file: sudo nano /boot/loader/entries/[NAME_OF_FILE].conf Add the flag: Find the line that starts with options. Go to the very end of that line and add usbcore.autosuspend=-1. Save and Exit. (No "update" command is needed for systemd-boot). 3. The "CachyOS Way" (Kernel Command Line) Alternatively, CachyOS provides a tool to manage this safely. Try this: cat /proc/cmdline This shows you exactly what flags are currently active. If usbcore.autosuspend=-1 isn't in there, the kernel is still defaulting to its "save power and break the Yeti" mode. 4. Why your GRUB was empty You're likely on a high-performance filesystem setup (like XFS or ZFS with systemd-boot) where GRUB is considered legacy bloat. I should have caught that—CachyOS users usually opt for the faster boot path. Wait! Before you dig into boot files: Since you already installed tuned and set it to throughput-performance, try a reboot now. In many cases, tuned is smart enough to force the /sys/ entries to on as soon as the service starts, which might be "good enough" without the kernel flag. Reboot, then run: cat /sys/bus/usb/devices/1-28/power/control (Note: Your Yeti moved from 1-14 to 1-28 in your last lsusb. Use lsusb -t to find its current port number if it changed again). Does it say on now after the Tuned change and a reboot?
