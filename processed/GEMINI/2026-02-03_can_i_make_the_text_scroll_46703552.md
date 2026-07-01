---
category: streaming
date: 2026-02-03
id: 551810
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan wants to know if he can make text scroll in an OBS overlay, likely
  for a now-playing display.
tags:
- obs-studio
- text-scroll
- streaming-overlay
- marquee
---
# can i make the text scroll?

### USER
can i make the text scroll?

### GEMINI
Since your album art is finally updating but your text is static, you've reached the final "boss" of the layout: the OBS Filter. You don't need a plugin or code for this; OBS has a built-in "Scroll" filter specifically for this purpose. 1. Add the Scroll Filter Right-click your Text Source in the OBS Sources list. Select Filters. Click the + icon at the bottom left and select Scroll. Give it a name (e.g., "Song Scroll"). 2. Set the Speed Horizontal Speed: Drag this to the right. A value between 50 and 100 is usually perfect for readability. If you go too fast, you'll give your viewers a headache. Vertical Speed: Keep this at 0. Loop: Make sure this is Checked. 3. Fixing the "Crowded Text" (Critical Step) If you just enable scrolling, the end of the song title will touch the beginning of the title as it loops, making it look like one giant word. Go back to Tuna Settings. Edit your Song info output format. Change it to: {title} - {artists} (Add 5-10 spaces at the end of the format). Hit OK and Start. Now there will be a clean gap before the text repeats. 4. How to keep it from taking over the screen Since some song titles are longer than others, the text box will "grow" and "shrink" in OBS, which can mess up your layout. Right-click the Text Source -> Properties. Check the box for "Use Custom Extents" (or "Limit Width"). Set a Width (e.g., 400). Now the text will only scroll inside that specific box, keeping your overlay tidy. The Advisor's Final Mirror: Your widget is now alive. You’ve successfully moved from a "one-click" Spotify tool to a custom, Arch-based, universal music machine. It took some work because you're using a system that prizes control over convenience. One last check: Since you're on CachyOS, if the scrolling looks "stuttery," go into your OBS Settings > Advanced and ensure "Enable Browser Source Hardware Acceleration" is on (though for a text source, it's usually just your GPU compositor—make sure your refresh rate is set correctly). Is the text moving across the screen now, or do you need help positioning it next to the album art?
