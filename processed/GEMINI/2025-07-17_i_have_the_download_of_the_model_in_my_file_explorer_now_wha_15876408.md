---
id: 745911
source: GEMINI
date: 2025-07-17
tags: ['ai-tools', 'ai', 'gemini', 'model', 'oobabooga', 'rag', 'openai', 'gguf']
category: ai-tools
sentiment: executing
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# i have the download of the model in my file explorer. now what?

### USER
i have the download of the model in my file explorer. now what?

### GEMINI
Excellent! Having the .gguf file downloaded manually is the key. Now, let's get that model into Oobabooga so you can use it. Next Steps: Locate your Oobabooga models directory: Based on your previous console output, your Oobabooga installation seems to be located at: /home/bryan_/text-generation-webui/ Inside that folder, there should be a models subfolder. The full path you're looking for is: /home/bryan_/text-generation-webui/models/ Action: Open your file explorer (e.g., Nautilus on Linux, or whatever you use) and navigate to this models directory. Move the downloaded .gguf file into the models directory: Find the Meta-Llama-3-8B-Instruct-Q4_K_M.gguf file you just downloaded (it's likely in your "Downloads" folder). Action: Drag and drop (or copy and paste) this .gguf file into the /home/bryan_/text-generation-webui/models/ folder. Load the new model in Oobabooga's Web UI: Make sure your Oobabooga text-generation-webui is still running in your browser (at http://127.0.0.1:46227 or similar). Go to the "Model" tab in the Oobabooga web UI. You'll see a dropdown list of available models. It might still show "Phi-3-mini-4k-instruct-q4". Action: Click the refresh icon (usually a circular arrow) next to the model dropdown list. This tells Oobabooga to rescan the models folder for new files. Action: After refreshing, open the dropdown list again. You should now see Meta-Llama-3-8B-Instruct-Q4_K_M.gguf (or the exact filename you downloaded). Action: Select Meta-Llama-3-8B-Instruct-Q4_K_M.gguf from the dropdown. Action: Click the large "Load" button. Oobabooga will now unload the Phi-3-mini model and load the Llama 3 8B Instruct model. You should see confirmation in your Oobabooga console that the new model has been loaded successfully. Once loaded, your CrewAI workflow will automatically use this more powerful model when it connects to Oobabooga's OpenAI-compatible API.