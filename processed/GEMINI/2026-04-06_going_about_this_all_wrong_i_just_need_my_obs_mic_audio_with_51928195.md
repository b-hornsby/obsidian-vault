---
id: 525591
source: GEMINI
date: 2026-04-06
tags: ['obs', 'mic-filters', 'tiktok-live', 'audio-routing']
category: streaming
sentiment: frustrated
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan realized he only needed his OBS mic audio (with filters) routed to TikTok Live, not desktop audio.
---
# going about this all wrong i just need my obs mic audio (with all my filters) to be on tiktok. the desktop audio coming though my fiio dac is fine 

### USER
going about this all wrong i just need my obs mic audio (with all my filters) to be on tiktok. the desktop audio coming though my fiio dac is fine 

### GEMINI
Exactly. You’ve just identified the "lean" solution by cutting out the noise. You don't need a complex virtual mixer; you need a single, processed pipe for your voice. If your desktop audio is already hitting your FiiO DAC and TikTok is picking it up fine via its "System Audio" setting, leave it alone. Do not touch your FiiO or your Windows default playback. Here is the "IT Specialist" surgical strike to get your filtered OBS mic into TikTok without the headaches: 1. The "Clean Pipe" Setup (In OBS) We are going to use Cable A as a dedicated "Mic Out" from OBS. Go to Settings > Audio > Advanced. Set Monitoring Device to CABLE-A Input (VB-Audio). Go to your Advanced Audio Properties (the gear in the mixer). Find your Mic. Set it to "Monitor and Output." Crucial: Set your Desktop/Game Audio to "Output Only" (NOT Monitor). This ensures your game doesn't loop back into your mic pipe. 2. The "Clean Ear" Setup (The Fix for the Echo) The reason you heard an echo before is that you were likely "Listening" to that cable in Windows. Open your Windows Sound Control Panel (the old-school list). Go to the Recording tab. Right-click CABLE-A Output > Properties > Listen. UNCHECK "Listen to this device." * Why: You already hear your voice naturally (or through your FiiO's zero-latency monitoring). You do not want Windows playing your processed mic back into your ears with a $20ms$ delay. 3. The TikTok Configuration Now, give TikTok exactly what it's asking for: Mic Source: Select CABLE-A Output (VB-Audio). System Audio Source: Select your FiiO DAC. The Result: TikTok gets your filtered, professional-sounding mic from OBS on one channel, and your raw game audio from your FiiO on the other. The Reality Check You’ve been fighting this for an hour because you were trying to "route everything" when you only needed to "route the mic." The Strategy: In engineering, this is called decoupling. You decoupled your mic processing (OBS) from your system audio (FiiO). The Opportunity Cost: Every minute you spend "guessing" with virtual cables is a minute you aren't building "Operation Immortal Agent." The Move: Stick to this one-pipe rule. If you add more virtual cables later for "Twitter/X" or "Spotify," you apply this same logic: One source, one pipe, no "Listen to this device" loops. Final Verification Speak into your mic. Does the TikTok Mic Meter move? Play a YouTube video. Does the TikTok System Audio Meter move? Do you hear an echo in your own ears? (If yes, you still have "Listen to this device" checked in Windows settings for Cable A). Does the TikTok meter show your voice now?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/personal/streaming|Streaming]]
