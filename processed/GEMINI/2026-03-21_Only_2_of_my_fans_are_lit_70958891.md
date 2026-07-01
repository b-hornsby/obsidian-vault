---
category: homelab
date: 2026-03-21
id: 986275
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is reporting that only two of his RGB fans are lighting up, indicating
  a potential hardware or software issue.
tags:
- rgb-fans
- lighting-issues
- fan-control
- hardware-problem
---
# Only 2 of my fans are lit?

### USER
Only 2 of my fans are lit?

### GEMINI
If only 2 of the 3 fans are lit, your "Size" number is too low for the total LED count of your specific fan model. OpenRGB is literally running out of "instructions" before it reaches the end of the third fan. Since you have 3 fans, let's stop guessing and use a number that will definitely cover them. The "Overfill" Fix Go back to the Resize the zones menu (if it's closed, click the Information tab in the main window and find the Resize button). Find the Corsair Lighting Node Core -> Corsair Channel 1. Change the Size to 120. Why 120? Even the most power-hungry Corsair fans (QL series) only use 34 LEDs each ($34 \times 3 = 102$). Setting it to 120 ensures you have plenty of "headroom." Click Save and Close. In the main window, select the Corsair Lighting Node Core, pick a color (like bright Blue), and hit Set All Devices. Why did this happen? You likely have LL120 or QL120 fans. If you entered 24, that only covers 1.5 fans. If you entered 48, that covers exactly 3 "standard" fans, but if yours have inner and outer rings, it's not enough. The Operations Check If you set it to 120 and that third fan still doesn't light up: The "Port" Rule: Ensure your fans are plugged into ports 1, 2, and 3 on the Hub. If you skipped a port (e.g., ports 1, 2, and 4), the chain is broken and the signal won't reach the last fan. The "Cold Boot" Reminder: Since you’re coming from Linux/CachyOS, the controller might be "stuck" in its old state. If the software says 120 and the fan is dark, shut down and flip the PSU switch for 10 seconds. Did the third fan kick on after you bumped the number to 120?
