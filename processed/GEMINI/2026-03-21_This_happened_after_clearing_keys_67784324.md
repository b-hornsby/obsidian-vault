---
id: 866566
source: GEMINI
date: 2026-03-21
tags: ['secure-boot', 'keys', 'bios', 'troubleshooting']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is troubleshooting an issue that occurred after clearing secure boot keys.
---
# This happened after clearing keys?

### USER
This happened after clearing keys?

### GEMINI
The first image shows you are back in the Limine Panic. This is happening because when you cleared the keys, your BIOS boot priority likely reset or defaulted back to the "CachyOS" (Limine) entry instead of the "GRUB" entry you fixed earlier. The second image (the wall of text) shows a partial boot sequence that stalled out. This is a mess of competing boot configurations. Let’s get you back to the Desktop (Again) You need to bypass that hash check one more time to get into the OS so we can finalize the keys. On the Limine Panic screen: Press a key to return to the menu. Highlight the CachyOS entry and press E to edit. Delete the # and everything after it on the module_path and path lines (just like you did at the very beginning of this session). Press F10 to boot. The "Brutally Honest" Final Steps (Once Logged In) Since your keys are already cleared in the BIOS, your system is in Setup Mode. This is the only time the following commands will actually work to link your Secure Boot to CachyOS forever. Run these in the terminal immediately upon reaching the desktop: Enroll the keys (Crucial step): sudo sbctl enroll-keys -m If this works, it will say "Successfully enrolled keys". Sign your files (The "Magic" step): sudo sbctl sign -s /boot/EFI/GRUB/grubx64.efi sudo sbctl sign -s /boot/vmlinuz-linux-cachyos Kill the Limine problem for good: Since Limine keeps jumping in front of GRUB, we need to tell the system to prioritize GRUB (Minegrub) in the actual EFI variables: sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB Why did it look like it was crashing? When you cleared the keys, the BIOS lost its "memory" of which bootloader was the preferred one. It saw a bunch of new files and tried to boot the first one it found (Limine), which then panicked because the hashes didn't match. Once you do those 3 terminal steps above, you can reboot and everything—Minegrub, Tiny 11, and Valorant (Secure Boot)—will finally be "exactly as it was." Were you able to bypass the Limine screen and reach the desktop?
