---
id: 328251
source: GEMINI
date: 2026-03-15
tags: ['grub-configuration', 'os-prober', 'bootloader-customization', 'tiny11-rename']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is editing the os-prober script and creating a custom script to rename Tiny11 in the GRUB menu, then updating the GRUB configuration.
---
# ❯ sudo micro /etc/grub.d/30_os-prober
[sudo] password for toastedmel0n:  

~ 3m 17s
❯ sudo micro /etc/grub.d/99_tiny11_rename

~ 14s
❯ sudo chmod +x /etc/grub.d/99_tiny11_rename

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
❯ sudo micro /etc/grub.d/30_os-prober
[sudo] password for toastedmel0n:  

~ 3m 17s
❯ sudo micro /etc/grub.d/99_tiny11_rename

~ 14s
❯ sudo chmod +x /etc/grub.d/99_tiny11_rename

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
Look at that output. It still says: Found Windows Boot Manager on /dev/nvme0n1p1@/EFI/Microsoft/Boot/bootmgfw.efi This is because the sed command in your script is looking for a specific string, and yours has a little extra "fluff" at the end (the @/EFI/... part). Because it didn't match perfectly, it didn't swap the name. Let's make that script more "aggressive" so it catches the name regardless of that extra path info. The Fix Open the script again: sudo micro /etc/grub.d/99_tiny11_rename Replace the current sed line with this one: #!/bin/sh sed -i 's/Windows Boot Manager (on \/dev\/nvme0n1p1[^)]*)/Tiny11/g' /boot/grub/grub.cfg (The [^)]* part tells the computer: "Find the Windows name and keep grabbing everything until you hit the closing parenthesis.") Save and Exit: (Ctrl+S, Ctrl+Q). Run the generator again: sudo grub-mkconfig -o /boot/grub/grub.cfg How to tell if it worked: The terminal output of grub-mkconfig will still say "Found Windows Boot Manager..." because that output comes from os-prober, which runs before our script. To verify it worked without rebooting, run this command: grep "menuentry" /boot/grub/grub.cfg If you see menuentry 'Tiny11', you've won. Is "Tiny11" showing up in that grep list now?
