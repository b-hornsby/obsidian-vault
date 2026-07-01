---
category: streaming
date: 2026-02-03
id: 772352
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan can't find the index.html file in the Tuna-style folder for his OBS
  browser source configuration.
tags:
- tuna
- obs-studio
- browser-source
- file-path
- now-playing
---
# the index html isnt in tuna-style but the folder is there?

### USER
the index html isnt in tuna-style but the folder is there?

### GEMINI
The permission error you saw is just your system complaining about unrelated folders—it didn't actually "fail" the search, it just didn't find anything in your user directory. If the folder ~/obs-assets/tuna-style is empty after you ran those wget commands, it’s because wget likely failed to connect to the raw GitHub links or didn't save them where you expected. Let’s skip the terminal struggle and do this via your Browser and File Manager (Dolphin/Thunar). This is foolproof. 1. Download the files manually Open these three links in your browser. For each one, Right Click -> Save Page As... (make sure the file extension stays .html, .css, and .js): index.html style.css script.js Put all three files into that ~/obs-assets/tuna-style folder you created. 2. Add to OBS (The Local File Way) Open OBS. Double-click your Browser Source. Check the box Local file. Click Browse and select the index.html you just saved. Set Width to 600 and Height to 300. Click OK. 3. The "Communication" Check If the box is still blank, it means the widget can't "see" the Tuna plugin's data. Go to Tools -> Tuna Settings. In the Basics tab: Make sure Port is 1608. Make sure "Host/receive information on local webserver" is CHECKED. In the MPRIS tab: Make sure your music player (Spotify, Soundcloud, etc.) is selected and showing a song title at the bottom of the Tuna window. Why this is happening: The index.html file acts as a "receiver." It looks for data at localhost:1608. If the file is missing from the folder, OBS shows nothing. If the file is there but the "Host" box in Tuna isn't checked, the file shows nothing. The Advisor's Pivot: If you look in your tuna-style folder and see those three files, but OBS is still blank, it's almost certainly the Port number. Does the Tuna Settings window currently show a song title at the very bottom? If it doesn't, we need to fix the MPRIS connection before the overlay will ever work.
