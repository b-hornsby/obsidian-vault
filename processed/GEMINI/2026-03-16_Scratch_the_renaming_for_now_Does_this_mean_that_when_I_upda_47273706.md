---
id: 785470
source: GEMINI
date: 2026-03-16
tags: ['dual-boot', 'cachyos', 'windows', 'update-safety']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan asked whether both OS installations would be safe from each other's updates in a dual-boot setup.
---
# Scratch the renaming for now. Does this mean that when I update either os, they both should be safe now?

### USER
Scratch the renaming for now. Does this mean that when I update either os, they both should be safe now?

### GEMINI
Smart move. Let's get back to the big picture—stability. The short answer is: Yes, you are in a much safer spot now than you were two hours ago. However, because you are dual-booting on a single drive, "safe" has a specific meaning. Here is how updates will work now: 1. CachyOS (Linux) Updates Is it safe? Yes. When you run your updates (sudo pacman -Syu), CachyOS might update the Linux Kernel. Since we installed GRUB and set it up correctly, the system will update its own boot files without touching Windows. The "Minegrub" Factor: If a system update ever runs grub-mkconfig automatically, your Minecraft theme will stay, but those custom names we were fighting with might reset to "Arch Linux." The menu itself won't break; it’ll just look slightly more boring. 2. Tiny11 (Windows) Updates Is it safe? Mostly. Windows is the "bad roommate." Usually, it stays in its own room (the NTFS partition). The Risk: Occasionally, a major Windows Feature Update (like moving from 24H2 to a newer build) might decide to set the Windows Boot Manager back to Priority #1 in your BIOS. The Fix: If you ever turn on your PC and it skips the Minecraft menu and goes straight to Windows, don't panic. You don't need to reinstall anything. Just go into your BIOS and move GRUB back to the top of the list. 3. The "Secure Boot" Trap If you ever see a "Secure Boot Violation" red box after an update: Windows sometimes tries to re-enable Secure Boot during updates. If this happens, just go back into BIOS and set Secure Boot to "Disabled" or "Other OS." Summary Table: What to do if... If this happens...Do this...PC boots straight to WindowsGo to BIOS -> Boot Tab -> Move GRUB to #1."Secure Boot Violation" ErrorGo to BIOS -> Secure Boot -> Set to Disabled.Minecraft Menu looks "Default"Run sudo grub-mkconfig -o /boot/grub/grub.cfg in Linux. Final Status: Stable. Your partitions are separated, your bootloader is registered to the motherboard, and your "Rescue" path (the Live USB) is something you now know how to use. You’ve successfully done the hard part of "Modern PC Gaming" on Linux. Since we're pausing the renaming, are you ready to finally boot into one of those "Worlds" and actually use the PC, or is there one last thing on your mind?
