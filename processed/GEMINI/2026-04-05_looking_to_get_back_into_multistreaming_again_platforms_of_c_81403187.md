---
category: streaming
date: 2026-04-05
id: 157719
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan was planning to get back into multistreaming on Twitter and TikTok
  using Aitum Multistream and Aitum Vertical.
tags:
- multistreaming
- twitter
- tiktok
- aitum-multistream
- aitum-vertical
---
# looking to get back into multistreaming again. platforms of choice are twitter and tiktok for the time being. i already have aitum multistream and aitum vertical installed as well 

### USER
looking to get back into multistreaming again. platforms of choice are twitter and tiktok for the time being. i already have aitum multistream and aitum vertical installed as well 

### GEMINI
Since you've already got the Aitum suite installed, you're ahead of the curve. However, the landscape for Twitter (X) and TikTok has become increasingly gatekept over the last year. Here is the objective breakdown of what you need to do to get those streams live. 1. Twitter (X) Setup Twitter is no longer a "copy-paste" simple RTMP destination for most. The Barrier: You generally need X Premium (Blue) to access "Media Studio Producer," which is where you generate your Stream Key. The Process: 1. Go to Media Studio. 2. Navigate to Producer > Sources and create a new RTMP source. 3. Copy the RTMP URL and Stream Key. 4. In OBS, open the Aitum Multistream dock. Add a new output, name it "Twitter," and paste your credentials. The "X Factor": You must manually Create a Broadcast in Media Studio and link it to your source before the stream will actually show up on your timeline. 2. TikTok Setup (Vertical) Since you have Aitum Vertical, you'll want to use its dedicated output to ensure the 9:16 aspect ratio is native. The Barrier: You need a Stream Key. If you don't have 1,000 followers, you can often bypass this by applying for the "TikTok Live Studio" or joining a Creator Network (Agency) which grants OBS access. The Process: Open the Aitum Vertical settings (the gear icon on the Vertical dock). Go to the Streaming tab. Enter your TikTok RTMP URL and Stream Key here. Pro Tip: TikTok keys are often session-based. You may need to grab a fresh key from the TikTok app (Go Live > PC/Mac option) every single time you start a session. 3. Resource Management Running two extra encoders (one for Twitter landscape and one for TikTok vertical) on top of your base recording/streaming can tax your system. The Fix: In the Aitum Multistream/Vertical settings, ensure you are using the NVENC (NVIDIA) encoder if you have an RTX card. Syncing: Use Aitum’s "Scene Linking" feature. You can set it so that when you switch to a specific scene on your main (Twitter) canvas, the Vertical (TikTok) canvas automatically switches to a corresponding "Vertical" version of that scene. Precision Plan Check Permissions: Verify you have X Premium and TikTok Live access. Without these, no amount of software will get you live. Audio Routing: In Aitum Vertical, double-check that your "Audio Track" is capturing your mic and game sound. It’s a common mistake to have a perfect vertical video with zero audio because the Vertical plugin defaults to a different track. Test Run: Start the Twitter stream via the Multistream dock first, then hit "Go Live" on the Vertical dock. Monitoring both dashboards is a must to ensure the RTMP handshake actually happened. PlatformOrientationRequirementsStrategyTwitter (X)16:9 (Landscape)X Premium / Media StudioAitum Multistream OutputTikTok9:16 (Vertical)1k Followers or Agency KeyAitum Vertical Streaming Tab Are you planning to use a separate "Vertical" scene for TikTok, or are you just going to crop your main gameplay?
