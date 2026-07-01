---
id: 032235
source: GEMINI
date: 2026-03-21
tags: ['secure-boot', 'sbctl', 'status-check', 'uefi-configuration']
category: coding
sentiment: exploratory
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is checking the status of sbctl to verify secure boot configuration, indicating he's troubleshooting secure boot issues.
---
# ❯ sudo sbctl status
[sudo] password for toastedmel0n:  
Installed:      ✓ sbctl is installed
Owner GUID:     ec897f63-4161-4381-abaf-68b5d043d37e
Setup Mode:     ✓ Disabled
Secure Boot:    ✗ Disabled
Vendor Keys:    microsoft builtin-db builtin-db builtin-db builtin-KEK

~
❯  

### USER
❯ sudo sbctl status
[sudo] password for toastedmel0n:  
Installed:      ✓ sbctl is installed
Owner GUID:     ec897f63-4161-4381-abaf-68b5d043d37e
Setup Mode:     ✓ Disabled
Secure Boot:    ✗ Disabled
Vendor Keys:    microsoft builtin-db builtin-db builtin-db builtin-KEK

~
❯  

### GEMINI
Your sbctl status shows that Setup Mode is Disabled, which means your BIOS is already locked down with a set of keys. If those aren't your keys from a previous setup, sbctl won't let you enroll new ones without a fight. Since you want to get back to "exactly as they were" with the least amount of friction, we are going to sign the new files using the keys already on your system. The "Brutally Honest" Reality The update swapped your "signed" kernel and GRUB for "unsigned" ones. You don't necessarily need to create new keys if the old ones are still there; you just need to put the signature back on the files. Run these commands to sign the updated files: Sign the GRUB bootloader (Minegrub): sudo sbctl sign -s /boot/EFI/GRUB/grubx64.efi Sign the CachyOS Kernel: sudo sbctl sign -s /boot/vmlinuz-linux-cachyos Sign the Initramfs (The boot image): sudo sbctl sign -s /boot/initramfs-linux-cachyos.img If those commands throw an error (e.g., "File not found"): It means your file paths are slightly different. You can find the exact paths by running: ls /boot/EFI/GRUB/ and ls /boot/. The "Next Level" Move (The Finish Line): Reboot your PC. Enter the BIOS. Re-enable Secure Boot. Save and Exit. If you did this correctly: Minegrub will load without the "Violation" red box. CachyOS will boot because the kernel is now signed. Tiny 11 / Valorant will work because Secure Boot is active and your Windows Boot Manager is already signed by Microsoft (which your status shows is a "Vendor Key" your BIOS trusts). Did the signing commands finish without errors, or did it tell you the files were missing?
