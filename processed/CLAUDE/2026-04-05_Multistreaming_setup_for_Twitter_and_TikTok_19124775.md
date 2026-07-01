---
id: 446235
source: CLAUDE
date: 2026-04-05
tags: ['multistreaming', 'twitter-x', 'tiktok', 'aitum-multistream', 'streaming-agency']
category: streaming
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan is looking to get back into multistreaming on Twitter and TikTok, exploring options for joining a TikTok agency and dealing with Twitter's premium requirements.
---
# Multistreaming setup for Twitter and TikTok

### HUMAN
looking to get back into multistreaming again. platforms of choice are twitter and tiktok for the time being. i already have aitum multistream and aitum vertical installed as well

### ASSISTANT
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Good news — you've already got the two plugins you need. Here's the full rundown for getting Twitter and TikTok going through Aitum:

## TikTok

**Requirement first:** TikTok stream keys in 2026 are only unlocked through Creator Networks (agencies). There's no follower requirement for many of them and it's free — you join a vetted network, hop into their Discord, and follow their process to unlock RTMP access. If you already have RTMP access from before, you're good.

**Getting your stream key each session:**
Go to livecenter.tiktok.com/producer, create a live session with a title and category, hit "Save & Go LIVE" (this won't start the stream yet), then scroll down to find your Server URL and Stream Key. Note that TikTok generates a new stream key for every session, so you'll need to grab a fresh one each time you go live.

**In Aitum Multistream:** Since TikTok is vertical, this goes into the **Vertical** section of the Aitum Multistream dock (that's where Aitum Vertical ties in). Add a TikTok output there, paste in the server URL and stream key, and it'll handle the vertical canvas separately from your main horizontal stream.

So realistically your options are:

1. **Join a free TikTok agency + pay for X Premium** — gets you full RTMP access on both, Aitum works as intended. Agencies like Mirrorcle are commonly recommended in the streaming community and are free to join.

2. **Use TikTok LIVE Studio for TikTok side, skip X for now** — zero cost, but you lose the unified OBS workflow since TikTok LIVE Studio runs separately. Aitum Vertical/Multistream wouldn't be in the picture for TikTok.

3. **Swap platforms entirely** — Twitch and YouTube both have direct OBS integration with zero paywalls and no agency requirements. If Twitter and TikTok specifically aren't a hard requirement, you'd be up and running today.

What's driving the choice of Twitter and TikTok specifically? That might help figure out the best path.

### HUMAN
how do i join an agency for tiktok?

### ASSISTANT
```
This block is not supported on your current device yet.
```

Here's the full process:

**Step 1 — Find an agency**

The most commonly recommended resource is **toktutorials.com/list-of-agencies** — it's a maintained list of vetted agencies. Agencies are free to join and don't take any of your money — you keep your complete gift share. They get a small cut of TikTok's portion instead. For US/Canada specifically, **Atomik** gets recommended a lot.

**Step 2 — Apply**

You join their Discord community to begin the review process. Once approved, you automatically receive full access — including stream key, technical support, and onboarding — in less than 24 hours.

**Step 3 — Get your stream key unlocked**

After joining, you'll be directed into their Discord server. Inside, there's usually a clear step-by-step process for getting your TikTok LIVE stream key unlocked. If anything is unclear, just ask in their Discord.

**What they'll expect from you**

Agencies are looking for serious creators — they'll typically ask you to stream between 10 and 20 hours per month as a minimum. So just keep that in mind going in.

**One heads up:** Atomik notes about 14 days processing time before having the OBS stream key, so don't expect it to be instant on every agency — timelines vary.

Once you're in and have the key, it plugs straight into Aitum Multistream's vertical output for TikTok exactly like we talked about before.