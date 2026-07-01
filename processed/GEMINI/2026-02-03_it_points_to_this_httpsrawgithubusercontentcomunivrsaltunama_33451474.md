---
id: 327258
source: GEMINI
date: 2026-02-03
tags: ['tuna', 'obs-studio', 'browser-source', 'github', 'now-playing']
category: streaming
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan is sharing the GitHub URL for Tuna's web index.html, likely troubleshooting the browser source path for OBS.
---
# it points to this https://raw.githubusercontent.com/univrsal/tuna/master/data/web/index.html

### USER
it points to this https://raw.githubusercontent.com/univrsal/tuna/master/data/web/index.html

### GEMINI
Those "search.html" files in your folder are garbage—they are just the results of a Google search page you accidentally saved instead of the actual code. This is why your widget looks like a wall of text or a broken webpage. To fix this right now, we are going to bypass the "save as" struggle and use the raw code itself. 1. Fix the "Host" Setting (Crucial) In your first screenshot, the "Host/receive information" box was unchecked. If that is off, nothing else works. Go to Tools > Tuna Settings. Check the box "Host/receive information on local webserver with port:". Set the port to 1608. Click Start at the bottom of the Tuna window. 2. The "Nuclear Option" (Direct CSS) Since your local files are currently broken, do this to get a clean look instantly without needing the index.html file: In OBS, double-click your Browser Source. Uncheck "Local file". In the URL box, type: http://localhost:1608 Scroll down to the Custom CSS box. Delete everything inside it and paste this exact code: body { background-color: rgba(0, 0, 0, 0.8); color: #fff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; padding: 20px; border-radius: 15px; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; overflow: hidden; } /* This hides the JSON brackets and quotes */ pre { white-space: pre-wrap; font-weight: bold; font-size: 1.5em; } /* This forces the cover image to show up if Tuna is sending it */ img { max-width: 100px; border-radius: 10px; margin-bottom: 10px; } 3. Why the "search.html" failed you: When you "Saved Page As" from GitHub or Google, you saved the webpage layout of GitHub, not the raw text of the plugin. That's why your folder has files starting with "search" instead of "index". The Strategy: The CSS hack above treats the raw JSON data like a design. It’s the fastest way to get your stream looking professional without you having to fight the Linux file system any longer. Once you paste that CSS and hit OK, does the wall of text turn into a centered, dark box with your song info?
