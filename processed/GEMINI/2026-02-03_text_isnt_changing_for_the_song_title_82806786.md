---
category: streaming
date: 2026-02-03
id: 200680
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan's OBS now-playing overlay isn't updating the song title text when the
  track changes.
tags:
- obs-studio
- tuna
- now-playing
- song-title
- streaming-overlay
---
# text isnt changing for the song title?

### USER
text isnt changing for the song title?

### GEMINI
If the song title isn't changing, it's usually because Tuna is "ghosting" the file—it either isn't writing to it, or OBS has stopped listening to it. Since you're on CachyOS, we need to verify the handshake between the music player and the file. 1. The "Basics" Check Go to Tools > Tuna Settings and look at the very bottom of the window. Is a song title actually showing there? * No: Your MPRIS connection is broken. Go to the MPRIS tab and make sure your player (SoundCloud/Spotify) is selected. Yes: Tuna "knows" the song, but it isn't "saying" it to the file. 2. Fix the "Output" Configuration In the Basics tab, look at your Song info outputs list. You need an entry that looks like this: Path: /home/toastedmel0n/nowplaying.txt Format: {title} - {artist} (You must use the curly brackets {}. If you just type %t, it will literally just display "%t" and never change). Click Stop, then click Start at the bottom of the Tuna window to force a refresh. 3. Kickstart the OBS Text Source OBS sometimes "caches" a text file and refuses to check for updates. Open your Text Source properties in OBS. Uncheck "Read from file", click OK, then open it again and re-check it. Pro Tip: If you're using Text (GDI+), there is no "refresh" button, but if you use Text (FreeType 2) (common on Linux), it's more stable for real-time file updates. 4. Permission Check (The Linux Special) If Tuna says it's writing but the file nowplaying.txt never changes when you open it in a text editor: It might be a permission issue. Try changing the output path to your Documents folder instead of a hidden config folder. Run this in terminal: touch ~/nowplaying.txt to create the file manually, then point Tuna to that specific file in your home directory. The Advisor's Diagnostic: If the Album Art is changing but the Text isn't, the problem is 100% your Format string. You likely have it set to a static word or a broken placeholder. The Priority Fix: Change the format string in Tuna to {title}. Just that. Hit Start, and check if the text file in your folder actually updates. Does the Tuna window itself show the correct song title at the bottom right now?
