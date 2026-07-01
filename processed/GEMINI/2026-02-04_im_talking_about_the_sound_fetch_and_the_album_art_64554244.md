---
id: 248769
source: GEMINI
date: 2026-02-04
tags: ['sound-fetch', 'album-art', 'music', 'cachyos', 'troubleshooting']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan clarified he was referring to sound fetch and album art functionality, likely in a music or media app context.
---
# im talking about the sound fetch and the album art

### USER
im talking about the sound fetch and the album art

### GEMINI
On CachyOS (Linux), you’re likely using MPRIS (the Linux standard for media control) to fetch that data. When you switch between Spotify and SoundCloud, the "owner" of the data changes, and the temporary files (the text and the album art image) are being deleted or overwritten. Because you are using Shaders, OBS has to re-calculate the math for the new image/text size every single time. If the file is missing for even a millisecond during the switch, the shader crashes or goes blank. Stop using the "Internal OBS Source + Shader" method. It is too fragile for a dynamic Linux setup. The "Bulletproof" Way: Tuna Plugin Since you're on an Arch-based distro, you have access to the best tool for this: Tuna. It is designed to handle Spotify, SoundCloud, and local players on Linux without breaking. Install Tuna: paru -S obs-tuna Configure in OBS: Go to Tools -> Tuna Settings. Set your source to MPRIS (this covers both Spotify and SoundCloud). In the "Basics" tab, tell it where to save the cover_art.png and current_song.txt. Add to OBS: Image Source: Point it to the cover_art.png Tuna is saving. Browser Source (For Text): Instead of a Text source, add a Browser Source. The Outline Fix: Use the CSS below in that Browser Source. It will never "stop working" or error out when you change songs. The CSS for Your Text (Paste into Browser Source) body { color: white; font-family: 'Your Font Name', sans-serif; font-weight: bold; font-size: 36px; /* This creates a high-quality black outline that won't break like shaders */ text-shadow: -2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000, 2px 2px 0 #000, 0px 0px 8px rgba(0,0,0,0.8); } Why this fixes your problem: Tuna acts as a stable middleman. It waits for the new album art to download before updating the file, so OBS never sees a "missing" image. Browser Sources don't use the GPU shader pipeline in the same way; they use standard web rendering which doesn't "crash" or throw Unexpected EOF errors when the text changes length. The Brutal Truth: You’ve spent more time debugging a shader than it takes to set up a professional-grade plugin. Switch to Tuna and the Browser Source method, and you’ll never have to look at a shader error code again. Do you want the terminal commands to find exactly where Spotify/SoundCloud are storing their album art if you don't want to use Tuna?
