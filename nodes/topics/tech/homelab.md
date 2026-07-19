---
type: topic
tags: [topic, moc, q2-2026, homelab, infrastructure, linux]
aliases: [homelab, infrastructure, self-hosted, cachyos, wsl2]
description: 793 conversations worth of breaking things, fixing things, and learning how infrastructure actually works. The values and habits that show up every time hardware or OS gets touched.
primary_projects:
  - nodes/projects/homelab-stack.md
last_node_review: 2026-07-19
related_nodes:
  - nodes/people/bryan.md
  - nodes/projects/homelab-stack.md
  - nodes/topics/tech/ai-tools.md
  - nodes/topics/tech/coding.md
  - nodes/topics/career/career.md
  - nodes/topics/thinking-patterns.md
  - nodes/topics/personal/streaming.md
  - nodes/projects/streaming-rig.md
  - nodes/projects/model-vault.md
---

# Homelab

*793 conversations worth of breaking things, fixing things, and learning how infrastructure actually works. I think of this as the topic behind the work, not the project itself — the values and bad habits that keep showing up whenever I touch hardware.*

---

## How Bryan thinks about homelab

- **Learning style:** break it first, then rebuild it. The best lessons came from rescuing an overwritten boot entry or stopping WSL2 from substantializing. I learn by reading the exact error string, not from architecture docs.
- **Decision rules:** if it's installable on CachyOS without sacrificing my Windows boot option, I'll try it. Otherwise I keep WSL2 as a compromise OS. I also standardize on whatever removes manual GUI steps — NVIM, TMUX, CUDA CLI workflows.
- **Current obsessions:** DGX Spark specs vs 3070 reality, model vault download automation, cron/model-switcher reliability, Wazuh alert tuning, and Mac Mini as a local inference host.
- **Recurring loops:** I re-ask whether the RTX 3070 can handle a model size, then boot it anyway. I keep coming back to 7B–13B quantized, but every new repo makes me ask again.

---

## Why this lane matters

The homelab isn't a project with a finish line. It's the environment I live inside while everything else happens. Every fix, upgrade, or new tool is a small win that compounds over time, and every avoided GUI path is a vote for long-term maintainability.

---

## The major arcs

### Getting started
I made a bootable Ubuntu drive once and got stuck — I wanted to go back to Windows 11 and didn't know how. That was the beginning. I learned about dual-boot configurations, bootloader entries, and why you should never install a model before running the Oobabooga installation.

### The WSL2 era
I set up WSL2 instances, fought with permissions on `/boot/loader/entries/`, and learned that "Permission denied (os error 13)" means you need sudo. I've restored WSL2 to stock state more than once because I broke something and wanted a clean slate.

### The CachyOS migration
I made CachyOS my daily driver because it's Arch-based, fast, and doesn't hold my hand. When OBS stopped appearing in the KDE Plasma launcher, I worked through desktop database refresh methodically. When I needed to get rid of OBS Tuna, I uninstalled it properly instead of living with it.

### The Steam Deck
Citron setup on Deck. ROMs in `~/internal_games`. AppImage in `~/Applications`. Save sync between PC and Deck. NordVPN connection issues — "Unknown reason" with a verified plugin almost always resolves to a cipher/encryption mismatch.

### The Mac Mini consideration
Unified memory architecture is appealing for local LLM inference, specifically `gpt-oss-20b` class models. The question is cost per effective token per hour, not list price.

---

## Honest gaps

- WSL2 audio and CUDA pass-through still aren't clean.
- The 3070 "good enough" answer is technically true and emotionally unresolved.
- Docker, Syncthing, and Windows coexistence is workable but never fully explained in one place in the vault.

---

## What I've learned

**Isolation is leverage.** Docker, WSL2, virtual environments. When something breaks, I want to know exactly what broke and why. That's only possible if things don't share a surface.

**Document the error string, not just the fix.** The lesson is less "how to" and more "what to search for."

