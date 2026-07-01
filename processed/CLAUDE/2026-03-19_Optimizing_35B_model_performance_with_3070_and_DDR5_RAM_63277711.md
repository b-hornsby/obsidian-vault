---
category: ai-tools
date: 2026-03-19
id: 3811
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
- operation-immortal-agent
resolution: partial
sentiment: curious
source: CLAUDE
summary: Bryan is trying to determine the most efficient local LLM to run given his
  hardware limitations (RTX 3070, 32GB DDR5 RAM), specifically for use in his 'Operation
  Immortal Agent' project.
tags:
- local-llm-optimization
- hardware-limitations
- 35b-model
- ollama
- lm-studio
- rtx-3070
---
# Optimizing 35B model performance with 3070 and DDR5 RAM

### HUMAN
This is what Gemini had to say about the current model I’m using: Strictly speaking, the 9B model is your "Velocity King," but it is not the most "efficient" in terms of extracting the most intelligence out of your hardware.
With 32GB of DDR5 RAM, your system is actually under-utilized if you only run the 9B model. You are leaving about 20GB of RAM idle that could be used to host a significantly more capable "brain."
Here is how the 9B stacks up against the real alternatives for your specific 8GB VRAM / 32GB RAM split:
1. The "Daily Driver" (9B)
• Efficiency: High speed, low resource.
• Experience: Instant responses (90+ t/s).
• Limitation: It is a "small" model. It will hallucinate more often on complex logic, struggle with long-form nuance, and occasionally drift into English if you're using other languages.  
2. The "Power User" Choice (35B-A3B)
• Efficiency: High intelligence-to-VRAM ratio.
• Experience: Respectable speed (25–35 t/s).
• Why it might be "better": Because it is a Mixture-of-Experts (MoE) model, it only "thinks" with 3B parameters at a time. On your hardware, a Q4_K_M quantization will fit partly in VRAM and partly in your 32GB RAM. It is significantly smarter than the 9B at agentic tasks (like "vibe coding") and complex reasoning.  
3. The "Pure Logic" Choice (DeepSeek-R1-Distill-Qwen-14B/32B)
• Efficiency: Peak reasoning.
• Experience: Slower (5–15 t/s).
• Why it matters: If you are troubleshooting code or complex Linux configs, these "Reasoning" models (which use a Chain-of-Thought process) will run circles around the standard Qwen 3.5 9B. Your 32GB of RAM allows you to run the 32B version of these models comfortably, even if your GPU can't hold the whole thing.
The Brutal Advisor Verdict
You are currently optimized for speed, not capability.
If you are just chatting or doing basic summaries, stay with the 9B. If you are doing anything that actually matters—like building your "Operation Immortal Agent" or debugging CachyOS kernels—you are doing yourself a disservice by not using the 35B-A3B.
The 35B-A3B is the most "efficient" use of your specific 32GB RAM upgrade. It gives you 35B-level world knowledge with a speed that is still faster than most people can read.
Would you like me to give you the specific ollama or LM Studio settings to bridge the 35B model across your 3070 and your DDR5 RAM?

### ASSISTANT
That's a solid breakdown from Gemini, and honestly pretty accurate. A few things worth adding from my end:

**The 35B-A3B rec is legit** for your use case. MoE models are genuinely well-suited to split VRAM/RAM setups because the inactive experts just sit in system RAM until called. For agentic work like Operation Immortal Agent, the reasoning quality jump over a 9B is real.

**One thing Gemini glossed over:** inference speed on CPU-offloaded layers tanks hard depending on how many layers get pushed to RAM vs VRAM. The "25–35 t/s" estimate for the 35B-A3B is optimistic if a significant chunk offloads to DDR5. You might land closer to 10–18 t/s depending on layer split. Still usable, but worth setting expectations.

**On the DeepSeek R1 Distill options:** the 14B is probably the sweet spot for your rig if you want reasoning without a painful speed penalty. The 32B will run but you'll feel it — more of a "set it and cook dinner" situation. For CachyOS debugging or complex Solana logic, even the 14B distill will noticeably outperform a standard 9B on multi-step problems.

**Practical suggestion:** rather than picking one, keep the 9B as your default chat/quick-task model in Ollama and pull the 35B-A3B or R1-14B as task-specific models you call intentionally. That's basically how a lot of home lab setups handle it — right tool for the job.

What are you currently running the 9B for day-to-day? That'd help narrow down whether the MoE route or the reasoning route makes more sense to prioritize first.

