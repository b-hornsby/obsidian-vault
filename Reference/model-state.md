# Model State

_Canonical reference for local model config and model library state. Supersedes `Reference/local-qwen-models.md` and `hermes-memories/2026-07-18-futureproof-vault-plan.md` model sections._

## Provenance

| Source file | Role | Date |
|-------------|------|------|
| `Reference/local-qwen-models.md` | Operational local Qwen config + run scripts | 2026-07-01 |
| `hermes-memories/2026-07-18-futureproof-vault-plan.md` | Future-proof model library plan + execution log | 2026-07-18 |
| `Reference/model-state.md` | Canonical merged state | current |

## Active Local Models (RTX 3070 8GB workstation)

Only one model runs at a time; both listen on port 8081. Start the desired model before switching Hermes to it.

### Qwen3.5-9B (lightweight)

- Path: `~/models/Qwen3.5-9B/Qwen3.5-9B-Q4_K_M.gguf`
- Context: 65536
- Use case: simple tool calls, 1-2 step tasks
- Limitation: weak at multi-step search→synthesize loops

Launch:

```bash
cd ~/llama.cpp/build/bin
./llama-server \
  -m ~/models/Qwen3.5-9B/Qwen3.5-9B-Q4_K_M.gguf \
  --ctx-size 65536 \
  -ngl 35 \
  --flash-attn on \
  --cache-type-k q8_0 \
  --cache-type-v q8_0 \
  --defrag-thold 0.1 \
  --cache-ram 0 \
  -ub 256 \
  -b 512 \
  --parallel 1 \
  --host 127.0.0.1 \
  --port 8081 \
  --jinja \
  --no-mmap
```

### Qwen3.6-35B-A3B-UD-IQ3_XXS (workhorse)

- Path: `~/models/Qwen3.6-35B-A3B/Qwen3.6-35B-A3B-UD-IQ3_XXS.gguf`
- Context: 102400 server, 131072 in Hermes config
- Use case: complex tool work, summarization, research loops
- Better at: multi-step retrieval → read structured output → synthesize

Launch:

```bash
cd ~/llama.cpp/build/bin
./llama-server \
  -m ~/models/Qwen3.6-35B-A3B/Qwen3.6-35B-A3B-UD-IQ3_XXS.gguf \
  --alias "Qwen3.6-35B-A3B-UD-IQ3_XXS" \
  --ctx-size 102400 \
  -ngl 99 \
  --n-cpu-moe 28 \
  --parallel 1 \
  --flash-attn on \
  --cache-type-k q4_0 \
  --cache-type-v q4_0 \
  --threads 8 \
  -b 512 \
  --host 127.0.0.1 \
  --port 8081 \
  --jinja \
  --no-mmap
```

### Hermes Custom Provider

```yaml
custom_providers:
  - name: Qwen Local
    base_url: http://127.0.0.1:8081/v1
    model: Qwen3.5-9B-Q4_K_M.gguf
    api_mode: chat_completions
    models:
      Qwen3.5-9B-Q4_K_M.gguf:
        context_length: 65536
      Qwen3.6-35B-A3B-UD-IQ3_XXS.gguf:
        context_length: 131072
```

### Live Troubleshooting Notes

- If `session_search` returns empty/bad results and the model loops, switch to the 35B for research/summarization — it’s a 9B limitation, not a config issue.
- `curl http://127.0.0.1:8081/v1/models` is the server-side verification; Hermes may warn if the server isn’t ready yet.
- We patched `conversation_loop.py` to remove `session_search` from housekeeping tools and changed the post-tool nudge to discourage repeat tool calls; restart Hermes after code changes.

## Future-Proof Model Library (Disk Target: `D:\models`)

Goal: complete local LLM library for current hardware and future upgrades.

### Hardware Targets

| Hardware | Capable Models |
|----------|---------------|
| RTX 3070 8GB | small-edge, quantized 7-14B, embeddings, TTS, image gen. (dev only) |
| DGX Spark 128GB | most 70B Q4, vision, audio, MoE up to ~70B active |
| DGX Spark LINKED 248GB | Qwen3-235B-A22B Q4, DeepSeek-V3 Q4, full 70-120B at high quant |
| colibri (GLM-5.2 352GB) | disk-stream on any of the above via colibri loader |

### Final Decisions (locked 2026-07-18)

**KEEP** (already in 79-model plan): all current models. Run great on a Spark.

**ADD** (future-proof, fit 248GB linked ceiling):
- Qwen3-235B-A22B Q4_K_M — 142.2GB
- DeepSeek-V3 planned quant

**CUT** (stay cut):
- Hy3+MiMo colibri (293GB) — over even linked 248GB ceiling. Skip.
- GLM-5.2-colibri (352GB) — STAYS cut from direct load, but disk-streams via colibri, so it runs on Spark.

### Gap-Fill Tier-1 (mandatory)

ADD:
- Llama-4-Scout-17B-16E Q4_K_M 65.4GB
- whisper-large-v3-turbo Q8_0 0.9GB
- Janus-Pro-7B Q4_K_M 12.1GB
- Qwen3-VL-8B Q4_K_M 5.0GB
- gemma-4-26B UD-Q4_K_M 16.9GB

DROP:
- Mixtral-8x7B
- MythoMax-13B
- SmolLM2-360M
- TinyLlama

Net gap-fill change: ~+80GB.

### Execution Status (as of 2026-07-18)

Drive D: 3.7T total, 1.2T used, 2.6T FREE (31%).

- 61 of 79 planned model dirs present on disk.
- Categories present: core-llms 16/19, code 8/8, math 8/8, vision-multimodal 6/6, image-generation 5/5, audio-speech 1/1, embeddings-rag 8/8, small-edge 8/8, abliterated 0/4, moe-distilled 0/9, big-boys 1/3.
- GLM-5.2-colibri-int4 present but PARTIAL (~41GB of 352GB). Needs re-pull.

Execution log:
- Subagents reconstructed + HF-VERIFIED repo_ids. Master list built at `/tmp/vault_master.json` (37 entries, 1427GB; whisper pulled early as command-path test so 36 remain pending).
- Downloader hardened + validated: real 1.7GB whisper pull succeeded (20s). HF download path works.
- Background launch fired with timeout=max(1800, est_gb*70); forces partials (GLM-colibri full-repo 378GB, Qwen2.5-VL-72B 47GB, clean-stray).

### Deviations / Exceptions

- DeepSeek-V3 CANNOT be added under 248GB linked-Spark ceiling; smallest GGUF on HF is ~319GB. Excluded.
- Pixtral-Large has NO GGUF on HF (only safetensors). Empty dir dropped.
- W-colibri / Y dirs have unresolved cryptic identities; excluded to avoid guessing.
- GLM-5.2-colibri resolved to `jlnsrk/GLM-5.2-colibri-int4` (352GB full-repo, disk-streams).
- Stale 07-15 cron (`vault_gapfill_watcher.sh`, watched dead PID + [79/79]) removed.

### Resume for a Fresh Session

1. Reconstruct list -> `/tmp/vault_master.json`
2. Rebuild downloader (hardened, timeout-scaled)
3. `python3 /tmp/vault_downloader.py` (background, notify)
4. After done: Tier-1 gap-fill + adds (Qwen3-235B, DeepSeek-V3 if ceiling changes)
5. Arm watchers/crons if needed
6. Verify: every target dir has real model files; `df -h` shows expected; README written; spot-check GGUFs.
