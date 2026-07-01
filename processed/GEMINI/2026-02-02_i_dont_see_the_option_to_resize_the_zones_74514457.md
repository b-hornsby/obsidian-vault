---
id: 089550
source: GEMINI
date: 2026-02-02
tags: ['obs-studio', 'resize-zones', 'streaming-layout', 'cachyos']
category: streaming
sentiment: frustrated
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
summary: Bryan couldn't find the option to resize zones in OBS Studio or a streaming layout tool on CachyOS.
---
# i dont see the option to resize the zones

### USER
i dont see the option to resize the zones

### GEMINI
The reason you don't see the "Resize the zones" window anymore is that you likely checked "Do not show again" in that specific popup during a previous session. Because that window is gone, OpenRGB is defaulting your fan zones to a size of 0, which keeps them dark. How to Manually Resize the Zones You don't need the popup to configure your fans. You can do it directly from the main interface: Select the Device: In the left-hand list, click on Corsair Lighting Node Core. Access the Zone: Click the Edit button next to the "Zone" dropdown menu (usually located at the top of the device settings). Enter the Count: A new window will appear. Look for "Corsair Channel 1" and enter the total number of LEDs for your fans (e.g., 48 for three standard fans or 96 for six). Save: Click Save or Apply. The "Brutally Honest" Clean-up Plan You are still seeing the "Internal devices may not be detected" warning because you correctly removed the acpi_enforce_resources=lax flag to fix your boot issue. Stop trying to fix this. Your Corsair fans are USB-based, and as your latest screenshot shows, they are already detected. That warning only applies to your ASUS motherboard and RAM; ignore it so you don't break your bootloader again. Your Prioritized To-Do List: Step 1: Permanent Boot Fix: Ensure you have fixed the syntax in /boot/limine.conf. If you haven't merged those two lines into one continuous string yet, your next reboot will send you straight back to Emergency Mode. Step 2: Apply Color: Once you have resized the zones as described above, select a color on the ring, set the Mode to "Direct" or "Static," and click Apply All Devices. Step 3: Silence the Warning: In the warning popup that keeps appearing, check the box "Don't show this message again" and hit OK. The Blind Spot You are searching for a specific "option" to appear, but in Linux, once you dismiss a helper window, you have to go into the actual device settings to find those controls. You have the hardware detected; you just need to tell the software that the "Channel" has LEDs attached to it. Would you like me to give you a specific LED count based on your fan model so your lighting effects line up perfectly?
