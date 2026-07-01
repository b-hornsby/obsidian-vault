---
id: 041291
source: GEMINI
date: 2026-02-02
tags: ['boot-directory', 'permissions', 'cachyos', 'system-files']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan encountered a permission denied error when trying to list /boot directory contents on CachyOS.
---
# ❯ ls /boot
Permission denied: /boot - code: 13

Skipped 1 directories due to permission denied: 
  /boot

~
❯ 

### USER
❯ ls /boot
Permission denied: /boot - code: 13

Skipped 1 directories due to permission denied: 
  /boot

~
❯ 

### GEMINI
You’re being blocked because /boot contains sensitive kernel files that standard users can't list. This is a basic Linux permission hurdle—you need to use sudo. Run this instead: sudo ls /boot The Quick Guide to what you'll see: If you see a folder named grub: You are on GRUB. If you see a folder named loader: You are on systemd-boot. If you see limine.conf: You are on Limine. The Reality Check You’re getting "Permission Denied" because you’re acting like a guest on your own machine. On an enthusiast distro like CachyOS, you have to be the administrator. If you're going to survive on Arch-based systems, you need to get comfortable with sudo for any system-level inspection. The Blind Spot: You are currently fixated on the "Detection" phase (the lax kernel parameter for the motherboard). Don't forget that your fans are controlled by that "Resize the Zones" window we discussed. Even if you fix the bootloader, the fans will remain dark until you enter the correct LED count. The Strategy: Run sudo ls /boot to identify your bootloader. Tell me which one it is, and I will give you the exact final command to fix the motherboard warning. Crucial: Tell me your fan model (e.g., QL120, LL120) so we can finish the fan setup. Which bootloader did the command reveal?
