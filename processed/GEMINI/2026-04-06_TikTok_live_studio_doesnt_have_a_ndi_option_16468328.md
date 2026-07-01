---
category: streaming
date: 2026-04-06
id: 581895
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was noting that TikTok Live Studio lacks NDI support, limiting his
  streaming setup options.
tags:
- tiktok-live-studio
- ndi
- streaming
- limitation
---
# TikTok live studio doesn’t have a ndi option

### USER
TikTok live studio doesn’t have a ndi option

### GEMINI
The reason you don't see NDI is that TikTok Live Studio doesn't support it natively—it's a closed ecosystem designed to force you to use their tools. Since Restream is "revoked" and the Virtual Camera is lagging CS2, you're being bottlenecked by the "Virtual Camera" driver, which is notoriously inefficient for high-motion games. Here is the most efficient way to fix this without needing a stream key or a third-party site. 1. The "Projector" Method (Bypass Virtual Camera) Instead of using the "Virtual Camera" button, which uses a laggy software driver, use a Windowed Projector. This uses your GPU's direct output and is much smoother for CS2. In OBS: Right-click on your Aitum Vertical Canvas (or the Vertical scene). Select Windowed Projector (Source). A window will pop up showing only your vertical feed. In TikTok Live Studio: Add a new source -> Window Capture. Select the OBS Windowed Projector window. Critical: In TikTok Live Studio's Window Capture settings, make sure "Capture Method" is set to Windows 10 (Graphics Capture). This is the lowest-latency capture method available. 2. The "Priority" Fix (The Lag Killer) The reason CS2 lags is that Windows sees two apps (OBS and TikTok) and doesn't know which one to give the GPU to. Run both as Admin: Right-click OBS and TikTok Live Studio -> Properties -> Compatibility -> Run this program as an administrator. Windows Game Mode: Turn it ON. It specifically tells Windows to prioritize the game while allowing OBS to record in the background without stuttering. 3. Change your Encoder in TikTok Studio If TikTok Live Studio is trying to use your CPU (x264) while OBS uses your GPU (NVENC), your 12700K will choke during CS2 gunfights. In TikTok Live Studio, go to Settings -> Video. Ensure Encoder is set to NVIDIA NVENC (H.264). Set the Quality to 720p 60fps (at 4000-5000 kbps). TikTok mobile users cannot tell the difference between 720p and 1080p, but it will save your 3070 from overworking. 4. Use "Spout2" (The "Secret" Pro Way) If the Windowed Projector still lags, there is a specialized "bridge" called Spout2. It’s like NDI but stays entirely inside your GPU memory, meaning zero CPU lag. Install the OBS Spout2 Plugin. In OBS, add a "Spout2 Filter" to your Vertical Scene. In TikTok Live Studio, add a Spout2 Capture source (if it's not appearing, use the Spout2 Video Receiver app and capture that window). The Brutal Truth: You have a solid PC, but you’re running two "Studio" apps at once. If you don't run them both as Administrator, Windows will always throttle one of them, causing that CS2 lag. Try the Windowed Projector method first—it's the fastest way to ditch the Virtual Camera's overhead.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
