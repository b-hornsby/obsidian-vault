---
category: streaming
date: 2025-10-12
id: 666517
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was looking for a source to get a streaming widget for his TikTok setup.
tags:
- streaming-widget
- overlay
- tiktok-studio
- streaming-tools
---
# can you link me to a place that has this widget? 

### USER
can you link me to a place that has this widget? 

### GEMINI
The absolute best place for a simple, customizable counter widget that provides a URL you can use in TikTok Studio is StreamElements. StreamElements is a popular streaming platform that offers a free "Bot Counter" widget designed for this exact purpose. The Link and How to Set It Up Platform Link (Dashboard): You'll need to start on the StreamElements website to create your widget. Go to the StreamElements Dashboard: https://streamelements.com/dashboard You will need to sign up and connect your streaming account (Twitch, YouTube, etc.) to use their service, though you don't have to stream on that platform to use the widgets. Steps to Get the Counter URL: Create an Overlay: Navigate to My Overlays and click New Overlay. Choose a resolution (e.g., 1080p). Add the Counter Widget: Click the $+$ (Add Widget) button. Go to Labels $\rightarrow$ Other $\rightarrow$ Bot Counter. Configure the Counter: In the settings for the new widget, change the name of the counter to something simple like deaths. Customize the font, size, and color to your liking. Get the URL: After customizing, click the Save button. Click the Copy Overlay URL icon (it looks like a chain link) at the top of the Overlay Editor. Chat Commands (To Control the Number): You need to create a command for your chat that updates the counter. Go to StreamElements Dashboard $\rightarrow$ Chatbot $\rightarrow$ Commands $\rightarrow$ Default Commands. Find or add a custom command (e.g., !death). You will use the following variable: Command: !death Response: ${count deaths} (This is a simplified example that shows the current count and increases it by 1). You can also set up a command for mods to reset it, like !deathreset with the response ${count deaths 0}. Once you have the copied URL, you paste it into TikTok Studio as a Link Source as described previously.
