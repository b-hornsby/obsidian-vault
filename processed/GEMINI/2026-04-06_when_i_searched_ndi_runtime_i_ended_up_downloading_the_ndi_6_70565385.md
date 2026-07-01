---
id: 396067
source: GEMINI
date: 2026-04-06
tags: ['ndi', 'distroav', 'obs-plugin', 'ndi-runtime']
category: streaming
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan accidentally downloaded NDI 6 Tools instead of the NDI runtime and learned the plugin is now called DistroAV.
---
# when i searched ndi runtime i ended up downloading the ndi 6 tools and i dont think thats what i needed. the plugin is now called distroAV

### USER
when i searched ndi runtime i ended up downloading the ndi 6 tools and i dont think thats what i needed. the plugin is now called distroAV

### GEMINI
You’re right to be confused—the NDI ecosystem just went through a major rebranding. The plugin formerly known as obs-ndi is now DistroAV, and it requires the NDI 6 Runtime to function. Since you already downloaded "NDI 6 Tools," you actually have the runtime installed (it’s bundled in the tools), but the DistroAV plugin is the specific piece of "connective tissue" that adds the NDI options into OBS. The 3-Step Setup to Kill the Lag Follow this exactly to replace that laggy Virtual Camera with a high-speed NDI stream. 1. Install DistroAV (The Plugin) If you don't see "DistroAV" or "NDI" under your Tools menu in OBS, you need to install the plugin specifically: Go to the DistroAV GitHub Releases. Download the Windows .exe installer (usually named something like DistroAV-6.x.x-Windows-Installer.exe). Install it and restart OBS. 2. Enable NDI Output in OBS Now you need to tell OBS to "broadcast" your video over your internal PC memory so TikTok can see it. In OBS, go to Tools > DistroAV Settings (or NDI Output Settings). Check the box for Main Output. Give it a name like "OBS-Main". Crucial for your setup: Since you want to stream your Vertical setup to TikTok, make sure your Aitum Vertical plugin is active. Some versions of DistroAV allow you to right-click your Vertical Scene/Source -> Filters -> Dedicated NDI Output. Use this if you only want to send the vertical feed to TikTok while keeping Twitch horizontal. 3. Capture in TikTok Live Studio Open TikTok Live Studio. Add a new source and look for NDI (it might be under "More Sources" or "Third Party Apps"). Select "OBS-Main" (or whatever you named it). Efficiency Win: You can now lower the "Preview" resolution in TikTok Live Studio to the absolute minimum. NDI handles the heavy lifting, so TikTok Live Studio doesn't have to work hard to "capture" the window. Why this is the "Advisor" Choice Virtual Camera: Acts like a generic webcam driver. It’s slow, unoptimized, and Windows treats it with low priority. NDI: Acts like a "virtual cable" inside your RAM. It has almost zero latency and is designed for high-bitrate video. It won't fight CS2 for GPU priority nearly as much. One Final Warning: The "Reliable UDP" Bug There is a known bug in NDI 6 (DistroAV) where a setting called "Reliable UDP" causes stuttering on Windows 11. Open your NDI Tools (the ones you already downloaded). Open the app called Access Manager. Go to the Advanced tab. Look for Receive Mode and change it from "Auto" to Unicast or Multicast. Avoid "Reliable UDP" if you see it, as that is the primary cause of "bursty lag" in CS2. Does "DistroAV" show up in your OBS Tools menu now? If not, the installer likely put the files in the wrong folder, and I can show you how to move them manually.
