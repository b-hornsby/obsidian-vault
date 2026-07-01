---
id: 930973
source: GEMINI
date: 2026-04-06
tags: ['tiktok-live', 'obs', 'virtual-camera', 'aitum', 'audio-routing']
category: streaming
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan simplified his goal to just getting OBS audio picked up by TikTok Live Studio through the virtual camera.
---
# okay so no worries about tiktok vods then. i just want my audio to be picked up from obs to tiktok live studio due to the fact im using a virtual camera to mirror my aitum multistream/vertical setup 

### USER
okay so no worries about tiktok vods then. i just want my audio to be picked up from obs to tiktok live studio due to the fact im using a virtual camera to mirror my aitum multistream/vertical setup 

### GEMINI
Since you've moved to Voicemeeter Banana and you have Cable A, we can finally stop the guessing games. We are going to treat Cable A as a private "tunnel" between OBS and Voicemeeter, and then use Voicemeeter to talk to TikTok. Here is the exact, step-by-step path from where you are right now. 1. The OBS "Handshake" First, tell OBS to send a copy of everything it hears to your virtual cable. Open OBS Settings > Audio > Advanced. Find Monitoring Device and set it to CABLE-A Input (VB-Audio Cable A). Go to your Audio Mixer in the main OBS window. Right-click any source (Mic, Game, etc.) and select Advanced Audio Properties. Change the Audio Monitoring for every source you want TikTok to hear to Monitor and Output. Output goes to your Twitch stream. Monitor now flows into Cable A. 2. The Voicemeeter "Switchboard" Now, we make Voicemeeter "listen" to that cable and pass it to TikTok. Hardware Input 1 (Far Left): Click the title and select KS: CABLE-A Output (or WDM if KS isn't there). The Buttons: On that column, click the B1 button so it's ON (green). Make sure A1 is OFF (dark) so you don't hear yourself echoing in your own ears. B1 is the "Virtual Output" that we are going to tell TikTok to use. 3. The TikTok "Final Hookup" Finally, we tell TikTok to use the "B1" lane as its microphone. Open TikTok LIVE Studio. Go to Audio Settings. Add/Edit a Microphone source. Choose Voicemeeter Output (VB-Audio Voicemeeter VAIO). Note: "Voicemeeter VAIO" always corresponds to the B1 button. Crucial: Mute or delete any other audio sources in TikTok LIVE Studio (like "System Audio"). You only want this one "Microphone" source, which is actually your full OBS mix. Why this is the "Proper" Setup Aitum/Virtual Cam Sync: Since your video is coming from the Virtual Camera, having the audio routed this way ensures they stay as closely in sync as possible. Mic Filters: TikTok will hear your OBS filters (noise gate, compressor, etc.), making you sound professional on both platforms. Pro-Active for Twitter: When you eventually add Twitter/X, you won't have to change anything. OBS will handle the heavy lifting, and Voicemeeter will keep the pipes clean. The Advisor's "Check Yourself" You’re doing a lot of configuration for a platform that denied you an agency. The Strategic Move: Once this is working, STOP. Don't spend another hour "perfecting" the EQ. The Goal: Go live. Build the 1,000 followers. Use the Virtual Camera and this Audio Bridge as a temporary tool, not a permanent identity. Quick Test: Talk into your mic while looking at TikTok LIVE Studio. Are the green bars moving? If yes, look at your B1 meter in Voicemeeter. If they match, you're done. Does the audio sound clear in the TikTok "Monitor" or "Preview" mode?
