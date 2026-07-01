---
id: 845566
source: GEMINI
date: 2025-06-24
tags: ['coding', 'ai', 'gemini', 'model', 'oobabooga', 'llama.cpp', 'text-generation', 'dex']
category: coding
sentiment: building
resolution: partial
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 --versionPython 3.10.18(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 --versionPython 3.10.18(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Excellent! Python 3.10.18 is exactly what we want to see. This confirms that python3 now correctly points to the 3.10 version. Now, we can finally proceed with Step 26: Re-create the Virtual Environment with Python 3.10 and Reinstall Dependencies. This is the crucial part that should resolve the TypeError you were encountering due to Python 3.12 incompatibility. Step 26: Re-create the Virtual Environment with Python 3.10 and Reinstall Dependencies Action: Deactivate your current virtual environment: deactivate Your prompt should go back to bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Delete the existing virtual environment: rm -rf .venv Create a new virtual environment using Python 3.10: python3.10 -m venv .venv Activate the new virtual environment: source .venv/bin/activate Your prompt should now show (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Re-install torch and torchvision: If you have an NVIDIA GPU and CUDA is correctly set up in WSL2, and you're confident it's CUDA 11.8: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 If you do NOT have a supported NVIDIA GPU, or if you're unsure about CUDA in WSL2 (safe option): pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu Important: Choose only one of the above pip install commands. Re-install other necessary dependencies (including the specific Gradio/Gradio Client and markdown): pip install -r requirements.txt pip install markdown pip install gradio==4.37.2 gradio_client==1.0.2 This order is important: requirements.txt might try to install a newer Gradio, but then our explicit pip install gradio==4.37.2 gradio_client==1.0.2 will force the correct, older versions. Run the llama.cpp specific build (important for the --loader llama.cpp argument): pip install -r extensions/webui_llama_cpp/requirements.txt Finally, launch Oobabooga again: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2 Please provide the output of each of these commands as you execute them. This is a very thorough rebuild, and it stands the best chance of resolving your long-standing issue!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]