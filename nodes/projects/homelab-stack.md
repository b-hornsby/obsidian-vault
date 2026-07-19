---
type: project
status: active
priority: P1
first_seen: 2025-04-01
tags: [homelab, infrastructure, linux, docker, cachyos, obs, syncthing, tailscale]
aliases: [Homelab, Homelab Stack, Home Infrastructure]
---
ma# Homelab Stack

> The longest-lived project in the vault: 793+ conversations spanning CachyOS, Docker, Syncthing, OBS, CUDA, WSL2, and ongoing infrastructure tinkering.

## Core Components

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Host OS | CachyOS (Arch-based) | Daily driver, gaming, development |
| Virtualization | Docker, QEMU/KVM | Service isolation, testing |
| Storage | Syncthing, external drives | File sync between WSL, Steam Deck, Windows |
| Monitoring | OBS, audio routing | Streaming, recording, content production |
| Networking | Tailscale, Syncthing | Remote access, mesh VPN |
| Compute | i7-12700K, RTX 3070 | Local LLM inference, gaming, encoding |

## What This Project Actually Is

homelab-stack is not a project with a finish line. It's an environment I live in. Every fix, upgrade, or new tool is a small win that doesn't require a big commitment.

This is why it's the highest-conviction project in the vault: 793 conversations, sustained over 29 months, consistently moving from curiosity to building to resolution. The other projects stall because they have finish lines. The homelab doesn't.

## Linked Conversations

Depth first, breadth second: [[insights/conversation-topic-index.md|Browse topic index]] for homelab-tagged conversations (linux, wsl2, cachyos, docker, syncthing, obs-studio). Canonical file is `insights/conversation-topic-index.md`.

## Current State

- **OS:** CachyOS full-time (migrated off dual-boot Windows)
- **LLM inference:** Ollama + Oobabooga on RTX 3070, testing GGUF models
- **Streaming stack:** OBS + VoiceMeeter + Aitum, multistream experiments
- **Remote access:** Tailscale mesh, SSH key auth, WSL integration

## Security Layer

The homelab is also the security monitoring platform:

- **Wazuh + ntfy:** Real-time PC security monitoring with phone alerts — see [[nodes/topics/tech/pc-security|PC Security]]
- **Sysmon:** Process, file, and network telemetry
- **Dashboard:** `http://127.0.0.1:8080` for at-a-glance status

## Lessons from 793 Conversations

1. Small wins compound. A working Syncthing config is worth more than a 10-page architecture doc.
2. Fix what breaks rather than replacing the whole stack. Most upgrades were bug fixes, not feature additions.
3. The homelab is a platform, not a product. Its value is what it enables, not what it is.
