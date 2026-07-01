---
id: 182543
source: GEMINI
date: 2025-06-25
tags: ['oobabooga', 'text-generation-webui', 'local-llm-ui', 'server-running']
category: ai-tools
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan confirmed that the text-generation-webui (oobabooga) server started successfully and is accessible at http://127.0.0.1:7860.
---
# okay so it went and did its thing and now we here:   http://127.0.0.1:7860 

### USER
okay so it went and did its thing and now we here:   http://127.0.0.1:7860 

### GEMINI
That's fantastic news! When your terminal displayed http://127.0.0.1:7860, it means Oobabooga's text-generation-webui has successfully started and is now running! What you need to do now: Open your web browser on your Windows machine. Go to the address: http://127.0.0.1:7860 You should now see the Oobabooga text-generation-webui interface. This is where you can download models, load them, and start interacting with them. Next Steps within the Oobabooga UI: Go to the "Model" tab: This is usually the first place you'll go. Download a model: You'll see a section like "Download custom model or LoRA". Recommendation: Start with a smaller, well-regarded GGUF model to test. Search Hugging Face for GGUF models. A good starting point might be a 7B parameter model, like: TheBloke/Llama-2-7B-Chat-GGUF (look for the .Q4_K_M.gguf file for a good balance of size and quality) mistralai/Mistral-7B-v0.1 (and then search for GGUF quantizations from "TheBloke" or similar repos, e.g., TheBloke/Mistral-7B-v0.1-GGUF) Copy the full model repository ID (e.g., TheBloke/Llama-2-7B-Chat-GGUF) and paste it into the "Download custom model or LoRA" box. Click "Download". You'll see the download progress in your WSL2 terminal where Oobabooga is running. Load the model: Once the download is complete, click the "refresh" button next to the "Model" dropdown menu on the Oobabooga "Model" tab. Select the downloaded model from the dropdown. Click the "Load" button. Wait for the terminal to confirm the model has loaded. Go to the "Chat" or "Text Generation" tab: Once loaded, you can switch to these tabs to start interacting with the model! You've successfully set up a local LLM inference environment with GPU acceleration in WSL2! This is a major accomplishment. Enjoy exploring the world of local LLMs!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
