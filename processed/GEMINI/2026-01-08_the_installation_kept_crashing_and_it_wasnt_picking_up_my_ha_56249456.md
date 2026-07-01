---
category: homelab
date: 2026-01-08
id: 418898
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is experiencing crashes during Linux Mint installation and the installer
  is not detecting his hard drive for partitioning.
tags:
- linux-mint
- installation-failure
- hard-drive-detection
- partitioning
---
# the installation kept crashing and it wasnt picking up my hard drive when it asks for the partition i wish to install? 

### USER
the installation kept crashing and it wasnt picking up my hard drive when it asks for the partition i wish to install? 

### GEMINI
This is the classic "invisible drive" wall. If the installer is crashing and the partition list is empty, it means the Linux kernel literally cannot communicate with your storage controller. This isn't a Linux Mint "bug"—it’s a hardware configuration lock-out. Here is how you break through it. 1. The "Intel RST" Trap (Most Likely) Most modern laptops (especially Dell, HP, and Acer) come with SATA mode set to Intel RST (Rapid Storage Technology) or RAID. Linux cannot see drives in this mode; it requires AHCI. The Fix: Enter your BIOS/UEFI settings. Look for SATA Mode, Storage Configuration, or VMD Controller. If it says "RST" or "RAID," change it to AHCI. Note: If you are dual-booting with Windows, changing this will make Windows unbootable until you perform a specific "Safe Mode" registry fix. If you are wiping the drive anyway, just flip it to AHCI and proceed. Pro Tip for Acer/HP: Some BIOS menus hide these settings. Try pressing Ctrl + S while in the Main tab of the BIOS to reveal hidden storage options. 2. Manual Partition Kickstart If the BIOS is already in AHCI but the drive is still missing, the drive's existing partition table might be "dirty" or corrupted in a way the installer doesn't like. While in the Linux Mint Live desktop (the "try" mode), open the application menu and search for GParted. In the top-right corner of GParted, select your hard drive (usually /dev/sda or /dev/nvme0n1). If the drive shows up here but not in the installer: Go to Device -> Create Partition Table. Select gpt (for modern laptops) and click Apply. (WARNING: This wipes the drive completely). Once the drive shows as "Unallocated," close GParted and restart the installer. 3. Why it’s Crashing The installer crashes because it’s trying to write to a "null" location. It’s essentially reaching into a dark room for a door handle that isn't there. Once the hard drive is visible, the crashes will stop. 4. The "Intel Optane" Issue If your laptop has Intel Optane memory, it acts as a cache that locks the drive. You must disable Optane in the BIOS (or in Windows before you wipe it) for Linux to gain direct access to the SSD. Your Prioritized Plan: Check BIOS SATA Mode: Ensure it is AHCI, not RST/RAID. Disable VMD: If you see an "Intel VMD" setting, disable it. Run GParted: See if the drive appears there. If it does, create a new GPT partition table. Relaunch Installer: Do not connect to the internet during the install process (this prevents certain driver-download crashes). Which laptop model are you using? If I know the model, I can tell you exactly where the hidden storage settings are located.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
