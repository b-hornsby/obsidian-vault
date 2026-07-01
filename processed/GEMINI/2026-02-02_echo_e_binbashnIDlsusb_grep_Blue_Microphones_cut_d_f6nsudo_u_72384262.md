---
id: 503752
source: GEMINI
date: 2026-02-02
tags: ['blue-yeti', 'usb-reset', 'bash-script', 'audio-fix']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is creating a script to reset his Blue Yeti microphone by identifying its USB ID and using `usbreset`.
---
# ❯ echo -e '#!/bin/bash\nID=$(lsusb | grep "Blue Microphones" | cut -d" " -f6)\nsudo usbreset $ID' > ~/reset_yeti.sh && chmod +x ~/reset_yeti.sh

~
❯ 

### USER
❯ echo -e '#!/bin/bash\nID=$(lsusb | grep "Blue Microphones" | cut -d" " -f6)\nsudo usbreset $ID' > ~/reset_yeti.sh && chmod +x ~/reset_yeti.sh

~
❯ 

### GEMINI
That script is your "software crowbar." Since we’ve already applied the kernel quirk and fixed the BIOS settings, the fact that you still need a replug means the Yeti's hardware is entering a "halt" state before the OS even loads. By running usbreset, you are electronically simulating a physical unplug/replug. Here is exactly how to make that script work automatically so you never have to touch the cable or the terminal again. 1. Fix the Script (It needs the specific ID) Your command created the file, but usbreset works best when given the exact Vendor:Product ID. Let's make it more robust. Run this command to overwrite the script with the perfected version: echo -e '#!/bin/bash\n# Reset the Blue Yeti by ID\nsudo usbreset 046d:0ab7' > ~/reset_yeti.sh && chmod +x ~/reset_yeti.sh 2. Allow it to run without a Password Since usbreset requires sudo, the script will hang waiting for your password at startup unless we give it a "hall pass." Run: sudo visudo Scroll to the very bottom of the file and add this exact line (replace yourusername with your actual CachyOS username): yourusername ALL=(ALL) NOPASSWD: /usr/bin/usbreset Save and exit (Ctrl+O, Enter, Ctrl+X). 3. Make it Run at Startup Now, we tell CachyOS to run this "electronic replug" every time you log in. If you use GNOME: Open "Startup Applications" and add a new entry. Name: Yeti Reset Command: /home/yourusername/reset_yeti.sh If you use KDE Plasma: Go to System Settings -> Autostart -> Add Script. The Advisor's Final Word You have now done everything humanly possible via software: Kernel Quirk: Disabled the power management that crashes the Yeti. Autosuspend: Disabled globally. BIOS: Disabled S5 power so the Yeti dies when the PC dies. Script: An automated electronic replug. If this still doesn't work: The Blue Yeti is literally failing to "boot" its own internal firmware fast enough for your modern PC's ultra-fast startup. If the script above works when you run it manually (~/reset_yeti.sh) but the mic is still dead after a reboot, you might need to add a small delay to the script: Update the script with a delay if needed: echo -e '#!/bin/bash\nsleep 5\nsudo usbreset 046d:0ab7' > ~/reset_yeti.sh Would you like me to help you check your journalctl logs one last time to see if the USB controller itself is throwing an "overcurrent" or "babble" error?
