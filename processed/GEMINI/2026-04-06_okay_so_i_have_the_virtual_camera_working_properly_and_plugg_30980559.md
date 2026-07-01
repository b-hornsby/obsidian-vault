---
id: 552539
source: GEMINI
date: 2026-04-06
tags: ['virtual-camera', 'tiktok-live', 'audio-routing', 'obs']
category: streaming
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan had the virtual camera working and needed to ensure audio was also being picked up by TikTok Live.
---
# okay so i have the virtual camera working properly and plugged into tiktok live. how do i make sure that my audio is also being picked up on tiktok live side of things? 

### USER
okay so i have the virtual camera working properly and plugged into tiktok live. how do i make sure that my audio is also being picked up on tiktok live side of things? 

### GEMINI
Since the Virtual Camera only sends video, you have to find a "digital pipe" to send your audio from OBS into TikTok LIVE Studio. Because you're on Windows, the most reliable way to do this without lag is using a Virtual Audio Cable. Here is your prioritized plan to bridge the audio: 1. The Tool: VB-Audio Cable (Free/Donationware) This creates a "Fake Speaker" in OBS that acts as a "Fake Microphone" for TikTok. Download and install VB-Cable. Crucial: You must restart your computer after installation for the drivers to register. 2. The OBS Routing (The "Pipe" In) You need to tell OBS to send a copy of your audio to this new virtual cable. Open OBS Settings > Audio. Under Advanced, find Monitoring Device and set it to CABLE Input (VB-Audio Virtual Cable). Click Apply and OK. In your Audio Mixer (the sliders), click the three dots (or right-click) on the audio sources you want TikTok to hear (e.g., your Mic and Desktop Audio). Select Advanced Audio Properties. Change the Audio Monitoring dropdown for those sources to Monitor and Output. Logic: "Output" goes to your main stream (Twitch); "Monitor" now goes into the Virtual Cable (TikTok). 3. The TikTok Setup (The "Pipe" Out) Now, you make TikTok LIVE Studio "listen" to that cable. Open TikTok LIVE Studio. In the bottom left, click Add Source or go to your Audio Settings. Add a Microphone source. Select CABLE Output (VB-Audio Virtual Cable) as the device. Test it: Play some music or talk in OBS. You should see the green bars moving in both OBS and TikTok LIVE Studio simultaneously. 4. The "Advisor" Performance Audit Since you are running a RTX 3070 and an i7-12700K, you have the horsepower, but you're now running: OBS (Encoding for Twitch) Aitum Vertical (Rendering a second canvas) TikTok LIVE Studio (Encoding for TikTok) Virtual Audio Drivers Plus your DeFi bots and Local AI models in the background. The Opportunity Cost: Every bit of "Virtual" routing (Virtual Cam + Virtual Cable) adds a tiny bit of system latency. Action: If you see your DeFi bot slowing down or your stream dropping frames, disable the preview in TikTok LIVE Studio. You don't need to see it twice; look at your OBS preview instead. Warning: Monitor your VRAM. Local AI models (like Llama/DeepSeek via Ollama) are VRAM hogs. If you're streaming and running a heavy model, your 3070's 8GB VRAM will hit a wall, causing your stream to stutter. Close your LLMs before you go live. Summary Checklist: [ ] Install VB-Cable & Restart. [ ] Set OBS Monitoring Device to "CABLE Input." [ ] Set Mic/Desktop to "Monitor and Output" in Advanced Audio Properties. [ ] Set TikTok Mic Source to "CABLE Output." Does the audio level in TikTok match what you’re seeing in OBS, or is it hitting the red too early?
