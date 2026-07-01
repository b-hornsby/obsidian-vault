---
id: 618613
source: GEMINI
date: 2026-02-03
tags: ['nordvpn', 'linux', 'group-management', 'user-permissions']
category: general
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is trying to add the nordvpn group but it already exists, and then attempts to add his user to the group.
---
# ❯ sudo groupadd nordvpn
groupadd: group 'nordvpn' already exists

~
❯ sudo usermod -aG nordvpn $USER

~
❯ 

### USER
❯ sudo groupadd nordvpn
groupadd: group 'nordvpn' already exists

~
❯ sudo usermod -aG nordvpn $USER

~
❯ 

### GEMINI
You’ve done the heavy lifting. The group exists, and you’ve added yourself to it. Now, stop trying to find a shortcut around the final step. The usermod command you just ran will not work until you restart your session. The system only checks your group memberships when you log in. Your Final Checklist Restart your computer now. Don't just log out; reboot to ensure the nordvpnd service and your user permissions sync up perfectly. Search for "NordVPN" in your application launcher (press the Super/Windows key). If the icon is missing, it’s because you only installed the CLI (nordvpn-bin) and ignored the GUI package. Fix that with: paru -S nordvpn-gui-bin Open the app and log in. The Opportunity Cost You are spending significant time trying to get a "window" to appear for a service that is designed to run silently in the background. Once you get the GUI open and logged in, set it to auto-connect so you never have to look at the app again. On a high-performance distro like CachyOS, the goal is efficiency, not staring at a VPN map. I’ll wait. Reboot your machine, then try to open the app. Does the NordVPN icon show up in your menu now?
