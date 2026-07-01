---
category: homelab
date: 2025-06-23
id: 882248
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- text-generation-webui
resolution: resolved
sentiment: executing
source: GEMINI
summary: The user successfully started the Text Generation Web UI server with llama.cpp
  backend, loading models from a custom directory with GPU layers set to CPU-only
  mode (-1), and the server is running on localhost:7860.
tags:
- text-generation-webui
- llama.cpp
- GPU configuration
- local AI server
- model loading
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
14:03:54-851020 INFO     Starting Text generation web UI
14:03:54-853053 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
14:03:54-851020 INFO     Starting Text generation web UI
14:03:54-853053 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

### GEMINI
SUCCESS! This is exactly what we wanted to see! The output: 14:03:54-851020 INFO Starting Text generation web UI 14:03:54-853053 INFO Loading settings from "user_data/settings.yaml" Running on local URL: http://127.0.0.1:7860 Means that oobabooga's text-generation-webui has successfully started within your WSL2 Ubuntu environment! It's now listening for connections. Step 8: Access the Web UI from Windows and Load the Model You can now access the web UI directly from your Windows web browser. Action: Open your web browser on your Windows desktop and navigate to the provided URL. Then, load your model. What I need you to do now (on your Windows desktop): Open your web browser (Chrome, Edge, Firefox, etc.). Go to the URL: http://127.0.0.1:7860 Simply copy and paste this into your browser's address bar and press Enter. You should now see the oobabooga Text Generation WebUI interface! Inside the Web UI: Navigate to the "Model" tab. This is usually one of the tabs at the top. In the "Model" dropdown menu on the left side, you should see Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf. (It might be the only one listed if you haven't downloaded others through the UI). Select this model. Confirm the "Model loader" is set to llama.cpp. (It should be, as we specified it in the launch command, but it's good to double-check). Click the "Load" button (it's usually a large button below the model selection). What to expect after clicking "Load": Your Ubuntu WSL2 terminal (where oobabooga is running) will start showing a lot of messages. This is the llama.cpp loader loading the model into memory and offloading layers to your RTX 3070's VRAM. You'll see messages like "llama_model_loader: loaded meta data with X tensors from X", "llm_load_vocab: missing tokens", "ggml_init_cublas: found 1 NVIDIA GPUs", "offloading X layers to GPU", etc. The loading process can take anywhere from a few seconds to a minute or two, depending on the model size and your system speed. Once loaded, the terminal will show a "Successfully loaded..." message. What I need from you now: Confirm that you can access the web UI in your browser. Once you attempt to load the model in the UI, copy and paste all of the new output from your Ubuntu WSL2 terminal here. This will confirm if the model successfully loaded onto your GPU. You are incredibly close to chatting with your model!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]