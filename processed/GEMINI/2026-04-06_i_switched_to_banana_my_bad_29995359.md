---
id: 979141
source: GEMINI
date: 2026-04-06
tags: ['voicemeter-banana', 'audio-routing']
category: streaming
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan clarified he had switched to Voicemeter Banana for his audio routing setup.
---
# i switched to banana my bad 

### USER
i switched to banana my bad 

### GEMINI
That’s the right move—Banana gives you three hardware inputs and two virtual outputs, which means more breathing room for your TikTok bridge. Here is the precise, high-level routing using your Banana setup: 1. The OBS "Send" In OBS Settings > Audio > Advanced: Set Monitoring Device to CABLE-A Input (VB-Audio Cable A). In OBS Audio Mixer: Right-click your Mic and Desktop Audio > Advanced Audio Properties. Change Audio Monitoring for both to Monitor and Output. Result: OBS is now "broadcasting" its audio into the virtual Cable A. 2. The Voicemeeter "Bridge" (Looking at your image) Stereo Input 1 (Far Left): Click the "Select Input Device" text. Choose KS: CABLE-A Output (or WDM if KS is unavailable). Routing Buttons: On that same column, click B1 so it is ON (lit up green). Make sure A1, A2, and A3 are all OFF (dark). Why? This sends the OBS audio to your "Virtual Output B1" specifically for TikTok without looping it back into your own ears. 3. The TikTok "Receive" In TikTok LIVE Studio: Go to Audio Settings. Add a Microphone source. Choose Voicemeeter Output (VB-Audio Voicemeeter VAIO). Note: This corresponds to the B1 button you just turned on. Disable/Mute all other audio sources in TikTok Studio. The Advisor's Strategic Check You have a lot of "green sliders" now. Here is the objective truth about managing this: Master Control: Your Hardware Input 1 slider in Voicemeeter is now your "TikTok Master Volume." If viewers say you're too quiet but Twitch says you're perfect, move that slider up. Hardware Out (Top Right): Make sure your A1 (Hardware Out) is set to your FiiO DAC. If you don't set a hardware out, Voicemeeter can sometimes act unstable. The Trap: Do not accidentally set your Windows "Default Playback Device" to Cable A. Keep Windows set to your FiiO DAC or "Voicemeeter Input." Cable A should only be used as the bridge between OBS and Voicemeeter. Final Audit: Open TikTok LIVE Studio and speak. Look at the B1 meter in the MASTER SECTION (far right of your image). Are the bars moving when you speak? If the bars are moving in Voicemeeter but not in TikTok, it means TikTok is looking at the wrong device—double-check that it's set to Voicemeeter Output. How does the latency feel between your OBS mic meter and the TikTok meter? It should be nearly identical now.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
