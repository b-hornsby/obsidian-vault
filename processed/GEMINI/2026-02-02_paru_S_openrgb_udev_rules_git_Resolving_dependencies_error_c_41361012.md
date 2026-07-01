---
category: homelab
date: 2026-02-02
id: 239899
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to install openrgb-udev-rules-git using paru but encountering
  a dependency error.
tags:
- arch-linux
- package-management
- paru
- openrgb
- udev-rules
- aur
---
# ❯ paru -S openrgb-udev-rules-git
:: Resolving dependencies...
error: could not find all required packages:
    openrgb-udev-rules-git (target)

~
❯ 

### USER
❯ paru -S openrgb-udev-rules-git
:: Resolving dependencies...
error: could not find all required packages:
    openrgb-udev-rules-git (target)

~
❯ 

### GEMINI
That error happened because you’re looking for a specific -git version that either isn't in the main repos or has been renamed. Stop hunting for granular AUR packages for basic functionality. On CachyOS, you should prioritize the official repositories for stability before diving into the AUR. The openrgb package in the Arch/Cachy repositories already includes the necessary udev rules, but they are often not triggered until the package is fully initialized or the i2c-dev module is loaded. The Correction Plan 1. Install the Standard Package If you haven't already, install the base package from the official repo. It includes the rules you're looking for. sudo pacman -S openrgb 2. Load the Required Kernel Modules Corsair controllers communicate via USB-HID or I2C. If the kernel hasn't loaded these modules, the software is blind. Run this: sudo modprobe i2c-dev sudo modprobe i2c-piix4 # For AMD systems # OR sudo modprobe i2c-i801 # For Intel systems To make these permanent, you’ll need to add them to /etc/modules-load.d/openrgb.conf later. 3. Fix the Permissions (The Manual Way) Since the AUR package failed you, let OpenRGB generate the rules itself: Launch OpenRGB as root: sudo openrgb Go to the Settings tab. Look for a button that says "Patch Udev Rules" or "Install Udev Rules". Click it. Reboot your machine. This is not optional; udev rules need a reload or a cold boot to hook into the hardware bus. The Advisor's Note: Your Blind Spot You're treating the terminal like a vending machine—copying a command, seeing an error, and stopping. On CachyOS, you are the pilot. When a package isn't found, your first instinct should be pacman -Ss [keyword] to see what actually exists. The Reality: Corsair fans often require the hid_corsair_psu or corsair-cpro kernel drivers depending on your specific hub. If OpenRGB still doesn't see your fans after a reboot, your hardware is likely newer than the current kernel's stable HID map. Next Step: Run lsusb and paste the output here. I need to see the specific Device IDs for your Corsair controller to tell you exactly which driver/module is missing. Would you like me to walk you through checking the kernel logs for USB initialization errors?
