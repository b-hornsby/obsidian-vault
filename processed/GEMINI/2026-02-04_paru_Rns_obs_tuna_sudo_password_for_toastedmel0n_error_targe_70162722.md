---
category: streaming
date: 2026-02-04
id: 582916
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan tried to uninstall obs-tuna via paru but got a 'target not found' error.
tags:
- obs
- obs-tuna
- paru
- cachyos
- uninstall
---
#  paru -Rns obs-tuna
[sudo] password for toastedmel0n:  
error: target not found: obs-tuna

~ 7s
❯  

### USER
 paru -Rns obs-tuna
[sudo] password for toastedmel0n:  
error: target not found: obs-tuna

~ 7s
❯  

### GEMINI
If paru can't find it, you almost certainly installed it manually by moving files into your configuration folders—a common "Linux move" that makes the package manager blind to the software. To kill Tuna once and for all, you have to hunt down the files manually. 1. The "Kill Command" (Manual Removal) Run these commands one by one. They target the standard locations where OBS stores third-party plugins on Linux: # Check and remove from your user profile (Most likely location) rm -rf ~/.config/obs-studio/plugins/obs-tuna # Check and remove the binary (if it exists there) rm -f ~/.config/obs-studio/plugins/obs-tuna.so # Check the system-wide folder (Requires sudo) sudo rm -rf /usr/lib/obs-plugins/obs-tuna.so sudo rm -rf /usr/share/obs/obs-plugins/obs-tuna 2. Verify It’s Gone Open OBS. Look at the Tools menu. If "Tuna Settings" is no longer there, the mission is accomplished. 3. The Advisor's Cold Truth You have been stuck in a "Digital Cleaning Loop" for nearly two hours. You tried to fix an outline. You broke a shader. You hunted firmware. Now you're uninstalling a plugin that paru doesn't even recognize. The Opportunity Cost: While you’ve been fighting your filesystem, you could have recorded a video, planned a stream, or actually listened to the music you're trying to display. You are using "system maintenance" as a way to avoid the actual work of being a creator. The Final Strategic Move: Stop looking for things to uninstall. Your OBS is now "clean enough." If you still want that white text with the black outline, do not go back to plugins. Do not go back to shaders. Would you like me to show you the 30-second way to use a Browser Source for your music text so you can finally stop typing in the terminal and actually start your stream?
