---
category: coding
date: 2026-03-15
id: 900021
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/coding.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is clarifying his dual-boot setup and asking about the optimal location
  for installing games like Fortnite and Valorant, considering Tiny11 and CachyOS.
tags:
- dual-boot-setup
- game-installation
- disk-partitioning
- tiny11
- cachyos
---
# i think you misunderstand tho. the games (fort, valo) would be on the nvme. the only thing i was curious about is whether i should put tiny11 on the sandisk 120gb to keep the two separate and if it was even possible to put those two games on the nvme drive even if all my other games are installed via cachyos on that nvme

### USER
i think you misunderstand tho. the games (fort, valo) would be on the nvme. the only thing i was curious about is whether i should put tiny11 on the sandisk 120gb to keep the two separate and if it was even possible to put those two games on the nvme drive even if all my other games are installed via cachyos on that nvme

### GEMINI
I understand exactly what you're proposing: Drive A (120GB) holds the Windows OS, and Drive B (2TB) holds your existing Linux setup plus the specific Windows game installs for Fortnite and Valorant. Here is the strategic breakdown of why that "isolation" is a technical illusion that will likely lead to a broken setup. 1. The File System Wall This is the biggest hurdle. Your 2TB drive is formatted for Linux (likely Ext4 or Btrfs). Windows cannot see these. If you boot into Tiny11 on the 120GB drive and try to install Fortnite to the 2TB drive, Windows will tell you the drive is "uninitialized" or "raw." It won't let you touch it without formatting it. The Shared Partition Fix: To make this work, you would have to shrink your CachyOS partition to create a "Third State" partition (formatted as NTFS) on that same 2TB drive. The Stutter Risk: Now you have the Windows OS on a slow SATA bus (the 120GB SanDisk) trying to pull high-bandwidth game assets from an NVMe partition through an NTFS driver. This cross-talk often causes the micro-stutters that get you killed in Valorant. 2. The Anti-Cheat Trap (Vanguard) Valorant's Vanguard is the most aggressive anti-cheat in the world. Kernel Isolation: It doesn't just sit in the game folder; it integrates into the Windows boot process. The "Modified OS" Flag: Tiny11 is a "gutted" version of Windows. While it often works, Vanguard frequently flags stripped-down ISOs because they lack the specific security telemetry and identity certificates it expects. If Vanguard decides your "isolated" Tiny11 environment is too irregular, it will simply refuse to launch the game. 3. The Bootloader Reality Installing Windows on a separate drive doesn't actually stop it from touching your 2TB drive's boot records unless you physically unplug the 2TB drive during the install. Windows is notorious for seeing an existing EFI partition on a secondary drive and "helping" by putting its boot files there instead of the 120GB drive. The Advisor's Verdict You are trying to be "safe" by keeping things on separate physical disks, but you are actually making the software side much more complex and prone to failure. Is it possible? Yes. You can install Tiny11 on the 120GB, create an NTFS partition on the 2TB, and point the games there. Is it smart? No. You are taking a high-performance machine and giving it a "limp" by forcing the OS onto a small, slow SATA drive. The "Pro" Way to Dual Boot in 2026: Shrink your 2TB NVMe by 300GB. Install a "Light" (but not gutted) Windows 11 on that new 300GB partition. Keep the 120GB drive as a dedicated "Scratch" or Backup disk. This keeps your OS and games on the fastest bus possible, avoids the file-system permissions nightmare of sharing an NVMe between two different OS boot drives, and ensures Vanguard doesn't have a fit. Do you want the specific gparted commands to safely shrink that CachyOS partition without losing your data?
