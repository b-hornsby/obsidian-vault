---
id: 605135
source: GEMINI
date: 2026-03-21
tags: ['cachyos', 'boot-menu', 'installation', 'linux']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan accidentally booted into CachyOS and is asking about what happened.
---
# The image I just sent I pressed space and it went through and now I’m in cachy?

### USER
The image I just sent I pressed space and it went through and now I’m in cachy?

### GEMINI
Since you are in CachyOS now, you are in the "Golden Window." Your BIOS is currently in Setup Mode, which means it is wide open and waiting for you to tell it what to trust. If you reboot right now without running these commands, you'll just end up back at that panic screen. We need to "lock in" your Minegrub and CachyOS kernel so Secure Boot and Valorant work perfectly. The "Lock-In" Sequence Run these commands in your terminal immediately: 1. Enroll the New "VIP List" This tells your BIOS to trust your own custom keys plus Microsoft's keys (so Tiny 11 still boots). sudo sbctl enroll-keys -m Wait for it to say "Successfully enrolled keys." 2. Sign the Files (The Permanent Fix) This "stamps" your bootloader and kernel with your new trusted keys. # This signs your Minegrub/GRUB sudo sbctl sign -s /boot/EFI/GRUB/grubx64.efi # This signs your CachyOS Kernel sudo sbctl sign -s /boot/vmlinuz-linux-cachyos 3. Re-assert GRUB (Minegrub) as #1 Since Limine keeps trying to cut in line, this command ensures GRUB is the primary boot entry in your BIOS. sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB The Final Test Reboot your PC. Go into your BIOS one last time. Ensure Secure Boot is ENABLED. Check that "GRUB" is the #1 Boot Option. Save and Exit. Why this is "Exactly how it was" Minegrub will load because you signed it. Tiny 11 will boot because you used the -m flag (Microsoft keys). Valorant will work because Secure Boot is officially "Enabled" and your BIOS is back in "User Mode" with valid keys. Did the sudo sbctl enroll-keys -m command give you a success message?
