---
id: 387864
source: GEMINI
date: 2025-06-24
tags: ['ai-tools', 'ai', 'gemini', 'model', 'oobabooga', 'llama.cpp', 'text-generation', 'python']
category: ai-tools
sentiment: building
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -l requirements*
total 8
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 22 18:00 full
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 22 18:00 portable
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -l requirements*
total 8
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 22 18:00 full
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 22 18:00 portable
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
I see the problem! The ls -l requirements* command shows that requirements.txt itself is missing from the main directory. Instead, you have full and portable directories, which likely contain their own requirements.txt files. This means that the original requirements.txt file from the text-generation-webui repository is gone or was never there in the first place for some reason in your current clone. The text-generation-webui project has moved to having different requirements/ subdirectories. When you run pip install -r requirements.txt at the root, it expects a file directly named requirements.txt. Solution: Use the correct requirements file from the requirements/ directory. Based on your previous commands and the way text-generation-webui is typically installed, you probably want to use requirements/requirements_linux.txt or requirements/requirements_windows.txt or a more general one like requirements/requirements.txt if it exists in that subdirectory. Given you are on WSL2, the linux one is probably more appropriate. Let's try that. Step 28: Install Dependencies from the Correct requirements File Action: Ensure your virtual environment is still active. Your prompt (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ indicates it is. Try installing from the requirements/requirements_linux.txt file: pip install -r requirements/requirements_linux.txt If that file doesn't exist, we'll try another, but this is a common one. After that completes (or if it errors out, let me know), then proceed with: pip install markdown pip install gradio==4.37.2 gradio_client==1.0.2 (These are still important to ensure specific versions are used). Then the llama.cpp specific build: pip install -r extensions/webui_llama_cpp/requirements.txt Finally, launch Oobabooga: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2 Please share the full output of pip install -r requirements/requirements_linux.txt. This should get us past the file not found error.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]