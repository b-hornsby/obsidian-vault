---
id: 567594
source: GEMINI
date: 2026-04-06
tags: ['tiktok-live', 'audio-output', 'desktop-audio']
category: streaming
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan couldn't find an audio output option and decided desktop sounds being broadcast was acceptable.
---
# yeah i dont see an output option and honestly i dont care if my desktop sounds are broadcast its not that deep 

### USER
yeah i dont see an output option and honestly i dont care if my desktop sounds are broadcast its not that deep 

### GEMINI
If you don't care about separating sounds and just want it to work, let's stop over-complicating it. We can skip Voicemeeter entirely and use the simplest path available in your Windows sound settings. The "No-Nonsense" Setup In OBS: Go to Settings > Audio. Set your Monitoring Device to your actual speakers or headphones (your FiiO DAC). Go to the Audio Mixer, right-click your Mic, and select Advanced Audio Properties. Set your Microphone to Monitor and Output. Result: You will now hear your own voice in your headphones. This is the only way to "push" the audio into the system for TikTok to grab it. In TikTok LIVE Studio: Click the Audio icon/settings in the bottom left. Add a Microphone source. Select Default or your FiiO DAC (whichever one is currently playing your game sound). TikTok will now "hear" everything you hear in your headphones—your game, your music, and (because of the OBS monitor setting) your processed mic. The Reality Check (Brutal Honesty) The Echo: Because you are "Monitoring" your mic in OBS, you will hear yourself talking in real-time. If you find that distracting, you must use the Virtual Cable/Voicemeeter method we discussed earlier to "silently" route it. The "Double Up": If you hear a weird robotic echo on the TikTok side, it's because TikTok is trying to capture your Desktop sound and your Mic at the same time. Mute everything in TikTok except for that one Microphone source. Why you "don't see an output option" TikTok LIVE Studio is designed to be "dummy-proof." It doesn't look for "Outputs" (speakers); it only looks for "Inputs" (microphones). That’s why we have to trick it by sending our OBS sound into a "Virtual Output" (like Voicemeeter B1 or a Virtual Cable) which then shows up as a "Microphone" in TikTok. If you can't stand hearing yourself talk: You have to go back to the VB-Cable plan. Set OBS Monitoring to Cable Input. Set TikTok Mic to Cable Output. Done. No echos in your ears, and TikTok hears everything perfectly. Are you okay with hearing your own voice in your headset while you stream? If not, the cable is your only exit.
