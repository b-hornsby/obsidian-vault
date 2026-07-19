# VAULT DOWNLOAD — STATUS & HANDOFF (END OF DAY)
Updated: 2026-07-18 ~17:00 (afternoon session, after STOP)
Supersedes the 12:21 cold-start handoff. Verify live state with the commands below — don't trust blindly.

## WHAT THIS IS
Building a future-proof local LLM vault on /mnt/d/models (D: drive, 3.7T, 2.4T free).
Target hardware: RTX 3070 8GB (dev only) + future NVIDIA DGX Spark (128/248GB).
Vault single-model ceiling = 248GB. 8GB-3070 cap is DEAD.

## LIVE STATE @ STOP (~17:00, all killed per user "stop everything we'll continue tomorrow")
- Main downloader: pid 59176 + shell 59161 — KILLED. Was OLD unpatched code.
- Auto-rescue daemon: pid 121072 (detached via setsid) — KILLED.
- All manual rescues (6 hf pulls): KILLED (DeepSeek-Instruct 104775, DeepSeek-Lite 106861, Nemotron-253B 113103, Hermes 114170, Qwen14B 117861, Qwen32B 126223, Qwen7B 126042).
- `hf download` children: all KILLED.
- **36 `.incomplete` blobs LEFT ON DISK** — the 9 partials will resume from these, no re-download.
```
# quick re-verify nothing is running tomorrow:
pgrep -af "vault_downloader|vault_autorescue|hf download" | grep -v pgrep || echo "all clear"
```

## KEY FILES (all on disk, real)
- /tmp/vault_master.json        -> 40 verified entries, ~1.59TB total
- /tmp/vault_downloader.py      -> PATCHED (throughput-aware timeout + async ntfy). NOT yet run live with patch.
- /tmp/vault_nvidia_pass.py     -> PATCHED (same). Not running.
- /tmp/vault_autorescue.py      -> PATCHED (async throttled ntfy + shared-state launch + auto-register live pulls). Was the detached daemon.
- /tmp/run_autorescue.sh        -> setsid detached launcher for the daemon.
- /tmp/vault_autorescue_state.json -> reset to empty {} before stop.
- Logs: /mnt/d/models/vault_download.log, /mnt/d/models/vault_autorescue.log
- HF_TOKEN source: /home/toastedmel0n/.cache/huggingface/token (never hardcode in scripts)

## MASTER = 40 ENTRIES (HF-verified)
Main (34) + NVIDIA (3: Nemotron-Ultra-253B, Nano-12B, Nano-9B) + gapfill (3 added later: Janus-Pro, Llama-4-Scout, Qwen3-235B, Qwen3-VL, gemma-4 = 5 not-yet-created).
Categories: code(8), core-llms(14), math(10), vision-multimodal(2: Qwen2.5-VL-72B + GLM-5.2), big-boys(2: Nemotron-253B + GLM-5.2-colibri), gapfill(6).

