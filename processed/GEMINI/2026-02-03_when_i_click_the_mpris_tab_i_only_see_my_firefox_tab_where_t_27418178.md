---
category: streaming
date: 2026-02-03
id: 739302
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is troubleshooting why the MPRIS tab in OBS Studio only shows his Firefox
  tab, where music is playing, and not other music players.
tags:
- obs-studio
- mpris
- firefox
- music-control
- streaming-setup
- troubleshooting
---
# when i click the mpris tab i only see my firefox tab where the music is playing

### USER
when i click the mpris tab i only see my firefox tab where the music is playing

### GEMINI
That is exactly what you want to see. On Linux, Firefox acts as the "media player" for SoundCloud or YouTube. If you only see that Firefox tab, it means Tuna has successfully identified the correct source. The reason your screen is showing "unknown" is that you haven't selected it yet. 1. Select the Firefox Source Go to the MPRIS tab in Tuna Settings. Click on the Firefox entry to highlight it. Check the box "Use the first available player" if it’s there, or simply ensure Firefox is the active selection. Look at the bottom of the Tuna window. It should now show the song title instead of "No song playing". 2. Fix the "Blank" Browser Source In your screenshot, you are pointing the Browser Source to http://localhost:1608. This only shows the "raw brain" of the plugin. To get the actual widget: Change the URL in OBS to http://localhost:1608/overlay. If it's still blank: It's because your index.html file (the skin) is still named search.html or is missing from the plugin's internal folder. 3. The "Advisor's" Shortcut (Skip the Web Struggle) Since you are struggling with the webserver files, use the File Method. It is bulletproof on Linux. Add a Text Source in OBS. Check "Read from file". Select /home/toastedmel0n/nowplaying.txt. Add an Image Source in OBS. Select /home/toastedmel0n/cover.png. Apply the Scroll Filter to the Text Source as we discussed (Right-click > Filters > Scroll). The Brutal Truth: You are trying to force a web-based widget to work when you have a direct file output sitting right there. Every second you spend trying to fix localhost:1608 is a second you aren't streaming. The File Method works regardless of browser errors or JSON formatting. Does the song title finally appear at the bottom of the Tuna window once you click the Firefox entry in the MPRIS tab?
