---
type: topic
tags: [topic, moc, q2-2026]
aliases: [homelab, infrastructure, self-hosted]
---

# Homelab

*793 conversations worth of breaking things, fixing things, and learning how infrastructure actually works.*

---

## What it is

My homelab is my proudest achievement. It's not a project with a finish line — it's an environment I live in. Every fix, upgrade, or new tool is a small win that compounds over time.

I run CachyOS (Arch-based) as my daily driver on an i7-12700K with an RTX 3070. I've got a Steam Deck that doubles as a Linux testbed. I've set up WSL2 instances, fought with bootloader entries, debugged BSODs after installing new drives, and spent hours getting Ubuntu to cooperate before deciding CachyOS was the move.

---

## The journey

### Getting started
I made a bootable Ubuntu drive once and got stuck — I wanted to go back to Windows 11 and didn't know how. That was the beginning. I've since learned about dual-boot configurations, bootloader entries, and why you should never install a model before running the Oobabooga installation.

### The WSL2 era
I set up WSL2 instances, fought with permissions on `/boot/loader/entries/`, and learned that "Permission denied (os error 13)" means you need sudo. I've restored WSL2 to a stock state more than once because I broke something and wanted a fresh slate.

### The CachyOS migration
I committed to CachyOS as my daily driver. It's Arch-based, it's fast, and it doesn't hold my hand. When OBS stopped appearing in the KDE Plasma application launcher, I worked through the desktop database refresh process methodically. When I needed to get rid of OBS Tuna, I figured out how to uninstall it properly.

### The Steam Deck
I'm setting up Citron (a Nintendo Switch emulator) on my Steam Deck. I have the AppImage in `~/Applications`, ROMs in `~/internal_games`, and I'm working through the configuration. I've also dealt with NordVPN connection issues on the Deck — "Unknown reason" with a verified plugin almost always means a cipher/encryption mismatch.

### The Mac Mini consideration
I've been looking at Mac Mini products for local LLM inference. The unified memory architecture is appealing, and I've heard it's the most efficient with running these models. I'm specifically looking for the most cost-effective option that can handle models like gpt-oss-20b.

---

## What I've learned

**Isolation is everything.** Docker containers, WSL2 instances, virtual environments — I've learned to keep things separated. When something breaks, I want to know exactly what broke and why.

**Document everything.** When I fix something, I write it down. Not just the solution, but the problem, the debugging process, and the reasoning. This vault is part of that documentation.

**Break things on purpose.** The best way to learn infrastructure is to break it and fix it. I've debugged CUDA driver issues, audio routing nightmares, and dual-boot configurations. Each one taught me something I couldn't have learned from a tutorial.

**The 3070 is good enough.** I've asked dozens of times whether my RTX 3070 can handle local LLMs. The answer is always the same: yes, run a 7B-13B quantized model, stop worrying. I'm still working on believing "good enough" is good enough.

---

## Current setup

- **CachyOS** — daily driver, Arch-based, KDE Plasma
- **WSL2** — for Windows-specific tools and testing
- **Steam Deck** — emulation on the go (Citron, PCSX2, Dolphin, Cemu, Duckstation)
- **OBS Studio** — scene composition, audio mixing, virtual camera
- **VoiceMeeter Banana** — audio routing hub
- **Docker** — service isolation
- **Syncthing** — file syncing across devices
- **Local LLM inference** — Ollama, Oobabooga, various models

---

## What I'm working on

- **Steam Deck emulation** — getting Citron configured, syncing save data between PC and Deck
- **Audio routing** — getting OBS audio to properly reach TikTok Live Studio through a virtual camera pipeline
- **Local LLM optimization** — finding the right model size for my 3070's 8GB VRAM
- **NordVPN on Steam Deck** — troubleshooting the cipher/encryption mismatch

---

## Key Conversations

- [[processed/GPT/2025-05-10_Exit_Ubuntu_Return_Windows_24149382.md|Stuck in Ubuntu]] — "I made a bootable Ubuntu drive but I want to go back to my windows 11"
- [[processed/GEMINI/2026-01-21_It_said_something_about_please_substantialize_or_something_l_91498505.md|WSL2 issues]] — "It said something about please substantialize or something like that"
- [[processed/GEMINI/2026-03-10_decksteamdeck_nmcli_connection_modify_us12313nordvpncomudp_v_79543006.md|NordVPN on Deck]] — "Unknown reason with a verified plugin almost always means a cipher/encryption mismatch"
- [[processed/GEMINI/2025-08-08_Im_specifically_looking_for_a_Mac_mini_product_if_possible_h_74071153.md|Mac Mini research]] — "I'm specifically looking for a Mac mini product if possible"
- [[processed/GEMINI/2026-01-20_setting_up_citron_on_my_steamdeck_and_so_far_this_is_what_th_52608457.md|Citron setup]] — "setting up citron on my steamdeck and so far this is what the situation looks like"

---

## Related
- [[nodes/people/bryan|Bryan]]

- [[nodes/people/bryan.md|Bryan]] — the person who built this
- [[nodes/projects/homelab-stack.md|Homelab Stack]] — the project behind the topic
- [[nodes/topics/tech/ai-tools.md|AI Tools]] — the tools running on this infrastructure
- [[nodes/topics/tech/coding.md|Coding]] — the skills being practiced
- [[nodes/topics/personal/streaming.md|Streaming]] — the creative outlet this infrastructure supports
- [[nodes/projects/streaming-rig.md|Streaming Rig]] — the streaming setup
- [[nodes/topics/thinking-patterns.md|Thinking Patterns]] — the 72-hour build window in action
