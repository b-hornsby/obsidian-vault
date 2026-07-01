---
category: homelab
date: 2026-03-15
id: 236812
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking whether to boot into CachyOS using the normal boot option
  or the Grub2 option, likely in a dual-boot setup.
tags:
- linux
- cachyos
- bootloader
- grub
- dual-boot
---
# Do I boot into cachy in normal or grub2

### USER
Do I boot into cachy in normal or grub2

### GEMINI
When you select the CachyOS ISO from the Ventoy menu, choose GRUB2 mode. Why GRUB2? Modern Compatibility: Since you are on a 12700K (Intel 12th Gen), you are definitely running a UEFI system. Ventoy's "Normal" mode sometimes uses a generic boot loader that can hang on modern hardware. Kernel Handshake: GRUB2 mode provides a more reliable "handshake" between Ventoy and the CachyOS kernel, ensuring your hardware (like your NVMe and RTX 3070) is correctly recognized during the Live session. Your Checklist Once You're In: Don't Install Yet: Remember, you're just there to use the tools (GParted). Open GParted: Find it in the application menu. The Shrink: * Right-click nvme0n1p2. Shrink it to leave 300GB to 500GB of "Unallocated Space" at the end of the drive (right side). Click the Checkmark (Apply): This is the only way the changes actually happen. The "Mirror" Warning: Resizing a partition is a mechanical process for the drive. Do not interrupt it. If it looks like it's "stuck" at 99%, leave it alone. It’s moving blocks of data to ensure your CachyOS install doesn't break. Let me know once GParted shows that gray "Unallocated" block at the end of your NVMe. Ready?
