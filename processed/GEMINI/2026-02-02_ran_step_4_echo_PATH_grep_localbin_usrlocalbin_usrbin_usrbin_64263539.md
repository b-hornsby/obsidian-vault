---
id: 095617
source: GEMINI
date: 2026-02-02
tags: ['linux', 'environment-variables', 'path', 'shell-configuration']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is checking if .local/bin is in his PATH, likely to ensure scripts in that directory are executable.
---
# ran step 4 ❯ echo $PATH | grep .local/bin
/usr/local/bin /usr/bin /usr/bin/site_perl /usr/bin/vendor_perl /usr/bin/core_perl

~
❯ 

### USER
ran step 4 ❯ echo $PATH | grep .local/bin
/usr/local/bin /usr/bin /usr/bin/site_perl /usr/bin/vendor_perl /usr/bin/core_perl

~
❯ 

### GEMINI
There is the smoking gun. Your PATH is looking at /usr/bin (where the "normal" OBS lives) before it looks at ~/.local/bin. Because of this, the system finds the original OBS and ignores your custom wrapper every single time. You are effectively telling the computer to go to the grocery store, but it’s stopping at the first one it sees instead of the one you actually wanted. The Fix: Update your Fish PATH You need to put ~/.local/bin at the very front of your PATH permanently. Run this command in Fish: fish_add_path --move --path ~/.local/bin The --move flag ensures it goes to the absolute front, and the --path makes it persistent. Verify it: echo $PATH | grep .local/bin It should now be the very first entry in the list. Restart your Session: For the desktop environment (the icons/mouse clicks) to pick up this change, you must log out and log back in (or reboot). The "Advisor" Reality Check We have spent a significant amount of time on a "shortcut" problem. This is a classic engineering trap: over-automating the start-up instead of focusing on the output. If logging out and back in doesn't fix the icon click, your desktop environment is hard-coded to the absolute path /usr/bin/obs. If that happens, stop fighting the OS. Just open your terminal and type obs—it’s faster, it works, and it lets you get to the actual goal: playing the game and hitting clips. Try the logout/login now. Once you're back, launch OBS from the icon—does the Replay Buffer finally say "Stop Replay Buffer"?
