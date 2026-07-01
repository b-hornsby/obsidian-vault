---
category: coding
date: 2026-03-21
id: 703269
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to create and enroll secure boot keys using sbctl, but the
  system is not in setup mode, indicating a problem with secure boot configuration.
tags:
- secure-boot
- sbctl
- key-creation
- enroll-keys
- setup-mode
---
# ❯ sudo sbctl create-keys
  sudo sbctl enroll-keys -m
[sudo] password for toastedmel0n:  
Created Owner UUID ec897f63-4161-4381-abaf-68b5d043d37e
✓ Secure boot keys have already been created!
Your system is not in Setup Mode! Please reboot your machine and reset secure boot keys before attempting to enroll the keys.

~ 7s
❯ 

### USER
❯ sudo sbctl create-keys
  sudo sbctl enroll-keys -m
[sudo] password for toastedmel0n:  
Created Owner UUID ec897f63-4161-4381-abaf-68b5d043d37e
✓ Secure boot keys have already been created!
Your system is not in Setup Mode! Please reboot your machine and reset secure boot keys before attempting to enroll the keys.

~ 7s
❯ 

### GEMINI
This is the "Brutally Honest" wall every Linux user hits with Secure Boot. Your BIOS is currently in User Mode (it’s "locked" with the factory keys). To take control and sign your own files so this never breaks again, you have to temporarily "unlock" the BIOS. The "Unlock" Plan (In your BIOS) You need to put your motherboard into Setup Mode. Reboot and enter your BIOS (F2/Del). Navigate to the Secure Boot settings. Look for an option called "Clear Secure Boot Keys" or "Delete All Keys". Don't worry: This doesn't delete Windows; it just tells the BIOS "I'm about to give you new instructions." Once you click that, the status should change from User Mode to Setup Mode. Ensure Secure Boot is still ENABLED (even if keys are cleared). Save and Exit. The "Enroll" Plan (Back on Desktop) Once you boot back into CachyOS, your BIOS is now "listening" for new keys. Run these commands: Enroll your new keys: sudo sbctl enroll-keys -m (The -m is crucial—it includes Microsoft’s keys so Tiny 11 and Valorant don't break). Sign your files (The permanent fix): # Sign GRUB (Minegrub) sudo sbctl sign -s /boot/EFI/GRUB/grubx64.efi # Sign the Kernel (The thing that panics) sudo sbctl sign -s /boot/vmlinuz-linux-cachyos Check the status: sbctl status It should now show Setup Mode: Disabled and Secure Boot: Enabled. Why this is better than before: By using sbctl, CachyOS will now automatically re-sign these files every time you run an update. You won't have to do this BIOS dance again. Ready to jump into the BIOS and "Clear Keys" so we can finish the enrollment?
