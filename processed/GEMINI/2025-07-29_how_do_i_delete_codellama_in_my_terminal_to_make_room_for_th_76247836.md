---
category: ai-tools
date: 2025-07-29
id: 677338
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan wants to know how to remove the CodeLlama model from his terminal using
  Ollama, presumably to free up space for a new model.
tags:
- ollama-model-management
- codellama
- local-llm-deployment
- terminal-commands
---
# how do i delete codellama in my terminal to make room for this new model i wanna try? 

### USER
how do i delete codellama in my terminal to make room for this new model i wanna try? 

### GEMINI
You're in luck! Ollama makes deleting models very straightforward and easy. You don't need to completely uninstall Ollama itself, just the specific model. Here's how to do it in your terminal (Command Prompt or PowerShell on Windows): 1. List your currently installed models: First, it's a good idea to see exactly what models you have and their precise names. This command will show you a list: ollama list This will output something like: NAME ID SIZE MODIFIED codellama:7b-code df94f1a233b 3.8 GB 3 days ago mistral:7b-instruct 61f855363b9 4.1 GB 2 weeks ago llama2:7b 6221c0022d1 3.8 GB 2 months ago Look for the exact name of your codellama model. It might be codellama:7b or codellama:13b or codellama:latest or have a specific quantization suffix like codellama:7b-instruct-q4_K_M. 2. Delete the specific codellama model: Once you have the exact name, use the ollama rm command followed by the model name. Example: If your codellama model is named codellama:7b-code, you would type: ollama rm codellama:7b-code Ollama will usually give you a confirmation message, like: deleted 'codellama:7b-code' 3. Verify the deletion: You can run ollama list again to confirm that codellama is no longer in your list of installed models and that the disk space has been reclaimed. ollama list Important Notes: Exact Name: Make sure you use the exact model name as it appears in the ollama list output. Case sensitivity matters. Running Models: If you happen to have the codellama model currently loaded and running (e.g., if you opened it in a chat session or your IDE is actively using it), you might need to stop the Ollama service or close the application using it before it can be deleted. Typically, you can stop the Ollama service via your system's services manager, or if you're just running it from the command line, closing that window might be enough. Shared Layers: Ollama is smart about sharing "blob" files (the actual model weights) between different models if they use common components. If you delete codellama but still have another model that uses some of the same underlying data, those shared files won't be fully deleted until all models relying on them are removed. However, for a unique model like codellama, you should see a significant amount of disk space freed up. Once you've successfully deleted codellama, you'll have ample space on your 2TB SSD and VRAM for the new llama3.1:8b-instruct-q4_K_M model.
