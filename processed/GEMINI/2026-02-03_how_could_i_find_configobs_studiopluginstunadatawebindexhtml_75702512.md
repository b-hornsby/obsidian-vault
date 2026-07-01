---
category: streaming
date: 2026-02-03
id: 875500
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was trying to locate the index.html file for the Tuna plugin within
  the OBS Studio configuration directory.
tags:
- file-system-search
- obs-studio
- tuna-plugin
- index.html
---
# how could i find ~/.config/obs-studio/plugins/tuna/data/web/index.html

### USER
how could i find ~/.config/obs-studio/plugins/tuna/data/web/index.html

### GEMINI
Finding that file path on Linux can be a pain because ~/.config is a "hidden" directory (indicated by the dot), and depending on how you installed OBS (AUR vs. Flatpak), the files could be in two completely different places. Since you're on CachyOS, let's find it the "Arch way" so you can stop guessing. Step 1: Locate the file via Terminal Open your terminal and run this command. It will search your entire home directory for any file named index.html associated with Tuna: find ~ -name "index.html" | grep tuna Step 2: Where it likely is Based on common Arch/CachyOS installations, check these two specific paths in your File Manager (Dolphin/Thunar): If you installed via AUR (yay or paru): ~/.config/obs-studio/plugins/tuna/data/web/index.html If you accidentally used the Flatpak version: ~/.var/app/com.obsproject.Studio/config/obs-studio/plugins/tuna/data/web/index.html Note: To see the .config or .var folders in your file manager, you must press Ctrl + H to "Show Hidden Files." Step 3: How to actually add it to your overlay Once you find that index.html file, do not just copy the path. Follow these steps in OBS to make the widget appear: Add a Browser Source in OBS. Check the box "Local file". Click Browse and navigate to the file you just found. Set the Width to 600 and Height to 200 (you can adjust this later). The Secret Sauce: If it still looks like just text, look at the Tuna Settings > Web UI tab in OBS. Make sure "Enable Web UI" is checked. The index.html file is basically a "skin" that sucks the data out of that localhost:1608 link you saw earlier. The Advisor's Shortcut: If you can't find the file or it's missing (sometimes the AUR package doesn't include the web templates), you can just download the official "web" folder from the Tuna GitHub, put it anywhere in your Home folder, and point the Browser Source to that index.html. If you find the file but it looks "broken" or "ugly" when you load it, would you like a 5-line CSS snippet to make it look like a clean, modern pop-up?
