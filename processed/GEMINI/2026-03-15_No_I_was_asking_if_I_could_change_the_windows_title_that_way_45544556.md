---
category: homelab
date: 2026-03-15
id: 705137
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan asked if he could rename the Windows Boot Manager entry to say 'tiny11'
  in the boot menu.
tags:
- boot-menu-labeling
- windows-boot-manager
- grub-customization
- tiny11
- custom-boot-entry
---
# No I was asking if I could change the windows title that way to say tiny11

### USER
No I was asking if I could change the windows title that way to say tiny11

### GEMINI
The short answer is: No. You can't change the actual name "Tiny11" inside the theme.txt file. Here is the "why" so you don't waste time digging through those theme folders: GRUB is the Boss: GRUB decides the names (like "Windows Boot Manager" or "Tiny11"). Minegrub is just the Painter: The theme just takes whatever name GRUB gives it and draws it on the screen. It's like a picture frame—it can't change what's in the photo. To make it say Tiny11 and have it stay that way forever, you have to go back to the "Source" (the script that tells GRUB what the name is). The Final "Permanent" fix for the Tiny11 Title Run these steps one last time. This is the only way to make it stick regardless of updates: Open the Name-Maker script: sudo micro /etc/grub.d/30_os-prober Find the Title Logic: Press Ctrl+W and search for LONGNAME. You will see a line like: LONGNAME="${LABEL} (on ${DEVICE})" Force it to say Tiny11: Change that entire line to: LONGNAME="Tiny11" (Make sure the quotes are there!) Save & Lock it in: Press Ctrl+S, then Ctrl+Q. Now run: sudo grub-mkconfig -o /boot/grub/grub.cfg What about the "Under-text"? The theme does control the "Survival Mode" and "No Cheats" text. If you want to change that specifically: Go to /boot/grub/themes/minegrub-world-selection/theme.txt. The theme actually uses different icons to "guess" what the text should be. It’s hardcoded to say "Survival Mode" if it sees a Windows icon. To change that, you'd have to edit the actual theme code, which is a headache. Is "Tiny11" showing up as the main title now after running that command?
