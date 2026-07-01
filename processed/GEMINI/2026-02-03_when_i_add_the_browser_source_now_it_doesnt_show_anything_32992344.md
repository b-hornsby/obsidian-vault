---
category: streaming
date: 2026-02-03
id: 820173
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is troubleshooting why his browser source in OBS Studio is not displaying
  anything.
tags:
- obs-studio
- browser-source
- streaming-setup
- troubleshooting
---
# when i add the browser source now it doesnt show anything?

### USER
when i add the browser source now it doesnt show anything?

### GEMINI
In your final screenshot, the browser source is showing "status": "unknown" and blank title fields. This means the communication loop is active, but your music player is no longer "talking" to the Tuna plugin. Here is how to get the text scrolling and the art visible right now: 1. Reconnect the "Brain" (MPRIS) Because you are on CachyOS, Tuna needs to be told exactly which app to listen to. Go to Tools > Tuna Settings. Click the MPRIS tab. Look for your player (SoundCloud, Spotify, or your Browser) in the list. Select it. Look at the bottom of the Tuna window—if it doesn't show a song title there, the overlay will stay blank. 2. Fix the Scrolling Text To get the text moving across the screen, use the OBS Scroll Filter: Right-click your "now playing" text source in the OBS source list. Go to Filters > + > Scroll. Set Horizontal Speed to about 50-80. The Crucial Trick: Go back to your Tuna Song info outputs. Edit the format to include a bunch of spaces at the end: {title} - {artists} . This prevents the end of the song from touching the beginning as it loops. 3. Add the Album Art Image Since your "web" files were broken, don't use the browser source for the picture. Use an Image Source: Click + in OBS > Image. Browse to /home/toastedmel0n/cover.png. Check the box "Unload image when not showing". This forces OBS to update the picture every time the song changes. Why it shows "Unknown": Your last screenshot shows the server is running, but it has no data. This happens if you closed your browser tab or if the MPRIS tab in Tuna lost track of the player. The Precision Plan: Play a song in your browser. In Tuna settings, click Stop then Start to refresh the connection. Check the MPRIS tab to ensure your browser is the active source. Would you like me to give you a CSS code snippet to hide the "JSON brackets" in your browser source so it only shows the clean text?
