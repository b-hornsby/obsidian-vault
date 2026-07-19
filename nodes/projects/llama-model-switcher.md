---
title: Llama Model Switcher
tags:
  - project
  - homelab
  - ai-tools
  - qwen
  - llama.cpp
aliases:
  - local-model-switcher
  - model-switcher
---

# Llama Model Switcher

Single-port, stop-before-start local model control for Qwen 9B and Qwen 3.6 MoE; works from local shells, tmux, and Termius SSH.

## What this is

A thin wrapper around `~/.local/bin/model-switch 8081` so I can start/stop/status llama.cpp servers from my phone.

Ports:
- `8081` = shared model server
- `8080` = dashboard only; do not touch

Models:
- `run-9b.sh` → Qwen 9B
- `run-moe.sh` → Qwen 3.6 MoE

## Why it’s built this way

- Same port means OS enforces single listener.
- `nohup` + `disown` lets the server outlive Termius disconnect/tmux close.
- `model-switch` kills by listener PID first, then `pkill -9` backstops orphaned wrappers.
- Aliases in `~/.bash_aliases` (not `~/.bashrc`) because Termius non-interactive SSH shells still load `.bash_aliases`.
- `lsof` on dashboard check uses `/usr/bin/lsof` (absolute path) because Termius PATH often drops `/usr/sbin`.

## .bash_aliases

\```bash
model9b() {
  echo "🛑 Stopping any existing model (if running)..."
  /home/toastedmel0n/.local/bin/model-switch 8081 stop >/dev/null 2>&1 || true
  echo "🚀 Starting Qwen 9B model (uses port 8081)..."
  local pid
  pid=$(/home/toastedmel0n/.local/bin/model-switch 8081 start-9b) || true
  echo "✅ Started! PID: ${pid:-unknown} (log: $HOME/9b.log)"
}

model35b() {
  echo "🛑 Stopping any existing model (if running)..."
  /home/toastedmel0n/.local/bin/model-switch 8081 stop >/dev/null 2>&1 || true
  echo "🚀 Starting Qwen 3.6 MoE model (uses port 8081)..."
  local pid
  pid=$(/home/toastedmel0n/.local/bin/model-switch 8081 start-35b) || true
  echo "✅ Started! PID: ${pid:-unknown} (log: $HOME/moe.log)"
}

model-stop() {
  echo "🛑 Stopping all models..."
  /home/toastedmel0n/.local/bin/model-switch 8081 stop
}

model-status() {
  echo "=== Model Status (Port 8081) ==="
  local line
  line="$(/home/toastedmel0n/.local/bin/model-switch 8081 status 2>/dev/null || true)"
  if [[ "$line" == RUNNING* ]]; then
    local pid
    pid="$(echo "$line" | awk '{print $2}' | cut -d= -f2)"
    local args
    args="$(ps -p "$pid" -o args= 2>/dev/null || true)"
    if echo "$args" | grep -q 'Qwen3.5-9B'; then
      echo "RUNNING: Qwen 9B"
    elif echo "$args" | grep -q 'Qwen3.6-35B-A3B'; then
      echo "RUNNING: Qwen 3.6 MoE"
    else
      echo "$line"
    fi
  else
    echo "$line"
  fi
  echo ""
  echo "--- Dashboard (Port 8080) ---"
  if /usr/bin/lsof -ti:8080 >/dev/null 2>&1; then
    echo "IN USE (dashboard) — do NOT touch"
  else
    echo "FREE"
  fi
}
\```

## model-switch behavior

Core rules:
- stop-before-start, always
- identifies listener by port with `lsof -ti:8081`
- verifies listener is actually `llama-server`
- stops with `kill <pid>` + `sleep 2` + `pkill -9 -f "llama-server"` + `pkill -9 -f "run-9b.sh|run-moe.sh"`
- verifies port is free after stop and warns if it isn’t
- logs: `~/9b.log`, `~/moe.log`

## Wrapper scripts

- `~/run-9b.sh`
- `~/run-moe.sh`

Both launch `llama-server` and must background via `nohup` + `disown` so the process survives after SSH disconnect.

## Termius gotchas that broke this once

- `lsof` must be absolute `/usr/bin/lsof` in non-interactive SSH.
- `model-status` must call `model-switch status` and only then label the model; don’t inline `lsof -ti:8081` because that bypasses `running_model`’s `llama-server` sanity check.
- `.bash_aliases` must be the single source of truth; `.profile` is restored to its default `.bashrc`-sourcing shape.

## Known issues / watchouts

- Port `8081` is shared; both models can’t run at the same time.
- 35B model is effectively unusable on RTX 3070 8GB for fast interactive use; this setup is not meant for 35B, even though the script supports it.
- Hermes `/tool terminal` has its own `pkill` quirks; use real bash/term/tmux for lifecycle management.


## Related
- [[nodes/topics/tech/homelab|Homelab]]
- [[goals-index|Goals Index]]
