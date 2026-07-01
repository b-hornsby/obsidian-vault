---
id: 751186
source: GEMINI
date: 2026-03-15
tags: ['grub-mkconfig', 'dmraid-error', 'os-prober-warning', 'minegrub', 'non-critical-error']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan ran grub-mkconfig and received a non-critical dmraid mkdir error but the config was still generated successfully with Windows detected.
---
# [root@CachyOS /]# grub-mkconfig -o /boot/grub/grub.cfg
Generating grub configuration file ...
Found theme: /boot/grub/themes/minegrub-world-selection/theme.txt
Warning: os-prober will be executed to detect other bootable partitions.
Its output will be used to detect bootable binaries on them and create new boot entries.
ERROR: mkdir /var/lock/dmraid
Found Windows Boot Manager on /dev/nvme0n1p1@/EFI/Microsoft/Boot/bootmgfw.efi
Adding boot menu entry for UEFI Firmware Settings ...
done
[root@CachyOS /]# 

### USER
[root@CachyOS /]# grub-mkconfig -o /boot/grub/grub.cfg
Generating grub configuration file ...
Found theme: /boot/grub/themes/minegrub-world-selection/theme.txt
Warning: os-prober will be executed to detect other bootable partitions.
Its output will be used to detect bootable binaries on them and create new boot entries.
ERROR: mkdir /var/lock/dmraid
Found Windows Boot Manager on /dev/nvme0n1p1@/EFI/Microsoft/Boot/bootmgfw.efi
Adding boot menu entry for UEFI Firmware Settings ...
done
[root@CachyOS /]# 

### GEMINI
It only found Windows. The reason is that CachyOS has placed your kernel inside a subfolder named after your Machine ID (6cd86a12...), but GRUB’s standard scripts are looking for it directly in the top level of /boot. To fix this and get your Linux "World" to show up, we just need to move the files to where GRUB expects them. 1. Move the Kernel Files Run these two commands to move the kernel and the boot image out of that subfolder and into the main /boot directory: cp /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos/vmlinuz-linux-cachyos /boot/ cp /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos/initramfs-linux-cachyos.img /boot/ 2. Update the Minecraft Menu Now that the files are in the right spot, run the config command again: grub-mkconfig -o /boot/grub/grub.cfg The "Win" Condition Look at the output this time. You must see a line that looks like this: Found linux image: /boot/vmlinuz-linux-cachyos Found initrd image: /boot/initramfs-linux-cachyos.img Why this is the final step: GRUB is a bit "old school." It doesn't like searching through deep, randomized folder names for a kernel. By moving the files to the root of /boot, you're putting the "start button" exactly where GRUB is programmed to look. Once you see "Found linux image," you're done. Type exit, reboot, and enjoy the Minegrub menu. Does it see the Linux image now?
