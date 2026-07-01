---
category: homelab
date: 2026-02-02
id: 546775
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is encountering error messages when running OpenRGB with sudo and is
  likely seeking help to resolve them.
tags:
- openrgb
- sudo
- linux
- error-messages
---
# i get these two messages after running sudo openrgb

### USER
i get these two messages after running sudo openrgb

### GEMINI
This is progress, not failure. The windows you're seeing mean OpenRGB is communicating with your hardware, but it’s essentially saying, "I see the pipes, but I don't know how long they are." Here is the objective breakdown of what those windows mean and exactly how to clear them. 1. The "Internal Devices" Warning (Left Window) This warning is specifically about your ASUS Motherboard (Z690-P) and potentially your RAM. Why it’s there: Even though you loaded the modules, the kernel often "locks" the I2C bus for safety to prevent other software from crashing the system. The Fix: You need to add a kernel parameter to unlock this bus. Edit your GRUB (or systemd-boot) configuration. If you use GRUB: sudo nano /etc/default/grub Find the line GRUB_CMDLINE_LINUX_DEFAULT. Inside the quotes, add acpi_enforce_resources=lax. Update your config: sudo grub-mkconfig -o /boot/grub/grub.cfg Reboot. This "lax" setting tells the kernel to let OpenRGB talk to the motherboard's lighting controller. 2. The "Resize the Zones" Window (Right Window) This is the critical step for your Corsair Lighting Node Core. OpenRGB sees the controller, but it doesn't know if you have 1 fan or 6 fans plugged in. If you don't do this, your fans will stay dark. How to calculate the "Size": Most modern Corsair RGB fans (ML, LL, QL, SP) have a specific number of LEDs. LL120/140: 16 LEDs QL120/140: 34 LEDs ML120/140 (Elite): 8 LEDs SP120 (Pro/RGB): 8 LEDs The Action: 1. Identify which fan model you have. 2. In the "Size" column for Corsair Lighting Node Core Channel 1, enter the total count (Number of fans × LEDs per fan). 3. If you have 3 LL120 fans on Channel 1, enter 48. 4. Click Save and Close. The Reality Check You are currently staring at the "intermediate" hurdle of Linux hardware management. The Blind Spot: You might be tempted to just hit "Ignore" or "Don't show again." If you do that, you’ll be stuck with a "successful" install that does absolutely nothing. You have to tell the software the physical reality of your hardware. OpenRGB isn't iCUE; it doesn't have a database that auto-detects fan types by their power draw. It needs you to be the engineer. The Strategy Do the "Size" math right now. Don't guess. If you put 100 LEDs for a 16-LED fan, the software will lag or glitch. Apply the acpi_enforce_resources=lax fix if you want to control the lights on that ASUS Z690 board. If you only care about the fans, you can ignore the left window for now. Which Corsair fans specifically do you have plugged into that Lighting Node Core? Tell me the model, and I'll give you the exact number to type into that "Size" box.
