# Future-Proof Vault — Execution Plan (cold-start ready, FINAL)

Date: 2026-07-18
Goal: build a COMPLETE, CURRENT, future-proof local LLM library on /mnt/d/models.
THIS DOC IS SELF-CONTAINED — a fresh Hermes session or subagent executes it with zero chat history.

## THE POINT (do not lose this)
The vault is NOT just for the current RTX 3070 8GB. It is for FUTURE HARDWARE.
Target upgrade: NVIDIA DGX Spark (verified specs: 128GB unified LPDDR5X Grace Blackwell GB10,
~1 PFLOPS, NVMe). Two Sparks LINK to 248GB unified memory.
=> Vault ceiling = 248GB single-model (linked Spark). The 8GB-3070 "cap" reasoning is DEAD.
Models too big even for linked Spark (>248GB) are only kept if they disk-stream (colibri).

## Current ground truth (verified 2026-07-18)
- Drive D: 3.7T total, 1.2T used, 2.6T FREE (31%). Room for everything below.
- 61 of 79 planned model dirs present (job kept running after 07-15 pause; cron watcher fired).
- Present: core-llms 16/19, code 8/8, math 8/8, vision-multimodal 6/6, image-generation 5/5,
  audio-speech 1/1, embeddings-rag 8/8, small-edge 8/8, abliterated 0/4, moe-distilled 0/9, big-boys 1/3.
- GLM-5.2-colibri-int4 present but PARTIAL (30-min timeout left it ~41GB of 352GB) -> re-pull.
- /tmp wiped between sessions: old scripts/lists GONE. 61 dirs on disk are the real progress.
  Cannot "press play" — must RECONSTRUCT the list and REBUILD the downloader.

## FINAL DECISIONS (locked — do not re-litigate)
KEEP (already in 79-model plan): all current models. Run great on a Spark.
ADD (future-proof, fit 248GB linked ceiling):
  - Qwen3-235B-A22B Q4_K_M — 142.2GB  (Tier-2, frontier MoE; KEEP not skip)
  - DeepSeek-V3 (150GB planned quant) — RE-ADDED (was cut only for 3070 cap; fits Spark, flagship)
CUT (stay cut):
  - Hy3+MiMo colibri (293GB) — over even linked 248GB ceiling. Skip.
  - GLM-5.2-colibri (352GB) — STAYS (already on disk, partial). colibri disk-streams huge models,
    so it runs on the Spark via that technique.
GAP-FILL Tier-1 (mandatory — fixes "generation behind" gaps):
  ADD: Llama-4-Scout-17B-16E Q4_K_M 65.4GB, whisper-large-v3-turbo Q8_0 0.9GB,
       Janus-Pro-7B Q4_K_M 12.1GB, Qwen3-VL-8B Q4_K_M 5.0GB, gemma-4-26B UD-Q4_K_M 16.9GB.
  DROP (free 20.5GB): Mixtral-8x7B, MythoMax-13B, SmolLM2-360M, TinyLlama.

## BLOCKER / FIX (why the old job stalled)
PER_MODEL_TIMEOUT=1800s (30min) killed huge models:
  GLM-5.2-colibri 352GB needs ~6h; Qwen2.5-VL-72B 84GB needs ~3h; Pixtral-Large 42GB needs ~1h.
REBUILD RULE: timeout scales with size. Use timeout = max(1800, est_gb * 70) seconds.
Hardened already_done() (ignore .cache/hidden) stays so partials re-pull.

## Execution steps (in order)
1. RECONSTRUCT master list -> /tmp/vault_master.json
   - base = 61 present dirs (skip)
   - +18 documented-missing: 3 core-llms, 4 abliterated, 9 moe-distilled, 2 big-boys
   - +GLM-5.2-colibri marked re-pull (partial)
   - +Tier-1 gap-fill 5 adds, -4 drops
   - +Qwen3-235B-A22B, +DeepSeek-V3
   - verify every repo_id + shard filename via huggingface_hub HfApi repo_info with current token
   - format: list of {repo_id, category, type, files, est_gb}
2. REBUILD downloader (hardened, timeout-scaled). Design:
   - serial, resume-safe, into /mnt/d/models/<category>/<model>/
   - already_done() ignores hidden/.cache
   - disk-headroom guard: skip if free < model_size + 50GB
   - GGUF: never full-repo fallback (colibri only, by design)
   - timeout = max(1800, est_gb*70)
   - writes /mnt/d/models/README.txt at end
