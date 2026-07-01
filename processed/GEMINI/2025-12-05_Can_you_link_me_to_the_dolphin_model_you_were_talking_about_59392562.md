---
category: ai-tools
date: 2025-12-05
id: 781976
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is requesting a link to the Dolphin LLM model that was previously discussed.
tags:
- local-llm
- dolphin-model
- model-link
---
# Can you link me to the dolphin model you were talking about?

### USER
Can you link me to the dolphin model you were talking about?

### GEMINI
I will give you the two most direct ways to access the optimal Dolphin Llama 3 model, based on whether you prefer the command line or a graphical interface. This model is a strong contender for your goal of an uncensored/unaligned, high-performing 8B model that fits your 8GB VRAM. 💻 Option 1: Using Ollama (Recommended for Command Line/API) If you followed the advice to install Ollama, this is the quickest and cleanest way to get the model running. Ollama handles the GGUF download and GPU offload configuration for you. Install Ollama: If you haven't, download and install the Windows client from the official Ollama website. Run the Pull Command: Open your command prompt or terminal and execute the following command: ollama run dolphin3:8b This command will automatically pull the Dolphin 3.0 Llama 3.1 8B model, which is typically in the recommended Q4_K_M quantization (around 4.9 GB). This is the optimal, fast-running version for your 8GB RTX 3070. 🖼️ Option 2: Using LM Studio (Recommended for Desktop Chat Interface) If you prefer a Windows desktop application to search, download, and chat with the model, use LM Studio. Install LM Studio: Download and install LM Studio (available for Windows). Search: In the search bar at the top, type one of the following to find the model: Dolphin 3.0 Llama 3.1 8B bartowski/Dolphin3.0-Llama3.1-8B-GGUF Download the Right File: Look for the model by the user bartowski or a similar highly-rated quantizer (like Triangle104 or dphn). Crucially, on the model download page, look for the file that has the quantization type: Filename: Dolphin3.0-Llama3.1-8B-Q4_K_M.gguf Size: Look for the file around 4.9 GB. Warning: Be sure to stick with the Q4_K_M (or Q5_K_M) quantization. Avoid the 70B versions—they are too large for your VRAM and will grind your system to a halt. Would you like me to find a direct installation link for Ollama or LM Studio to get you started?
