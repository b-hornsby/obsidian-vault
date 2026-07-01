---
category: streaming
date: 2026-02-02
id: 494448
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is having trouble getting the OBS replay buffer to start when clicking
  the OBS icon, even though it works from the command line.
tags:
- obs-studio
- replay-buffer
- streaming-setup
- command-line-interface
---
# when i run obs --startreplaybuffer it does work but when i click the obs icon it doesn't

### USER
when i run obs --startreplaybuffer it does work but when i click the obs icon it doesn't

### GEMINI
This confirms the problem: you have two different "shortcuts" for OBS. Your system is ignoring the one you edited (~/.local/share/applications/) and is instead pulling the default one from the system folder (/usr/share/applications/). In Arch-based systems like CachyOS, the desktop database needs to be told that a local override exists. The "Brute Force" Fix Since the terminal works, we know the command is correct. Let's make sure the OS actually uses your version of the shortcut. 1. Force-Update the Desktop Database Run this in your terminal: update-desktop-database ~/.local/share/applications/ This tells CachyOS: "Hey, stop looking at the system defaults, I have a custom version of OBS here." 2. Verify the Filename If it still doesn't work, the filename might be slightly off. CachyOS sometimes uses obs-studio.desktop instead of com.obsproject.Studio.desktop. Check which one exists in the system folder: ls /usr/share/applications/ | grep obs If the name is different (e.g., obs-studio.desktop), rename your local copy to match it: mv ~/.local/share/applications/com.obsproject.Studio.desktop ~/.local/share/applications/obs-studio.desktop The "Bulletproof" Alternative (The GUI Way) If you don't want to mess with files anymore, do this: Open your Application Launcher (Start menu). Right-click the OBS Studio icon. Select Edit Application... (On KDE) or Properties. Look for the Arguments or Command box. It will likely just say obs. Change it to: obs --startreplaybuffer Click OK/Save. The "High-Level Advisor" Reality Check You are currently spending time on micro-optimization. While having it auto-start is nice, don't let "setting up the perfect shortcut" become a distraction from the actual goal: recording high-quality clips. Test the actual clipping now: Launch OBS via the terminal (obs --startreplaybuffer). Open your game. Hit your Save Replay hotkey. Go to your folder and check the video. Is the video smooth, or is it choppy? If it's choppy, your CQP level or your "Preset" is too high for the background task, and we need to tune the encoder. Would you like me to tell you how to check the OBS log file to see if you're actually dropping frames during a clip?
