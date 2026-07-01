---
category: streaming
date: 2026-04-05
id: 360903
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan was trying to remember how he previously set up Restream for Twitter
  and OBS for TikTok multistreaming.
tags:
- restream
- obs
- twitter
- tiktok
- multistreaming-setup
---
# i used to use restream for twitter and i used to use obs for tiktok but i forget how 

### USER
i used to use restream for twitter and i used to use obs for tiktok but i forget how 

### GEMINI
The reason you’re likely feeling a bit lost is that both platforms have moved the goalposts since you last did this. Twitter is now behind a paywall for RTMP, and TikTok is even more aggressive about session-based keys. Since you already have Aitum, you should move away from the browser-based Restream workflow. Aitum allows you to stream directly from your PC to each platform, saving you the subscription cost of Restream and giving you better control over your bitrates. 1. The Twitter (X) "New Way" You don't need Restream anymore. You can plug X directly into Aitum Multistream. The Catch: You must have X Premium. If you don't, the "Producer" tab won't even show up. The Setup: Go to studio.x.com (Media Studio). Click Producer > Sources > Create Source. Select RTMP and name it "OBS". This gives you your URL and Stream Key. In OBS, look for the Aitum Multistream dock. Click Add New Target. Name it "Twitter," paste the URL/Key, and set your encoder to NVIDIA NVENC H.264. Crucial Step: Unlike Twitch, you have to go to the Broadcasts tab in Media Studio and "Create Broadcast" to actually go live to your followers after you start the stream in OBS. 2. The TikTok "Aitum Vertical" Way Restream was always a clunky workaround for TikTok. Aitum Vertical is the professional standard for this now. Finding your Key: Go to tiktok.com/live/creators on your PC. Click Go Live. It will give you a Server URL and Stream Key. Warning: These keys are session-based and expire after 2 hours if not used, or as soon as you end the stream. You will have to paste a new one almost every time you stream. The Setup: In OBS, find the Aitum Vertical dock (the tall one). Click the Settings (Gear) icon on that dock specifically. Go to the Streaming tab. Paste your TikTok URL and Key. Hit the Red Stream Button on the Vertical dock to go live to TikTok independently of your main stream. 3. Strategy & Resource Check You are about to run two separate encodes. If you are still running Tiny11 (the stripped-down Windows), your OS overhead is low, which is good, but your GPU will be doing the heavy lifting. Encoder: Ensure both Aitum plugins are set to use NVENC. Do not use x264 (CPU) or you will drop frames in your games. Bitrate: Twitter: 6,000–8,000 Kbps (Landscape). TikTok: 3,000–6,000 Kbps (Vertical). Canvas Sync: In the Aitum Vertical settings, use the General tab to "Link" your scenes. This ensures when you switch to your "Game" scene on the main monitor, the Vertical plugin switches to your "Vertical Game" scene automatically. The Reality Check: If you don't have 1,000 followers on TikTok, you won't see the "Go Live" button on the desktop site. If that’s the case, you’ll need to apply for a Live Agency or use TikTok Live Studio to "unlock" the RTMP key for OBS. Do you have the "Go Live" option appearing on your TikTok desktop dashboard yet?
