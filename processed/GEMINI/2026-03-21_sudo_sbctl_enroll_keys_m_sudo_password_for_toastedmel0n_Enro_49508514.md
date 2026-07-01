---
id: 224386
source: GEMINI
date: 2026-03-21
tags: ['secure-boot', 'sbctl', 'enroll-keys', 'efi-configuration']
category: coding
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is enrolling secure boot keys using sbctl, indicating he's configuring secure boot.
---
# ❯ sudo sbctl enroll-keys -m
[sudo] password for toastedmel0n:  
Enrolling keys to EFI variables...
With vendor keys from microsoft...✓  
Enrolled keys to the EFI variables!

~
❯  

### USER
❯ sudo sbctl enroll-keys -m
[sudo] password for toastedmel0n:  
Enrolling keys to EFI variables...
With vendor keys from microsoft...✓  
Enrolled keys to the EFI variables!

~
❯  

### GEMINI
Perfect. The BIOS "bouncer" now has the new guest list, and it includes Microsoft so Tiny 11 and Valorant stay happy. Now you just need to "tag" your specific Linux files so the BIOS recognizes them as authorized. If you don't do this next step, the BIOS will still block them for being "unsigned." 1. Sign the Bootloader and Kernel Run these two commands to apply your new signatures: # This signs your Minegrub/GRUB bootloader sudo sbctl sign -s /boot/EFI/GRUB/grubx64.efi # This signs your CachyOS Kernel sudo sbctl sign -s /boot/vmlinuz-linux-cachyos 2. Make GRUB the Boss Again Because Limine (that blue screen) keeps trying to hijack the boot process, run this to re-assert GRUB as the #1 priority in your BIOS boot list: sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB The Finish Line Once those are done, you are ready for the final reboot: Reboot and enter your BIOS. Ensure Secure Boot is ENABLED. Check that "GRUB" is the #1 Boot Option (move it to the top if Limine or "CachyOS" is ahead of it). Save and Exit. The Brutally Honest Result: You will boot into Minegrub, you'll see Tiny 11, and Valorant will launch without complaining because Secure Boot is officially "on" and verified. Plus, sbctl will now automatically sign your kernel every time you update in the future—no more red boxes. Did the signing commands (Step 1) finish without any errors?
