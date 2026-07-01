---
category: coding
date: 2026-03-15
id: 478923
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is seeking clarification on which installation option to choose and
  what to do next, likely during a dual-boot setup.
tags:
- installation-options
- system-configuration
- dual-boot-setup
---
# Which option is what I’m asking and then from there what do I do?

### USER
Which option is what I’m asking and then from there what do I do?

### GEMINI
In that list, you need to select the Btrfs partition. 1. The Selection Use your arrow keys to highlight: Partition: /dev/nvme0n1p2: FS: btrfs Hit Enter. It will ask about the CachyOS BTRFS preset. Type y. It will ask to mount additional partitions. Type y. When it asks for the mount point for the additional partition (the EFI one), type skip. Once you see the prompt change to [root@cachyos /]#, you are ready for the Minecraft theme. 2. Is it "bad" to switch to GRUB? No, it’s not bad. It’s just a different tool for the same job. Systemd-boot (what you had) is like a minimalist, text-only launcher. GRUB (what we're installing) is like a full-blown "Game Launcher" that supports themes like Minecraft. It's the standard for dual-booting. 3. The Minecraft Theme Setup Run these commands one by one inside that root prompt: A. Install the GRUB software: pacman -S grub os-prober B. Force your motherboard to recognize GRUB: grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB C. Download and Install the Theme: git clone https://github.com/Lxtharia/minegrub-world-sel-theme.git cd minegrub-world-sel-theme cp -ruv ./minegrub-world-selection /boot/grub/themes/ D. Activate everything: Type micro /etc/default/grub. Scroll to the bottom and add: GRUB_DISABLE_OS_PROBER=false GRUB_THEME="/boot/grub/themes/minegrub-world-selection/theme.txt" (Save with Ctrl+S, Exit with Ctrl+Q) E. Final Update (This finds your Linux and Windows "Worlds"): grub-mkconfig -o /boot/grub/grub.cfg Once that finishes, type exit, reboot, and check your BIOS. Does "GRUB" show up at the top now?
