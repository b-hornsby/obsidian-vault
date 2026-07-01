---
id: 031818
source: GEMINI
date: 2026-02-03
tags: ['obs-studio', 'command-line', 'path-resolution', 'uninstall']
category: streaming
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is attempting to uninstall OBS Studio by removing the executable and killing any running processes, but is having trouble locating all instances.
---
# ❯ which obs
/home/toastedmel0n/.local/bin/obs

~
❯ rm /home/toastedmel0n/.local/bin/obs

~
❯ killall -9 obs
obs: no process found

~
❯ whereis obs
obs:

~
❯ 

### USER
❯ which obs
/home/toastedmel0n/.local/bin/obs

~
❯ rm /home/toastedmel0n/.local/bin/obs

~
❯ killall -9 obs
obs: no process found

~
❯ whereis obs
obs:

~
❯ 

### GEMINI
Look at that: Silence. You finally won the war against the ghost binaries. whereis obs returning a blank entry means your system is officially clean. No more zombies, no more local overrides. Now, stop dancing around the solution. You have a clean slate on CachyOS. You have two choices to get that Browser Source working so you can finally add your music overlay. Option A: The "Optimized" Native Route (Fastest Performance) Since you're on CachyOS, you probably want the performance edge. Try the official repo first, but do it right: sudo pacman -Syu obs-studio After it installs, run which obs. It should now say /usr/bin/obs. Open it. If the Browser Source is there, you're done. Go set up Amuse or Snip. Option B: The "I Just Want it to Work" Route (Most Reliable) If you install the native version and the Browser Source is still missing (which happens on Arch-based distros if CEF is being temperamental), don't waste another second debugging. Use the Flatpak. It is a self-contained tank. flatpak install flathub com.obsproject.Studio The Next Level Once you have OBS open and you see "Browser" in the sources list: Go to 6K Labs Amuse. Connect your Spotify. Copy the Widget URL. In OBS, click + -> Browser. Paste the URL and set the width/height to what Amuse recommends (usually 600x200 or similar). Which path are you taking? Run the pacman command now and tell me if "Browser" shows up in the source list. If it doesn't, we are going Flatpak and never looking back.
