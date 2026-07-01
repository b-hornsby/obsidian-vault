---
category: streaming
date: 2026-04-06
id: 459743
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was figuring out how to stream to TikTok after being denied a streamer
  key, assuming he'd need to use Restream.
tags:
- tiktok
- streamer-key
- denied
- restream
- workaround
---
# I was denied a streamer key for TikTok so I have to use restream I’m assuming

### USER
I was denied a streamer key for TikTok so I have to use restream I’m assuming

### GEMINI
Actually, being denied a key is a blessing in disguise because Restream has a direct "login" integration for TikTok that bypasses the need for a manual stream key and Server URL altogether. Since you have an RTX 3070, this is the most efficient way to get your CS2 performance back while maintaining your vertical setup. The "No-Key" Restream Strategy In 2026, Restream acts as an authorized partner for TikTok. Instead of pasting keys, you "handshake" the accounts. Add TikTok to Restream: Go to your Restream Dashboard -> Add Channel. Select TikTok. It will ask you to Login and Authorize. This uses an "App Connection" rather than an RTMP key. Once authorized, Restream can push to your TikTok account directly. The OBS Setup (Using Aitum Vertical): In OBS, go to your Aitum Vertical settings (the cog wheel on the vertical dock). Set the Streaming output to Restream. Log in to Restream through OBS if you haven't already. Why this kills the lag: No Virtual Camera: You aren't "mirroring" your screen to another app (TikTok Live Studio). One Encoder: You are sending one vertical video stream to Restream's servers. Restream then does the heavy lifting of distributing it to TikTok. Close TikTok Live Studio: You don't even need that program open. It’s a resource hog that's likely the primary cause of your CS2 stuttering. If You Still Encounter Lag: The "NVENC" Reality Check Even with Restream, you are still encoding two separate videos (one horizontal for Twitch, one vertical for TikTok). Your 12700K/3070 can handle this, but only if configured correctly: Encoder Priority: Ensure both your main OBS output and your Vertical output are set to NVIDIA NVENC H.264 (or AV1 if available). Bitrate Management: If your upload speed is under 20Mbps, sending two streams (e.g., 6000kbps to Twitch + 6000kbps to TikTok) will cause network-induced lag in CS2. Fix: Use Restream's single-stream feature where you send one feed and it splits it, OR lower your vertical bitrate to 4000kbps. TikTok mobile viewers won't notice the difference. Windows "Game Mode": Ensure it is ON. It specifically helps CS2 stay prioritized when OBS is running in the background. The Brutally Honest Advisor Bottom Line You were trying to run a "daisy-chain" setup: Game -> OBS -> Virtual Camera -> TikTok Live Studio -> TikTok. That is four points of failure and four layers of latency. By using Restream + Aitum Vertical, you cut it down to: Game -> OBS -> Restream -> TikTok. Do this now: Uninstall TikTok Live Studio. It’s holding your PC hostage. Use your browser to monitor TikTok chat/alerts if you need to, but keep that software off your RAM.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
