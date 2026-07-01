---
category: streaming
date: 2026-02-03
id: 725098
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking how to make the background of scrolling text transparent
  in OBS Studio.
tags:
- obs-studio
- scrolling-text
- transparency
- overlay
- streaming
---
# how do i get a transparent bg on the scrolling text?

### USER
how do i get a transparent bg on the scrolling text?

### GEMINI
To get a transparent background on your scrolling text, you need to adjust the Text Source properties in OBS, as the background is controlled by the source itself, not the scrolling filter. 1. Configure the Text Source Double-click your Text Source (the one reading from nowplaying.txt). Scroll down to the Background Color or Opacity settings. Set the Background Opacity slider to 0%. Ensure the Color is set to something readable (like White) so it stands out against your gameplay. 2. The "Filter" Cleanup If you see a black box moving with your text, it might be because of the Scroll Filter settings. Right-click the source > Filters > Scroll. Ensure "Limit Width" is not creating a solid-colored bounding box. If you want a specific width for the text to scroll within without a background, use the "Custom Extents" option in the main Text Source properties, not the filter. 3. Professional Polish (The Outline) Transparent text can sometimes get lost against bright backgrounds in your stream. In the Text Source properties, scroll down to Outline. Enable it and set the color to Black with a thickness of 2-4. This keeps the background transparent while making the text "pop" regardless of what is happening behind it. The Advisor's Priority Plan You’ve successfully built a scrolling, universal music widget on Linux. Now, to keep it clean: Set Opacity to 0 in the source properties. Add 5-10 spaces to the end of your format in Tuna ({title} - {artists} ) so the scroll doesn't look cluttered. Lock the source in your OBS scene so you don't accidentally drag it. Is the text now floating cleanly over your capture, or is there still a visible "box" around it?