**Good enough is an operating mode, not a surrender.** I've asked dozens of times whether the 3070 can handle local LLMs. The answer is always 7B–13B quantized. The skill is deciding when that's acceptable and when it isn't.

**Linux-native beats Windows GUI, but Linux-native breakage is still breakage.** The cleaner surface is worth it. The fragility is the cost.

---

## Current setup

- **CachyOS** — daily driver, Arch-based, KDE Plasma
- **WSL2** — Windows-specific tools, testing, and occasional escape hatch
- **Steam Deck** — Citron, PCSX2, Dolphin, Cemu, Duckstation; also a Linux testbed
- **OBS Studio** — scene composition, audio mixing, virtual camera support
- **VoiceMeeter Banana** — audio routing hub
- **Docker** — service isolation
- **Syncthing** — cross-device file sync
- **Local LLM inference** — Ollama, Oobabooga, various quantized models
- **Model vault downloader** — background-serial, `timeout=max(1800, est_gb*70)`, resume-safe into `/mnt/d/models`
- **Kimi K3 watcher** — cron `*/30` pings ntfy when a real K3 repo exists; fake placeholder excluded

---

## What I'm working on

- Steam Deck emulation + save-sync between Deck and CachyOS
- Model vault downloader reliability after HF repo verification changes
- Kimi K3 watcher reliability and cron repair
- Model-switcher automation around the 3070's 8GB VRAM ceiling

---

## Current setup snapshot

```dataview
TABLE provider, summary, file.ctime
FROM "processed"
WHERE contains(file.outlinks, "[[nodes/topics/tech/homelab.md]]") OR contains(file.tags, "homelab")
SORT file.ctime DESC
LIMIT 20
```

---

## Key Conversations

- [[processed/GPT/2025-05-10_Exit_Ubuntu_Return_Windows_24149382.md|Stuck in Ubuntu]] — "I made a bootable Ubuntu drive but I want to go back to my windows 11"
- [[processed/GEMINI/2026-01-21_It_said_something_about_please_substantialize_or_something_l_91498505.md|WSL2 issues]] — "It said something about please substantialize or something like that"
- [[processed/GEMINI/2026-03-10_decksteamdeck_nmcli_connection_modify_us12313nordvpncomudp_v_79543006.md|NordVPN on Deck]] — "Unknown reason with a verified plugin almost always means a cipher/encryption mismatch"
- [[processed/GEMINI/2025-08-08_Im_specifically_looking_for_a_Mac_mini_product_if_possible_h_74071153.md|Mac Mini research]] — "I'm specifically looking for a Mac mini product if possible"
- [[processed/GEMINI/2026-01-20_setting_up_citron_on_my_steamdeck_and_so_far_this_is_what_th_52608457.md|Citron setup]] — "setting up citron on my steamdeck and so far this is what the situation looks like"

---

## Related

- [[nodes/people/bryan.md|Bryan]] — the person who built this
- [[nodes/projects/homelab-stack.md|Homelab Stack]] — the project behind the topic
- [[nodes/topics/tech/ai-tools.md|AI Tools]] — the tools running on this infrastructure
- [[nodes/topics/tech/coding.md|Coding]] — the skills being practiced
- [[nodes/topics/personal/streaming.md|Streaming]] — the creative outlet this infrastructure supports
- [[nodes/projects/streaming-rig.md|Streaming Rig]] — the streaming setup
- [[nodes/topics/thinking-patterns.md|Thinking Patterns]] — the break-then-rebuild learning loop
- [[nodes/topics/career/career.md|Career]] — the professional demand this stack is meant to fund
- [[nodes/topics/general.md|General]] — the curiosity lane that occasionally becomes a new tool to host

---

## Backlinks

_This page is referenced from WSL2 debugging sessions, OBS troubleshooting notes, model-switcher documentation, and Deck emulation write-ups._
