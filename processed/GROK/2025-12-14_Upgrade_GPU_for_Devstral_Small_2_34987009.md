---
id: 016291
source: GROK
date: 2025-12-14
tags: ['gpu-upgrade', 'devstral-small-2', 'local-llm', 'amd-gpu', 'rtx-4090']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was researching what GPU and other component upgrades he'd need to run Devstral Small 2 locally, including AMD alternatives to the RTX 4090.
---
# Upgrade GPU for Devstral Small 2

### HUMAN
If I wanted to run devstral small 2 at the very least, given my specs what gpu or other components would need upgraded and what would I need to upgrade to? This is my spec sheet: Cpu: Intel Core i7-12700K
Motherboard: Asus Prime Z790-P
Cpu cooler: Noctua NH-U12S
Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB)
4800MHz CL40
Storage: 970 Evo Plus M.2 SSD 2TB
Graphics card: PNY GeForce RTX™ 3070 8GB XLR8 Gaming
REVEL EPIC-X RGB
Case: Corsair 4000D Airflow
PSU: Corsair CX750M
OS: Windows 11

### ASSISTANT
Your current setup is solid overall (great CPU, 32GB RAM, fast storage, and a decent PSU/case/cooler), but the **RTX 3070's 8GB VRAM** is the main bottleneck for running **Devstral Small 2** (a 24-billion-parameter coding-focused model from Mistral AI, released in December 2025).

### Why the RTX 3070 Falls Short
- A 24B model typically requires ~14–18GB VRAM for reasonable quantized inference (e.g., Q4 or Q5) with usable context lengths (8k–32k tokens) and acceptable speed.
- With only 8GB VRAM, you'd be forced into very low quantization (e.g., Q3 or lower), heavy layer offloading to system RAM/CPU, or tiny context windows. This results in slow generation (often <10–20 tokens/second), potential out-of-memory crashes, and degraded quality.
- Mistral explicitly states Devstral Small 2 is designed for "consumer hardware" like a **single RTX 4090** (24GB VRAM) or high-end Macs with unified memory.

### What Needs Upgrading
- **Primary upgrade: Graphics card (GPU)** — This is essential. Everything else in your build (CPU, motherboard, RAM, PSU, cooler, case) is compatible and sufficient—no changes needed there.
- Your Corsair CX750M PSU has enough wattage headroom for higher-end GPUs (e.g., up to ~450W TDP cards like the RTX 4090 or 5090).

### Recommended GPU Upgrades
To run Devstral Small 2 comfortably (Q4/Q5 quantization, 32k+ context, 50–100+ tokens/second speeds via tools like Ollama, LM Studio, or llama.cpp):

| Priority | GPU Model                  | VRAM | Approx. Price (2025) | Why It Works for Devstral Small 2                                                                 | Performance Expectation |
|
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
-|
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
-
---
-
---
-
---
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
-
---
--|
| Best overall | NVIDIA RTX 4090           | 24GB | $1,600–2,000 (new) or $1,200–1,500 (used) | Official benchmark reference from Mistral; fits the model easily with room for long contexts.    | Excellent (100+ t/s, full context) |
| Top-tier future-proof | NVIDIA RTX 5090           | 32GB | $2,000+ (new)       | Extra VRAM for even larger models or multi-model setups; fastest consumer option.                | Outstanding (150+ t/s) |
| Strong value | NVIDIA RTX 3090 (used)    | 24GB | $700–900 (used)     | Same VRAM as 4090, slightly slower but proven for 24B models; great bang-for-buck in 2025 used market. | Very good (80–100 t/s) |
| Minimum viable | NVIDIA RTX 4080 Super / 4080 | 16GB | $900–1,200          | Fits lower quants (Q4) with shorter contexts; some offloading possible but not ideal.            | Acceptable (50–80 t/s, limited context) |

- **Top pick**: Go for a used RTX 3090 if budget is a concern—it's widely available, performs nearly as well as a 4090 for LLM inference, and directly matches Mistral's hardware examples.
- Avoid anything below 16GB VRAM (e.g., RTX 4070/4060 Ti) if you want smooth performance on this model.

No other components need upgrading—your i7-12700K, 32GB DDR5, and 750W PSU will handle any of these GPUs fine. Just ensure good airflow (your case and cooler are already good). If you upgrade the GPU, you'll be set for Devstral Small 2 and many other current/future local LLMs.

### HUMAN
What is the amd equivalent of a 4090 card? 4090 is running like 3k right now

### ASSISTANT
There is **no direct AMD equivalent** to the NVIDIA RTX 4090 in terms of raw performance as of December 2025. AMD chose not to release a high-end flagship in its RDNA 4 generation (RX 9000 series), focusing instead on mid-range cards like the RX 9070 XT. Their current top consumer GPU remains the **Radeon RX 7900 XTX** (from 2022's RDNA 3 lineup).

### Closest AMD Alternative: Radeon RX 7900 XTX
- **Performance comparison** (based on 2025 benchmarks across rasterization, ray tracing, and 4K gaming):
  - The RTX 4090 is generally **20–35% faster** overall.
  - In non-ray-traced games: RX 7900 XTX delivers ~80–90% of the 4090's performance (sometimes matching or slightly exceeding in AMD-optimized titles).
  - In ray-traced games: The gap widens significantly (up to 50–80% in favor of the 4090) due to NVIDIA's superior RT cores and DLSS.
  - For AI/local LLM tasks (like running models): The 4090's 24GB VRAM and better CUDA/Tensor core support make it far superior; AMD cards lag in ROCm ecosystem maturity and raw inference speed.

- **Key specs side-by-side**:

| Aspect              | NVIDIA RTX 4090                  | AMD RX 7900 XTX                  |
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
---|
| VRAM                | 24GB GDDR6X                     | 24GB GDDR6                       |
| Architecture        | Ada Lovelace                    | RDNA 3                          |
| Power Draw          | 450W                            | 355W                            |
| Typical Price (Dec 2025) | $2,500–3,000+ (new/scalped; used ~$2,000–2,500) | ~$900–1,000                     |
| Strengths           | Best ray tracing, DLSS, AI/features | Better value, lower power, strong rasterization |

### Why No True Equivalent?
AMD canceled its planned ultra-high-end RDNA 4 flagship (rumored as RX 8900 XTX) to focus on competitive mid-range options. The RX 7900 XTX is still excellent for 4K gaming and offers outstanding bang-for-buck, especially if ray tracing or NVIDIA-specific features (like DLSS 3/4) aren't critical for you.

### If You're Considering an Upgrade
- If budget allows and you want the absolute best (especially for your local AI/LLM needs): Stick with RTX 4090 (or look at the newer RTX 5090, which is ~30% faster but costs even more at ~$3,000 street price).
- For a cheaper high-end option: The RX 7900 XTX is the best AMD alternative—it's often half the price while delivering strong performance in most scenarios.

Your complaint about the 4090 "running like 3k" aligns with current market reality—high demand (gaming + AI) keeps prices inflated despite its age. Used 4090s or 3090s (also 24GB) can sometimes be found cheaper if you're open to that.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
