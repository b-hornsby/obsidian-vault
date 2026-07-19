---
type: project
status: planning
priority: P2
first_seen: 2025-08-01
tags: [streaming, obs, obs-studio, audio-routing, multistream, content-creation, ffmpeg, blender]
aliases: [Streaming Rig, Streaming Setup, Content Production]
---

# Streaming Rig

> Content production infrastructure. OBS, audio routing, multistream experiments, FFmpeg/Blender pipelines, and content ideas. 262 conversations across streaming topics.

## Asset Ledger

Use this as the ownership record. Add rows when gear moves in or out.

| Item | Type | Source / Cost | Status | Notes |
|------|------|---------------|--------|-------|
| OBS Studio | Software | Free / GitHub | Installed | Scenes + transitions defined; profile-backed |
| VoiceMeeter | Audio mixer | Free | Installed | Platform-specific audio separation |
| Aitum | Audio plugin | Free | Installed | Used with VoiceMeeter for stream audio routing |
| Deck / Aitum integration | Stream management | — | Planned | Deck/Aitum control surface for stream events |
| FFmpeg | Video/audio CLI | Free | Installed | Clips, zoompan text, transitions, vertical crop, batch |
| Blender VSE | Compositor | Free | Installed | Headless Python scripting for advanced cuts/compositing |
| Counter-Strike clips | Source footage | Game | Available | Test material for TikTok-style edits |
| Cannabis character art | Asset | Commission/draft | N/A | Niche but fun concept art candidates |
| PC repair flyer design | Asset | Draft | Archived | Retro poster aesthetic; surfaced in general.md |

## Current Build State

- OBS Studio with custom scenes and transitions
- Audio routing: VoiceMeeter + Aitum for platform-specific audio separation
- Multistream experiments: pushing to Twitter and TikTok simultaneously

## Audio Routing

Audio layers: desktop, game, mic, media.  
Target: stream music without TikTok VOD inclusion.  
Status: not solved cleanly. Retrospective conclusion: audio routing breaks something on every attempt — stream quality, recording integrity, or VOD output.

## Edit Pipeline

Live content pipeline goals:
- TikTok-style CS gameplay edits
- Meme edits from short-form clips
- Batch processing for concept/meme content

Tool selection:
- Start with FFmpeg for speed of iteration
- Escalate to Blender VSE when compositing/headless automation is required
- DaVinci Resolve considered but excluded from this workflow because GUI-only and inaccessible from WSL

## Content Ideas

All content ideas tie back to visible build artifacts. Pick one ledger row as the deliverable and ship it.

- "Can I Prompt a Flappy Bird Clone in 30 Mins?" — actually built
- CS gameplay TikTok-style edit — test footage available; use FFmpeg pivot
- Cannabis-themed character art — Niche but fun
- PC repair flyer design — retro poster aesthetic

## Capture Workflow

1. Capture gameplay/source clips.
2. Batch normalize with FFmpeg.
3. Color/audio treatment as needed.
4. Vertical crop for TikTok.
5. Export to backfill queue.

## Linked Conversations

Depth first via topic index: [[insights/conversation-topic-index.md|Browse topic index]] — filter by `streaming`, `obs-studio`, `audio-routing`, `obs-studio` tags.
