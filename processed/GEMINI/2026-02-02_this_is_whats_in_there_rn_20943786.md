---
id: 402643
source: GEMINI
date: 2026-02-02
tags: ['directory-listing', 'visual-debugging']
category: general
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was sharing what was currently in a directory or configuration for troubleshooting purposes.
---
# this is whats in there rn 

### USER
this is whats in there rn 

### GEMINI
Since you are using Limine on CachyOS, your kernel parameters are managed in a specific file that the bootloader uses to auto-generate its configuration. We need to add the usbcore.quirks parameter. This is a "surgical strike" that tells the kernel to stop trying to use advanced power-saving features (like Link Power Management) on the Yeti, which is almost certainly what is causing it to crash during the initial boot handshake. 1. Update the Limine Configuration Open the configuration file: sudo nano /etc/default/limine Find the KERNEL_CMDLINE line: Look for a line that starts with KERNEL_CMDLINE[default]. Add the Yeti Quirk: At the end of the existing parameters (inside the quotes), add a space and then: usbcore.quirks=046d:0ab7:k The k flag is the specific instruction to disable "LPM" for this device. Save and Exit: Press Ctrl+O, Enter, then Ctrl+X. Apply the changes: On CachyOS, you must regenerate the boot entries to move your changes from the "default" file into the actual bootloader. Run: sudo limine-mkinitcpio (This command triggers the limine-entry-tool in the background to rewrite your boot entries with the new quirk). 2. The Final BIOS Check (S5 Power) If you still have to unplug the mic after a reboot, it's because the Yeti is "remembering" its crashed state from the previous session because it never lost power. Go back into BIOS. Navigate to: Advanced -> Onboard Devices Configuration. Set: USB power delivery in Soft Off state (S5) to DISABLED. Result: This forces the Yeti to lose 100% of its power when the PC turns off. It will be forced to perform a clean hardware reset every single time you boot up. Verify the Quirk After you reboot, run this command to make sure the kernel actually received your instruction: cat /proc/cmdline Does usbcore.quirks=046d:0ab7:k appear in that list? If it does, and you have disabled S5 power in the BIOS, the Yeti should now initialize correctly on every boot without you touching the cable. If it still doesn't show up, paste the output of dmesg | grep usb so I can see the exact error code the kernel is throwing during the handshake.
