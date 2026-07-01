---
category: streaming
date: 2026-04-06
id: 602558
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was experiencing delay/latency when using OBS virtual camera for streaming.
tags:
- virtual-camera
- obs
- latency
- streaming-delay
---
# why is there a delay when i use the virtual camera?

### USER
why is there a delay when i use the virtual camera?

### GEMINI
The delay you're seeing—usually between 200ms and 1,000ms—is a mechanical reality of how "Virtual Cameras" work. You aren't just streaming; you are asking your PC to perform a complex handoff between two different programs in real-time. Here is the objective breakdown of why that delay exists and how to kill as much of it as possible. 1. The "Double Encode" Tax When you stream normally, OBS encodes your video once and sends it to a server. When you use the Virtual Camera + TikTok LIVE Studio: OBS renders your frame. Aitum/OBS converts that frame into a "Virtual Webcam" signal (this is the first delay). TikTok LIVE Studio has to "capture" that webcam signal, re-process it, and then encode it again to send to TikTok. The Fix: Hardware Encoding: Ensure TikTok LIVE Studio is using your NVIDIA NVENC (since you have a 3070). If it’s using your CPU (x264), the delay will be massive. Reduce OBS Load: Since you're running local AI and DeFi bots (Operation Immortal Agent), your GPU/CPU overhead is likely tighter than you think. Every millisecond of processing time adds to that "buffer" you're seeing. 2. Aitum Vertical Syncing The Aitum plugin creates its own separate canvas. If your main OBS canvas is set to 60fps but your Vertical canvas or your TikTok Studio is set to 30fps, the mismatch forces the software to hold frames to keep them in sync, causing a visible "floaty" delay. The Fix: Go to Settings > Video in OBS and ensure your Base and Output resolutions are 1920x1080 at 60fps. Go to your Aitum Vertical Settings and ensure it is also locked at 60fps. Match these exactly in TikTok LIVE Studio. 3. Audio Desync (The Real Problem) The most annoying "delay" isn't the video—it’s when your mouth moves and the sound comes out a second later. Why: Your audio goes straight to the stream, but your video has to do the "Virtual Camera" dance, making the video slower than the audio. The Strategy: Open OBS Advanced Audio Properties. Add a Sync Offset to your microphone (start with 200ms). This "delays" your voice so it matches the delayed video hitting TikTok. The "Brutal Honesty" Reality Check The Virtual Camera is a workaround, not a professional solution. It will never be as fast as a direct RTMP stream key. Stop chasing "zero" delay: You won't get it with this setup. Focus on Sync. As long as your audio and video match, the viewers won't care if they see you 500ms later than Twitch does. Don't over-optimize: If you spend 10 hours trying to shave 100ms off a virtual camera delay instead of actually streaming and getting to that 1,000-follower mark, you're wasting time. Next Step: Check your TikTok LIVE Studio settings. Is it using "Compatibility Mode" or "Quality Mode"? Switch to Performance/Quality and make sure that NVIDIA encoder is selected.
