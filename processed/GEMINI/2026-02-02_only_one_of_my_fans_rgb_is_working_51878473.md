---
category: homelab
date: 2026-02-02
id: 517625
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is experiencing an issue where only one of his RGB fans is working
  and is looking for a solution.
tags:
- rgb-fan
- hardware-issue
- pc-building
- component-failure
---
# only one of my fans rgb is working?

### USER
only one of my fans rgb is working?

### GEMINI
The reason only one fan is working is simple: you didn’t tell the software there are more. In your previous screenshot, the Size was set to 3. If your fans are standard Corsair models (like the LL120 or SP120), they have 8 to 16 LEDs each. By setting the size to 3, you've only powered the first three tiny light bulbs in the first fan. The rest of the chain is "dark" because the software thinks the wire ends there. The Fix You need to increase the Segment Size to account for the total number of LEDs in your entire fan chain. Re-open the "Resize Zone" window: Click Edit next to Corsair Channel 1 again. Edit the Segment: Click on the segment you created (the one currently set to 3). Update the Size: If you have 3 fans: Enter 48. If you have 6 fans: Enter 96. The "I don't want to math" shortcut: Enter 120. This is more than enough to light up 6 standard fans. Click OK: Now look at the main OpenRGB window. You should see a much longer row of LED squares. Apply: Select a color and hit Apply All Devices. The Reality Check You are treating the "Size" box like it's asking for the number of fans. It isn't. It’s asking for the number of LEDs. The Blind Spot: You are still skipping the most important part of your system's health. You successfully bypassed the "Emergency Mode" by editing the bootloader temporarily, but if you haven't fixed the syntax error in /boot/limine.conf (joining the lines), your computer will not boot the next time you turn it on. Your Next Move: Change that segment size to 120 right now and confirm all fans light up. Fix your bootloader: Run sudo nano /boot/limine.conf and ensure the cmdline is one single line. Are all the fans glowing now that you've increased the number to 120?