### HUMAN
Well right now I had the 9b model plugged into Claude code but i was asking Gemini if it is the efficient given my hardware limitations: Cpu:%20Intel%20Core%20i7-12700K%0AMotherboard%3A%20Asus%20Prime%20Z790-P%0ACpu%20cooler%3A%20Noctua%20NH-U12S%0AMemory%3A%20Corsair%20Vengeance%20Ddr5%20ram%2032GB%20(2x16GB)%0A4800MHz%20CL40%0AStorage%3A%20970%20Evo%20Plus%20M.2%20SSD%202TB%0AGraphics%20card%3A%20PNY%20GeForce%20RTX%E2%84%A2%203070%208GB%20XLR8%20Gaming%0AREVEL%20EPIC-X%20RGB%0ACase%3A%20Corsair%204000D%20Airflow%0APSU%3A%20Corsair%20CX750M%0AOS%3A%20Windows%2011

### ASSISTANT
Ah, important context — you're on **Windows 11**, not CachyOS for this setup. That changes a few things.

For **Claude Code specifically**, the model you plug in matters differently than a general chat use case. Claude Code is doing a lot of structured, multi-step reasoning — file edits, planning, tool calls. A 9B is going to struggle with that compared to a purpose-built coding/reasoning model.

**The real question for your setup:** are you hitting actual limitations with the 9B in Claude Code right now, or are you just wondering if you're leaving performance on the table?

Because if it's the latter — yes, you are. The 9B will miss context, make logical errors on multi-file edits, and lose the thread on longer tasks. That's not a hardware problem, that's just model size.

**For your specific rig on Windows:**

The 35B-A3B in Ollama will work, but layer offloading behavior on Windows can be flakier than Linux. You'll want to explicitly set `num_gpu` layers to something like 20–28 and let the rest hit RAM, rather than letting Ollama auto-detect and potentially do something dumb.

The **R1-Distill 14B** is actually my pick for Claude Code integration on your hardware — it's a cleaner fit for the agentic reasoning Claude Code needs, and it'll fit mostly in VRAM + a little RAM without the MoE complexity.

Are you running Ollama on Windows natively or through WSL2?

### HUMAN
My bad my specs are actually: • Cpu: Intel Core i7-12700K
•Motherboard: Asus Prime Z790-P
•Cpu cooler: Noctua NH-U12S
•Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB)
4800MHz CL40
• Storage: 970 Evo Plus M.2 SSD 2TB
•Graphics card: PNY GeForce RTX™ 3070 8GB
•Case: Corsair 4000D Airflow
•PSU: Corsair CX750M
•OS: CachyOS + Tiny11

### ASSISTANT
No worries — so you're dual-booting CachyOS and Tiny11. That actually makes the conversation more interesting.

Quick question before going further:
```
This block is not supported on your current device yet.
```

### HUMAN
Q: Where are you running Ollama / Claude Code?
A: CachyOS

### ASSISTANT
Good — CachyOS is the better environment for this anyway. CUDA/ROCm support is cleaner on Arch-based distros, and you won't have the Windows driver overhead eating into your VRAM headroom.

So back to the core question: the 9B plugged into Claude Code is functional but you're leaving capability on the table for anything non-trivial. For Operation Immortal Agent especially, you'll hit the 9B's ceiling pretty fast on multi-step agentic reasoning.

Given you're on CachyOS with 8GB VRAM + 32GB DDR5, my honest ranking for Claude Code specifically:

**1. R1-Distill 14B** — best fit for Claude Code's agentic loop. Reasoning model, fits mostly in VRAM with minimal RAM spillover, and handles multi-step tool use noticeably better than a standard 9B.

**2. Qwen3 35B-A3B** — better raw knowledge, but the MoE layer offloading adds latency variability that can make Claude Code feel inconsistent. Great for chat/research, slightly awkward for tight agentic loops.

**3. Stay on 9B** — only if speed is the priority and tasks are simple.

To pull the R1-Distill 14B right now it's just:

```bash
ollama pull deepseek-r1:14b
```

Then swap it in your Claude Code config. Want help with the exact config change, or do you already know where that lives?

