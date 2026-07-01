---
id: 480424
source: GEMINI
date: 2026-02-02
tags: ['cachyos', 'c-states', 'cpu-power-management', 'bios-settings']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is looking for global C-states settings on his CachyOS system for CPU power management.
---
# Looking for global c states

### USER
Looking for global c states

### GEMINI
You are looking in the CPU - Power Management Control submenu, but on ASUS boards, Global C-state Control is usually one level up or tucked further down the list. Based on the image of your BIOS, here is how to find it and what to fix right now: 1. Find Global C-states Scroll Down: In that current screen (Advanced\CPU Configuration\CPU - Power Management Control), use your mouse or arrow keys to scroll to the very bottom. Alternative Location: If it isn't at the bottom of that list, press Esc once to go back to the main CPU Configuration page. Look for a setting called CPU - Power Management Control or simply Global C-state Control near the bottom of that main list. Action: Change it from "Auto" to Disabled. 2. While You Are on This Specific Screen (Image 1) I see three settings in your photo that affect how the CPU ramps power. To maximize peripheral stability on CachyOS: Intel(R) SpeedStep(tm): Leave as Enabled. Intel(R) Speed Shift Technology: Leave as Enabled. Turbo Boost Max Technology 3.0: Leave as Enabled. Note: These aren't the problem; it's the idle "Sleep" states (C-states) that drop the voltage too low for the Yeti. 3. The "USB Handshake" Fix (Crucial) You are currently in the CPU sub-menu. You need to navigate to the USB sub-menu to fix the actual handshake: Press Esc until you are back at the main Advanced tab. Find and enter USB Configuration. Ensure XHCI Hand-off is set to Enabled. 4. The "Power Drop" Fix Navigate to Advanced -> APM Configuration. Find ErP Ready. Set it to Disabled. Next Step: Once you've disabled Global C-states and ErP Ready, press F10 to save and exit. When you get back into CachyOS, open a terminal and run lsusb. Does the Blue Yeti show up immediately without you touching the cable? If not, copy and paste that lsusb output here so we can force the OS to keep the port "alive."
