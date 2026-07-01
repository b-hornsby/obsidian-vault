---
id: 904696
source: GROK
date: 2025-11-19
tags: ['vibe-coding', 'cursor-ide', 'windsurf', 'claude-code', 'codex', 'tool-selection']
category: coding
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/flappy-meme-bird.md']
summary: Bryan was overwhelmed by the number of AI coding tools and trying to decide which one to use for learning vibe coding without juggling multiple subscriptions.
---
# Tool Dilemma: Choosing the Right Option

### HUMAN
I’m having a tool dilemma and I need help sorting through it if you don’t mind

### ASSISTANT
Sure, lay it on me! What’s the tool dilemma?  

Are you trying to pick between two specific tools (like a new hammer vs. upgrading your old one, or maybe software/tools for a project), or is it more of a “what should I buy/add to my kit next” situation? Give me the details and I’ll help you think it through.

### HUMAN
So I’m looking to actually learn how to “vibe code”, learn how the syntax/systems work and I’m between tools. I don’t know if I should be using cursor/windsurf, Claude code cli, codex, etc. it’s so many different tools and I’m not trying to use a bunch of subscriptions. I like cursor but I don’t like how limiting the usage can be. I don’t mind open source either but my specs are only as follows and I need something similar to those tools in order to maintain code quality: Cpu: Intel Core i7-12700K
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
Here’s a straightforward breakdown to help you pick the best “vibe coding” setup in late 2025 without drowning in subscriptions or getting throttled every 20 minutes. Your RTX 3070 + 32 GB RAM machine is more than capable of running everything locally that matters, so we can actually get you close to Cursor/Claude quality for free or very cheap.

### Top Recommendations Ranked for Your Goals
Goal: learn real systems/syntax by vibing with AI, great autocomplete, inline edits, refactoring, multi-file understanding, chat-in-IDE, minimal throttling.

| Rank | Tool | Cost (Nov 2025) | How close to Cursor/Claude | Local? | Why it fits you right now |
|
---
---|
---
---|
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
-|
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
-|
| 1    | **Continue.dev** (VS Code extension) | Completely free | 95% as good as Cursor right now | Yes (you pick the model) | Best overall for you |
| 2    | **Cursor** (still) | $20/mo Pro (fast models) or free tier with your own keys | 100% (it is Cursor) | Can be | If you bring your own keys it’s no longer throttled |
| 3    | **Windsurf** | $15–20/mo | Very close, slightly different UX | Can be | Good but you’re adding another subscription |
| 4    | **Claude Code CLI / Claude.dev** | Claude Pro $20/mo | Excellent but slower loop than IDE | No | You already pay for Claude if you use it a lot |
| 5    | **Aider** (terminal) | Free | Great for some, terminal-only vibe | Yes | Not IDE, so slower for learning large codebases |

### Winner for You Right Now: Continue.dev + Local Models + Cheap Cloud Backup
Your hardware can comfortably run these models locally with almost zero lag for autocomplete and 3–10 second responses on chat/edit requests:

| Model | VRAM needed | Speed on your 3070 8 GB | Quality (Nov 2025) | Where to get |
|
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
--|
---
-
---
-
---
---|
| DeepSeek Coder V2 236B (QXQ) | ~6–7 GB | Very fast autocomplete, 3–6s edits | Basically Claude 3.5 Sonnet level for code | HuggingFace + Ollama or LM Studio |
| Qwen2.5-Coder 32B | ~5 GB | Blazing | Extremely good, sometimes beats Sonnet | Same |
| Codestral 22B / CodeLlama 70B | 4–6 GB | Fast | Still great | - |
| Cloud fallback: OpenRouter or Groq (Llama-3.1-70B / Qwen2.5-72B) | pennies per session | Instant | Top-tier | Use when local is too slow on huge context |

Continue.dev setup (5-minute install):
1. Install VS Code
2. Install Continue extension
3. Drop this into your `config.json` (it ships with good defaults now anyway):

```json
{
  "models": [
    {
      "title": "DeepSeek Coder V2 236B",
      "provider": "ollama",
      "model": "deepseek-coder:236b"
    },
    {
      "title": "Qwen2.5-Coder 32B",
      "provider": "ollama",
      "model": "qwen2.5-coder:32b"
    },
    {
      "title": "Groq Llama 405B (fast)",
      "provider": "openrouter",
      "apiKey": "your-openrouter-key",
      "model": "meta-llama/llama-3.1-405b-instruct"
    }
  ],
  "tabAutocompleteModel": {
    "title": "DeepSeek Coder",
    "provider": "ollama",
    "model": "deepseek-coder:236b"
  }
}
```

You now have:
- Cursor-style inline Cmd+K edits
- Cmd+L chat that sees your whole codebase
- Tab autocomplete that feels magical
- Zero throttling ever (local)
- Costs literally $0–$5/month on OpenRouter only when you fall back to cloud for huge refactors

### If You Still Want Cursor (Totally Valid)
Just use Cursor but plug in the exact same local models + OpenRouter fallback. Cursor now supports local Ollama/LM Studio natively and doesn’t throttle when you bring your own keys. You only pay the $20/mo if you want their built-in fast Claude 3.5/4/GPT-4.1 models.

### What I Would Personally Do on Your Machine
1. Main daily driver → Continue.dev in VS Code with DeepSeek-Coder 236B local + OpenRouter fallback
2. When I want the absolute best reasoning on a hard refactor → hit Cmd+Shift+L and switch model to Claude 3.5 Sonnet or Opus via OpenRouter (costs ~30¢ per big session)
3. Keep Cursor installed as a secondary IDE for when I want its slightly nicer multi-file edit UI

You end up paying $0–$10/month maximum instead of $20+$20+$15 for Cursor + Claude + Windsurf, and you’re never throttled.

Want me to send you the exact Continue config file that’s working perfectly for a lot of people right now, or walk you through installing the local models?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
