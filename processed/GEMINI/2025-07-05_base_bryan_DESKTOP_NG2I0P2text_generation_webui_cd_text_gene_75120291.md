---
id: 779908
source: GEMINI
date: 2025-07-05
tags: ['ai-tools', 'ai', 'gemini', 'grok', 'model', 'oobabooga', 'rag', 'openai']
category: ai-tools
sentiment: building
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cd ~/text-generation-webui/extensions
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$ ls -l
total 64
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 Training_PRO
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 character_bias
drwxr-xr-x 3 bryan_ bryan_ 4096 Jun 25 12:32 coqui_tts
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 example
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 gallery
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 google_translate
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 long_replies
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 ngrok
drwxr-xr-x 3 bryan_ bryan_ 4096 Jul  2 18:50 openai
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 perplexity_colors
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 sd_api_pictures
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 send_pictures
drwxr-xr-x 3 bryan_ bryan_ 4096 Jun 25 12:32 silero_tts
drwxr-xr-x 3 bryan_ bryan_ 4096 Jun 25 13:15 superbooga
drwxr-xr-x 5 bryan_ bryan_ 4096 Jun 25 13:15 superboogav2
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 whisper_stt
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$

### USER
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cd ~/text-generation-webui/extensions
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$ ls -l
total 64
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 Training_PRO
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 character_bias
drwxr-xr-x 3 bryan_ bryan_ 4096 Jun 25 12:32 coqui_tts
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 example
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 gallery
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 google_translate
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 long_replies
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 ngrok
drwxr-xr-x 3 bryan_ bryan_ 4096 Jul  2 18:50 openai
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 perplexity_colors
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 sd_api_pictures
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 send_pictures
drwxr-xr-x 3 bryan_ bryan_ 4096 Jun 25 12:32 silero_tts
drwxr-xr-x 3 bryan_ bryan_ 4096 Jun 25 13:15 superbooga
drwxr-xr-x 5 bryan_ bryan_ 4096 Jun 25 13:15 superboogav2
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 25 12:32 whisper_stt
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$

### GEMINI
Okay, the ls -l output for your extensions directory does not show a web_rag folder. This means the web_rag extension is not included by default in your current Oobabooga installation. To add web RAG capabilities, we'll need to manually obtain this extension and install its dependencies. Step 1: Clone the web_rag Extension We'll use git clone to get the web_rag extension from its GitHub repository. Ensure you are in your Oobabooga extensions directory: cd ~/text-generation-webui/extensions Your prompt should be (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$. Clone the web_rag repository: git clone https://github.com/Anglebrackets/web_rag This command will create a new directory named web_rag within your extensions folder and download all the necessary files for the extension. Step 2: Install web_rag Extension Dependencies Now that the web_rag folder exists, we need to install its required Python packages. Go back to the Oobabooga root directory: cd ~/text-generation-webui Your prompt should be (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Install web_rag dependencies: ./installer_files/env/bin/pip install -r extensions/web_rag/requirements.txt Allow this command to complete fully. It will download and install any necessary Python packages. This might take a few moments. Step 3: Restart Oobabooga To ensure the new extension is recognized and loaded, you need to restart the Oobabooga server. ./installer_files/env/bin/python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf Wait for Oobabooga to fully load the model and display its URL (http://127.0.0.1:7860). Step 4: Enable and Configure web_rag in the Web UI Open your web browser and go to http://127.0.0.1:7860. Navigate to the "Extensions" tab. Locate "web_rag" in the list and check its box to enable it. Click the "Save settings" button. You will likely be prompted to restart the server by the UI. Click the button to restart it again. After this restart, a new "Web RAG" tab (or similar) should appear in your Oobabooga UI. You will then need to explore this new tab to configure how it fetches and uses web content for RAG. It will likely have options to input URLs or specify a method for automated web searching. Please let me know the output of each command as you execute them!