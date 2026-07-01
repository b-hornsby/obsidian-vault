---
category: homelab
date: 2025-06-23
id: 2049
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- operation-immortal-agent
resolution: unresolved
sentiment: executing
source: GEMINI
summary: The user has successfully gotten a model running in Oobabooga and is asking
  for guidance on next steps to further develop their local LLM setup at home.
tags:
- local-llm-deployment
- oobabooga
- self-hosted-ai
- homelab-setup
- next-steps-planning
---
# so now that i have the model interacting within oobabooga, what are my next steps to take this home? lets get this shit 

### USER
so now that i have the model interacting within oobabooga, what are my next steps to take this home? lets get this shit 

### GEMINI
That's awesome news, Bryan! You've successfully navigated the complexities of WSL2, Python versions, and GPU integration. Now that you have the model interacting within Oobabooga, let's "take this home" and get you comfortable with running it, exploring more models, and understanding the basics. Here's your roadmap: 1. Stopping and Restarting Oobabooga You'll need to know how to stop the server cleanly and how to fire it up again for future sessions. To Stop Oobabooga: Go back to your Ubuntu WSL2 terminal where Oobabooga is running. Press Ctrl + C repeatedly until you see your command prompt (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ again. This ensures the server shuts down gracefully. You can then close the WSL2 terminal if you're done. To Restart Oobabooga (in a new session): Open your Ubuntu WSL2 terminal. Navigate to the text-generation-webui directory: cd ~/text-generation-webui Activate your Python 3.11 virtual environment: source .venv/bin/activate You should see (.venv) appear at the beginning of your prompt. Start the Oobabooga server with your model: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp Once it says server is listening on http://127.0.0.1:<port_number>, open your Windows browser to that address. 2. Downloading and Using More Models Now that llama.cpp is working, you can easily download and use other GGUF models. Where to find GGUF models: The best place is Hugging Face: https://huggingface.co/models Filter for GGUF: When searching on Hugging Face, look for models with the "GGUF" tag, or search for "GGUF" in the model name. These are optimized for llama.cpp. Quantization Levels: You'll see different quantization levels (e.g., Q4_K_M, Q5_K_S, Q8_0). Lower numbers (like Q4_K_M) use less VRAM but have slightly lower quality. Higher numbers (like Q8_0) use more VRAM but offer better quality. Your RTX 3070 (8GB VRAM) can handle most 7B models at Q5_K_M or even Q6_K, and some smaller 13B models if you manage gpu-layers. Recommended Repositories: Look for models from reputable quantizers like TheBloke, PulsarForge, MaziyarPanahi, etc., on Hugging Face. How to Download Models: On the Hugging Face model page, navigate to the "Files and versions" tab. Find the .gguf file you want (e.g., model-name.Q4_K_M.gguf). Click the download icon next to the filename. Save the .gguf file directly into your ~/text-generation-webui/user_data/models/ directory in WSL2. You can do this by opening your File Explorer in Windows, typing \\wsl$\Ubuntu\home\bryan_\text-generation-webui\user_data\models in the address bar, and dragging the downloaded file there. Loading a New Model in Oobabooga: Make sure your Oobabooga server is running. In the Oobabooga Web UI, go to the "Model" tab (left-hand panel). In the "Model" tab, click the "Refresh" button (usually a circular arrow icon). Your newly downloaded model should now appear in the dropdown list. Select the model from the dropdown. Click the "Load" button. Keep an eye on your WSL2 terminal; it will show the loading progress and confirmation once the model is ready. 3. Key Oobabooga Web UI Tabs Chat: This is your primary interface for conversing with the model. Experiment with different chat modes (e.g., "Chat," "Chat-instruct") and prompt formats. Parameters: Generation Parameters: This tab lets you tweak how the model generates text. Temperature: Higher values (e.g., 0.7-1.0) make responses more creative/random. Lower values (e.g., 0.1-0.5) make them more focused/deterministic. Top P, Top K: Control the diversity and quality of the generated tokens. Default values are often good starting points. Max new tokens: Sets the maximum length of the model's response. llama.cpp Specific Settings: When using llama.cpp, you'll see settings like gpu-layers and ctx_size. gpu-layers: You're currently using -1 which means Oobabooga will try to offload all possible layers to the GPU. You can reduce this number if you run out of VRAM for larger models (e.g., 20 instead of -1). ctx_size (Context Size): This is the maximum number of tokens (words/pieces of words) the model can "remember" in a conversation. Your current model supports 32768, but your launch command uses 8192. You can experiment with increasing the ctx_size in the "Parameters" tab if your GPU VRAM allows, but be mindful that higher context sizes use significantly more VRAM. Session: You can save and load your chat histories here, which is handy for continuing long conversations. 4. Important Tips for Future Use GPU RAM is Key: Your RTX 3070 has 8GB VRAM. This is good for 7B models and some 13B models, especially if you use efficient quantizations (Q4_K_M, Q5_K_M). Larger models (e.g., 70B) will likely require much more VRAM. Keep Oobabooga Updated: The text-generation-webui project is actively developed. Periodically, you might want to update it to get the latest features and bug fixes. deactivate (if .venv is active) cd ~/text-generation-webui git pull source .venv/bin/activate pip install -r requirements/full/requirements.txt --upgrade (this will update existing packages) Community and Resources: The Oobabooga GitHub repository and community are great resources for troubleshooting and learning more: https://github.com/oobabooga/text-generation-webui YouTube tutorials often show visual walkthroughs of common tasks. You've done the hard part, Bryan. Now it's time to experiment, download different models, and have fun interacting with your local AI! Let me know if you run into any more specific questions as you explore.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]