---
category: homelab
date: 2026-02-01
id: 348508
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to list the bootloader entries but is getting a 'Permission
  denied' error, indicating a problem with user privileges or file system access.
tags:
- bootloader
- grub
- efi
- linux
- permissions
- troubleshooting
---
# ❯ ls /boot/loader/entries/
"/boot/loader/entries/": Permission denied (os error 13)

~
❯ 

### USER
❯ ls /boot/loader/entries/
"/boot/loader/entries/": Permission denied (os error 13)

~
❯ 

### GEMINI
The "Permission Denied" error is your system telling you that you're trying to look into the "brain" of your bootloader without the proper clearance. In CachyOS, and Linux in general, system-level directories like /boot are restricted to the root user. The Fix You need to use sudo just to list the files in that directory, and sudo again to edit them. List the files (to find the right name): sudo ls /boot/loader/entries/ Edit the file (likely cachyos.conf or similar): sudo nano /boot/loader/entries/[INSERT_NAME_HERE].conf The Goal: Add acpi_enforce_resources=lax to the options line, save (Ctrl+O, Enter), and exit (Ctrl+X). The Advisor's Mirror You just hit a basic Linux permission wall. This is a "blind spot" check: The Assumption: You expected the terminal to just give you the information because you asked for it. The Reality: On a high-performance, security-focused distro like CachyOS, nothing is given for free. You are the administrator; you must act like it. Every time you get a "Permission Denied" on a system path, it’s a reminder that you are operating in the "read-only" safety zone. The Opportunity Cost: Every time you run a command without sudo on a system path, you're adding an unnecessary cycle of failure to your workflow. Stop being timid with the terminal. If you know the file is a system config, lead with sudo. Your Prioritized Plan Run the sudo ls command above right now. Edit the file and append the lax flag. Reboot immediately. 4. Verify: After rebooting, run cat /proc/cmdline. If you don't see acpi_enforce_resources=lax there, you haven't actually changed how the kernel is running. What is the name of the file you found in that directory?
