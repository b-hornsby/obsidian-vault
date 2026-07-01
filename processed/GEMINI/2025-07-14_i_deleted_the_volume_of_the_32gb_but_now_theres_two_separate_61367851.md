---
category: homelab
date: 2025-07-14
id: 995140
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan deleted a volume and now has two separate partitions, indicating he's
  trying to reconfigure disk space and is encountering unexpected results.
tags:
- disk-partitioning
- data-recovery
- mintool
- storage-management
---
# i deleted the volume of the 32gb but now theres two separate partitions? 

### USER
i deleted the volume of the 32gb but now theres two separate partitions? 

### GEMINI
That's a good step! You're seeing two "Unallocated" partitions on Disk 1 because the 32GB partition you deleted was likely at the beginning or end of the drive, leaving separate unallocated spaces. To get your 4TB drive back to its full size, you need to combine these unallocated spaces and then create a new single partition. Here's how to do it: 🖥️ On Windows (Disk Management) Locate Your External Drive (Disk 1): In the Disk Management window, you've correctly identified "Disk 1" as your external drive. It now shows 2048.00 GB Unallocated and 1678.02 GB Unallocated. Create a New Simple Volume: Right-click on either of the "Unallocated" spaces on Disk 1. It doesn't matter which one you choose to start with. Select "New Simple Volume..." The New Simple Volume Wizard will open. Click "Next." For "Specify Volume Size," the wizard should automatically detect and present the maximum possible size by combining all the unallocated spaces on that drive (which will be close to 3726.02 GB, the total capacity of Disk 1). Do not change this number. Click "Next." Assign a drive letter (e.g., "E:"). Click "Next." For "Format Partition," choose your preferred file system: NTFS: Recommended for Windows users. Supports large files and drives. exFAT: Good for cross-platform compatibility (Windows and macOS) and supports large files. You can leave the "Allocation unit size" as default. Give your drive a "Volume label" (e.g., "My 4TB Drive"). Make sure "Perform a quick format" is checked. Click "Next," then "Finish." Disk Management will now format the entire combined unallocated space into a single partition, making your 4TB drive fully usable again.
