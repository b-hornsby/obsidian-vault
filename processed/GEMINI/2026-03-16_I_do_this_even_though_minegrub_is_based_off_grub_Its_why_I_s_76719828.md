---
category: homelab
date: 2026-03-16
id: 869361
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is questioning why he's performing a certain action, given that Minegrub
  is based on GRUB and he switched from Limine for that reason.
tags:
- minegrub
- grub
- limine
- bootloader-comparison
---
# I do this even though minegrub is based off grub? It’s why I switched from limine I thought?

### USER
I do this even though minegrub is based off grub? It’s why I switched from limine I thought?

### GEMINI
Ah, that changes everything. If you manually switched back to GRUB specifically to run Minegrub, then deleting the GRUB folder would indeed break your menu. The reason you are stuck in this loop is that GRUB is built-in with a security feature that specifically looks for a Microsoft-signed "Shim." When you use sbctl to sign the kernel yourself, GRUB sees a mismatch and triggers that prohibited by secure boot policy error. Since you want to keep Minegrub (GRUB) and have Secure Boot ON for Valorant, we have to force GRUB to stop checking for that "Shim." The "Nuclear" fix for Minegrub + Secure Boot We need to tell GRUB to be "blind" to the security policy because the BIOS has already done the verification for us. 1. Boot back into CachyOS (Secure Boot: Disabled). 2. Edit your GRUB configuration: We need to disable the module that is causing the "shim_lock" error. sudo micro /etc/default/grub 3. Add the ignore flag: Find the line GRUB_CMDLINE_LINUX_DEFAULT and add module_blacklist=shim_lock to the end of the list inside the quotes. It should look something like: GRUB_CMDLINE_LINUX_DEFAULT="quiet splash ... module_blacklist=shim_lock" 4. Reinstall GRUB without the "Shim" dependency: This is the critical step. We are going to reinstall the GRUB binaries to the EFI partition without the "Shim" middleman that is failing. sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=CachyOS --no-uefi-secure-boot (Don't let the --no-uefi-secure-boot flag scare you; it just tells GRUB not to look for the Microsoft Shim. Your BIOS will still be in Secure Boot mode.) 5. Sign the new GRUB binary: Now we sign the exact file we just created: sudo sbctl sign -s /boot/EFI/CachyOS/grubx64.efi 6. Update the config: sudo grub-mkconfig -o /boot/grub/grub.cfg Why this is the "Brutal" Truth: GRUB tries to be "too helpful" by enforcing its own secondary security check. By installing it with --no-uefi-secure-boot, you're telling GRUB: "I've already handled the security at the BIOS level with my own keys, so just load the OS." Try those steps. By bypassing the Shim, GRUB should stop throwing that error and just let the Minecraft menu load. Does it get you past the grub rescue screen now?
