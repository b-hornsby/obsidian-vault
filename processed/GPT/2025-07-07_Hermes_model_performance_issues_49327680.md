---
source: GPT
date: 2025-07-07
category: ai-tools
id: 49327680
linked_nodes: ['nodes/people/bryan.md']
---
# Hermes model performance issues

### USER
Is there a difference between those quantized models and the DPO version?

### USER
When I was adjusting parameters for the Hermes model it ran slower than it did when I first tested it when I was making the helpdesk agent before I switched to phi3. Any reason why?

### ASSISTANT
Great follow-up — here's the straight answer:

### 🧪 But in **your case**, the slowdown is more likely due to:

#### ✅ The **parameter changes** you made.

When you tuned the settings to make Hermes more **Claude/GPT-like**, you probably adjusted things like:

- **Higher `context size`** (2048 → 4096+)
- **Enabled `mirostat` sampling** (or advanced sampling tweaks)
- **Increased `repeat_penalty`, `temperature`, `top_k/top_p` settings** for better creativity
- **Enabled extensions** (RAG, tools, voice input/output, etc.)
- **Lowered `n_gpu_layers`** by accident (or didn’t set it at all)

These **increase the token generation cost per step** and push more work to CPU if GPU layers aren’t set right.

### 💡 Recommendation for Speed + Claude-Like Output

For your 3070 (8GB), these are **good balanced settings**:

- **Model**: `nous-hermes-2-mistral-dpo.Q4_K_M.gguf`
- **Parameters**:
  ```bash
  --n_gpu_layers 99 \
  --ctx-size 2048 \
  --threads 12 \
  --top_k 40 \
  --top_p 0.9 \
  --temperature 0.7 \
  --repeat_penalty 1.1
  ```

Optional:
- Use `mirostat` *only if* you need Claude-style writing; it slows things down.

### ⚙️ 1. **Different Parameters = Different Load**
Changing certain parameters can significantly affect performance:

- **`n_gpu_layers`**: If you *reduced* this, more of the model is being run on the CPU instead of GPU, which is much slower.
- **`context_size` / `ctx_size`**: A larger context window means more tokens need to be kept in memory and processed—this slows things down and increases VRAM usage.
- **`--threads` / `--numa` flags**: Thread count misconfiguration can also bottleneck CPU usage, especially if llama.cpp wasn't compiled with OpenBLAS or similar.

### 🔄 3. **Swap or Memory Pressure**
If other processes are using VRAM or RAM (e.g., browser tabs, image tools, other background apps):

- The model could spill into swap or run into memory throttling.
- Windows + WSL2 doesn’t always handle memory sharing gracefully, especially with heavy models.

Check system usage with:
```bash
htop
watch -n 1 nvidia-smi
```

### 💡 5. **Model Warm-up vs Real Usage**
Your original "test" may have been short and cached much of the model quickly. Now that you're using longer prompts or heavier contexts (like multi-step helpdesk questions), it's working harder per token.

If you paste your exact command or oobabooga parameters you're using now vs before, I can point out the exact bottleneck. Want to do that?

### ASSISTANT
Yes — **big difference** between quantized models and **DPO** versions.

Let’s break it down clearly:

### 🔸 What is a **DPO Model**?
**DPO = Direct Preference Optimization**. It's a **fine-tuning method** where the model is trained on *ranking human preferences* (e.g., “response A is better than response B”).

- ✅ **Better Alignment**: More helpful, safe, and human-like replies.
- ✅ **Less hallucination**: Especially in open-ended or instruction-following tasks.
- ❌ **Slower if unquantized**: DPO models are often shared in full precision (FP16 or BF16), which is *much* heavier to run.

### 🧠 TL;DR Comparison

| Feature              | Quantized Model          | DPO Model                      |
|
---
-
---
-
---
-
---
-
---
--|
---
-
---
-
---
-
---
-
---
-
---
---|
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
|
| Purpose             | Faster inference         | Better alignment & quality     |
| Precision           | 4–8 bits (int4/int5/etc) | FP16 or quantized later        |
| Output Quality      | Slightly degraded        | More helpful, humanlike        |
| Size                | Smaller (1.5–5 GB)        | Larger (10+ GB if full-precision) |
| Best Use Case       | Local deployment, fast   | When quality matters most      |
---
## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]