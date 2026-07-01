---
category: homelab
date: 2026-03-15
id: 983128
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan encountered a mkinitcpio error about missing presets and was trying
  to regenerate the initramfs on CachyOS.
tags:
- mkinitcpio
- cachyos
- initramfs
- boot-error
---
# [root@CachyOS /]# mkinitcpio -P
==> ERROR: No presets found in /etc/mkinitcpio.d
==> WARNING: This does not update Limine boot entries.
    Use 'limine-mkinitcpio' or 'limine-update' instead.
==> Would you like to run 'limine-mkinitcpio' now? [Y/n]: 

### USER
[root@CachyOS /]# mkinitcpio -P
==> ERROR: No presets found in /etc/mkinitcpio.d
==> WARNING: This does not update Limine boot entries.
    Use 'limine-mkinitcpio' or 'limine-update' instead.
==> Would you like to run 'limine-mkinitcpio' now? [Y/n]: 

### GEMINI
This is the "moment of truth" regarding why your kernel files are missing. Because you don't have any presets in /etc/mkinitcpio.d, it confirms the kernel package isn't actually installed on your system right now—it’s just the leftover configuration folders. Since we are moving to GRUB for the Minecraft theme, we don't need Limine. Answer n (no) to that prompt. Then, run these commands to force-install the kernel and build the presets: 1. Reinstall the kernel packages This is what creates those missing presets so mkinitcpio can actually do its job. pacman -Sy linux-cachyos linux-cachyos-headers linux-cachyos-nvidia-open nvidia-utils 2. Now run the build command again Now that the files are physically there, this command should actually work: mkinitcpio -P It should now list "cachyos" and say "Successfully generated." 3. Update the Minecraft Menu grub-mkconfig -o /boot/grub/grub.cfg Why the error happened: mkinitcpio is the "chef" and the presets are the "recipes." Right now, the chef is standing in an empty kitchen. Running the pacman command in Step 1 puts the recipes (presets) and the ingredients (kernel files) back on the counter. After you run that pacman command, does the mkinitcpio -P command actually show progress this time?
