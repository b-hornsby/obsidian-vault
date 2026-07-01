---
category: homelab
date: 2026-03-21
id: 811542
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan encountered an error after installing OpenRGB and is seeking help to
  resolve it.
tags:
- openrgb
- installation-error
- rgb-control
- software-issue
---
# Installed open rgb and got this?

### USER
Installed open rgb and got this?

### GEMINI
That screen is the "Manual Configuration" step. OpenRGB can see your ASUS Prime Z690 and your Corsair Lighting Node Core, but it doesn't know how many LEDs are actually plugged into them. If you leave these at 0, your lights will stay off because the software thinks there is nothing to light up. Think of this like setting the capacity for a warehouse rack—if you tell the system the capacity is 0, it won't send any inventory there. How to fill this out: 1. Corsair Lighting Node Core (Most Important) This is where your fans are plugged in. Corsair Fans: Most standard Corsair RGB fans (like the SP, LL, or ML series) have a specific LED count. ML series: 4 LEDs SP-RGB series: 8 LEDs LL series: 16 LEDs QL series: 34 LEDs The Math: If you have 3 LL fans on one channel, the "Size" should be 48 ($16 \times 3$). If you aren't sure, start with 10 and keep clicking the "up" arrow until all your fans are fully lit. 2. ASUS PRIME Z690-P WIFI (Aura Addressable) These are the headers on your motherboard. If you have an RGB strip or a CPU cooler plugged into the motherboard headers (3-pin ARGB), you need to enter the LED count for those strips. Common strip lengths: Usually 30 or 60 LEDs. If nothing is plugged into your motherboard's RGB headers, just leave these at 0. The "Quick Fix" Strategy Focus on the Corsair Lighting Node Core first. Type 20 into "Corsair Channel 1" and click Save and Close. Go to the main OpenRGB window, select the Lighting Node Core, pick a bright color (like Red), and click Set All Devices. If only half a fan lights up, come back to this "Resize" menu and increase the number. Don't overthink it: You won't break anything by putting a number that is too high; it just creates "empty" LED slots in the software. It’s better to over-estimate than under-estimate. How many fans do you have plugged into that Lighting Node Core? Tell me the model (or what they look like) and I'll give you the exact number to type in.
