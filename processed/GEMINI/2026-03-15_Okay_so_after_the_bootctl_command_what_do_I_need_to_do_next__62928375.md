---
category: homelab
date: 2026-03-15
id: 928921
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan asked what to do after the bootctl command and whether switching from
  CachyOS's default bootloader to GRUB for the Minecraft theme was advisable.
tags:
- bootctl
- grub-switch
- minecraft-theme
- cachyos-bootloader
- next-steps
---
# Okay so after the bootctl command, what do I need to do next? Is it bad to switch the cachyos thing to grub for this Minecraft theme?

### USER
Okay so after the bootctl command, what do I need to do next? Is it bad to switch the cachyos thing to grub for this Minecraft theme?

### GEMINI
Those "security hole" warnings are just the system being overly cautious because the Live USB has full access to the files—it is perfectly safe to proceed. To answer your question: No, it is not "bad" to switch to GRUB. * The Pro: You get the Minegrub theme and a much better visual experience for dual-booting. The Reality: CachyOS uses systemd-boot by default because it's slightly faster and simpler. Switching to GRUB is a standard move for people who want customization. As long as we run the commands correctly, it won't hurt your performance. Since you already have the "chroot" open and the prompt says [root@CachyOS /]#, stay right there and run these commands to finish the Minegrub setup: 1. Install the GRUB software This installs the bootloader and the tool needed to find your Windows partition. pacman -S grub os-prober 2. Register GRUB with your BIOS This command tells your ASUS motherboard that GRUB is now the primary boot manager. grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB 3. Download and Install the Theme git clone https://github.com/Lxtharia/minegrub-world-sel-theme.git cd minegrub-world-sel-theme cp -ruv ./minegrub-world-selection /boot/grub/themes/ 4. Enable the "Select World" Screen We need to tell GRUB to use the theme and to look for Windows. Type: micro /etc/default/grub Scroll to the very bottom and add these lines: GRUB_DISABLE_OS_PROBER=false GRUB_THEME="/boot/grub/themes/minegrub-world-selection/theme.txt" Save & Exit: Press Ctrl+S, then Ctrl+Q. 5. Generate the Final Menu This is the part that actually creates the Minecraft menu. grub-mkconfig -o /boot/grub/grub.cfg Watch the output: It should say "Found Windows Boot Manager" and "Found theme." The Reboot Type exit to leave the chroot. Restart your PC. Mash F2/Delete to enter the BIOS. In the Boot tab, you should now see "GRUB". Move it to Priority #1. Save and Exit (F10). Does the Minecraft "World Selection" screen pop up for you now?
