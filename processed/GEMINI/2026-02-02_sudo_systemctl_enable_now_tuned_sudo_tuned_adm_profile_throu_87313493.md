---
id: 031690
source: GEMINI
date: 2026-02-02
tags: ['tuned', 'performance-profile', 'throughput-performance', 'cachyos']
category: homelab
sentiment: building
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was enabling and configuring the tuned service with a throughput-performance profile to optimize system performance.
---
# ❯ sudo systemctl enable --now tuned
  sudo tuned-adm profile throughput-performance
Created symlink '/etc/systemd/system/multi-user.target.wants/tuned.service' → '/usr/lib/systemd/system/tuned.service'.

~
❯ 

### USER
❯ sudo systemctl enable --now tuned
  sudo tuned-adm profile throughput-performance
Created symlink '/etc/systemd/system/multi-user.target.wants/tuned.service' → '/usr/lib/systemd/system/tuned.service'.

~
❯ 

### GEMINI
You’ve successfully swapped the "laptop-brain" power manager for a professional-grade performance tuner. By enabling tuned and setting it to throughput-performance, you’ve signaled to CachyOS that you value device stability and I/O speed over saving a few milliwatts. However, we are still missing the final nail in the coffin. Without the GRUB kernel parameter, the kernel might still default to auto before tuned even initializes during the boot sequence. The Final Execution You are one reboot away from never touching that USB cable again. Edit the GRUB config: sudo nano /etc/default/grub Find the line starting with GRUB_CMDLINE_LINUX_DEFAULT and add the parameter: Make it look like this (keep whatever other flags are already there): GRUB_CMDLINE_LINUX_DEFAULT="... usbcore.autosuspend=-1" Commit the changes to the system: sudo grub-mkconfig -o /boot/grub/grub.cfg Reboot the machine. The Audit (Post-Reboot) Once you're back in, run these two commands to confirm you've won: Check the Yeti's pulse: cat /sys/bus/usb/devices/1-14/power/control (It must say on now.) Check the Bus distribution: lsusb (If you haven't physically moved it yet, it’s still on the crowded Bus 001. If you experience even one crackle in your audio, move it to a USB 3.0 port to get it onto Bus 002.) One last thing You have a FiiO DAC and a Blue Yeti. Having two high-quality audio devices on the same USB controller (Bus 001) is a recipe for IRQ (Interrupt Request) conflicts. If you see the Yeti but the audio "pops," it’s a physical traffic jam, not a software bug. Would you like me to show you how to check for USB buffer overruns in the kernel log once you’ve rebooted?
