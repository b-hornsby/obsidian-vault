---
category: streaming
date: 2026-04-06
id: 560064
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan encountered a 'not approved or revoked' error on Restream when trying
  to connect TikTok.
tags:
- restream
- not-approved
- revoked
- tiktok
- streaming-error
---
# When I tried it it says not approved or revoked now on restream

### USER
When I tried it it says not approved or revoked now on restream

### GEMINI
The "Not approved or revoked" message means TikTok’s moderation system has manually flagged or automated a block on your account’s third-party API access. This usually happens if you haven't met their minimum requirements (like 1,000 followers or consistent "gaming" content) or if you’ve had a minor guideline strike in the past. Since Restream and the direct Stream Key are currently blocked for you, we have to go back to the only method that works—but we’re going to strip it down so it doesn't kill your CS2 performance. The "Surgical" Fix for Virtual Camera Lag Your PC (12700K/3070) is lagging not because of the task, but because of the priority. Windows and the "Virtual Camera" driver are fighting. Here is the most efficient way to make it work: 1. Force GPU Priority (The "Admin" Fix) This is the single most important step. Close OBS and TikTok Live Studio. Right-click the OBS shortcut -> Run as Administrator. Right-click the TikTok Live Studio shortcut -> Run as Administrator. Why: This forces Windows to give OBS the GPU "headroom" it needs for the Virtual Camera before CS2 tries to take it all. 2. Optimize TikTok Live Studio (The "Receiver") TikTok Live Studio defaults to settings that eat resources. Open TikTok Live Studio. Go to Settings > Video. Set quality to 720p 60fps (TikTok mobile viewers can't tell the difference between 720p and 1080p, but your GPU will). Ensure Encoder is set to NVIDIA NVENC (H.264). If it's on "Intel" or "Default," change it. Disable "Scene Enhancement" or "Video Smoothing." These are AI filters that will absolutely tank your CS2 frames. 3. The OBS "Aitum" Handoff In OBS, make sure you are using the Aitum Vertical plugin. Click the Gear icon in the Vertical window. Turn on the Virtual Camera only for the Vertical canvas. Do not use the main OBS Virtual Camera (this sends your horizontal layout). The "Brutally Honest" Reality Check If you do the above and CS2 is still laggy, your issue is Resource Contention. Even with a 3070, running two encoding apps simultaneously is messy. If the above doesn't work, do this: Use NDI instead of Virtual Camera: 1. Download the NDI Runtime and OBS-NDI plugin. 2. In OBS, go to Tools > NDI Output Settings and turn on the "Main Output." 3. In TikTok Live Studio, add an NDI Source. Result: NDI is a professional-grade video-over-IP protocol. It’s significantly more stable than the "Virtual Camera" driver, which is basically a hack for Zoom calls. Your Action Plan Run both as Admin. (Try this first, it fixes 90% of lag). Lower TikTok Studio to 720p. Check for TikTok Strikes. Go to the TikTok Live Center to see why your Restream access was revoked. If you have 0 violations, you can usually re-apply for access in 30 days. How many followers are you at on TikTok currently? Knowing that helps me determine if we can force a "Live Producer" (Direct Key) unlock for you.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
