---
category: coding
date: 2025-07-30
id: 979582
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is clarifying whether he needs to install the model in the terminal
  where Ollama is running.
tags:
- ollama
- model-installation
- local-llm-setup
---
# do i then need to physically install that model in my terminal that ollama is running in? 

### USER
do i then need to physically install that model in my terminal that ollama is running in? 

### GEMINI
Yes, absolutely! You must physically install (download) the qwen2.5-coder:1.5b model in your terminal where Ollama is running. Here's why and how: Ollama is the Model Server: Continue.dev (and your config.yaml) tells the VS Code extension which model name to request from an Ollama server. However, Continue.dev doesn't actually store or run the model itself. Ollama does. Models are Downloaded by Ollama: When Continue.dev asks Ollama for qwen2.5-coder:1.5b, if Ollama doesn't have that model downloaded and stored locally, it won't be able to serve it. Ollama will usually try to download it automatically the first time it's requested, but it's best practice to explicitly pull it yourself to ensure it's ready. How to "install" (pull) the model in your terminal: Open your terminal where you run Ollama (or a new terminal if Ollama is running as a background service). Run the Ollama pull command: ollama pull qwen2.5-coder:1.5b Important: Make sure the name qwen2.5-coder:1.5b exactly matches the model tag you intend to use and which you put in your config.yaml. You can verify available model tags on the Ollama Library website or by running ollama list if you've already pulled other qwen2.5-coder models. This command will: Check if qwen2.5-coder:1.5b is already downloaded. If not, it will start downloading all the necessary layers for the model. This can take some time depending on your internet connection and the model size (1.5B is relatively small, so it should be quick). You'll see progress bars in your terminal during the download. Once the download is complete, Ollama will have the qwen2.5-coder:1.5b model available locally, and Continue.dev will be able to successfully request completions from it for your "Autocomplete" feature.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
