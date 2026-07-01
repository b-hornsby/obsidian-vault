---
category: homelab
date: 2026-03-15
id: 658109
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan reported that his Linux installation wasn't showing up in the boot
  menu.
tags:
- bootloader
- linux-not-detected
- grub
- dual-boot-issues
- os-prober
---
# It does but my Linux doesn’t show up?

### USER
It does but my Linux doesn’t show up?

### GEMINI
This happens because grub-mkconfig sometimes misses the Linux kernel if it's looking in the wrong place during a chroot. Since you can see the Minecraft menu but only Windows is listed, we need to go back in and tell GRUB exactly where your CachyOS "World" is. The Fix (Back in the Live USB Terminal) If you already closed the terminal, run sudo cachy-chroot again to get back to the [root@CachyOS /]# prompt. Then run these steps: 1. Check for the Kernel Run this to make sure your Linux kernel files are actually visible: ls /boot You should see files like vmlinuz-linux-cachyos and initramfs-linux-cachyos.img. If you don't see them, let me know immediately. 2. Re-run the Config (The "Deep Scan") Sometimes GRUB needs a nudge to refresh its script. Run this: grub-mkconfig -o /boot/grub/grub.cfg Watch the output closely. It should say: Found linux image: /boot/vmlinuz-linux-cachyos Found initrd image: /boot/initramfs-linux-cachyos.img 3. If it still doesn't find Linux: We need to make sure the GRUB package for CachyOS is fully updated. Run: pacman -Sy grub-cachyos-settings grub-mkconfig -o /boot/grub/grub.cfg Why this is happening: In a dual-boot setup, os-prober is great at finding Windows, but GRUB sometimes ignores the local Linux install if it thinks it’s already handled by another bootloader. By running the config again inside the chroot, we’re forcing it to look at the local drive. One Final Check: If you reboot and still only see Windows: Is there a "Skip" or "Advanced Options" button on the Minecraft screen? Did the grub-mkconfig command actually list "Found linux image" in the terminal? Does the terminal show "Found linux image" when you run that last command?
