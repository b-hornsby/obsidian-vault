---
category: general
date: 2026-02-03
id: 330954
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/topics/tech/coding.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan is likely listing the contents of a folder, possibly for troubleshooting
  or documentation.
tags:
- coding
- ''
- ''
- ''
- ''
- ''
---
# this is whats in the folder 

### USER
this is whats in the folder 

### GEMINI
In your second screenshot, you are seeing raw JSON data because you are viewing the source data directly rather than through a visual "skin". In the fourth screenshot, the files you downloaded are named search.html, search.css, and search.js—this is likely because you "Saved Page As..." from a Google search result instead of the direct raw file links. To fix this and get the actual widget visible, you need to rename those files so they can "talk" to each other properly. 1. Rename the files in Dolphin Your HTML file is looking for its styling in a file called style.css, but your file is named search.css. They won't connect until you fix the names. Open your ~/obs-assets/tuna-style folder and rename them exactly like this: search.html → index.html search.css → style.css search.js → script.js 2. Update the OBS Browser Source Double-click your Browser Source in OBS. Ensure "Local file" is checked. Click Browse and select your newly renamed index.html. Set the Width to 600 and Height to 300. 3. Activate the "Brain" In your first screenshot, the box "Host/receive information on local webserver with port" is unloaded/unchecked. Go to Tools > Tuna Settings. Check the box "Host/receive information on local webserver with port:". Ensure the port is set to 1608. Click Start at the bottom of the Tuna window. Why this is the "final step": The Problem: The index.html file is a script that "grabs" the data from localhost:1608 and uses style.css to make it look pretty. The Status: You have the data (the JSON wall), and you have the "skin" (the renamed files). Checking that "Host" box is the final handshake that lets the skin see the data. The Advisor's Mirror: You’ve done the hard work of switching to a universal Linux setup. Don't let a few misnamed files stop you now. Rename those files, check that "Host" box, and your music widget will finally look professional. Is the widget now showing the song title and album art instead of the code?
