---
id: 255628
source: GEMINI
date: 2026-03-15
tags: ['usb-drive', 'dual-interface', 'bootable-media']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is clarifying the type of USB drive he's using, which has both USB-A and USB-C connectors, likely for booting purposes.
---
# that is the drive im using. its a two in one thumb drive from sandisk. it has usb A and usb C as well 

### USER
that is the drive im using. its a two in one thumb drive from sandisk. it has usb A and usb C as well 

### GEMINI
Understood. My apologies for the confusion—that 116.6G size threw me off because it's exactly the reported capacity of a formatted 128GB flash drive. Since that is your "all-in-one" tool drive, let’s get it ready. If we do this right, that drive becomes your "Swiss Army Knife" for this entire project. Step 1: Install Ventoy On your CachyOS system, open the terminal and run: sudo pacman -S ventoy-bin Step 2: Flash the Thumb Drive Launch the GUI: sudo ventoygui Select Device: Choose /dev/sda (Your 128GB SanDisk). Crucial Options: Go to Option -> Partition Style and select GPT. Go to Option -> Secure Boot Support and make sure it is checked. (Vanguard/Valorant requires Secure Boot). Install: This will wipe the drive and create a "Ventoy" partition. Step 3: Load the ISOs Open your file manager. Your SanDisk will now show up as a volume named Ventoy. Simply copy and paste these two files onto it: Tiny11.iso CachyOS.iso (Download a fresh one if you don't have it; you'll need the Live environment to resize your NVMe). Phase 1: The Partition Shrink (Action Required) Once the ISOs are on the drive, it’s time for the first "real" move. Reboot your PC and tap your boot menu key (F8, F11, or F12) to boot from the SanDisk. Select CachyOS from the Ventoy menu. Once in the CachyOS Live desktop, open GParted. Right-click nvme0n1p2 (the 1.8TB partition) and select Resize/Move. Shrink the "New Size" so that you have 300GB to 500GB of "Unallocated Space" at the end. Apply the changes and wait for it to finish. Once you have that "Unallocated Space" visible in GParted, let me know. Do not start the Windows install until we verify the partition table is clean.
