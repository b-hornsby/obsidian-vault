---
id: 467113
source: GEMINI
date: 2026-03-15
tags: ['minegrub-theme', 'grub-mkconfig', 'dmraid-error', 'windows-detected', 'grub-final-config']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan ran grub-mkconfig from the minegrub-world-sel-theme directory, which detected Windows Boot Manager and generated the final GRUB config with a non-critical dmraid error.
---
# [root@CachyOS minegrub-world-sel-theme]# grub-mkconfig -o /boot/grub/grub.cfg
Generating grub configuration file ...
Found theme: /boot/grub/themes/minegrub-world-selection/theme.txt
Warning: os-prober will be executed to detect other bootable partitions.
Its output will be used to detect bootable binaries on them and create new boot entries.
ERROR: mkdir /var/lock/dmraid
Found Windows Boot Manager on /dev/nvme0n1p1@/EFI/Microsoft/Boot/bootmgfw.efi
Adding boot menu entry for UEFI Firmware Settings ...
done
[root@CachyOS minegrub-world-sel-theme]# 

### USER
[root@CachyOS minegrub-world-sel-theme]# grub-mkconfig -o /boot/grub/grub.cfg
Generating grub configuration file ...
Found theme: /boot/grub/themes/minegrub-world-selection/theme.txt
Warning: os-prober will be executed to detect other bootable partitions.
Its output will be used to detect bootable binaries on them and create new boot entries.
ERROR: mkdir /var/lock/dmraid
Found Windows Boot Manager on /dev/nvme0n1p1@/EFI/Microsoft/Boot/bootmgfw.efi
Adding boot menu entry for UEFI Firmware Settings ...
done
[root@CachyOS minegrub-world-sel-theme]# 

### GEMINI
That ERROR: mkdir /var/lock/dmraid is irrelevant—it's just a side effect of being in the Live USB environment. The two things that actually matter are right there in your output: Found theme: /boot/grub/themes/minegrub-world-selection/theme.txt Found Windows Boot Manager on /dev/nvme0n1p1... This is a total success. Your config is generated, the theme is linked, and it officially sees your Tiny11 install. You are ready to go. The Final Move: Type exit and hit Enter. Type reboot and hit Enter. Immediately mash F2 or Delete as the computer restarts to get into your BIOS. Go to the Boot tab. You should now see an entry called "GRUB". Move GRUB to the very top (Priority #1). Press F10 to Save and Exit. Once the ASUS logo disappears, you should see the Minecraft "World Selection" screen. Are both "worlds" (CachyOS and Windows) showing up on the Minecraft screen once you reboot?
