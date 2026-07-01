---
id: 029946
source: GROK
date: 2025-11-18
tags: ['cursor-ide', 'lm-studio', 'ollama', 'ngrok', 'continue-extension', 'local-llm-coding']
category: coding
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan was trying to integrate open-source models into Cursor via LM Studio/Ollama and ngrok, or find the best open-source AI coding alternative, and needed help configuring the Continue extension.
---
# Integrating Open-Source AI Coding Models

### HUMAN
working on figuring out one of two things. either how to plug in open source models into cursor using lm studio/ollama and ngrok OR what the best open source alternative is for ai assisted coding. for even more context here are my specs: Cpu: Intel Core i7-12700K\
\
Motherboard: Asus Prime Z790-P\
\
Cpu cooler: Noctua NH-U12S\
\
Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40\
\
Storage: 970 Evo Plus M.2 SSD 2TB\
\
Graphics card: PNY GeForce RTX™ 3070 8GB XLR8 Gaming REVEL EPIC-X RGB\
\
Case: Corsair 4000D Airflow\
\
PSU: Corsair CX750M\
\
OS: Windows 11

### ASSISTANT
### Option 1: Using Local/Open-Source Models Directly in Cursor (via Ollama/LM Studio + ngrok)

Your hardware (RTX 3070 8GB + i7-12700K + 32GB RAM) is solid for running quantized coding-focused models locally — you can comfortably run 7B-34B models at good speed (e.g., Qwen2.5-Coder 32B, DeepSeek-Coder-V2, CodeLlama, or Llama-3.1/3.2 variants). As of late 2025, **this still works reliably** using Ollama (or LM Studio) + ngrok, even though Cursor proxies requests through their backend and blocks direct localhost access for security reasons.

#### Recommended Setup: Ollama + ngrok (simplest and most reliable)
1. **Install Ollama** (Windows installer from ollama.com).
2. Pull a strong coding model:
   ```
   ollama pull qwen2.5-coder:32b   # Excellent for coding, runs well on your 3070
   # or
   ollama pull deepseek-coder-v2:33b
   # or smaller/faster: ollama pull llama3.2:11b or codestral:22b
   ```
3. Start the Ollama server (it runs in the background by default).
4. **Install ngrok** (ngrok.com → download Windows binary, sign up for free account).
   - Authenticate: `ngrok config add-authtoken YOUR_TOKEN`
   - Start the tunnel (crucial flags for Ollama compatibility):
     ```
     ngrok http 11434 --host-header="localhost:11434"
     ```
   - Copy the HTTPS forwarding URL (e.g., `https://abcd-1234.ngrok-free.app`).

