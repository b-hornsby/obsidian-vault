---
id: 641704
source: GROK
date: 2026-04-07
tags: ['hermes-agent', 'claude-code-skills', 'obsidian', 'local-ai-stack', 'personal-knowledge-base', 'multi-agent']
category: ai-tools
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/second-brain-vault.md', 'nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan was exploring how to use Hermes agent with Claude Code skills, Obsidian, and his personal chat logs and Wikipedia data to build a personalized local AI knowledge system.
---
# Hermes Agent Using Claude Code Skills

### HUMAN
Technically with the Hermes agent can’t you technically use the skills it builds with Claude code for example?

### ASSISTANT
**Yes, exactly.** Hermes Agent has a built-in **claude-code** skill (it's one of the official built-in ones), so you can directly delegate coding tasks to Anthropic's Claude Code CLI from within Hermes.<grok:render card_id="082ace" card_type="citation_card" type="render_inline_citation"><argument name="citation_id">0</argument></grok:render>

### How it works
Hermes Agent is designed with a **skills system** that's quite flexible and compatible across agents. Its "Skills Hub" includes:

- A built-in **claude-code** skill that lets Hermes hand off tasks like building features, refactoring, PR reviews, iterative coding/debugging, etc., straight to Claude Code (you just need the Claude CLI installed).
- Skills are essentially reusable, improvable tools or workflows that Hermes creates from experience, errors, and interactions. They follow an open standard that's compatible with other agents/tools like Claude Code, Cursor, Codex, etc.<grok:render card_id="02982f" card_type="citation_card" type="render_inline_citation"><argument name="citation_id">2</argument></grok:render>

So technically, yes — Hermes can **use, invoke, and even build upon** skills/workflows that originate from or are designed for Claude Code (and vice versa in many cases). The agent has a self-improving "learning loop" where it:
- Observes outcomes.
- Refines or creates new skills.
- Stores persistent memory across sessions.
- Can improve those skills over time, including ones that wrap or extend Claude's coding capabilities.<grok:render card_id="a71afa" card_type="citation_card" type="render_inline_citation"><argument name="citation_id">6</argument></grok:render>

### Practical example
You could tell Hermes something like "Build a new feature for my project using Claude Code for the heavy lifting, then review and integrate it." Hermes would:
1. Delegate the coding part to Claude Code via the skill.
2. Learn from the result.
3. Potentially create an improved/custom skill for similar future tasks.

This interoperability is a key feature — the skills are meant to be portable across these agent ecosystems.<grok:render card_id="8581d2" card_type="citation_card" type="render_inline_citation"><argument name="citation_id">18</argument></grok:render>

If you're running Hermes locally or on a VPS, it's model-agnostic too (you can use it with various backends), which makes mixing tools like this even smoother. Check the official docs at hermes-agent.nousresearch.com for setup and the full skills list.

### HUMAN
No I meant like the skills it learns as you use it. Aren’t those transferable?

### ASSISTANT
**Yes, the skills Hermes learns and creates as you use it are designed to be transferable and portable.** 

This is one of the core strengths of the system. Here's the breakdown:

### Open Standard Format
Hermes skills (both the ones it auto-creates from experience and the built-in/community ones) follow the **agentskills.io open standard**. These are essentially self-contained `SKILL.md` files (Markdown with YAML frontmatter) stored in `~/.hermes/skills/`. 

Because it's an open format, they're **compatible and portable** across many agent ecosystems, including:
- Claude Code
- Cursor
- Codex / OpenAI tools
- Other agents like those using similar skill systems (e.g., integrations with VS Code, GitHub, Goose, Amp, etc.)

You can share, export, copy, or install them elsewhere without major conversion. The agent itself can browse/install from hubs like agentskills.io, ClawHub, LobeHub, GitHub repos, and more.<grok:render card_id="45405e" card_type="citation_card" type="render_inline_citation"><argument name="citation_id">44</argument></grok:render>

### How Learned Skills Work & Transfer
- **Auto-creation & self-improvement**: After completing complex tasks, Hermes synthesizes the experience into a new or improved reusable skill (procedural memory). It can also refine existing ones over time during use.
- **Storage**: They live as files in your local skills directory, making them easy to back up, share, or move.
- **Migration/Import**: Hermes has explicit support for importing skills from other systems (e.g., it can automatically migrate skills from OpenClaw during setup). You can point it at external/shared skill directories via config for multi-tool use.<grok:render card_id="341c98" card_type="citation_card" type="render_inline_citation"><argument name="citation_id">18</argument></grok:render>
- **Export/Publish**: Commands like `hermes skills publish`, `snapshot`, or simply copying the folder let you share them or use them in other compatible agents.

In practice, a skill Hermes builds for your specific workflow (e.g., a custom refactoring process or project-specific automation) can often be dropped into Claude Code or another tool that supports the standard, and vice versa—skills originating from Claude Code can be used or adapted in Hermes.

### Practical Tips
- Check your skills folder: `~/.hermes/skills/` (or use `hermes skills list`).
- For sharing/transfer: Use the CLI for publish/snapshot or just git clone/share the Markdown files.
- Community aspect: Many users build and share custom skills that work across Hermes + Claude Code setups.

If you're running it locally or on a VPS, this portability means your "grown" agent capabilities aren't locked in—one reason it's popular as a self-improving system that outgrows single-tool limitations. 

For the most up-to-date details, the official docs at hermes-agent.nousresearch.com/docs/skills/ cover the full system, including external dirs and the open spec. Let me know if you want help with specific commands or examples!

### HUMAN
Can Hermes spin up multiple sub agents?

### ASSISTANT
**Yes, Hermes can spin up multiple sub-agents (also called child agents).**

This is a core built-in capability via the **`delegate_task`** tool. Here's how it works:

### Subagent Delegation Features
- **Isolated child agents**: Hermes spawns temporary, fully isolated `AIAgent` instances. Each sub-agent gets:
  - Its own fresh conversation (zero knowledge of the parent's history).
  - Its own terminal session.
  - A restricted/custom toolset (you can specify exactly what tools/skills it can use).
  - Independent execution.
- **Parallel execution**: You can run **up to 3 concurrent sub-agents** at once (via batch mode with a thread pool). This is great for parallel workstreams—like researching multiple topics, processing batches of items, or breaking down complex tasks (e.g., one for research, one for coding, one for review).
- **How results return**: Only the final summary from each sub-agent comes back to the parent. Intermediate steps and tool calls stay isolated to keep the parent's context clean and token-efficient.
- **Depth limits**: Currently limited (e.g., MAX_DEPTH=2 in some setups), so grandchildren are often blocked to prevent uncontrolled spawning.
- **Modes**:
  - Single task delegation.
  - Parallel batch (up to 3).

**Example use cases**: "Break this down: delegate research on X to one sub-agent, Y to another, and synthesize results" or handling 50 items in parallel by spawning a few workers.

Sub-agents are **ephemeral/throwaway** by design for delegation—they don't persist like the main agent or share ongoing state/communication with each other mid-task. This is more "hierarchical delegation with parallelism" than a fully collaborative peer-to-peer swarm (though there's an open GitHub issue working toward richer multi-agent orchestration, roles, and inter-agent cooperation).

### Separate from Profiles (Persistent Multiple Agents)
In addition to on-the-fly sub-agents, Hermes supports **Profiles** for running **multiple fully independent, persistent Hermes agents** on the same machine. Each profile has its own:
- Config, `.env`, memory, skills, sessions, cron jobs, etc.
- Isolated directory and identity (e.g., one "coder" profile, one "researcher," one "personal").

You can create them easily (e.g., `hermes profile create coder`), and they become separate commands like `coder chat`.

### Other Related Capabilities
- **Skills for agents**: There are bundled skills for spawning additional full Hermes instances as subprocesses or orchestrating coding agents.
- **Code execution tool**: For more mechanical pipelines, Hermes can write Python scripts that call tools via RPC, collapsing workflows without spawning full sub-agents.

This makes Hermes flexible for parallelization and task breakdown while keeping the main agent's context manageable. It's evolved from a single-agent focus but includes strong delegation tools today.

For the latest details and examples, check the official docs:
- [Subagent Delegation](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation/)
- [Profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles/)
- [Delegation Patterns](https://hermes-agent.nousresearch.com/docs/guides/delegation-patterns/)

If you're setting it up or want command examples, let me know!

### HUMAN
Is obsidian open source? Does the data leave your machine?

### ASSISTANT
**No, Obsidian is not open source.** Its core application is closed-source (proprietary), even though it's free to use. 

Many people initially assume it is open source because:
- Your notes are stored as plain Markdown files in a local folder (fully open format).
- The community plugins and themes ecosystem is largely open source.
- The company maintains some public GitHub repos (e.g., for plugin lists and samples), but the main Obsidian app itself is not.

The developers have explained their reasons for keeping the core closed, and there’s no indication it has changed as of 2026. If full open-source transparency is important to you, popular alternatives include **Logseq**, **Joplin**, **Anytype**, or **Trilium**.

### Does the data leave your machine?
**By default, no — your notes stay completely local.** 

- Obsidian stores everything as plain Markdown files in a folder (called a "vault") on your device’s file system.
- The app itself does **not** send your note content to Obsidian’s servers. The official privacy policy states: "All data is saved locally on your device and is never sent to our servers. We do not collect any personal data. We do not collect any telemetry data."
- You can use it 100% offline with zero internet required for core functionality.

**Exceptions (optional features):**
- **Obsidian Sync** (paid): If you enable their sync service, your vaults are end-to-end encrypted before leaving your device. The company cannot read your notes.
- **Obsidian Publish**: For sharing public sites — only the pages you explicitly publish go to their servers.
- **Community plugins**: Some third-party plugins may connect to the internet (e.g., for updates, AI features, or external services). You can review/block them individually.

**Bottom line for privacy**: Your raw notes never leave your machine unless you choose a sync/publish option or use a plugin that does so. Many users sync vaults manually with tools like Git, Syncthing, Dropbox, or iCloud without ever touching Obsidian’s servers. You can even firewall the app to prevent any outbound connections.

This local-first design is one of Obsidian’s biggest strengths for privacy-conscious users, even though the app itself isn’t open source.

### HUMAN
Okay back to the skills aspect of things. So you’re saying I can use the skills my agent creates with other ai tools like Claude code for example?

### ASSISTANT
**Yes, exactly.** Skills that Hermes creates (or improves) as you use it are **portable and can be used with other AI tools like Claude Code**.

### Why They’re Transferable
Hermes skills follow the **agentskills.io open standard** (originally from Anthropic and now adopted widely). Each skill is a self-contained `SKILL.md` Markdown file with YAML frontmatter + structured sections like:
- Name, description, version
- When to use / Quick reference
- Procedure / steps
- Pitfalls / verification

These live in your local folder (usually `~/.hermes/skills/`). Because it’s a plain-text, open format with no proprietary lock-in, you can:
- Copy the skill folder/file directly into Claude Code’s skills directory (Claude Code looks for them in `~/.claude/skills/` or similar paths).
- Use them in Cursor, OpenAI Codex, other compatible agents, or even share via GitHub.
- Install/share the other way around—skills made for Claude Code often work in Hermes with little or no modification.

### Practical Flow
1. Hermes works on tasks → learns from outcomes → auto-generates or refines a `SKILL.md` file (its "procedural memory").
2. You (or Hermes) can then copy/export that skill.
3. Drop it into Claude Code (or another tool) and it becomes available there for delegation, reuse, or further improvement.

Many users run **hybrid setups**: Hermes as the main orchestrator that delegates heavy coding to Claude Code via the built-in `claude-code` skill, while sharing custom learned skills back and forth.

### How to Move Them
- **Manual**: Just copy the skill folder from `~/.hermes/skills/` to the equivalent folder in Claude Code/Cursor/etc.
- **Hermes commands**: There are export/import/publish options for skills.
- **Community hubs**: Install from agentskills.io, GitHub repos, ClawHub, LobeHub — most are cross-compatible.

This interoperability is a deliberate design goal so your invested time building agent capabilities isn’t trapped in one tool.

If you want step-by-step commands for exporting a skill from Hermes and importing it into Claude Code (or examples of what a transferable skill looks like), just let me know!

### HUMAN
So for the stack to set this up I’m thinking Docker + Gemma 4 + Hermes agent + obsidian. Thoughts?

### ASSISTANT
**Yes, that's a solid, privacy-focused, local-first stack** — especially if you want everything running on your own hardware with minimal data leaving the machine. It aligns well with self-improving agents, portable skills, and note-taking.

Here's a balanced breakdown of **pros, cons, and practical thoughts** on Docker + Gemma 4 + Hermes Agent + Obsidian:

### Strengths of This Combination
- **Fully local & private**: Gemma 4 (Google's latest open models, released early April 2026) runs offline via Ollama or vLLM. Your notes stay in Obsidian's local Markdown vaults. Hermes can be configured to use only local inference — no cloud APIs needed unless you want hybrid.
- **Hermes + Docker**: Excellent synergy. Hermes has official Docker support and can use **Docker as its terminal backend** for sandboxed command execution (highly recommended for safety). You can run the entire Hermes agent itself in a container with persistent volumes for skills/memory.
- **Gemma 4 for Hermes**: Gemma 4 models (especially the larger 26B/31B variants or efficient ones) are strong for agentic/reasoning tasks. Hermes works great with Ollama-backed models like Gemma. Smaller quantized versions (e.g., 4B–9B effective) run on consumer hardware; bigger ones need a decent GPU (24GB+ VRAM recommended for reliable multi-step agent work).
- **Obsidian integration**: Hermes has built-in skills/plugins for Obsidian (e.g., reading/writing notes, task extraction). Your Markdown vaults are perfect for feeding context to Hermes or storing its outputs/skills. Many users run agents *from* Obsidian notes.
- **Skills portability**: As we discussed, Hermes-learned skills (agentskills.io standard) are portable and can be used/shared with Claude Code, Cursor, etc.
- **Self-improving loop**: Hermes will build/refine skills over time, and Docker makes the setup reproducible and isolated.

### Potential Challenges & Mitigations
- **Hardware demands**: Gemma 4 larger models are capable but VRAM-hungry for good speed/context (256K window is a plus). Start with a smaller quantized Gemma 4 via Ollama on a machine with at least 16–32GB RAM + GPU. For heavier use, a $5–15/mo VPS with GPU works well.
- **Setup complexity**: Not one-click, but doable.
  1. Install Docker.
  2. Run Ollama + pull a Gemma 4 model (e.g., `ollama pull gemma4:27b` or similar tag).
  3. Run Hermes via its Docker image or installer, pointing it at your local Ollama endpoint (http://host.docker.internal:11434 or similar).
  4. Configure Hermes terminal backend to Docker for isolation.
  5. Point Obsidian at a shared vault folder (volume-mounted).
- **Performance**: Local inference is slower than cloud. Use smaller models for quick tasks and route complex ones appropriately. Hermes supports model routing.
- **Obsidian limitations**: It's closed-source (as we covered), but data stays local. Use community plugins for AI (e.g., Copilot with local LLMs) or Hermes skills to bridge them.

### Recommended Setup Flow
1. **Docker** as the foundation — Run Hermes and Ollama in containers with volumes for persistence (`~/.hermes`, vaults, etc.).
2. **Ollama** → Gemma 4 as the backend for Hermes.
3. **Hermes** as the orchestrator (sub-agents, skills learning, delegation).
4. **Obsidian** as the knowledge/notes layer — Mount the vault so Hermes can interact with it via skills.

This gives you a powerful, evolving personal agent that writes to and reads from your Obsidian vault, all sandboxed.

### Alternatives/Tweaks to Consider
- If Gemma 4 is too heavy: Try Qwen 3.5, Llama 4, or smaller Gemma variants.
- For easier local serving: vLLM + OpenWebUI alongside Ollama.
- Full isolation: Run everything (including Obsidian access) via Hermes' Docker backend.
- Remote option: Host on a VPS for always-on without draining your laptop.

Overall, **this is a strong stack for what you're describing** — local, private, extensible, and skill-portable. It's popular in the current community for exactly these reasons.

If you want specific commands for the Docker + Ollama + Hermes setup, hardware recommendations for your machine, or how to connect Obsidian skills, just give more details (e.g., your GPU/RAM) and I'll walk you through it step by step!

### HUMAN
No what about using my chat log data from gpt, Gemini, grok, etc to train it on my thoughts, ideas etc and also use the backup Wikipedia file I have as its general knowledge that it can pull from when it’s relevant? I’m already aware of a python library that does exactly that just asking

### ASSISTANT
**Yes — this is an excellent extension to your Docker + Gemma 4 + Hermes + Obsidian stack, and it fits perfectly with Hermes’ design.**

Your Python library (whatever it is — likely something like LlamaIndex, LangChain with custom loaders, or a dedicated personal RAG tool) can be integrated to ingest chat logs (from GPT, Gemini, Grok exports) for personal “thoughts & ideas” memory **and** your Wikipedia backup file for on-demand general knowledge retrieval. Hermes doesn’t do full model fine-tuning natively (and that’s usually overkill here anyway), but its layered memory + skills system makes this straightforward via RAG-style augmentation or direct ingestion into its persistent stores.

### Why This Works So Well
- **Hermes’ memory is built for exactly this kind of personalization**:
  - It has native persistent memory (Markdown files like `MEMORY.md` / `USER.md` + SQLite with full-text search).
  - Cross-session search + LLM summarization so it can recall relevant bits from your past chats without dumping everything into context.
  - Optional vector/RAG layers via bundled skills (e.g., **chroma** for embeddings and semantic search, **qmd** for hybrid retrieval on personal notes/docs, **llm-wiki** for ingesting sources into a maintainable Markdown knowledge base).
  - External memory providers (one active at a time) and skills let you plug in custom vector stores or scripts.

- **Chat logs → your “thoughts & ideas”**:
  - Export them (GPT/Gemini/Grok all have JSON/HTML exports).
  - Your Python lib parses/chunks/embeds them.
  - Then ingest: Either append summarized insights to Hermes’ `USER.md`/`MEMORY.md`, or feed into a Chroma vector index (or LanceDB if you extend it). Hermes’ learning loop will treat this as part of its “model of you” and retrieve contextually.

- **Wikipedia backup file → general knowledge**:
  - If it’s a dump (XML, SQL, or ZIM), your lib can extract/parse relevant chunks.
  - Ingest via the **llm-wiki** skill (builds an interlinked Markdown KB that Hermes queries directly) or the **chroma** skill (semantic vector search).
  - When a task needs facts, Hermes pulls relevant sections automatically via retrieval — exactly the “when relevant” behavior you want. No need to stuff the whole encyclopedia into every prompt.

This keeps **everything 100% local and private** — no data leaves your machine, aligns with self-hosted ethos, and lets Hermes’ self-improving loop refine skills based on *your* history + reliable general knowledge.

### Integration into Your Docker Stack (Practical & Simple)
Use Docker Compose for the whole thing:

1. **Existing containers**:
   - Ollama (Gemma 4 — quantized for your hardware).
   - Hermes (official Docker image, mount `~/.hermes` for skills/memory persistence).

2. **Add your RAG layer**:
   - Run your Python library in its own container (or as a FastAPI service).
   - Mount volumes: chat exports folder + Wikipedia file + vector DB storage (Chroma/LanceDB is lightweight and Docker-friendly).
   - Expose it as a local API or let Hermes call it via subprocess/terminal (Hermes’ Docker backend makes this sandboxed and easy).

3. **Bridge to Hermes**:
   - Create a custom skill (just a `SKILL.md` file) that calls your Python lib: e.g., `ingest_chat_logs`, `query_wikipedia_kb`, or `retrieve_personal_idea`.
   - Or use the built-in **chroma** / **llm-wiki** skills directly — point them at the folders your lib outputs.
   - Obsidian vault stays mounted; you can even have Hermes write retrieval results or summaries back into notes.

4. **One-time setup flow**:
   - Export chats → run your lib to build index.
   - `hermes skills install chroma` (or llm-wiki) and configure paths.
   - Test: Ask Hermes something that should pull from your old Grok chat or a Wikipedia fact — it will retrieve and cite.

### Pros vs. Gotchas
**Pros**:
- Turns Hermes into a *truly personal* agent that knows your ideas without re-explaining.
- Wikipedia becomes fast, offline, and context-aware (way better than raw dump searches).
- Reproducible in Docker, persistent across restarts.
- Skills stay portable (you can even export the new retrieval skill to Claude Code if wanted).

**Gotchas & Mitigations** (realistic on consumer hardware):
- **“Train” vs. RAG**: Full fine-tuning Gemma 4 on chat logs is possible with QLoRA but heavy (VRAM/RAM intensive, risk of forgetting other knowledge). **RAG/ingestion is the practical winner** here — faster, reversible, and what Hermes is optimized for. Your lib probably does RAG already.
- **Scale**: Full Wikipedia dump vectors are huge. Start with a subset (your lib can filter by topics) or use hybrid search (Hermes’ FTS5 + vectors). Kiwix + extraction works great for ZIM files.
- **Performance**: Embeddings/indexing is one-time; queries are fast. Gemma 4 handles retrieval well; use model routing in Hermes for lighter tasks.
- **Initial effort**: ~1-2 hours to wire the skill + ingest. After that, Hermes maintains it.

This stack becomes a **self-contained personal knowledge engine** that grows with you — exactly the local-first power users like. Many in the community do similar personal-data + offline-KB setups with Hermes.

If you share the name of your Python library (or a quick description of what it outputs — e.g., Chroma DB, JSON chunks, etc.), I can give exact skill commands, Docker Compose snippets, or ingestion examples tailored to it. Want the quickstart for the chroma/llm-wiki skills or how to expose your lib as a Hermes tool? Just say the word!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/second-brain-vault|Second Brain Vault]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/tech/homelab|Homelab]]
