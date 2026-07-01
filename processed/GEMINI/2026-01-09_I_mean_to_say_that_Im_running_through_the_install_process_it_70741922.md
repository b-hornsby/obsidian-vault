---
category: homelab
date: 2026-01-09
id: 868741
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is describing a boot loop after completing the Linux Mint installation
  process.
tags:
- linux-mint
- installation-loop
- boot-problem
---
# I mean to say that I’m running through the install process, it finishes, I restart and then that happens

### USER
I mean to say that I’m running through the install process, it finishes, I restart and then that happens

### GEMINI
This loop is happening because your Lenovo is basically "forgetting" that it has a new OS on its hard drive and is looking for anything familiar to boot from—usually defaulting back to the USB or just giving up and restarting. Since the install actually finished, the data is likely on the disk. The problem is the handshake between your hardware and the Linux bootloader (GRUB). Here is the "brutally honest" fix list, prioritized by what actually works for IdeaPads: 1. The "Invisible" Boot Entry (Most Likely) Lenovo firmware often "locks" the boot list. Even though Mint installed, the BIOS hasn't refreshed to show the new "ubuntu" boot entry (Mint uses the name 'ubuntu' for its bootloader). The Fix: Shut down. Use the Novo Button (the tiny hole on the side) to enter BIOS. Go to the Boot tab. Look for "Boot Priority Order." * If you see "ubuntu" or "Linux Mint" in that list but it's at the bottom, move it to #1. Crucial: If you don't see it, look for a setting called "Boot Order Lock" or "Changes to Boot Order" and ensure it is Disabled or Unlocked. 2. Disable "Intel Platform Trust Technology" (PTT) On many IdeaPads, PTT (Intel's version of TPM) causes a "Reset System" loop immediately after the Lenovo logo. The Fix: In BIOS, go to the Security tab. Find Intel Platform Trust Technology or TPM and set it to Disabled. Save and exit. This often breaks the loop immediately. 3. The UEFI vs. Legacy Mismatch If you booted the USB in "Legacy/CSM" mode but installed it to a "UEFI" disk (or vice versa), the BIOS won't know how to trigger the start. The Reality Check: In BIOS, check the Boot Mode. If it says "Legacy," change it to UEFI. If it was already UEFI, ensure Secure Boot is Disabled. Secure Boot is the #1 reason Linux fails to "handshake" with Lenovo hardware on the first boot. 4. The "Hollow Install" (Intel RST) If your IdeaPad is newer, your hard drive might be set to RAID/RST mode. Linux Mint can sometimes "see" the drive during install but fails to write the bootloader in a way the BIOS can read. The Fix: In BIOS, change SATA Controller Mode from "Intel RST" to AHCI. Note: If you change this, you must re-install Mint. The previous install will not work after this toggle. Your Tactical Plan: Immediate: Go into BIOS, Disable Secure Boot, and Disable PTT/TPM. Save and Restart. The "F12" Test: Tap F12 (or Fn+F12) rapidly as the laptop turns on. If you see "ubuntu" or "Linux Mint" in the menu, select it manually. If it boots, your only issue is the Boot Order in BIOS. The Nuclear Option: If you do step 1 and it still loops, go back to BIOS, switch to AHCI mode, and re-install. Don't waste time troubleshooting a "ghost" installation. Which specific model of IdeaPad are you using? (The exact name like "IdeaPad 3 15IIL05" is usually on a sticker on the bottom; knowing the CPU gen helps pinpoint if the RST/AHCI issue is your specific bottleneck.)


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
