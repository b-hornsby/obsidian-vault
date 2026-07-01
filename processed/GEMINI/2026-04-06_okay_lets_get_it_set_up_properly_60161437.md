---
id: 939603
source: GEMINI
date: 2026-04-06
tags: ['audio-routing', 'setup', 'streaming']
category: streaming
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md']
summary: Bryan was ready to properly set up his streaming audio routing from scratch.
---
# okay lets get it set up properly 

### USER
okay lets get it set up properly 

### GEMINI
If we’re doing this properly, we need to stop relying on "Windows Default" and create a dedicated lane for your TikTok audio. Since you already have Voicemeeter Banana and Cable A in your ecosystem, we’re going to leverage those. Using what you already have is more efficient than installing a second "VB-Cable." Here is the professional-grade routing plan. 1. The Strategy: The "TikTok Bus" We are going to use Voicemeeter as your central hub. Twitch gets your clean OBS mix. TikTok gets a specific feed from a Voicemeeter "Bus." 2. OBS Configuration (The Send) Open OBS Settings > Audio. Set Monitoring Device to Voicemeeter Input (VB-Audio Voicemeeter VAIO). Go to your Audio Mixer, right-click, and select Advanced Audio Properties. For your Mic and Desktop Audio/Game, set Audio Monitoring to Monitor and Output. Result: Your audio now hits your Twitch stream ("Output") and flows into Voicemeeter ("Monitor"). 3. Voicemeeter Configuration (The Bridge) Open Voicemeeter Banana. In the Virtual Inputs section (middle columns), you should see your OBS audio hitting the "Voicemeeter VAIO" column. On that column, make sure the B1 button is selected. B1 is your "Virtual Output" that other programs can "listen" to. 4. TikTok LIVE Studio (The Receive) Open TikTok LIVE Studio. Go to Audio Settings. Add/Edit your Microphone source. Select Voicemeeter Output (VB-Audio Voicemeeter VAIO) as the device. Turn off any other "Desktop Audio" sources in TikTok Studio to prevent doubling or echoing. 5. Why This is the "High-Level" Way Independent Control: You can now use the sliders in Voicemeeter to make yourself louder on TikTok without affecting your Twitch stream. TikTok’s compression is aggressive; often you need to boost your mids to sound clear there. Mute Logic: If you want to talk to Twitch but not TikTok, you just click the "B1" button in Voicemeeter. You are now a "Master of your Domain." Clean VODs: This setup ensures your TikTok stream doesn't accidentally pick up copyrighted music if you have your Spotify routed differently (like your Cable A setup), which protects your TikTok account from strikes. The Advisor's Reality Check You’re running a complex audio matrix now on top of CachyOS/Windows dual-boot, AI agents, and multistreaming. The Risk: Complexity breeds failure points. If your audio stops working, 99% of the time it’s because the Voicemeeter Engine crashed or Windows changed your default playback device. Action: Right-click your Sound icon in the Windows Taskbar. Ensure your Playback Device is still your FiiO DAC (so you can hear) and not Voicemeeter. Voicemeeter should only handle the routing, not your ears. Test it now: Open TikTok LIVE Studio and speak. Do the bars move? If so, play a game sound—do the bars move again? If yes, you are officially "wired" correctly. What does the "System" load look like in your Task Manager with all this running? Still under 70%?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
