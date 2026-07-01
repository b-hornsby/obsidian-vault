---
id: 401071
source: GEMINI
date: 2026-04-06
tags: ['voicemeter', 'vb-cable', 'tiktok-live', 'twitter-streaming', 'audio-routing', 'music-exclusion-vod']
category: streaming
sentiment: frustrated
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan was trying to set up a cable routing system to play music on stream but exclude it from TikTok VODs, while planning for future Twitter multistreaming.
---
# damn yeah i guess i need that cable setup. its just mad confusing especially because i want to be able to play music on stream but not include it in vods for tiktok live. remember im trying to stream on twitter on tiktok but im pinning twitter for now i dont have the premium sub required. solely focused on getting things proactively set up but not worried about twitter right now  

### USER
damn yeah i guess i need that cable setup. its just mad confusing especially because i want to be able to play music on stream but not include it in vods for tiktok live. remember im trying to stream on twitter on tiktok but im pinning twitter for now i dont have the premium sub required. solely focused on getting things proactively set up but not worried about twitter right now  

### GEMINI
I hear you—it feels like you're wiring a spaceship just to go live. But if you want to play music on Twitch/Twitter while keeping your TikTok and your future VODs "clean" from copyright strikes, you have to be the architect of your own audio. Since you have Voicemeeter Banana and Cable A+B, you have everything needed to build a "Filtered Bridge." The Strategic Logic We are going to create two separate "Buses" (think of them as distinct lanes of travel): Lane 1 (The Full Mix): Mic + Game + Music. This goes to your headphones and eventually Twitch. Lane 2 (The Clean Mix): Mic + Game (NO Music). This goes to TikTok. Step 1: Isolate Your Music in OBS TikTok LIVE Studio doesn't have a "VOD Track" feature like Twitch does. If TikTok hears it, it records it. So, we have to stop the music from ever reaching TikTok's "ear." In OBS, add your music (Spotify/YouTube) as an Application Audio Capture source. Right-click the Mixer > Advanced Audio Properties. The Secret Sauce: * Mic & Game: Set to Monitor and Output. Music: Set to Output Only. Result: Because Music is NOT being "Monitored," it will not be sent to the Virtual Cable we are about to set up. Step 2: The "Clean" Pipe to TikTok Now we send the "Monitored" audio (everything except music) to Voicemeeter. In OBS Settings > Audio > Advanced: Set Monitoring Device to CABLE-A Input. In Voicemeeter Banana: Set Hardware Input 1 to CABLE-A Output. Click the B1 button (make sure A1/A2/A3 are OFF). In TikTok LIVE Studio: Set your Microphone to Voicemeeter Output (VB-Audio Voicemeeter VAIO). Step 3: Handling the Twitter/Twitch Side Since you're pinning Twitter for now, this setup already works for Twitch. When you eventually add Twitter via Aitum: Twitter will take your Main OBS Output (which includes music). TikTok will take your Voicemeeter B1 Output (which is clean). The "Advisor" Audit (Brutal Honesty) The Opportunity Cost: You are choosing a complex setup to save time later. The risk is that if one driver (Cable A or Voicemeeter) glitches, your TikTok goes silent. The Check: Look at your Voicemeeter bars while music is playing. If you did Step 1 correctly, the bars in Voicemeeter should not move when the music hits, but should move when you talk. One final thing: Since you're in Akron and likely dealing with standard home upload speeds, streaming to Twitch (Horizontal) and TikTok (Vertical) simultaneously via Aitum/Virtual Cam is going to double your bitrate needs. Do you know what your current Upload Speed is? We need to make sure your DeFi bot and your two streams aren't fighting for the same 10-15 Mbps upload pipe.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
