---
id: 286526
source: GEMINI
date: 2026-03-15
tags: ['usb-drive-setup', 'bootable-media', 'system-preparation']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is agreeing to a plan but wants to prepare a thumb drive first, likely for installing an operating system or troubleshooting.
---
# yeah lets run this plan BUT lets set up the thumb drive first so i dont mess anything up 

### USER
yeah lets run this plan BUT lets set up the thumb drive first so i dont mess anything up 

### GEMINI
Smart move. Prepping the thumb drive is the "foundational" step. If the drive isn't solid, the whole dual-boot house of cards falls down. Since you're on CachyOS, you have access to their optimized repositories. We’re going to use Ventoy because it turns your USB into a storage drive where you just "drop" ISO files. This means you can keep your CachyOS ISO on there and add the Windows ISO without ever needing to re-flash it. Step 1: Install Ventoy on CachyOS Open your terminal and run: sudo pacman -S ventoy-bin Step 2: Initialize the USB Drive Plug in your USB drive. Identify the drive name: Run lsblk. Look for your USB (usually something like /dev/sdb or /dev/sdc—pay attention to the size, likely 16GB, 32GB, etc.). Do not confuse it with your 2TB NVMe (/dev/nvme0n1). Launch the Ventoy GUI: sudo ventoygui In the Ventoy window: Device: Select your USB drive. Option -> Partition Style: Set this to GPT. This is non-negotiable for a modern 12700K system and CachyOS. Option -> Secure Boot Support: Check this (Vanguard requires Secure Boot on Windows 11). Click "Install" (This will wipe the thumb drive). Step 3: Load the ISOs Once Ventoy is installed, your USB will appear in your file manager as a regular empty drive named "Ventoy." Copy/Paste your Tiny11 (or Windows) ISO directly onto that USB. Copy/Paste your CachyOS ISO onto the same USB. Note: If you don't have the CachyOS ISO anymore, download it now. You need it for the partition resizing phase. The Next Step Once both ISOs are on the drive, you're officially "safety-netted." You can boot from this one drive and choose between Windows or Linux at any time. Are both ISOs ready to go on the thumb drive, or do you need a minute to download the Tiny11/Cachy images?
