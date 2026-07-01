---
id: 572212
source: GEMINI
date: 2026-02-03
tags: ['troubleshooting', 'configuration', 'unexpected-output']
category: general
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
summary: Bryan is describing that a field or output isn't blank but contains something unexpected.
---
# its not blank but its this 

### USER
its not blank but its this 

### GEMINI
That text wall is the raw "JSON" data. It proves Tuna is successfully "hearing" your music, but you haven't given OBS the "skin" to dress that data up. Since you can see the text, your local server is working. Now we just need to apply the visual layer. The 2-Minute Fix: Use a Pre-made "Skin" The files you downloaded (or are looking for) act as a translator that turns that code into a widget. Open your Browser Source properties in OBS. Check the box "Local file". Browse to that index.html file you just saved in ~/obs-assets/tuna-style/. Crucial: Ensure the style.css and script.js files are in that same folder. The HTML file needs them to know how to look. If it’s STILL just showing text: If you point OBS to the index.html and it still looks like a wall of code, the "skin" is failing to load its instructions. Try this Custom CSS hack to force a clean look without needing external files: Keep your Browser Source URL as http://localhost:1608. Scroll down to the "Custom CSS" box at the bottom of the Browser Source settings. Delete everything in that box and paste this: body { background-color: rgba(0, 0, 0, 0.7); color: white; font-family: sans-serif; padding: 15px; border-radius: 10px; overflow: hidden; } /* This hides the raw JSON "brackets" and just shows the title/artist */ pre { white-space: pre-wrap; word-wrap: break-word; font-size: 1.2em; } The Brutal Advisor's Mirror: You are currently staring at the engine of a car and complaining that it doesn't look like a Ferrari. The JSON you see is the engine. The Priority Plan: Step 1: Verify those three files (index.html, style.css, script.js) are all together in ~/obs-assets/tuna-style/. Step 2: Point the Local File Browser Source to that index.html. Step 3: If it’s still ugly, use the "Text Source" method (Method 3 from my last message). It’s less "webby" but 100% reliable on Linux. Does the widget change at all when you check "Local file" and select that index.html?
