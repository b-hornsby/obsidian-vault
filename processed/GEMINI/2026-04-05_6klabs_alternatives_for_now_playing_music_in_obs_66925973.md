---
category: streaming
date: 2026-04-05
id: 190698
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan was looking for alternatives to 6klabs for displaying currently playing
  music in OBS for his stream.
tags:
- obs
- now-playing
- music-widget
- streaming
- 6klabs
---
# 6klabs alternatives for now playing music in obs?

### USER
6klabs alternatives for now playing music in obs?

### GEMINI
If you're looking to move away from 6K Labs (Amuse), there are several robust alternatives ranging from lightweight browser widgets to local, privacy-focused scripts. 1. The Lightweight Choice: Jamlog Fast & Simple This is currently one of the most popular alternatives for those who want a "set it and forget it" browser source without heavy overhead. How it works: It uses your Last.fm scrobbles to pull data. Since almost every service (Spotify, Apple Music, Tidal, YouTube Music) can scrobble to Last.fm, it’s a universal bridge. Pros: Extremely fast; auto-themes colors based on album art; no complex login for OBS; highly customizable via a web editor. Setup: Connect your music player to Last.fm, then put your username into the Jamlog editor to generate your OBS URL. 2. The Local/Privacy Choice: Snip If you prefer not to use third-party web services or "vibe" with a more manual, local approach, Snip is the gold standard. How it works: It’s a small Windows application that runs in the background. It detects what’s playing and writes the track info to a .txt file. Pros: Zero latency; no browser source required; works offline; works with Spotify, iTunes, Winamp, and Foobar2000. Setup: You add a Text (GDI+) source in OBS and check the "Read from file" box, pointing it to snip.txt. 3. The Feature-Rich Choice: PixelChat (Now Playing) PixelChat is a suite of overlays that includes a very polished music widget. How it works: Directly connects to your Spotify or YouTube account. Pros: Offers unique "pixel art" and "minimalist" skins that look different from the standard Amuse aesthetic. It also includes built-in commands for your chat (e.g., !song) if you use their other tools. Setup: Connect via PixelChat.tv, customize the "Now Playing" overlay, and paste the URL into OBS. 4. The Specialist Choice: Cider (For Apple Music) Since 6K Labs is often buggy with Apple Music, many users have switched to Cider. How it works: Cider is an open-source Apple Music client. It has a built-in "Remote" and "Overlay" feature designed specifically for streamers. Pros: Best-in-class integration for Apple Music users; much lower resource usage than the official iTunes or Apple Music Windows app. Summary Comparison ToolBest ForConnection TypeStyleJamlogLow latency & multi-platformLast.fmModern/CleanSnipLocal control & privacyLocal .txt fileText-only (Customizable)PixelChatInteractivity & Chat commandsAPI (Spotify/YT)Varied/GamerCiderApple Music loyalistsInternal ClientApple Aesthetic Pro Tip: If you want that "scrolling" effect from Snip but it's cutting off, remember to right-click the Text source in OBS → Filters → Scroll. Set the horizontal speed to around 50 for a smooth look.
