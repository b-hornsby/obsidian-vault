---
id: 051530
source: GEMINI
date: 2026-02-02
tags: ['shell-script', 'blue-yeti', 'microphone', 'script-name', 'linux']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is stating the name of his Blue Yeti reset script, likely in response to a question about its name.
---
# its called reset_yeti.sh

### USER
its called reset_yeti.sh

### GEMINI
Go ahead and run cat ~/reset_yeti.sh and paste the contents here. Why we need to look at it: I’m willing to bet that script is using a hardcoded path (like /sys/bus/usb/devices/1-1/). If you plugged the mic into a different USB port since you wrote that script, or if CachyOS updated its kernel and re-indexed your USB tree, that script is currently "resetting" an empty port while your Yeti sits ignored on a different one. The Strategy: The Audit: We check if the path in the script matches where the Yeti is currently sitting (which we saw earlier was 1-3). The Upgrade: I'll help you modify the script so it searches for the Yeti by its ID (046d:0ab7) instead of a fixed port. This makes the script "smart"—it won't matter which USB port you use or how the system boots; it will find the mic and kick it. The Permission: We need to make sure you have the sudo rule set up so this script can run at boot without asking you for a password (since you won't be there to type it while the system is initializing). Paste the code from reset_yeti.sh. Let's see how "dumb" or "smart" it currently is.
