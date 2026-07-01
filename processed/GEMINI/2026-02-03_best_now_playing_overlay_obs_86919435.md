---
category: streaming
date: 2026-02-03
id: 329723
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is looking for the best now-playing overlay solution for OBS to display
  current music during streams.
tags:
- obs-studio
- now-playing
- streaming-overlay
- music-display
---
# best now playing overlay obs

### USER
best now playing overlay obs

### GEMINI
Look, if you want a "now playing" overlay, stop overthinking the fluff. You don’t need 50 options; you need the one that fits your technical patience and your aesthetic. Most streamers are either looking for "plug-and-play" or "total control." Here is the objective breakdown of the best tools available right now in 2026. 1. The Best All-Rounder: Amuse (by 6K Labs) This is currently the gold standard for most streamers. It’s a web-based widget that connects to Spotify or YouTube Music. The Look: Extremely clean, modern designs (Card, Bar, Vinyl, etc.). It can even show the "Canvas" (the looping video) from Spotify. The Setup: You create a "Developer App" on Spotify (takes 2 minutes), paste the keys into 6K Labs, and add the URL as a Browser Source in OBS. Why it wins: Zero CPU impact on your PC because it’s a browser source. It’s "set it and forget it." 2. The Power-User Plugin: Tuna If you hate web-based tools and want everything running locally, use the Tuna plugin. The Versatility: It supports almost everything: Spotify (desktop), VLC, YouTube (via browser extensions), and even local MP3 files. The Control: It outputs information to a text file or a dedicated OBS source. You can style it yourself using OBS's built-in text filters (like scrolling) or custom CSS. The Catch: It requires an actual installation. If you aren't comfortable managing OBS plugins, stick to a browser source. 3. The Minimalist Choice: Pixel Chat Pixel Chat’s "Now Playing" overlay is for people who want a very specific, high-end "lo-fi" or "minimalist" aesthetic without any setup friction. Key Feature: It’s incredibly easy to theme. If you want a small bar that slides out when a song starts and hides when it ends, this is the one. Downside: Some of the deeper customization is locked behind their Pro tier, but the free version is usually enough for a basic song display. 4. The "Old School" Reliable: Snip Snip is a tiny application that runs in your system tray. It watches Spotify/iTunes and writes the song info to a .txt file and the album art to a .jpg file. How to use: In OBS, you add a Text (GDI+) source, check "Read from file," and select the Snip text file. The Benefit: It is the most lightweight way to get raw song data. You have 100% control over the font, color, and positioning because it’s just a standard OBS text source. Comparison at a Glance ToolSource TypeBest ForEffort LevelAmuseBrowser SourceModern, "Apple-style" aestheticsMedium (Spotify API setup)TunaOBS PluginHandling multiple music sourcesHigh (Plugin management)Pixel ChatBrowser SourceQuick setup, clean minimalist barsLow (One-click sync)SnipText FileTotal customization of fonts/layoutsLow (Local app) My Advice: If you want your stream to look professional with zero lag, go with Amuse. It handles the album art and transitions better than anything else. If you are a tinkerer who wants a specific font and a scrolling marquee, use Snip. Which music service are you actually using? I can give you the specific "gotchas" for Spotify vs. YouTube Music if you're undecided.
