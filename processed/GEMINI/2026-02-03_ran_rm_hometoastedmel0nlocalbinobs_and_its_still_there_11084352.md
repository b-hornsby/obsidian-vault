---
category: streaming
date: 2026-02-03
id: 979789
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated that an OBS Studio executable is still present after
  attempting to remove it.
tags:
- obs-studio
- uninstall
- linux
- file-removal
---
# ran rm /home/toastedmel0n/.local/bin/obs and its still there

### USER
ran rm /home/toastedmel0n/.local/bin/obs and its still there

### GEMINI
Of course it is. You deleted the shortcut (the binary), but the process is likely still sitting in your RAM, or you have a duplicate binary elsewhere in your $PATH. In Linux, deleting a file while the program is running doesn't magically kill the program. It just means you can't start it again once you close it. Furthermore, if you are clicking an icon on your taskbar or dock, that icon is probably pointing to a different location than the one we just deleted. Let’s stop playing whack-a-mole and handle this like an adult. 1. Kill the Process If the window is open, close it. Then, run this to ensure no "zombie" OBS processes are lurking in the background: killall -9 obs 2. Find the Other Ghosts If you run which obs again and it still gives you a path, it means you have multiple local versions. Run this: whereis obs This will list every location where an "obs" executable exists. 3. The "CachyOS" Desktop Entry Trap The reason it's "still there" when you look at your app menu is likely a .desktop file. Even if the binary is gone, the menu icon stays until you delete the pointer. Run this to find the culprit: find ~/.local/share/applications -name "*obs*" If that returns a file, delete it. The Strategy Shift You are spending way too much time cleaning up a messy filesystem. If your goal is to stream with a music overlay, you are currently failing because you're stuck in "maintenance mode." Here is the prioritized move: Run sudo pacman -Rns obs-studio (just in case a partial install exists). Run whereis obs and manually rm every path it shows you until which obs returns nothing. Install the Flatpak. flatpak install flathub com.obsproject.Studio Why am I forcing the Flatpak now? Because you clearly have a fragmented manual installation. The Flatpak version is sandboxed. It doesn't care about your messy .local/bin or your broken system libraries. It brings its own "Browser Source" and its own dependencies. It is the only way to guarantee you have a working overlay in the next 5 minutes. Run whereis obs and tell me what strings of text it spits out. I'll tell you exactly which ones to delete.