### HUMAN
Gemini said: Claude is correct about the environment, but the recommendation for DeepSeek-R1-Distill-14B is where the real "unlock" for your specific project lies.
Since you are running CachyOS, you have a massive advantage: lower system overhead compared to Windows 11 means your 8GB VRAM is actually "purer." In Windows, the OS and desktop compositor often eat 1.5–2GB of VRAM just to exist. On CachyOS, you can get that down to under 500MB, giving the model more room to breathe.
As of March 2026, Claude Code (the CLI tool) now has a built-in compatibility layer for the Anthropic Messages API via Ollama and other local providers. If you are using it as your primary terminal assistant, you should choose a model specifically tuned for the "Agentic Loop" (Plan -> Tool Call -> Execute -> Verify).
Here is the objective ranking for your hardware (8GB VRAM / 32GB DDR5) on CachyOS:
1. The Heavyweight: DeepSeek-R1-Distill-14B
This is the most "intelligent" choice for Claude Code.
• Why: Unlike standard models, R1 uses a "Thinking" process. When Claude Code asks it to "Refactor this entire folder," R1 will actually reason through the dependencies before outputting code.
• Efficiency: A 4-bit quantization will fit entirely in your 8GB VRAM on CachyOS (since you don't have Windows bloat).
• The Catch: It can be slightly more verbose, which can sometimes slow down the agentic loop if the context gets too long.
2. The Specialist: Qwen3-Coder-Next (14B or 32B MoE)
• Why: This model was trained specifically for the Claude Code/Cline era of agentic tools. It understands the "Diff" format and tool-calling better than almost any other open-weight model.
• Fit: The 14B fits in VRAM. The 32B MoE will spill into your 32GB of RAM, but because it's an MoE, it will still feel snappy (around 20-30 tokens/sec).
• The Verdict: If R1 feels too slow or "overthinks" simple tasks, this is the most reliable "workhorse" for coding.
3. The "Legacy" Choice: Qwen 3.5 9B
• The Advisor's Reality Check: You are underutilizing your 12700K and 32GB RAM if you stick with this. It’s fine for simple scripts, but it will frequently fail on complex multi-file edits where the 14B models succeed.

### ASSISTANT
Gemini's mostly right here, but there's one thing worth flagging — it mentioned **Qwen3-Coder-Next** like it's a current released model, and I'm not confident that's actually out yet as of early 2026. That might be a hallucination or a conflation with Qwen2.5-Coder, which *is* real and actually a strong pick for exactly the reasons Gemini described — trained for diff format, tool calling, agentic workflows.
```
This block is not supported on your current device yet.
```

Okay, I was wrong to second-guess Gemini on that one — Qwen3-Coder-Next is very real and very relevant. My bad for not knowing it, it dropped in February 2026 after my knowledge cutoff.

Here's the updated picture: it's an 80B MoE model that only activates 3B parameters at a time, and it was specifically trained for agentic workflows — tool calling, environment interaction, and reinforcement learning from real execution feedback. Explicitly built for Claude Code integration too.

**The catch for your hardware though:** to run the smallest quantization you need at least 42GB of RAM. You have 32GB DDR5 + 8GB VRAM = 40GB total addressable, which puts you just under the minimum. You'd likely hit OOM on anything but the most aggressive quantizations.

So the revised honest ranking for your rig:

**1. DeepSeek-R1-Distill 14B** — still fits cleanly, strong reasoning, no RAM ceiling issues.

**2. Qwen3-Coder-Next** — technically the best tool for Claude Code, but you're right at the edge of runnable. Might work with a heavily compressed quant and context size limited to ~32k, but it'd be tight and potentially unstable.

**3. Qwen2.5-Coder 14B** — solid middle ground, proven agentic performance, no hardware drama.

Worth trying the Qwen3-Coder-Next with a low quant if you want to experiment, but I wouldn't make it your daily driver on this rig until you have more RAM.

### HUMAN
So for daily driver and to get off 9b, what should I be using given my specs:

### ASSISTANT
Nice build by the way — RGB on point.

Given your specs (8GB VRAM + 32GB DDR5 on CachyOS), here's the straight answer:

**Daily driver: DeepSeek-R1-Distill 14B**

It fits cleanly in your VRAM with room to breathe, the reasoning quality is a genuine step up for Claude Code work, and it won't give you the instability headaches that come with pushing right up against your RAM ceiling.

```bash
ollama pull deepseek-r1:14b
```

**If you want to experiment on the side: Qwen2.5-Coder 14B**

Trained specifically for agentic/coding workflows, handles diffs and tool calls well, same hardware comfort zone as the R1-14B.

```bash
ollama pull qwen2.5-coder:14b
```

Qwen3-Coder-Next is the dream option for your use case but realistically you're about 2-8GB short of running it without fighting OOM errors. Not worth the headache as a daily driver right now.

**The move:** run R1-14B as your Claude Code default, pull Qwen2.5-Coder as a second option and see which feels better for your workflow. Both are free to pull and you can swap them in Claude Code's config in seconds.

Want the exact config lines for Claude Code to point at whichever model you pick?

### HUMAN
And the deepseek model would be better than the qwen 3.5 9b on my hardware?

### ASSISTANT
Yes, definitively — but let me break down exactly why so it's not just "trust me."

**Why the R1-14B beats the 9B for your use case:**

The 9B is a standard next-token prediction model. It generates answers. The R1-14B is a *reasoning* model — it thinks through a problem step by step before outputting anything. For Claude Code specifically, that difference shows up as:

- Multi-file edits where it actually tracks dependencies instead of breaking things
- Debugging where it reasons through *why* something is failing, not just pattern-matching a fix
- Agentic tasks like Operation Immortal Agent where it needs to plan multiple steps ahead

**The hardware math:**

The 14B at Q4 quantization sits around 8-9GB. On CachyOS with your VRAM overhead under 500MB, it fits almost entirely in your 3070. You won't take a big speed penalty from RAM spillover. You're looking at roughly 20-30 t/s vs the 9B's 90+ t/s — but for Claude Code that speed difference doesn't matter because you're not watching it stream, you're waiting for it to finish a task.

**Short version:** the 9B is fast but shallow. For anything you actually care about building, the R1-14B will produce meaningfully better results on your hardware without breaking a sweat.

### HUMAN
And the deepseek model is the optimal choice given my hardware constraints? I need to make the most out of my hardware while maintaining quality overall. The goal is for it to be a cost effective solution when I’m low on the pro sub for Claude

### ASSISTANT
Honestly, given everything — your hardware, your use case, and the goal of being a Claude fallback — I'd actually push back slightly on R1-14B being the *optimal* pick and reopen the Qwen2.5-Coder 14B comparison before you commit.
```
This block is not supported on your current device yet.
```

Here's the honest answer based on current data:

**Yes, R1-14B beats the 9B** — that's not in question. But the more important nuance from the research:

R1 distills win on pure math and reasoning, but Qwen3 is better at everything else: chat, coding, multilingual, instruction following. And Qwen3 can toggle thinking on and off, while R1 distills always reason.

That "always reasoning" behavior is actually a drawback for a Claude Code fallback, because Ollama defaults to 4096 tokens, which isn't enough for a reasoning model — thinking chains can easily exceed that. You'd need to configure a custom Modelfile to bump that up or R1 will cut itself off mid-thought.

Also worth flagging: Qwen 14B wins on SWE-bench tasks — the more practical agentic benchmarks — which is exactly what Claude Code runs.

**My actual recommendation for your use case:**

**Qwen2.5-Coder 14B** is probably the better daily driver than R1-14B for your specific goal. Better on agentic/SWE benchmarks, no thinking token overhead, cleaner Claude Code integration, same hardware fit.

R1-14B is the better pick if you're doing heavy debugging or logic-heavy Solana work where you want to see the reasoning chain.

Realistically — pull both, they're free:

```bash
ollama pull qwen2.5-coder:14b
ollama pull deepseek-r1:14b
```

Use Qwen2.5-Coder as your Claude Code default, switch to R1 when you're deep in a tricky problem.

### HUMAN
So no 9b?

### ASSISTANT
Correct — drop the 9B for anything that matters.

The only reason to keep it around is if you want a near-instant response for something trivial, like a quick one-liner or a basic question. At that point you're basically just using it as a fast autocomplete.

For Claude Code specifically, the 9B will let you down on anything multi-step. It's not a hardware limitation on your end — your rig can comfortably run better. You're just leaving capability on the table for no reason.

Pull Qwen2.5-Coder 14B, set it as your Claude Code default, and don't look back.

### HUMAN
Can you run both models in two different terminals?

### ASSISTANT
Yes, Ollama handles this natively. It can serve multiple models simultaneously — each `ollama run` in a separate terminal just loads that model into memory and they coexist.

The catch on your hardware is **memory pressure**. Two 14B models at Q4 would want roughly 16-18GB total, split across your 8GB VRAM and 32GB RAM. Ollama will figure out the layer distribution automatically, but you may notice the second model loads slower and runs at reduced token speed since it's competing for resources.

Practical way to test it:

**Terminal 1:**
```bash
ollama run qwen2.5-coder:14b
```

**Terminal 2:**
```bash
ollama run deepseek-r1:14b
```

Ollama will keep both loaded as long as you're actively using them. If one sits idle too long it'll unload it from memory automatically.

For your workflow though — since you're piping one model into Claude Code at a time — running both simultaneously only really makes sense if you're manually comparing outputs side by side. Otherwise just swap models in Claude Code's config as needed rather than running both hot.

### HUMAN
No I meant using these in Claude code. Can I use the Claude code for both models next to each other in two different terminals?

### ASSISTANT
Yes, absolutely. Claude Code reads its model config from the environment, so you can override it per terminal session.

Something like this:

**Terminal 1 (Qwen2.5-Coder):**
```bash
ANTHROPIC_BASE_URL=http://localhost:11434 ANTHROPIC_MODEL=qwen2.5-coder:14b claude
```

**Terminal 2 (R1):**
```bash
ANTHROPIC_BASE_URL=http://localhost:11434 ANTHROPIC_MODEL=deepseek-r1:14b claude
```

Each terminal runs its own Claude Code session pointed at a different model. Useful for exactly what you're thinking — running the same task against both and seeing which handles it better.

The memory caveat from before still applies. Both models loaded simultaneously will compete for VRAM/RAM, so expect slower token speed than running one at a time. For your rig it should still be usable, just not as snappy as a single model session.

Worth experimenting with on a real task from one of your projects to get a feel for where each model shines.

### HUMAN
So all together, what is the absolute best way to make use of my hardware constraints and what model/models should I be using

### ASSISTANT
Given everything we've covered, here's the definitive answer for your rig:

**Default Claude Code model: Qwen2.5-Coder 14B**
Best all-around for agentic coding, diffs, multi-file edits. This is your workhorse.

**Secondary model: DeepSeek R1 14B**
Pull this out specifically when you're deep in a logic problem, debugging something gnarly, or working on Solana contract logic for Operation Immortal Agent where step-by-step reasoning actually matters.

**Drop entirely: Qwen 3.5 9B**
You've outgrown it for anything meaningful.

**The bigger picture:**

This setup costs you nothing extra, fits comfortably in your hardware, and gives you a genuine Claude fallback when your Pro sub runs low. You're not leaving capability on the table anymore, and you're not fighting your RAM ceiling either.

Qwen3-Coder-Next remains the upgrade path when you eventually add more RAM. But for right now, this two-model setup is the most you can responsibly squeeze out of 8GB VRAM + 32GB DDR5 without introducing instability.

### HUMAN
btw im using cc in cursor so when i run the claude command i just use claude --model and then either model name?

### ASSISTANT
Not exactly — since you're running Claude Code inside Cursor, the `--model` flag syntax is slightly different, and you also need to make sure Ollama is exposed as the backend. Quick clarification question:

How do you currently have Claude Code connected to Ollama in Cursor — are you using the `ANTHROPIC_BASE_URL` environment variable, or did you set it up another way?

That'll determine the exact command you need, because if the base URL isn't pointing at Ollama already, just passing `--model` won't do anything useful.

### HUMAN
i have it within my fish config on cachyos

### ASSISTANT
Perfect, that makes it simple. Can you paste the relevant lines from your Fish config? Specifically the `ANTHROPIC_BASE_URL` and any `ANTHROPIC_MODEL` or alias lines you have set.

That way I can give you the exact command to swap models rather than guessing at your current setup.

### HUMAN
❯ echo $ANTHROPIC_BASE_URL http://localhost:11434 ~ ❯

### ASSISTANT
Okay so the base URL is set globally pointing at Ollama. Now just check if you have a model set too:

```bash
echo $ANTHROPIC_MODEL
```

If that returns something, that's your current default. If it's empty, Claude Code is probably falling back to whatever Ollama has loaded.

Either way, once you know that, swapping models per session is just:

```bash
ANTHROPIC_MODEL=qwen2.5-coder:14b claude
```
or
```bash
ANTHROPIC_MODEL=deepseek-r1:14b claude
```

No `--model` flag needed — you're just overriding the env var inline for that terminal session without touching your Fish config. Clean and simple.

### HUMAN
❯ echo $ANTHROPIC_MODEL ~ ❯

### ASSISTANT
Empty — so no default model is set, which means Ollama is just serving whatever it has loaded by default (probably your 9B still).

Two options:

**Option 1 — Set a permanent default in your Fish config:**
```bash
set -gx ANTHROPIC_MODEL qwen2.5-coder:14b
```
Add that to your `~/.config/fish/config.fish` and it'll always default to Qwen2.5-Coder when you run `claude`.

**Option 2 — Per session override (no config change):**
```bash
ANTHROPIC_MODEL=qwen2.5-coder:14b claude
```

I'd go with Option 1 for your daily driver and use the inline override in a second terminal when you want R1. Best of both worlds without constantly typing the model name.

### HUMAN
i dont want either to be the default because i still want to be able to use claude code whenever i have the sub

### ASSISTANT
Good call. Just use the inline override every time then:

```bash
ANTHROPIC_MODEL=qwen2.5-coder:14b claude
```
```bash
ANTHROPIC_MODEL=deepseek-r1:14b claude
```

When your sub is active, just run `claude` as normal and it hits Anthropic's API. When you're low, prefix with the model override and it routes to Ollama instead. No config changes needed, nothing to undo.

You could also make it easier with a couple of Fish aliases:

```bash
alias ccq='ANTHROPIC_MODEL=qwen2.5-coder:14b claude'
alias ccr='ANTHROPIC_MODEL=deepseek-r1:14b claude'
```

Add those to your `config.fish` and you've got `ccq` for Qwen and `ccr` for R1 — keeps it clean without touching your default `claude` command.

### HUMAN
so i have both models..now what: ❯ ollama list  NAME                 ID              SIZE      MODIFIED            deepseek-r1:14b      c333b7232bdb    9.0 GB    15 seconds ago         qwen2.5-coder:14b    9ec8897f747e    9.0 GB    About a minute ago      ~ ❯

### ASSISTANT
You're good to go. Both models are pulled and ready.

Next steps are just:

**1. Add the aliases to your Fish config:**
```bash
nano ~/.config/fish/config.fish
```
Add these two lines:
```bash
alias ccq='ANTHROPIC_MODEL=qwen2.5-coder:14b claude'
alias ccr='ANTHROPIC_MODEL=deepseek-r1:14b claude'
```
Save and then reload:
```bash
source ~/.config/fish/config.fish
```

**2. Test it:**
```bash
ccq
```
Should launch Claude Code with Qwen2.5-Coder as the backend. Give it a simple task and make sure it responds correctly.

That's it. You're set up. `claude` for when your sub is active, `ccq` as your daily driver when it's not, `ccr` when you need heavier reasoning.

### HUMAN
normally i would just launch the model in cursor with a command like this and im not sure what i need to do to get those two models plugged in?: claude --model qwen2.5-coder:14b

### ASSISTANT
That flag won't work for local Ollama models — `--model` in Claude Code expects an Anthropic model ID like `claude-sonnet-4-6`, not an Ollama model name.

The inline env var override is the correct approach. So instead of:
```bash
claude --model qwen2.5-coder:14b
```

You'd run:
```bash
ANTHROPIC_MODEL=qwen2.5-coder:14b claude
```

In Cursor's terminal that works exactly the same way. The aliases just save you from typing that every time.

Do the aliases work in Cursor's terminal for you, or does it use a different shell?

### HUMAN
when i ran the command it does work see?: ❯ claude --model qwen2.5-coder:14b
 ▐▛███▜▌   Claude Code v2.1.70
▝▜█████▛▘  qwen2.5-coder:14b · API Usage Billing
  ▘▘ ▝▝    ~/vc projects/immortal agent
  /model to try Opus 4.6
───────────────────────────────────────────────────────────────────────── ▪▪▪ ─
❯ Try "fix lint errors"
───────────────────────────────────────────────────────────────────────────────
  ? for shortcuts
  Claude Code has switched from npm to native installer. Run `claude install…

### ASSISTANT
My bad — it does work and it's even cleaner than the env var approach. So your commands are just:

```bash
claude --model qwen2.5-coder:14b
```
```bash
claude --model deepseek-r1:14b
```

And when your sub is active, plain `claude` as usual. Simple as that, you're fully set up.

### HUMAN
im not sure how my env var are set up tho how do i check?

### ASSISTANT
Just run:

```bash
env | grep -i anthropic
```

That'll show you everything Anthropic-related that's set in your current environment.

### HUMAN
~ ❯ env | grep -i anthropic ANTHROPIC_API_KEY= ANTHROPIC_AUTH_TOKEN=ollama ANTHROPIC_BASE_URL=http://localhost:11434 ~ ❯

### ASSISTANT
Clean setup. Here's what each one is doing:

- `ANTHROPIC_BASE_URL=http://localhost:11434` — points Claude Code at your local Ollama instance instead of Anthropic's API
- `ANTHROPIC_AUTH_TOKEN=ollama` — dummy auth token so Claude Code doesn't reject the connection (Ollama doesn't need a real key)
- `ANTHROPIC_API_KEY=` — empty, which is fine since you're routing through Ollama locally

