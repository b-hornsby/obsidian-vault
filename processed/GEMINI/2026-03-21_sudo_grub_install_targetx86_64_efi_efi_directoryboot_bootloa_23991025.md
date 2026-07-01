---
id: 271404
source: GEMINI
date: 2026-03-21
tags: ['grub-install', 'efi-bootloader', 'boot-configuration', 'os-prober']
category: coding
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is installing GRUB as the EFI bootloader and generating the GRUB configuration file, indicating he's configuring his boot process.
---
# ❯ sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
Installing for x86_64-efi platform.
Installation finished. No error reported.

~
❯ sudo grub-mkconfig -o /boot/grub/grub.cfg
Generating grub configuration file ...
Found theme: /boot/grub/themes/minegrub-world-selection/theme.txt
Found linux image: /boot/vmlinuz-linux-cachyos
Found initrd image: /boot/intel-ucode.img /boot/initramfs-linux-cachyos.img
Warning: os-prober will be executed to detect other bootable partitions.
Its output will be used to detect bootable binaries on them and create new boot entries.
Found Windows Boot Manager on /dev/nvme0n1p1@/EFI/Microsoft/Boot/bootmgfw.efi
Adding boot menu entry for UEFI Firmware Settings ...
done

~
❯  

### USER
❯ sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
Installing for x86_64-efi platform.
Installation finished. No error reported.

~
❯ sudo grub-mkconfig -o /boot/grub/grub.cfg
Generating grub configuration file ...
Found theme: /boot/grub/themes/minegrub-world-selection/theme.txt
Found linux image: /boot/vmlinuz-linux-cachyos
Found initrd image: /boot/intel-ucode.img /boot/initramfs-linux-cachyos.img
Warning: os-prober will be executed to detect other bootable partitions.
Its output will be used to detect bootable binaries on them and create new boot entries.
Found Windows Boot Manager on /dev/nvme0n1p1@/EFI/Microsoft/Boot/bootmgfw.efi
Adding boot menu entry for UEFI Firmware Settings ...
done

~
❯  

### GEMINI
You nailed it. The output is exactly what you were looking for: Found theme: .../minegrub-world-selection/theme.txt — Your aesthetics are back. Found Windows Boot Manager — Tiny 11 is back on the menu. Installation finished. No error reported. — GRUB is officially back in the driver's seat. The "Brutally Honest" Reality Check You are about 90% of the way home, but there is one final hurdle. Because CachyOS pushed that Limine update, your motherboard’s UEFI (the BIOS) likely still has "CachyOS" (Limine) as the #1 priority. If you reboot right now and see that purple/blue screen again, don't panic. It just means the BIOS hasn't switched back to the "GRUB" entry you just re-installed. The Finish Line: Reboot your PC. If you see the Minegrub menu, you're done. Great success. If you see the Limine panic or the blue Limine menu again: Restart and spam F2 or Del (since you're on a 12700K system, it's likely one of those). Find the Boot section. Look for Boot Option #1 or Boot Priority. Select the entry explicitly named "GRUB" and move it to the top. Save and Exit. Once you reboot, does your Minegrub menu load up correctly with the Tiny 11 option visible?
