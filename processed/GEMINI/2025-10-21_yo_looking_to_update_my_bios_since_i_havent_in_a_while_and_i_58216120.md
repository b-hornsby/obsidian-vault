---
category: homelab
date: 2025-10-21
id: 537582
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was seeking help with updating his BIOS and wanted to share his system
  info for guidance.
tags:
- bios-update
- motherboard-maintenance
- system-info
---
# yo looking to update my bios since i haven't in a while and i need help. my sys info looks like this

### USER
yo looking to update my bios since i haven't in a while and i need help. my sys info looks like this

### GEMINI
That's great you're looking to update your BIOS! Based on your system information, you have an ASUS PRIME Z690-P WIFI motherboard with the BIOS Version/Date of 1620 from 8/16/2022. Updating your BIOS can improve stability, compatibility, and sometimes add support for newer hardware. Your motherboard manufacturer is ASUS, and the recommended method for an ASUS board is usually to use the built-in ASUS EZ Flash 3 Utility in the BIOS. Steps for Updating Your ASUS BIOS Identify the Latest BIOS Version: Visit the official ASUS support page for the PRIME Z690-P WIFI motherboard. Go to the Drivers and Tools or Support section and look for BIOS & FIRMWARE. Your current BIOS version is 1620. Check the list for the latest official BIOS version. For example, the search results show versions up to 3601 (as of the search data). Always download the one labeled as the latest stable (non-beta, unless you have a specific reason for a beta) version. Download the BIOS File: Download the latest BIOS file for your specific model: PRIME Z690-P WIFI. If you have the DDR4 version, make sure it's the PRIME Z690-P WIFI D4 file. Your system information shows DDR5-based memory, but double-check your physical memory sticks to be sure, although Z690 boards typically support one type. Unzip the downloaded file. There may be a utility to rename the file. Read any instructions included with the download (like a README file). Prepare the USB Drive: You'll need a USB flash drive (preferably 1GB or larger) that is formatted to FAT32. Copy the unzipped BIOS file (often with a .CAP extension) to the root directory of the USB drive (not inside any folder). Update the BIOS (EZ Flash 3): Restart your computer and repeatedly press the Delete key or F2 key to enter the BIOS setup. Once in the BIOS, switch to Advanced Mode (often by pressing F7). Navigate to the Tool tab and select the ASUS EZ Flash 3 Utility. Select the BIOS file you copied to the USB drive. Confirm the update and let the process run. DO NOT interrupt the process or turn off the power during the update. Reboot and Re-configure: The system will reboot automatically once the flash is complete. You may need to enter the BIOS again to load optimized defaults and re-configure any custom settings you had (like XMP for your memory, boot order, etc.). This tutorial walks through the EZ Flash 3 process for an ASUS Z690-P WIFI D4 motherboard. ASUS Motherboard BIOS Update Tutorial | ASUS PRIME Z690-P WIFI D4


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