The only thing worth noting is that `ANTHROPIC_API_KEY` being empty means if you run plain `claude` without a model flag, it'll try to hit Anthropic's API and fail since there's no key. You'd need to either set your real API key there or always use `--model` when using Ollama.

How do you currently launch Claude Code when your Pro sub is active — through Cursor's UI or the terminal?

### HUMAN
through the terminal within cursor

### ASSISTANT
Then you'll want your real Anthropic API key in there so plain `claude` works when your sub is active. Otherwise it'll just error out.

Check if you have it somewhere:
```bash
cat ~/.config/fish/config.fish
```

Paste what you see and I can tell you exactly what needs to be added or changed to make both workflows work cleanly — `claude` for Pro sub, `claude --model qwen2.5-coder:14b` for Ollama.

### HUMAN
source /usr/share/cachyos-fish-config/cachyos-config.fish # overwrite greeting # potentially disabling fastfetch #function fish_greeting #    # smth smth #end function fish_greeting    fastfetch --logo ~/.config/fish/ascii-art.txt end ~ ❯

### ASSISTANT
Your Fish config is pretty bare — the Anthropic env vars must be getting set somewhere in the CachyOS config it's sourcing. Check there:

```bash
cat /usr/share/cachyos-fish-config/cachyos-config.fish | grep -i anthropic
```

