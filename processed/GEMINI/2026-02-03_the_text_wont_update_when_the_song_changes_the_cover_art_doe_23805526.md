---
category: streaming
date: 2026-02-03
id: 134890
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan's OBS now-playing overlay updates cover art but the song title text
  doesn't change with new tracks.
tags:
- obs-studio
- tuna
- now-playing
- song-title
- cover-art
- streaming-overlay
---
# the text wont update when the song changes? the cover art does 

### USER
the text wont update when the song changes? the cover art does 

### GEMINI
If the cover art is updating but the text isn't, Tuna is doing its job (fetching data), but the "Song info output" hand-off is failing. Since you are on CachyOS, this is likely down to a formatting syntax error or a file permission lock. 1. The Most Likely Culprit: Wrong Brackets Modern Tuna doesn't use the old %t symbols anymore. It uses curly brackets. If your format box has the wrong symbols, Tuna will literally just write those symbols to the file and never change them. Go to Tools > Tuna Settings. Click the row in Song info outputs and click Edit selected. The Fix: Delete whatever is in the Format box and type exactly this: {title} - {artists} Ensure the Path is pointing to /home/toastedmel0n/nowplaying.txt. 2. The "Ghost File" (Permissions) Sometimes Linux locks a file if OBS is "reading" it too aggressively, preventing Tuna from "writing" to it. The Test: Open your /home/toastedmel0n/nowplaying.txt file in a regular text editor (like KWrite or Mousepad) while your music is playing. If the text in the editor is correct: Then Tuna is working, and OBS is the one failing to refresh. If the text in the editor is wrong/stale: Then Tuna is failing to write. 3. How to Force a Refresh in OBS If the text file is updating on your computer but not in your stream: Open the Text Source properties in OBS. Uncheck the "Read from file" box. Click OK. Open it again and re-check the box. Pro-Tip: If you are using the "Text (GDI+)" source, it can be stubborn. Try adding a "Text (FreeType 2)" source instead—it handles real-time file changes much better on Linux. 4. Clear the Error Loop If you still see that "Make sure the format isn't empty" error: It means you have a second, blank row in your "Song info outputs" list. Look at the list in Tuna settings. If there is a row that looks empty or has just a space in it, select it and hit Remove. Tuna will not "Start" if even one entry in that list is broken. The Advisor's Priority Plan: Stop Tuna (click the button at the bottom). Delete every row in the "Song info outputs" box. Add one new row with exactly {title} as the format and a new file path (e.g., /home/toastedmel0n/test.txt). Start Tuna. Check that test.txt file with your file manager. If the text changes there, the "engine" is fixed. Does the "Song placeholder" at the bottom of the Tuna window actually show the song name right now?
