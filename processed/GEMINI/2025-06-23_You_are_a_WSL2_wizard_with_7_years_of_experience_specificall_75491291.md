---
category: career
date: 2025-06-23
id: 071875
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/it-certification.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan was seeking expert guidance to build a local offline Helpdesk AI assistant
  using his WSL2 setup and RTX 3070 for career advancement.
tags:
- wsl2-optimization
- local-llm
- helpdesk-ai
- resume-project
---
# You are a WSL2 wizard with 7+ years of experience, specifically specializing in localized LLM models and maximizing the specs used for maximum performance. These are the given specs here:

( Cpu: Intel Core i7-12700K
Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40
Storage: 970 Evo Plus M.2 SSD 2TB
Graphics card: PNY GeForce RTX™ 3070 8GB XLR80)

I currently have a certificate from Tiffin University from going through the IMAP program they are a part of (CompTIA A+ and Network+ course) so I figure it coming from an actual university might give me that edge I need, even if I don't have the certs in hand just yet (currently studying for them). Working on a big resume building project that allows me to run LLM locally and completely offline as a personal little Helpdesk AI assistant, that I believe might give me the edge I need to wiggle my way into a tech/help desk role in the meantime but I'm currently stuck in the middle of that project. For context, I have the  Nous-Hermes-2 Mistral 7B model running within the terminal of WSL2 but when I try to get oobabooga working, (I plan to add image generation at some point just as an added feature) it doesn't pick up the model that I know works because it works in the terminal in WSL2.  

to best assist me in resolving this issue and getting everything to run seamlessly given everything I've told you, can you run me through what I need to do in order to get that done? I don't need you to assume anything when explaining, so be sure to be thorough in your instruction, explaining as beginner friendly as possible and be sure to explain each step in its entirety for maximum understanding to a complete normie such as myself. be sure to wait for me to paste any errors along the way before going on to next steps also please.

Knowing all of this, starting from the begininng, making sure things are where they are supposed to be (have me check this first before going on to explain everything), how would I go about this? 

### USER
You are a WSL2 wizard with 7+ years of experience, specifically specializing in localized LLM models and maximizing the specs used for maximum performance. These are the given specs here:

( Cpu: Intel Core i7-12700K
Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40
Storage: 970 Evo Plus M.2 SSD 2TB
Graphics card: PNY GeForce RTX™ 3070 8GB XLR80)

I currently have a certificate from Tiffin University from going through the IMAP program they are a part of (CompTIA A+ and Network+ course) so I figure it coming from an actual university might give me that edge I need, even if I don't have the certs in hand just yet (currently studying for them). Working on a big resume building project that allows me to run LLM locally and completely offline as a personal little Helpdesk AI assistant, that I believe might give me the edge I need to wiggle my way into a tech/help desk role in the meantime but I'm currently stuck in the middle of that project. For context, I have the  Nous-Hermes-2 Mistral 7B model running within the terminal of WSL2 but when I try to get oobabooga working, (I plan to add image generation at some point just as an added feature) it doesn't pick up the model that I know works because it works in the terminal in WSL2.  

to best assist me in resolving this issue and getting everything to run seamlessly given everything I've told you, can you run me through what I need to do in order to get that done? I don't need you to assume anything when explaining, so be sure to be thorough in your instruction, explaining as beginner friendly as possible and be sure to explain each step in its entirety for maximum understanding to a complete normie such as myself. be sure to wait for me to paste any errors along the way before going on to next steps also please.

Knowing all of this, starting from the begininng, making sure things are where they are supposed to be (have me check this first before going on to explain everything), how would I go about this? 

### GEMINI
Alright, my friend! You've got some solid hardware to work with, and the ambition to build a local LLM helpdesk assistant is a fantastic resume builder. Your Tiffin University experience, even without the certs in hand, shows initiative, and that's exactly what employers look for. Let's get you unstuck and get that Nous-Hermes-2 Mistral 7B model purring in oobabooga. We're going to approach this systematically, making sure every step is clear and understandable, even if you feel like a "complete normie." No assumptions here, just clear instructions. Before we dive into troubleshooting oobabooga, let's make sure your WSL2 environment is set up optimally and that you know where your model files are. Step 1: Verify WSL2 Distribution and Model Location First things first, we need to confirm which WSL2 distribution you're using and, more importantly, where your Nous-Hermes-2 Mistral 7B model is located within that distribution. This is crucial for oobabooga to find it. Action: Open PowerShell (or Command Prompt) in Windows, and let's check your WSL2 distributions. Command to run in PowerShell: wsl -l -v What I need you to do: Run the command above in PowerShell. Copy and paste the entire output here. This will show me your WSL2 distributions and their states. Once I have that, we'll proceed to the next step of verifying your model's location. Don't move on until I've seen the output from wsl -l -v.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/it-certification|IT Certification]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
