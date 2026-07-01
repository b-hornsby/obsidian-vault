---
id: 060392
source: GEMINI
date: 2025-12-09
tags: ['ollama', 'windows-11', 'uninstall', 'clean-slate', 'local-llm']
category: homelab
sentiment: frustrated
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan wanted to completely remove Ollama from Windows 11 to start fresh.
---
# how do i 100% get rid of ollama on windows 11 so i can have a fresh slate?

### USER
how do i 100% get rid of ollama on windows 11 so i can have a fresh slate?

### GEMINI
To 100% remove Ollama from Windows 11 and ensure a completely fresh slate, you must go beyond the standard uninstaller. The standard uninstall removes the app but leaves behind your downloaded models and configuration files, which can take up gigabytes of space and retain old settings. Here is the brutal, step-by-step protocol to remove everything. Phase 1: Kill the Process Files cannot be deleted if they are in use. Check your System Tray (bottom right corner, near the clock). If you see the Ollama icon (a little llama), right-click it and select Quit. Open Task Manager (Ctrl + Shift + Esc). Search for "Ollama". If any processes remain, right-click them and select End Task. Phase 2: Standard Uninstall Press Win + I to open Settings. Go to Apps > Installed apps. Search for Ollama. Click the three dots ... on the right and select Uninstall. Phase 3: The "Deep Clean" (Crucial) This is the step most people miss. Ollama stores your models (often 10GB+) and config files in a hidden folder that the uninstaller does not touch. Press Win + R to open the Run dialog. Type %UserProfile% and hit Enter. Look for a folder named .ollama. Note: If you don't see it, select View > Show > Hidden items in the File Explorer ribbon. Delete the entire .ollama folder. This deletes all downloaded models (Llama 3, Mistral, etc.) and your history/configuration. Open Win + R again. Type %LOCALAPPDATA% and hit Enter. Look for an Ollama folder (usually contains logs like server.log). Delete it. Phase 4: Wipe Environment Variables If you ever tweaked Ollama to store models on a different drive or listen on a specific port, these variables will persist and mess up a future installation. Press Win key and type "env". Select "Edit environment variables for your account". In the top section ("User variables"), look for any of the following: OLLAMA_MODELS OLLAMA_HOST OLLAMA_ORIGINS OLLAMA_KEEP_ALIVE Select them and click Delete. Click OK. Phase 5: Check WSL & Docker (If applicable) If you are a developer or "power user," you might have installed it inside a subsystem. If you only used the Windows installer, skip this. WSL (Linux Subsystem): Open your Ubuntu/Linux terminal and run: sudo rm -rf /usr/share/ollama and rm -rf ~/.ollama Docker: If you ran it via Docker, run: docker rm -f ollama and docker rmi ollama/ollama Verification To confirm it is 100% gone: Open PowerShell or Command Prompt. Type ollama. You should receive an error saying: "'ollama' is not recognized as an internal or external command..." You now have a clean slate.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
