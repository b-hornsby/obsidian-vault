---
id: 783441
source: GEMINI
date: 2026-04-06
tags: ['tiktok-live', 'vertical-streaming', 'blurred-background', 'obs-filters', 'virtual-camera']
category: streaming
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan wanted to create a blurred game background effect for vertical TikTok streaming using OBS.
---
# how do i get a blurred effect when vertically streaming on tiktok? specifically im trying to have a blurred bg of the game im playing and then a clear version over top of it. im using obs to virtually stream my obs setup to tiktok live studio 

### USER
how do i get a blurred effect when vertically streaming on tiktok? specifically im trying to have a blurred bg of the game im playing and then a clear version over top of it. im using obs to virtually stream my obs setup to tiktok live studio 

### GEMINI
To get that "blurred background with clear gameplay overlay" look for your TikTok stream, you need to layer your gameplay source twice within OBS and apply a specific filter to the bottom layer. Since you're already using OBS to virtually stream to TikTok Live Studio, you have everything you need. The Strategy: "Layer & Blur" You will create two instances of your game. The bottom one will be stretched to fill the vertical 9:16 space and blurred, while the top one will remain clear and centered. Step 1: Install the "Composite Blur" Plugin OBS doesn't have a high-quality "Blur" filter by default. You need the Composite Blur plugin (or similar) to make it look professional. Download and install the Composite Blur plugin for OBS. Restart OBS after installation. Step 2: Set Up the Blurred Background Add a Source Clone: Instead of adding your "Game Capture" twice (which can be laggy), use the Source Clone plugin or simply right-click your existing Game Capture and select Copy, then Paste (Reference). Size it Up: Stretch this background copy so it fills the entire vertical canvas. You’ll lose the sides of the game, but it will cover the black bars. Apply the Blur: Right-click this background source → Filters. Click the + under Effect Filters and select Composite Blur. Set the Blur Radius to something between 20 and 40 depending on how much "dreamy" bokeh you want. Step 3: Layer the Clear Gameplay Ensure your original (clear) Game Capture is at the very top of your Sources list. Transform: Right-click the clear game source → Transform → Center Horizontally. Keep its aspect ratio (16:9) so it sits in the middle of the screen, revealing the blurred version behind it on the top and bottom. Pro-Tip: Use a "Group" for the Blur If you have multiple scenes and don't want to apply filters to the game source itself (which would blur it everywhere), put the background copy into a Group. Right-click the background source → Group Selected Items. Apply the Composite Blur filter to the Group instead of the source. This keeps your actual game source "clean" for your other horizontal scenes. Connecting to TikTok Live Studio Since you're using the Virtual Camera: Click Start Virtual Camera in OBS. In TikTok Live Studio, add a Camera source and select OBS Virtual Camera. Ensure your TikTok Live Studio canvas is set to 9:16 (Vertical). Is this setup causing any frame drops or lag? Sometimes running two layers of the same game plus the Virtual Camera can be heavy on the GPU depending on your specs.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
