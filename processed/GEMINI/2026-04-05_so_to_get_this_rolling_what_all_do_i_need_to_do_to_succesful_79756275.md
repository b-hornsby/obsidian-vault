---
category: streaming
date: 2026-04-05
id: 348972
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan was asking for a complete setup guide to stream to Twitter and TikTok
  simultaneously given his existing tools.
tags:
- multistreaming
- twitter
- tiktok
- obs-setup
- streaming-workflow
---
# so to get this rolling, what all do i need to do to succesfully be able to stream via twitter and tiktok given my setup? i know i can multistream because i used to on twitch and tiktok at the same time 

### USER
so to get this rolling, what all do i need to do to succesfully be able to stream via twitter and tiktok given my setup? i know i can multistream because i used to on twitch and tiktok at the same time 

### GEMINI
To get back into the game with Twitter and TikTok, you have a specific technical path to follow. Since you’re running Tiny11, your OS overhead is low, which is a massive advantage for dual-encoding. Here is your pre-flight checklist to go from zero to live: 1. The Twitter (X) Mission X has locked the gates. You can no longer just "go live" for free via RTMP. The Requirement: You must have X Premium. If you don't have the checkmark, the "Producer" tools are disabled. The Setup: Go to studio.x.com > Producer > Sources. Create a new RTMP Source. Copy the URL and Key. In OBS, open the Aitum Multistream dock. Click Add New Target. Name it "Twitter," paste your credentials, and set the encoder to NVIDIA NVENC. The "Gotcha": Twitter requires a manual start. You must "Create a Broadcast" on the website, link it to your OBS source, and then hit go live in OBS. 2. The TikTok Mission (456 Followers) Since you are under 1,000 followers, you likely don't have a "Stream Key" button on the website yet. The Immediate Move: Download TikTok Live Studio. It often grants a "7-day trial" to accounts even at your follower count. The Aitum Integration: * If Live Studio gives you a key: Paste it into the Aitum Vertical settings (Gear icon > Streaming tab). If it doesn't: Open your Vertical Canvas in OBS, right-click it, and select Windowed Projector. In TikTok Live Studio, add a Window Capture source and select that projector. This is how you "bridge" your high-quality OBS scenes into TikTok. The Professional Move: Apply to a TikTok Live Agency (like Atomik). They can whitelist your account for a permanent RTMP key regardless of your follower count. 3. The Audio & Video "Handshake" Your main OBS settings do not automatically apply to your Vertical stream. Mic Setup: Go to Aitum Vertical Settings > Streaming. Ensure the Audio Track is set to the same track your Mic is on in your main OBS mixer (usually Track 1). Encoding: In both Aitum Multistream and Aitum Vertical, set the Video Encoder to NVIDIA NVENC H.264. Bitrates: Twitter: 6,000 Kbps (1080p) or 4,000 Kbps (720p). TikTok: 3,000 - 6,000 Kbps. Precision Action Plan StepActionStatus1Verify X Premium status at studio.x.com.🟩2Install TikTok Live Studio to check for trial RTMP access.🟩3In OBS, set your Mic to Track 1 & 2 in Advanced Audio Properties.🟩4Point Aitum Vertical to Audio Track 2 (Clean Game/Mic mix).🟩5Sync your scenes using Aitum's Scene Linking tab.🟩 The Brutal Truth: If you don't have X Premium and you aren't willing to use the "Live Studio Window Capture" workaround for TikTok, you're stuck. Use the Window Capture method tonight to start building that TikTok following back to 1,000. Are you planning to run a "clean" audio feed for TikTok (no music) while keeping music on Twitter, or do you want the same audio on both?
