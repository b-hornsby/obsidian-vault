---
category: homelab
date: 2025-07-25
id: 112889
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan encountered an error when booting up his PC.
tags:
- pc-boot
- error-troubleshooting
- windows-11
---
# Booted up my pc and this error came up? 

### USER
Booted up my pc and this error came up? 

### GEMINI
That error message, "Reboot and Select proper Boot device or Insert Boot Media in selected Boot device and press a key," indicates that your computer is having trouble finding an operating system to load. Here's a breakdown of what might be happening and how to troubleshoot it: Common Causes: Loose or disconnected hard drive/SSD: The cable connecting your storage drive to the motherboard might have come loose. Incorrect boot order in BIOS/UEFI: Your computer might be trying to boot from a device that doesn't contain an operating system (like a USB drive or network boot) before checking your main hard drive. Corrupted operating system: The Windows (or macOS, Linux) installation on your drive might be damaged. Failing hard drive/SSD: Your storage drive itself could be failing. New drive with no OS: If you just installed a new hard drive or SSD, it won't have an operating system on it yet. External media interfering: Sometimes, if you have a USB drive, CD, or DVD plugged in, the computer might try to boot from it first, even if it's not bootable. Troubleshooting Steps (Try these in order): Remove all external media: Unplug any USB drives, external hard drives, CDs/DVDs, or memory cards from your computer. Then, reboot. If it boots normally, the external media was likely the issue. Check physical connections: Unplug and replug your PC: Sometimes a full power cycle can help. Open your computer case (if you're comfortable): Before you do this, power down your PC completely and unplug it from the wall. Carefully check the SATA data and power cables connected to your hard drive or SSD. Make sure they are firmly seated at both ends (on the drive and on the motherboard/power supply). If you have an M.2 SSD, ensure it's properly seated in its slot. Enter BIOS/UEFI and check boot order: Reboot your PC. As it starts up, repeatedly press the key to enter BIOS/UEFI setup. This key is usually Del, F2, F10, F12, or Esc, depending on your motherboard manufacturer. Look for a message on the screen during startup that tells you which key to press. Once in BIOS/UEFI: Look for a "Boot," "Boot Options," "Boot Order," or "Startup" tab/menu. Ensure your main hard drive/SSD (the one with your operating system) is listed as the first boot device. If it's not, change the boot order to prioritize it. Check if your hard drive/SSD is even detected in the BIOS. If it's not listed at all, it could indicate a connection issue or a failed drive. Save changes and exit BIOS/UEFI. Your computer should then attempt to boot. Try to repair your operating system (Windows): If you have a Windows installation USB drive or DVD, insert it into your computer. Boot from the installation media (you might need to adjust the boot order in BIOS again to do this). Choose "Repair your computer" instead of "Install now." Follow the prompts to access troubleshooting options like "Startup Repair." Consider a fresh operating system installation (last resort): If none of the above works and you suspect a corrupted OS or new drive, you might need to perform a clean installation of your operating system. Be aware that this will erase all data on the drive. Hardware failure: If your drive is not detected in BIOS after checking connections, or if you continue to get this error after trying all software-related fixes, it's possible your hard drive or SSD has failed. In this case, you would need to replace the drive and then install your operating system. Important Note: If you are unsure about opening your computer case, it's best to consult with someone knowledgeable about computer hardware or take it to a professional.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
