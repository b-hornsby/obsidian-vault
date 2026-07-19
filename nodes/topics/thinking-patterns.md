---
type: topic
tags: [meta, second-brain, bryan]
aliases: [Bryan's Thinking Patterns, How Bryan Thinks, Mental Models]
---

# Thinking Patterns

*How I think, decide, learn, and build — synthesized from 3,400+ conversations across 30 months.*

This page is the mind of the second brain. It's not just what I know — it's *how* I know it. The patterns that show up across every project, every conversation, every late-night troubleshooting session.

See: [[insights/thinking-patterns/2026-05-18-patterns-raw-data.md|May 18 Patterns (raw data)]]

---

## Core Identity

**I'm a builder who has confused preparation with progress.**

This is the single biggest pattern across 3,400 conversations. Every other pattern flows from this one. I research instead of deciding. I plan instead of shipping. I optimize instead of committing. I build infrastructure instead of products. I ask questions instead of answering them. I start projects instead of finishing them.

The vault is full of potential energy — plan.md files, architecture diagrams, tool comparisons. It's nearly empty of shipped products, paying customers, and completed certifications.

But I'm aware of this pattern. Awareness is the first step. And this vault is part of the solution — it's a thing that exists in the world, not just another plan.

---

## How I Approach Problems

### Research-First, Then Build (But the Ratio Is Skewed)

15.6% of my conversations start with "how do i" or "how to." I don't jump into code. I ask how things work first. This is genuine intellectual curiosity, not laziness.

11.9% start with "build/create/make/setup." When I do commit to building, I go deep fast. The Flappy Bird project went from zero to full PRD with Phaser 3, pixel art style, shop economy, and character roster in 10 days.

But only 51.5% of conversations reach "resolved" status. The rest are partial (73.4%), unresolved (4.1%), or abandoned (0.5%). The research-to-completion pipeline leaks badly.

### The 72-Hour Build Window

Every project follows the same arc:
- **Day 1:** High energy. Architecture, planning, tool selection, first steps.
- **Day 2:** Continued momentum. Implementation details, debugging, iteration.
- **Day 3:** Either shipping (rare) or stalling (common).
- **Day 4+:** Either done or abandoned.

The homelab is the exception that proves the rule. It's the only project that sustains long-term energy (793 conversations) because it's not a project with a finish line — it's an environment I live in. Every fix, upgrade, or new tool is a small win that doesn't require a big commitment.

### When I'm Stuck: Switch, Don't Push

I rarely say "I'm stuck." Instead:
1. **Switch tools** — if Cursor isn't working, try LM Studio. If Ollama has CUDA issues, try a different model.
2. **Switch LLMs** — if GEMINI can't solve it, ask CLAUDE. If CLAUDE can't either, ask GROK.
3. **Switch projects** — the most common response to being stuck isn't persistence, it's a new conversation about something else entirely.

The rare exception: when something genuinely breaks and I can't ignore it. CUDA drivers, bootloader entries, audio routing — these get very specific, error-message-level questions. Short, frustrated, often unresolved. But I don't linger on stuck — I move on.

---

## Decision-Making Style

### Analysis Paralysis Disguised as Due Diligence

My decision-making process follows a predictable cycle:
1. Identify the decision (which tool, which model, which title)
2. Research exhaustively (ask multiple LLMs, compare features, read reviews)
3. Narrow to 2-3 options
4. Seek external validation (ask another LLM, ask again in a week)
5. Either choose arbitrarily or let the decision expire

5.2% of conversations contain "vs" comparisons. I frame decisions as head-to-head matchups. Cursor vs Windsurf. Ollama vs Oobabooga. GEMINI vs CLAUDE. The comparison loop is a way of avoiding commitment.

### What Prevents Execution

1. **"Good enough" threshold is undefined.** I don't know when to stop optimizing. The 3070 is good enough for local LLMs, but I keep researching. The LinkedIn profile is good enough, but I keep tweaking.
2. **Cost of being wrong > cost of not deciding.** Every choice has visible opportunity cost. Choosing Cursor means not choosing Windsurf. Choosing the 9B model means not choosing the 35B.
3. **Planning is safer than shipping.** A plan can't fail. A shipped product can be judged. I've written more plan.md files than lines of shipped code.

### What Triggers Action

- **Deadlines and external pressure.** "I need this working by Friday." "I'm applying for jobs next week."
- **Frustration as catalyst.** 13% of conversations are tagged "frustrated." When something breaks and I can't ignore it, I fix it.
- **Novelty.** New tools, new models, new platforms — these trigger immediate engagement. The first conversation about a new thing has the highest energy. The tenth conversation about the same thing has the lowest.

---

## Recurring Loops (Unresolved)

These are the questions I've asked repeatedly, across multiple LLMs, over months, without reaching resolution:

| Loop | Frequency | Root Cause |
|------|-----------|------------|
| Which AI coding tool? | 25+ times | Permission to start building |
| Best local LLM for RTX 3070? | 15+ times | "Good enough" isn't trusted |
| How do I learn Python? | 15+ times | LLM as replacement for curriculum |
| What LinkedIn title? | 12+ times | Identity, not strategy |
| How do I set up [infrastructure]? | 100+ times | Productive loop — actually learns |

### What I Never Ask About

- **Pricing, sales, customer acquisition.** The Private AI Consulting project has 85+ conversations and zero about finding or closing clients. I build the product in my head but never ask "who will pay for this?"
- **Health, fitness, sleep.** Despite working a warehouse job and spending hours at a computer, there are no conversations about physical well-being.
- **Relationships in depth.** 16 conversations linked to girlfriend, 17 to dad, but they're surface-level (helping with a resume, casual mentions). I don't process emotional dynamics with LLMs the way I process technical problems.
- **"Am I good enough?"** — never asked directly, but every cross-LLM cluster, every tool comparison, every LinkedIn title question is asking it indirectly.

---

## Knowledge Map

### What I Know Deeply

- **Homelab infrastructure** (793 conversations). Expert-level for a hobbyist. CachyOS, Steam Deck Linux, WSL2, Windows 11, CUDA, Docker, Syncthing, OBS. I can set up complex systems and debug them methodically.
- **AI tooling landscape** (744 conversations). I know every major LLM, every coding assistant, every local inference tool. I can compare features and pricing. But this knowledge is encyclopedic, not practical — I know about the tools more than I know how to use any single one to ship a product.
- **Crypto/Web3 mechanics** (194 conversations). I understand leverage, perps, stop-losses, DEX aggregators (Jupiter), and wallet management (Phantom). The gap is in consistent strategy execution.

### Dunning-Kruger Zones

- **Python programming** (533 conversations). 15+ months of "learning," still asks beginner questions. I use LLMs to write Python instead of learning Python. The knowledge doesn't transfer.
- **Trading strategy.** I understand indicators (EMA, MA crossovers, slippage, MEV) but can't explain a coherent trading thesis. I know the vocabulary but not the language.
- **Business/consulting.** I talk about "private AI solutions" but have never had a customer conversation, defined a service package, or set a price. The business exists in planning documents and LinkedIn headlines, not in revenue.

### What I Avoid Learning

- **Fundamentals.** I avoid structured learning (courses, books, curricula) in favor of just-in-time LLM queries. This works for specific problems but fails for building a coherent knowledge base.
- **Sales and marketing.** I build the product (in my head) and ignore the business entirely.
- **Soft skills.** No conversations about communication, negotiation, leadership, or management. The career transition plan is entirely technical.

---

## Emotional Patterns

### Frustration (13% of conversations)

Frustration clusters in three contexts:
1. **Tooling failures** — CUDA errors, model loading failures, IDE configuration issues. Sharp but short-lived. I either fix it or move on.
2. **Crypto trading problems** — liquidations, leverage confusion, platform restrictions. More persistent because they involve real money.
3. **Career stagnation** — quieter but deeper. Conversations about LinkedIn titles, cover letters, and job applications carry an undercurrent of "I'm still here, I'm still in the warehouse, nothing has changed."

Technical frustration gets solved. Existential frustration gets avoided.

### Curiosity (26% of conversations — #1 sentiment)

Curiosity is my default state. "What is X?" "How does X work?" "Can I build X?" This is where I do my best learning. Most building conversations start as curiosity.

### Energy (13% of conversations — #2 sentiment)

Building is where I do my best work. When I'm building, I ask specific, actionable questions. I iterate quickly. I follow through to resolution. I'm generous with context — I share my full setup, my goals, my constraints.

### The Emotional Arc

```
Day 1: Curious → Building (high energy, specific questions)
Day 2: Building → Frustrated (hitting walls, debugging)
Day 3: Frustrated → Exploratory (researching alternatives)
Day 4: Exploratory → [Abandoned or Resolved]
```

Projects that sustain past Day 3 are the ones where frustration leads to breakthrough (not a tool switch) and exploration leads to a decision (not another comparison).

---

## What Gives Me Momentum

1. **Quick wins** — Syncthing working, OBS routing audio, a model loading successfully. Small victories compound.
2. **Visible progress** — The homelab works because every change is immediately visible. The streaming rig works because every overlay, every audio route, every scene is a tangible improvement.
3. **Novelty** — New models, new tools, new platforms. The first conversation about Hermes Agent had more energy than the 100th conversation about Ollama configuration.

---

## Key Relationships

- [[nodes/people/bryan.md|Bryan]] — the person these patterns describe
- [[nodes/projects/homelab-stack.md|Homelab]] — the one project that sustains long-term energy
- [[nodes/projects/private-ai-consulting.md|Private AI Consulting]] — the most ambitious, least executed
- [[nodes/projects/operation-immortal-agent.md|Operation Immortal Agent]] — the most thoroughly planned, least running
- [[nodes/topics/career/it-certification.md|IT Certification]] — the career escape plan in progress
- [[nodes/projects/streaming-rig.md|Streaming Rig]] — the creative outlet that actually ships
- [[nodes/projects/job-search.md|Job Search]] — the active escape plan
- [[nodes/projects/resume.md|Resume]] — the document that has to do 80% of the work

---

## The Meta-Pattern

**The vault is a mirror.** 3,400 conversations showing what I *could* build, *could* learn, *could* become. The conversion rate from potential to actual is low. But it's getting better.

**I don't want sugarcoating.** I asked an AI to be my brutally honest advisor. I told it to cut through my blind spots. That's how I learn best — direct, uncomfortable truth.

**The next conversation matters more than the next 3,400.** Pick the smallest project. Ship it in 72 hours. Not a plan. Not a blueprint. A thing that exists in the world. Then do it again.

---

*Last updated: 2026-05-19. Based on analysis of 3,400 enriched conversations. For the full data report, see [[insights/thinking-patterns/2026-05-18-patterns-raw-data.md|May 18 Patterns (raw data)]].*


## Related
- [[nodes/people/bryan|Bryan]]
