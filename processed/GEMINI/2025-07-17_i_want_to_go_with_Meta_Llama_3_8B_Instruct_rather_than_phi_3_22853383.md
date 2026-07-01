---
category: ai-tools
date: 2025-07-17
id: 665260
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wants to switch from Phi-3-mini to Meta Llama 3 8B Instruct in oobabooga.
tags:
- meta-llama-3
- oobabooga
- model-switching
- local-llm
---
# i want to go with Meta Llama 3 8B Instruct rather than phi 3 mini. can you help me get that setup? currently have oobabooga running main: server is listening on http://127.0.0.1:46227 - starting the main loop
12:21:47-545830 INFO     Loaded "Phi-3-mini-4k-instruct-q4" in 3.01 seconds.
12:21:47-546931 INFO     LOADER: "llama.cpp"
12:21:47-547458 INFO     TRUNCATION LENGTH: 4096
12:21:47-547909 INFO     INSTRUCTION TEMPLATE: "Custom (obtained from model metadata)"
12:21:47-548368 INFO     Loading the extension "openai"
12:21:47-637304 INFO     Loading the extension "whisper_stt"
12:21:47-638197 INFO     OpenAI-compatible API URL:   http://0.0.0.0:5000

### USER
i want to go with Meta Llama 3 8B Instruct rather than phi 3 mini. can you help me get that setup? currently have oobabooga running main: server is listening on http://127.0.0.1:46227 - starting the main loop
12:21:47-545830 INFO     Loaded "Phi-3-mini-4k-instruct-q4" in 3.01 seconds.
12:21:47-546931 INFO     LOADER: "llama.cpp"
12:21:47-547458 INFO     TRUNCATION LENGTH: 4096
12:21:47-547909 INFO     INSTRUCTION TEMPLATE: "Custom (obtained from model metadata)"
12:21:47-548368 INFO     Loading the extension "openai"
12:21:47-637304 INFO     Loading the extension "whisper_stt"
12:21:47-638197 INFO     OpenAI-compatible API URL:   http://0.0.0.0:5000

### GEMINI
Okay, let's get your Oobabooga setup running with Meta Llama 3 8B Instruct. Your current Oobabooga output shows: Loaded "Phi-3-mini-4k-instruct-q4": This is the model we need to switch. Loading the extension "openai": Good, the OpenAI API is already enabled. OpenAI-compatible API URL: http://0.0.0.0:5000: This is your API endpoint, which your CrewAI workflow will connect to. Here are the steps to switch the model: Step 1: Download Meta Llama 3 8B Instruct (GGUF) Go to Hugging Face: Open your web browser and go to https://huggingface.co/. Search for the model: In the search bar, type Meta-Llama-3-8B-Instruct-GGUF. Find "TheBloke" repository: Look for a repository by a user named "TheBloke" (e.g., TheBloke/Meta-Llama-3-8B-Instruct-GGUF). TheBloke is a well-known uploader of quantized models. Go to the "Files and versions" tab: Once you're on TheBloke's model page, click on the "Files and versions" tab. Download a quantized .gguf file: Scroll down the list of files. Look for a file ending with .gguf. Given your 8GB RTX 3070, I highly recommend downloading the Q5_K_M quantization. This offers an excellent balance of quality and performance for your VRAM. The filename will look something like: meta-llama-3-8b-instruct.Q5_K_M.gguf Click the download icon next to this file. Step 2: Place the Downloaded Model in Oobabooga's Directory Locate your Oobabooga installation folder. This is the directory where you installed text-generation-webui (e.g., C:\oobabooga-windows\text-generation-webui). Navigate to the models subfolder within your Oobabooga installation. Move the downloaded .gguf file (e.g., meta-llama-3-8b-instruct.Q5_K_M.gguf) into this models folder. Step 3: Load the New Model in Oobabooga's Web UI Open your Oobabooga web UI in your browser (it's likely still running at http://127.0.0.1:46227 based on your console output, or http://localhost:46227). Go to the "Model" tab. In the dropdown menu under "Model loader" (or similar, it might just be the main model selection dropdown), you should now see meta-llama-3-8b-instruct.Q5_K_M.gguf (or whatever the exact filename is). If you don't see it, click the refresh icon next to the dropdown. Select meta-llama-3-8b-instruct.Q5_K_M.gguf from the dropdown. Click the "Load" button. Oobabooga will now unload Phi-3-mini and load Meta Llama 3 8B Instruct. You'll see confirmation in your Oobabooga console. Step 4: Verify CrewAI Configuration (No Changes Needed Here) Your CrewAI Python script should remain exactly as you had it, using the OPENAI_API_BASE and OPENAI_MODEL_NAME environment variables: import os # ... (other imports) ... # --- Configuration for Oobabooga's OpenAI-compatible API --- # This matches the API URL you already have running in Oobabooga os.environ["OPENAI_API_BASE"] = "http://localhost:5000/v1" # Use 127.0.0.1 if localhost doesn't work # Dummy API key (Oobabooga's local API doesn't need a real one) os.environ["OPENAI_API_KEY"] = "sk-not-needed-for-local" # Your CrewAI workflow will request this model name # Oobabooga will use the Llama 3 8B model you just loaded os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo" # ... (rest of your CrewAI agents, tasks, and crew definition) ... Now, when your CrewAI workflow runs, it will send requests to your Oobabooga server, which will process them using the much more capable Meta Llama 3 8B Instruct model. You should see a significant improvement in the quality and reasoning of your multi-agent interactions!
