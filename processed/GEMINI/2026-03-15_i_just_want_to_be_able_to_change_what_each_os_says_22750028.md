---
category: coding
date: 2026-03-15
id: 886029
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan wants to customize the names displayed for each operating system in
  the bootloader menu.
tags:
- bootloader-customization
- os-naming
- grub-configuration
- dual-boot-appearance
---
# i just want to be able to change what each os says

### USER
i just want to be able to change what each os says

### GEMINI
Look, the "clean" way failed because GRUB's automation is stubborn. If you want the names changed right now without fighting the scripts, you have to go straight to the source. The file /boot/grub/grub.cfg is what actually draws that menu. We’re going to manually overwrite the labels. The Direct Method (Immediate Results) Open the actual boot file: sudo micro /boot/grub/grub.cfg Find the Windows Entry: Press Ctrl+F and search for Windows Boot Manager. You’ll see a line starting with menuentry "Windows Boot Manager". Change it to: menuentry "Hardcore Mode (Tiny11)" (or whatever you want). Find the Linux Entry: Search for CachyOS. You’ll see a line starting with menuentry "CachyOS". Change it to: menuentry "Survival Mode (Linux)". Save and Exit: Press Ctrl+S then Ctrl+Q. The Reality Check (The "Catch") The reason I didn't tell you to do this first is that this is a temporary fix. The next time CachyOS updates your kernel or you run a system update that triggers grub-mkconfig, it will overwrite this file and your "boring" names will come back. The "Permanent" Fix If you want these names to stay forever, you have to edit the template that GRUB uses to build the file. For Linux: sudo micro /etc/default/grub Find the line GRUB_DISTRIBUTOR="CachyOS" and change it to GRUB_DISTRIBUTOR="Survival Mode". For Windows: This is harder because it's "found" by a script called os-prober. To change this permanently, you'd have to edit the os-prober script itself—which is overkill. My advice: Just do the Direct Method above for now. It takes 30 seconds. If a system update wipes the names in a month, just run that micro command again. Do you want to try the "Direct Method" and reboot to see if it worked?
