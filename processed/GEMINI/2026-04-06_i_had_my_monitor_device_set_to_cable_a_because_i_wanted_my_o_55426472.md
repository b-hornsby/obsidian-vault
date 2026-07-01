---
category: streaming
date: 2026-04-06
id: 541762
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan set his OBS monitoring device to Cable A to transfer mic settings to
  TikTok Live Studio but it wasn't working.
tags:
- obs-monitoring
- vb-cable
- tiktok-live
- audio-routing
---
# i had my monitor device set to cable a because i wanted my obs mic settings to transfer over to tiktok live studio

### USER
i had my monitor device set to cable a because i wanted my obs mic settings to transfer over to tiktok live studio

### GEMINI
This is exactly where the "collision" in your routing is happening. You’re trying to use Cable A as a Microphone Pipe and a Monitoring Device at the same time, which is causing your Discord "wackiness" and the Brave routing confusion. In a professional IT environment, you don't use the same "IP address" for two different servers. You need to segment your traffic. The "Clean Split" Architecture Since you have two cables (A and B), let’s use them for their specific "jobs" so your FiiO DAC (your ears) stays clear of the mess. 1. The Mic Pipe (OBS to TikTok/Discord) In OBS: Go to Settings > Audio > Advanced. Set Monitoring Device to CABLE-A Input. In OBS Mixer: Click the gear on your Mic > Advanced Audio Properties. Set it to Monitor and Output. In TikTok/Discord: Set Input Device to CABLE-A Output. The Result: Only your filtered voice goes through this pipe. 2. The Music Pipe (Brave to Visualizer) In Windows Volume Mixer: Set Brave's Output to CABLE-B Input. In OBS: Add an Audio Input Capture called "Brave Music" set to CABLE-B Output. In OBS Mixer: Set "Brave Music" to Output Only (Do NOT monitor it to Cable A, or your music will play through your "Mic" on TikTok/Discord). The Visualizer: Point your Waveform plugin only at the "Brave Music" source. 3. Your Ears (The "Safety" Path) Windows Default Output: Set this to your FiiO DAC. In OBS: If you want to hear your Brave music in your headphones while you stream: You cannot use Cable A as your "Monitoring Device" if you want to hear music, because Cable A is currently acting as your "Virtual Mic." The Fix: Change your OBS Monitoring Device back to your FiiO DAC. The "Aha!" Moment (The IT Logic) You are currently "monitoring" to Cable A to trick TikTok into hearing your mic. But if you do that, everything you "Monitor" in OBS (Mic, Brave, Game) gets shoved into that one pipe. The Conflict: If you monitor Brave to Cable A so TikTok hears the music, your Discord friends will also hear your music through your "Mic." The Professional Move: 1. Stop using the OBS "Monitor" to talk to TikTok. 2. Use the OBS-Virtual Audio plugin or just give TikTok two separate sources: Mic (Cable A) and System Audio (FiiO DAC). The Strategic Mirror You’re trying to force a "one-pipe" solution on a "multi-stream" problem. The Risk: You're playing it "safe" by sticking to one monitoring path, but it's creating a bottleneck that makes your Discord sound like garbage. The Move: Stop monitoring your mic to a cable. Use the Windows Volume Mixer to send Brave to Cable B, and use Cable A only as a dedicated output for your Mic via a specialized OBS filter (like "Audio Monitor" plugin) or a separate track. Are you ready to stop "Monitoring" to Cable A and actually segment these signals like a pro?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/personal/streaming|Streaming]]
