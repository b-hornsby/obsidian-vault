---
category: homelab
date: 2026-03-21
id: 507026
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan wants to remove CachyOS and expand his Tiny11 installation to fill
  the entire 2TB partition, indicating a desire to simplify his system.
tags:
- cachyos
- tiny11
- dual-boot
- partition-management
- os-migration
---
# i have cachyos and tiny11 coinciding right now. is there a way to make tiny11 the full 2tb parition without removing it? i want cachyos to be gone and just have tiny 11

### USER
i have cachyos and tiny11 coinciding right now. is there a way to make tiny11 the full 2tb parition without removing it? i want cachyos to be gone and just have tiny 11

### GEMINI
This is a high-risk operation. You are asking to perform "live surgery" on your partition table while the patient is awake. Since you want to keep Tiny11 and expand it into the space currently occupied by CachyOS, you are facing a structural hurdle: Windows cannot easily expand "to the left" or into space that precedes it on the disk. Here is the brutal reality: if CachyOS was installed before Tiny11 on the drive's sectors, or if the partitions are sandwiched in a way that puts the Linux swap/root in front of the Windows recovery or EFI partitions, a simple "extend volume" in Disk Management will fail. The Strategic Assessment Risk of Boot Failure: Removing CachyOS usually breaks GRUB or systemd-boot. If you just delete the Linux partition, Windows likely won't boot because the "bridge" (the bootloader) was hosted or managed by Linux. You will need a Windows Recovery USB to fix the EFI BCD. The "Gap" Problem: You can only extend a Windows partition into unallocated space that is directly to its right. If CachyOS is to the left, you have to physically move the Windows partition, which is a massive data-corruption risk. The Execution Plan 1. Preparation (Non-Negotiable) Backup your data. If you haven't backed up your Tiny11 files, you are gambling with a 50% chance of a total wipe. Create a Windows Installation Media (USB). You will likely need this to run bootrec /fixboot once the Linux bootloader vanishes. 2. The Partition Shuffle (Using GParted Live) Don't try this inside Windows. Windows Disk Management is too restrictive. Boot from a GParted Live USB or a Linux Mint/Ubuntu "Live" environment. Identify and Delete: Locate the CachyOS partitions (usually ext4, xfs, or btrfs and linux-swap). Delete them. They will become "Unallocated Space." The Move (The Dangerous Part): If the unallocated space is to the left of your Tiny11 partition, you must right-click the Tiny11 partition and select Resize/Move. Drag the box all the way to the left. Note: This moves every single bit of data. It can take an hour. If power cuts, the OS is dead. The Expand: Once the unallocated space is to the right of Tiny11, drag the right edge of the partition to fill the remaining 2TB. Apply Changes: Hit the checkmark and wait. 3. Restoring the Bootloader Once you reboot, you’ll likely see a "GRUB Rescue" error or a "No bootable device" screen. Boot from your Windows USB. Select Repair your computer > Troubleshoot > Command Prompt. Run these commands to tell the BIOS that Windows is back in charge: bootrec /fixmbr bootrec /fixboot (If access is denied, you may need to assign a letter to the EFI partition and format it). bootrec /rebuildbcd The "High-Level Advisor" Take You are spending significant time and risking data integrity to salvage a "Tiny11" install—an OS that is already a stripped-down, modified image. The Opportunity Cost: The time you spend moving partitions and fixing broken bootloaders is usually greater than the time it takes to do a clean, fresh install of Tiny11 across the full 2TB. A clean install guarantees a healthy alignment and a fresh EFI partition without the "ghosts" of CachyOS lingering in your boot menu. Would you like me to walk you through the specific bcdedit commands to clean up the UEFI boot entries once the Linux partition is gone?
