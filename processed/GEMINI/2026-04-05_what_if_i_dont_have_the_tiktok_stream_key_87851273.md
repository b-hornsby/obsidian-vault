---
category: streaming
date: 2026-04-05
id: 897245
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was asking how to stream to TikTok without having a TikTok stream key.
tags:
- tiktok
- stream-key
- streaming-setup
- restream
---
# what if i dont have the tiktok stream key?

### USER
what if i dont have the tiktok stream key?

### GEMINI
If you don’t have a TikTok stream key, you’ve hit the biggest hurdle in modern multistreaming. Unlike Twitch or Twitter, TikTok doesn't just hand these out to everyone. Since you are using Aitum Vertical and OBS, you have three specific paths to get that key. 1. The "1,000 Follower" Requirement The standard way to get a key is to have at least 1,000 followers. How to check: Log into tiktok.com on your PC. On the left sidebar, look for a "Go LIVE" button. If it’s there: Click it, and it will take you to the Live Center / Producer. Once you hit "Save and Go Live" there, it generates the Server URL and Stream Key you need for Aitum. Note: These keys are session-based. They expire if you don't start the stream within a few minutes, so you have to copy/paste them every single time you go live. 2. The "Live Studio" Shortcut If you don't have 1,000 followers, TikTok sometimes grants access if you use their official software, TikTok Live Studio. Download and install TikTok Live Studio. Complete the "New Streamer" trial (usually requires streaming for 30 minutes). Once you've done this, some users find that the "Go LIVE" option (and thus the RTMP key) unlocks for them on the desktop website, allowing them to switch back to OBS. 3. Joining a Creator Network (Agency) In 2026, this has become the most common "workaround" for OBS users. What it is: You join a TikTok-verified agency (like Atomik or similar networks). The Benefit: They can manually "whitelist" your account for RTMP/OBS access even if you have zero followers. The Cost: Usually free for the creator (the agency takes a cut of the "diamonds" TikTok already takes from gifts), but it gives you that permanent "Live Producer" tab on your desktop. Immediate Action Plan Check Eligibility: Go to livecenter.tiktok.com/producer. If it redirects you to the home page, you aren't unlocked yet. Try TikTok Live Studio: If you're close to 1,000 followers or have a gaming-focused account, download their software and do a test stream. This is the fastest way to "prove" to the algorithm you're a serious streamer. Bridge via TikTok Live Studio (The "Desperation" Move): If you absolutely cannot get a key but still want to use OBS: Set up your Aitum Vertical canvas in OBS. Right-click the Vertical Projector and select Windowed Projector. Open TikTok Live Studio and add a "Window Capture" source, selecting that OBS projector window. It’s not as clean as a direct RTMP stream, but it works. How many followers are you sitting at right now? That determines which of these doors is easiest to kick down.
