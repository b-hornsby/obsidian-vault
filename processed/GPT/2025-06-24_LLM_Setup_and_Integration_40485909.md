---
id: 948132
source: GPT
date: 2025-06-24
tags: ['wsl2', 'oobabooga', 'cuda', 'gpu-optimization', 'rag', 'voice-conversation']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was seeking comprehensive guidance to optimize his WSL2+Oobabooga setup with RAG, file upload, and voice features.
---
# LLM Setup and Integration

### TOOL
Model set context updated.

### ASSISTANT
Awesome — you’ve made it really far already, and this setup **is very much resume-worthy**, especially if you can polish it with things like .txt knowledge injection, future image generation, and voice support. We'll make it airtight, step by step. Here's how we'll break it down — **but first we double-check your current setup to avoid breaking anything**.

### ✅ GOAL:
Enable `.txt` file lookup/search within your local model (running in oobabooga via WSL2), setting the groundwork for image generation and voice later.

### 🔎 PART A — Your Environment

1. **You can launch WSL2 and get into Ubuntu.**
   - ✅ Example: You open “Ubuntu” from Start menu or type `wsl` in PowerShell and land in your Linux shell.

2. **You know how to activate oobabooga and run the model.**
   - ✅ You can run something like:  
     ```bash
     python3 server.py --model [path-to-your-model]
     ```
     or however you're running it.

3. **You can access oobabooga’s web UI from your browser.**
   - ✅ You open `http://localhost:7860` or similar and see the web UI.

Please reply by confirming:
✅ = Yes, ❌ = No  
You can just copy this:

```
✅ Can open WSL2 (Ubuntu)
✅ Can run oobabooga and load model
✅ Can access localhost UI
✅/❌ Have main oobabooga folder (name: ____)
✅/❌ Have extensions folder inside it
✅/❌ Have a folder for .txt files already
```

Once I have that, I’ll give you **STEP 1: Installing the Text Loader + Search Tool**, and from there we’ll get you fully set up to load `.txt` files and have your AI assistant use them for offline helpdesk tasks.

### TOOL
Model set context updated.

### ASSISTANT
User has Nous-Hermes-2 Mistral 7B running locally inside WSL2 using oobabooga for their self-hosted AI Helpdesk Assistant project. They want to enable .txt file lookup, image generation, and voice input/output features.

### ASSISTANT
User has Nous-Hermes-2 Mistral 7B running locally in WSL2 using oobabooga for a personal Helpdesk AI project. They want to add .txt file lookup capabilities, image generation, and voice input/output in the future. They are using this project to build their resume and aim for a tech/help desk role.

### USER
You are a WSL2 wizard with 7+ years of experience, specifically specializing in localized LLM models and maximizing the specs used for maximum performance. These are the given specs here:

( Cpu: Intel Core i7-12700K
Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40
Storage: 970 Evo Plus M.2 SSD 2TB
Graphics card: PNY GeForce RTX™ 3070 8GB XLR80)

I currently have a certificate from Tiffin University from going through the IMAP program they are a part of (CompTIA A+ and Network+ course) so I figure it coming from an actual university might give me that edge I need, even if I don't have the certs in hand just yet (currently studying for them). Working on a big resume building project that allows me to run LLM locally and completely offline as a personal little Helpdesk AI assistant, that I believe might give me the edge I need to wiggle my way into a tech/help desk role in the meantime but I'm currently stuck in the middle of that project. For context, I have the  Nous-Hermes-2 Mistral 7B model running within the terminal of WSL2 and finally got things working within oobabooga but I know in order to make this stand out, I need the model to be a super expert to REALLLY be as useful as possible in this use case. 

I wanted to explore the concept of uploading .txt files over in oobabooga but I was having trouble getting the whole extension thing set up so I was wondering if there's a way to set up some sort of function that allows the model to look things up in that regard before rather than doing it manually like that and giving an answer if that makes sense? I know at some point image generation and actual voice conversation are features I would also like to add to really flesh this out if thats even possible? 

to best assist me in resolving this issue and getting everything to run seamlessly given everything I've told you, can you run me through what I need to do in order to get that done? I don't need you to assume anything when explaining, so be sure to be thorough in your instruction, explaining as beginner friendly as possible (like you're explaining to someone's grandparents if need-be) and be sure to explain each step in its entirety for maximum understanding to a complete novice such as myself. be sure to wait for me to paste any errors along the way before going on to next steps also please.

Knowing all of this, starting from the begininng, making sure things are where they are supposed to be (have me check this first before going on to explain everything), how would I go about this?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/it-certification|IT Certification]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]