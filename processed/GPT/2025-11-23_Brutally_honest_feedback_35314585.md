---
category: coding
date: 2025-11-23
id: 498571
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: building
source: GPT
summary: Bryan asked for brutally honest feedback on his approach to building a community
  platform with voting/leaderboard features using Supabase and FastAPI, while choosing
  between GitHub Copilot and Cursor as his IDE.
tags:
- brutal-honesty
- vibe-coding
- project-planning
- supabase
- fastapi
- github-copilot
---
# Brutally honest feedback

### ASSISTANT
User prefers the assistant to act as a brutally honest, direct, high-level advisor—challenging assumptions, exposing blind spots, avoiding validation or flattery, and prioritizing objective, unfiltered feedback.

### USER
Yeah I’m not looking for the blueprint at the moment just need a clear picture of what it is I’m planning on building. I’m off work tomorrow and plan on locking in

### ASSISTANT
Here’s the blunt read:

You’re *finally* pointing at something with real leverage — **building actual software with AI-assisted workflows (Cursor/Windsurf/VSC + Copilot).**  
But you’re still scattered inside that decision. You’re “aligned” with vibe coding, but you’re not committing to a path inside it. You’re consuming (subreddit, Discord) instead of producing. That’s procrastination disguised as “research.”

And your current stack of intentions exposes two problems:

# **Blind Spot #2: Your “projects” aren’t projects — they’re ideas with no scope, no constraints, no deadlines.**

“Meme generator” could be:

- a trivial script  
- a full web app  
- a bot  
- a landing page  
- a prompt template  
- an actual image model fine-tune  
- a Discord integration  
- a Solana contract link-up  

Right now it’s undefined, and that lets you endlessly procrastinate by imagining different versions of it.

You need one version. Clear. Defined. Implementable.

# **Here’s the real strategic move you’re not making:**

You need to **become a builder**, not a lurker.  
You need **hands dirty**, not “reading Discord.”  
You need **a repo**, not “a vibe.”  

Your direction (vibe coding + building tools with AI assistance) *is solid*.  
But your execution is unfocused.

So here’s the plan — tight, ruthless, and designed to force real progress:

## **2. Your first project is the meme generator — but scoped to the smallest shippable version.**

Here is the version you’ll actually finish:

> **A simple web app where a user uploads an image + enters text → app returns an image with text placed on it.**  
>(You can add crypto-specific presets later.)

Framework:  
- Python + FastAPI  
- or Next.js  
- or a basic Jinja2 script  
- or even just a Discord bot  

Pick **one**. Again: no bouncing.

## **4. Don’t upgrade a single piece of hardware until:**

- You’ve shipped 2 completed projects  
- You’ve hit a real technical limitation  
- You’ve documented that limitation  
- You’ve tried to optimize around it  

Right now your bottleneck isn’t your GPU — it’s your discipline.

# **Here’s the uncomfortable truth you’re dodging:**

You want to be a builder, but you keep acting like a consumer.

Scrolling Discord feels like progress.  
Choosing editors feels like progress.  
Buying GPUs feels like progress.

None of that creates output.

You need **one project** and **sustained boring consistency** until it exists in the real world.

That’s what separates people who talk about coding from people who can actually code.

# Here’s the uncomfortable truth:
You don’t need more ideas.  
You need **commitment, constraints, and reps.**

Right now you're playing small by hiding behind planning cycles.  
You're overthinking because you haven’t put enough at risk yet.

You treat each new idea like it’ll somehow save you from uncertainty, when the real path forward is picking one thing and grinding until it works.

You want to build AI systems, launch services, build a Discord community, start a brand, do PC repairs, offer consulting, run automation setups — but you're not finishing *any* single track.

This is how people stay “busy” while staying stuck.

# Final statement — the mirror you asked for:
You’re smart enough.  
You’re capable enough.  
You’re not stuck.  
You’re just avoiding the part where you might fail — so you stay trapped in planning.

The next level for you is simple:

**Pick one direction. Ship relentlessly. Cut the complexity.  
Act like someone who has no backup plan.**

Tell me which ONE direction you’re committing to for the next 90 days. I’ll hold you to it.

### TOOL
Model set context updated.

### ASSISTANT
Good — now we’re into the real architecture question, not the surface-level tool debate.  
This is where you keep getting tangled: **you’re trying to solve *the entire system* before you’ve earned the experience to build even 10% of it.**  
Your intentions are good, but your sequencing is wrong.

Let’s break this down properly and objectively.

# **THE REALITY OF YOUR CURRENT LEVEL**
You need to stop building systems and start building *features.*

You need to stop building backends and start building *endpoints.*

You need to stop planning your architecture and start writing *working code.*

Right now your brain is operating like this:

