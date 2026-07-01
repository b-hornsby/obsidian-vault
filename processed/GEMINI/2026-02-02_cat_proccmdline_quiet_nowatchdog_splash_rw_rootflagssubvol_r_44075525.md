---
id: 307896
source: GEMINI
date: 2026-02-02
tags: ['kernel-parameters', 'boot-options', 'linux-configuration']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is checking the kernel command line parameters, possibly to diagnose boot issues or understand system configuration.
---
# ❯ cat /proc/cmdline
quiet nowatchdog splash rw rootflags=subvol=/@ root=UUID=dab63c75-0142-4154-abed-4915a693f699

~
❯ 

### USER
❯ cat /proc/cmdline
quiet nowatchdog splash rw rootflags=subvol=/@ root=UUID=dab63c75-0142-4154-abed-4915a693f699

~
❯ 

### GEMINI
Based on your cat /proc/cmdline, you are not using GRUB or systemd-boot. As of January 2026, CachyOS has switched to Limine as the default bootloader. This is why those other config files were empty or missing. Since your current command line is "clean" (just the basics like quiet and splash), your Yeti is getting shut down by the kernel's default power management before the OS even fully loads. 1. The Limine Fix (The "Pro" Way) To permanently stop the kernel from suspending your USB devices, you need to add the parameter to Limine's configuration. Open the Limine config: sudo nano /etc/default/limine Find the line: KERNEL_CMDLINE["linux-cachyos"] (or the default one). Add the flag: Append usbcore.autosuspend=-1 inside the quotes. It should look like: KERNEL_CMDLINE["linux-cachyos"]="quiet splash ... usbcore.autosuspend=-1" Sync the changes: sudo limine-mkinitcpio Note: This command is specific to CachyOS to ensure the Limine entries are actually updated. 2. The "I just want it to work now" Way If you don't want to mess with bootloaders yet, you can use the CachyOS Kernel Manager (the GUI tool). Open CachyOS Kernel Manager from your app menu. Look for a "Command Line" or "Parameters" section. Add usbcore.autosuspend=-1. Apply/Execute. 3. The "Traffic Jam" Reality Check I’m looking at your device list again. You have Device 027 (Razer Mouse) and Device 028 (Blue Yeti) right next to each other on the same hub. The Problem: High-polling gaming mice (like your Viper V3 Pro) flood the USB bus with data. The Result: The Yeti, which uses a very old USB 1.1/2.0 "Isochronous" transfer mode, gets its packets dropped. This is why it "dies" and needs a replug—the hardware buffer overflows. Stop ignoring the physical side: Move the Yeti to a different physical port—specifically one that is a different color or on a different part of the motherboard. If you can get it to show up on Bus 002 (the empty 3.0 hub you showed earlier), 90% of your problems will vanish without a single line of code. Your Final Action Plan Apply the Limine fix above (Step 1). Physically move the Yeti to a USB 3.0 port (usually blue/red). Reboot. Run lsusb and ensure the Yeti is on Bus 002. Once you reboot, run cat /sys/module/usbcore/parameters/autosuspend. Does it return -1?
