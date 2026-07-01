---
type: topic
tags: [topic, moc, q2-2026]
aliases: [ai tools, ai tooling, local llm]
---

# AI Tools

*744 conversations about LLMs, agents, local inference, and the tooling landscape. This is where I spend most of my time — and most of my energy.*

---

## What I know

I don't just use AI tools — I study them. I can compare features, pricing, and capabilities across every major LLM, coding assistant, and local inference tool. I know the difference between an LLM (text-in, text-out) and an agent (framework + tools + loop). I understand quantization (Q4_K_M), VRAM constraints, and the trade-offs between model size and performance.

But here's the thing: this knowledge is encyclopedic, not practical. I know *about* the tools more than I know how to use any single one to ship a product. That's the gap I'm working on.

---

## The journey

### Image generation
I started with image generation. I really liked the style of a ghost with sunglasses, but I wanted it more weed-themed with fantasy themes from Elden Ring or Dark Souls. I've generated retro-styled posters of people fixing computers for Facebook flyers. I've asked about Gucci snow goggles on character images with specific positioning and branding details.

I asked about Freepik: *"What can you tell me about freepik? How does it work and can you use local models with it? I'm assuming it has credit costs the same way you would with any other LLM."*

### Local LLM setup
I've set up Ollama, Oobabooga, and various models. I've fought with requirements.txt files, virtual environments, and the fact that `llama-cpp-binaries` markers don't match my environment. I've learned that you should install the model *after* running the Oobabooga installation, not before.

I asked: *"wouldn't it make more sense to use the gguf version since I only have a 8gb 3070?"* The answer was yes. I'm still working on the optimization.

### The agent epiphany
I had a breakthrough understanding of how agents work — LLM as brain, framework as body, skills as hands. This reframed my entire approach from "building agents" to "understanding repeatable processes." I stopped thinking about which framework was best and started thinking about what I actually wanted the agent to *do*.

I've designed JSON context profiles for multi-agent workflows in Cursor. I've worked on CrewAI-based helpdesk systems with five-agent structures. I've asked: *"for each thing I want do I need to use each tool or is it all within one ui I can use?"*

### The cost question
I've asked about Claude API pricing more times than I can count. *"Can you break down how API cost works with Claude and whether I need Claude Pro to use it in Cursor?"* I've looked for open-source models to plug into Claude Code as cost-effective alternatives. I'm always trying to balance capability with cost.

### The environmental impact
I was just wondering about the environmental effect of LLM data centers. *"I was just wondering because of the environment effect the current cooling method has."* It's not just about what the tools can do — it's about what they cost the planet.

---

## What I've learned

**The 3070 is good enough.** Every LLM expert says the same thing: your 3070 is fine, run a 7B-13B quantized model, stop worrying. I keep asking because I don't trust that "good enough" is good enough. But it is.

**Local is the future.** I want my AI helpdesk to execute real commands — installing software, automating IT support tasks. I want models running on my own machine, not dependent on big tech's API. The unified memory architecture of Mac Minis is appealing for this reason.

**Skills matter more than frameworks.** I've moved from "building agents" to "understanding repeatable processes." The agent framework is almost commodity — the real value is in understanding what you want the agent to do and encoding that as a skill.

**Cost matters.** I'm always balancing capability with cost. I've asked about open-source alternatives, local inference, and API pricing. I want the most capability for the least spend.

---

## Current setup

- **Ollama** — local model inference
- **Oobabooga** — text generation web UI
- **Cursor** — AI-powered IDE
- **Claude Code** — terminal-based coding assistant
- **CrewAI** — multi-agent framework
- **Various models** — Mistral, Llama, Gemma, Qwen, and more

---

## What I'm working on

- **Multi-agent helpdesk** — CrewAI-based system with five-agent structure
- **Local LLM optimization** — finding the right model for my 3070
- **Cost reduction** — open-source alternatives to expensive API calls
- **Project Immortal Agent** — the ambitious one that's on hold until the funding model is realistic

---

## Key Conversations

- [[processed/GEMINI/2025-02-16_I_really_like_the_style_of_this_ghost_with_sunglasses_but_I__51943442.md|Image generation]] — "I really like the style of this ghost with sunglasses but I want it more weed themed"
- [[processed/GPT/2025-08-02_Freepik_features_and_usage_72722123.md|Freepik research]] — "What can you tell me about freepik?"
- [[processed/GEMINI/2025-06-24_So_the_one_thing_Ive_seen_that_I_kind_of_had_an_issue_with_t_68034055.md|Oobabooga lessons]] — "I tried to install the model before running the Ubuga installation"
- [[processed/GEMINI/2026-04-07_Do_you_even_know_what_project_immortal_agent_was_for_me_60173943.md|Agent epiphany]] — "I was riffing based on the Second Me blueprint"
- [[processed/GPT/2025-05-01_LLM_Server_Cooling_Solutions_27119142.md|Environmental impact]] — "I was just wondering because of the environment effect the current cooling method has"
- [[processed/GEMINI/2025-07-05_what_model_did_we_switch_to_56954498.md|Model switching]] — "what model did we switch to?"

---

## Related

- [[nodes/people/bryan.md|Bryan]] — the person who knows these tools
- [[nodes/projects/operation-immortal-agent.md|Operation Immortal Agent]] — the most ambitious AI project
- [[nodes/projects/private-ai-consulting.md|Private AI Consulting]] — the business built on this knowledge
- [[nodes/topics/tech/homelab.md|Homelab]] — the infrastructure these tools run on
- [[nodes/topics/tech/coding.md|Coding]] — the skills AI helps with
- [[nodes/topics/career/career.md|Career]] — where this knowledge is taking me
- [[nodes/topics/thinking-patterns.md|Thinking Patterns]] — how I approach learning new tools
