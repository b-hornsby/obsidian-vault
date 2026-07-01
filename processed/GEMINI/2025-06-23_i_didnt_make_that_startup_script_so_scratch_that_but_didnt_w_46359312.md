---
category: homelab
date: 2025-06-23
id: 704661
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user is trying to update or add an extension to their working Oobabooga
  setup via git pull without breaking their current configuration, but the expected
  extension isn't appearing after the attempt.
tags:
- oobabooga
- git-pull
- extension-management
- local-ai
- startup-scripts
---
# i didn't make that startup script so scratch that, but didn't we try the git pull command? we have oobabooga working right now so i dont wanna erase anything or mess it up but the extension you're talking about isn't showing up 

### USER
i didn't make that startup script so scratch that, but didn't we try the git pull command? we have oobabooga working right now so i dont wanna erase anything or mess it up but the extension you're talking about isn't showing up 

### GEMINI
You're right to be cautious, Bryan! It's good to double-check before making changes. First, no, we have not tried the git pull command yet. I just recommended it as the next step because the specific RAG extension isn't showing up in your current list. Second, your concern about messing things up or erasing data is very understandable. Let me reassure you: git pull will NOT erase your models, character settings, or your data_sources folder. git pull only updates the core code files of the text-generation-webui itself. It brings down the latest changes and features from the official Oobabooga project. Your user_data folder (where your models are) and your data_sources folder (with your .txt files) are separate from the core code and will not be touched by git pull. pip install -r requirements.txt --upgrade only updates the Python libraries that Oobabooga uses. It doesn't affect your user data. This process (git pull followed by pip install) is the standard and safe way to update Oobabooga to get new features and extensions without losing your work. The reason the RAG extension isn't showing up is likely because it was added in a version newer than what you currently have installed. Let's Safely Update Your Oobabooga (Manual Steps) To get access to those RAG extensions, we need to perform this update. Here are the steps, relying on the manual commands since you don't have the startup script: Go to your Ubuntu WSL2 terminal where Oobabooga is currently running. Stop the Oobabooga server: Press Ctrl + C on your keyboard repeatedly (you might need to press it a few times quickly). You'll know it's stopped when you see your command prompt return, looking something like: (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ Ensure you are in the correct directory: Type the following command and press Enter: cd ~/text-generation-webui (You should already be there, but it's good practice to confirm). Pull the latest code changes: This command updates the Oobabooga application files. git pull Press Enter. You'll see messages indicating files being updated. Update Python dependencies: This command updates or installs any necessary Python libraries for the new code. pip install -r requirements.txt --upgrade Press Enter. This might take a few minutes as it downloads and installs libraries. Restart Oobabooga: Once the pip install command finishes and you see your prompt return, start Oobabooga again with your usual manual command: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp Press Enter. Wait for the UI to load in your browser. After Oobabooga has fully restarted, go back to the "Settings" tab in your browser and look at the "Available extensions" list again. You should now see more options, and hopefully a clear RAG-related extension to enable.