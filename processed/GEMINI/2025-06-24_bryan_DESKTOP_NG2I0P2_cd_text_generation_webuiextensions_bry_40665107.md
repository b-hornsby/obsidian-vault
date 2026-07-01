---
category: ai-tools
date: 2025-06-24
id: 587960
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: exploratory
source: GEMINI
summary: The user was exploring the extensions directory of text-generation-webui
  to understand what extensions are available for the local AI text generation setup.
tags:
- text-generation-webui
- extensions
- local-ai
- model-extensions
- ai-tooling
---
# bryan_@DESKTOP-NG2I0P2:~$ cd ~/text-generation-webui/extensions
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$ ls -F
Training_PRO/    example/           long_replies/  perplexity_colors/  silero_tts/    whisper_stt/
character_bias/  gallery/           ngrok/         sd_api_pictures/    superbooga/
coqui_tts/       google_translate/  openai/        send_pictures/      superboogav2/
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$

### USER
bryan_@DESKTOP-NG2I0P2:~$ cd ~/text-generation-webui/extensions
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$ ls -F
Training_PRO/    example/           long_replies/  perplexity_colors/  silero_tts/    whisper_stt/
character_bias/  gallery/           ngrok/         sd_api_pictures/    superbooga/
coqui_tts/       google_translate/  openai/        send_pictures/      superboogav2/
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$

### GEMINI
Excellent! Confirmed. The ls -F output clearly shows superboogav2/ is indeed present in your ~/text-generation-webui/extensions directory. This means the files for the extension are in the correct place. Given this, the issue of the tab not appearing after being checked is almost certainly a UI-related glitch or a persistent caching problem. Let's try the full restart and hard refresh one more time with this confirmed knowledge. Step 11: Final Attempt to Display SuperBooga Tab (Full Restart & Hard Refresh) Action: Go to your WSL2 terminal where Oobabooga might still be running. Stop the server completely. Press Ctrl + C multiple times until you see your command prompt (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Relaunch Oobabooga from the main text-generation-webui directory. Ensure your virtual environment is active. cd ~/text-generation-webui source .venv/bin/activate python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2 (Make sure superboogav2 is explicitly in the --extensions list, as this overrides any config.json settings and forces it to load). Wait for the server to fully start and give you the Running on local URL: http://127.0.0.1:7860 message. Go to your web browser. Even if Oobabooga is open, close that tab completely. Then, open a brand new tab and navigate directly to http://127.0.0.1:7860. This is sometimes more effective than just a hard refresh. Carefully examine all the tabs at the top of the Oobabooga UI. Look very closely for "SuperBooga", "Booga", "RAG", "Knowledge Base", or anything new. It usually appears alongside the standard tabs like "Chat", "Notebook", "Model", etc. If, after all these steps (confirmed extension folder, confirmed uninstallation of flash-attn, full server restart, and fresh browser tab), the "SuperBooga" tab still does not appear, then we might have a deeper, more unusual UI loading issue specific to your Oobabooga installation or browser, or there might be an obscure, unprinted error during the extension's setup() routine. Please let me know the result of this final attempt. If it still doesn't show, we'll need to explore some more advanced troubleshooting for the Oobabooga UI itself.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]