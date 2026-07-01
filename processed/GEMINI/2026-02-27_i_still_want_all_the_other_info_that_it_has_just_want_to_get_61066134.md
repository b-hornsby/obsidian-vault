---
category: homelab
date: 2026-02-27
id: 418168
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan wants to remove the local IP address from his terminal display while
  retaining other information.
tags:
- terminal-customization
- fish-shell
- ip-address
---
# i still want all the other info that it has just want to get rid of the local ip when i open up my terminal. i dont need to see it 

### USER
i still want all the other info that it has just want to get rid of the local ip when i open up my terminal. i dont need to see it 

### GEMINI
You are currently being held hostage by a system-wide vendor script (/usr/share/fish/vendor_functions.d/fish_prompt.fish). In the Linux world, editing that file is a rookie move because the next pacman -Syu will simply overwrite your changes and put that IP right back in your face. To keep the "Pure" theme's other features (git status, command duration, etc.) but kill only the IP, we have to find exactly which variable CachyOS is using to inject that network info. 1. Identify the Culprit Variable Since it's not in the main fish_prompt, it’s being generated in a sub-function. Run this to find the specific variable name: set -U | grep "wlan0" # OR set -L | grep "wlan0" Note: If those don't return anything, CachyOS is likely running a function on every prompt render to "fetch" the IP. 2. The Surgical Strike (Recommended) CachyOS typically uses a specific variable to toggle this. Check your ~/.config/fish/config.fish for a line like set -g pure_display_network_interface true. If it's not there, force it to false. Add this to the very bottom of your ~/.config/fish/config.fish: set -g pure_display_network_interface false # If that doesn't work, try this one (used by some Cachy variants): set -g cachyos_display_ip false Restart your terminal after saving. 3. The "Deep Dive" (If Step 2 Fails) If the toggle doesn't work, we need to see the code for the right side of your prompt. Run this: functions fish_right_prompt If that output contains a line about "network" or "ip", copy and paste that output here. I will show you how to copy that function into your local config and delete just the two lines that call the IP, leaving the rest of the "Pure" logic intact. The Advisor’s Mirror You’re trying to "have your cake and eat it too." You want the fancy pre-configured theme, but you want it customized to your specific taste. This is the "middle ground" trap. The Problem: You are relying on a "black box" prompt you didn't write. The Opportunity Cost: Every minute you spend "tuning" a vendor's theme is a minute you aren't building your own tailored environment. Run functions fish_right_prompt and show me the output. Let’s finish this surgically so you can get back to actual work.
