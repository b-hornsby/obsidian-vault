---
category: streaming
date: 2026-02-03
id: 590616
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking how to add something to his OBS Studio overlay, likely a
  visual element or data source.
tags:
- obs-studio
- overlay
- streaming
- configuration
---
# how do i add this so its on my overlay?

### USER
how do i add this so its on my overlay?

### GEMINI
Since you are on CachyOS and (presumably) have Tuna installed, you now have the data, but you need the visuals. You have two paths: the "Lazy & Ugly" way or the "Pro" way. Since you're using a high-performance distro, let's do this the Pro way. Option 1: The Web UI (Clean & Modern) Tuna comes with a built-in web server that creates a URL you can use as a Browser Source. This is the closest experience to 6K Labs. Open Tuna Settings: Tools -> Tuna settings. Go to the "Web UI" Tab: Check the box "Enable web UI". Set the Port (default is usually 16000). Click the "Open in browser" button to see if it works. Add to OBS: Add a new Browser Source to your scene. Set the URL to http://localhost:16000. Set the Width/Height (usually 400x150 or similar depending on the style). Customize it: In that same Web UI tab, you can choose different "Themes" from the dropdown. Option 2: The Text + Album Art Way (Maximum Control) If you want to design your own layout using OBS sources directly: The Text: In Tuna Settings, go to the "Output" tab. Check "Write to file" for the "Song info" section. Note the file path (it’s usually in your Documents or OBS folder). In OBS, add a Text (GDI+) or Text (FreeType2) source. Check the box "Read from file" and select the file Tuna is writing to. The Album Art: In Tuna Settings -> Output tab, find the "Cover path". Check "Save cover to file". In OBS, add an Image Source. Check the box "Unload image when not showing" (crucial so it updates when the song changes). Point it to the cover.png (or .jpg) file Tuna is generating. ⚠️ The Linux "Gotcha" (MPRIS) Since you are on CachyOS, make sure you are actually feeding Tuna data: In Tuna Settings > Basics, set the Source to MPRIS. In the MPRIS tab, you might need to click "Refresh" and select your player (e.g., chromium, spotify, or vlc) from the list. Pro-Tip: Set it to * (asterisk) if the plugin allows, or just select your primary browser. This tells Tuna to listen to the system's "Now Playing" bus. The Advisor's Mirror: Don't get stuck spending four hours pixel-pushing a song title. 6K Labs was "good enough" because it stayed out of your way. If you're going to use Tuna, set it up once, make it legible, and get back to your actual content. A fancy widget won't save a boring stream. Would you like the CSS code to make that localhost Browser Source look exactly like a minimalist Spotify pop-up?
