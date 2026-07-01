---
id: 901316
source: GEMINI
date: 2026-02-02
tags: ['screenshot-sharing', 'visual-reference', 'web-page']
category: general
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
summary: Bryan shared a scrolled view of a previous page/screen to provide more context on something he was examining.
---
# This is what I see when I scroll down in that same page

### USER
This is what I see when I scroll down in that same page

### GEMINI
In your second image, the settings you need are right in front of you. ASUS hides them under the "Acoustic Noise Settings" block. 1. Disable C-states Right Now In the second image, look at the bottom half of the list: Enhanced C-states: Change this from "Enabled" to Disabled. CPU C-states: Change this from "Auto" to Disabled. Why you're doing this: By disabling these, you prevent the CPU from entering deep sleep modes that cause the 5V USB rail to fluctuate. For a sensitive, older USB controller like the one in the Blue Yeti, these tiny power dips are often enough to make the hardware "detach" logically while remaining physically plugged in. 2. Next: The USB Handshake Fix You are currently in the CPU Configuration menu. You need to switch to the USB menu to ensure the OS and BIOS aren't fighting over the mic: Press Esc to go back to the main Advanced tab. Find USB Configuration. Set XHCI Hand-off to Enabled. (If it’s already enabled, leave it). 3. Final Step: The Power Rail Fix Go back to the Advanced tab. Find APM Configuration. Find ErP Ready and set it to Disabled. This ensures the Yeti doesn't lose total power and fail to wake up when you start the PC. Exit and Verify Press F10 to Save and Exit. Let CachyOS boot normally. Do not touch the USB cable. Once you're at your desktop, open your terminal. Would you like me to give you the specific terminal command to check if the Yeti is officially "alive" and recognized by the audio server once you're back in?
