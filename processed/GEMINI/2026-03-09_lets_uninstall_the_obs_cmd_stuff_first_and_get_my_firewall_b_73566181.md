---
id: 661148
source: GEMINI
date: 2026-03-09
tags: ['obs-cmd', 'firewall', 'uninstall', 'troubleshooting', 'streaming-setup']
category: streaming
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md', 'nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/streaming-rig.md']
summary: Bryan is deciding to uninstall obs-cmd and reset his firewall configuration, likely to troubleshoot issues.
---
# lets uninstall the obs-cmd stuff first and get my firewall back in order

### USER
lets uninstall the obs-cmd stuff first and get my firewall back in order

### GEMINI
Smart. You're cleaning the "technical debt" before it piles up. Let’s revert the changes so your system is back to a clean, secure state before we try the next method. 1. Reverting the Firewall Since we only opened one port, we’ll close it and verify the status. sudo ufw delete allow 4455/tcp sudo ufw status It should show "active" but 4455 should no longer be in the list. 2. Uninstalling obs-cmd Since you installed it via paru, we’ll remove the binary and the configuration files you created. # Remove the package paru -Rs obs-cmd # Delete the config directory we created rm -rf ~/.config/obs-cmd 3. Cleaning the "Fish" Environment If you added any environment variables to your Fish config (the set -gx commands we discussed), you should remove them. Open the config: micro ~/.config/fish/config.fish Delete any lines containing OBS_WS_PASSWORD or OBS_WS_ADDRESS. Save and exit (Ctrl+Q or Ctrl+S in micro). The Advisor's Mirror: Why This Failed We hit a "Permission/Handshake" loop. In a "vibe coding" workflow, it's easy to keep throwing code at a problem until it sticks, but on Linux, security layers (UFW + Wayland + WebSockets) often act as a triple-lock. You were fighting three different systems at once. By cleaning this up, you're ensuring that your "Operation Immortal Agent" and your gaming performance aren't being dragged down by a ghost configuration that doesn't even work. The Next Move Once you’ve run those commands, your system is back to baseline. Would you like me to walk you through the obs-wayland-hotkeys installation now, or do you want to verify your firewall status one last time first?
