---
category: streaming
date: 2026-02-03
id: 462771
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wants to create or configure a widget to display album art in his OBS
  streaming overlay using Tuna.
tags:
- obs-studio
- album-art
- now-playing
- streaming-overlay
- tuna
---
# i want a widget to show the album art with this 

### USER
i want a widget to show the album art with this 

### GEMINI
To get the album art visible alongside the text, we have to stop treating the widget as just a "web link" and start using it as a composite source in OBS. Since you are on Linux and using MPRIS, the plugin is already saving a local image of your cover art every time the song changes. We just need to display it. Step 1: The "Dual-Source" Setup (Most Reliable) Instead of one Browser Source, use two separate sources in OBS. This gives you 100% control over the layout. Add the Cover Art: In OBS, click the + and add an Image Source. Name it "Music Cover." Check the box "Unload image when not showing". For the file path, browse to: /home/toastedmel0n/cover.png (as seen in your earlier Tuna settings). Pro Tip: Right-click the image in your preview -> Transform -> Edit Transform. Set "Bounding Box Type" to Scale to inner bounds. Now, no matter if the art is a rectangle or square, it won't break your layout. Add the Text: Keep your Browser Source with the CSS I gave you earlier, and simply move it next to the image. Step 2: The "Widget" Way (Album Art + Text in one) If you want them both inside a single box like 6K Labs, we have to fix the link. In your previous screenshot, you were looking at raw JSON code. To see the image inside that web view, you need a different URL. In your Browser Source, change the URL to: http://localhost:1608/overlay The Secret Sauce: If it’s still blank, it’s because Tuna doesn't know where your CSS is. Open your style.css file in a text editor and make sure this line exists at the top: #cover { width: 100px; height: 100px; display: block; } Step 3: Verify the "Brain" Settings Go back to Tools -> Tuna Settings one last time and verify these two paths: Song cover path: /home/toastedmel0n/cover.png Song info path: /home/toastedmel0n/nowplaying.txt If these files are being updated when you play a song, but they aren't appearing in OBS, it's a file permission issue. Since you're on CachyOS, make sure the folder they are in isn't locked. The Reality Check You're trying to replicate a "cloud" widget (6K Labs) with a "local" power tool (Tuna). 6K Labs: Easy, but limited to Spotify. Tuna: Hard to set up, but plays anything. My prioritized plan for you: Forget the index.html struggle for a moment. Add the Image Source pointing to cover.png and the Text Source pointing to nowplaying.txt. It will take you 30 seconds, it will never break, and it will look exactly how you want. Do you want me to give you a specific OBS "Filter" setting to make that album art look extra clean (rounded corners, drop shadow)?
