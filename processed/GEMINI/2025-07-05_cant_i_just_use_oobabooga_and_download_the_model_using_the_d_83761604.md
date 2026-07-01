---
id: 477936
source: GEMINI
date: 2025-07-05
tags: ['text-generation-webui', 'model-download', 'oobabooga']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is asking if he can download a model directly through the Oobabooga interface.
---
# can't i just use oobabooga and download the model using the download link?

### USER
can't i just use oobabooga and download the model using the download link?

### GEMINI
Yes, absolutely! You are correct. You don't have to manually download the GGUF file and then move it. Oobabooga has a built-in "Download models" feature that is often the easiest way to get new models. Here's how to use Oobabooga's download functionality: Stop Oobabooga: If your Oobabooga server is currently running in your WSL2 terminal, press Ctrl+C to stop it. Start Oobabooga Normally (without specifying a model yet): ./installer_files/env/bin/python server.py This will start the web UI without immediately loading a large model, making it quicker to navigate to the download section. Go to the "Model" Tab in the Web UI: Open your web browser and go to http://127.0.0.1:7860. Click on the "Model" tab. Use the "Download models" Section: In the "Model" tab, you'll see a section specifically for downloading models. Model name (or HuggingFace ID): In the input field (it might say "Enter the model's name or a HuggingFace ID here"), type the full Hugging Face ID of the model you want. For Phi-3-mini-4k-instruct: Type microsoft/Phi-3-mini-4k-instruct. Oobabooga will then show you a list of available GGUF files for that model. Select the specific GGUF file: From the list that appears, choose the quantization you want (e.g., phi-3-mini-4k-instruct.Q4_K_M.gguf). Click the "Download" button. Wait for the Download: Oobabooga will download the model directly into your ~/text-generation-webui/models/ directory. You'll see progress in your terminal. Load the Newly Downloaded Model: Once the download is complete, go back to the top of the "Model" tab. In the dropdown menu where your current model is listed, you should now see the newly downloaded model (e.g., phi-3-mini-4k-instruct.Q4_K_M.gguf). Select it, and then click the "Load" button next to the dropdown. Confirm GPU Offload: While the model is loading, ensure that the "Number of layers to offload to GPU" (or n_gpu_layers) is set to 999 to maximize GPU utilization for speed. If you change this, click "Load" again. Using the built-in downloader is generally the most straightforward method.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
