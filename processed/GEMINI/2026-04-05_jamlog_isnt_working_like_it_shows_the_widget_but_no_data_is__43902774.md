---
category: streaming
date: 2026-04-05
id: 660643
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was troubleshooting Jamlog not displaying music data in OBS despite
  Last.fm being connected.
tags:
- jamlog
- lastfm
- obs-widget
- now-playing
- streaming
---
# jamlog isnt working like it shows the widget but no data is showing even tho my lastfm is connected

### USER
jamlog isnt working like it shows the widget but no data is showing even tho my lastfm is connected

### GEMINI
If Jamlog is showing the widget frame but no track data, the issue is almost always a "handshake" failure between your music player and Last.fm, rather than a problem with OBS or Jamlog itself. Since Jamlog is just a window into your Last.fm "Recent Tracks," if Last.fm doesn't see you're playing something, Jamlog has nothing to display. 1. The "Scrobble" Check (Most Likely Culprit) Open your Last.fm profile in a browser. Look at your "Recent Tracks" list. If you don't see your current song listed as "Scrobbling now" or "1 minute ago": The problem is between your player (Spotify/Apple Music) and Last.fm. The Fix: 1. Go to your Last.fm Applications Settings. 2. Find Spotify Scrobbling and click Disconnect. 3. Refresh the page and click Connect again. 4. Crucial: Play a new song (don't just unpause). Last.fm often won't register a song that was already playing during the reconnect. 2. Verify the Jamlog Username It sounds simple, but check the URL you pasted into the OBS Browser Source. Make sure your username is spelled exactly as it appears on Last.fm. If you changed your Last.fm username recently, the old Jamlog URL will stop working immediately. 3. Check for "Private Session" If you are using Spotify, check if you are in a Private Session. Desktop: Click your profile name at the top right. If "Private Session" has a checkmark, turn it off. Last.fm cannot "see" what you're playing if you're in stealth mode. 4. Force a Refresh in OBS Sometimes the Browser Source cache hangs. Double-click the Jamlog Source in your OBS Sources list. Scroll down to the bottom of the properties window. Click the button that says "Refresh cache of current page." 5. If it's still blank (The "New Account" Bug) If your Last.fm account is brand new (less than 24 hours old), the API sometimes fails to push data to third-party widgets like Jamlog until you have at least 10-20 "scrobbles" (completed songs) in your history. Quick Alternative if Jamlog stays dead: If you can't get the Last.fm API to behave, try PixelChat. It connects directly to Spotify via a login button rather than relying on the Last.fm scrobble bridge, which usually bypasses these "no data showing" sync issues.
