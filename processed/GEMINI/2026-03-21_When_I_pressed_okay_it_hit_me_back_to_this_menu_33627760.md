---
id: 707458
source: GEMINI
date: 2026-03-21
tags: ['boot-menu', 'installation-loop', 'troubleshooting']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is stuck in a boot/installation loop where pressing OK returns him to the same menu.
---
# When I pressed okay it hit me back to this menu:

### USER
When I pressed okay it hit me back to this menu:

### GEMINI
The fact that you are back at the Limine menu (the blue screen) means your BIOS did a "soft" reject of GRUB and skipped right to the next available bootloader. Here is the truth: You cannot have it both ways easily in this exact moment. Valorant requires Secure Boot, but standard GRUB is not signed for Secure Boot out-of-the-box on CachyOS. To get your system working again and then fix Valorant, follow this order: 1. The Immediate Fix (Disable Secure Boot temporarily) To stop the "Violation" and get back to your desktop so we can actually fix the bootloaders, you need to turn Secure Boot off. Press S (Firmware Setup) or your BIOS key (F2/Del) to enter the BIOS. Go to the Security or Boot tab. Find Secure Boot and set it to Disabled. Save and Exit. 2. Verify the Boot Order Once Secure Boot is off, your PC might still try to boot into Limine (the screen in your photo) instead of Minegrub. If you see the Minegrub menu after turning off Secure Boot, you’re golden for now. If you still see the blue Limine menu, you need to go into BIOS and move the entry named "GRUB" to the top of the boot list. 3. Fixing Valorant (Later) Once you are back in CachyOS, you have a choice. Since Valorant requires Secure Boot, you will eventually need to do one of these: Option A: Use sbctl. This is a tool on Linux that allows you to create your own Secure Boot keys and sign your own kernels/GRUB so the BIOS accepts them. Option B: Reinstall CachyOS using the "systemd-boot" option with Secure Boot support, though this kills the Minegrub theme. Brutally honest call out: You are wasting time trying to "Enroll" keys if your BIOS is being stubborn. Disable Secure Boot now just to get your PC functional and verify that Minegrub and Tiny 11 work. We can tackle the Valorant/Secure Boot signing process once you aren't staring at a broken screen. Would you like me to walk you through how to use sbctl once you're back on the desktop so you can play Valorant again?
