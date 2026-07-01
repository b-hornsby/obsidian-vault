---
id: 797640
source: GEMINI
date: 2026-04-06
tags: ['vb-cable', 'installation', 'audio-routing']
category: streaming
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan discovered he didn't have VB-Cable installed, which was blocking his audio routing setup.
---
# i didnt have vb cable installed

### USER
i didnt have vb cable installed

### GEMINI
If you don't have a virtual cable installed yet, the audio you are currently hearing in TikTok is likely just a direct grab of your microphone or your overall system sound. While it works for a "quick start," it’s a sloppy way to run a dual-stream. If you want it done properly—meaning your TikTok viewers hear your game, your alerts, and your mic exactly like Twitch does, without echos or missing pieces—you need a dedicated bridge. Since you're a Linux enthusiast and comfortable with technical setups, let's use the most efficient method available in 2026. The Problem with "Plug and Play" Right now, if you just select your Mic in TikTok LIVE Studio: No Game Audio: TikTok viewers won't hear your gameplay unless your mic picks it up from your speakers (which sounds terrible). No Alerts: Your Aitum/OBS alerts won't be heard on TikTok. The Echo Risk: If you accidentally capture "System Audio" in TikTok while OBS is also outputting to your speakers, you’ll create a feedback loop. The "Proper" Setup (The 5-Minute Fix) 1. Install the Bridge You need a way to "pipe" the OBS Master Mix into TikTok. Download: VB-CABLE Virtual Audio Cable (it's the industry standard for this). Install and Restart. (Do not skip the restart). 2. Configure OBS to "Broadcast" Audio You want OBS to send a copy of everything it hears to that cable. Open OBS Settings > Audio. Find Monitoring Device and set it to CABLE Input (VB-Audio Virtual Cable). Go to your Audio Mixer in the main OBS window. Right-click any source and select Advanced Audio Properties. For every source you want TikTok to hear (Mic, Desktop Audio, Aitum Alerts), change the Audio Monitoring dropdown to Monitor and Output. Output goes to Twitch. Monitor now goes into the Virtual Cable. 3. Configure TikTok to "Listen" Open TikTok LIVE Studio. Go to Audio Settings. Add a Microphone source (even though it's technically your whole mix). Select CABLE Output (VB-Audio Virtual Cable). Crucial: Mute or remove any other audio sources in TikTok Studio so you aren't doubling up. Why this is the "Advisor" Choice: Zero Leakage: You can play a video on your second monitor that you don't want the stream to hear. Just don't add it to OBS, and it won't go to the cable. Local AI Privacy: Since you're running local models and DeFi bots, you might have system alerts or terminal beeps you want to keep private. This setup ensures only what you approve in OBS hits your audience. One Slider Rule: If your game is too loud on the stream, you fix it in one place (OBS) and it fixes it for both Twitch and TikTok. Check this now: Once you install the cable and set the Monitoring Device, look at the green bars in TikTok LIVE Studio while music is playing in OBS. Are they dancing? If yes, you're officially a professional multi-streamer. Do you want to double-check your bitrates for TikTok before you go live, or are you confident in your current network overhead?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