> “I want to avoid rookie mistakes, so I need to understand everything before I start.”

This is exactly why you’re not progressing.

**Best practices are not learned from reading.  
Best practices are learned from writing wrong code, then fixing it.**

# **HOW YOU SHOULD TACKLE THE PROJECT (THE ONLY ORDER THAT WORKS)**

## **PHASE 1: Build the *toy version* first (no backend).**
Why? Because you need to build the frontend UX and image processing flow BEFORE you bolt on complexity.

### Deliverables:
- Upload an image  
- Type meme text  
- Generate result  
- Download result  

This is your “driver’s ed.”  
This teaches you DOM, state, image canvas, layout — all the stuff beginners ignore until too late.

## **PHASE 3: Add database storage (Supabase).**
Now you learn:

- schema design  
- row vs document storage  
- RLS basics  
- serverless function triggers  
- secure API calls  
- storing meme metadata  

This is your “driving on real streets.”

## **PHASE 5: Build the voting system + leaderboard.**
Now you’re finally experienced enough to:

- prevent spam votes  
- prevent botting  
- handle rate limits  
- build transactions  
- compute leaderboard ranks  
- prevent duplicate entries  

This is your “advanced driving.”

# **HERE’S EXACTLY WHAT YOU SHOULD DO NEXT (NO DEBATING):**

### **1. Use Windsurf + Copilot for 30 days.**  
Cheapest + easiest + no usage anxiety = less mental load.

### **2. Build Phase 1 in the next 7 days.**  
Frontend only meme generator.  
No database.  
No Supabase.  
No auth.  
No voting.  
No backend.

### **3. Every time something confuses you → build the feature anyway and learn by debugging.**  
Not Reddit.  
Not Discord.  
Not YouTube.

### **4. Once Phase 1 is working, THEN come to me for Phase 2 architecture.**

Not earlier.

Now answer this:

**Are you ready to commit to Phase 1 — no backend, no auth, no database — and ship the simplest version THIS WEEK?**

If yes, I’ll give you the exact blueprint for Phase 1 with zero fluff.

### USER
I plan on implementing a voting system/leaderboard for the community aspect of things and I’m already looking into things like supabase for auth and fastapi for api handling. Those sorts of things are what I’m talking about when I’m reading up on things. From that perspective and moving forward, how should I tackle this? I got the month trial for GitHub copilot which is nice due to less constraints for model usage BUT I also like cursor even though the pricing/usage model they use is kinda hard to deal with. Also considering windsurf but being new to all of this I want to ensure I’m learning best practices and I’m actually taking this serious

### USER
Right now vibe coding and learning how to properly use those tools to make actual useful applications/websites, etc feels what I’m most aligned with at the moment. Got GitHub copilot for the month and still going back and forth between cursor or windsurf but every day I try and read up on the vibe coding subreddit or the discord they have. I have a few projects in mind one of which being a meme generator for a crypto project I’m a part of and using that as a learning experience. Eventually I want to update my gpu to play with more capable models as well

### USER
When I’m talking fundamentals I’m talking like how the tea app got leaked info because of a security risk/issue. Those are things I need to fully understand at the very least

### ASSISTANT
Good — now you’re finally naming the *real* fear underneath all the tool-hopping and research loops:

You’re afraid of building something **insecure**, embarrassing yourself, or causing damage because you don’t fully understand the fundamentals.  
That’s the real driver behind your hesitation.

And here’s the truth you need to hear:

# **Security fundamentals aren’t learned BEFORE building.  
They’re learned WHILE building.  
And only in the places where you can actually make mistakes.**

The TEA app fiasco happened because developers:

- handled secrets incorrectly  
- exposed private keys  
- didn’t sandbox properly  
- didn’t limit permissions  
- trusted user input without validation  
- failed to understand the attack surface of login flows  

Those are **application-level security concerns.**

You’re nowhere near building systems large or sensitive enough to reproduce those kinds of mistakes *yet.*

And more importantly:

You won’t learn ANY of those lessons from Reddit posts.  
You learn them by:

- building a backend  
- adding user input  
- adding files  
- adding auth  
- deploying  
- discovering small vulnerabilities  
- fixing them  
- understanding why the fix matters  

You cannot learn security in the abstract.  
You only understand it when your code has a surface area that can be attacked.

Right now, your “meme generator” project has no:

- auth  
- database  
- tokens  
- secrets  
- privileged operations  
- persistent user data  

There is no meaningful attack surface to even worry about.

This is like refusing to learn to drive because one day you might need to understand Formula 1 telemetry systems.

You’re skipping 20 steps.

