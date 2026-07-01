---
category: homelab
date: 2026-02-17
id: 792827
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is indicating that a file is still present despite attempts to remove
  it, suggesting a file system issue.
tags:
- linux-troubleshooting
- file-system
- ghost-file
---
# theres still a ghost file?

### USER
theres still a ghost file?

### GEMINI
That "ghost" is a leftover desktop entry. Since you've already confirmed the binary is gone (the icon is a generic document, not the OBS logo), your system is just holding onto a link to a file that no longer exists. Quit playing whack-a-mole with commands and just delete the entry. 1. The Instant Fix (Terminal) The most likely culprit is a .desktop file hiding in your user's local applications folder. Run this to nuke it: rm ~/.local/share/applications/com.obsproject.Studio.desktop If that says "No such file," try: rm ~/.local/share/applications/obs-studio.desktop 2. The Systematic Search If it's still there, you have a rogue file in one of two places. Use these commands to find exactly where it's hiding: ls ~/.local/share/applications | grep obs ls /usr/share/applications | grep obs Once it spits out the name, delete it using rm (for the first location) or sudo rm (for the second). Why this happened (The Blind Spot) You likely installed this via a method that didn't register with pacman (like a manual script, a third-party installer, or an AppImage that "integrated" itself). Your package manager can't clean up what it didn't track. Opportunity Cost: You're spending minutes hunting a shortcut file. Clean it manually and move on. Should I show you how to find and kill the actual configuration folders so you don't have hidden "settings" bloat taking up space, too?
