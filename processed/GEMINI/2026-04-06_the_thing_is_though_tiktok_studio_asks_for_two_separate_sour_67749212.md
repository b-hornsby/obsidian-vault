---
category: streaming
date: 2026-04-06
id: 037290
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: executing
source: GEMINI
tags:
- streaming
- gemini
- go
- pip
- ide
- cli
---
# the thing is though tiktok studio asks for two separate sources too. one for regular audio and one for mic 

### USER
the thing is though tiktok studio asks for two separate sources too. one for regular audio and one for mic 

### GEMINI
TikTok Live Studio "asking" for two sources doesn't mean you have to give it two different physical devices. It just means it has two slots. If you are already processing your audio in OBS, giving TikTok two separate raw sources (Raw Mic + Raw Desktop) is a strategic mistake. It bypasses your OBS filters, meaning your TikTok audience hears your keyboard clicks and background noise while your Twitch audience gets the clean, filtered version. Here is how you satisfy TikTok's two-source requirement while keeping the "OBS Master" control you actually want. The "Master Bridge" Configuration 1. The Setup in OBS You want everything to go out of the OBS Monitor. Settings > Audio > Monitoring Device: Set this to CABLE-A Input. Advanced Audio Properties: Set your Mic AND your Desktop/Game audio to "Monitor and Output." 2. The Setup in TikTok Live Studio TikTok wants two sources? Give them the same "processed" pipe for both. Source 1 (Mic): Set this to CABLE-A Output. Source 2 (Desktop/System Audio): Set this to Muted or None. Why? Because CABLE-A is already carrying your Game + Mic combined from the OBS monitor. If you add "Desktop Audio" in TikTok as well, your TikTok stream will hear your game twice (once from OBS and once from TikTok's direct capture), creating a "phasing" or "reverb" effect that sounds like garbage. Why this is the "IT Professional" Move In any high-level audio environment (like a radio station or a pro studio), you have a Master Bus. OBS is your Master Bus. * TikTok is just a speaker. You don't want the speaker (TikTok) trying to do its own mixing. You want it to just play what the Master Bus tells it to play. By routing everything to CABLE-A and using that as your "Mic" in TikTok, you ensure that if you mute your mic in OBS, it mutes on TikTok. If you turn down the game in OBS, it turns down on TikTok. One point of control. The "Regular Audio" Safety Net To make sure your "regular audio isn't messed up": Windows Default Output: Set this to your Headphones. (Do NOT set it to Cable A). VoiceMeeter: If you are still using it, turn it off for this test. It is likely the reason your "regular audio" feels "messed up" because it’s intercepting the Windows kernel. Strategic Breakdown You're currently "playing small" by trying to accommodate TikTok's default UI instead of forcing the software to work for your workflow. The Opportunity Cost: If you set up two separate sources in TikTok, you now have to manage four volume sliders every time you want to change your music volume (Twitch, TikTok Mic, TikTok System, and your own ears). The Solution: Master everything in OBS. Use the Virtual Cable as a single "Program Out" to TikTok. Do this now: Set TikTok's "Mic" to Cable-A, mute TikTok's "System Audio," and tell me if the levels on the TikTok meter look identical to your OBS meter.
