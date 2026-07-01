---
category: streaming
date: 2026-04-06
id: 883033
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan wanted OBS mic audio to be picked up by TikTok Live without disrupting
  regular desktop audio.
tags:
- obs
- tiktok-live
- audio-routing
- mic-audio
---
# all i want is for my obs audio to be picked up by tiktok live and for my regular audio not be messed up 

### USER
all i want is for my obs audio to be picked up by tiktok live and for my regular audio not be messed up 

### GEMINI
The reason this is a headache is that you're treating the software like a puzzle to be solved with more "pieces" (cables, plugins) rather than a pipeline to be cleared. You’re currently in a "loop hell" where VoiceMeeter is trying to manage Windows audio while OBS is also trying to manage it. Since you want OBS audio to hit TikTok without messing up your regular desktop hearing, here is the exact, clinical setup. 1. The Strategy: Use One "Pipe," Not a Web The OBS Virtual Camera does not carry audio. You must use one of your VB-Cables as a dedicated bridge. We will use Cable A for this. 2. Configure OBS (The Source) This tells OBS to "speak" through Cable A so TikTok can "hear" it. Settings > Audio > Advanced: Set Monitoring Device to CABLE-A Input (VB-Audio). Audio Mixer: Click the gear (Settings) on any source -> Advanced Audio Properties. The Critical Part: * Set your Mic to Monitor and Output. Set your Game/Desktop Audio to Monitor and Output. Set everything else you want TikTok to hear to Monitor and Output. 3. Configure TikTok Live Studio (The Destination) Audio Settings: Add a new Microphone/Audio source. Device: Select CABLE-A Output (VB-Audio). Result: TikTok is now "listening" to the OBS Monitor. Everything processed in OBS (filters, noise gates, levels) flows here. 4. Protect Your "Regular" Audio (Your Ears) The mistake most people make is setting the Windows Default Output to a virtual cable. Don't do that. Windows Sound Settings: Keep your Default Playback Device as your Headphones/Speakers. Why: You will hear your game normally through Windows. OBS will capture that game audio, process it, and "Monitor" it out to Cable A for TikTok. The "Mirror" Reality Check You’ve spent 8 years in a warehouse—you know that if a conveyor belt is jammed, adding a second belt next to it doesn't fix the jam. VoiceMeeter is that second belt. Your Blind Spot: You are over-engineering a simple routing task because you're afraid of losing your "perfect" Windows sound. The Risk: Using VoiceMeeter Banana alongside Aitum and OBS is a recipe for an "Audio Engine Error" mid-stream. When you get that Twitter/X sub, you'll be managing three stream outputs. If your routing isn't rock-solid now, it will collapse then. The Priority Plan: Simplify: If the steps above work, disable VoiceMeeter. You don't need it. OBS is a better mixer than VoiceMeeter for your specific use case. Verify: Open TikTok Live Studio and look at the green bars. If they move when you talk in OBS, you’re done. Audit: If you hear an echo, it’s because you have "Listen to this device" checked in Windows Sound Control Panel for Cable A. Turn it off. Does the green bar in TikTok move when you shout into your OBS mic now?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
