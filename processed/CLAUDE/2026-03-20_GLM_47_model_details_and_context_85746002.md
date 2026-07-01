---
id: 619286
source: CLAUDE
date: 2026-03-20
tags: ['glm-47-model', 'llm-details', 'ai-model-selection']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md', 'nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/coding.md']
summary: Bryan is seeking information about the GLM 4.7 model, specifically the 'flash' version, to understand its capabilities.
---
# GLM 4.7 model details and context

### HUMAN
What can you tell me about the glm 4.7 model we decided on?

### ASSISTANT
```
This block is not supported on your current device yet.
```

I don't have any record of us discussing GLM-4.7 in past conversations, so I can't speak to what you decided or the context around that choice. It's possible that conversation just hasn't made it into my memories yet, or it happened somewhere else.

That said, here's what I can tell you about the model itself:

GLM-4.7 is Z.ai's latest flagship model, with upgrades focused on enhanced programming capabilities and more stable multi-step reasoning.

**Coding performance** is the headline feature. It ranks #1 open-source on LMArena Code Arena, hits 73.8% on SWE-bench Verified, and scores 84.9% on LiveCodeBench V6 — beating Claude Sonnet 4.5 on that benchmark.

**Reasoning architecture** is notably different from most models. It uses interleaved thinking, where the model reasons before each action, tool call, or response — rather than treating reasoning as a single upfront step. It also introduces preserved thinking, allowing reasoning context to persist across turns.

**Turn-level thinking control** is a practical feature for agentic work. You can disable thinking for lightweight requests to reduce latency and cost, or enable it for complex tasks to improve accuracy and stability.

**Local deployment** is viable with the Flash variant. GLM-4.7-Flash is a 30B MoE model — the smallest version requires at least 16GB of RAM, supports tool use and reasoning, and is available in GGUF and MLX formats. That could be relevant for your home lab setup.

**Agentic framework support** includes mainstream agent frameworks like Claude Code, Kilo Code, Cline, and Roo Code.

Can you give me more context on where GLM-4.7 fits — is this for one of your projects like Operation Immortal Agent or the Offline Helpdesk Assistant?

### HUMAN
Specifically glm 4.7 flash

### ASSISTANT
Good context — the Flash variant is the more relevant one for local/home lab use. Here's what stands out:

GLM-4.7-Flash is a 30B MoE reasoning model built for local deployment, using ~3.6B active parameters, supporting 200K context, and leading benchmarks in coding, agentic workflows, and chat. It runs on 24GB RAM/VRAM (32GB for full precision).

It's available in GGUF and MLX formats, supports tool use and reasoning, and the minimum to run it is 16GB of RAM.

A few practical notes for running it locally:

- The GGUF works well on llama.cpp and backends like LM Studio and Jan, but they currently don't recommend running it with Ollama due to potential chat template compatibility issues.
- There was a notable bug in llama.cpp that caused looping and poor outputs — it's been fixed, but if you're downloading a GGUF, make sure you're grabbing the updated version. Also, disable repeat penalty or set it to 1.0.
- For 4-bit quantization you'll need around 18GB RAM/unified memory.

Given that you're running Ollama for your Offline Helpdesk Assistant project, that compatibility caveat is worth keeping in mind. LM Studio or llama.cpp directly might be the safer path with this one. Do you remember what prompted the decision to go with Flash specifically — was it the VRAM constraints on your setup?
