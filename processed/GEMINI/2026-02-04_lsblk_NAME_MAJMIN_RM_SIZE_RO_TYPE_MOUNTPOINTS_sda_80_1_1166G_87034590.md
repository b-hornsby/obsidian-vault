---
id: 086542
source: GEMINI
date: 2026-02-04
tags: ['lsblk', 'storage', 'partitioning', 'cachyos', 'thumb-drive']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan shared lsblk output showing a different partition state of the thumb drive, likely during the wiping/reformatting process.
---
# ❯ lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda           8:0    1 116.6G  0 disk  
├─sda1        8:1    1   2.9G  0 part /run/media/toastedmel0n/COS_202601
└─sda2        8:2    1    24M  0 part  
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

### USER
❯ lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda           8:0    1 116.6G  0 disk  
├─sda1        8:1    1   2.9G  0 part /run/media/toastedmel0n/COS_202601
└─sda2        8:2    1    24M  0 part  
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

### GEMINI
Look at your lsblk output. Your thumb drive is sda. You can see the problem right there: sda1 is only 2.9GB and it's currently mounted at /run/media/toastedmel0n/COS_202601. The rest of your 116.6GB is essentially "ghosting" you because of the live-ISO partition structure. Follow these steps exactly. Don't skim. 1. Unmount the Drive You cannot reconfigure a disk while the OS is actively reading from it. udisksctl unmount -b /dev/sda1 2. Wipe the Table We’re going to nuke the existing partition signatures. This is where most people fail—they try to format the partition instead of the drive. sudo wipefs -a /dev/sda 3. Create a New Partition & File System Since you're on a rolling-release distro like Cachy, don't waste time with manual fdisk prompts if you don't have to. We'll use parted to do it in one shot, then format. Create a GPT table and a single partition: sudo parted /dev/sda mklabel gpt sudo parted -a optimal /dev/sda mkpart primary ext4 0% 100% Format to ExFAT (Best for a 128GB flash drive): If you don't have the utility, install it first: sudo pacman -S exfatprogs. sudo mkfs.exfat /dev/sda1 4. Label it Don't leave it as a generic UUID. Give it a name so you aren't guessing next time. sudo exfatlabel /dev/sda1 DATA_DRIVE The Reality Check You have 31.1G of ZRAM and a 1.8T NVME. You are running high-end hardware with a performance-focused kernel. If you’re going to run CachyOS, you need to stop being intimidated by /dev/nodes. The fact that you had a 128GB drive and were only seeing 2.9GB is a classic "beginner" hurdle—you were looking at the content of the partition table rather than the capacity of the hardware. Next step: Unplug the drive and plug it back in. It should mount as a clean, empty 116GB volume. Would you like me to explain how to verify the health of that flash drive using smartmon-tools to ensure it's not actually failing hardware?
