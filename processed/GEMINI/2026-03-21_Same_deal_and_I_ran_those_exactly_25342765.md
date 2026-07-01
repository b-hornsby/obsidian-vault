---
id: 972235
source: GEMINI
date: 2026-03-21
tags: ['command-execution', 'troubleshooting', 'setup']
category: coding
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
summary: Bryan confirms he ran some previously discussed commands exactly as instructed.
---
# Same deal and I ran those exactly

### USER
Same deal and I ran those exactly

### GEMINI
This is happening because your BIOS is currently fighting between two different "identities" you've given it, and it's defaulting back to the Limine bouncer instead of the GRUB bouncer you just signed. The red box means it found a file it doesn't trust. The panic means it tried to load a file it doesn't recognize. The "Brutally Honest" Fix You are almost there, but your BIOS is being stubborn about the boot order. We need to force it to use the GRUB file you just signed and ignore Limine entirely. 1. Get past the Red Box (Temporary) Go into BIOS. Disable Secure Boot just for this one boot so you can get back to the desktop. 2. Clean up the Boot Order (On Desktop) Once you are logged in, run these commands to make sure Limine is dead and GRUB is the only king: # This forces GRUB back to the top of the EFI list sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB # This removes the Limine entry from the BIOS so it can't hijack your boot sudo efibootmgr Look at the output of efibootmgr. You will see numbers like Boot0001* CachyOS. Find the one for CachyOS/Limine and delete it: sudo efibootmgr -b [NUMBER] -B (e.g., sudo efibootmgr -b 0001 -B). 3. The "Nuclear" Signing Step Just to be 100% sure the BIOS has no reason to throw that red box again, sign the shim as well: sudo sbctl sign -s /boot/EFI/GRUB/grubx64.efi sudo sbctl sign -s /boot/vmlinuz-linux-cachyos # If you have a file named mmx64.efi or bootx64.efi in /boot/EFI/boot/ sign those too sudo sbctl sign -s /boot/EFI/BOOT/BOOTX64.EFI The Final Move Reboot and enter BIOS. Re-enable Secure Boot. Look at your Boot Priority. You should see "GRUB". Make sure it is the only thing at the top. Save and Exit. Why the red box happened again: Even though you signed the files, your BIOS might be trying to launch a fallback file (like BOOTX64.EFI) that isn't signed yet. Signing everything in that /boot/EFI folder with sbctl sign will stop the "Violation" for good. Would you like me to help you identify which boot numbers to delete in efibootmgr once you're on the desktop?
