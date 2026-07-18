# Future-Proof Vault — Execution Plan (cold-start ready)

Date: 2026-07-18
Goal: turn the half-finished /mnt/d/models vault into a COMPLETE, CURRENT, future-proof local LLM library. This doc is self-contained — a fresh Hermes session (or subagent) can execute it with zero chat history.

## Current ground truth (verified 2026-07-18)
- Drive D: 3.7T total, 1.2T used, 2.6T FREE (31% used). Full plan fits with room.
- 61 of 79 planned model dirs present on disk. Job kept running after the 07-15 pause (cron watcher fired).
- Present per category:
  - core-llms: 16/19
  - code: 8/8 | math: 8/8 | vision-multimodal: 6/6 | image-generation: 5/5
  - audio-speech: 1/1 | embeddings-rag: 8/8 | small-edge: 8/8
  - abliterated: 0/4  (NONE)
  - moe-distilled: 0/9  (NONE)
  - big-boys: 1/3  (GLM-5.2-colibri present but was a 30-min-timeout PARTIAL = 41GB of 352GB)
- /tmp was wiped between sessions. The old scripts (download_models_vault.py, download_gapfill_vault.py) and lists (download_ready.json, gapfill_ready.json) are GONE. The 61 dirs on disk are the real progress record. Cannot "press play" — must rebuild.

## BLOCKER / FIX for the stalling bug
The original job stalled because PER_MODEL_TIMEOUT=1800s (30 min) was too short for huge models:
- GLM-5.2-colibri-int4 = 352GB -> needs ~6h
- Qwen2.5-VL-72B = 84GB -> needs ~2-3h
- Pixtral-Large = 42GB -> needs ~1h
REBUILD RULE: per-model timeout must scale with size. Use a formula: timeout = max(30min, est_gb * 60s/GB * headroom). Or simpler: colibri/VL-72B -> 6h, others keep 30min. The hardened `already_done()` (ignore .cache/hidden dirs) stays so partials re-pull correctly.

## Execution steps (do in order)
1. RECONSTRUCT the master list.
   - Base = 61 present dirs (already done, skip).
   - Add the 18 documented-missing from the 07-15 plan:
     * core-llms: 3 (the 3 not in present list)
     * abliterated: 4 (Llama-3.3-70B, Qwen2.5-32B, Qwen2.5-14B, Mistral-24B abliterated)
     * moe-distilled: 9 (original list)
     * big-boys: 2 (Qwen2.5-VL-72B + 1 more from original list)
   - Special: GLM-5.2-colibri-int4 is PRESENT but PARTIAL -> mark as "re-pull" (resume-safe).
   - Verify all repo IDs + exact shard filenames reach HF with current token (huggingface_hub HfApi repo_info). Fix any 404/renamed before launching.
   - Write to /tmp/vault_master.json (format: list of {repo_id, category, type, files, est_gb}).

2. REBUILD the downloader (hardened, timeout-scaled). Reuse the 07-15 design:
   - serial, resume-safe, organized into /mnt/d/models/<category>/<model>/
   - already_done() ignores hidden/.cache dirs
   - disk-headroom guard: skip if free < model_size + 50GB
   - GGUF: never fall back to full-repo pull (only colibri uses full-repo by design)
   - timeout scaled per model (see BLOCKER above)
   - writes /mnt/d/models/README.txt summary at end

3. LAUNCH main job background with notify_on_complete.
   - It skips the 61 done dirs, re-pulls the GLM partial, downloads the 18 missing.
   - ETA: big-boys dominate. ~352GB colibri + 84GB VL-72B + ~18 missing small/med ≈ 500GB-ish remaining of the original 1.88TB. At ~50-100MB/s HF that's many hours — run background, do NOT block.

4. GAP-FILL (mandatory, Tier-1) — fold in so the vault isn't a generation behind:
   - ADD (verified sizes from 07-15 research):
     * Llama-4-Scout-17B-16E Q4_K_M — 65.4GB (current MoE SOTA)
     * whisper-large-v3-turbo Q8_0 — 0.9GB (speech-to-text gap)
     * Janus-Pro-7B Q4_K_M — 12.1GB (any-to-any gap)
     * Qwen3-VL-8B Q4_K_M — 5.0GB (vision current)
     * gemma-4-26B UD-Q4_K_M — 16.9GB (general flagship)
     * total +100.3GB
   - DROP to free 20.5GB: Mixtral-8x7B, MythoMax-13B, SmolLM2-360M, TinyLlama
   - Net Tier-1: +~80GB. Lands ~1.28T used / ~2.4T free. SAFE.
   - Run as a second background job after main job, OR chained. Keep the existing
     /home/toastedmel0n/vault_gapfill_watcher.sh (already armed via cron */5) — but
     point it at the rebuilt list, or just run gap-fill manually after main completes.

5. KIMI K3 — DO NOT BLOCK. Announced 2026-07-16 (official @Kimi_Moonshot, 2.8T params).
   Weights NOT on HF yet (only a fake placeholder repo audnai/penclaw-Kimi-K3.0-abliterated-GGUF, 0 files).
   Action: set a watcher (cron or check) that pings ntfy toastedmel0n-pc-alerts the moment
   moonshotai/ publishes a real K3 repo. Add to vault only when weights exist + fit cap.

6. VERIFY at end:
   - every target dir has real model files (no .cache-only)
   - df -h /mnt/d/ shows expected usage
   - /mnt/d/models/README.txt summary written
   - spot-check 2-3 GGUFs load via llama.cpp (or at least `file` shows GGUF magic)

## Decisions already made (don't re-litigate unless user says so)
- SKIP Tier-2 (Qwen3-235B-A22B +142GB, drops 4 older). Overkill for RTX 3070 8GB, pushes toward cap.
- SKIP Hy3+MiMo colibri (293GB) and DeepSeek-V3 (227GB) — original cuts, stay cut.
- Uncensored goal covered by the 4 abliterated (being added in step 1).

## Open question for the user (ask ONCE, not bundled)
- Tier-2 skip confirmed? (recommend SKIP)

## One-shot resume command for a fresh session
Read this file, then:
1. Reconstruct list (step 1) -> /tmp/vault_master.json
2. Rebuild downloader (step 2)
3. python3 /tmp/vault_downloader.py  (background, notify)
4. After done: run Tier-1 gap-fill (step 4)
5. Arm Kimi K3 watcher (step 5)
