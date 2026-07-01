---
category: streaming
date: 2025-10-12
id: 052295
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking if TikTok Studio supports blurred background effects natively.
tags:
- blurred-background
- tiktok-studio
- streaming-overlay
- visual-effects
---
# is there a way to have a blurred background in tiktok studio? 

### USER
is there a way to have a blurred background in tiktok studio? 

### GEMINI
Yes, there are a few ways to get a blurred background in TikTok LIVE Studio, but the most reliable and highest-quality methods involve using a third-party tool like OBS Studio as a middleman, as TikTok Studio's own effects are somewhat limited. Here are the best methods, from easiest to most advanced: Method 1: Use an External Webcam Software (Easiest) Many modern webcams (Logitech, Razer, etc.) or utility apps (like NVIDIA Broadcast for NVIDIA users) have a built-in "Background Blur" filter. Apply the Blur: Open your camera's software (e.g., Logitech G HUB, NVIDIA Broadcast, or a third-party virtual camera app) and apply the Background Blur filter there. Select the Output in TikTok Studio: In TikTok LIVE Studio, add your camera as a source, but instead of selecting the physical webcam, select the virtual camera output from the software you used (e.g., "NVIDIA Broadcast," "Logitech Camera," etc.). The stream will now receive the high-quality, blurred video feed. Method 2: Use OBS Studio as a Virtual Camera (Most Control) This method gives you the most control over the blur intensity and quality. Set up the Blur in OBS: In OBS, add your webcam as a Video Capture Device source. Right-click the source $\rightarrow$ Filters $\rightarrow$ Click the + under Effect Filters. Add a "Background Removal" filter (or a third-party plugin like StreamFX) to separate you from the background. Add a second source (either your raw webcam feed or a static image) below your primary webcam source in the source list. Apply a Blur Filter (you may need a plugin like Composite Blur) to this background source. Send to TikTok Studio: In the bottom-right of OBS, click Start Virtual Camera. In TikTok LIVE Studio, go to Add Source $\rightarrow$ Camera, and select "OBS Virtual Camera" (or a similar name) as the camera device. Method 3: Use TikTok Studio's Built-in Green Screen (Workaround) If you already have a physical green screen or a very clean background, you can use TikTok Studio's built-in background removal and replace it with a blurred image. Find/Create a Blurred Background: Get a picture of a room or a pattern and use a simple online image editor to heavily blur it. Save this blurred image. Add to TikTok Studio: In TikTok LIVE Studio, add your camera as a source. Go to the Effects panel for your camera source. Enable the Green Screen or Background Removal effect. Choose to replace the background with a Source. Select your pre-blurred image as the background replacement. This gives the effect of a blurred background, even though it's technically a blurred image placed behind you.
