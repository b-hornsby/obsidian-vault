---
category: homelab
date: 2026-03-15
id: 254443
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is seeking confirmation on whether he needs to install Tiny11 on a
  separate drive or if he can use his existing 2TB drive for both operating systems.
tags:
- dual-boot
- tiny11
- os-installation
- storage-partitioning
---
# so you're saying its no need to install tiny11 on the separate drive and just use the 2tb to hold both os?

### USER
so you're saying its no need to install tiny11 on the separate drive and just use the 2tb to hold both os?

### GEMINI
Exactly. You are holding onto that 120GB drive like a security blanket, but it’s actually a performance anchor. Here is the brutal truth: You have a high-end i7-12700K and an RTX 3070. Running a modern OS and kernel-level anti-cheat games off a bottom-tier SATA SSD while your NVMe sits there half-used is a massive waste of your hardware's potential. Why the "Single Drive" strategy is superior: The Latency Gap: NVMe (Gen4, which your 12700K supports) is roughly 10x to 25x faster than a SATA SSD. Valorant and Fortnite constanty stream assets and security checks. On a SATA drive, you’re asking for micro-stutters that your GPU can't fix. The "Clean" ESP: Since you’re on CachyOS, you’re likely using systemd-boot or rEFInd. These are modern UEFI boot managers. They don't "fight" like the old MBR days. They simply look for a .efi file. When you install Windows on a partition of your 2TB drive, it adds its own folder to the EFI partition. Your Linux bootloader will see it and give you a menu. It's clean, digital, and intended by design. The 120GB Bottleneck: 120GB is the "danger zone" for Windows 11. Between the OS, the page file (for your 32GB RAM), and the shader caches for those games, you will be at 90% capacity instantly. SSDs slow down to a crawl when they are that full. The Strategic Blueprint If you want to do this like a pro and stop "playing small" with spare parts: Backup your CachyOS dots: Just in case. Shrink the 2TB Partition: Use gparted from a Live USB. Carve out 300GB-500GB of "Unallocated Space." Install Tiny11 to that Space: It will see the unallocated space on the NVMe and install there. Update CachyOS: Boot back into Linux, run sudo bootctl update (if using systemd-boot), and you’re done. One drive, maximum speed, zero cable clutter. The "Opportunity Cost" of the 120GB Drive Every minute you spend troubleshooting why your games are stuttering on that SanDisk or why Windows can't "see" the game files on the other drive is a minute you aren't actually playing or coding. Use the 120GB drive as a dedicated Linux Timeshift backup location instead. That gives it actual value. Are you ready to commit to the 2TB partition shrink, or do you need me to walk you through the risks of resizing a live CachyOS partition?
