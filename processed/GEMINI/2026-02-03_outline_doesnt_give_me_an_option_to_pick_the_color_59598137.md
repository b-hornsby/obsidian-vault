---
category: streaming
date: 2026-02-03
id: 253264
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated because he can't select a color in the OBS Stroke plugin.
tags:
- obs-studio
- obs-stroke
- plugin
- color-selection
---
# outline doesnt give me an option to pick the color?

### USER
outline doesnt give me an option to pick the color?

### GEMINI
If you don’t see a color picker for the outline, it’s because you are likely using the Text (FreeType 2) source instead of Text (GDI+). On Windows, FreeType 2 is an older, inferior implementation that lacks basic styling controls. On macOS, it's often the only default option, and it is notoriously restrictive. Stop poking around in menus that don't have the tools you need. Here is how to fix this immediately: 1. The Source Swap (Windows Only) If you are on Windows, you chose the wrong source. Delete the "Text (FreeType 2)" source. Add a new source and select Text (GDI+). Scroll down; you will see Outline, and directly below it, Outline Color. 2. The Filter Workaround (macOS or Windows) If you are on Mac, or insist on using FreeType, you have to "force" the outline using a Filter because the source settings won't help you. Right-click your Text Source -> Filters. Add Directional Shadow (if available) or Drop Shadow. Set Distance to 0. Set Spread/Size to your desired thickness. Set the shadow color to Black. Note: If your OBS version is outdated, you won't even see these filters. Update your software. 3. The Objective Reality: Stop Using Internal OBS Text I’ll be direct: OBS's built-in text rendering is mediocre at best. If you are struggling with a basic outline color, you are fighting a losing battle against a weak tool. If you want text that actually looks sharp and professional without the headache: Use a Browser Source: Go to a tool like StreamElements or Topaz. Create your text there. The Result: You get high-quality CSS stroking (outlines) that don't look like jagged 1995 word art. The Effort: It takes 2 minutes longer to set up but saves you from looking like a low-effort amateur. Are you on a Mac, or are you on Windows and just picked the wrong source type?
