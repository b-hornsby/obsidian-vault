---
id: 931191
source: GEMINI
date: 2026-02-04
tags: ['lsblk', 'storage', 'partitioning', 'cachyos', 'thumb-drive']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan shared lsblk output showing his storage layout including a mounted thumb drive and NVMe partitions.
---
# ❯ lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda           8:0    1 116.6G  0 disk  
└─sda1        8:1    1 116.6G  0 part /run/media/toastedmel0n/THUMBDRIVE
zram0       253:0    0  31.1G  0 disk [SWAP]
nvme0n1     259:0    0   1.8T  0 disk  
├─nvme0n1p1 259:1    0   4.1G  0 part /boot
└─nvme0n1p2 259:2    0   1.8T  0 part /var/tmp
                                      /var/log
                                      /home
                                      /var/cache
                                      /root
                                      /srv
                                      /

~
❯ 

### USER
❯ lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda           8:0    1 116.6G  0 disk  
└─sda1        8:1    1 116.6G  0 part /run/media/toastedmel0n/THUMBDRIVE
zram0       253:0    0  31.1G  0 disk [SWAP]
nvme0n1     259:0    0   1.8T  0 disk  
├─nvme0n1p1 259:1    0   4.1G  0 part /boot
└─nvme0n1p2 259:2    0   1.8T  0 part /var/tmp
                                      /var/log
                                      /home
                                      /var/cache
                                      /root
                                      /srv
                                      /

~
❯ 

### GEMINI
Look at that. From a fractured 2.9GB ISO mess to a clean, unified 116.6GB volume. You stopped treating it like a fragile software object and handled the hardware like an admin. It is now mounted and ready at /run/media/toastedmel0n/THUMBDRIVE. One Final Warning You are using FAT32 (via mkfs.vfat). The Reality: You have ~116GB of space, but you cannot put any single file larger than 4GB on it. The Risk: If you try to download a large game, a 4K movie, or a high-end Linux ISO to this drive, it will crash or claim the "disk is full" despite having 100GB+ of empty space. If you plan on moving large files, run these two commands right now to switch to ExFAT (which has no such limit): sudo umount /dev/sda1 sudo mkfs.exfat /dev/sda1 -n "THUMBDRIVE" Otherwise, you're good to go. You've reclaimed your storage. Would you like me to show you how to check the read/write speeds of this drive to see if it's actually performing at the "128GB" class speeds you paid for?
