---
category: homelab
date: 2026-03-15
id: 227114
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan asked what steps to take after entering sudo cachy-chroot, likely for
  GRUB reconfiguration.
tags:
- cachy-chroot
- grub-reconfiguration
- bootloader-setup
- cachyos-recovery
---
# So from sudo cachy-chroot, what do I do?

### USER
So from sudo cachy-chroot, what do I do?

### GEMINI
Since you are back at the [root@cachyos /]# prompt, we need to find your missing "Linux World." The Minecraft menu (GRUB) is likely only seeing Windows because it didn't look deep enough into your /boot folder. Let's fix that. 1. The Kernel Check First, let's verify your Linux files are actually where they should be. Type: ls /boot If you see vmlinuz-linux-cachyos and initramfs-linux-cachyos.img, proceed to step 2. If you see nothing or just a "grub" folder, we missed a mount point. Exit the chroot (exit) and start sudo cachy-chroot again, but make sure you say Yes when it asks to mount the EFI partition (/dev/nvme0n1p1). 2. Force GRUB to find the Linux Kernel Run this command to rebuild the menu. Watch the screen closely as it runs. grub-mkconfig -o /boot/grub/grub.cfg The "Success" Check: Look for these specific lines in the terminal output: Found linux image: /boot/vmlinuz-linux-cachyos Found initrd image: /boot/initramfs-linux-cachyos.img Found Windows Boot Manager on /dev/nvme0n1p1@... 3. What if it still doesn't find Linux? If the command above only finds Windows, run this to install the CachyOS-specific GRUB settings which usually fix detection issues: pacman -Sy grub-cachyos-settings grub-mkconfig -o /boot/grub/grub.cfg 4. Final Exit Once the terminal successfully lists both Linux and Windows: Type exit and hit Enter. Restart your PC. Ensure the BIOS still has "GRUB" as Priority #1. When you reboot into the Minecraft menu, does your CachyOS "World" show up now?
