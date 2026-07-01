---
category: homelab
date: 2026-03-16
id: 097295
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/homelab.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
tags:
- homelab
- module
- gemini
- go
- error
- package
---
# ❯ sudo micro /etc/default/grub
[sudo] password for toastedmel0n:  

~ 1m 34s
❯ sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=CachyOS --no-uefi-secure-boot
grub-install: unrecognized option '--no-uefi-secure-boot'
Try 'grub-install --help' or 'grub-install --usage' for more information.

~
❯  

### USER
❯ sudo micro /etc/default/grub
[sudo] password for toastedmel0n:  

~ 1m 34s
❯ sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=CachyOS --no-uefi-secure-boot
grub-install: unrecognized option '--no-uefi-secure-boot'
Try 'grub-install --help' or 'grub-install --usage' for more information.

~
❯  

### GEMINI
My bad—some versions of grub-install don't recognize that specific flag, or they expect it slightly differently. Since we are on CachyOS (Arch-based), we can achieve the exact same result by just omitting the shim package during the install. We’re going to run a slightly different command that forces GRUB to generate a clean, standalone EFI file that doesn't look for the "Shim" middleman. Step 2 (Revised): Re-Install GRUB Run this command instead: sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=CachyOS --modules="tpm" --disable-shim-lock --modules="tpm": Ensures it can still talk to your motherboard's security chip. --disable-shim-lock: This is the specific internal flag that stops that "prohibited by policy" error. Step 3: Sign the Result Once that finishes (it should take a few seconds), sign that new file so the BIOS accepts it: Sign the binary: sudo sbctl sign -s /boot/EFI/CachyOS/grubx64.efi Verify everything is green: sudo sbctl verify Step 4: Final BIOS Check If sbctl verify shows green checkmarks for grubx64.efi and your vmlinuz kernel: Reboot. Enable Secure Boot. Save and Exit. Does that grub-install command with the --disable-shim-lock flag go through without an error?
