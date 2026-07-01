---
category: homelab
date: 2026-03-15
id: 327574
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: executing
source: GEMINI
summary: Bryan is running the command to generate a new GRUB configuration file, but
  then checks for the Tiny11 entry and it's missing, indicating a problem.
tags:
- grub-configuration
- grub-update
- bootloader-generation
---
# ❯ sudo grub-mkconfig -o /boot/grub/grub.cfg
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
❯ sudo grep "menuentry 'Tiny11'" /boot/grub/grub.cfg

~
❯ 

### USER
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
❯ sudo grep "menuentry 'Tiny11'" /boot/grub/grub.cfg

~
❯ 

### GEMINI
Still nothing. This is happening because the sed command in your script is trying to find and replace text inside /boot/grub/grub.cfg while that file is still being written or held by the grub-mkconfig process. Basically, your "ninja" is swinging its sword before the target is even standing there. Let's stop trying to be fancy with the /etc/grub.d/ scripts for a second and just run the "Brute Force" command manually to see it work. 1. Run the "Brute Force" Command Manually Copy and paste this exact line into your terminal: sudo sed -i "s/menuentry 'Windows Boot Manager (on \/dev\/nvme0n1p1)'/menuentry 'Tiny11'/g" /boot/grub/grub.cfg 2. Verify it immediately Now run your grep again: sudo grep "menuentry 'Tiny11'" /boot/grub/grub.cfg If it works now: It means the command is correct, but the timing of the script in /etc/grub.d/99_tiny11_rename is the problem. GRUB scripts are executed to generate text, but sed -i tries to edit a file that isn't finished yet. To make it truly permanent and "automated": If that manual command worked, the real way to automate this is to add that sed line to your .bashrc or create an alias, but honestly, the most "honest" way is to just edit the Distributor name for Linux (which you did) and realize that Windows' name is just a stubborn piece of metadata. Did the manual sed command finally make Tiny11 show up in the grep?
