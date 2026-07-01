---
id: 323102
source: GEMINI
date: 2026-03-15
tags: ['bootloader-configuration', 'system-inspection']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is sharing what he sees in his bootloader configuration, likely to provide context for a problem he's troubleshooting.
---
# this is what i see in the boot loader config:

### USER
this is what i see in the boot loader config:

### GEMINI
The config looks exactly right! You've successfully added the os-prober and GRUB_THEME lines at the bottom (lines 63 and 64). Since you’re still in that terminal, there is one final, critical step to actually "bake" these settings into the bootloader. If you don't do this, the computer won't know the file has changed. The Final Command Type this in your terminal and hit Enter: grub-mkconfig -o /boot/grub/grub.cfg What to watch for: It should say: Found theme: /boot/grub/themes/minegrub-world-selection/theme.txt It should say: Found Windows Boot Manager on /dev/nvme0n1p1@... Wrapping Up Once that command finishes without errors: Type exit and hit Enter. Restart your PC. Mash F2/Delete to enter your BIOS. In the Boot tab, you should now see an option named "GRUB". Move GRUB to Priority #1. Save and Exit (F10). If everything went according to plan, your monitor should light up with the Minecraft "World Selection" screen. One world for CachyOS, one world for Tiny11. Did the grub-mkconfig command find both the theme and Windows?
