---
category: coding
date: 2026-03-15
id: 600320
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is encountering a 'Permission denied' error when trying to access the
  GRUB configuration file, preventing him from making changes.
tags:
- grub-configuration
- permission-denied
- linux-commands
- troubleshooting
---
# ❯ grep "menuentry" /boot/grub/grub.cfg
grep: /boot/grub/grub.cfg: Permission denied

~
❯ 

### USER
❯ grep "menuentry" /boot/grub/grub.cfg
grep: /boot/grub/grub.cfg: Permission denied

~
❯ 

### GEMINI
Ah, the classic "I'm not a superuser" block. In Linux, even reading certain system files requires permission. Run it with sudo: sudo grep "menuentry" /boot/grub/grub.cfg What to check for: You want to see a line that says menuentry 'Tiny11'. If you see that, your script successfully performed the swap after the file was generated. If it worked, you are officially finished. The names are set, the "under-text" is fixed, and your custom script will keep it that way even after system updates. Go ahead and reboot—does it look exactly how you wanted it?
