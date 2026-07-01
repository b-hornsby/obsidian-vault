---
category: homelab
date: 2026-01-09
id: 444220
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is stuck in a boot loop after installing Linux Mint on his Lenovo IdeaPad.
tags:
- linux-mint
- lenovo-ideapad
- boot-loop
- os-installation
---
# Trying to put Linux mint on a Lenovo idea pad and when I finish the install process it tells me to unplug the thumb drive and press enter. I do and it keeps looping over and over and nothing else 

### USER
Trying to put Linux mint on a Lenovo idea pad and when I finish the install process it tells me to unplug the thumb drive and press enter. I do and it keeps looping over and over and nothing else 

### GEMINI
You are caught in a classic "re-install loop." Since you’ve already completed the installation, the fact that you’re back at the start suggests one of two things: either your BIOS/UEFI is ignoring your hard drive and prioritizing the USB port, or the bootloader (GRUB) failed to write correctly to your disk. Here is the objective breakdown of why you are stuck and how to fix it. 1. The Boot Order Sabotage Most Lenovo IdeaPads are configured with a strict boot priority. Even though you removed the drive, the system might be failing to find the "Linux Mint" or "ubuntu" entry in your UEFI, causing it to default back to a network boot or a recovery state that looks like a loop. The Fix: Shut the laptop down completely. Use a paperclip to press the Novo Button (usually a small hole on the side of the laptop with a curved arrow icon). Select BIOS Setup. The Action: Go to the Boot tab. Ensure "Boot Mode" is set to UEFI. Look at the "EFI" list. If your hard drive (SSD) isn't at the top, move it there using the F5/F6 keys. Save and Exit (F10). 2. The "Secure Boot" Conflict Lenovo firmware is notorious for blocking "unauthorized" bootloaders. If Secure Boot is enabled, it may be preventing Linux Mint from initializing the first time. The Action: In that same BIOS menu, go to the Security tab. Find Secure Boot and set it to Disabled. This removes the handshake requirement that often trips up new Linux installs on Windows-optimized hardware. 3. The "Intel RST" Blind Spot (Common Pitfall) If your IdeaPad uses a modern Intel processor, your storage controller might be set to RST (RAID) mode instead of AHCI. Linux Mint often installs successfully in RST mode but fails to actually see the drive to boot from it later. The Reality Check: If you didn't change this before installing, your installation might be "hollow"—the files are there, but the kernel can't mount the drive. The Fix: In BIOS, look for "Storage" or "SATA Mode." If it says Intel RST Premium, change it to AHCI. Warning: If you are dual-booting with Windows, changing this will break your Windows boot unless you perform a specific registry fix first. If you are wiping the drive for Linux, change it and re-install Mint. 4. The "Grub-Install" Failure If the above steps don't work, the installer failed to write the GRUB bootloader to the EFI partition. This happens if the partition table wasn't refreshed. The Action: Plug the USB back in, boot into the "Live" Mint environment, and run Boot-Repair. Connect to Wi-Fi. Open a terminal and run: sudo add-apt-repository ppa:yannubuntu/boot-repair && sudo apt update Then run: sudo apt install -y boot-repair && boot-repair Click Recommended Repair. Priority Strategy Check BIOS/UEFI: Disable Secure Boot and ensure the internal drive is the #1 priority. (90% of cases). Verify AHCI Mode: If the drive doesn't even show up in the boot list, this is your culprit. Wipe and Recalibrate: If you spent less than 20 minutes on this, don't waste time "fixing" a broken install. Change the BIOS settings first (Secure Boot OFF, AHCI ON), then re-install from scratch. It is faster than troubleshooting a corrupted GRUB. Would you like me to walk you through the specific terminal commands to verify if your hard drive is even being recognized by the OS?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