That'll tell us where those vars are actually living so we know the right place to add your API key without breaking anything.

### HUMAN
❯ cat __/usr/share/cachyos-fish-config/____cachyos-config.fish__ | grep -i anthropic ~ ❯

### ASSISTANT
Nothing there either — so those env vars must be set somewhere else. Check:

```bash
cat ~/.config/fish/conf.d/*.fish 2>/dev/null | grep -i anthropic
```

And also:

```bash
cat ~/.bashrc ~/.profile ~/.bash_profile 2>/dev/null | grep -i anthropic
```

One of those should turn up where they're defined.

### HUMAN
~ ❯ cat ~/.config/fish/conf.d/*.fish 2>__/dev/null__ | grep -i anthropic fish: No matches for wildcard '~/.config/fish/conf.d/*.fish'. See `help language#wildcards-globbing`. cat ~/.config/fish/conf.d/*.fish 2>/dev/null | grep -i anthropic    ^~~~~~~~~~~~~~~~~~~~~~~~~~~^ ~ ❯ cat __~/.bashrc__ ~/.profile __~/.bash_profile__ 2>__/dev/null__ | grep -i anthropic ~ ❯

### ASSISTANT
Hmm, not showing up anywhere in the usual spots. Try:

```bash
grep -r "ANTHROPIC" ~/.config/ 2>/dev/null
```

And also check if Claude Code set them itself:

```bash
cat ~/.claude.json 2>/dev/null | grep -i anthropic
```

### HUMAN
❯ grep -r "ANTHROPIC" __~/.config/__ 2>__/dev/null__ /home/toastedmel0n/.config/fish/fish_variables:SETUVAR --export ANTHROPIC_API_KEY: /home/toastedmel0n/.config/fish/fish_variables:SETUVAR --export ANTHROPIC_AUTH_TOKEN:ollama /home/toastedmel0n/.config/fish/fish_variables:SETUVAR --export ANTHROPIC_BASE_URL:http\x3a//localhost\x3a11434

### ASSISTANT
There it is — they're stored in Fish's universal variables file, not `config.fish`. That's why they persist across sessions without being explicitly in the config.

To add your real Anthropic API key, just run:

```bash
set -Ux ANTHROPIC_API_KEY your-actual-key-here
```

But here's the problem — you have `ANTHROPIC_BASE_URL` pointing at Ollama globally. So even with a real API key set, plain `claude` will still route to Ollama instead of Anthropic's API.

You've basically got two options:

**Option 1 — Manual swap (simplest):**
When using your Pro sub, temporarily override the base URL:
```bash
ANTHROPIC_BASE_URL=https://api.anthropic.com claude
```

**Option 2 — Aliases for everything:**
```bash
alias cc='ANTHROPIC_BASE_URL=https://api.anthropic.com ANTHROPIC_API_KEY=your-key claude'
alias ccq='claude --model qwen2.5-coder:14b'
alias ccr='claude --model deepseek-r1:14b'
```

`cc` for Pro, `ccq` and `ccr` for Ollama. Clean separation, nothing conflicts.

Which approach feels better to you?

### HUMAN
when i tested the deepseek model i got this error?:  ▐▛███▜▌   Claude Code v2.1.70
▝▜█████▛▘  deepseek-r1:14b · API Usage Billing
  ▘▘ ▝▝    ~/vc projects/immortal agent
  /model to try Opus 4.6
❯ summarize what this project does based on the code                                                                                                               
  ⎿  API Error: 400 {"type":"error","error":{"type":"invalid_request_error","message":"registry.ollama.ai/library/deepseek-r1:14b does not support 
     tools"},"request_id":"req_7fce302a170234346489e065"}

### ASSISTANT
That's a known limitation — the R1 14B model doesn't support tool calling, which Claude Code relies on heavily for its agentic loop (reading files, running commands, etc).

This is actually the deciding factor. **Qwen2.5-Coder 14B is your model.** R1 won't work with Claude Code at all for anything practical.

Test Qwen to confirm it works:
```bash
claude --model qwen2.5-coder:14b
```
Then run the same summarize command and it should work fine.

### HUMAN
yeah that worked perfectly. is this the most optimal given my setup and limitations? i want the most efficient model for a cc backup when i dont have the sub

### ASSISTANT
Yes — Qwen2.5-Coder 14B is your answer, and the R1 limitation actually made the decision for you. No more debating.

It fits cleanly in your hardware, handles tool calling, works natively with Claude Code's agentic loop, and is specifically trained for exactly this use case. For a Pro sub backup on your rig, it's the optimal choice.

Your setup is now:
- `claude` → Anthropic API (when sub is active)
- `claude --model qwen2.5-coder:14b` → local Ollama backup

That's it. Clean, efficient, costs nothing to run.

### HUMAN
and this is better than the qwen 3.5 9b model?

### ASSISTANT
Yes, significantly. Same answer as before but now you have proof — you just ran it successfully on a real project.

Qwen2.5-Coder 14B is bigger, coding-specific, and trained for exactly the agentic tool-calling workflow Claude Code uses. The 9B is a general purpose model that happens to do some coding. Not the same thing.

You're done — stick with Qwen2.5-Coder 14B.

### HUMAN
seems kinda dumb?:

### ASSISTANT
Yeah that's the model hitting its limits on context-heavy tasks. A couple things happening there:

1. **The dev log summary was shallow** — it just read the file and gave you the first entry instead of actually parsing the full 642 lines and finding the most recent meaningful work.

2. **The "full rundown" response was weird** — it called a diagnostics tool instead of actually reading through the log properly.

3. **It just stopped** when you asked it to run tests, no response at all.

This is Qwen2.5-Coder 14B showing its ceiling. It's not dumb exactly, it just struggles when tasks require holding a lot of context and reasoning about what to do next simultaneously.

For Operation Immortal Agent specifically — this is a complex enough project that honestly the local model is going to frustrate you more than help. My real recommendation:

**Use your Pro sub for this project.** Save the Qwen2.5-Coder backup for simpler tasks — quick scripts, config edits, basic questions. Anything involving your actual projects with real codebases and dev logs, you want the real Claude behind it.

The local model setup is still worth having, just be realistic about where it earns its keep.

### HUMAN
anything local that COULD keep up?

### ASSISTANT
Honestly, on your current hardware? Not really — not for a codebase this complex.

The models that could actually keep up are the ones you can't run:

- **Qwen3-Coder-Next** — purpose built for exactly this, but needs 42GB minimum
- **DeepSeek R1 32B** — better reasoning, but needs ~20GB+ and breaks on tool calling anyway
- **Qwen2.5-Coder 32B** — the right model, but needs ~20GB VRAM/RAM headroom you don't have stably

The hard truth is your 8GB VRAM is the wall. Operation Immortal Agent has a 642 line dev log, multiple interconnected modules, Jupiter/Marinade API integrations — that's not a 14B model job.

**The practical answer:** a RAM upgrade changes everything. Going from 32GB to 64GB DDR5 would let you run Qwen2.5-Coder 32B comfortably offloaded across VRAM and RAM, and that's a model that could actually handle your project meaningfully.

For now though — Pro sub for Immortal Agent, Qwen2.5-Coder 14B for everything lightweight. That's the honest ceiling of your current setup.

### HUMAN
When I was testing qwen 3.5 9b tho it felt better even if it took longer for a response

### ASSISTANT
That's actually useful feedback and worth trusting your gut on. A few possible reasons:

**The 9B might have felt better because:**
- Qwen3.5 is a newer architecture than Qwen2.5-Coder — newer training, better instruction following
- The 9B you tested may have been more coherent on conversational/contextual tasks even if slower
- Qwen2.5-Coder 14B is optimized for code completion, not necessarily for the back-and-forth agentic conversation style Claude Code uses

**Worth checking:** pull the Qwen3.5 14B instead — it's the newer architecture at the same size:

```bash
ollama pull qwen3:14b
```

That might give you the best of both — newer Qwen3.5 quality at 14B size, with tool calling support. Could genuinely outperform Qwen2.5-Coder 14B for your use case based on what you described.

Test it the same way on your project and compare. Your real world experience on your actual codebase is more reliable than benchmarks at this point.

### HUMAN
Will that run on my hardware?

### ASSISTANT
Yes, same size as what you're already running — 14B at Q4 is around 9GB, fits in your VRAM just like the others.

```bash
ollama pull qwen3:14b
```

Then test it:
```bash
claude --model qwen3:14b
```

Run the same summarize and dev log commands you used before and see how it feels compared to Qwen2.5-Coder. At this point you're just finding which one clicks best with your workflow on real tasks.

### HUMAN
I said 3.5 why are you saying qwen 3?

### ASSISTANT
My bad — I assumed Qwen3.5 wasn't out yet since it's past my knowledge cutoff. Let me check.
```
This block is not supported on your current device yet.
```

Good news — Qwen3.5-9B was released on March 2, 2026, so it's very recent and likely what you were already testing. Now the key question is whether it's on Ollama yet:
```
This block is not supported on your current device yet.
```

It's on Ollama and supports tool calling. Qwen3.5 small models support native tool calling, thinking, and multimodal capabilities in Ollama.

So if the 9B felt better to you in practice, there's now a legitimate reason to test it properly against Qwen2.5-Coder 14B for Claude Code. Pull it and compare:

```bash
ollama pull qwen3.5:9b
claude --model qwen3.5:9b
```

It's only 6.6GB so it'll sit entirely in your VRAM with room to spare, and being a newer architecture it may genuinely outperform the older Qwen2.5-Coder 14B on instruction following and agentic tasks despite being smaller.

Run the same test — summarize the project, ask about the dev log — and just go with whichever one actually performs better for you. Real world feel on your own codebase beats benchmarks every time.