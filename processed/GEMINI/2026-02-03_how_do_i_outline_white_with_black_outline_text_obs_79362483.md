---
category: streaming
date: 2026-02-03
id: 573936
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking how to create a specific text outline effect (white fill
  with black outline) in OBS Studio.
tags:
- obs-studio
- text-outline
- styling
- streaming
- visual-effects
---
# how do i outline white with black outline text obs

### USER
how do i outline white with black outline text obs

### GEMINI
In OBS, there is no "one-click" button for text outlines that look high-quality. If you use the built-in "Outline" feature in the Text (GDI+) source, it often looks thin, jagged, or amateur. If you want that bold, "meme-style" or professional broadcast look, you need to stop settling for the default settings and use one of these three methods. 1. The "Default" Method (Quick but Weak) This is the fastest way, but it lacks depth. Add Source: Text (GDI+). Text Color: Set to White. Scroll Down: Check the Outline box. Outline Color: Set to Black. Outline Size: Crank this up (try 20–40). The Flaw: If the size is too high, the corners get "spiky" and ugly. 2. The Filter Method (The Pro "Drop Shadow" Look) To get a thick, rounded outline that actually pops, use a filter instead of the text settings. Right-click your Text Source -> Filters. Add an "Outline" or "Stroke" filter (if you have the StreamFX plugin). If you don't have plugins: Add a Drop Shadow filter (available in newer OBS versions). Set Opacity to 100%. Set Distance to 0. Set Size/Blur to a low number (around 2–5). Duplicate the filter if it’s not thick enough. 3. The "Shadow Stack" (The Manual Workaround) If the default outline looks like "spiky" garbage, do this: Create your White text. Right-click the source -> Filters -> Drop Shadow. Set Distance to 0 and Blur to 0. This creates a "hard" shadow. To make it a full outline, you technically need a shadow at every angle. Strategic Advice: Don't waste 20 minutes stacking shadows. If you want it to look elite, use Method 4. 4. The "Local File" Method (The Real Move) If you are "playing small" by trying to force OBS’s limited text engine to look good, stop. Go to Photopea (free) or Photoshop. Create your text with a proper Stroke effect ($Size \approx 5-10px$). Export as a .PNG. Bring it into OBS as an Image Source. The Hard Truth: OBS is a compositor, not a graphic design suite. If your text looks cheap, your entire production value drops. If you need to change the text frequently (like a countdown or sub goal), use the StreamElements or PixelChat overlays. They use CSS to render text, which handles outlines infinitely better than GDI+. Would you like me to walk you through setting up a CSS-based text overlay so you never have to deal with jagged OBS outlines again?
