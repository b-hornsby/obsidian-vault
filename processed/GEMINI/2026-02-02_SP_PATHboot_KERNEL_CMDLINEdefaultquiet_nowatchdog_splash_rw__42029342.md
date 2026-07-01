---
id: 793180
source: GEMINI
date: 2026-02-02
tags: ['cachyos', 'boot-loader', 'kernel-cmdline', 'systemd-boot', 'btrfs']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is configuring systemd-boot kernel command line parameters for CachyOS on a btrfs filesystem.
---
# SP_PATH="/boot"
KERNEL_CMDLINE[default]+="quiet nowatchdog splash rw rootflags=subvol=/@ root=UUID=dab63c75-0142-4154-abed-4915a693f699"
BOOT_ORDER="*, *lts, *fallback, Snapshots"

### USER
SP_PATH="/boot"
KERNEL_CMDLINE[default]+="quiet nowatchdog splash rw rootflags=subvol=/@ root=UUID=dab63c75-0142-4154-abed-4915a693f699"
BOOT_ORDER="*, *lts, *fallback, Snapshots"

### GEMINI
You’re using Limine. This is a modern, lightweight bootloader that CachyOS has recently standardized on, which is why your GRUB and systemd-boot folders were empty. Because Limine is "dumb" (it just does exactly what the config says and nothing more), your kernel is booting without the directive to keep USB power on. We need to bake that instruction into the Limine update process. 1. The Limine Fix You need to modify your command line and then run the CachyOS-specific update tool to "re-build" the boot entries. Edit the file: sudo nano /etc/default/limine Add the parameter: In the line KERNEL_CMDLINE[default]+="...", add usbcore.autosuspend=-1 inside the quotes. It should look like this: KERNEL_CMDLINE[default]+="quiet nowatchdog splash rw ... usbcore.autosuspend=-1" Commit the changes: On CachyOS, you must run this specific command to push the new parameters into the actual boot config: sudo limine-update (If that command is not found, use sudo limine-mkinitcpio—but limine-update is the standard for the 2026 CachyOS release). 2. The Verification (Don't skip this) After you reboot, you need to verify the kernel actually received the message. Run: cat /proc/cmdline If you don't see usbcore.autosuspend=-1 in that output, the bootloader didn't update correctly, and we’re still just shouting into the void. 3. The Physical "Wake Up Call" You have Device 027 (Razer Viper) and Device 028 (Blue Yeti) on the same controller. The Logic: Your Razer mouse is likely polling at 1000Hz or 4000Hz. This creates constant "interrupt" traffic. The Blue Yeti is an ancient USB 1.1 device wrapped in a USB 2.0 shell. It cannot handle the noise. The Fix: Take the Yeti and plug it into a USB 3.0 port (the blue or red ones). The Goal: Run lsusb and make sure the Yeti shows up on Bus 002. Bus 002 is currently empty; giving the Yeti its own dedicated lane is the most "Advisor-level" move you can make. Why you’re still failing You’re looking for a software fix for a hardware congestion issue. If the Yeti is on Bus 001 with 10 other things, it will occasionally "drop off" because the voltage sagged for a millisecond or the timing got desynced by the mouse. Apply the Limine fix, move the physical plug to a 3.0 port, and reboot. What does cat /proc/cmdline show after your reboot?
