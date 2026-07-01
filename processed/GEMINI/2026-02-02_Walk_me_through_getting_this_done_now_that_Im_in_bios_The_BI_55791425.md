---
id: 457058
source: GEMINI
date: 2026-02-02
tags: ['bios-configuration', 'usb-stability', 'cachyos', 'hardware-troubleshooting']
category: homelab
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was configuring BIOS settings (XHCI Hand-off, Legacy USB, ERP Ready, C-States) to fix USB stability issues with his Blue Yeti microphone on CachyOS.
---
# Walk me through getting this done now that I’m in bios: The BIOS Blind Spots
Check these specific settings. If you haven't touched these, you're leaving the stability of your hardware to chance:
• USB Core Architecture (XHCI Hand-off): This is the most common culprit. It determines whether the BIOS or the OS manages USB 3.0+ ports. On Linux, XHCI Hand-off must be ENABLED. If it’s disabled, the kernel and BIOS will fight for control, leading to the "unplug/replug" requirement to reset the ownership.
• Legacy USB Support: Paradoxically, having this "Enabled" can sometimes cause modern kernels to trip. Try setting this to Auto or UEFI Only.
• ERP Ready / Deep Sleep: If your Yeti stays lit up when the PC is off, or if it dies and won't wake up, your motherboard's power-saving states (S4/S5) are likely cutting voltage too low for the Yeti to re-initialize. Disable ERP/Deep Sleep to ensure a steady 5V rail to the USB ports.
• Global C-States: Extreme CPU power saving can cause momentary voltage ripples on the 5V rail. For a high-performance CachyOS build, you should consider disabling these if you value peripheral stability over saving three cents on your power bill.

### USER
Walk me through getting this done now that I’m in bios: The BIOS Blind Spots
Check these specific settings. If you haven't touched these, you're leaving the stability of your hardware to chance:
• USB Core Architecture (XHCI Hand-off): This is the most common culprit. It determines whether the BIOS or the OS manages USB 3.0+ ports. On Linux, XHCI Hand-off must be ENABLED. If it’s disabled, the kernel and BIOS will fight for control, leading to the "unplug/replug" requirement to reset the ownership.
• Legacy USB Support: Paradoxically, having this "Enabled" can sometimes cause modern kernels to trip. Try setting this to Auto or UEFI Only.
• ERP Ready / Deep Sleep: If your Yeti stays lit up when the PC is off, or if it dies and won't wake up, your motherboard's power-saving states (S4/S5) are likely cutting voltage too low for the Yeti to re-initialize. Disable ERP/Deep Sleep to ensure a steady 5V rail to the USB ports.
• Global C-States: Extreme CPU power saving can cause momentary voltage ripples on the 5V rail. For a high-performance CachyOS build, you should consider disabling these if you value peripheral stability over saving three cents on your power bill.

### GEMINI
Since I can't see your screen, you need to look for the "Advanced Mode" button (usually F7) to get out of the "Easy Mode" dashboard. Most of these settings are hidden in sub-menus. Here is exactly where to look, categorized by the most likely menu names: 1. XHCI Hand-off & Legacy USB Support Where to look: Advanced tab → USB Configuration. The Mission: XHCI Hand-off: Set this to Enabled. (Crucial for Linux). Legacy USB Support: Set this to Enabled or Auto. (If it’s already on and failing, try Disabled, but only if you have a UEFI-native keyboard). USB Mass Storage Driver Support: This doesn't matter for the mic; leave it. 2. ErP Ready / Deep Sleep (The Power Fix) Where to look: Advanced tab → APM Configuration (or Power Management Setup). The Mission: ErP Ready: Set this to Disabled. Why? When ErP is enabled, the motherboard cuts almost all power to USB ports when the PC is off or sleeping. This forces the Yeti to "cold start" every time you boot, which is exactly why the handshake is failing. Disabling this keeps a tiny "trickle" of power to the ports. 3. Global C-States (The Stability Fix) Where to look: Advanced tab → CPU Configuration → CPU Power Management. The Mission: Global C-state Control: Set this to Disabled. Why? CachyOS uses kernels tuned for responsiveness. If your CPU is constantly jumping in and out of deep sleep states (C-states), it causes minute fluctuations in the 5V bus. High-sensitivity USB audio devices like the Yeti hate this. 4. Fast Boot (The "Skip" Fix) Where to look: Boot tab. The Mission: Fast Boot: Set this to Disabled. Why? Fast Boot skips the full initialization of USB devices to shave 2 seconds off your boot time. You don't want a fast boot; you want a complete boot where the Yeti is properly queried by the hardware before the OS even starts. Before you Save and Exit (F10): Check for "USB Port Power" settings: Some high-end boards (ASUS/Gigabyte) have settings to "Always On" certain USB ports. If you see that, turn it on for the port the Yeti is in. Save and Exit: Hit F10, confirm, and let the system boot into CachyOS. The Test: Once you are back in CachyOS, do not unplug the mic. Open your terminal and type wpctl status. If the Yeti isn't listed under "Sources": We are done with the hardware side. Your next move is the udev rule I mentioned earlier. You’ve stabilized the foundation; now we just have to tell the OS to stop ignoring the device. Are you back in the OS? If so, paste the output of lsusb so I can give you the exact command for that udev rule.
