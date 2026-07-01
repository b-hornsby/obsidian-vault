---
category: homelab
date: 2026-02-04
id: 192580
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is experiencing an issue where audio playback stops when switching
  between Spotify and SoundCloud on CachyOS.
tags:
- spotify
- soundcloud
- audio-playback
- cachyos
- audio-switching
- troubleshooting
---
# every time i switch between spotify or soundcloud it stops working?

### USER
every time i switch between spotify or soundcloud it stops working?

### GEMINI
When you switch between Spotify and SoundCloud, your song-ticker app updates the text file. Every time that text file changes, OBS re-renders the text source, which forces the shader to recompile. On Linux, the obs-shaderfilter is notoriously sensitive to these "dynamic updates". If the text length changes or the source re-activates, the shader loses its reference to the texture size (uv_size) or fails to re-initialize the variables, causing the "No song playing" text to go blank or the outline to vanish. Why it's breaking: Re-compilation Lag: The shader has to "re-build" every time a new song title appears. If the compiler hits a hiccup during that rapid switch, it fails silently. Variable Reset: When the text source refreshes, it may momentarily report a size of 0x0 pixels, causing the shader math to divide by zero and break. The Final, Brutal Solution: Stop using Shaders You are trying to use a high-performance gaming technique (Shaders) to put an outline on a simple text file that changes every 3 minutes. It's like using a jet engine to power a lawnmower—it's over-engineered and prone to exploding. Do this instead (The "Browser Source" fix): Stop using the Text (FreeType 2) source for your song titles. Add a Browser Source in OBS. Set the URL to the local path of your song text file (e.g., file:///home/user/Documents/current_song.txt). In the Custom CSS box at the bottom, paste this: body { color: white; font-family: Arial, sans-serif; font-weight: bold; font-size: 40px; /* This creates a perfect, unbreakable black outline */ text-shadow: -2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000, 2px 2px 0 #000; } Why this is the "Pro" move: Zero Crashes: Browsers handle text updates perfectly without re-compiling code. OS Independent: It doesn't care that you're on CachyOS; it uses the standard Chromium engine built into OBS. Dynamic: When the text file changes, the browser updates the view instantly and keeps the outline intact. Would you like me to help you find the exact file path for your Spotify/SoundCloud text file so you can set this up in 30 seconds?
