---
category: homelab
date: 2025-07-14
id: 244734
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is having trouble extending a volume in MiniTool Partition Wizard,
  as the slider is limited, suggesting a constraint preventing him from allocating
  more space.
tags:
- disk-partitioning
- mintool
- volume-extension
- storage-management
---
# it won't let me slide the slider any further than where the screenshot is at 

### USER
it won't let me slide the slider any further than where the screenshot is at 

### GEMINI
I see the problem. If MiniTool Partition Wizard isn't letting you slide the bar further than 2048 GB, even though you have 3726 GB unallocated, it almost certainly means your 4TB drive is currently using the Master Boot Record (MBR) partition style. MBR has a limitation where it cannot address more than 2TB (roughly 2048 GB) of disk space. To use the full capacity of your 4TB drive, you need to convert it to the GUID Partition Table (GPT) partition style. Warning: Converting from MBR to GPT will erase all data on the drive. Since your drive is already entirely unallocated, this won't cause any new data loss, but it's important to be aware of the process. Here's how to convert your Disk 2 (the 4TB external drive) from MBR to GPT using MiniTool Partition Wizard and then format it: 🛠️ Convert Disk to GPT and Create New Partition Select Disk 2 in MiniTool Partition Wizard: In the main MiniTool Partition Wizard window, click on "Disk 2" itself (the entire disk entry, not just the unallocated space). Make sure the grey bar for Disk 2 is highlighted. You'll see "MBR" listed under "Disk 2" indicating its current partition style. Convert MBR to GPT Disk: On the left sidebar, under "Convert Disk," click on "Convert MBR Disk to GPT Disk." Confirm the Conversion: MiniTool Partition Wizard will likely show a warning that this operation will be applied. Click "OK" or "Yes" to confirm. This action is now pending. Apply the Pending Conversion: Click the "Apply" button in the bottom-left corner of the MiniTool Partition Wizard window (the blue checkmark icon). Confirm the operation by clicking "Yes" when prompted. The conversion will take a moment. MiniTool Partition Wizard will change the partition style of Disk 2 to GPT. After this, Disk 2 should still show as fully "Unallocated." Create New Partition (Now with Full Capacity): Once the conversion is complete, right-click on the entire large "Unallocated" space for Disk 2. Select "Create." In the "Create New Partition" window: Partition Label: Type a name like "My 4TB Drive." Create As: Select "Primary." Drive Letter: Choose a drive letter. File System: Choose NTFS (for Windows) or exFAT (for Windows & Mac). Cluster Size: Leave as "Default." Size And Location: Now, drag the slider all the way to the right. It should now allow you to select the full 3726.0 GB. Click "OK." Apply the Final Changes: Click the "Apply" button in the bottom-left corner again to execute the partition creation. Confirm with "Yes." After these steps, your 4TB external hard drive will be converted to GPT and formatted as a single, full-capacity partition, finally allowing you to use all its storage!
