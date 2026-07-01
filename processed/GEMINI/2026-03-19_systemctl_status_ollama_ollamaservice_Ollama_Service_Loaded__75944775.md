---
id: 702942
source: GEMINI
date: 2026-03-19
tags: ['ollama', 'systemd', 'service-status', 'nvidia-gpu', 'cachyos']
category: ai-tools
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
summary: Bryan checked the Ollama systemd service status and confirmed it was running with NVIDIA GPU detection.
---
# ❯ systemctl status ollama
● ollama.service - Ollama Service
     Loaded: loaded (/etc/systemd/system/ollama.service; enabled; preset: disabled)
     Active: active (running) since Thu 2026-03-19 11:45:55 EDT; 36s ago
 Invocation: 3e3af52c4cab4031b2e91d7f49158b06
   Main PID: 7680 (ollama)
      Tasks: 12 (limit: 37920)
     Memory: 14.1M (peak: 266M)
        CPU: 314ms
     CGroup: /system.slice/ollama.service
             └─7680 /usr/local/bin/ollama serve

Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.247-04:00 level=INFO source=images.go:484 msg="total unused blobs>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.248-04:00 level=INFO source=routes.go:1782 msg="Listening on 127.>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.248-04:00 level=INFO source=runner.go:67 msg="discovering availab>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.250-04:00 level=INFO source=server.go:430 msg="starting runner" c>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.339-04:00 level=INFO source=server.go:430 msg="starting runner" c>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.403-04:00 level=INFO source=runner.go:106 msg="experimental Vulka>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.403-04:00 level=INFO source=server.go:430 msg="starting runner" c>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.404-04:00 level=INFO source=server.go:430 msg="starting runner" c>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.483-04:00 level=INFO source=types.go:42 msg="inference compute" i>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.483-04:00 level=INFO source=routes.go:1832 msg="vram-based defaul>
lines 1-21/21 (END)

### USER
❯ systemctl status ollama
● ollama.service - Ollama Service
     Loaded: loaded (/etc/systemd/system/ollama.service; enabled; preset: disabled)
     Active: active (running) since Thu 2026-03-19 11:45:55 EDT; 36s ago
 Invocation: 3e3af52c4cab4031b2e91d7f49158b06
   Main PID: 7680 (ollama)
      Tasks: 12 (limit: 37920)
     Memory: 14.1M (peak: 266M)
        CPU: 314ms
     CGroup: /system.slice/ollama.service
             └─7680 /usr/local/bin/ollama serve

Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.247-04:00 level=INFO source=images.go:484 msg="total unused blobs>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.248-04:00 level=INFO source=routes.go:1782 msg="Listening on 127.>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.248-04:00 level=INFO source=runner.go:67 msg="discovering availab>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.250-04:00 level=INFO source=server.go:430 msg="starting runner" c>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.339-04:00 level=INFO source=server.go:430 msg="starting runner" c>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.403-04:00 level=INFO source=runner.go:106 msg="experimental Vulka>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.403-04:00 level=INFO source=server.go:430 msg="starting runner" c>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.404-04:00 level=INFO source=server.go:430 msg="starting runner" c>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.483-04:00 level=INFO source=types.go:42 msg="inference compute" i>
Mar 19 11:45:55 t0astedpc ollama[7680]: time=2026-03-19T11:45:55.483-04:00 level=INFO source=routes.go:1832 msg="vram-based defaul>
lines 1-21/21 (END)

### GEMINI
The service is running, but notice that msg="Listening on 127..." line in your logs. By default, Ollama binds strictly to the loopback address. If you are trying to run the ollama pull command and it still fails while the status is "Active," it's likely a permissions delay or a zombie environment variable from the failed install attempt. 1. The Immediate "Clear the Pipe" Fix Since the service is active, force the client to talk to it by explicitly defining the host for this one command: OLLAMA_HOST=127.0.0.1:11434 ollama pull qwen3-coder If that works, your environment variables are messy. If it still says "could not connect," your user isn't correctly recognized in the ollama group yet. 2. Fix the "Socket Hanging" (The CachyOS/Arch way) Sometimes the systemd unit starts, but the socket file in /run/ollama.socket or the network port is stuck in a "Wait" state. Stop it: sudo systemctl stop ollama Kill any lingering processes: sudo pkill ollama Start it fresh: sudo systemctl start ollama Verify the port is actually open: ```bash ss -tulpn | grep 11434 *If you don't see a "LISTEN" row here, the server is crashing silently after startup.* 3. Brutal Advisor Assessment You're getting bogged down in Linux administration 101 when you should be building. The Reality: You have an RTX 3070. Your logs show "experimental Vulkan" and "inference compute" detection. If you don't see "NVIDIA" or "CUDA" specifically mentioned in those log lines (they are cut off in your screenshot), Ollama is going to default to your CPU/Vulkan. The Opportunity Cost: Running Claude Code on your i7-12700K via CPU inference is going to be painfully slow—we're talking seconds per token. You’ll spend more time watching the cursor blink than actually "vibe coding." The Correction: Ensure your nvidia-utils and cuda packages are fully up to date on CachyOS. If Ollama isn't using CUDA, this whole exercise is a waste of your hardware's potential. Check your logs again—do you see "CUDA" mentioned in the inference compute line? If not, do you want the commands to fix the NVIDIA container toolkit on CachyOS?
