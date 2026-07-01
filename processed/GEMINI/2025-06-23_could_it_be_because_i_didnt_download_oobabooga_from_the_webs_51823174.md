---
category: ai-tools
date: 2025-06-23
id: 980273
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
- homelab-stack
- private-ai-consulting
- second-brain-vault
- streaming-rig
- it-certification
- flappy-meme-bird
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user is troubleshooting an issue with Oobabooga installation and questioning
  whether the problem stems from not downloading it directly from the official website,
  indicating they are stuck on setup or configuration of a local AI tool.
tags:
- Oobabooga
- installation
- AI tools
- local AI
- troubleshooting
---
# could it be because i didn't download oobabooga from the website itself? 

### USER
could it be because i didn't download oobabooga from the website itself? 

### GEMINI
No, Bryan, it's highly unlikely that's the reason. In fact, if you've been using git pull as we have, you are getting Oobabooga directly from its primary "website" or source, which is its GitHub repository. When you first set up Oobabooga, you typically use git clone to download the entire project from https://github.com/oobabooga/text-generation-webui. Then, git pull (which we just ran successfully) is the command you use to update that cloned project to the very latest code directly from GitHub. So, your method of acquiring and updating Oobabooga is the correct and most up-to-date way to get the software. The issue isn't how you downloaded it. The problem seems to be a peculiar display anomaly in your Oobabooga web UI where the dedicated RAG extensions simply aren't showing up in the "Available extensions" list, even though your code is current (commit 17f9c188) and those extensions are present in recent Oobabooga versions. Given that we've updated your code and dependencies, and still can't see the RAG extension, the most reliable next step to ensure you have full access to all extensions (including RAG) is to perform a clean re-installation of Oobabooga. This helps clear any potential old configuration files or unexpected states that might be preventing the extensions from appearing correctly. Are you ready to try a clean re-installation? It's a bit more involved as it means starting fresh with the Oobabooga program files, but we'll make sure your models and data are safe.