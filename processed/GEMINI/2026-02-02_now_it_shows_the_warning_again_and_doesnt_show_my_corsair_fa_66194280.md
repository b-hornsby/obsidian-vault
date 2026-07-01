---
category: homelab
date: 2026-02-02
id: 493296
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was dealing with a recurring warning and his Corsair fans not being
  detected by his system software.
tags:
- corsair-fan-control
- usb-device
- hardware-monitoring
---
# now it shows the  warning again and doesnt show my corsair fans again 

### USER
now it shows the  warning again and doesnt show my corsair fans again 

### GEMINI
The reason you’re back at square one is that your emergency edit at the boot screen was temporary. It got you back into the system, but the "Configuration is INVALID" error in your last photo proves your physical limine.conf file is still a mess. Because the bootloader can’t read your config file correctly, it’s failing to load the i2c-dev and i2c-i801 modules you set up earlier. No modules = no Corsair fans. The Repair Plan 1. Fix the Bootloader Syntax Permanently You need to make that cmdline one single line again. Open the terminal. Run: sudo nano /boot/limine.conf Look at the bottom of the file. Your root=UUID... is likely on a separate line. Delete the line break so that everything follows cmdline: in one continuous string. Delete acpi_enforce_resources=lax. Your system clearly hated it, and you don't need it for the fans. Save (Ctrl+O, Enter) and Exit (Ctrl+X). 2. Force-Reload the Modules Since the bootloader skipped them, load them manually right now so you don't have to reboot again: sudo modprobe i2c-dev sudo modprobe i2c-i801 3. Reset OpenRGB Detection Close OpenRGB completely. Launch it as root to ensure it has full hardware access: sudo openrgb If the fans appear, don't touch the motherboard settings. Go straight to the "Resize the Zones" window. Enter your LED count (e.g., 48 for 3 standard fans) and click Save and Close. The "Mirror" Reality Check You are stuck in a loop because you're treating the symptoms (the warning message) rather than the cause (the broken config file). You "got back in," but you didn't actually fix the damage. The Blind Spot: You are staring at that warning message like it’s a brick wall. It’s not. It’s just a sign saying "I can't see the I2C bus." The moment you fix the line in limine.conf and run those modprobe commands, that wall vanishes. The Strategy: Don't reboot again until you have confirmed that cat /boot/limine.conf shows the cmdline as one single line. If you see it split across two lines, you will end up back in Emergency Mode. Once you run those two modprobe commands and launch sudo openrgb, do the Corsair Lighting Node Core entries reappear in the list?
