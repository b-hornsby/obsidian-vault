---
category: homelab
date: 2026-03-21
id: 379295
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is stating that his BIOS settings were already configured before a
  system update (Syu) caused problems.
tags:
- bios
- secure-boot
- syu-update
- system-update
---
# I already had my stuff enrolled on my bios before the Syu update

### USER
I already had my stuff enrolled on my bios before the Syu update

### GEMINI
The "brutally honest" reality is that the pacman -Syu update replaced your enrolled files with new versions. Even if you previously enrolled grubx64.efi and your kernel, Secure Boot works by checking a specific digital signature. When the update downloaded the new kernel and updated GRUB, those files changed. Because the signature changed, your BIOS now sees them as "unauthorized" tampering—hence the red violation box. Your old enrollment is now a "ghost" record; it points to a version of the files that no longer exists on your disk. The "Strategic Depth" Plan (To get back to "Exactly as it was"): You have to re-verify the new files. You don't need to delete your old enrollments, but you must add the new ones. Step 1: Get to the Desktop (The only way to fix this quickly) Enter your BIOS. Temporarily Disable Secure Boot. (This is just a "maintenance mode" so we can reach the OS). Save and Exit. You should boot straight into Minegrub and see your Tiny 11 option. Step 2: Re-Enroll the NEW Files (Once you're in CachyOS) Since you've done this before, you know the drill, but you need to point the BIOS to the current versions that were just installed: Reboot and enter BIOS again. Go to Key Management / Enroll EFI Image. Navigate to and select the new grubx64.efi in your EFI partition. Navigate to and select the new vmlinuz-linux-cachyos (the kernel). Re-enable Secure Boot. Save and Exit. Why did Limine show up? When CachyOS updated, it added a new boot entry for Limine to your BIOS. Even if you re-enroll your keys, your BIOS might still try to boot Limine first. Critical Priority: In your BIOS Boot Priority list, make sure the entry named "GRUB" is moved to the #1 spot, above "CachyOS" or "Limine". The Blind Spot: If you try to force Secure Boot to "just work" without re-enrolling these specific updated files, you'll stay stuck in that violation loop. The update essentially "broke the seal" on your security, and you have to reseal it manually. Would you like me to wait while you disable Secure Boot and confirm you can get back to the Minegrub screen?
