---
category: streaming
date: 2026-04-06
id: 381893
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was troubleshooting persistent video lag when using NDI for streaming.
tags:
- ndi
- streaming-lag
- obs
- latency
---
# Yeah the lag is still there even with ndi

### USER
Yeah the lag is still there even with ndi

### GEMINI
Since the NDI route didn't kill the lag, we need to address the "hidden" resource war happening on your PC. You have a solid 3070 and a 12700K, so you shouldn't be lagging—which means your GPU is likely "starving" because of how Windows is prioritizing these apps. Here is the precise, high-level advisor checklist to stop the stutter in CS2. 1. The "Priority" Kill-Switch (Admin Mode) If you haven't done this yet, nothing else will work. Close CS2, OBS, and TikTok Live Studio. Right-click the OBS shortcut -> Properties -> Compatibility -> Check "Run this program as an administrator." Do the exact same for the TikTok Live Studio shortcut. Why: Windows 10/11 has a feature called "Hardware-accelerated GPU scheduling." If OBS isn't in Admin mode, Windows will give 100% of the GPU to CS2, leaving OBS to "stutter" as it tries to grab leftover frames for the NDI/Virtual Cam feed. 2. Cap Your FPS (The "Breathing Room" Rule) This is the biggest mistake high-end players make. Open CS2 and go to the console (~). Type fps_max 165 (or whatever your monitor's refresh rate is). The Logic: If you let CS2 run at 400 FPS, your GPU is at 99% load. OBS needs about 5-10% of your GPU to encode the stream and handle the Aitum Vertical plugin. If the GPU is at 99%, OBS "drops" frames, which you feel as lag in the game. Give the GPU 5% breathing room. 3. Change the Capture Method (The "Legacy" Lag) In TikTok Live Studio, where you added the NDI or Window Capture: Click on the source settings. Look for "Capture Method." If it’s on "Auto" or "BitBlt," it will lag. Change it to "Windows 10 (Graphics Capture)" or "DXGI Desktop Duplication." These are the modern, low-latency ways to grab video. 4. TikTok Studio Hardware Encoding If TikTok Live Studio is trying to use your CPU (x264), it will fight CS2 for processing power. In TikTok Live Studio Settings -> Video -> Encoder. Force it to NVIDIA NVENC (H.264). Set the quality to 720p 60fps. (Sending 1080p to a phone screen is a waste of your resources). 5. Disable "HAGS" (Hardware-Accelerated GPU Scheduling) Sometimes the very feature meant to help actually breaks dual-streaming setups. Go to Windows Settings -> System -> Display -> Graphics -> Change default graphics settings. Toggle Hardware-accelerated GPU scheduling to OFF. Restart your PC. Many streamers find this fixes the "micro-stutter" in high-motion games like CS2. The Advisor's Bottom Line You are currently trying to run three GPU-heavy things: CS2 (Source 2 engine), OBS (with Aitum Vertical plugin), and TikTok Live Studio. The Reality Check: TikTok Live Studio is poorly optimized "bloatware." If the lag persists after doing the steps above, the issue isn't your PC—it's the software. Since Restream is out, your next move should be trying Prism Live Studio. It is much lighter than TikTok's official app and usually handles the "Virtual Camera" or "NDI" handoff from OBS without the massive performance hit. Are you running the game in Fullscreen or Windowed Borderless? (Fullscreen is almost always better for stream stability).


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