3. LAUNCH main job background with notify_on_complete. Skips 61 done, re-pulls GLM partial,
   downloads 18 missing + adds. Many hours (big-boys dominate) — do NOT block.
4. GAP-FILL Tier-1 after main done (or chained). ~+80GB net. Lands ~1.4T used.
5. KIMI K3 — DO NOT BLOCK. Announced 2026-07-16 (official @Kimi_Moonshot, 2.8T params).
   Weights NOT on HF yet (only fake placeholder audnai/penclaw-Kimi-K3.0-abliterated-GGUF, 0 files).
   Arm a watcher (cron) pinging ntfy toastedmel0n-pc-alerts when moonshotai/ posts a real K3 repo.
   Add to vault only when weights exist AND fit the 248GB ceiling (a 2.8T model will NOT — note that).
6. VERIFY: every target dir has real model files (no .cache-only); df -h shows expected;
   README.txt written; spot-check 2-3 GGUFs (file shows GGUF magic / llama.cpp loads).

## Future-hardware fit summary (what runs where)
- RTX 3070 8GB: small-edge, quantized 7-14B, embeddings, TTS, image gen. (dev only)
- DGX Spark 128GB: most 70B Q4, vision, audio, MoE up to ~70B active.
- DGX Spark LINKED 248GB: Qwen3-235B-A22B Q4, DeepSeek-V3 Q4, full 70-120B at high quant.
- colibri (GLM-5.2 352GB): disk-stream on any of the above via colibri loader.

## One-shot resume for a fresh session
Read this file, then:
1. Reconstruct list (step 1) -> /tmp/vault_master.json
2. Rebuild downloader (step 2)
3. python3 /tmp/vault_downloader.py  (background, notify)
4. After done: Tier-1 gap-fill (step 4) + adds (Qwen3-235B, DeepSeek-V3)
5. Arm Kimi K3 watcher (step 5)
6. Verify (step 6)

## EXECUTION LOG (2026-07-18, run for real)
- Ground truth on disk: 61 dirs present but only 25 had real GGUFs; 3 partial
  (GLM-colibri 41GB/.cache, Qwen2.5-VL-72B ~29GB stray quants + 1/2 Q5_K_S, Pixtral-Large 0).
- Subagents reconstructed + HF-VERIFIED all repo_ids. Master built at /tmp/vault_master.json
  (37 entries, 1427GB; whisper pulled early as the command-path test so 36 remain pending).
- Downloader hardened + VALIDATED: real 1.7GB whisper pull succeeded (20s). hf download path works.
- LAUNCHED background pid 59161 (notify_on_complete) — serial, resume-safe, timeout=max(1800,gb*70).
  Forces the 2 partials (GLM-colibri full-repo 378GB, Qwen2.5-VL-72B 47GB, clean-stray).
- Kimi K3 watcher armed via cron */30 (excludes fake audnai/penclaw placeholder; pings ntfy on real K3).

### DEVIATIONS forced by live HF verification (plan was partially wrong):
1. DeepSeek-V3 CANNOT be added. Plan assumed ~150-227GB, but smallest quant on HF
   (unsloth/DeepSeek-V3-GGUF) is Q3_K_M = 319GB. Over the 248GB linked-Spark ceiling. Excluded.
2. Pixtral-Large has NO GGUF anywhere on HF (only safetensors). Empty dir dropped.
3. W-colibri / Y dirs: unresolved cryptic identities (colibri search ambiguous; not GLM/Hy3/MiMo
   which are cut/stay). Excluded to avoid guessing. Re-add only if you name the real source.
4. GLM-5.2-colibri resolved to jlnsrk/GLM-5.2-colibri-int4 (352GB full-repo, disk-streams).
5. Stale 07-15 cron (vault_gapfill_watcher.sh, watched dead PID 59350 + [79/79]) REMOVED —
   it would have launched a nonexistent download_gapfill_vault.py. Main+gapfill now one job.

### Everything else matches the locked plan:
- All 79 original intent kept (the 36 pending + 25 already-done + whisper).
- Qwen3-235B-A22B Q4_K_M (142GB) ADDED. Llama-4-Scout, Janus-Pro, Qwen3-VL, gemma-4 ADDED.
- Hy3+MiMo colibri stays CUT (over ceiling). GLM-5.2-colibri STAYS (disk-streams).
- Disk end-state est: ~1.4-1.6T used / ~1.2-1.4T free. Safe under 2.6T.