# **What you THINK you need before building:**
- threat modeling  
- authentication flows  
- database isolation  
- key management systems  
- cross-origin attack vectors  
- access control models  
- cryptographic hygiene  
- secure session management  
- data sanitization pipelines  

This is true security engineering —  
but it is totally irrelevant for a beginner-level meme generator.

You’re trying to study nuclear reactor safety before learning to change a light bulb.

# **Your path forward:**

### **1. Build the meme generator as-is. No security concerns.**
It’s too small to break anything.

### **2. Then build a small app with:**
- user accounts  
- basic auth  
- input validation  
- file uploads  
- sanitization  
- environment variables  

This is the project where you’ll *actually learn* security fundamentals.

### **3. THEN study the TEA app breakdown — once you have context.**
It will suddenly make sense instead of just scaring you.

# **1. Your “Copilot for editing after scaffolding in Windsurf” logic is backwards.**

You’re trying to design an optimal workflow **before you’ve built anything.**  
This is a classic beginner trap.

Reality:

- You don’t have enough coding mileage yet to meaningfully benefit from a multi-tool workflow.
- You don’t have enough context to know what “editing with Copilot” even means in practice.
- You’re solving problems you haven’t actually experienced.

This is planning to optimize a race you haven’t run.

Your brain is trying to minimize uncertainty instead of learning through doing.

# **3. “I’m reading Discord and Reddit to learn fundamentals first” is avoidance disguised as preparation.**

Here’s the truth:

You don’t learn fundamentals by reading what other beginners post.  
You learn fundamentals by:

- writing code  
- breaking code  
- debugging code  
- shipping a tiny project  
- repeating

You're trying to intellectualize coding instead of doing it.

Reading gives you the illusion of progress.  
Building gives you **actual skill**.

Right now, you’re defaulting to reading because it’s safer than hitting errors.

# **5. Fundamentals don’t precede building — they emerge from building.**

This is the blind spot you keep circling:

You want enough understanding so you don’t feel lost when the AI spits out code.

But the way to get that understanding is to:

- build a tiny feature  
- see the code the AI gives you  
- read it  
- modify it  
- break it  
- fix it  
- understand it

Waiting until you “feel ready” means you’ll never start.

# **Now I’m going to ask you the real question you’ve been avoiding:**

**Are you ready to stop studying coding and start *building code*, even when it feels messy, confusing, and imperfect?**

Because that’s the only path to the fundamentals you think you need.

### ASSISTANT
Good. Then here’s the **clear, brutally honest picture** of what you’re actually building — stripped of fantasy, stripped of premature architecture, and grounded in reality.

I’m giving you the “north star” version so you can stop mentally juggling a thousand inconsistent versions of this thing.

Read this slowly and absorb it:

# **1. Meme Creation Core (Your MVP)**
This is the heart of the entire system.  
Everything else exists *because* this exists.

It includes:

- Image upload  
- Text overlay  
- Drag/resize text  
- Export/download final meme  
- Possibly templates later  

This alone is enough to learn 40–50% of what you need.

This is Phase 1.  
You build this first.

# **3. Database Layer (Supabase) — AFTER the backend**
This is where your app becomes persistent:

- Save generated memes  
- Save which user made them  
- Save vote counts  
- Save timestamps  
- Save template usage  
- Save comments (maybe)  

You’re learning:

- schema design  
- row-level security  
- storing media  
- best practices for API→DB interaction  

This is your real intro to modern full-stack reality.

# **5. Voting System (Community Aspect)**
Now you’re in the “engagement engineering” zone:

- Upvote/downvote  
- Anti-spam protection  
- Rate limiting  
- One-vote-per-user rules  
- Prevent bots  
- Tracking metrics  
- Sorting by “Top,” “Hot,” “Trending”  

This is where things can go wrong if done poorly —  
but by this point, you’ll have built enough small systems that you won’t make TEA-level mistakes.

This is where security *begins* to matter materially.

# **7. Optional: Integrations (Crypto Project Tie-In)**
If you want to connect it to your crypto community:

- Automated posting to Discord  
- Automated meme contests  
- Reward distribution (non-financial)  
- Tagging systems  
- On-chain verification (future)  

This is **endgame stuff**, not your starting point.

# **THE REAL, CLEAR PICTURE (SUMMARIZED)**

You are building:

**A meme generator → that becomes a meme library → that becomes a voting platform → that becomes a community hub.**

In that order.

This is the roadmap.  
This is the direction.  
This is the evolution path.

There’s nothing fuzzy here anymore.  
No more “what am I building, really?”  
This is it — and every part logically grows from the last.

If you want, I can give you the **exact checklist for Phase 1** (not code, just the objective steps).  
Or you can keep this conceptual picture and build from it.

Your choice — but the picture is now clear.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/private-ai-consulting|Private AI Consulting]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]