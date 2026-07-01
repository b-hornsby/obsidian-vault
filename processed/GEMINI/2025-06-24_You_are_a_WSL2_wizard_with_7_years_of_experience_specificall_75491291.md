---
category: ai-tools
date: 2025-06-24
id: 527204
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/it-certification.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
- private-ai-consulting
- it-certification
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan was seeking comprehensive guidance to build a local offline LLM helpdesk
  AI assistant using WSL2 and oobabooga, with plans to add RAG via text file uploads,
  image generation, and voice conversation to strengthen his resume for tech/help
  desk roles.
tags:
- local-llm
- wsl2
- oobabooga
- helpdesk-ai
- career-strategy
- superbooga
---
# You are a WSL2 wizard with 7+ years of experience, specifically specializing in localized LLM models and maximizing the specs used for maximum performance. These are the given specs here:

( Cpu: Intel Core i7-12700K
Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40
Storage: 970 Evo Plus M.2 SSD 2TB
Graphics card: PNY GeForce RTX™ 3070 8GB XLR80)

I currently have a certificate from Tiffin University from going through the IMAP program they are a part of (CompTIA A+ and Network+ course) so I figure it coming from an actual university might give me that edge I need, even if I don't have the certs in hand just yet (currently studying for them). Working on a big resume building project that allows me to run LLM locally and completely offline as a personal little Helpdesk AI assistant, that I believe might give me the edge I need to wiggle my way into a tech/help desk role in the meantime but I'm currently stuck in the middle of that project. For context, I have the  Nous-Hermes-2 Mistral 7B model running within the terminal of WSL2 and finally got things working within oobabooga but I know in order to make this stand out, I need the model to be a super expert to REALLLY be as useful as possible in this use case. 

I wanted to explore the concept of uploading .txt files over in oobabooga but I was having trouble getting the whole extension thing set up so I was wondering if there's a way to set up some sort of function that allows the model to look things up in that regard before rather than doing it manually like that and giving an answer if that makes sense? I know at some point image generation and actual voice conversation are features I would also like to add to really flesh this out if thats even possible? 

to best assist me in resolving this issue and getting everything to run seamlessly given everything I've told you, can you run me through what I need to do in order to get that done? I don't need you to assume anything when explaining, so be sure to be thorough in your instruction, explaining as beginner friendly as possible (like you're explaining to someone's grandparents if need-be) and be sure to explain each step in its entirety for maximum understanding to a complete novice such as myself. be sure to wait for me to paste any errors along the way before going on to next steps also please.

Knowing all of this, starting from the begininng, making sure things are where they are supposed to be (have me check this first before going on to explain everything), how would I go about this? 

### USER
You are a WSL2 wizard with 7+ years of experience, specifically specializing in localized LLM models and maximizing the specs used for maximum performance. These are the given specs here:

( Cpu: Intel Core i7-12700K
Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40
Storage: 970 Evo Plus M.2 SSD 2TB
Graphics card: PNY GeForce RTX™ 3070 8GB XLR80)

I currently have a certificate from Tiffin University from going through the IMAP program they are a part of (CompTIA A+ and Network+ course) so I figure it coming from an actual university might give me that edge I need, even if I don't have the certs in hand just yet (currently studying for them). Working on a big resume building project that allows me to run LLM locally and completely offline as a personal little Helpdesk AI assistant, that I believe might give me the edge I need to wiggle my way into a tech/help desk role in the meantime but I'm currently stuck in the middle of that project. For context, I have the  Nous-Hermes-2 Mistral 7B model running within the terminal of WSL2 and finally got things working within oobabooga but I know in order to make this stand out, I need the model to be a super expert to REALLLY be as useful as possible in this use case. 

I wanted to explore the concept of uploading .txt files over in oobabooga but I was having trouble getting the whole extension thing set up so I was wondering if there's a way to set up some sort of function that allows the model to look things up in that regard before rather than doing it manually like that and giving an answer if that makes sense? I know at some point image generation and actual voice conversation are features I would also like to add to really flesh this out if thats even possible? 

to best assist me in resolving this issue and getting everything to run seamlessly given everything I've told you, can you run me through what I need to do in order to get that done? I don't need you to assume anything when explaining, so be sure to be thorough in your instruction, explaining as beginner friendly as possible (like you're explaining to someone's grandparents if need-be) and be sure to explain each step in its entirety for maximum understanding to a complete novice such as myself. be sure to wait for me to paste any errors along the way before going on to next steps also please.

Knowing all of this, starting from the begininng, making sure things are where they are supposed to be (have me check this first before going on to explain everything), how would I go about this? 

### GEMINI
Okay, this sounds like a fantastic project for your resume and a great way to showcase your skills! Building a local, offline Helpdesk AI assistant with LLMs is a cutting-edge application of technology, and your enthusiasm for maximizing performance and adding advanced features is exactly what employers look for. Given your current setup and goals, we're going to focus on getting your Nous-Hermes-2 Mistral 7B model to use external knowledge (your .txt files) effectively within Oobabooga, and then we can look at the future steps for image generation and voice. Let's start by making sure everything is in its right place and that we're on the same page regarding your current Oobabooga setup. Step 1: Verify your Oobabooga Text Generation WebUI Installation and Model Location Before we dive into extensions or advanced features, it's crucial to confirm that your Oobabooga Text Generation WebUI is installed correctly and that your Nous-Hermes-2 Mistral 7B model is in the expected location. This will help us troubleshoot any potential issues down the line. Action: Please open your WSL2 terminal and navigate to the directory where you installed Oobabooga's Text Generation WebUI. Typically, this would be something like ~/text-generation-webui or a similar path you chose during installation. Once you are in the text-generation-webui directory, please run the following command and paste the output here: ls -F This command will list all the files and directories in your Oobabooga installation folder. I'm looking to confirm the presence of key files and folders like start_wsl.bat, run_wsl.sh, modules/, models/, extensions/, etc. After that, please navigate into your models directory: cd models And then run ls -F again to show the contents of your models folder. I want to see the exact name and structure of your Nous-Hermes-2 Mistral 7B model directory. For example, it might be Nous-Hermes-2-Mistral-7B/ or TheBloke_Nous-Hermes-2-Mistral-7B-GGUF/ depending on how you downloaded it. ls -F Please provide the output of both ls -F commands. This will give me a clear picture of your current setup, and we can proceed from there.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/it-certification|IT Certification]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
