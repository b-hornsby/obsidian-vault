---
id: 479834
source: GEMINI
date: 2026-03-21
tags: ['secure-boot', 'sbctl', 'efi-signing', 'bootloader-configuration']
category: coding
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is trying to sign EFI files using sbctl, but the files are already signed, indicating he's configuring secure boot.
---
# ~
❯ sudo find /boot/EFI -name "*.efi" -exec sbctl sign -s {} +
[sudo] password for toastedmel0n:  
File has already been signed /boot/EFI/limine/limine_x64.efi

~
❯  

### USER
~
❯ sudo find /boot/EFI -name "*.efi" -exec sbctl sign -s {} +
[sudo] password for toastedmel0n:  
File has already been signed /boot/EFI/limine/limine_x64.efi

~
❯  

### GEMINI
The bouncer is still looking at the wrong ID card. The fact that it only signed limine_x64.efi tells me your Minegrub/GRUB files might be hiding in a different directory or your /boot partition isn't mounted where sbctl expects it to be. If you are ready to give up, I don't blame you—this is the "Linux Tax" at its most expensive. But as an operations guy, you know that deleting the wrong process is the key to stability. The "One Last Strike" Strategy We need to find where the real GRUB file is and sign it, then kill the "CachyOS" (Limine) entry from the BIOS so it physically cannot boot that blue screen anymore. 1. Find and Sign EVERYTHING Run this to see where your EFI files actually live: ls -R /boot/EFI If you see a GRUB or arch folder in there, run this to force-sign it specifically: sudo sbctl sign -s /boot/EFI/GRUB/grubx64.efi # AND sign the kernel again just to be safe sudo sbctl sign -s /boot/vmlinuz-linux-cachyos 2. The "Nuclear" BIOS Cleanup This is the most important step. We need to see what the BIOS thinks is #1 and delete the "CachyOS" entry that keeps forcing Limine on you. sudo efibootmgr Look at the output. * You will see things like Boot0001* CachyOS and Boot0002* GRUB. Delete the one that says CachyOS: sudo efibootmgr -b 0001 -B (replace 0001 with whatever number CachyOS is). 3. Re-Verify the Signatures sudo sbctl list-files If vmlinuz-linux-cachyos and grubx64.efi both say Signed: ✓, you are officially done. The "Mirror" Truth If you do this and you still see that red box or the Limine screen upon reboot, it means your BIOS is caching the "Limine" bootloader in its own internal memory and refusing to let it go. At that point, the opportunity cost has peaked. If you value your time more than this specific OS configuration, go full Tiny 11. You've got an i7-12700K and a 3070; you should be playing games, not acting as a unpaid sysadmin for a bootloader that doesn't want to cooperate. Do you want to paste the output of efibootmgr here so I can tell you exactly which one to delete?
