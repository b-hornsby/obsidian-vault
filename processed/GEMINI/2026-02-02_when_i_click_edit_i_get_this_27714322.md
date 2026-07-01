---
category: general
date: 2026-02-02
id: 476031
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan encountered an unspecified error when clicking 'edit' in an application
  and is seeking help.
tags:
- unknown-error
- application-debugging
---
# when i click edit i get this 

### USER
when i click edit i get this 

### GEMINI
In that Resize Zone window, you are looking at a blank list because you haven't defined the hardware segments for the controller yet. OpenRGB sees the "pipe" (the Lighting Node Core), but it doesn't know what's inside it. The Fix: Adding Your Fans Click "Add Segment": In that small popup window, click the Add Segment button. Name It: You can name it "Fans" or "Channel 1". Set the Size: This is the critical part. If you have 3 standard Corsair fans (like LL120s), enter 48. If you have 6 fans, enter 96. If you aren't sure of the model, enter 100 just to see them light up. Click OK: Once you click OK, the main OpenRGB window will update, and you will see a long row of LED boxes appear in the preview area. Apply Color: Select a color on the wheel and hit Apply All Devices. The Advisor's "Mirror" Check You’re getting frustrated because the UI isn't "auto-filling" for you. You're waiting for the machine to tell you what's connected, but on Linux, you tell the machine. The Blind Spot: Look at your previous bootloader error one more time. The "Configuration is INVALID" message was caused by that line break. If you haven't fixed /boot/limine.conf to be one single line yet, your next reboot will be another trip to Emergency Mode. Do not prioritize the RGB over the ability to turn the computer on. The Strategy The Command: Run cat /boot/limine.conf right now. If the cmdline: and root=UUID are on different lines, run sudo nano /boot/limine.conf and backspace that second line up to join the first. The Fans: Follow the "Add Segment" steps above. Once you click "Add Segment" and put in a number like 48, do the fans finally light up when you click a color?
