---
id: 954303
source: GEMINI
date: 2026-02-02
tags: ['systemd-boot', 'boot-entries', 'cachyos']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was looking for systemd boot loader entries but discovered the directory does not exist on his CachyOS system.
---
# ❯ sudo ls /boot/loader/entries/
ls: cannot access '/boot/loader/entries/': No such file or directory

~
❯ 

### USER
❯ sudo ls /boot/loader/entries/
ls: cannot access '/boot/loader/entries/': No such file or directory

~
❯ 

### GEMINI
If it's not GRUB and it's not systemd-boot, you are likely using Limine or your /boot partition isn't mounted where you think it is. CachyOS has been moving toward Limine as a default recently because it's faster. But frankly, we are over-complicating this by trying to find the "correct" bootloader file. Let's use the tool CachyOS provides to manage the kernel without hunting for files. 1. The "Cachy" Way CachyOS includes a kernel manager. Check if you can use it to see your command line: cat /proc/cmdline Look at that output. Does it mention usbcore.autosuspend=-1? If not, the kernel is still the boss of your USB power. 2. Force it via sysctl (The Software Workaround) Since we know tuned is running, let's force the kernel's hand through a configuration file that doesn't care which bootloader you use. Create a custom sysctl rule: echo "options usbcore autosuspend=-1" | sudo tee /etc/modprobe.d/disable-usb-autosuspend.conf Note: This tells the USB core module to set the autosuspend delay to -1 (disabled) the moment it loads. 3. Verify the Yeti's Port You've been checking /sys/bus/usb/devices/1-14/, but in your last lsusb, the Yeti moved to Device 028. The address probably changed. Let's find exactly where the Yeti is sitting right now so we stop checking the wrong "folder." Run this: lsusb -t Look for the line that says Driver=snd-usb-audio. It will have a path like 1-1.2 or 1-4. What is that number? The Strategy We are going to stop guessing where your bootloader is. The Modprobe fix above (Step 2) works at the driver level. The Tuned profile you set earlier should be handling this, but if the Yeti is on a sub-hub (like that Alcor hub), the power command might not be trickling down. Run lsusb -t and give me that port number. I need to see the "tree" to see if a hub is blocking our commands.
