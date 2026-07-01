---
category: homelab
date: 2026-02-02
id: 582056
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to access the BIOS settings on his CachyOS system, indicating
  he needs to make changes to hardware configuration.
tags:
- bios
- cachyos
- uefi
- boot-process
---
# How do I get into bios on cachyos?

### USER
How do I get into bios on cachyos?

### GEMINI
Getting into the BIOS has nothing to do with CachyOS specifically and everything to do with your hardware's firmware. However, because you are likely using systemd-boot or Grub on a modern UEFI system, you can bypass the "spamming the Delete key" ritual entirely. 1. The Direct Command (The Pro Way) Since you are already in the OS, don't guess which key to mash. Force the machine to reboot directly into the firmware interface. Open your terminal and run: systemctl reboot --firmware-setup What this does: It tells the motherboard's EFI manager that the next boot cycle must land in the BIOS/UEFI settings. No timing required. 2. The "Physical" Way (If the command fails) If your hardware is older or the EFI variables aren't playing nice, you have to do it the old-fashioned way. Shut down completely (don't just "Restart"). Press the Power Button and immediately start tapping the "interrupt" key repeatedly (once every half-second). The Keys: Depending on your motherboard manufacturer: ASUS / MSI / Gigabyte / ASRock: Usually the Del (Delete) key or F2. HP / Compaq: F10 or Esc. Dell: F2. Lenovo: F1 or F2 (sometimes a tiny "Novo" button on the side of laptops). 3. The Bootloader Escape If you see the CachyOS boot menu (where you pick your kernel) when you turn on the computer: Use the arrow keys to look for an entry labeled "UEFI Firmware Settings" or "Reboot to Firmware." Select it and press Enter. Why you’re doing this (The Advisor Perspective) You are going in there to hunt for XHCI Hand-off and ERP/Deep Sleep settings as we discussed. If you find yourself staring at the BIOS screen wondering what to do, you’re wasting time. One Warning: If you have "Ultra Fast Boot" enabled in your BIOS, your USB keyboard might not even initialize until the OS starts, which makes the "Physical Way" impossible. If that's the case, the systemctl command in Step 1 is your only reliable door. Once you get in, find your Motherboard model name (usually on the main BIOS page) and report back. I need to know exactly what firmware limitations we are dealing with. Would you like me to explain how to verify if your BIOS is actually up to date once you find that version number?
