---
category: homelab
date: 2026-03-15
id: 713434
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking whether to use Grub2 mode or normal mode for a system rescue
  operation, likely for CachyOS.
tags:
- linux
- cachyos
- bootloader
- grub
- system-rescue
---
# Grub2 mode or normal for rescue mission?

### USER
Grub2 mode or normal for rescue mission?

### GEMINI
Go with Normal Mode. Since we’re just running a few terminal commands to repair the bootloader, Normal Mode is the most stable and compatible way to load the Live environment. Quick Checklist once you're in the Live Desktop: Open Terminal (Konsole). sudo cachy-chroot: Make sure you pick the Btrfs partition (your 1.5TB one). sudo bootctl install: This is the command that "yells" at your BIOS to remember CachyOS exists. Once you finish those and reboot, does CachyOS finally show up in your BIOS boot list again?
