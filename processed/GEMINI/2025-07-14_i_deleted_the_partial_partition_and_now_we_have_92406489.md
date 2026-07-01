---
category: homelab
date: 2025-07-14
id: 027686
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan deleted a partition and is now facing a new issue, likely related to
  disk space or partition management.
tags:
- disk-partitioning
- data-recovery
- mintool
- storage-management
---
# i deleted the partial partition and now we have: 

### USER
i deleted the partial partition and now we have: 

### GEMINI
Okay, that's excellent news! Your latest screenshot of MiniTool Partition Wizard (image_e8d7b9.png) shows that Disk 2 (your 3.64 TB external drive) is now entirely "Unallocated" space (3726.0 GB). This is exactly what we wanted to achieve! Now that the entire drive is unallocated, creating a single partition is straightforward. Here's how to proceed in MiniTool Partition Wizard to format it to its full 4TB capacity: Select the Unallocated Space: In MiniTool Partition Wizard, under "Disk 2," click on the large "Unallocated" space (the gray bar that says "3726.0 GB"). It should highlight. Create a New Partition: On the left sidebar, under "Partition Management," click on "Create Partition." Configure the New Partition: A "Create New Partition" window will pop up. Partition Label: Type a name for your drive, e.g., "My 4TB Drive" or "External Drive." File System: NTFS: Choose this if you'll primarily use the drive with Windows computers. exFAT: Choose this if you plan to use the drive with both Windows and macOS computers. Drive Letter: Assign a drive letter (it will usually pick the next available one automatically). Cluster Size: Leave this as "Default." Size and Location: Make sure the slider is dragged all the way to the right to use the full available 3726.0 GB. The "Partition Size" should reflect this maximum. Create As: Select "Primary". This is generally the best choice for a single data partition. Click "OK." Apply the Changes: Back in the main MiniTool Partition Wizard window, you'll see a pending operation for creating the new partition. To execute this, click the "Apply" button located in the bottom-left corner (it's the blue checkmark icon). A confirmation dialog will appear. Click "Yes" to proceed. MiniTool Partition Wizard will now format the entire 4TB drive as a single partition. This process may take a few moments. Once it's complete, you should be able to see and use your 4TB external drive at its full capacity in File Explorer and Windows Disk Management.
