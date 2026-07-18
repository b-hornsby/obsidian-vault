# VAULT DOWNLOAD — COLD-START HANDOFF
Generated: 2026-07-18 12:21 UTC (context ~94%, written proactively)
Purpose: a fresh Hermes session or the user can resume/verify with ZERO chat history.

## WHAT THIS IS
Building a future-proof local LLM vault on /mnt/d/models (D: drive, 3.7T, 2.5T free).
Target hardware: RTX 3070 8GB (dev only) + future NVIDIA DGX Spark (128GB, or 248GB linked).
Vault single-model ceiling = 248GB (linked Spark). 8GB-3070 cap is DEAD.

## LIVE STATE @ handoff (verify with the commands below, do not trust this blindly)
- Main downloader: pid 59161 ALIVE. 1/37 done (CodeLlama-34B), now pulling DeepSeek-Coder-V2 142GB.
  Log: /mnt/d/models/vault_download.log   Marker when complete: "=== DONE ==="
- NVIDIA pass: pid 64829 ALIVE. Pulling Ultra-253B 150GB, then 2 Nanos.
  Log: /mnt/d/models/vault_nvidia.log     Marker when complete: "=== NVIDIA DONE ==="
- Both jobs throttled: nice 19 + ionice idle (won't touch game/foreground perf).
- Free disk: ~2.5T. Downloads target D: only; C: untouched; GPU not used by downloads.

## KEY FILES (all on disk, real)
- /tmp/vault_master.json        -> 40 verified entries, 1592GB total (main 37 + nvidia 3)
- /tmp/vault_nvidia_add.json    -> the 3 NVIDIA entries (standalone pass)
- /tmp/vault_downloader.py      -> main hardened downloader (recursive done-check, timeout=max(1800,gb*70), 50GB headroom guard, colibri full-repo, no full-repo fallback for GGUF)
- /tmp/vault_nvidia_pass.py     -> nvidia standalone pass (recursive done-check)
- /tmp/vault_stopwatch.sh       -> cron */5, pings ntfy ONCE per pass done, waits for user confirm (NO auto-continue)
- /tmp/kimi_k3_watcher.sh       -> cron */30, pings ntfy if REAL Kimi K3 weights appear (excludes fake audnai/penclaw placeholder)
- Plan doc (source of truth): C:\Users\toastedmel0n\Obsidian\Tw1n\hermes-memories\2026-07-18-futureproof-vault-plan.md (has full EXECUTION LOG + NVIDIA ADDITIONS sections)

## MASTER = 40 ENTRIES (all HF-verified with token ~/.cache/huggingface/token)
Main (37): code(8), core-llms(14), math(10), vision-multimodal(2 incl Qwen2.5-VL-72B FORCE-resume), big-boys(1 GLM-colibri FORCE full-repo 378GB), gapfill(6: Qwen3-235B, Llama-4-Scout, whisper, Janus-Pro, Qwen3-VL, gemma-4). whisper already pulled as command-path test.
NVIDIA (3): Llama-3.1-Nemotron-Ultra-253B-v1 Q4_K_M (150.9GB, big-boys), NVIDIA-Nemotron-Nano-12B-v2 Q4_K_M (7.5GB), NVIDIA-Nemotron-Nano-9B-v2 Q4_K_M (6.5GB) — both bartowski, filenames prefixed lowercase "nvidia_".

## PLAN DEVIATIONS (verification proved plan wrong — already applied)
1. DeepSeek-V3 EXCLUDED: smallest HF quant (unsloth, Q3_K_M) = 319GB > 248GB ceiling.
2. Pixtral-Large DROPPED: no GGUF on HF anywhere (safetensors only).
3. W-colibri / Y dirs EXCLUDED: unresolvable cryptic identities (avoid guessing).
4. GLM-5.2-colibri resolved to jlnsrk/GLM-5.2-colibri-int4 (352GB full-repo, disk-streams).
5. Stale 07-15 cron (vault_gapfill_watcher.sh, dead PID 59350) REMOVED.

## GOTCHAS (learned the hard way — reuse, don't rediscover)
- hf download v1.17.0: NO --local-dir-use-symlinks flag (old bug). Default --local-dir writes real files.
- bartowski NVIDIA repos prefix filenames with lowercase "nvidia_" (e.g. nvidia_NVIDIA-Nemotron-Nano-12B-v2-Q4_K_M.gguf).
- unsloth nests shards in subdirs (Q4_K_M/Llama-...-0000X-of-00004.gguf) -> done-check MUST be recursive (os.walk), not top-level glob, or it mislabels complete as INCOMPLETE.
- already_done() must ignore hidden/.cache partials but count nested real *.gguf.
- Partial resume (GLM-colibri, Qwen2.5-VL-72B): set force=True + clean stray wrong-quant ggufs first.

## RESUME / VERIFY COMMANDS (fresh session)
```
# are jobs still alive?
for p in 59161 64829; do kill -0 $p 2>/dev/null && echo "pid $p ALIVE" || echo "pid $p DEAD"; done
# tail live logs
tail -5 /mnt/d/models/vault_download.log
tail -5 /mnt/d/models/vault_nvidia.log
# if a job DIED mid-run, just relaunch (resume-safe, skips done dirs):
cd /tmp && python3 /tmp/vault_downloader.py
cd /tmp && python3 /tmp/vault_nvidia_pass.py
# verify final state: every target dir has real *.gguf (recursive), df shows ~1.4-1.6T used
```

## STOPPING-POINT PROTOCOL (user rule)
When a pass log shows its DONE marker, the stopwatch pings ntfy toastedmel0n-pc-alerts ("good stopping point? confirm").
DO NOT auto-continue or declare finished. Wait for user reply, then verify disk + landed files, confirm stop or keep going.

## NEXT ACTIONS WHEN USER CONFIRMS STOP
1. Kill pids 59161 + 64829 (and any hf children) if not already exited.
2. Verify: for each master entry, recursive-glob for *.gguf in /mnt/d/models/<cat>/<dir>; report OK/MISSING.
3. Confirm df -h /mnt/d (~1.4-1.6T used, 1.2-1.4T free).
4. Spot-check 2-3 GGUFs (file magic / llama.cpp load) if user wants.
5. Commit final state to b-hornsby/obsidian-vault.
