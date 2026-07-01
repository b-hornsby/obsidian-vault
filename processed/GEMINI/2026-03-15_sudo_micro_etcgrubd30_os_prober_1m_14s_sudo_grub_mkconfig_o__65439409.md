---
category: homelab
date: 2026-03-15
id: 749315
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: executing
source: GEMINI
summary: Bryan is editing the os-prober script, then generating a new GRUB configuration,
  and checking for the Tiny11 entry, suggesting he's trying to get Tiny11 recognized.
tags:
- grub-configuration
- os-prober
- bootloader-generation
- tiny11
---
# ❯ sudo micro /etc/grub.d/30_os-prober

~ 1m 14s
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

### USER
❯ sudo micro /etc/grub.d/30_os-prober

~ 1m 14s
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
Look, we've been trying to perform surgery on a file while the system is still holding it. It’s like trying to paint a car while it’s driving down the highway—it’s just not sticking because the system finishes writing the file after our script runs. If you want this to stick permanently without ever touching it again, we have to move the fix to the only place that runs after everything else is done: the 40_custom script. The Final, Bulletproof Setup Undo the change to 30_os-prober first: Open sudo micro /etc/grub.d/30_os-prober, delete that sed line you added at the bottom, save, and exit. Put the "Auto-Correct" in the right place: sudo micro /etc/grub.d/40_custom Paste this at the very bottom of that file: sed -i "s/menuentry 'Windows Boot Manager (on \/dev\/nvme0n1p1)'/menuentry 'Tiny11'/g" /boot/grub/grub.cfg Save and Exit (Ctrl+S, Ctrl+Q). Run the update: sudo grub-mkconfig -o /boot/grub/grub.cfg Why this works: In GRUB, the scripts in /etc/grub.d/ run in numerical order. 30_os-prober finds Windows, and 40_custom runs after it. By putting the sed command in 40_custom, it waits until the Windows entry is already created and then swaps the name. If that STILL doesn't show in grep: It means grub-mkconfig is buffering the output and only writing the file at the very, very end. If that's the case, the only way to make it stick forever is to create an alias. Add this to your shell config: echo "alias update-grub='sudo grub-mkconfig -o /boot/grub/grub.cfg && sudo sed -i \"s/menuentry '\''Windows Boot Manager (on \/dev\/nvme0n1p1)'\''/menuentry '\''Tiny11'\''/g\" /boot/grub/grub.cfg'" >> ~/.bashrc source ~/.bashrc Now, whenever you want to update your boot menu, you just type update-grub. It will generate the menu and immediately rename Windows for you in one move. Does the grep show "Tiny11" now after the 40_custom fix?
