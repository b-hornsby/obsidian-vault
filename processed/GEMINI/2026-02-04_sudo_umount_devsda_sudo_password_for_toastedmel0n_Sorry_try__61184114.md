---
id: 412504
source: GEMINI
date: 2026-02-04
tags: ['thumb-drive', 'wipe', 'wipefs', 'parted', 'cachyos', 'vfat']
category: homelab
sentiment: executing
resolution: resolved
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan successfully wiped and reformatted a CachyOS-flashed thumb drive back to a normal FAT32 USB drive.
---
# 
❯ sudo umount /dev/sda*
[sudo] password for toastedmel0n:  
Sorry, try again.
[sudo] password for toastedmel0n:  
umount: /dev/sda: not mounted.
umount: /dev/sda2: not mounted.

~ 10s
❯ sudo wipefs -a /dev/sda
/dev/sda: 5 bytes were erased at offset 0x00008001 (iso9660): 43 44 30 30 31
/dev/sda: 2 bytes were erased at offset 0x000001fe (dos): 55 aa
/dev/sda: 8 bytes were erased at offset 0x00000200 (gpt): 45 46 49 20 50 41 52 54
/dev/sda: calling ioctl to re-read partition table: Success

~
❯ sudo parted /dev/sda mklabel msdos
Information: You may need to update /etc/fstab.


~
❯ sudo parted -a optimal /dev/sda mkpart primary fat32 0% 100%
Information: You may need to update /etc/fstab.


~
❯ sudo mkfs.vfat -F 32 /dev/sda1 -n "THUMBDRIVE"
mkfs.fat 4.2 (2021-01-31)

~
❯ 

### USER

❯ sudo umount /dev/sda*
[sudo] password for toastedmel0n:  
Sorry, try again.
[sudo] password for toastedmel0n:  
umount: /dev/sda: not mounted.
umount: /dev/sda2: not mounted.

~ 10s
❯ sudo wipefs -a /dev/sda
/dev/sda: 5 bytes were erased at offset 0x00008001 (iso9660): 43 44 30 30 31
/dev/sda: 2 bytes were erased at offset 0x000001fe (dos): 55 aa
/dev/sda: 8 bytes were erased at offset 0x00000200 (gpt): 45 46 49 20 50 41 52 54
/dev/sda: calling ioctl to re-read partition table: Success

~
❯ sudo parted /dev/sda mklabel msdos
Information: You may need to update /etc/fstab.


~
❯ sudo parted -a optimal /dev/sda mkpart primary fat32 0% 100%
Information: You may need to update /etc/fstab.


~
❯ sudo mkfs.vfat -F 32 /dev/sda1 -n "THUMBDRIVE"
mkfs.fat 4.2 (2021-01-31)

~
❯ 

### GEMINI
Done. You’ve successfully stripped the ISO signatures and reclaimed the hardware. The mkfs.fat output confirms the filesystem was created. The Verification Run lsblk one last time. You should see: sda: 116.6G (the raw disk) └─sda1: ~116G (your new partition) It will no longer have that 2.9GB/24MB split. You now have a single, clean "THUMBDRIVE" partition. A Quick Warning (The FAT32 Limitation) You used fat32 in the commands. It’s the most compatible format on the planet, but it has a 4GB individual file size limit. If you try to move a 5GB movie or a large game ISO onto that 128GB drive, it will fail and give you a cryptic "Disk Full" or "Error" message even though you have 110GB+ free. If you plan on storing large files, you should re-run that last command using ExFAT instead: sudo mkfs.exfat /dev/sda1 -n "THUMBDRIVE" Would you like me to show you how to set up a udev rule so that this specific drive always mounts with specific permissions the moment you plug it in?
