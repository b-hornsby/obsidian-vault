---
id: 398997
source: GEMINI
date: 2026-02-03
tags: ['file-system-search', 'index.html', 'tuna-plugin', 'permission-denied']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was searching for index.html files related to the Tuna plugin, but encountered a permission error.
---
# ~
❯ find ~ -name "index.html" | grep tuna
find: ‘/home/toastedmel0n/.cache/paru/clone/cemu-git/pkg’: Permission denied

~
❯ 

### USER
~
❯ find ~ -name "index.html" | grep tuna
find: ‘/home/toastedmel0n/.cache/paru/clone/cemu-git/pkg’: Permission denied

~
❯ 

### GEMINI
The terminal didn't return a result for Tuna because it got hung up on a permissions error in a completely different folder (cemu-git). This usually means the web templates weren't included in the specific AUR package you installed, or they are stored in the system's root directory instead of your user folder. Since you're on CachyOS (Arch), let's stop hunting for hidden files and just grab the latest official templates directly. This is faster and guarantees you get the most modern look. 1. Download the "Web" folder Run these commands in your terminal to download the official Tuna web templates into a dedicated folder in your Home directory: mkdir -p ~/obs-assets/tuna-style cd ~/obs-assets/tuna-style wget https://raw.githubusercontent.com/univrsal/tuna/master/data/web/index.html wget https://raw.githubusercontent.com/univrsal/tuna/master/data/web/style.css wget https://raw.githubusercontent.com/univrsal/tuna/master/data/web/script.js 2. Point OBS to this new folder Now that you know exactly where the files are: Open OBS. Open your Browser Source settings. Check the Local file box. Click Browse and go to /home/toastedmel0n/obs-assets/tuna-style/index.html. 3. Ensure the "Brain" is connected For that index.html to show anything other than a blank screen: Open Tuna Settings in OBS. In the Basics tab, ensure the Port is set to 1608 (matching your earlier setup). Ensure "Host/receive information on local webserver" is CHECKED. Why this is better: Permissions: You own this folder, so OBS will never have "Permission Denied" issues reading it. Customization: You can now open ~/obs-assets/tuna-style/style.css in any text editor and change colors or fonts without breaking the plugin itself. Portability: If you ever move distros, you just take your obs-assets folder with you. The Truth about Linux Streaming: You’re learning the "Arch Tax" right now. On Windows, things are bundled in installers; on Arch, you are the architect. You now have a universal music setup that will work with Soundcloud, Spotify, VLC, and YouTube all at once—something 6K Labs literally cannot do. Is the widget showing up in OBS now, or is it still appearing as a blank box?
