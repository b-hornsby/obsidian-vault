---
category: streaming
date: 2025-10-12
id: 810905
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- homelab-stack
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to use OBS as a virtual camera for TikTok Studio to stream
  Dark Souls 3 with a death counter, but is having trouble getting his vertical scene
  to appear and finding a workaround for TikTok Studio's inability to read from a
  .txt file.
tags:
- obs-studio
- tiktok-studio
- virtual-camera
- vertical-streaming
- dark-souls-3
- death-counter
---
# trying to use obs as a virtual camera for streaming via tiktok studio and i cant get my vertical scene to pop up in that menu? specifically i'm trying to stream dark souls 3 and i wanted a death counter BUT tiktok studio doesn't allow reading from a .txt file 

### USER
trying to use obs as a virtual camera for streaming via tiktok studio and i cant get my vertical scene to pop up in that menu? specifically i'm trying to stream dark souls 3 and i wanted a death counter BUT tiktok studio doesn't allow reading from a .txt file 

### GEMINI
This is a common issue when using OBS's built-in Virtual Camera, as it typically outputs the Program Output (your main, horizontal scene) by default. The best solution for a vertical stream on TikTok Studio while using complex OBS scenes is often to use an additional plugin or a dedicated vertical virtual camera. Here's a breakdown of the two issues and potential solutions: 1. Vertical Scene Not Showing in TikTok Studio The OBS Virtual Camera usually transmits your main OBS canvas, which is likely set to a 16:9 (horizontal) resolution, even if you're using a vertical scene in OBS. Solution: Use a Third-Party Vertical Virtual Camera Plugin To get your vertical scene to output to a virtual camera that TikTok Studio can recognize, you'll likely need to use a dedicated solution like a specialized OBS plugin: Aitum Vertical Plugin: This is frequently cited as a solution for creating a separate, vertical canvas in OBS and outputting it to its own dedicated vertical virtual camera that is recognized by TikTok Studio. This allows you to run a horizontal stream for other platforms and a separate vertical stream for TikTok simultaneously, without the scenes conflicting. General OBS Virtual Camera Troubleshooting: If you insist on using the standard OBS Virtual Camera, make sure you do the following steps in the correct order: Open OBS Studio first. Start the Virtual Camera in the Controls dock in OBS. Open TikTok Live Studio and add a Camera source. Select "OBS Virtual Camera" from the camera list. If the virtual camera doesn't show up, try restarting both programs. Some users have also reported that instead of adding a Camera source in TikTok Studio, they had to add a Capture Card source and select "OBS Virtual Camera." 2. Death Counter without a .txt File Since TikTok Studio doesn't allow reading from a local .txt file, you need a web-based counter solution that can be added as a Browser Source in OBS (which is then captured by your virtual camera). Solution: Use a Web-Based Overlay Service The most reliable way to display a dynamic counter that TikTok Studio can use (via your OBS virtual camera) is to use a stream overlay service: Streamer.bot/StreamElements/Streamlabs: Many third-party stream tools offer counters that are displayed as Browser Sources (URLs). You use a hotkey or chat command to increment the count, and the number updates on the web page. Set up a StreamElements (or similar) overlay widget for a counter. Add this widget's URL as a Browser Source in your OBS vertical scene. Your OBS Virtual Camera will then capture the scene, including the counter. This bypasses the .txt file restriction completely, as your counter is being updated on a web page and streamed into OBS. The video below demonstrates how to set up the Aitum Virtual Camera with TikTok Live Studio. How to Use OBS Plugin on TikTok Live Studio (Aitum Virtual Camera Setup) explains how to use a specific plugin to connect an OBS vertical scene to TikTok Live Studio.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
