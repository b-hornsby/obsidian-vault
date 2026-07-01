---
category: general
date: 2025-10-12
id: 140431
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/general.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking for the easiest way to accomplish an unspecified task.
tags:
- streaming
- ''
- ''
- ''
- ''
- ''
---
# what is the easiest way to do this? 

### USER
what is the easiest way to do this? 

### GEMINI
The easiest way to get a simple, functional counter widget for your stream is to use StreamElements' Bot Counter and treat it as a "Link Source" in your streaming software (like TikTok LIVE Studio). This method is easy because it requires no file editing, no external apps, and no complex coding—just a single web link (URL). Here is the straightforward, step-by-step process: Part 1: Create the Counter on StreamElements Go to StreamElements: Open the StreamElements Dashboard and log in (you'll need to link a platform like Twitch or YouTube). Create a New Overlay: Navigate to My Overlays and click New Overlay. (Choose a resolution like 1080p). Add the Widget: Click the $+$ icon (Add Widget). Go to Labels $\rightarrow$ Other $\rightarrow$ Bot Counter. Name Your Counter: In the widget settings (on the left), under the Settings tab, give your counter a simple name like deaths or wins in the Counter Name field. Customize the font, size, and color in the Text Settings section. Get the Widget URL: Click the Save button (top right). Click the Copy Overlay URL icon (looks like a chain link) next to the "Save" button. Part 2: Add the Counter to TikTok LIVE Studio Open TikTok LIVE Studio (or OBS/Streamlabs). Add a Source: Click the Add Source button ($\mathbf{+}$). Choose Link Source (or Browser Source in OBS/Streamlabs). Paste the URL: Paste the URL you copied from StreamElements into the URL field. Set the width and height if prompted (e.g., $600$ width and $150$ height for just the counter text). The counter should now appear on your screen. Part 3: Control the Counter in Your Chat To make the number go up (or down), you and your moderators will use a simple chat command. Set up the Chat Command: Go back to the StreamElements Dashboard $\rightarrow$ Chatbot $\rightarrow$ Commands $\rightarrow$ Custom Commands. Click Add New Command. Command: !death Response: ${count deaths} The deaths part must match the counter name you chose in Part 1. Use the Command: When you or a moderator types !death in your Twitch/YouTube/Kick chat, the number on your stream will instantly go up by one. That's it! You have a fully functioning, command-controlled counter on your TikTok stream without downloading any extra software.
