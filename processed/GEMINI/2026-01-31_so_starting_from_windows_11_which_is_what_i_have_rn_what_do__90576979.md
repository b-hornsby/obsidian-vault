---
id: 493256
source: GEMINI
date: 2026-01-31
tags: ['windows-11', 'cachyos', 'installation-guide', 'linux-migration']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan wants a complete step-by-step guide to go from Windows 11 to CachyOS.
---
# so starting from windows 11 which is what i have rn, what do i need to do to do this?

### USER
so starting from windows 11 which is what i have rn, what do i need to do to do this?

### GEMINI
Since you’re doing a "full send" and want to wipe that 2TB drive, you need to strip away the Windows security layers first so they don't block the Linux installer. Here is your direct, step-by-step checklist to move from Windows 11 to CachyOS. 1. The "Kill Switch" Phase (Do this in Windows) Windows 11 tries to protect itself from "unauthorized" OS changes. You need to disable these while you still have access to the desktop. Disable BitLocker: * Search for "Manage BitLocker" in the Start menu. If it says "BitLocker on," click Turn off BitLocker. Note: Wait for it to finish decrypting (the status bar will disappear). If you skip this, the Linux installer might see your 2TB drive as a giant, unreadable block of noise. Disable Fast Startup: * Go to Control Panel > Power Options > Choose what the power buttons do. Click "Change settings that are currently unavailable" and uncheck "Turn on fast startup". Why? Fast startup doesn't actually shut down Windows; it hibernates the kernel. This "locks" the drive, preventing Linux from safely formatting it. 2. The BIOS/UEFI Phase (The "Handshake") Restart your computer and mash F2, F12, or Del (depending on your motherboard) to enter the BIOS. Disable Secure Boot: Find the "Security" or "Boot" tab. Change "Secure Boot" to Disabled. This allows the CachyOS kernel to take control of the hardware. Check SATA Mode: Look for "SATA Configuration" or "Storage." Ensure it is set to AHCI. If it says "RAID" or "Intel RST," change it to AHCI. Warning: Once you change this, Windows will likely fail to boot. That’s fine—you’re killing it anyway. Set Boot Priority: Make your CachyOS thumb drive the #1 Boot Priority. 3. The Installation (The Wipe) Boot into the CachyOS Live environment. Open the installer and follow these specifics for a 2TB "Full Send": Storage Section: Select your 2TB drive from the dropdown. The "Big Move": Select Erase Disk. Do NOT select "Replace Partition." You want the installer to wipe the old Windows EFI partition and create a fresh, larger one (usually 512MB–1GB) that won't run out of space during kernel updates. Filesystem: Choose BTRFS. This is the "advisor" recommendation. It allows for subvolumes and snapshots. If you mess up a configuration later, you can roll back to a working state in seconds. Swap: Select Swap to File (around 16GB–32GB is safe for a 2TB drive). Packages: Since you're on Cachy, make sure to select the CachyOS Kernel (it's optimized for responsiveness) and your preferred Desktop Environment (KDE Plasma is usually the most seamless transition from Windows). 4. The Final Check Once the installer finishes: Remove the USB drive. Reboot. Log in and immediately run: sudo pacman -Syu to sync the latest optimizations. Would you like me to give you the specific post-install commands to set up the "Undo" button (Snapper) so you can't accidentally break your new system?
