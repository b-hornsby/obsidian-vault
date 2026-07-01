---
id: 464542
source: GEMINI
date: 2026-03-15
tags: ['boot-partition', 'nvme', 'cachyos', 'filesystem']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan mounted the boot partition to inspect its contents after encountering boot configuration issues.
---
# [root@CachyOS /]# mount /dev/nvme0n1p1 /boot
[root@CachyOS /]# ls /boot
6cd86a12288e4089802591bd1a9a39ce  grub             limine-splash.png  limine.conf.old
EFI                               intel-ucode.img  limine.conf        loader
[root@CachyOS /]# 

### USER
[root@CachyOS /]# mount /dev/nvme0n1p1 /boot
[root@CachyOS /]# ls /boot
6cd86a12288e4089802591bd1a9a39ce  grub             limine-splash.png  limine.conf.old
EFI                               intel-ucode.img  limine.conf        loader
[root@CachyOS /]# 

### GEMINI
Alright, the mount didn't reveal the files. This confirms it: when you installed Tiny11, it likely cleared out the "keys" to your Linux house from the EFI partition. But stay calm: your data (projects, settings, etc.) is still 100% safe. It lives on a different part of the drive. We just need to reinstall the Linux "engine" (the kernel) so the system knows how to start up again. Run these exact commands in your terminal right now: 1. Reinstall the Kernel This will download the missing files and put them back into /boot. pacman -Sy linux-cachyos linux-cachyos-headers Wait for this to finish. It shouldn't take long. 2. Update the Minecraft Menu (GRUB) Now that the files actually exist in /boot, we need to tell the Minegrub menu to go find them so CachyOS shows up as a "World" you can enter. grub-mkconfig -o /boot/grub/grub.cfg 3. Verification (Crucial) Run ls /boot one more time. You must see a file named vmlinuz-linux-cachyos now. If you see that file, look at the output of the grub-mkconfig command you just ran. It should say: Found linux image: /boot/vmlinuz-linux-cachyos The Strategy Why did this happen? Windows is notorious for "cleaning up" boot partitions during installation. It saw your Linux files and basically deleted them to make room for its own. Is my data safe? Yes. We are only touching the /boot folder. Your /home folder (where your actual life is) is untouched. Once you run those and see the "Found linux image" message, type exit, reboot, and your CachyOS "World" will finally be back in the Minecraft menu. Does the pacman command finish successfully?
