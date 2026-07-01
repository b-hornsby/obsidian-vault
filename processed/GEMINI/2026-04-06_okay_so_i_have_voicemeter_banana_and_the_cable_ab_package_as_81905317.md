---
id: 500251
source: GEMINI
date: 2026-04-06
tags: ['voicemeter-banana', 'vb-cable', 'audio-routing', 'setup-guide']
category: streaming
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan had Voicemeter Banana and Cable A+B installed and wanted a walkthrough to set up proper audio routing.
---
# okay so i have voicemeter banana and the cable a+b package as well. walk me through it from there 

### USER
okay so i have voicemeter banana and the cable a+b package as well. walk me through it from there 

### GEMINI
Since you already have Voicemeeter Banana and the Cable A+B package, you have the "industrial grade" setup. We are going to use these to create a dedicated, filtered audio "pipe" from OBS to TikTok without it ever touching your main speakers (preventing echos). Here is the step-by-step to wire it properly: 1. The OBS "Send" (Monitoring) We need OBS to output its audio into one of your virtual cables so Voicemeeter can pick it up. In OBS: Go to Settings > Audio > Advanced. Set Monitoring Device to CABLE-A Input (VB-Audio Cable A). Go to your Audio Mixer in the main OBS window, right-click, and select Advanced Audio Properties. Find your Microphone and Desktop Audio. Change the Audio Monitoring column to Monitor and Output. Output goes to Twitch. Monitor now sends a copy to Cable A. 2. The Voicemeeter "Bridge" Now we tell Voicemeeter to take that OBS audio and prepare it for TikTok. Hardware Input 2: Click the title at the top and select KS: CABLE-A Output (or WDM if KS isn't there). On that channel (Input 2), Deselect A1 (so you don't hear yourself twice) and Select B1. B1 is your "Virtual Output" that TikTok will listen to. 3. The TikTok "Receive" Finally, we tell TikTok to use the "B1" output from Voicemeeter as its microphone. In TikTok LIVE Studio: Go to Audio Settings. Add a Microphone source. Select Voicemeeter Output (VB-Audio Voicemeeter VAIO). Note: This corresponds to the "B1" button you clicked in Voicemeeter. Disable/Mute all other audio sources in TikTok Studio to prevent echos. Why this is the "Pro" way: Isolated Control: You can now use the Hardware Input 2 slider in Voicemeeter to boost your volume for TikTok viewers specifically without making it too loud for Twitch. Mic Filters: Because you are monitoring your mic from OBS, all your VSTs, noise gates, and compressors are applied before the audio hits TikTok. The "Cousin" Logic: You’re using Cable A specifically for the bridge, leaving Cable B and Voicemeeter VAIO/AUX free for other high-level tasks (like separating Spotify from your VODs or routing Discord). The Advisor's Cold Truth You have a complex signal chain now. The Risk: If you forget to open Voicemeeter before you stream, TikTok will be silent. The Check: Look at the "B1" meter in Voicemeeter while you talk. If those green bars are moving, TikTok is receiving your audio. If they aren't, the "Monitor" setting in OBS is likely off. Action Item: Open TikTok LIVE Studio and play a game sound in OBS. Do the bars in TikTok move? If they do, you are officially configured. Are you seeing any "Red" peaking on the TikTok side, or is the level hitting the Yellow comfortably?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
