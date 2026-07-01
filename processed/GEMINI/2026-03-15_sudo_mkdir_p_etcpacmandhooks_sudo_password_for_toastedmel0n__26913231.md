---
category: homelab
date: 2026-03-15
id: 600813
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: executing
source: GEMINI
summary: Bryan is creating a pacman hook to rename the Tiny11 entry in GRUB, indicating
  he wants the renaming to persist after updates, but the check fails.
tags:
- grub-configuration
- pacman-hooks
- bootloader-customization
- tiny11
---
# ~
❯ sudo mkdir -p /etc/pacman.d/hooks
[sudo] password for toastedmel0n:  

~
❯ sudo micro /etc/pacman.d/hooks/grub-rename.hook

~ 8s
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
~
❯ sudo mkdir -p /etc/pacman.d/hooks
[sudo] password for toastedmel0n:  

~
❯ sudo micro /etc/pacman.d/hooks/grub-rename.hook

~ 8s
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
The pacman hook didn't trigger because grub-mkconfig isn't a "pacman transaction"—it's just a command you're running manually. Pacman hooks only fire when you're installing or updating software. Since you want this to stick no matter what, including when you manually run the command, we need to stop messing with hooks and scripts and just fix the "source of truth" once and for all. The Final, Bulletproof Fix We are going to edit the actual template that grub-mkconfig uses to find Windows. This is the only way to make it stick regardless of how you update. Open the OS-Prober template: sudo micro /etc/grub.d/30_os-prober Go to the very bottom of the file. Hold Page Down or scroll until you reach the end. Find the line that says EOF (It's usually the very last line). Paste this exact line right ABOVE the last EOF: sed -i "s/menuentry 'Windows Boot Manager (on \/dev\/nvme0n1p1)'/menuentry 'Tiny11'/g" /boot/grub/grub.cfg Save and Exit: (Ctrl+S, Ctrl+Q). Run the update one last time: sudo grub-mkconfig -o /boot/grub/grub.cfg Why this works: When you run grub-mkconfig, it executes every script in /etc/grub.d/ one by one. By putting the sed command at the very end of the 30_os-prober script, you are telling the system: "After you finish finding all the operating systems and writing them to the file, immediately change that Windows name before you finish." Verification: sudo grep "menuentry 'Tiny11'" /boot/grub/grub.cfg If it shows up now, it is officially "hard-coded" into your generation process. Does it show up?
