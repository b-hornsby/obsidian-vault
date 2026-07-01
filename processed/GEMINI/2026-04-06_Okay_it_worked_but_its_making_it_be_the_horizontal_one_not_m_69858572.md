---
category: streaming
date: 2026-04-06
id: 760222
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan got a workaround working but it was outputting horizontal instead of
  the vertical format needed for TikTok.
tags:
- obs
- vertical-stream
- aspect-ratio
- tiktok
- orientation
---
# Okay it worked but it’s making it be the horizontal one not my vertical one?

### USER
Okay it worked but it’s making it be the horizontal one not my vertical one?

### GEMINI
The reason you're seeing the horizontal feed is that the "Main Output" in OBS NDI settings defaults to your primary (16:9) canvas. Because the Aitum Vertical plugin creates a completely separate second canvas, it requires a "Dedicated NDI Output" to send that specific vertical feed to TikTok. Here is how to point the NDI signal specifically at your vertical setup: 1. Add the NDI Filter to your Vertical Scene This is the "secret" to separating the two feeds: In your Vertical Scenes list, find the one you're using (e.g., "fps games"). Right-click the scene name and select Filters. Click the + icon to add a new filter and select Dedicated NDI Output. Give it a distinct name like OBS-Vertical. Close the filter window. (This starts "broadcasting" the vertical scene over NDI). 2. Update the NDI Webcam App Now you need to tell the receiver to listen to that new "Vertical" signal: Find the NDI Webcam (or Virtual Input) icon in your Windows system tray (bottom right, near the clock). Right-click the icon. Hover over your PC name. You should now see two options: your main OBS output and the new OBS-Vertical output you just created. Select OBS-Vertical. 3. Check TikTok Live Studio TikTok Live Studio should instantly switch from your horizontal gameplay to your vertical Aitum layout. The Advisor's Strategic Check If it looks "squished" or has black bars: Resolution Check: Go to your Aitum Vertical Settings (the gear icon in the vertical dock) and ensure your Base Resolution is set to 1080x1920 (not 1920x1080). Frame Rate: Make sure both your main OBS and your Vertical settings are at 60 FPS. If they are different, NDI will stutter like crazy. Why this is the "final boss" of fixes: By using a Dedicated NDI Filter, you are telling your GPU to take that specific vertical "slice" of memory and send it directly to TikTok. This is way more efficient than the "Virtual Camera" button, which tries to force everything through a single, generic Windows driver. Is the vertical alignment looking correct in TikTok now, or is it trying to stretch the image?
