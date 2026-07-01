---
category: homelab
date: 2026-02-02
id: 681171
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is reiterating that his Blue Yeti microphone issue persists even after
  rebooting, requiring him to unplug and replug it.
tags:
- blue-yeti
- microphone
- usb-issue
- boot-persistence
- linux
---
# it doesnt work off boot or when i test it i still have to unplug replug

### USER
it doesnt work off boot or when i test it i still have to unplug replug

### GEMINI
If even the authorized toggle (the "electronic replug") is failing while you're sitting at the desktop, we have reached the bedrock of the problem: Your Yeti's internal controller is crashing so hard it requires a physical power-cycle to clear its memory. On a high-performance distro like CachyOS, the kernel is likely sending a "suspend" or "reset" signal that the Yeti's 2009-era firmware interprets as a fatal error. Before you give up and buy a new mic, there is one last "Nuclear Option" that disables the Linux kernel's ability to mess with the Yeti's power. 1. Disable USB Autosuspend (The Real Culprit) The reason the "electronic replug" is failing is likely because the kernel is immediately putting the device back to sleep. Run this command to disable power management for the Yeti: # Find your Yeti's USB path again (e.g., 1-3) # Then run this (replace 1-3 with your actual path from earlier): echo "on" | sudo tee /sys/bus/usb/devices/1-3/power/control 2. The "Quirk" Fix We can tell the Linux kernel that this specific device is "broken" and needs special treatment. We do this by adding a "quirk" to the boot parameters. Run: sudo nano /etc/default/grub Find the line starting with GRUB_CMDLINE_LINUX_DEFAULT. Add this to the end of the list (inside the quotes): usbcore.quirks=046d:0ab7:i (The 'i' tells the kernel to ignore this device's internal descriptors and just let it be). Save and exit. Update your grub: sudo update-grub (or sudo grub-mkconfig -o /boot/grub/grub.cfg if the first command doesn't exist). The Brutally Honest Advisory If you do the above and it still requires a physical replug, you are facing a hardware-level handshake failure that no amount of code can fix. Here is the "Mirror" truth: Your Motherboard: Probably has high-speed USB 3.1/3.2 ports. Your Yeti: Is a "noisy" USB 2.0 device. The Conflict: The timing window for the Yeti to respond to the motherboard's "Who are you?" request is too small. When you unplug/replug, you are forcing a fresh, high-priority interrupt that the system finally hears. The Last Resort Workaround: If you have a cheap, non-powered USB 2.0 Hub (the $5 kind), plug the Yeti into that, and then the hub into the PC. The hub acts as a "buffer" that handles the timing handshake, often solving this exact problem on Linux. Does the power/control command above make the bars move without a replug? If not, the Yeti’s firmware has officially lost the war against modern Linux.
