---
id: 095368
source: GEMINI
date: 2025-06-24
tags: ['ai-tools', 'ai', 'gemini', 'model', 'gguf', 'quantized', 'lora', 'hermes']
category: ai-tools
sentiment: building
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# (venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ echo $?
0
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --listen --model-menu
15:28:17-944390 INFO     Starting Text generation web UI
15:28:17-946589 WARNING
                         You are potentially exposing the web UI to the entire internet without any access password.
                         You can create one with the "--gradio-auth" flag like this:

                         --gradio-auth username:password

                         Make sure to replace username:password with your own.
15:28:17-951042 ERROR    No models are available! Please download at least one.
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ echo $?
0
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --listen --model-menu
15:28:17-944390 INFO     Starting Text generation web UI
15:28:17-946589 WARNING
                         You are potentially exposing the web UI to the entire internet without any access password.
                         You can create one with the "--gradio-auth" flag like this:

                         --gradio-auth username:password

                         Make sure to replace username:password with your own.
15:28:17-951042 ERROR    No models are available! Please download at least one.
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Excellent! That's fantastic news! Here's a breakdown of what happened: echo $? returning 0 means the pip install -r requirements/full/requirements.txt command completed successfully. All your Python dependencies are now correctly installed in your virtual environment. When you ran python3 server.py --listen --model-menu: INFO Starting Text generation web UI: This confirms that the web UI itself has launched! The WARNING about exposing the web UI is standard when you use --listen without --gradio-auth. It's just a heads-up, not an error that prevents the UI from working. ERROR No models are available! Please download at least one.: This is completely expected and good! It means the UI started, but since we confirmed you don't have Nous-Hermes-2 Mistral 7B downloaded yet, it's correctly telling you that you need to get a model. Your text-generation-webui is now running in the background within your WSL terminal! What to do now: Open your web browser on Windows. Go to the URL that the text-generation-webui typically runs on: http://127.0.0.1:7860 If that doesn't work for some reason (though it almost always does with --listen), look carefully at the output in your WSL terminal just above where it printed the "ERROR No models are available!" line. It should have printed something like Running on local URL: http://127.0.0.1:7860 or similar. Use that exact URL. Download the model: Once the text-generation-webui interface loads in your browser, navigate to the "Model" tab (it's usually one of the main tabs at the top). In the "Download model or LoRA" section, enter the Hugging Face repository ID for the model. For Nous-Hermes-2 Mistral 7B from TheBloke (recommended for GGUF versions), use: TheBloke/Nous-Hermes-2-Mistral-7B-DPO-GGUF A dropdown list will appear below where you typed, showing different quantized versions of the model (e.g., Q4_K_M, Q5_K_M). Choose one that fits your GPU's VRAM and your performance/quality preference. Q4_K_M is a good balance. Click the "Download" button. The model will then start downloading into your ~/text-generation-webui/models/ directory inside WSL. This will take some time, as it's a large file. You'll see progress updates in the web UI. Load the model: Once the download is complete, it will appear in the "Model" dropdown menu at the top of the "Model" tab. Select the downloaded model from the dropdown. Click the "Load" button. The UI will then load the model and offload layers to your GPU. Once loaded, you can go to the "Text generation" tab and start interacting with your AI model! You've successfully overcome all the setup hurdles! Great job!