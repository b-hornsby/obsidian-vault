---
category: homelab
date: 2026-03-15
id: 523491
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan ran the bootctl install command and received two security hole warnings,
  asking if they were concerning.
tags:
- bootctl
- systemd-boot
- security-warnings
- bootloader-install
- cachyos
---
# No I ran that bootctl install command, it ran and I got two security hole warning?

### USER
No I ran that bootctl install command, it ran and I got two security hole warning?

### GEMINI
Those "security hole" warnings are normal when you're working from a Live USB. It's just complaining because the permissions on your boot folder are currently wide open so the Live USB can work on them. Ignore the warnings. The important part is the very last line: Created EFI boot entry "Linux Boot Manager". This means your motherboard finally sees CachyOS again. Now, let’s get that Minecraft theme (Minegrub) set up before you reboot, so you don't have to come back here. Run these commands exactly in that same terminal: 1. Install GRUB (the manager for the Minecraft theme): pacman -S grub os-prober 2. Install GRUB to your motherboard: grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB 3. Download and Install the Minecraft Theme: git clone https://github.com/Lxtharia/minegrub-world-sel-theme.git cd minegrub-world-sel-theme cp -ruv ./minegrub-world-selection /boot/grub/themes/ 4. Activate the Theme and Windows Detection: Type micro /etc/default/grub (or nano /etc/default/grub). Scroll to the very bottom and add these two lines: GRUB_DISABLE_OS_PROBER=false GRUB_THEME="/boot/grub/themes/minegrub-world-selection/theme.txt" Save and Exit (Ctrl+S, Ctrl+Q for Micro; Ctrl+O, Enter, Ctrl+X for Nano). 5. Final Step—Apply everything: grub-mkconfig -o /boot/grub/grub.cfg Watch the text scroll by. It should say "Found Windows Boot Manager" and "Found theme." The Finish Line Type exit and hit Enter. Restart your PC and mash F2/Delete to enter the BIOS. In the Boot tab, you should now see "GRUB". Move it to Priority #1. Save and Exit (F10). If you see the Minecraft "Select World" screen, you've won. Which world are you entering first?
