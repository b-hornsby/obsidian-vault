---
category: streaming
date: 2026-02-04
id: 735374
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is looking for an easier way to track something using a browser source
  in OBS Studio.
tags:
- obs-studio
- browser-source
- streaming-setup
- streaming-tools
---
# what is an easier way to do this? what browser source tracks all?

### USER
what is an easier way to do this? what browser source tracks all?

### GEMINI
Since you’re on Linux, the "easiest" way to avoid shader errors and broken text while tracking both Spotify and SoundCloud is to use a Last.fm-based Browser Source. On Linux, Spotify and SoundCloud both support "scrobbling" (sending play data) to Last.fm. By using a widget that reads your Last.fm profile, you bypass the need for local files or fragile OBS plugins entirely. 1. The Easiest Widget: Jamlog (fast.jamlog.lol) This is a lightweight, "plug and go" widget that works perfectly in an OBS Browser Source. Step 1: Create a free Last.fm account if you don't have one. Step 2: In Spotify Settings, go to "Social" and connect your Last.fm. For SoundCloud, use the Last.fm Scrobbler extension or internal settings. Step 3: Go to fast.jamlog.lol. Step 4: Enter your Last.fm username. Step 5: Customize the colors (White text, Black background/outline). Step 6: Copy the URL at the bottom and paste it into a Browser Source in OBS. 2. The Professional Alternative: Amuse If you want something that looks like a sleek app and handles album art beautifully without breaking: Search for Amuse OBS Widget (6K Labs). It supports Linux and acts as a single Browser Source link that handles Spotify and YouTube Music/SoundCloud via web hooks. Why it's better: It has a built-in "Editor" where you can toggle the outline/stroke with a slider—no CSS or shaders required. The "Brutal Honest" Comparison MethodEffortReliabilityLookOBS ShadersHigh (Broken)Terrible on LinuxJitteryLocal Text FilesMediumGoodBasicJamlog/AmuseLow (3 mins)Rock SolidProfessional Your Prioritized Plan: Delete the shader filter and the FreeType 2 text source. They are causing you 90% of your stress. Connect your Spotify/SoundCloud to Last.fm (takes 60 seconds). Add a Browser Source using the Jamlog link. Would you like me to give you the specific CSS to make the Jamlog widget have that "White text with thick Black outline" look?
