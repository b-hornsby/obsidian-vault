---
id: 611997
source: GEMINI
date: 2026-03-15
tags: ['disk-partitioning', 'unallocated-storage', 'dual-boot-prep', 'storage-management']
category: homelab
sentiment: executing
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan reported having 297.43GB of unallocated storage on a drive, likely after partitioning for a dual-boot setup.
---
# I now have 297.43gb of unallocated storage on that drive

### USER
I now have 297.43gb of unallocated storage on that drive

### GEMINI
Perfect. That is exactly what we need to see. You have successfully carved out the space without touching your nvme0n1p1 (the boot partition), which is key to keeping this clean. The "Checkmark" Moment Right now, GParted is just showing you a preview. Look at the toolbar at the top—see that Checkmark icon next to the "undo" arrow? Click the Checkmark to "Apply All Operations." Wait. Since you are moving data on a 1.8TB drive, this might take a few minutes. Do not force shut down your PC while this is running, or you'll corrupt the Btrfs filesystem. Next Phase: The Windows Occupation Once GParted finishes and says "All operations successfully completed," you are ready for Tiny11. Reboot your PC. When the Ventoy menu appears, select your Tiny11/Windows ISO. When you get to the screen that asks "Where do you want to install Windows?": You will see a list of partitions. Look for the one that says "Drive 0 Unallocated Space" with a size of roughly 297 GB. Select that space and click Next. Do not touch any other partition. Windows will take over from there, doing its usual series of reboots. Are you ready to hit that checkmark in GParted and commit to the resize?
