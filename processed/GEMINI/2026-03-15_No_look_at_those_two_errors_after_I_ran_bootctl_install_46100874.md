---
category: homelab
date: 2026-03-15
id: 513988
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan shared errors received after running the bootctl install command and
  asked for help diagnosing them.
tags:
- bootctl-errors
- bootloader-troubleshooting
- systemd-boot
- cachyos
- error-debugging
---
# No look at those two errors after I ran bootctl install

### USER
No look at those two errors after I ran bootctl install

### GEMINI
I see the issue. Those errors (Failed to open file, No such file or directory) happen because you are in a "chroot" (a virtual session) and the system is looking for configuration files that aren't mounted where it expects them to be. Since your goal is to switch to GRUB for the Minecraft theme anyway, don't worry about those bootctl errors. We are going to replace systemd-boot with GRUB right now. Follow these steps in your current terminal: 1. Install GRUB and the Windows detection tool: pacman -S grub os-prober 2. Install GRUB to your motherboard: This command bypasses the bootctl errors and writes a fresh boot entry directly to your ASUS BIOS. grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB 3. Set up the Minecraft Theme: git clone https://github.com/Lxtharia/minegrub-world-sel-theme.git cd minegrub-world-sel-theme cp -ruv ./minegrub-world-selection /boot/grub/themes/ 4. Make GRUB see Windows and the Theme: Open the configuration file: micro /etc/default/grub (If micro isn't found, use nano /etc/default/grub) Add these lines to the very bottom: GRUB_DISABLE_OS_PROBER=false GRUB_THEME="/boot/grub/themes/minegrub-world-selection/theme.txt" Save (Ctrl+S or Ctrl+O) and Exit (Ctrl+Q or Ctrl+X). 5. Update the boot menu: grub-mkconfig -o /boot/grub/grub.cfg The Reality Check The bootctl errors you saw are "soft" failures—they just mean the old bootloader is being stubborn. By running grub-install, you are essentially installing a new "manager" who doesn't care about the old one's mistakes. Once you finish step 5, type exit, reboot, and check your BIOS. Does "GRUB" appear as a boot option now?