## WHAT WE RAN INTO (the afternoon saga — 4 real bugs)
1. **Broken timeout math in OLD main loop.** Used `max(1800, gb*70)` — assumes ~70s/GB, but REAL throughput here is 2–5 MB/s. Any model >~9GB gets SIGTERM'd at 1800s with only scraps. Caused the recurring `TIMEOUT` lines (Instruct, Hermes, Qwen14B, Qwen32B). Was the root of "this keeps happening."
2. **ntfy 429 freeze.** The daemon POSTed to the free-tier topic on every rescue; blew past rate limit; its SYNC retry backoff (5→160s, ~6 min) BLOCKED the scan loop, so it couldn't catch the next kill during that window. This is why some rescues lagged.
3. **State clobber (silent).** `launch()` reloaded `load_state()` into its OWN private copy and saved that — while `main()` held a different in-memory `s`. When a rescue wrote to `active`, the next scan's `save_state(s)` overwrote it with stale data. Net: rescued models (e.g. Qwen32B) were DOWNLOADING but NOT tracked as active, so if they died the daemon wouldn't re-rescue them.
4. **.cache/huggingface lock contention.** Nemotron-253B + DeepSeek-Instruct got stuck "Still waiting to acquire lock on .cache/huggingface/.gitignore.lock" and never progressed. Required a full `.cache/huggingface/` wipe to clear (restart alone doesn't help).

## WHAT WE FIXED
- ntfy: now runs in a background THREAD + global 90s throttle + dedupe. Can't freeze the scan loop or spam 429s. (File-patched; daemon was killed before a clean relaunch.)
- `launch()` now mutates the SHARED `s` in place (no private reload) — every rescue is recorded in `active` and supervised. Fixed 3 call sites to pass `s`.
- Daemon auto-registers ALL live pulls via `register_live_pulls()` — no manual seeding needed. VERIFIED: on the last clean run it auto-detected and supervised 6 live pulls within 40s.
- Patched timeout in BOTH scripts on disk: `min_rate_bps=1.5e6; timeout=max(3600, int(est*1e9/min_rate_bps))` — stops the kill-at-source.
- NOTE: the live main loop was NEVER restarted with patched code, so the OLD kill behavior was still active when we stopped. The daemon was catching each kill. That's why progress was slow + churny.

## WHERE WE ARE (verified 16:55 via recursive dir scan)
- DONE 3/40 (7.5%): CodeLlama-34B, NVIDIA-Nemotron-Nano-12B, NVIDIA-Nemotron-Nano-9B
- PARTIAL 9 (paused, .incomplete on disk): GLM-5.2-colibri, Nemotron-253B, DeepSeek-Coder-V2-Instruct, DeepSeek-Coder-V2-Lite, Hermes-2-Theta, Qwen2.5-Coder-14B, Qwen2.5-Coder-32B, Qwen2.5-Coder-7B, Qwen2.5-VL-72B
- UNTOUCHED 28: 23 empty dirs + 5 never created (Janus-Pro, Llama-4-Scout, Qwen3-235B, Qwen3-VL, gemma-4)
- Disk: 36% used, 2.4T free.
- Real throughput: 2–5 MB/s (this is what dictates ETA — a 250GB model ~14+ hrs).

## TOMORROW PLAN (when user says go)
1. Run the PATCHED main loop ONCE — it has the throughput-aware timeout so it stops killing big models:
   `cd /tmp && python3 /tmp/vault_downloader.py`
   It resumes the 9 partials off their `.incomplete` blobs and finishes all 40. The auto-rescue daemon is NOT needed once the loop is patched.
2. If a partial won't resume (stuck "waiting to acquire lock"), wipe that dir's `.cache/huggingface/` first, then relaunch:
   `rm -rf /mnt/d/models/<cat>/<dir>/.cache/huggingface`
3. (Optional) Re-launch the daemon detached as a safety net: `bash /tmp/run_autorescue.sh`
4. Ping ntfy toastedmel0n-pc-alerts at each finish + final done (async, throttled).
5. Watch live log: `tail -f /mnt/d/models/vault_download.log` (markers: OK / FAIL / TIMEOUT / === DONE ===)

## GOTCHAS (still valid, reuse)
- hf download v1.17.0: NO --local-dir-use-symlinks flag (old bug). Default --local-dir writes real files.
- bartowski NVIDIA repos prefix filenames with lowercase "nvidia_" (e.g. nvidia_NVIDIA-Nemotron-Nano-12B-v2-Q4_K_M.gguf).
- unsloth nests shards in subdirs (Q4_K_M/Llama-...-0000X-of-00004.gguf) -> done-check MUST be recursive (os.walk), not top-level glob.
- already_done() must ignore hidden/.cache partials but count nested real *.gguf.
- Partial resume: set force=True + clean stray wrong-quant ggufs first.
- .cache/huggingface lock: stuck = full .cache wipe, not just restart.

## STOPPING-POINT PROTOCOL (user rule)
When a pass log shows its DONE marker, ping ntfy "good stopping point? confirm". DO NOT auto-continue. Wait for user reply, then verify disk + landed files, confirm stop or keep going.
