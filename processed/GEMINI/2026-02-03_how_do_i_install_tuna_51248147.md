---
category: streaming
date: 2026-02-03
id: 037876
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking how to install the Tuna plugin, likely for OBS Studio.
tags:
- tuna-plugin
- obs-studio
- installation
- streaming
---
# how do i install tuna?

### USER
how do i install tuna?

### GEMINI
Installing Tuna isn't as simple as pasting a URL into a browser source, which is exactly why most streamers avoid it—and why their setups remain basic. It requires manual file placement, but once it’s in, it’s bulletproof. Follow these steps precisely. Do not skip the dependency check or it will fail to load. Phase 1: Preparation Before touching the plugin, you need the OBS WebSocket. If you are on OBS 28 or higher, this is already built-in. If you are on an ancient version of OBS, update it. You’re wasting your own time troubleshooting outdated software. Phase 2: The Installation Download: Go to the Tuna GitHub Releases page or the OBS Forums. Download the .zip version for Windows (usually labeled tuna-VERSION-windows-x64.zip). Locate OBS: Find where your OBS is installed. Usually: C:\Program Files\obs-studio. Extract and Merge: * Open the Tuna .zip file. You will see folders named data and obs-plugins. Drag and drop these directly into your main obs-studio folder. Crucial: When Windows asks if you want to replace or merge folders, say Yes. You aren't deleting OBS; you are injecting the plugin files into the existing directories. Phase 3: Configuration (The Strategic Part) Restart OBS. If you don’t restart, the plugin won't initialize. Open Tuna: Go to the top menu bar: Tools -> Tuna settings. Select Your Source: This is where you stop being limited by Spotify. If using YouTube/Soundcloud: Check the "Chromium based browsers" or "Window title" options. If using VLC or Foobar2000: Select the specific integration. Universal Tip: If your player isn't listed, use the "Windows Media Control" source. This captures anything that shows up when you hit the "Play/Pause" media keys on your keyboard. Phase 4: Displaying the Info Tuna doesn't automatically create a visual; it gives you the data. You have two choices: The Basic Way: Use the "Output" tab in Tuna to write the song info to a .txt file. Add a Text (GDI+) source in OBS and check "Read from file." The Pro Way: Use the "Web UI" tab. Tuna hosts a local webserver (usually localhost:16000). You add a Browser Source in OBS pointing to that local address to get a clean, animated overlay. The Reality Check If you open "Tools" and you don't see Tuna, you likely dragged the files into the wrong sub-folder. You need to be in the root obs-studio directory, not just the plugins folder. Do you want me to explain how to customize the CSS for the Web UI so it actually looks better than the 6K Labs default?
