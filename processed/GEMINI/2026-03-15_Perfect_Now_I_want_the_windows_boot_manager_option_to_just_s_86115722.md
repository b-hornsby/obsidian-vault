---
category: homelab
date: 2026-03-15
id: 311573
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wanted to rename the Windows Boot Manager entry in the GRUB menu to
  simply say 'tiny11'.
tags:
- boot-menu-labeling
- windows-boot-manager
- grub-customization
- tiny11
- entry-rename
---
# Perfect. Now I want the windows boot manager option to just say tiny11 rather than that long title

### USER
Perfect. Now I want the windows boot manager option to just say tiny11 rather than that long title

### GEMINI
Since you're happy with the Linux side saying CachyOS, we’ll use a targeted command to clean up that long Windows title without you having to manually dig through the code again. Run this command in your CachyOS terminal: sudo sed -i 's/Windows Boot Manager (on \/dev\/nvme0n1p1)/Tiny11/g' /boot/grub/grub.cfg What this does: It performs a "surgical strike" on your boot file. It looks for that exact long string (Windows Boot Manager (on /dev/nvme0n1p1)) and swaps it for Tiny11. Important Note: As we discussed, if you ever run sudo grub-mkconfig in the future, it will generate that long name again. If that happens, just copy-paste that sed command above to fix it in one second. Go ahead and reboot. Does it finally look the way you want it?
