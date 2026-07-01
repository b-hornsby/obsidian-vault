# Local Qwen Model Setup — Backup

Date: 2026-07-01

## Models

### Qwen3.5-9B (lightweight)
- Path: `~/models/Qwen3.5-9B/Qwen3.5-9B-Q4_K_M.gguf`
- Context: 65536
- Use case: simple tool calls, 1-2 step tasks
- Limitation: weak at multi-step search→synthesize loops

### Qwen3.6-35B-A3B-UD-IQ3_XXS (workhorse)
- Path: `~/models/Qwen3.6-35B-A3B/Qwen3.6-35B-A3B-UD-IQ3_XXS.gguf`
- Context: 102400 server, 131072 in Hermes config
- Use case: complex tool work, summarization, research loops
- Better at: multi-step retrieval → read structured output → synthesize

## Launch Scripts

### run-9b.sh
```bash
#!/bin/bash
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

### run-moe.sh
```bash
#!/bin/bash
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

## Hermes Config

### custom_providers
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

## Important Notes

- Only one model runs at a time; both listen on port 8081, so start the desired model before switching Hermes to it
- If `session_search` returns empty/bad results and the model loops, switch to the 35B for research/summarization queries — it’s a 9B limitation, not a config issue
- We patched `conversation_loop.py` to remove `session_search` from housekeeping tools and changed the post-tool nudge to discourage repeat tool calls; restart Hermes after code changes
- `curl http://127.0.0.1:8081/v1/models` is the server-side verification; Hermes may warn if the server isn’t ready yet
