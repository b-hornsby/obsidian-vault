---
category: streaming
date: 2026-04-06
id: 708240
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: building
source: GEMINI
tags:
- streaming
- ai
- gemini
- rust
- go
- error
---
# so to clairfy give me a checklist of what to check to ensure that i have this all set up properly. again the main goal is to use obs for overlays, virtually stream that to tiktok live studio to pick that up and to then use my mic settings within obs on the tiktok side. i think i have it but i want to be sure

### USER
so to clairfy give me a checklist of what to check to ensure that i have this all set up properly. again the main goal is to use obs for overlays, virtually stream that to tiktok live studio to pick that up and to then use my mic settings within obs on the tiktok side. i think i have it but i want to be sure

### GEMINI
This is the "Pre-Flight Checklist" for a high-level production environment. You are moving away from hobbyist "guessing" and into a Modular Audio Architecture. If you follow this precisely, your signal chain will be clean, your Discord will sound professional, and your TikTok stream will have your full OBS processing power. 1. Windows System Layer (The Foundation) [ ] Default Playback Device: Set to your FiiO DAC. (Your "ears" stay on hardware). [ ] Brave Browser Routing: In Windows Volume Mixer, set Brave Output to CABLE-B Input. [ ] The "Listen" Kill-Switch: In Sound Control Panel > Recording Tab, ensure "Listen to this device" is UNCHECKED for CABLE-A and CABLE-B. 2. OBS Configuration (The Engine) [ ] Monitoring Device: Go to Settings > Audio > Advanced. Set this to your FiiO DAC. [ ] The Mic "Bridge": * Right-click your Mic in the Mixer > Filters. Add the "Audio Monitor" filter (or use the Global Monitor if you prefer the old way, but the filter is cleaner). Set the device to CABLE-A Input. [ ] Advanced Audio Properties (The Mixer Logic): Mic: Set to "Output Only" (This prevents the "double audio" and "echo" in your ears). Brave (Cable B): Set to "Monitor and Output" (This allows you to hear your music through your FiiO DAC while OBS processes it). Desktop Audio: Set to "Output Only" (Since you already hear this via Windows/FiiO). 3. TikTok Live Studio (The Destination) [ ] Video Source: Select the OBS Virtual Camera (or Aitum Vertical Virtual Camera). [ ] Microphone Input: Select CABLE-A Output. (This is your filtered OBS voice). [ ] System Audio: MUTE or set to None. Why: Your "System Audio" (Games/Alerts) should be managed within your OBS scenes. If you capture "System Audio" in TikTok and OBS, your audience hears everything twice. 4. Discord (The Client) [ ] Input Device: Set to CABLE-A Output. [ ] Audio Processing: Turn OFF Echo Cancellation, Noise Suppression (Krisp), and Automatic Gain Control. Let OBS do the work. The "Mirror" Reality Check You’ve spent 8 years in logistics; you know that a checklist isn't just a suggestion—it’s how you prevent a $100k shipping error. The Blind Spot: You might be tempted to turn "Monitoring" back on for your mic because you "want to hear if it's working." Don't. Trust your OBS meters. If the green bar moves in OBS, the signal is hitting the cable. The Opportunity Cost: Every time you "tweak" a setting outside of this checklist, you risk creating a loop that will crash your audio drivers mid-stream. Final Verification Open OBS. Speak. Does the "Mic" meter move in OBS? Does the "Mic" meter move in TikTok? (If yes, your voice bridge is active). Play Music in Brave. Does the "Brave" meter move? Does the Waveform Visualizer dance? (If yes, your music segment is active). Do you hear an echo? (If no, your monitoring is correctly configured). Does the setup pass this 4-step verification right now?
