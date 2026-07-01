---
category: homelab
date: 2026-03-16
id: 795941
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan reported the same boot issue persisted after attempting fixes.
tags:
- boot-issue
- cachyos
- reboot-problem
---
# Same deal after all that

### USER
Same deal after all that

### GEMINI
This is stubborn, but the error message gives us the final clue. That grub rescue> prompt proves that your computer is still trying to boot using GRUB, even though you are using CachyOS which defaults to Limine. The shim_lock error is happening because the BIOS trusts the GRUB file, but GRUB itself has its own internal security check that is failing because it doesn't recognize your custom keys. The Strategy: Delete the "Fake" Bootloader We need to stop the computer from ever looking at GRUB. We want it to go straight to Limine (the Minegrub menu). 1. Boot back into CachyOS (Secure Boot: Disabled). 2. Delete the GRUB EFI folder: This removes the "wrong" door that the BIOS keeps trying to walk through. sudo rm -rf /boot/EFI/GRUB 3. Tell the BIOS to forget GRUB: We need to remove the "GRUB" entry from your motherboard's memory so it defaults to CachyOS/Limine. sudo efibootmgr Look for an entry named grub. It will have a number like Boot0001. Delete it (replace XXXX with that number): sudo efibootmgr -b XXXX -B 4. Set Limine as the #1 Priority: Find the number for CachyOS or Limine (e.g., Boot0002) and force it to be first: sudo efibootmgr -o XXXX 5. One last "Safety Sign": Ensure the Limine file is absolutely signed one more time: sudo sbctl sign -s /boot/EFI/BOOT/BOOTX64.EFI Why this will work: The error in your photo is coming from GRUB. If we delete GRUB, the BIOS will be forced to use the Limine file we signed and enrolled earlier. Limine doesn't use the "Shim" system that is causing that prohibited by secure boot policy error—it just boots the kernel directly using the keys we put in the BIOS. Delete that /boot/EFI/GRUB folder and clean up the efibootmgr list. Does the PC finally skip that black screen and show you the Minecraft menu with Secure Boot ON?
