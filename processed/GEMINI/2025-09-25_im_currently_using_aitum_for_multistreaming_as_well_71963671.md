---
id: 683905
source: GEMINI
date: 2025-09-25
tags: ['multistreaming', 'aitum']
category: streaming
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan is stating that he is using Aitum for multistreaming.
---
# i'm currently using aitum for multistreaming as well 

### USER
i'm currently using aitum for multistreaming as well 

### GEMINI
That information is very important for troubleshooting this specific issue. If you are using Aitum Multistream or the Aitum Vertical plugin, the unclickable "ghost" scene is most likely related to how the plugin manages scenes. The Aitum Vertical plugin, for instance, adds a separate canvas to OBS for vertical content (like TikTok/Shorts) and often works by creating or managing hidden scenes that are linked to your main scenes. Here's what is likely happening and what you should do: 1. The Probable Cause (Aitum) Plugins like Aitum often create internal, hidden scenes to handle the logic, transitions, or separate outputs (like your vertical feed). The unclickable scene you are seeing is almost certainly one of these internal or phantom scenes that is not intended for user interaction but has visually slipped into your main Scenes list due to a minor display bug. This is a known type of issue that can occur with various OBS plugins, including Aitum. 2. Immediate Fix (Same as before, but with more emphasis) The fastest and safest way to clear a visual glitch caused by a plugin is still a clean restart: Close OBS Studio completely. Close the Aitum App/Service. Wait about 10 seconds. Relaunch OBS Studio (you can then relaunch Aitum). 3. If the Problem Persists If the restart doesn't work, the issue may be a persistent bug that needs attention from the plugin developer. Check for Aitum/Plugin Updates: Ensure that both your OBS Studio and your Aitum plugin (Multistream and/or Vertical) are running the absolute latest version. Plugin updates frequently fix scene and source management bugs. Aitum's Support Discord: Aitum has a very active community and development team. Searching their official resources or submitting a support question is often the fastest way to get a specific solution for a bug within their plugin. The Nuclear Option (If you need to get rid of it right now): If you are absolutely certain the unclickable scene is a persistent ghost entry, you may need to back up your Scene Collection (via Scene Collection -> Export in OBS) and then attempt to completely reinstall the Aitum plugin. However, only do this if you are comfortable with reinstalling plugins.
