---
id: 049854
source: GEMINI
date: 2025-06-24
tags: ['ai-tools', 'ai', 'gemini', 'model', 'oobabooga', 'llama.cpp', 'text-generation', 'python']
category: ai-tools
sentiment: executing
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -l requirements/
total 8
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 22 18:00 full
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 22 18:00 portable
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -l requirements/
total 8
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 22 18:00 full
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 22 18:00 portable
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Okay, I see the issue now! Your requirements/ directory doesn't contain a requirements.txt or requirements_linux.txt directly. Instead, it has two subdirectories: full and portable. This indicates that your version of text-generation-webui organizes its dependencies by installation type within these subdirectories. For a full installation that supports various features and extensions (like llama.cpp and superboogav2), the full requirements are usually the most appropriate. Let's try installing from the full requirements file: Step 29: Install Dependencies from requirements/full/requirements.txt Action: Ensure your virtual environment is still active. Your prompt (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ indicates it is. Execute the following command: pip install -r requirements/full/requirements.txt This command should now correctly find the requirements file. After that completes, proceed with the specific Gradio/Gradio Client installation to ensure the correct versions: pip install markdown pip install gradio==4.37.2 gradio_client==1.0.2 (It's crucial to run these two lines separately after the requirements.txt as they override any conflicting versions that might be pulled in by the main requirements file.) Then the llama.cpp specific build: pip install -r extensions/webui_llama_cpp/requirements.txt Finally, launch Oobabooga: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2 Please share the full output of pip install -r requirements/full/requirements.txt. This should resolve the file not found error and get us much closer!