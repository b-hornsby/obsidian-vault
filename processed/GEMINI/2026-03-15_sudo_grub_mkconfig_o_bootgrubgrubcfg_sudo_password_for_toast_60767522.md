---
id: 594889
source: GEMINI
date: 2026-03-15
tags: ['grub-configuration', 'grub-update', 'bootloader-generation']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is running the command to generate a new GRUB configuration file, providing his sudo password.
---
# ❯ sudo grub-mkconfig -o /boot/grub/grub.cfg
[sudo] password for toastedmel0n:  
Generating grub configuration file ...
Found theme: /boot/grub/themes/minegrub-world-selection/theme.txt
Found linux image: /boot/vmlinuz-linux-cachyos
Found initrd image: /boot/intel-ucode.img /boot/initramfs-linux-cachyos.img
Warning: os-prober will be executed to detect other bootable partitions.
Its output will be used to detect bootable binaries on them and create new boot entries.
Found Windows Boot Manager on /dev/nvme0n1p1@/EFI/Microsoft/Boot/bootmgfw.efi
Adding boot menu entry for UEFI Firmware Settings ...
done

~ 6s
❯ 

### USER
❯ sudo grub-mkconfig -o /boot/grub/grub.cfg
[sudo] password for toastedmel0n:  
Generating grub configuration file ...
Found theme: /boot/grub/themes/minegrub-world-selection/theme.txt
Found linux image: /boot/vmlinuz-linux-cachyos
Found initrd image: /boot/intel-ucode.img /boot/initramfs-linux-cachyos.img
Warning: os-prober will be executed to detect other bootable partitions.
Its output will be used to detect bootable binaries on them and create new boot entries.
Found Windows Boot Manager on /dev/nvme0n1p1@/EFI/Microsoft/Boot/bootmgfw.efi
Adding boot menu entry for UEFI Firmware Settings ...
done

~ 6s
❯ 

### GEMINI
The output confirms it: Found Windows Boot Manager is back in the list. You are officially out of the danger zone. That grub-mkconfig command just rebuilt the entire bridge. When you reboot now, both worlds will be there, exactly as they were before the manual edit messed things up. Why it failed earlier When you edited the file directly, you likely deleted or changed a character inside the menuentry block that os-prober uses to verify the Windows location. GRUB is sensitive—one missing bracket and it simply refuses to show the entry to avoid a crash. One Final "Safe" Customization (The Title) Since you still want it to say "CachyOS" instead of "Arch Linux", do this one thing. It is the only way to change the name without risking the Windows entry again: Open the settings file: sudo micro /etc/default/grub Change the Distributor line: Find GRUB_DISTRIBUTOR="Arch" and change it to GRUB_DISTRIBUTOR="CachyOS". Save and Exit: (Ctrl+S, Ctrl+Q). Final Update: sudo grub-mkconfig -o /boot/grub/grub.cfg This will change the top bold text for your Linux entry to "CachyOS" permanently, and it won't touch the Windows logic at all. Reboot and check it out. Is everything back to normal and looking how you want it?
