---
type: topic
tags: [topic, moc, q2-2026, streaming, content-creation]
aliases: [streaming, content creation, obs, tiktok, twitch, vertical streaming]
description: 262 conversations about OBS, audio routing, vertical streaming, and building a visible creative outlet.
primary_projects:
  - nodes/projects/streaming-rig.md
last_node_review: 2026-07-19
related_nodes:
  - nodes/people/bryan.md
  - nodes/projects/streaming-rig.md
  - nodes/projects/flappy-meme-bird.md
  - nodes/topics/tech/homelab.md
  - nodes/topics/tech/coding.md
  - nodes/topics/tech/ai-tools.md
  - nodes/topics/career/career.md
  - nodes/topics/thinking-patterns.md
  - nodes/topics/general.md
---

# Streaming

*262 conversations about OBS, audio routing, and the dream of creating content that matters.*

---

## How Bryan thinks about streaming

- **Learning style:** I learn audio routing best by breaking the chain on purpose and tracing which link dies. That means lots of partial conversations and a lot of voice-chat frustration, but it also means the fixes stick longer than anything from a tutorial.
- **Decision rules:** if a workflow forces me to touch Windows GUI tools, I treat that as a blocker until there's a CLI or Linux-native alternative. CachyOS-first, Discord/second-brain-backed troubleshooting.
- **Current obsessions:** multistream TikTok + Twitch from one scene, music-on-stream without shipping into VODs, vertical overlays that don't look broken on mobile, and shipping intentional content instead of technical montage.
- **Recurring loops:** I restart the audio-routing design from scratch every few months. Same problem, new cable, same conclusion: VoiceMeeter + Aitum Vertical + VB-Cable, with B1/B2 buses tested separately before touching TikTok Live Studio.

---

## Why this lane matters

Streaming is my creative outlet — the one area where I actually ship things and put them in front of people. It's also where I've fought with some of the most frustrating technical challenges in my setup. For a long time, "content" was implied and off-page; the real record was audio buses, browser sources that didn't appear, and a virtual camera that refused to carry sound.

---

## The technical battle I keep refighting

### Audio routing saga
The signal flow is precise and fragile:

1. Yeti mic → VoiceMeeter hardware input strip
2. VoiceMeeter mixes mic + desktop audio
3. Mixed signal → B1 (Cable A) → OBS audio input capture
4. Mixed signal → B2 (Cable B) → TikTok Live Studio mic input
5. OBS applies mic filters and encodes
6. TikTok Live Studio captures video from Aitum Vertical + audio from Cable B

When any link breaks — muted B2 bus, wrong OBS device, kernel driver issue with the Yeti — the whole setup fails. I've debugged each link methodically and repeatedly. The real insight is that the architecture kept drifting with plugins, cables, and platform updates; the durable part is the bus discipline.

I've said it directly: *"damn yeah i need that cable setup. its just mad confusing especially because I want to be able to play music on stream but not include it in vods for tiktok live."*

### OBS on CachyOS
Browser sources invisible immediately after install. Tuna packaging showing up when I didn't ask for it. Desktop database refreshes. The work is less about a single broken thing and more about package provenance, plugin state, and virtual-camera limitations. I've also explored DistroAV as an NDI-based alternative to the VB-Cable approach, but always keep returning to the simpler cable topology that I can explain to myself in thirty seconds.

### Vertical camera and streaming platforms
Aitum Vertical is the current choice because TikTok Live Studio expects a vertical webcam source and OBS Virtual Camera doesn't reliably carry audio from this Linux build. Twitter/X streaming is waiting on premium subscription. The platform-selection conversation deserves more space than "waiting on a subscription" — soon.

---

## What I've actually shipped

- **Flappy Bird clone series:** "Can I Prompt a Flappy Bird Clone in 30 Mins?" — a YouTube-style rollout showing process instead of polish.
- **Retro PC repair flyers:** poster work in a specific tone for Facebook outreach.
- **Vertical streaming experiments:** TikTok sessions built from gameplay clips, FFmpeg normalization, and a crop pipeline.

---

## What I've learned

