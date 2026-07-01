---
category: homelab
date: 2026-03-15
id: 372415
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/homelab.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is reporting an error message received after installing Tiny11, indicating
  a problem with the installation process.
tags:
- homelab
- tiny11
- installation-errors
---
# After the tiny11 install we got this message:

### USER
After the tiny11 install we got this message:

### GEMINI
This looks alarming, but don't panic. This is a classic "clash of egos" between the Windows installer and your motherboard's BIOS regarding the partition table. Windows tried to write its boot information, and your ASUS motherboard flagged it as "corruption" because it changed the GPT header that CachyOS originally created. The Immediate Fix Press F1 to enter your BIOS setup as the screen suggests. Check the "Boot" or "Advanced" tab: Look for a setting called "Boot Sector (MBR/GPT) Recovery Policy". Set it to "Auto Recovery" or "Manually Control". If it's on "Block" or something strict, it will keep giving you this error. Save and Exit (F10). What’s Happening Under the Hood Windows likely finished its initial file copy and is trying to reboot to finish the setup. Because we are dual-booting on a single drive, Windows modified the EFI partition. Your ASUS Prime Z690-P is just being "brutally honest" and overprotective of that partition. If it reboots and takes you back to this screen or straight into Windows: That’s actually a good sign—it means the hardware is still talking to the drive. If it boots straight to Windows, let it finish the installation. We will "rescue" the CachyOS bootloader later. If it boots to nothing or keeps hitting this error, we will use your Ventoy thumb drive to boot back into the CachyOS Live environment and repair the "GPT header" using a simple command. Go into the BIOS now and let me know if changing that Recovery Policy lets you past this screen.
