---
type: topic
tags: [topic, moc, q2-2026]
aliases: [streaming, content creation, obs]
---

# Streaming

*262 conversations about OBS, audio routing, and the dream of creating content that matters.*

---

## What it is

Streaming is my creative outlet — the one area where I actually ship things and put them in front of people. It's also where I've fought with some of the most frustrating technical challenges in my setup.

I stream to TikTok using TikTok Live Studio with a vertical virtual camera setup via Aitum Vertical. I want to add Twitter/X streaming when I get a premium subscription. The core challenge has been audio routing — getting OBS audio to properly reach TikTok Live Studio through the virtual camera pipeline without messing up my desktop audio.

---

## The technical battle

### Audio routing saga
The signal flow is complex:
1. Yeti mic → VoiceMeeter hardware input strip
2. VoiceMeeter mixes mic + desktop audio
3. Mixed signal → B1 (Cable A) → OBS audio input capture
4. Mixed signal → B2 (Cable B) → TikTok Live Studio mic input
5. OBS applies mic filters and encodes
6. TikTok Live Studio captures video from Aitum Vertical + audio from Cable B

When any link in this chain breaks — a muted B2 bus, a wrong device selected in OBS, a kernel driver issue with the Yeti — the whole setup fails. I've debugged each link systematically.

I've asked: *"damn yeah i need that cable setup. its just mad confusing especially because I want to be able to play music on stream but not include it in vods for tiktok live."*

### OBS configuration
I've fought with OBS on CachyOS — getting browser sources to work, installing plugins, and dealing with the fact that OBS Virtual Camera doesn't carry audio. I've asked: *"how do I get rid of tuna obs cachyos?"* and *"i still dont see browser surce"* after installing plugins.

I've explored DistroAV (an NDI-based audio/video routing tool) as an alternative to the VB-Cable approach.

### Content creation
I built a Flappy Bird clone as a YouTube series — "Can I Prompt a Flappy Bird Clone in 30 Mins?" That's the kind of content I want to create: showing the process, not just the result. Documenting the tech journey.

I've created retro-styled posters of people fixing computers for Facebook flyers. I've generated character images with specific styling — ghost with sunglasses, weed-themed fantasy art, Gucci snow goggles on characters.

---

## What I've learned

**Audio routing is genuinely complex.** It's not just plug-and-play. Every link in the chain has to be configured correctly, and when something breaks, you have to debug each link systematically.

**Content strategy matters less than I think.** My conversations are almost entirely technical. There's little discussion of what I actually stream, my content goals, audience growth, or monetization strategy. The focus is on making the technology work.

**The creative outlet is important.** Streaming is where I actually ship things. It's where I put content in front of people. It's the one area where the work is visible.

---

## Current setup

- **OBS Studio** — scene composition, audio mixing, virtual camera
- **VoiceMeeter Banana** — audio routing hub with virtual cables
- **Aitum Multistream** — multi-platform distribution
- **Aitum Vertical** — vertical camera feed for TikTok
- **Blue Yeti** — microphone
- **VB-Cable** — audio bridge to TikTok Live Studio

---

## What I'm working on

- **Audio routing final configuration** — getting the OBS + VoiceMeeter + VB-Cable setup working reliably
- **Music on stream but not in VODs** — the technical challenge of selective audio routing
- **Twitter/X streaming** — waiting on premium subscription
- **Content strategy** — figuring out what to stream, not just how to stream

---

## Key Conversations

- [[processed/GEMINI/2026-02-02_i_simply_want_to_be_able_to_clip_whatever_game_it_is_that_im_35035892.md|Clipping frustration]] — "i simply want to be able to clip whatever game it is that i'm playing"
- [[processed/GEMINI/2025-10-13_how_do_i_make_a_hot_key_in_tikfinity_that_allows_me_to_incre_10466068.md|Hotkey setup]] — creating hotkeys for streaming
- [[processed/GEMINI/2026-02-03_i_still_dont_see_browser_surce_71577189.md|OBS browser source]] — "i still dont see browser surce"
- [[processed/GEMINI/2026-02-04_how_do_i_get_rid_of_tuna_obs_cachyos_67999937.md|OBS Tuna]] — "how do i get rid of tuna obs cachyos"

---

## Related

- [[nodes/people/bryan.md|Bryan]] — the person behind the streams
- [[nodes/projects/streaming-rig.md|Streaming Rig]] — the technical setup
- [[nodes/projects/flappy-meme-bird.md|Flappy Meme Bird]] — content created through streaming
- [[nodes/topics/tech/homelab.md|Homelab]] — the infrastructure it runs on
- [[nodes/topics/tech/coding.md|Coding]] — the skills behind the content
- [[nodes/topics/career/career.md|Career]] — the financial pressure that makes content creation appealing
- [[nodes/topics/thinking-patterns.md|Thinking Patterns]] — the frustration-to-breakthrough pipeline