5. **Configure Cursor**:
   - Open Cursor → Settings (gear icon) → Models tab.
   - Scroll to "OpenAI API Key" section:
     - Enable "Override OpenAI Base URL"
     - Paste: `https://your-ngrok-url.ngrok-free.app/v1`  (append `/v1`)
     - API Key: type anything like `ollama` or `sk-123` (it's ignored locally).
   - Click "+ Add model" → enter the exact model name from Ollama (e.g., `qwen2.5-coder:32b`).
   - Disable/uncheck all other models (GPT/Claude) so Cursor only uses your local one.

6. Test in Cursor Chat (Cmd+L) or Composer — it should respond using your local model.

**Tips/Troubleshooting (2025 edition)**:
- Ngrok URL changes on restart → re-paste into Cursor settings.
- Free ngrok is fine; paid removes session limits if you code all day.
- Alternatives to ngrok: Cloudflare Tunnel (`cloudflared tunnel`) or Tailscale Funnel — both free and give static URLs.
- LM Studio works identically (default port 1234, enable server with CORS allowed).
- Some advanced Cursor features (e.g., full Agent mode or certain Composer tools) may be limited with local models, but chat, inline edits, and autocomplete work great.

This gives you Cursor's excellent UI + full privacy + zero API costs.

### Option 2: Best Fully Open-Source Alternatives to Cursor (No Workarounds Needed)

If the ngrok step feels hacky or you want native local model support + 100% open-source, here are the strongest alternatives in late 2025. Your hardware will fly with any of them.

| Tool          | Type                  | Closest to Cursor? | Native Local Models | Key Strengths for Your Setup                          | Maturity / Community |
|
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
-|
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
---|
| **Continue.dev** | VS Code / JetBrains extension | Very close (chat sidebar, inline edits, autocomplete, codebase @-mentions) | Yes (Ollama, LM Studio, etc. — zero config) | Most mature open-source option; highly customizable prompts; works offline; supports multi-file edits & agents | Highest — actively developed, huge user base |
| **Void**      | Standalone editor (VS Code fork) | Extremely close (almost 1:1 Cursor feel) | Yes (built-in Ollama integration) | Privacy-focused, lightweight, fast on your RTX 3070; full Cursor-like composer/chat | Rising fast in 2025 |
| **Cline**     | Terminal-based agent (or VS Code extension) | More agentic (plans + executes changes) | Yes (any local model) | Great for complex refactors; runs entirely locally; pairs perfectly with Continue | Strong for power users |
| **Tabby**     | Self-hosted completion server + IDE extensions | More Copilot-style autocomplete | Yes (fully local/self-hosted) | Blazing-fast inference on your GPU; privacy-first | Excellent for completion |
| **Aider**     | Terminal tool           | Less IDE-like, more "pair programmer" | Yes (Ollama native) | Best for git-aware, multi-file changes; very reliable with local models | Battle-tested |

**My personal recommendation for you**:
- Start with **VS Code + Continue.dev** — it turns VS Code (which you're probably already familiar with) into something that feels 90-95% like Cursor, but with seamless local model support and no tunneling hacks.
  - Install Continue extension → open the config (`config.json` or UI) → add Ollama models → done.
  - Pair it with the free **Codestral** or **DeepSeek-Coder** models for excellent results.
- If you love Cursor's standalone editor feel, try **Void** — it's the most direct open-source clone.

Both options will run circles around cloud-dependent tools on your 3070, keep everything private, and cost nothing.

Let me know which direction you want to go — happy to give exact model recommendations or config files!

### HUMAN
so not worth trying to plug into cursor 2.0? ive been trying and i cant get it figured out

### ASSISTANT
No, **Cursor 2.0** (released late October 2025) is **not worth fighting** if you've already spent time trying to get local models working and hit walls. Here's the current reality as of November 18, 2025:

### Why the Local Model Hack Broke (or Feels Broken) in Cursor 2.0
- Cursor still has **no native local LLM support** — they route most requests through their backend servers for preprocessing, tool calling, multi-agent orchestration, and their new in-house **Composer** model.
- The old ngrok/Ollama trick relied on overriding the OpenAI base URL. In 2.0, many users report it either:
  - Fails completely (e.g., "model does not exist" or connection errors).
  - Works partially for basic chat/completions but breaks advanced features like Agent mode, Composer multi-file edits, the new in-editor browser, or sandboxed terminals.
- Cursor's team has been pretty open that full offline/local mode isn't coming soon because so much of the "magic" (prompt engineering, context handling, agent coordination) happens on their servers.

If basic chat is all you need and you're okay with the tunnel constantly running, the ngrok method can still limp along with tweaks (e.g., Cloudflare Tunnel instead of ngrok for a static URL, or adding `--host-header` flags). But it's fragile, and with 2.0's heavier reliance on backend features, it's just not a great experience anymore.

### Switch to a True Local-Friendly Alternative (Your Hardware Will Love It)
Your RTX 3070 + 32GB RAM is perfect for this — you can run 32B–70B coding models at 30–60+ tokens/sec with almost zero hassle.

**Top pick right now: VS Code + Continue.dev (feels 95% like Cursor, often better for local)**  
- Zero tunneling, 100% offline, native Ollama/LM Studio support.
- Chat sidebar, inline edits, @-mention files/folders, autocomplete, multi-file "Composer-like" agents.
- Install → open `continue config.json` → add your Ollama models → done.
- Hotkeys and workflow are basically identical to Cursor.

**Runner-up if you want a standalone editor (not VS Code): Void**  
- Literal Cursor clone, built from the ground up for local models.
- Same UI/UX, full Composer-style multi-file editing, agents, etc.
- Ollama integration out of the box.

**Model recommendations for your 3070 8GB (quantized):**
| Model                        | Size   | Speed on your GPU | Strengths                          | Ollama tag                     |
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
-
---
---|
---
-
---
-|
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
-
---
-
---
-
---
-|
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
-|
| Qwen2.5-Coder                | 32B    | 35–50 t/s        | Best all-round coder right now     | qwen2.5-coder:32b              |
| DeepSeek-Coder-V2-Lite       | 16B/33B| 50–70 t/s        | Insanely good at reasoning/code    | deepseek-coder-v2:lite         |
| Llama-3.3-70B-Instruct       | 70B    | 25–40 t/s (Q4)   | Huge context, very smart           | llama3.3:70b (or AWQ/Q5)       |
| Codestral                    | 22B    | 60+ t/s          | Fast & accurate for autocomplete  | codestral:22b                  |

Just `ollama pull` them and point Continue/Void at Ollama — everything stays local, private, and free forever.

If you want, I can paste the exact Continue config or Void setup steps for your models. You've got great hardware — enjoy actually using it instead of wrestling with Cursor's proxy! Which direction sounds better to you?

### HUMAN
so to walk me through what it is that i have to do to get this set up, can i use LM studio instead?

### ASSISTANT
Yes, **LM Studio is actually easier and more reliable than Ollama** for Continue.dev (and Void) in late 2025 — many people prefer it now because:
- Better GUI for discovering/downloading quantized models
- Built-in OpenAI-compatible server with zero config
- Automatically uses your RTX 3070 (CUDA) at full speed
- No command-line fuss

Here’s the **exact step-by-step** to get you a Cursor-like experience in under 15 minutes using **LM Studio + Continue.dev in VS Code** (this will feel 95%+ like Cursor, fully local, no tunneling, no cost).

### Step 1: Install LM Studio (5 minutes)
1. Go to https://lmstudio.ai → Download the Windows version.
2. Install it (it’s just a normal .exe).
3. Open LM Studio → it will ask to download models.

### Step 2: Download a great coding model that fits your 3070 8GB
Recommended (pick one, all excellent):
| Model                            | VRAM used | Speed on 3070 | Download name in LM Studio                              |
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
|
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
---|
| Qwen2.5-Coder-32B-Instruct       | ~7.2 GB   | 35–50 t/s     | Qwen2.5-Coder-32B-Instruct → Q4_K_M or Q5_K_M            |
| DeepSeek-Coder-V2-Lite-16B       | ~5.5 GB   | 55–75 t/s     | DeepSeek-Coder-V2-Lite → Q5_K_M or Q6_K                  |
| Llama-3.3-70B-Instruct           | ~7.8 GB   | 25–40 t/s     | Meta-Llama-3.3-70B-Instruct → Q4_K_M (AWQ if available)  |
| Codestral-22B-v0.1               | ~6 GB     | 60+ t/s       | Codestral-22B-v0.1 → Q6_K or Q8_0                        |

Just search the name in LM Studio → click Download → choose the Q5_K_M or Q6_K version (best quality/speed balance for 8 GB).

### Step 3: Start the local server in LM Studio
1. Load the model you just downloaded (double-click it).
2. Go to the **“Local Server”** tab (bottom left, looks like </> icon).
3. Click **“Start Server”** — it will show:
   - Server running on http://localhost:1234/v1
   - It’s already OpenAI-compatible (no extra settings needed).

Leave LM Studio open in the background.

### Step 4: Install VS Code + Continue.dev
1. Install VS Code if you don’t have it: https://code.visualstudio.com/
2. Open VS Code → Extensions (Ctrl+Shift+X) → search “Continue” → install **Continue - Open Source AI Code Assistant** (the one by Continue.dev, blue icon).

### Step 5: Auto-configure Continue to use LM Studio
1. After installing, Continue will open a sidebar on the right and show a welcome screen.
2. It will **auto-detect** your LM Studio server and list your model — just select it!
   - If it doesn’t auto-detect (rare), press Ctrl+Shift+P → “Continue: Open config.json” and replace the contents with this:

```json
{
  "models": [
    {
      "title": "LM Studio",
      "model": "gpt-4",                // name doesn’t matter
      "apiBase": "http://localhost:1234/v1",
      "provider": "openai"
    }
  ],
  "tabAutocompleteModel": {
    "title": "Codestral (fast)",
    "model": "codestral-latest",     // or whatever small model you want for autocomplete
    "apiBase": "http://localhost:1234/v1",
    "provider": "openai"
  }
}
```

3. Save the file → Continue will instantly connect.

### Step 6: Start coding (exactly like Cursor)
- Cmd+L (or Ctrl+L) → chat sidebar, ask anything
- Cmd+I → inline edit (“fix this function”, “write tests”, etc.)
- Highlight code → “Ask” or right-click → Edit / Explain / etc.
- @-mention files or folders in chat just like Cursor
- Use “Cmd+Enter” for multi-file agent edits (their version of Composer)

That’s it — fully local, private, unlimited, and faster than Cursor on most days because no internet latency.

Want me to give you the exact LM Studio preset JSON for the fastest Qwen2.5-Coder-32B settings, or do you want to try Void instead (standalone app, no VS Code needed)? Just say the word!

### HUMAN
so for my model i'm using qwen 2.5 coider 32b instruct but the q4_k_m version. i need to know what needs to go into my .continue config.yaml

### ASSISTANT
Here’s the exact `config.yaml` you need for Continue.dev to perfectly use your **Qwen2.5-Coder-32B-Instruct Q4_K_M** that’s running in LM Studio right now.

### Option A: Simplest (LM Studio default server – recommended)
Since LM Studio’s local server is already running on port 1234 and is fully OpenAI-compatible, just paste this entire file:

```yaml
# ~/.continue/config.yaml   (on Windows this is usually C:\Users\YourName\.continue\config.yaml)

models:
  - name: Qwen2.5-Coder 32B
    title: Qwen2.5-Coder-32B Q4_K_M
    model: qwen2.5-coder:32b-instruct-q4_K_M   # this exact string is what LM Studio shows as the model ID
    apiBase: http://localhost:1234/v1
    provider: openai
    completionOptions:
      temperature: 0.2
      topP: 0.95
      maxTokens: 8192
      contextLength: 32768   # Qwen2.5-Coder 32B actually has 32k context

# Optional: a faster/smaller model just for autocomplete (saves VRAM)
tabAutocompleteModel:
  title: Codestral (fast autocomplete)
  model: codestral-latest   # or any smaller model you also have loaded in LM Studio
  apiBase: http://localhost:1234/v1
  provider: openai

# Some nice defaults for coding
systemMessage: |
  You are an expert software engineer. Always think step-by-step and explain your reasoning.
  Use Markdown fencing with the correct language tag for code blocks.
  When editing code, output the entire file when practical or use precise @-line references.

slashCommands:
  - name: edit
    description: Edit code with instructions
  - name: comment
    description: Add comments or documentation
  - name: test
    description: Generate tests

embeddingsProvider: none   # we’re running 100% local, no need for embeddings
```

### Option B: Even shorter version (works perfectly and is what most people use)
If you don’t care about the extra tweaks:

```yaml
models:
  - title: Qwen2.5-Coder 32B
    model: qwen2.5-coder:32b-instruct-q4_K_M
    apiBase: http://localhost:1234/v1
    provider: openai

tabAutocompleteModel:
  title: Qwen2.5-Coder 32B
  model: qwen2.5-coder:32b-instruct-q4_K_M
  apiBase: http://localhost:1234/v1
  provider: openai
```

### How to apply it
1. In VS Code press `Ctrl+Shift+P` → type “Continue: Open config.yaml” → hit Enter.
2. Delete everything in the file and paste one of the blocks above.
3. Save (`Ctrl+S`).
4. Continue will instantly switch to your model (you’ll see the name appear in the model selector dropdown).

That’s literally it — you’re done.  
Now Cmd+L, Cmd+I, Cmd+Enter (agent mode), @-mentions, everything will run on your RTX 3070 with zero internet and zero cost.

Enjoy — Qwen2.5-Coder-32B Q4_K_M is currently one of the absolute best coding models you can run locally, and on your 3070 it will feel lightning fast. Let me know if you want a tuned system prompt or some custom slash commands!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
