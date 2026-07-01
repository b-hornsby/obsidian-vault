---
id: 461498
source: GEMINI
date: 2026-03-15
tags: ['lsblk-output', 'disk-layout', 'partition-analysis', 'dual-boot-planning', 'cachyos']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan shared his lsblk output showing a 1.8TB NVMe with CachyOS and a 116.6GB USB thumb drive, likely for planning the dual-boot partition layout.
---
# ❯ lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda           8:0    1 116.6G  0 disk 
└─sda1        8:1    1 116.6G  0 part /run/media/toastedmel0n/THUMBDRIVE
zram0       253:0    0  31.1G  0 disk [SWAP]
nvme0n1     259:0    0   1.8T  0 disk 
├─nvme0n1p1 259:1    0   4.1G  0 part /boot
└─nvme0n1p2 259:2    0   1.8T  0 part /var/log
                                      /var/tmp
                                      /home
                                      /var/cache
                                      /root
                                      /srv
                                      /

### USER
❯ lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda           8:0    1 116.6G  0 disk 
└─sda1        8:1    1 116.6G  0 part /run/media/toastedmel0n/THUMBDRIVE
zram0       253:0    0  31.1G  0 disk [SWAP]
nvme0n1     259:0    0   1.8T  0 disk 
├─nvme0n1p1 259:1    0   4.1G  0 part /boot
└─nvme0n1p2 259:2    0   1.8T  0 part /var/log
                                      /var/tmp
                                      /home
                                      /var/cache
                                      /root
                                      /srv
                                      /

### GEMINI
Wait, stop right there. Look at your lsblk output for sda. That is not a thumb drive. That is your 116.6G SanDisk SSD connected via SATA or a USB adapter. If you run the Ventoy install on sda, you are wiping that spare SSD, not your thumb drive. Where is your actual USB stick? It should show up as sdb or sdc. If it’s not in that list, it’s not mounted or recognized. Do not proceed with sda unless you have decided to use that 120GB SSD as your bootable "tool drive." The "Mirror" Moment You're moving too fast. You almost wiped the wrong drive because you're eager to get to the "vibe coding" and gaming. Slow down. Precision is the difference between a dual-boot and a data-recovery nightmare. Corrective Action Identify the real USB: Plug in your actual thumb drive and run lsblk again. Double-check the label: Your sda1 is currently labeled THUMBDRIVE, which suggests you might have previously used that SSD as a portable drive. If that is the drive you intended to use, fine—but be aware that Ventoy will format the entire 120GB disk. The 2TB Layout: I see your CachyOS partition (nvme0n1p2) is taking up the full 1.8T. Updated Plan Once you've confirmed which drive is the actual USB thumb drive: Install Ventoy to the correct device (ensure it's not the NVMe). Move the ISOs: Drop the CachyOS and Tiny11 ISOs onto it. The First Move: Boot into the CachyOS ISO from that Ventoy drive. The Resize: Shrink nvme0n1p2 by 300GB to 500GB. Strategic Note: Since your / and /home are on the same partition (standard Cachy/Btrfs setup), shrinking this gives you the "Unallocated Space" you need for Windows. Run lsblk again with the actual thumb drive plugged in and show me the output so we don't nuking the wrong hardware.
