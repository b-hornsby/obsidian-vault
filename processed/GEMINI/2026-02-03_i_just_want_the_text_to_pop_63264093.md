---
category: streaming
date: 2026-02-03
id: 786819
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan wants to make text stand out or 'pop' in his OBS overlay with better
  visual styling.
tags:
- obs-studio
- text-styling
- streaming-overlay
- visual-effects
---
# i just want the text to pop

### USER
i just want the text to pop

### GEMINI
To make the text "pop" on a transparent background, you need to add visual contrast so it doesn't get lost in the colors of your game or video. 1. Add an Outline (Stroke) This is the most effective way to make text readable on any background. Double-click your Text Source. Scroll down to the Outline section. Enable Outline: Check the box. Color: Set it to Black (if your text is white). Size: Set it between 3 and 6. This creates a sharp "sticker" effect that separates the letters from the background. 2. Add a Drop Shadow Filter If the outline isn't enough, a subtle shadow will give it depth. Right-click your Text Source -> Filters. Click + and select Color Correction (or "Drop Shadow" if your version of OBS has it as a dedicated filter). If using Color Correction: Lower the Brightness slightly and look for Opacity. Alternatively, add a second Text Source exactly the same as the first, color it black, and offset it by a few pixels behind the original. 3. Use "Custom Extents" for Clean Scrolling Since you are scrolling, you want the text to stay within a specific "lane" so it doesn't overlap your album art. In the Text Source properties, check Use Custom Extents. Set the Width to something like 400 or 500. This forces the text to "disappear" and "reappear" at specific boundaries, making it look like a professional broadcast ticker. The Advisor's Precision Tip: Go back to Tuna Settings and check your Song format. If it’s just {title}, it might look a bit thin. Change it to: NOW PLAYING: {title} - {artists} . The "NOW PLAYING" prefix gives the viewer instant context, and the extra spaces at the end are mandatory to keep the scrolling text from looping back into itself immediately. Is the text sharp and readable now, or does it still feel a bit "flat" against your screen?
