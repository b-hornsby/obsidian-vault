---
source: GPT
date: 2025-05-11
category: ai-tools
id: 79762668
linked_nodes: ['nodes/people/bryan.md']
---
# Fix USB Storage Issue

### USER
this is what i put in the command prompt so far: Microsoft Windows [Version 10.0.26100.3915]
(c) Microsoft Corporation. All rights reserved.

C:\Windows\System32>diskpart

Microsoft DiskPart version 10.0.26100.1150

Copyright (C) Microsoft Corporation.
On computer: DESKTOP-NG2I0P2

DISKPART> list disk

  Disk ###  Status         Size     Free     Dyn  Gpt
  -
---
-
---  -
---
-
---
-
---
-  -
---
---  -
---
---  ---  ---
  Disk 0    Online         1863 GB  2048 KB        *
  Disk 1    Online          116 GB   116 GB

DISKPART> select disk 1

Disk 1 is now the selected disk.

DISKPART> clean

DiskPart succeeded in cleaning the disk.

DISKPART> create partion primary

Microsoft DiskPart version 10.0.26100.1150

PARTITION   - Create a partition.
VOLUME      - Create a volume.
VDISK       - Creates a virtual disk file.

DISKPART> format fs=exfat quick

There is no volume selected.
Please select a volume and try again.

DISKPART>

### USER
how do i fix my usb partitioning to have its full storage again

### USER
why am i seeing one called UEFI_NTFS under my removable usb?

### ASSISTANT
You're *almost* there—just a small typo and a missing step caused the error.

### Here's what happened:
1. You successfully **cleaned** the USB (✅).
2. You tried to run `create partion primary` — but there's a typo: it should be `partition` not `partion` ❌.
3. Then you tried to format, but no volume existed yet because the partition wasn't created properly.

### 🪟 **Windows**
#### Using Disk Management:
1. Press `Win + R`, type `diskmgmt.msc`, and press Enter.
2. Find your USB drive (be **very sure** it's the right one).
3. Right-click on **all partitions** on the USB drive and choose **Delete Volume** until it's all unallocated space.
4. Right-click the unallocated space and select **New Simple Volume**.
5. Follow the wizard, format as **FAT32** or **exFAT** (recommended for compatibility).
6. Finish. Your full capacity should now be available.

#### OR Use Diskpart (Advanced CLI method):
1. Open **Command Prompt** as Administrator.
2. Type:
   ```
   diskpart
   list disk
   select disk #  ← (replace # with your USB disk number)
   clean
   create partition primary
   format fs=exfat quick
   assign
   exit
   ```
3. Done.

### 🐧 **Linux**
Use `gparted` or terminal:

#### Using terminal:
```bash
sudo fdisk /dev/sdX  # Replace X with your USB's letter (e.g., sdb)
```
Then:
- Press `d` to delete existing partitions (repeat if needed)
- Press `n` to create a new primary partition
- Press `w` to write and exit

Then format:
```bash
sudo mkfs.vfat -F 32 /dev/sdX1  # Or use mkfs.exfat if preferred
```

### 🔍 **What is `UEFI_NTFS`?**

- It's a **small partition** (usually ~1MB–10MB) formatted as **FAT32**.
- It contains a **UEFI bootloader** that enables systems to boot from the **main NTFS partition** (which normally UEFI systems can't do directly).
- Without it, your bootable USB may not boot properly in UEFI-only environments.

### ✅ **How to remove it and get full storage back**

You just need to **clean** the entire USB and create a new partition:

#### 🪟 **Windows DiskPart Method (Full Reset)**:
1. Open **Command Prompt as Administrator**.
2. Type the following:
   ```bash
   diskpart
   list disk
   select disk #       ← Replace # with your USB drive number
   clean               ← This erases all partitions including UEFI_NTFS
   create partition primary
   format fs=exfat quick
   assign
   exit
   ```
3. This gives you one full-size partition with no weird leftovers.
---
## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]