**Troubleshooting is cheaper than documentation, but only in the short run.** The bus mapping is in my head. It needs to be externalized.

**Craving improvement isn't the same as shipping content.** The conversation record is overwhelmingly technical: audio cables, OBS plugins, encoder settings. There's almost nothing here about retention, titles, scheduling, or growth. That's the missing lane, not the tooling lane.

**Creative outlet matters because visibility matters.** The drive to stream is partly curiosity, and partly a refusal to keep every project private. That conflict is itself worth watching.

---

## Current setup

- **OBS Studio** — scenes + transitions; profile-backed on CachyOS with NVIDIA
- **VoiceMeeter Banana** — audio routing hub
- **Aitum Vertical** — vertical virtual camera feed for TikTok Live Studio
- **Blue Yeti** — main microphone
- **VB-Cable** — audio bridge into TikTok Live Studio
- **Target state:** Yeti → VoiceMeeter → B1 into OBS, B2 into TikTok Live Studio; music routes to desktop audio only, not B2
- **Capture pipeline draft:** gameplay/source clips → FFmpeg batch normalize → vertical crop → backfill queue

---

## Goals right now

- Lock one audio chain and stop re-architecting it
- Ship a TikTok vertical edit using the FFmpeg batch pipeline
- Run one double-stream test where both viewers hear the mic and neither hears music in VOD
- Stop replacing OBS/UAD plugins instead of debugging config drift

---

## Blockers

- OBS Virtual Camera doesn't carry audio on this Linux build; requires workaround
- Distributor-side compliance still blocks one platform from accepting the vertical stream
- Windows-side GUI tools still leak into troubleshooting; CachyOS-first audio routing is still fragile
- TikTok VOD music filtering path is undocumented in the vault; next session needs exact OBS + Aitum steps, not theory

---

## Key Conversations

- [[processed/GEMINI/2026-02-02_i_simply_want_to_be_able_to_clip_whatever_game_it_is_that_im_35035892.md|Clipping frustration]] — "i simply want to be able to clip whatever game it is that i'm playing"
- [[processed/GEMINI/2025-10-13_how_do_i_make_a_hot_key_in_tikfinity_that_allows_me_to_incre_10466068.md|Hotkey setup]] — creating hotkeys for streaming
- [[processed/GEMINI/2026-02-03_i_still_dont_see_browser_surce_71577189.md|OBS browser source]] — "i still dont see browser surce"
- [[processed/GEMINI/2026-02-04_how_do_i_get_rid_of_tuna_obs_cachyos_67999937.md|OBS Tuna]] — "how do i get rid of tuna obs cachyos"
- [[processed/GEMINI/2026-01-20_best_setup_for_streaming_to_tiktok_and_twitch_simultaneously.md|Multistream setup]] — "best setup for streaming to tiktok and twitch simultaneously"

---

## Recent signals

```dataview
TABLE topic_tags, provider, summary
FROM "processed"
WHERE contains(file.outlinks, "[[nodes/topics/personal/streaming.md]]") OR contains(file.tags, "streaming")
SORT file.ctime DESC
LIMIT 20
```

---

## Related

- [[nodes/people/bryan.md|Bryan]] — the person behind the streams
- [[nodes/projects/streaming-rig.md|Streaming Rig]] — the technical setup
- [[nodes/projects/flappy-meme-bird.md|Flappy Meme Bird]] — content created through streaming
- [[nodes/topics/tech/homelab.md|Homelab]] — the infrastructure behind the rig
- [[nodes/topics/tech/coding.md|Coding]] — the build skills that show up in tooling
- [[nodes/topics/tech/ai-tools.md|AI Tools]] — workflow and image-generation support
- [[nodes/topics/career.md|Career]] — the financial pressure that makes content creation appealing
- [[nodes/topics/thinking-patterns.md|Thinking Patterns]] — frustration-to-breakthrough pipeline + voice
- [[nodes/topics/general.md|General]] — retro poster art, character imagery, and flyer work feeding the creative identity

---

## Backlinks

_This page is referenced from project setup notes, audio-routing debugging sessions, OBS troubleshooting notes, and content-ship retrospectives._
