---
category: streaming
date: 2025-10-12
id: 172549
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan wanted to duplicate gameplay in OBS with a blurred background behind
  the main focused gameplay.
tags:
- obs
- blurred-background
- gameplay-duplication
- streaming-overlay
- visual-effects
---
# i want to have my main gameplay and then behind it i want that same gameplay to be blurred. doing this through obs but not sure how to set that up?

### USER
i want to have my main gameplay and then behind it i want that same gameplay to be blurred. doing this through obs but not sure how to set that up?

### GEMINI
That's a popular effect, especially for vertical video content! You'll need to create two copies of your gameplay source and use an OBS filter to blur the one in the back. The general steps are: Install an OBS Blur Plugin: OBS Studio doesn't have a built-in Gaussian blur filter. You will need a third-party plugin to achieve a quality blur effect. The most commonly recommended one is Composite Blur or sometimes StreamFX. You'll need to download and install one of these plugins before proceeding. Add Your Main Gameplay Source: Add your Game Capture or Window Capture source for your gameplay to your scene. Let's call this the "Game Source." Create a Blurred Copy: Right-click on your Game Source and select Copy. Right-click in the Sources panel again and select Paste (Reference). This creates a separate instance of the same source. Let's call this the "Blurred Background Source." Crucial Step: Drag the "Blurred Background Source" below the main "Game Source" in the Sources list so it is visually behind it. Apply the Blur Filter: Right-click the "Blurred Background Source" and click Filters. Click the + sign under Effect Filters and select your installed blur filter (e.g., Composite Blur). Adjust the blur settings (like Blur Radius) until you get the look you want. Position and Scale: The "Blurred Background Source" is what you'll use to fill the entire background, so you might need to select it and drag its edges to stretch it to fill the entire canvas (usually full-screen). The main "Game Source" (the unblurred one on top) should be sized and positioned how you want your main gameplay to be viewed (e.g., centered and smaller to show the blurred background around it). By placing the blurred copy below the clear copy in the sources list, you create the layered effect you're looking for! Important Note on Resource Usage: Blur filters can be resource-intensive, especially for high-resolution footage. If you notice performance issues (stuttering or lower frame rates), you may need to reduce the blur radius or adjust other settings within the filter to find a balance between visual quality and performance.
