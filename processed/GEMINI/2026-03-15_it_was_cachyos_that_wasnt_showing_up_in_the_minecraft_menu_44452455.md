---
category: homelab
date: 2026-03-15
id: 843814
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan identified that CachyOS was the OS not showing up in the Minecraft-themed
  GRUB boot menu.
tags:
- minegrub
- cachyos-boot-entry
- grub-theme
- boot-menu-missing
- os-prober
---
# it was cachyos that wasnt showing up in the minecraft menu 

### USER
it was cachyos that wasnt showing up in the minecraft menu 

### GEMINI
That’s because the Minecraft theme (GRUB) is looking for a configuration file that hasn’t been fully "mapped" to your Linux kernel yet. You’ve got the menu working, but the "World" (CachyOS) is missing from the list. Here is the no-nonsense fix to force GRUB to find CachyOS. Do this from that [root@cachyos /]# prompt: 1. Verify the Kernel exists Run this to make sure your Linux "engine" is actually there: ls /boot Success: You see vmlinuz-linux-cachyos. Failure: If you see nothing, you need to exit, restart sudo cachy-chroot, and make sure you say Yes to all mount prompts. 2. Force the Scan Run this command. Watch the output like a hawk. grub-mkconfig -o /boot/grub/grub.cfg What you want to see: A line that says Found linux image: /boot/vmlinuz-linux-cachyos. If it still doesn't see it: It means your GRUB is stuck in a "basic" mode. Run this to give it the CachyOS brain: pacman -Sy grub-cachyos-settings grub-mkconfig -o /boot/grub/grub.cfg 3. The "Missing World" Safeguard If you run grub-mkconfig and it still only lists Windows, it’s likely because CachyOS uses a specific Btrfs layout that GRUB is ignoring. Run this "force" command: os-prober If os-prober shows both Windows and Linux, run the grub-mkconfig command one last time. Is it "bad" to use GRUB instead of CachyOS default? No. You're trading about 0.5 seconds of boot speed for a high-level UI (Minecraft theme). On an i7-12700K with an NVMe drive, you won't even notice the difference. GRUB is the industry standard for dual-booting; it's not "worse," it's just more robust (and customizable) than the default systemd-boot. Run grub-mkconfig now. Does the terminal output finally say "Found linux image"?
