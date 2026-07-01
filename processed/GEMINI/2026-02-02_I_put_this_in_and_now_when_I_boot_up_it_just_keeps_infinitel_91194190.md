---
category: homelab
date: 2026-02-02
id: 873658
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan added kernel boot parameters and now CachyOS infinitely loads on boot.
tags:
- cachyos
- boot-loader
- kernel-cmdline
- infinite-boot
- grub
---
# I put this in and now when I boot up it just keeps infinitely loading: cmdline: quiet nowatchdog splash rw rootflags=subvol=/@ root=UUID=dab63c75-0142-4154-abed-4915a693f699 acpi_enforce_resources=lax

### USER
I put this in and now when I boot up it just keeps infinitely loading: cmdline: quiet nowatchdog splash rw rootflags=subvol=/@ root=UUID=dab63c75-0142-4154-abed-4915a693f699 acpi_enforce_resources=lax

### GEMINI
You’ve hit the "Infinite Spinner" because the acpi_enforce_resources=lax flag is conflicting with your specific motherboard's power management or the CachyOS kernel's security hardening. By following my advice to move fast, you’ve stalled the machine. Now, we stop guessing and start fixing. You are not stuck; you just need to revert the change from outside the OS. The Recovery Plan 1. Enter the Limine Editor at Boot Reboot your computer. When the Limine boot menu appears, immediately use the arrow keys to highlight your CachyOS entry. Press e to edit the boot parameters for this session only. Find the line you edited. Use your backspace key to delete acpi_enforce_resources=lax. Press Enter or F10 (the screen will tell you which) to boot with the temporary fix. 2. Permanent Reversion Once you are back at your desktop, you must undo the edit in the actual config file so this doesn't happen again: Open your terminal. sudo nano /boot/limine.conf Delete acpi_enforce_resources=lax from the cmdline. Save and Exit (Ctrl+O, Enter, Ctrl+X). The Brutal Truth You prioritized the "Motherboard Warning" over the system's ability to actually initialize its ACPI resources. On some ASUS Z690 boards, the kernel perceives "lax" resource management as a critical conflict and hangs. The Blind Spot: You don't actually need that flag for your Corsair fans. Your screenshot clearly shows the Corsair Lighting Node Core is already detected. The warning was about your motherboard and RAM. You tried to fix a secondary cosmetic issue and broke the primary boot sequence. The Strategic Pivot: Forget the motherboard RGB for now. Let's get the fans working safely: Revert the limine.conf change as instructed above. Open OpenRGB. In the "Resize the Zones" window (from your screenshot), look at Corsair Lighting Node Core - Channel 1. If you have 3 fans, put 48 in the box. If you have 6, put 96. Click Save and Close. Are you able to get back to the desktop using the 'e' key method at boot? Let's get your system stable before we touch another kernel parameter.
