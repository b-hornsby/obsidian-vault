---
category: streaming
date: 2026-04-06
id: 492049
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was trying to fix extreme lag when streaming his vertical OBS setup
  to TikTok Live Studio while playing CS2, and wanted to set up Restream for dual-platform
  streaming.
tags:
- obs
- vertical-camera
- tiktok-live-studio
- cs2
- lag
- restream
---
# So using the virtual vertical camera to stream my obs vertical setup to TikTok live studio isn’t working when I try to play cs2. It’s extremely laggy but I know my pc is capable of streaming to two platforms because I used to do twitch and TikTok at the same time. How do I set up restream (or whatever tool) so that I can set my obs up to stream to TikTok live studio without lag 

### USER
So using the virtual vertical camera to stream my obs vertical setup to TikTok live studio isn’t working when I try to play cs2. It’s extremely laggy but I know my pc is capable of streaming to two platforms because I used to do twitch and TikTok at the same time. How do I set up restream (or whatever tool) so that I can set my obs up to stream to TikTok live studio without lag 

### GEMINI
The reason you're lagging in CS2 while using the virtual camera is likely a resource conflict between OBS and TikTok Live Studio. Both apps are fighting for GPU priority to encode video, and CS2 is notoriously CPU/GPU intensive, especially with the Source 2 engine. Since you're on an RTX 3070 and i7-12700K, you have the power, but the "Virtual Camera" method adds a layer of processing that often breaks "Game Mode" optimizations. If you want to ditch the virtual camera and use a tool like Restream (or a direct plugin) to stabilize your setup, here is the most efficient way to do it in 2026. Option 1: The "Cleanest" Way (Aitum Vertical + Restream) Restream is great because it handles the distribution for you. Instead of your PC sending two separate high-bitrate streams, it sends one to Restream, and they push it to Twitch and TikTok. Connect TikTok to Restream: Go to your Restream dashboard and add TikTok as a channel. Note: If you don't have a direct RTMP key, you'll need to use their official TikTok integration which authenticates through your account. Configure OBS: Since you're using the Aitum Vertical plugin, go to the Vertical Settings in OBS. Instead of "Streaming" through the main OBS settings, you can set the Vertical plugin to stream to a Custom RTMP (your Restream TikTok ingest URL). Why this fixes lag: This bypasses TikTok Live Studio entirely. You won't even need that app open. Your PC only has to run OBS and the game. Option 2: The "Direct" Way (OBS Multi-RTMP Plugin) If you don't want to pay for Restream's premium "transcoding" or vertical features, use the Free OBS Multi-RTMP plugin. Step 1: Download and install the OBS Multi-RTMP plugin. Step 2: Start your main Twitch stream as usual in OBS. Step 3: In the Multi-RTMP panel, click "Add New Target." Name it "TikTok." Step 4: Input your TikTok Server URL and Stream Key (if you have one). Step 5: Check the box "Get Video from OBS" and select your Vertical Canvas as the source. The Benefit: This uses your GPU's NVENC encoder directly twice, which is much more efficient than the "Virtual Camera" handoff. Immediate Technical Fixes (If you MUST use TikTok Live Studio) If you are forced to use TikTok Live Studio (e.g., to see your TikTok-specific alerts/goals), do these three things to kill the lag: Run as Administrator: Run both OBS and TikTok Live Studio as Administrator. This tells Windows to give them GPU priority over background tasks. Hardware Encoding Check: In TikTok Live Studio, go to Settings > Video and ensure the "Encoder" is set to NVIDIA NVENC (H.264). If it's on "Default" or "Software," it’s eating your CPU. The NDI Alternative: If the Virtual Camera remains laggy, install the NDI Plugin for OBS. Enable NDI Output in OBS. In TikTok Live Studio, add an "NDI Source" instead of a "Camera." NDI is generally much lower latency and more stable than the Windows Virtual Camera driver for high-motion games like CS2. The Advice: Stop using the Virtual Camera for CS2. It’s a "wrapper" that creates unnecessary overhead. Move to the Multi-RTMP plugin or Restream so you can close TikTok Live Studio entirely while playing. Your 3070 will handle two NVENC encodes easily; it just can't handle the "middleman" software.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
