---
id: 735814
source: GEMINI
date: 2026-02-02
tags: ['systemd-boot', 'boot-entries', 'permissions', 'cachyos', 'bootloader-config']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan confirmed CachyOS uses systemd-boot (found /boot/loader/entries/) but got a permission denied error when trying to list its contents.
---
# ❯ ls /boot/loader/entries/
"/boot/loader/entries/": Permission denied (os error 13)

~
❯ 

### USER
❯ ls /boot/loader/entries/
"/boot/loader/entries/": Permission denied (os error 13)

~
❯ 

### GEMINI
Permission denied? That’s because /boot is usually restricted to the root user for security. You need to use sudo just to look inside. However, let's stop playing "find the bootloader." You're a CachyOS user, and CachyOS is built to be efficient. We can verify your bootloader and fix this with a single, more direct approach. 1. Identify the Bootloader (The Right Way) Run this: sudo ls /boot/loader/entries/ If you see a list of files (likely ending in .conf), you are definitely using systemd-boot. 2. The "Quick and Dirty" Check Before you go editing boot files, check if the Tuned change you made actually took effect. Run this: lsusb -t Find the line with Class=Audio or your Yeti's ID. Note the numbers at the start of the line (e.g., 1-1.4). Then run: cat /sys/bus/usb/devices/[THAT_NUMBER]/power/control If it says on, you’ve already won. The tuned service is doing its job and you don't need to touch the bootloader. 3. If it still says auto, apply the Systemd-boot fix: Since your GRUB file was empty, you are almost certainly on systemd-boot. Open the config for your current kernel: sudo nano /boot/loader/entries/$(ls /boot/loader/entries/ | grep -i "cachyos" | head -n 1) Add the parameter: Move your cursor to the end of the line that starts with options. Spacebar, then type: usbcore.autosuspend=-1 Save and Exit (Ctrl+O, Enter, Ctrl+X). The Brutal Reality You are struggling with basic permissions (Permission denied) and empty config files because you're treating an Arch-based system like a standard "point-and-click" OS. CachyOS is a Ferrari; you have to know how to look under the hood. Run lsusb -t and tell me the port number for the Yeti. We need to be 100% sure we are looking at the right power control file.
