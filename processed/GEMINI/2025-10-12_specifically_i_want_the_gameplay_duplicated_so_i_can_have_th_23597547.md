---
category: streaming
date: 2025-10-12
id: 386226
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan wanted to duplicate gameplay in OBS so the background version is blurred
  while the foreground stays sharp.
tags:
- obs
- gameplay-duplication
- blurred-background
- streaming-layout
- scene-composition
---
# specifically i want the gameplay duplicated so i can have the background be blurred while the main gameplay is in focus if that makes sense 

### USER
specifically i want the gameplay duplicated so i can have the background be blurred while the main gameplay is in focus if that makes sense 

### GEMINI
That is a very popular and professional look for vertical video content, especially for gaming clips! Currently, TikTok LIVE Studio does not have a built-in feature to duplicate a single Game/Screen Capture source, scale the copy up, and apply a blur filter to it. The most reliable and common way to achieve this live during a stream is to use OBS Studio as a middleman and then bring the finished, layered composition into TikTok Studio. Here is the step-by-step process using OBS Studio: Recommended Method: Using OBS Studio This method involves layering two identical copies of your gameplay inside OBS, blurring the bottom layer, and then sending the result to TikTok Studio. Part 1: Setting up the Layered Blur Effect in OBS Add the Game Source (x2): In OBS, go to the Sources panel. Add your game capture source (e.g., Game Capture or Window Capture). Once that source is added, right-click it, select Copy, then right-click in the Sources panel again and select Paste (Reference). You now have two identical sources linked to the same gameplay. Rename and Order the Sources: Rename the bottom source to something like "Game - Blurred BG". Rename the top source to something like "Game - Main Focus". Make sure "Game - Blurred BG" is below "Game - Main Focus" in the source list. Create the Blurred Background: Select the bottom source, "Game - Blurred BG". Stretch this source to fill the entire 9:16 vertical canvas (it will be zoomed in and cropped to the top and bottom). Right-click on "Game - Blurred BG" $\rightarrow$ Filters. Click the + button under Effect Filters and select a blur filter. (Note: OBS may require a third-party plugin like StreamFX or Composite Blur to have a high-quality blur effect. If you don't want plugins, use the simple Color Correction filter's "Gamma" or "Saturation" to slightly darken the background, but this won't actually blur it.) Adjust the blur intensity to your liking. Position the Main Focus: Select the top source, "Game - Main Focus". Resize and position this layer to the main, clear viewing area of your 9:16 vertical stream (the center part that is not covered by the blurred background). Part 2: Sending the OBS Scene to TikTok LIVE Studio Start the Virtual Camera: In OBS, click the Start Virtual Camera button (usually in the lower right). This turns your entire OBS Scene into a webcam-like video feed. Add to TikTok Studio: Open TikTok LIVE Studio. Click Add Source $\rightarrow$ Camera. For the camera device, select "OBS Virtual Camera" (or whatever the OBS output is named). Your TikTok stream will now show the layered, blurred-background effect you created in OBS!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
