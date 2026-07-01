---
category: streaming
date: 2026-02-03
id: 505066
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is looking for a 'now playing' widget that supports more music platforms
  than just Spotify, for his streaming setup.
tags:
- 6klabs-widget
- now-playing
- spotify
- music-platform-compatibility
- streaming-tools
---
# using 6klabs now playing widget but it only picks up spotify? any that pick up any music platform?

### USER
using 6klabs now playing widget but it only picks up spotify? any that pick up any music platform?

### GEMINI
The truth is, 6K Labs (Amuse) is built primarily as a Spotify-first tool. While they recently added support for YouTube Music, it still requires a specific desktop app workaround to function. If you’re looking for a "one widget to rule them all" solution that doesn't care if you're using Apple Music, Tidal, or some obscure local player, you need to change your strategy. Here are the hard facts and the best pivots for your setup: 1. The "Universal" Choice: PixelChat If you want to move away from being locked into Spotify, PixelChat is the most flexible direct competitor. How it works: It uses Last.fm scrobbling. The Advantage: Almost every music service (Tidal, Apple Music, Deezer, etc.) can "scrobble" to Last.fm. PixelChat reads your Last.fm profile in real-time and displays whatever is playing there. The Catch: There is sometimes a slight delay (10–20 seconds) compared to the instant Spotify API. 2. The Power User Choice: Tuna (OBS Plugin) Stop relying on browser-based widgets if you want maximum reliability across platforms. Tuna is a legendary OBS plugin. Compatibility: It can pull data from window titles, VLC, Spotify, YouTube (via browser extensions), and even generic media keys. Flexibility: It outputs the song info to a local text file or a customizable CSS overlay. You aren't at the mercy of a third-party server staying online. 3. The Specialist: "Now Playing" App There is a dedicated desktop application called Now Playing (nowplayingapp.com) used by high-end DJs and streamers. Best for: People who use professional software or want a highly polished, "it just works" desktop-to-OBS connection. Platform Support: Excellent for Apple Music and local files, which 6K Labs ignores. Why you’re feeling limited: You are currently optimized for convenience (a simple browser link), but you want versatility. Those two things are often at odds in streaming tech. 6K Labs is beautiful, but it's a "walled garden." My prioritized plan for you: Immediate Fix: Create a free Last.fm account and link your music service to it. Then, set up a PixelChat Now Playing overlay. This is the fastest way to get non-Spotify music on screen. Long-term Upgrade: Install the Tuna OBS plugin. It’s more "work" to style it yourself, but you will never have to ask this question again because it can grab info from literally anything playing audio on your PC. Stop making excuses for the 6K Labs delay: If it’s only picking up Spotify, it’s because you haven't set up the YouTube Music Desktop App integration (which is clunky anyway). Move to a tool designed for your actual workflow. Would you like me to walk you through how to set up the Last.fm bridge for PixelChat?
