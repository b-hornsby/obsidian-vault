---
id: 038352
source: GEMINI
date: 2026-02-04
tags: ['thumb-drive', 'wipe', 'cachyos', 'usb', 'storage']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan clarified that CachyOS is on his 2TB drive and he just wanted to wipe a thumb drive for normal use.
---
# im not reading cachyos from there i have it on my actual 2tb drive i just want to wipe this thumb drive so i can use it as normal 

### USER
im not reading cachyos from there i have it on my actual 2tb drive i just want to wipe this thumb drive so i can use it as normal 

### GEMINI
I know you aren't running the OS from the thumb drive. If you were, we'd be having a much shorter conversation because your system would have crashed the moment you wiped the partition table. The reason I pointed out your lsblk is that sda1 (the thumb drive) was mounted. Linux won't let you cleanly reformat a drive while the system is still holding onto a mount point. It’s like trying to replace a tire while the car is spinning on a jack. If you haven't run the commands from my previous message yet, here is the "no-nonsense" sequence to execute right now. The "Clean Slate" Protocol Force everything off: sudo umount /dev/sda* Destroy the ISO structure: This wipes the "ISO 9660" signature that makes your computer think it's still a CachyOS installer. sudo wipefs -a /dev/sda Create the new space: We’ll use a standard MBR (msdos) table for maximum compatibility with any device. sudo parted /dev/sda mklabel msdos sudo parted -a optimal /dev/sda mkpart primary fat32 0% 100% Finalize the format: sudo mkfs.vfat -F 32 /dev/sda1 -n "THUMBDRIVE" Why this matters You said you want to use it "as normal." The Problem: Flashing an ISO uses a "Read-Only" filesystem (ISO9660) that doesn't behave like a standard drive. The Trap: If you just try to "delete files" via your file manager, it will tell you you don't have permission. The Fix: The commands above treat the drive as raw plastic and silicon, ignoring whatever CachyOS data was left there and forcing it back into a state where it's a blank slate. Stop looking at the drive as a folder; start looking at it as a block device. Run those four commands and you'll have your 128GB back. Would you like me to show you how to create a "Ventoy" drive on that stick instead, so you can use it for storage AND keep multiple ISOs on it without ever having to "flash" it again?
