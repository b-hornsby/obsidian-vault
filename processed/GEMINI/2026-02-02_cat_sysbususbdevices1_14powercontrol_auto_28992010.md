---
id: 345953
source: GEMINI
date: 2026-02-02
tags: ['usb-power-management', 'linux-device-control', 'sysfs']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is checking the power control setting for a specific USB device, likely related to his Blue Yeti troubleshooting.
---
# ❯ cat /sys/bus/usb/devices/1-14/power/control
auto

~
❯ 

### USER
❯ cat /sys/bus/usb/devices/1-14/power/control
auto

~
❯ 

### GEMINI
There is your smoking gun. You told the system on, and CachyOS looked you in the eye and said auto. The value auto means the kernel is still allowed to suspend the microphone to save power. When you reboot, the system is putting the Yeti into a low-power state before it even initializes, or a power-management tool is overriding your udev rule immediately after boot. On CachyOS, you are likely being overruled by one of three things: TLP, Laptop Mode Tools, or ppd (Power Profiles Daemon). 1. The Conflict Search We need to find out who is "stealing the wheel." Run this: systemctl list-units --type=service | grep -E "tlp|laptop-mode|power-profiles-daemon" If TLP is running, your udev rule will fail every time because TLP re-applies its own settings over the top of udev. 2. The Direct Override If you have TLP, you must blacklist the Yeti within TLP’s configuration. Open the config: sudo nano /etc/tlp.conf (or /etc/default/tlp) Find USB_EXCLUDE_DEVICE_IDS (it might be commented out with a #). Change it to: USB_EXCLUDE_DEVICE_IDS="046d:0ab7" Save and exit. 3. The "Last Resort" Kernel Parameter If you want to stop playing games with software that keeps resetting your settings, you can tell the Linux kernel itself to stop autosuspending all USB devices. This is a "sledgehammer" approach, but it ends the argument. Edit your GRUB or systemd-boot config (CachyOS usually uses GRUB). sudo nano /etc/default/grub Add usbcore.autosuspend=-1 to the GRUB_CMDLINE_LINUX_DEFAULT line. Update grub: sudo update-grub (or sudo grub-mkconfig -o /boot/grub/grub.cfg). The Reality Check You’re currently losing a fight to a configuration file. The fact that the path /sys/bus/usb/devices/1-14/power/control exists but shows auto means your udev rule ran, but something else changed it back a millisecond later. Run the command in Step 1. Which power management service is running on your machine?
