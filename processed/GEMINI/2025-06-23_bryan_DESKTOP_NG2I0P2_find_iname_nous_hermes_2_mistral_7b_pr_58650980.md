---
category: homelab
date: 2025-06-23
id: 465343
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: resolved
sentiment: exploratory
source: GEMINI
summary: User located a GGUF model file on their local system using the find command,
  confirming the presence of the Nous-Hermes-2-Mistral-7B model in their text-generation-webui
  setup.
tags:
- local-llm
- model-management
- file-search
- text-generation-webui
- gguf-models
---
# bryan_@DESKTOP-NG2I0P2:~$ find ~ -iname "*nous-hermes-2-mistral-7b*" -print
/home/bryan_/text-generation-webui/user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf
bryan_@DESKTOP-NG2I0P2:~$

### USER
bryan_@DESKTOP-NG2I0P2:~$ find ~ -iname "*nous-hermes-2-mistral-7b*" -print
/home/bryan_/text-generation-webui/user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf
bryan_@DESKTOP-NG2I0P2:~$

### GEMINI
EXCELLENT! This is precisely what we needed! You've found your model: Full Path to Directory: /home/bryan_/text-generation-webui/user_data/models/ Exact Filename: Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf This tells us a lot: The model is located within a text-generation-webui directory, which strongly suggests you either downloaded it using oobabooga's interface before, or you intended to use it with oobabooga. This is perfect! The model file ends with .gguf, confirming it's a GGUF format model, which is ideal for CPU and GPU inference with llama.cpp-based backends (which oobabooga often leverages, especially for GGUF). Now that we've confirmed the model's location, we can move on to getting oobabooga's text-generation-webui to recognize it and run properly, maximizing your system's performance. Step 3: Optimizing and Launching Oobabooga's Text Generation WebUI The fact that your model is already in text-generation-webui/user_data/models is a great head start. We'll focus on ensuring oobabooga is set up to detect and utilize your RTX 3070 and that it starts correctly. Action: We need to navigate to your text-generation-webui directory and then launch the web UI with the correct flags for your GPU. What I need you to do now (in your Ubuntu WSL2 terminal): Change Directory to text-generation-webui: You are currently in /home/bryan_. Your text-generation-webui directory is right there. Command: cd text-generation-webui After you run this, your prompt should change to something like bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Launch Oobabooga with GPU Acceleration (Critical Step): This is where we tell oobabooga to use your NVIDIA GPU. The webui.sh script is the standard way to launch it. We'll add the --model-dir argument to explicitly point to your models directory, and --gpu-layers to ensure the model layers are loaded onto your RTX 3070. Context for --gpu-layers: The Mistral 7B model has roughly 32 layers. Your 8GB RTX 3070 should be able to load a significant portion, if not all, of a Q5_K_M GGUF model into VRAM. Loading more layers onto the GPU (VRAM) means faster inference, as it reduces the amount of data that needs to be swapped between RAM and VRAM. A value of -1 attempts to offload all layers possible, while a specific number, like 30 or 32, can be used if you want to be more precise or if -1 causes issues. Let's start with -1 for maximum offload. Command: python server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp Explanation of this command: python server.py: This is the main script that starts the web UI. --model-dir "user_data/models": This explicitly tells oobabooga to look for models in the user_data/models subdirectory relative to the current directory (text-generation-webui). Since we verified your model is there, this is important. --gpu-layers -1: This is the crucial flag that tells the llama.cpp backend (which handles GGUF models) to offload as many model layers as possible onto your NVIDIA GPU's VRAM. -1 means "all layers that fit." --loader llama.cpp: This specifies that oobabooga should use the llama.cpp loader, which is the correct one for GGUF models. What I need from you: Confirm that your terminal prompt has changed to reflect being inside the text-generation-webui directory after running cd text-generation-webui. Run the python server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp command. Crucially, copy and paste any and all output you see in the terminal after running this command. This includes lines about "Downloading...", "Loading...", "Listening on...", or any errors. I will be waiting for that output. This command will start the web UI, and we'll then address how to access it from Windows if it launches successfully. If there are errors, we'll troubleshoot them based on the output you provide.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]