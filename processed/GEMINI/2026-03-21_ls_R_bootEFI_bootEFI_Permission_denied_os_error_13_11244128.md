---
category: coding
date: 2026-03-21
id: 473085
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to list the contents of the /boot/EFI directory recursively
  but is getting a permission denied error, indicating a problem with boot configuration.
tags:
- efi-directory
- permission-denied
- boot-configuration
- file-permissions
---
# ~
❯ ls -R /boot/EFI
"/boot/EFI": Permission denied (os error 13)

~
❯ 

### USER
~
❯ ls -R /boot/EFI
"/boot/EFI": Permission denied (os error 13)

~
❯ 

### GEMINI
The permission denied error is just a minor hurdle—you just need sudo to peek into that directory. But let’s cut to the chase. You're an operations professional; you know that a system that requires this much manual "massaging" just to boot is a liability, not an asset. If you're 5 minutes away from wiping the drive for Tiny 11, this is your final diagnostic check. 1. Find the "Ghost" Bootloader Run this to see where the actual files are hiding: sudo ls -R /boot/EFI Look for a folder named GRUB or Arch. If you see grubx64.efi in there, that is the file we need to sign. 2. Sign the "Real" Minegrub Based on where you find it, run the sign command specifically on that path. For example: sudo sbctl sign -s /boot/EFI/GRUB/grubx64.efi 3. Kill the Limine Entry (The "Cleaner" Move) This is likely why you keep seeing that blue screen or the red violation box. Your BIOS still thinks the untrusted Limine is the #1 priority. Run this and look at the list: sudo efibootmgr Identify the number for "CachyOS" (which points to Limine). Identify the number for "GRUB" (which points to your Minegrub). Delete the CachyOS one: sudo efibootmgr -b [NUMBER] -B The "Mirror" Moment If you do this and you still see that red box, it means your BIOS's "Secure Boot" database is out of sync with your physical drive. The Strategy: If sudo efibootmgr shows that GRUB is the only boot option and it is signed (check with sbctl list-files), and it still fails? Wipe it. You have a high-performance 12700K/3070 rig. The "opportunity cost" of spending another hour on this is literally a night of gaming or working on your DeFi agent. Don't fall into the "Sunk Cost Fallacy"—if Linux isn't serving your goals right now, Tiny 11 is a perfectly rational pivot to get back to productivity. What does the output of sudo efibootmgr look like? I'll tell you exactly which entry is the "traitor" in your BIOS.
