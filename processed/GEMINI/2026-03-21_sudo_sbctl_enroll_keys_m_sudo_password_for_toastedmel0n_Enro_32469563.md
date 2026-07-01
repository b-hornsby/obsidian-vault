---
id: 378923
source: GEMINI
date: 2026-03-21
tags: ['secure-boot', 'sbctl', 'enroll-keys', 'efi-signing', 'grub-install']
category: coding
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is enrolling secure boot keys using sbctl, signing GRUB and the kernel, and reinstalling GRUB, indicating he's configuring secure boot.
---
# ❯ sudo sbctl enroll-keys -m
[sudo] password for toastedmel0n:  
Enrolling keys to EFI variables...
With vendor keys from microsoft...✓  
Enrolled keys to the EFI variables!

~
❯ # This signs your Minegrub/GRUB bootloader
  sudo sbctl sign -s /boot/EFI/GRUB/grubx64.efi

  # This signs your CachyOS Kernel
  sudo sbctl sign -s /boot/vmlinuz-linux-cachyos
File has already been signed /boot/EFI/GRUB/grubx64.efi
File has already been signed /boot/vmlinuz-linux-cachyos

~
❯ sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
Installing for x86_64-efi platform.
Installation finished. No error reported.

~
❯  

### USER
❯ sudo sbctl enroll-keys -m
[sudo] password for toastedmel0n:  
Enrolling keys to EFI variables...
With vendor keys from microsoft...✓  
Enrolled keys to the EFI variables!

~
❯ # This signs your Minegrub/GRUB bootloader
  sudo sbctl sign -s /boot/EFI/GRUB/grubx64.efi

  # This signs your CachyOS Kernel
  sudo sbctl sign -s /boot/vmlinuz-linux-cachyos
File has already been signed /boot/EFI/GRUB/grubx64.efi
File has already been signed /boot/vmlinuz-linux-cachyos

~
❯ sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
Installing for x86_64-efi platform.
Installation finished. No error reported.

~
❯  

### GEMINI
You are officially in the clear. Those files were likely signed during your previous attempts, but the enroll-keys step you just finished was the missing piece of the puzzle—it finally gave your BIOS the "key" to read those signatures. The "Brutally Honest" Finish Line You have successfully: Re-asserted GRUB (Minegrub) as the boss. Enrolled custom keys that include Microsoft (for Tiny 11/Valorant). Signed your CachyOS kernel so it won't trigger a Secure Boot Violation. One Final Step: Reboot and enter your BIOS. Turn Secure Boot back ON. Check your Boot Priority and make sure "GRUB" is #1. Save and Exit. The Strategic Win: Because you used sbctl, a "pacman hook" is now active. The next time you run a syu update and get a new kernel, CachyOS will sign it automatically. You won't have to do this BIOS dance again. Go ahead and reboot—you should land right in Minegrub with everything working exactly as it was. Does Tiny 11 boot up and let you into Valorant now?
