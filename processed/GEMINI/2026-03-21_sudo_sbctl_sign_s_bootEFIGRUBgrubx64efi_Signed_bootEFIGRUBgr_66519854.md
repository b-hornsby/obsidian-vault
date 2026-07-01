---
id: 858431
source: GEMINI
date: 2026-03-21
tags: ['secure-boot', 'sbctl', 'efi-signing', 'grub-configuration', 'kernel-signing']
category: coding
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is signing GRUB and the kernel using sbctl, but encounters an error when trying to sign the initramfs image, indicating a problem with secure boot configuration.
---
# ❯ sudo sbctl sign -s /boot/EFI/GRUB/grubx64.efi
✓ Signed /boot/EFI/GRUB/grubx64.efi

~
❯ sudo sbctl sign -s /boot/vmlinuz-linux-cachyos
File has already been signed /boot/vmlinuz-linux-cachyos

~
❯ sudo sbctl sign -s /boot/initramfs-linux-cachyos.img
failed reading PE file: unrecognized PE machine: 0x3730

~
❯  

### USER
❯ sudo sbctl sign -s /boot/EFI/GRUB/grubx64.efi
✓ Signed /boot/EFI/GRUB/grubx64.efi

~
❯ sudo sbctl sign -s /boot/vmlinuz-linux-cachyos
File has already been signed /boot/vmlinuz-linux-cachyos

~
❯ sudo sbctl sign -s /boot/initramfs-linux-cachyos.img
failed reading PE file: unrecognized PE machine: 0x3730

~
❯  

### GEMINI
The initramfs error is expected—ignore it. That file isn't a "PE file" (an executable), so it doesn't get signed like the others. Your kernel says it's already signed, and you just successfully signed the GRUB bootloader (grubx64.efi). The Finish Line You have officially "resealed" the security on your bootloader. Reboot and enter your BIOS. Re-enable Secure Boot. Check your Boot Priority one last time—make sure the entry named "GRUB" is at the very top. Save and Exit. The "Brutally Honest" Reality Check If you see the Minegrub menu and can boot into CachyOS, you've won. If Valorant gives you a hard time on the Tiny 11 side, it's because Vanguard is sensing the "Custom" keys you have in your BIOS. If that happens, you'll need to "Restore Factory Keys" in your BIOS Secure Boot menu, but let's see if it just works first. Does Minegrub load up without the red violation box now that you've re-enabled Secure Boot?
