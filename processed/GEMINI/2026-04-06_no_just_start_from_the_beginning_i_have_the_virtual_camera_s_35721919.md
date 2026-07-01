---
id: 464202
source: GEMINI
date: 2026-04-06
tags: ['obs', 'virtual-camera', 'tiktok-live', 'mic-audio', 'setup-guide']
category: streaming
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan wanted a step-by-step guide to route OBS mic audio to TikTok Live Studio starting from the virtual camera setup.
---
# no just start from the beginning. i have the virtual camera set up. from there what do i need to do to set this up properly? i want my obs mic audio to be picked up through tiktok live studio as well 

### USER
no just start from the beginning. i have the virtual camera set up. from there what do i need to do to set this up properly? i want my obs mic audio to be picked up through tiktok live studio as well 

### GEMINI
Setting up properly means creating a "digital bridge" so that TikTok hears exactly what OBS hears, including your mic filters, game audio, and alerts. Since the Virtual Camera only carries video, we have to manually route the audio. Here is the clean, step-by-step "Ground Zero" setup. Phase 1: The "Bridge" (Installation) Windows cannot natively "send" audio from one app to another without a virtual cable. Download: VB-CABLE Virtual Audio Cable (Free/Donationware). Install: Run the setup as Administrator. RESTART your PC: This is non-negotiable. The driver won't show up in your settings until you reboot. Phase 2: OBS Configuration (The "Send") We need to tell OBS to "broadcast" a copy of its audio mix to that virtual cable. Open OBS Settings > Audio. Under Advanced, find Monitoring Device. Change it to CABLE Input (VB-Audio Virtual Cable). Click Apply. Now, go to your Audio Mixer in the main OBS window. Click the three dots (or right-click) on your Microphone and Desktop Audio. Select Advanced Audio Properties. For your Microphone and Desktop Audio, change the Audio Monitoring dropdown to Monitor and Output. Output: Goes to Twitch. Monitor: Now "streams" into the Virtual Cable we just set up. Phase 3: TikTok LIVE Studio (The "Receive") Now we make TikTok "listen" to the other end of that cable. Open TikTok LIVE Studio. In the Audio section (usually bottom left or in Settings), click Add Source. Select Microphone. From the device list, choose CABLE Output (VB-Audio Virtual Cable). Crucial: Mute or remove any other "Desktop Audio" or "System" sources in TikTok Studio. If you don't, you will hear a double-echo because TikTok will be trying to capture your sound twice. Why this is the "Advisor" Level Setup Privacy: Because you're only "Monitoring" specific sources in OBS, if you play a YouTube video on your second monitor that isn't in your OBS mixer, TikTok won't hear it. This protects your stream from accidental pings or Discord audio leaking. Audio Quality: TikTok viewers will hear your processed mic (with your noise gates/compressors) instead of a raw, noisy Windows mic. Sync: This method keeps the audio closer to the video feed than other workarounds. The Mirror: Don't Get Distracted You've spent a lot of energy on this setup. The Opportunity Cost: A perfect technical setup with 0 viewers is a hobby, not a business. Once these bars are moving in TikTok Studio, stop tweaking. Your mission is to hit 1,000 followers so you can get a real Stream Key and delete all these workarounds. Immediate Action: Talk into your mic. Are the green bars moving in both OBS and TikTok LIVE Studio right now?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
