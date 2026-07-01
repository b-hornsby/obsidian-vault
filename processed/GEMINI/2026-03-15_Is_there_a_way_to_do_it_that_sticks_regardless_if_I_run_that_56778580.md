---
category: homelab
date: 2026-03-15
id: 103551
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan asked if there was a way to make bootloader changes persist regardless
  of running sudo grub commands.
tags:
- grub-configuration
- bootloader-persistence
- sudo-grub
- dual-boot
- cachyos
---
# Is there a way to do it that sticks regardless if I run that sudo grub command?

### USER
Is there a way to do it that sticks regardless if I run that sudo grub command?

### GEMINI
Yes, there is a way to make it permanent. To do this, we have to stop the script that "discovers" Windows from naming it that long, ugly string. We’re going to edit the actual os-prober logic that GRUB uses to build the menu. Follow these steps in your CachyOS terminal: 1. Open the OS-Prober GRUB script This is the file that decides how Windows is named when you run the grub-mkconfig command. sudo micro /etc/grub.d/30_os-prober 2. Find and Replace the Name Logic Press Ctrl+W (search) and type LONGNAME. You are looking for a line that looks exactly like this: LONGNAME="${LABEL} (on ${DEVICE})" Change it to this: LONGNAME="Tiny11" [!IMPORTANT] Make sure you keep the quotes. It should look like: LONGNAME="Tiny11" 3. Save and Apply Press Ctrl+S to save and Ctrl+Q to exit. Now, run the "magic" command to rebuild the menu: sudo grub-mkconfig -o /boot/grub/grub.cfg Why this works: By changing the LONGNAME variable in the template, you’ve told GRUB: "I don't care what device Windows is on; every time you find it, call it Tiny11." Now, even if you update your system or run that command again, it will always default to your custom name. One last thing: If you want to make sure the CachyOS name also sticks permanently (if it hasn't already): sudo micro /etc/default/grub Change GRUB_DISTRIBUTOR="Arch" to GRUB_DISTRIBUTOR="CachyOS" Save and run the grub-mkconfig command again. Reboot one more time—is the menu finally perfect and "update-proof"?
