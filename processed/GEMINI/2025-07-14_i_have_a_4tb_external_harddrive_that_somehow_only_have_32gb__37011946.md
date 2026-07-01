---
category: homelab
date: 2025-07-14
id: 581152
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan's 4TB external hard drive is only showing 32GB of capacity, and he's
  asking how to restore it to its original size, likely through formatting.
tags:
- external-harddrive
- disk-formatting
- storage-capacity
- data-recovery
---
# i have a 4tb external harddrive that somehow only have 32gb somehow? how do i format it back to its original size?

### USER
i have a 4tb external harddrive that somehow only have 32gb somehow? how do i format it back to its original size?

### GEMINI
That's definitely a common and fixable issue! Your 4TB external hard drive is likely showing 32GB because it's been formatted with a small partition, possibly for a bootable drive, a recovery partition, or an operating system installer. To get it back to its original 4TB size, you'll need to delete the existing partitions and create a new, single partition that uses the entire drive. Here's how you can typically do it on Windows and macOS: 🖥️ On Windows (Disk Management) Open Disk Management: Press Windows Key + X and select "Disk Management." (You can also search for "Disk Management" in the Start menu.) Locate Your External Drive: In the Disk Management window, you'll see a list of all your drives. Look for your 4TB external drive. It will likely show the 32GB partition and a large amount of "Unallocated" space. Be very careful to identify the correct drive to avoid accidentally formatting the wrong one! It's usually listed as "Disk 1," "Disk 2," etc., and you can often tell by its size and the small partition. Delete the Existing Partition(s): Right-click on the 32GB partition (or any other small partitions you see on that drive). Select "Delete Volume..." Confirm the deletion when prompted. This will turn the 32GB partition into "Unallocated" space. If there are other small partitions on the drive, delete those as well until the entire drive shows as "Unallocated" space. Create a New Simple Volume: Once the entire drive is "Unallocated," right-click on the "Unallocated" space for your external drive. Select "New Simple Volume..." The New Simple Volume Wizard will open. Click "Next." For "Specify Volume Size," leave the default maximum size (which should be the full capacity of your drive) and click "Next." Assign a drive letter if you wish, then click "Next." For "Format Partition," choose your preferred file system: NTFS: Recommended for Windows users. Supports large files and drives. exFAT: Good for cross-platform compatibility (Windows and macOS) and supports large files. You can leave the "Allocation unit size" as default. Give your drive a "Volume label" (e.g., "My External Drive"). Check "Perform a quick format." Click "Next," then "Finish." Your drive should now be formatted to its full 4TB capacity. 🍎 On macOS (Disk Utility) Open Disk Utility: Go to Applications > Utilities > Disk Utility. Select Your External Drive: In the Disk Utility sidebar, under "External," select your 4TB external drive itself (not just the 32GB volume listed under it). Make sure you select the entire physical drive. Erase the Drive: Click the "Erase" button in the toolbar. A dialog box will appear. You'll need to configure the following: Name: Give your drive a new name (e.g., "My 4TB Drive"). Format: Choose a suitable file system: APFS: The default for newer macOS versions. Excellent for macOS use. Mac OS Extended (Journaled): (HFS+) Older macOS format, still widely compatible. ExFAT: Best choice if you plan to use the drive with both macOS and Windows. Scheme: Select "GUID Partition Map" (essential for full drive recognition and modern boot compatibility). Click "Erase" again to confirm. Disk Utility will then erase and reformat the drive to its full capacity. ⚠️ Important Considerations Data Loss: This process will ERASE ALL DATA currently on the 32GB partition and the rest of the drive. Make sure you back up any important files before proceeding! Correct Drive: Double-check that you are selecting the correct external hard drive. Formatting the wrong drive could lead to data loss on your system or other storage devices. MBR vs. GPT: If your drive was initially formatted with a Master Boot Record (MBR) partition scheme for some reason (often seen with older drives or specific utility usage) and your drive is 4TB, it needs to be GUID Partition Table (GPT) to utilize the full space beyond 2TB. Both Disk Management (Windows) and Disk Utility (macOS) usually default to GPT when creating a new partition on a large drive, but if you run into issues, this could be a reason.
