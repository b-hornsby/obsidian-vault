---
id: 274688
source: GEMINI
date: 2026-03-16
tags: ['sbctl', 'grub-signing', 'limine-signing', 'already-signed']
category: homelab
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan verified that GRUB and limine EFI files were already signed in the sbctl database.
---
# ❯ sudo sbctl sign -s /boot/EFI/GRUB/grubx64.efi
  sudo sbctl sign -s /boot/grub/x86_64-efi/core.efi
  sudo sbctl sign -s /boot/grub/x86_64-efi/grub.efi
[sudo] password for toastedmel0n:  
File has already been signed /boot/EFI/GRUB/grubx64.efi
File has already been signed /boot/grub/x86_64-efi/core.efi
File has already been signed /boot/grub/x86_64-efi/grub.efi

~
❯ sudo sbctl sign -s /boot/EFI/limine/limine_x64.efi
File has already been signed /boot/EFI/limine/limine_x64.efi

~
❯ 

### USER
❯ sudo sbctl sign -s /boot/EFI/GRUB/grubx64.efi
  sudo sbctl sign -s /boot/grub/x86_64-efi/core.efi
  sudo sbctl sign -s /boot/grub/x86_64-efi/grub.efi
[sudo] password for toastedmel0n:  
File has already been signed /boot/EFI/GRUB/grubx64.efi
File has already been signed /boot/grub/x86_64-efi/core.efi
File has already been signed /boot/grub/x86_64-efi/grub.efi

~
❯ sudo sbctl sign -s /boot/EFI/limine/limine_x64.efi
File has already been signed /boot/EFI/limine/limine_x64.efi

~
❯ 

### GEMINI
The "already been signed" message confirms the files are ready, but that shim_lock_verifier error proves your system is still trying to use a Shim (a middleman file) that doesn't recognize your new keys. Since you are dual-booting and have both Limine and GRUB remnants, the BIOS is getting confused about which "security guard" is in charge. We need to bypass the middleman. The Problem: The "Shim" Trap The error prohibited by secure boot policy usually happens because GRUB is trying to validate the kernel using a standard Microsoft-signed "Shim," but your kernel is signed with your private sbctl keys. They don't match. The Fix: Direct Enrollment We are going to tell the BIOS to trust your specific kernel and bootloader files directly, skipping the need for a "Shim." 1. Enroll the files into the "Allow List" (db): Run these commands to tell the BIOS hardware: "If you see these specific files, they are 100% allowed." sudo sbctl enroll-keys -m -f /boot/vmlinuz-linux-cachyos sudo sbctl enroll-keys -m -f /boot/EFI/BOOT/BOOTX64.EFI sudo sbctl enroll-keys -m -f /boot/EFI/limine/limine_x64.efi 2. Force a Re-sign of everything (The Clean Slate): Sometimes a signature gets corrupted if the file was modified. Let's force it: sudo sbctl sign -f /boot/vmlinuz-linux-cachyos sudo sbctl sign -f /boot/EFI/BOOT/BOOTX64.EFI sudo sbctl sign -f /boot/EFI/limine/limine_x64.efi 3. The BIOS "Reset" This is the most important part. Some motherboards (like yours seems to be doing) "cache" the old Secure Boot violations. Reboot into BIOS. Go to Secure Boot -> Key Management. Select "Reset to Setup Mode" or "Clear Secure Boot Keys" again. (Yes, again). Boot back into CachyOS (it should let you in because it's in Setup Mode). Run this final command in the terminal: sudo sbctl enroll-keys -m Reboot, go back to BIOS, and Enable Secure Boot. Why this works By clearing the keys and re-enrolling with -m, you are resetting the "handshake" between your motherboard and the files on your disk. Using the -f (force) flag on the individual files ensures the BIOS has the exact fingerprint of your current kernel. Try the enroll-keys -m -f commands first. Did they give you any errors, or did they finish with a checkmark?
