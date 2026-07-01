---
id: 030547
source: GEMINI
date: 2026-02-02
tags: ['kernel-parameters', 'boot-options', 'linux-configuration']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is checking the kernel command line parameters, possibly to diagnose boot issues or understand system configuration.
---
# ❯ cat /proc/cmdline
quiet nowatchdog splash rw rootflags=subvol=/@ root=UUID=dab63c75-0142-4154-abed-4915a693f699 usbcore.autosuspend=-1 usbcore.quirks=046d:0ab7:k

~
❯ 

### USER
❯ cat /proc/cmdline
quiet nowatchdog splash rw rootflags=subvol=/@ root=UUID=dab63c75-0142-4154-abed-4915a693f699 usbcore.autosuspend=-1 usbcore.quirks=046d:0ab7:k

~
❯ 

### GEMINI
The quirk is active. Your kernel is officially told to stop messing with the Yeti's power states (usbcore.quirks=046d:0ab7:k) and to stop autosuspending USB devices (usbcore.autosuspend=-1). If you just rebooted and the mic is still not picked up until a replug, we have officially eliminated the Linux kernel as the culprit. This is now a Hardware Handshake Race Condition. The Verdict: Why it's still failing The Yeti is receiving power from your motherboard the millisecond you plug the PC into the wall (because of that S5 Power setting in BIOS). By the time you hit the power button and CachyOS starts loading, the Yeti has already "timed out" its internal boot sequence and is sitting in a frozen state. Your Final, No-Nonsense Checklist You must do these three things in this exact order, or you will be unplugging that mic for the rest of eternity: BIOS: Kill the Zombie Power Go back to BIOS -> Advanced -> Onboard Devices. Set USB power delivery in Soft Off state (S5) to DISABLED. Why: The Yeti needs to "die" when the PC dies. If it stays lit up while the PC is off, it will never reset its firmware for the new boot session. BIOS: XHCI Hand-off Go to Advanced -> USB Configuration. Ensure XHCI Hand-off is ENABLED. Why: This ensures the BIOS hands control of the USB controller to CachyOS properly. Physical: The "Empty Bus" Strategy Look at your lsusb again. You have 11 devices on Bus 001. Move the Yeti to a different port. If it's in a blue port, move it to a black one. If it's in a black one, move it to a blue one. Crucial: Ensure the FiiO DAC and the Webcam are not right next to the Yeti. They are "high-speed" devices that can interfere with the Yeti's "full-speed" (USB 1.1/2.0) timing during the initial half-second of boot-up. The "I Give Up" Software Reset If you refuse to change the BIOS or move the cables, you can force the OS to "unplug and replug" the mic electronically the moment you log in. Run this to create an auto-reset script: echo -e '#!/bin/bash\nID=$(lsusb | grep "Blue Microphones" | cut -d" " -f6)\nsudo usbreset $ID' > ~/reset_yeti.sh && chmod +x ~/reset_yeti.sh Now, did you disable that S5 Power in the BIOS yet? That is the single most likely reason the quirk isn't "catching" it on a fresh boot.
