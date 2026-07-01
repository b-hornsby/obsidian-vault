---
category: streaming
date: 2025-10-12
id: 880225
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was sharing his current screen view while troubleshooting a TikTok
  Studio streaming setup issue.
tags:
- tiktok-studio
- streaming-setup
- troubleshooting
- ui-reference
---
# this is what im looking at right now: 

### USER
this is what im looking at right now: 

### GEMINI
This is an excellent screenshot that immediately clarifies your issue. You are using the OBS Vertical Scenes plugin, which is a great first step! The problem is that the built-in OBS Virtual Camera (the one you are configuring) is only designed to output the main OBS canvas (which is typically horizontal), or a scene/source from that main canvas. The Vertical Scenes you created are part of a separate canvas added by the plugin, and the built-in Virtual Camera doesn't see them as standard scenes. Here is the most likely solution, broken down by your two problems: 1. The Vertical Scene Issue To use the vertical scene as a virtual camera, you need to use a virtual camera that is specifically created or designated to output the Vertical Canvas. You are looking at the settings for the standard OBS Virtual Camera: $$\text{Controls} \rightarrow \text{Start Virtual Camera} \rightarrow \text{Settings (Gear Icon)}$$ The Correct Solution (Most Reliable): Use the Vertical Plugin's Virtual Camera: If you are using a popular vertical plugin (like the Aitum Vertical Plugin), it will often create its own separate virtual camera that is specifically linked to the vertical canvas. Look for a separate button or setting within the Vertical Scenes dock or the plugin's settings to "Start Vertical Virtual Camera." In TikTok Studio, look for a second virtual camera device with a name like "Aitum Vertical Virtual Camera" (or similar, depending on the plugin you installed). If you don't have the Aitum plugin, consider installing it, as it is the most well-known solution for this exact problem on TikTok. Alternative Workaround (Less Ideal): If you don't want to install the Aitum plugin, your only other option for a vertical output is to manually change the main OBS Settings to a vertical resolution. Go to Settings $\rightarrow$ Video. Set Base (Canvas) Resolution to a vertical format (e.g., $1080 \times 1920$). Set Output (Scaled) Resolution to a vertical format (e.g., $1080 \times 1920$). Switch to your "Vertical Gameplay" scene. Start Virtual Camera (the one you see in your image). This will send a vertical feed, but it also forces your entire OBS to be vertical, which might break your normal streaming setup. 2. The Death Counter Issue (Without .txt) This is completely solvable using a web-based overlay, which is also easier to integrate into a complex setup like yours. Instead of a .txt file, you will use a Browser Source. Use a Stream Service for a Counter: Go to StreamElements, Streamlabs, or a similar service. Create a Custom Widget or use a Text/Goal widget and set up a counter. Crucially, this service will give you a "Widget URL" for that counter. This URL displays your counter number as a transparent web overlay. Add the Counter to your Vertical Scene in OBS: In your Vertical Scenes dock, select the "Other gameplay" scene. In the Sources dock (for that scene), click the $+$ button. Select Browser. Paste the Widget URL you got from StreamElements/Streamlabs. Position and resize the counter where you want it on your vertical screen. Since the death counter is now part of the OBS scene via a Browser Source, it will be included in the video feed that is sent to TikTok Studio via the Virtual Camera, bypassing the .txt file restriction. You'll update the counter using a hotkey or chat command via the streaming service's software (like Streamer.bot or the service's built-in controls).
