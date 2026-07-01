---
id: 183863
source: GEMINI
date: 2026-01-31
tags: ['bitlocker', 'decryption', 'windows-11', 'pre-install']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan confirmed his drive is fully decrypted via BitLocker and is asking what to do next before installing CachyOS.
---
# so i ran manage-bde -status and it says its fully decrypted. now what?

### USER
so i ran manage-bde -status and it says its fully decrypted. now what?

### GEMINI
Excellent. The software handcuffs are off. Now you move from the OS level to the hardware level. This is where most people fail because they get intimidated by the BIOS, but it's the most critical step for a "full send." 1. The BIOS Handshake Restart your computer and immediately start tapping the BIOS key (usually F2, Del, or F12—watch the screen, it usually tells you). You need to change exactly three things: Disable Secure Boot: Find the "Security" or "Boot" tab. Set Secure Boot to Disabled. Linux will boot much more reliably without it. Set SATA Mode to AHCI: Look under "Storage" or "Advanced." If it says RST or RAID, change it to AHCI. (This is non-negotiable for NVMe performance on Linux). Boot Priority: Move your USB Drive to the top of the list. Save and Exit. 2. The Point of No Return (The Installer) Once you boot into the CachyOS Live environment (the "Welcome" screen): Launch the Installer. Partitioning: This is your 2TB moment. Select "Erase Disk." * Advisor Tip: Verify it is targeting your 2TB drive and not the USB stick. The Filesystem (The "Smart" Choice): Choose BTRFS. Why? Because you’re new to this. BTRFS allows you to take "snapshots." If you break the system tomorrow, you can roll back to today's version in 10 seconds. Swap: Choose "Swap to File" and set it to 16GB or 32GB. With a 2TB drive, you have the space; don't starve your RAM. 3. The "Cachy" Specials CachyOS will ask you what you want to install. To get the most out of your hardware: Kernel: Stick with the Default CachyOS Kernel (it's heavily optimized). Desktop Environment: If you want it to feel familiar but powerful, go with KDE Plasma. Apps: Don't check everything. Keep it lean. You can always add more later with pacman or yay. 4. Opportunity Cost Check Once you hit "Install," Windows is gone. Ensure that "backup" you mentioned is physically disconnected from the computer (unplug the external drive) just so you don't accidentally wipe the backup too. It happens to the best of us. Are you in the BIOS right now? Tell me if you can't find the AHCI or Secure Boot settings—some manufacturers hide them behind "Advanced" menus (Ctrl+S or F1 on some laptops).
