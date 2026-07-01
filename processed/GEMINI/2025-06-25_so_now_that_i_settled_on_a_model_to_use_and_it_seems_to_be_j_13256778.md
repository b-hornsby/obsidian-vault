---
id: 556575
source: GEMINI
date: 2025-06-25
tags: ['oobabooga', 'model-setup', 'Nous-Hermes-2', 'Mistral-7B', 'model-configuration']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan had chosen a model (Nous-Hermes-2-Mistral-7B) and was asking how to download and configure it within oobabooga.
---
# so now that i settled on a model to use and it seems to be just what i need for this use case, how do i go about getting it and getting things set up in oobabooga? 

### USER
so now that i settled on a model to use and it seems to be just what i need for this use case, how do i go about getting it and getting things set up in oobabooga? 

### GEMINI
Excellent! Now that you have Oobabooga's text-generation-webui up and running, getting your chosen model, Nous-Hermes-2 Mistral 7B, and setting it up is quite straightforward. Here's a step-by-step guide: Step 1: Start Oobabooga's Text Generation Web UI First, ensure your Oobabooga web UI is running. If you closed the terminal window where you ran ./start_linux.sh, or if it's not currently active, you need to restart it. Open your WSL2 terminal. Navigate to the text-generation-webui directory: cd ~/text-generation-webui Start the web UI: ./start_linux.sh (Or python server.py --chat --listen --xformers if you prefer to bypass the full start_linux.sh script once the environment is set up. The script just ensures everything is up-to-date and then calls server.py.) Wait for the terminal to show the "Running on local URL" message, typically: Running on local URL: http://127.0.0.1:7860 Open this URL in your Windows web browser. Step 2: Find the GGUF Model on Hugging Face You need the exact repository ID for the GGUF version of Nous-Hermes-2 Mistral 7B. The most reliable source for GGUF quantizations of popular models is often "TheBloke" on Hugging Face. Go to Hugging Face: https://huggingface.co/ In the search bar, type: TheBloke/Nous-Hermes-2-Mistral-7B-DPO-GGUF (The DPO version is generally preferred for its better alignment.) Click on the model card. Look for the "Files and versions" tab. Click it. Identify the GGUF file you want. For a 7B model, Q4_K_M.gguf or Q5_K_M.gguf are typically excellent choices, offering a good balance between quality and VRAM usage. Q4_K_M.gguf: Good balance, smaller file size, faster inference. Q5_K_M.gguf: Slightly better quality, slightly larger file and more VRAM needed. Avoid Q8_0 unless you have ample VRAM and want the absolute best quality for a 7B (it's often overkill for the quality gain vs. resource usage). Example: Let's assume you choose nous-hermes-2-mistral-7b-dpo.Q4_K_M.gguf. The full repository ID you need to copy is: TheBloke/Nous-Hermes-2-Mistral-7B-DPO-GGUF (You do not need to copy the specific filename, just the repository ID.) Step 3: Download the Model in Oobabooga Now, back in the Oobabooga web UI: Navigate to the "Model" tab. (It's usually the second tab from the left). Scroll down to the section labeled "Download custom model or LoRA". Paste the full repository ID you copied from Hugging Face (e.g., TheBloke/Nous-Hermes-2-Mistral-7B-DPO-GGUF) into the text box. Self-correction: Make sure there are no leading/trailing spaces. Note: The UI might automatically suggest paths as you type. Click the "Download" button. Monitor your WSL2 terminal: You will see the download progress appearing in your terminal where Oobabooga is running. It will show the percentage and download speed. This file will be several gigabytes, so it will take some time depending on your internet connection. Once finished, the terminal will indicate completion. Step 4: Load the Model After the download is complete in the terminal: In the Oobabooga web UI, on the "Model" tab, click the 🔄 (refresh) button located next to the "Model" dropdown menu at the top of the tab. This will refresh the list of available models. From the "Model" dropdown menu, select TheBloke_Nous-Hermes-2-Mistral-7B-DPO-GGUF (it will list the repository name). Click the large green "Load" button below the dropdown. Monitor your WSL2 terminal again: You'll see messages indicating that the model is being loaded, how many layers are offloaded to the GPU, etc. Wait for the terminal to confirm that the model is fully loaded. This might take a minute or two. Step 5: Interact with Your Personal Helpdesk AI Once the model is loaded: Navigate to the "Chat" tab (typically the first tab). You should now see a chat interface. Type your first helpdesk-related question or scenario into the input box at the bottom. Press Enter or click "Generate". The AI should process your request and generate a response. You've successfully brought your personal helpdesk AI to life! Remember, for truly personalized helpdesk answers based on your unique documents, you'll eventually want to look into Retrieval Augmented Generation (RAG) as we discussed, which would be a separate layer of development beyond Oobabooga's direct functionality. But for now, enjoy interacting with a powerful base model!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
