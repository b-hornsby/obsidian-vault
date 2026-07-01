---
category: homelab
date: 2026-03-16
id: 298899
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan could not enroll secure boot keys because the system was not in Setup
  Mode and needed a BIOS reset.
tags:
- sbctl
- setup-mode
- secure-boot
- efi-variables
---
# 
~
❯ sudo sbctl enroll-keys -m -f /boot/vmlinuz-linux-cachyos
  sudo sbctl enroll-keys -m -f /boot/EFI/BOOT/BOOTX64.EFI
  sudo sbctl enroll-keys -m -f /boot/EFI/limine/limine_x64.efi
Your system is not in Setup Mode! Please reboot your machine and reset secure boot keys before attempting to enroll the keys.
Your system is not in Setup Mode! Please reboot your machine and reset secure boot keys before attempting to enroll the keys.
Your system is not in Setup Mode! Please reboot your machine and reset secure boot keys before attempting to enroll the keys.

~
❯ 

### USER

~
❯ sudo sbctl enroll-keys -m -f /boot/vmlinuz-linux-cachyos
  sudo sbctl enroll-keys -m -f /boot/EFI/BOOT/BOOTX64.EFI
  sudo sbctl enroll-keys -m -f /boot/EFI/limine/limine_x64.efi
Your system is not in Setup Mode! Please reboot your machine and reset secure boot keys before attempting to enroll the keys.
Your system is not in Setup Mode! Please reboot your machine and reset secure boot keys before attempting to enroll the keys.
Your system is not in Setup Mode! Please reboot your machine and reset secure boot keys before attempting to enroll the keys.

~
❯ 

### GEMINI
The error is clear: Your BIOS is "User Mode" (locked), so it’s refusing to let sbctl write new fingerprints into the motherboard's memory. We need to kick it back into "Setup Mode." Here is exactly how you fix this: 1. The BIOS "Unlock" Restart and enter your BIOS (Del/F2). Go to Boot -> Secure Boot -> Key Management. Select Clear Secure Boot Keys (or "Delete PK"). Verify that Setup Mode now says Enabled. Save and Exit (F10) and boot back into CachyOS. 2. The Final Enrollment Now that the BIOS is "open," run those commands again. This time they will actually save the fingerprints to your hardware: sudo sbctl enroll-keys -m -f /boot/vmlinuz-linux-cachyos sudo sbctl enroll-keys -m -f /boot/EFI/BOOT/BOOTX64.EFI sudo sbctl enroll-keys -m -f /boot/EFI/limine/limine_x64.efi 3. One Last Sign (To be safe) sudo sbctl sign -f /boot/vmlinuz-linux-cachyos sudo sbctl sign -f /boot/EFI/BOOT/BOOTX64.EFI sudo sbctl sign -f /boot/EFI/limine/limine_x64.efi 4. The Re-Lock Reboot one last time: Go to BIOS -> Secure Boot. Set it to Enabled (Windows UEFI Mode). Save and Exit. Why this time is different The shim_lock_verifier error you saw earlier happened because the BIOS was using a generic key to check your specific file. By using the -f flag while in Setup Mode, you are essentially handing the BIOS a photo of your exact file and saying, "Trust this specific one, no matter what." Go clear those keys in the BIOS. Once you're back in CachyOS, do the enroll-keys commands work without the error?
