---
id: 447152
source: GEMINI
date: 2025-06-24
tags: ['coding', 'ai', 'gemini', 'model', 'oobabooga', 'llama.cpp', 'text-generation', 'dex']
category: coding
sentiment: frustrated
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ rm -rf .venv
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ./start_linux.sh
13:45:00-214661 INFO     Starting Text generation web UI
13:45:00-216603 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ rm -rf .venv
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ./start_linux.sh
13:45:00-214661 INFO     Starting Text generation web UI
13:45:00-216603 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

### GEMINI
Thank you for running those commands and providing the output. Unfortunately, the output from ./start_linux.sh is the same as before: Starting Text generation web UI Loading settings from "user_data/settings.yaml" Running on local URL: http://127.0.0.1:7860 This indicates that even after deleting the .venv directory, the start_linux.sh script is still not triggering a full reinstallation of dependencies. It's immediately launching the web UI as if everything is already in place. This is highly unusual behavior for the start_linux.sh script, which is designed to set up the environment if it doesn't exist. This suggests that either: There's a very specific environment variable or cached state that's tricking the script into thinking the environment is ready. Your specific clone of the Oobabooga text-generation-webui repository might have a modified start_linux.sh script, or it's a very new version that handles dependency checking differently. There's a deeper underlying issue with Python or pip within your WSL2 environment that's preventing the script from correctly identifying missing packages. Since a full reinstallation via start_linux.sh isn't working as expected, we need to try to explicitly reinstall the core components that we know are missing or broken. Step 20: Manually Reinstall Core Oobabooga and Gradio Dependencies We'll manually re-create the virtual environment and then explicitly install the critical packages, focusing on torch (with CUDA support) and gradio. Action: Stop Oobabooga completely. (If it's still running from the last command). Press Ctrl + C repeatedly in your WSL2 terminal until you see your prompt. Ensure you are in the top-level text-generation-webui directory: cd ~/text-generation-webui Delete the .venv directory one more time to ensure we start completely fresh: rm -rf .venv Create a new Python virtual environment: python3 -m venv .venv Activate the newly created virtual environment: source .venv/bin/activate Your prompt should now change to (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Manually install the essential Oobabooga dependencies. This includes torch with CUDA, gradio, gradio_client, and transformers as these are the most common points of failure for UI and model loading. We'll use the --upgrade flag to ensure we get the latest compatible versions. pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 pip install gradio gradio_client transformers --upgrade pip install -r extensions/superboogav2/requirements.txt # Install superboogav2 specific requirements The first command installs PyTorch with CUDA 12.1 support, which is crucial for your RTX 3070. This will be a large download. The second command installs gradio, gradio_client, and transformers. The third command installs any specific requirements for superboogav2 (we found its requirements.txt earlier). Watch for any error messages during these pip install commands. They are critical. They will take a long time to complete. Once all the pip install commands finish successfully and return you to your prompt, launch Oobabooga: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2 Once the server fully starts and displays the URL, open a new incognito/private browser window and go to http://127.0.0.1:7860. First, navigate to the "Extensions" tab in the Oobabooga UI to verify that superboogav2 is listed and checked. If it's not, check it and then click "Reload UI". Then, meticulously check all the main tabs at the top of the UI for "SuperBooga". This manual, step-by-step installation within a fresh virtual environment gives us maximum control and visibility over the dependency installation process. Please provide all output from these commands, especially any errors during pip install.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]