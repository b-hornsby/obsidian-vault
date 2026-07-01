---
category: homelab
date: 2026-01-17
id: 897468
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was trying to reformat a 128GB USB drive back to full capacity after
  using it to flash Linux Mint.
tags:
- usb-drive-recovery
- partition-fix
- 128gb-usb
- linux-mint-flash
---
# so I had a 128 GB USB like a thumb drive and Basically, I went to go use it to flash a laptop to the Linux Mint. and now I'm trying to reformat the drive so that way it's back to being the normal full 128 GB and it's not like partition in a weird way. So can you walk me through how to how to fix that?

### USER
so I had a 128 GB USB like a thumb drive and Basically, I went to go use it to flash a laptop to the Linux Mint. and now I'm trying to reformat the drive so that way it's back to being the normal full 128 GB and it's not like partition in a weird way. So can you walk me through how to how to fix that?

### GEMINI
When you flash a Linux ISO to a USB drive, the software (like BalenaEtcher or Rufus) writes a raw image that essentially "tricks" the computer into seeing the drive as having the size and file system of the Linux installer—not the actual 128 GB hardware. Standard formatting tools often fail here because they only look at the visible partition, not the raw drive. To fix this, you need to "clean" the drive’s partition table. Here is the direct, no-fluff way to do it on Windows and macOS. On Windows (using Diskpart) This is the most reliable method. Be careful: Selecting the wrong disk will erase it instantly. Open Command Prompt as Admin: Press the Windows key, type cmd, right-click it, and select Run as Administrator. Start Diskpart: Type diskpart and hit Enter. Identify your drive: Type list disk. Look for the disk number that matches your 128 GB drive (it will likely show up as ~115–119 GB). Example: If your USB is Disk 2, remember "2". Select the drive: Type select disk X (Replace X with your USB's number). Wipe the drive: Type clean. This nukes the Linux partition table entirely. Create a new partition: Type create partition primary. Format it: Type format fs=exfat quick. (Use exfat for 128 GB drives; fat32 has a 32 GB limit on Windows). Finish up: Type assign to give it a drive letter, then exit. On macOS (using Disk Utility) Macs often struggle with Linux-flashed drives unless you change the "View" settings. Open Disk Utility: (Cmd + Space, type "Disk Utility"). Change View: Click the View button in the top left and select Show All Devices. This is the most common "blind spot"—if you don't do this, you're only seeing the small Linux partition, not the 128 GB physical drive. Select the Physical Drive: Click on the top-level name of your USB drive (e.g., "SanDisk Ultra Media"), not the indented partition below it. Erase: Click the Erase button at the top. Settings: Name: Anything you want. Format: ExFAT. Scheme: GUID Partition Map. Confirm: Click Erase. Why you likely failed before You were probably trying to right-click the drive in your file explorer and hit "Format." That only tries to format the existing partition (the 2 GB Linux installer). By using diskpart or "Show All Devices" on a Mac, you are reaching past the software "lie" and talking directly to the hardware. Next Step: Are you seeing any "Access Denied" errors while running these commands, or did the clean command finish successfully? How to Restore USB Drive Back To Original Full Capacity This video provides a visual walkthrough of the Diskpart process for Windows users who prefer seeing the steps in real-time.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/tech/homelab|Homelab]]
