---
category: homelab
date: 2025-06-23
id: 600367
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: unresolved
sentiment: exploratory
source: GEMINI
summary: The user is exploring how to set up or configure something in their homelab
  without using a startup script, seeking alternative manual methods.
tags:
- startup-script
- homelab-configuration
- manual-setup
- automation-alternative
- system-boot
---
# without the startup script, how would i go about it? 

### USER
without the startup script, how would i go about it? 

### GEMINI
Okay, if you didn't have the start_ooba.sh script, or if you prefer to go through the steps manually each time (perhaps to change a parameter on the fly or just understand the process better), here's how you would typically launch Oobabooga: Manual Steps to Launch Oobabooga Open your Ubuntu WSL2 terminal. Search for "Ubuntu" in your Windows Start Menu and click to open it. Navigate to the text-generation-webui directory: At your terminal prompt, type: cd ~/text-generation-webui Press Enter. Activate the Python virtual environment: This ensures you're using the correct Python version (3.11) and all the necessary libraries that Oobabooga needs, which are installed within this isolated environment. Type: source .venv/bin/activate Press Enter. You'll know it's active because your terminal prompt will change to something like (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Start the Oobabooga server: Now that you're in the correct directory and environment, run the main server script with your desired flags. Based on your previous successful launch, this would be: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp Press Enter. Explanation of flags: --model-dir "user_data/models": Tells Oobabooga where to look for your downloaded models. --gpu-layers -1: Instructs the llama.cpp loader to offload as many layers as possible of the model to your NVIDIA GPU (RTX 3070). --loader llama.cpp: Specifies which backend loader to use for your .gguf models. Wait for the server to load the model: Watch the terminal output. It will show messages about loading the model, offloading layers to the GPU, and then eventually say something like: main: server is listening on http://127.0.0.1:53767 - starting the main loop INFO Loaded "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf" in X.XX seconds. Manually open the Web UI in your browser: Once you see the "server is listening" message, open your web browser on your Windows machine. Go to the URL: http://127.0.0.1:53767 This manual process essentially performs the same sequence of commands that are encapsulated in your start_ooba.sh script. The script just automates the typing and waits for you!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]