---
category: homelab
date: 2026-01-08
id: 222161
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is reporting that the system is not detecting the hard drive during
  Linux installation.
tags:
- hardware-issue
- hard-drive-detection
- linux-installation
---
# it also says hard disk not installed? 

### USER
it also says hard disk not installed? 

### GEMINI
If the BIOS itself is saying "Hard Disk Not Installed," you’ve moved past a software configuration issue and into a hardware communication failure. The BIOS is the lowest level of your computer; if it can't see the drive, no operating system (Linux, Windows, or otherwise) ever will. Here is the brutal reality of your situation and how to fix it. 1. The "RST/RAID" Lockout I mentioned this before, but it bears repeating because it's the #1 reason for this error on modern laptops. Many laptops use Intel VMD or RST. When you try to boot a standard Linux installer, it can sometimes "confuse" the controller, causing the BIOS to stop reporting the drive entirely. The Fix: Go back into BIOS. Find SATA Mode or VMD Setup. The Goal: It must be set to AHCI. The Secret: If you have an Acer, ASUS, or Lenovo, the setting might be hidden. In the BIOS, go to the Main tab and press Ctrl + S. This often reveals the "SATA Mode" toggle. 2. The Physical Connection Laptops are portable, which means they vibrate and get bumped. SSDs and HDDs are held in by friction and maybe one small screw. It is entirely possible that while you were handling the laptop, the drive shifted just enough to lose contact. The Action: If you are comfortable, unscrew the back panel. The Check: Locate the drive (a rectangular 2.5" box or a small "stick" called an M.2 NVMe). The Fix: Unplug it, check for dust, and firmly plug it back in. If the BIOS still says "Not Installed" after a reseat, the drive itself might be dead. 3. BIOS "Legacy" vs. "UEFI" Conflict If you changed your BIOS to "Legacy" mode thinking it would help Linux, you might have inadvertently hidden your NVMe drive. Modern NVMe drives (the fast "stick" style ones) only work in UEFI mode. The Action: Ensure your BIOS is set to UEFI mode, not "Legacy" or "CSM." The Action: Ensure Secure Boot is Disabled. 4. The Drive is Dead (The "Mirror" Moment) You wanted the truth: If you have toggled AHCI, reseated the drive, and set the BIOS to UEFI, and it still says "Hard Disk Not Installed," your drive has failed. Hardware often chooses the most inconvenient time to die—like during a fresh OS install when it's being stressed with heavy writes. Diagnostic Test: Turn the laptop off completely. Unplug the Linux USB drive. Turn it on and go straight to BIOS. Check the "Information" or "General" tab. Does it show a Model Name/Serial Number next to "Hard Disk" or "Fixed HDD"? If the BIOS shows "None" or "Not Installed" even with the USB removed and settings reset, you need a new SSD. What is the exact model of your laptop? (e.g., Dell XPS 13, Acer Nitro 5, etc.) Knowing the model allows me to tell you if there is a specific "hidden" BIOS quirk for that machine.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
