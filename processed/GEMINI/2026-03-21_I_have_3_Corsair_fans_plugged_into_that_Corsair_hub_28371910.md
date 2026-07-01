---
id: 480510
source: GEMINI
date: 2026-03-21
tags: ['corsair-fans', 'rgb-hub', 'fan-controller', 'icue']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is providing information about his Corsair fan setup, likely in response to a troubleshooting question about RGB or fan control.
---
# I have 3 Corsair fans plugged into that Corsair hub

### USER
I have 3 Corsair fans plugged into that Corsair hub

### GEMINI
Since you have 3 fans on that Corsair hub, the number you enter depends on the specific model. Because you’re on Tiny11, we want the most efficient setup possible so you can "save to device" and never open this software again. Look at your fans right now and match them to these counts: 1. Identify Your Fans Single ring of light in the center only: These are SP RGB or ML RGB fans. Enter: 24 ($3 \text{ fans} \times 8 \text{ LEDs}$) Ring of light around the edge + center hub: These are LL120 fans. Enter: 48 ($3 \text{ fans} \times 16 \text{ LEDs}$) Bright rings on BOTH sides (Front and Back): These are QL120 fans. Enter: 102 ($3 \text{ fans} \times 34 \text{ LEDs}$) 2. Enter the Number Go to the line that says Corsair Lighting Node Core - Corsair Channel 1. Type the total number from above into the Size box. Click Save and Close. 3. Test the Setup In the main OpenRGB window, click on the Corsair Lighting Node Core. Select a color (like bright Green). Click Set All Devices. If the last fan is half-dark: Increase the number by 8 or 10. If they all light up: You’re golden. The "Operations" Efficiency Play: Once you have the colors you want, look for a "Save to Device" or "Hardware" button in the Corsair Lighting Node settings tab. If you click that, the Lighting Node will store the color in its own memory. This means you can uninstall OpenRGB entirely or just disable it at startup, and your 12700K rig will stay lit without a single background process running. Are all 3 fans lighting up fully now, or do we need to bump that number up?
