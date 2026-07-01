---
category: ai-tools
date: 2025-06-24
id: 020238
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
- homelab-stack
- private-ai-consulting
- second-brain-vault
- streaming-rig
resolution: partial
sentiment: exploratory
source: GEMINI
summary: The user is navigating the text-generation-webui directory structure, exploring
  available extensions and model paths, likely setting up or managing their local
  AI environment.
tags:
- text-generation-webui
- extensions
- local-ai
- model-management
- directory-navigation
---
# bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/user_data/models$ cd ~/text-generation-webui
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cd extensions
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$ ls -F
Training_PRO/    example/           long_replies/  perplexity_colors/  silero_tts/    whisper_stt/
character_bias/  gallery/           ngrok/         sd_api_pictures/    superbooga/
coqui_tts/       google_translate/  openai/        send_pictures/      superboogav2/
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$

### USER
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/user_data/models$ cd ~/text-generation-webui
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cd extensions
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$ ls -F
Training_PRO/    example/           long_replies/  perplexity_colors/  silero_tts/    whisper_stt/
character_bias/  gallery/           ngrok/         sd_api_pictures/    superbooga/
coqui_tts/       google_translate/  openai/        send_pictures/      superboogav2/
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$

### GEMINI
Excellent! This is great news. I see superbooga/ and even superboogav2/ listed. This means the extension files are already present in your Oobabooga installation. This saves us a step! The superbooga extension is exactly what you need for uploading .txt files and having the model use them for lookups. Since you have both superbooga and superboogav2, we'll go with superboogav2 as it's the newer version and likely has improvements. Now, let's get it activated and ready to use. Step 4b: Install superboogav2 requirements and enable it in Oobabooga. Even though the files are there, extensions often have their own Python dependencies (like libraries needed to process text, create embeddings, etc.) that need to be installed. After that, we'll enable the extension through the Oobabooga web interface. Action: Stop Oobabooga (if it's still running). You'll need to stop the server in your WSL2 terminal to install the extension's dependencies. Go to the WSL2 terminal where Oobabooga is running and press Ctrl + C (Control + C) a couple of times. You might see a message like Shutdowning server.... Wait until you see your prompt (bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$) again. Navigate to the superboogav2 directory: cd ~/text-generation-webui/extensions/superboogav2 Install the extension's dependencies. The superboogav2 extension usually has a requirements.txt file that lists its necessary Python libraries. We need to install these using pip. pip install -r requirements.txt This command tells pip (your Python package installer, which should be active in your .venv from your start command) to install all the packages listed in requirements.txt. This might take a few minutes as it downloads and installs various libraries. Important: If you encounter any errors during this pip install step, please paste them here. We need to make sure all dependencies are met. Once that command completes successfully (or if you encounter an error, paste it here), we'll move on to restarting Oobabooga and enabling the extension in the UI.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]