---
category: homelab
date: 2026-02-02
id: 584118
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan expresses frustration that his Blue Yeti microphone still requires
  manual unplugging/replugging despite previous troubleshooting steps and a reboot.
tags:
- blue-yeti
- usb-troubleshooting
- audio-issue
- frustration
---
# did all that and still have to unplug replug. i even rebooted

### USER
did all that and still have to unplug replug. i even rebooted

### GEMINI
If you’ve done the BIOS, the udev rules, and the WirePlumber config, and it’s still dead on boot until you touch the cable, then we are dealing with a hardware-level initialization failure that the OS literally cannot fix because the Yeti’s firmware is "hanging" before the kernel even gets to talk to it. Since your lsusb showed the device is present but wpctl showed it wasn't working (until replug), the Yeti is in a "zombie" state. It's powered, but its internal processor didn't start its audio engine. Here is the "Nuclear Option" to force this to work without you ever touching that cable again. 1. The Kernel "Quirk" (The Real Fix) The Blue Yeti is famous for failing to report its sample rate correctly on boot. We can force the Linux kernel to treat it with "special" parameters the moment it sees it. Open your GRUB/Boot configuration: If you use GRUB: sudo nano /etc/default/grub Find the line starting with GRUB_CMDLINE_LINUX_DEFAULT. Add this exact parameter inside the quotes: usbcore.quirks=046d:0ab7:k (The k flag tells the kernel to avoid certain power-management handshakes that crash the Yeti's old controller). Update and Reboot: sudo grub-mkconfig -o /boot/grub/grub.cfg (or the CachyOS equivalent if you use sd-boot). 2. The "Automated Replug" Script If the hardware is stubborn, we stop trying to "fix" it and we start simulating a replug via software every time you log in. Install usbreset: sudo pacman -S usbutils (usually already there). Create a script: nano ~/yeti-reset.sh Paste this in: #!/bin/bash # Find the Yeti and reset its USB port ID=$(lsusb | grep "Blue Microphones" | awk '{print $6}') if [ ! -z "$ID" ]; then sudo usbreset $ID echo "Yeti Reset Performed" fi Make it executable: chmod +x ~/yeti-reset.sh Add it to "Startup Applications" in your GNOME/KDE settings. The Advisor's Brutal Truth You are fighting a 15-year-old hardware design. The Blue Yeti uses a Mini-USB controller that was never designed for the fast-boot, aggressive power-saving world of 2026. If the usbcore.quirks doesn't work: You are likely experiencing a back-powering issue. Your ASUS board is keeping the 5V rail alive (S5 state), so the Yeti never "dies." When you reboot, the Yeti thinks it's still in the previous session and ignores the new initialization request. The fix you'll hate: Go back into BIOS and DISABLE "USB power delivery in Soft Off state (S5)." Yes, I know we enabled it earlier. But for some specific Yeti revisions, they need to lose total power when the PC shuts down so they can "cold boot" with the system. Try disabling the S5 power in BIOS first. Does the mic light turn OFF when the PC is off? If so, that's your winner.
