---
id: 503606
source: GEMINI
date: 2025-06-24
tags: ['coding', 'ai', 'gemini', 'model', 'oobabooga', 'llama.cpp', 'text-generation', 'dex']
category: coding
sentiment: building
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python --version
python3 --version
Python 3.12.3
Python 3.12.3
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python --version
python3 --version
Python 3.12.3
Python 3.12.3
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
You are absolutely correct. Your system-wide python and python3 commands are indeed pointing to Python 3.12.3. This confirms our hypothesis that the newer Python version is causing compatibility issues with Oobabooga's dependencies, especially Gradio. Now, let's proceed with the plan to install Python 3.10 and set it as the default for Oobabooga. Continuing with Step 25: Install Python 3.10 (Recommended) and Update Alternatives Action: Stop Oobabooga completely. (Press Ctrl + C in your WSL2 terminal until you see your prompt.) Ensure you are in the top-level text-generation-webui directory: cd ~/text-generation-webui Install Python 3.10 and its development tools: sudo apt update sudo apt install python3.10 python3.10-venv python3.10-dev -y This command will install Python 3.10 if it's not already fully present, and also python3.10-venv which is crucial for creating virtual environments, and python3.10-dev for building certain Python packages. Verify Python 3.10 is installed: python3.10 --version You should see Python 3.10.x (e.g., Python 3.10.12 on Ubuntu 22.04). Update update-alternatives to prefer Python 3.10 for the python3 command. This command adds Python 3.10 as an alternative for python3 with priority 1. sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1 Now, configure python3 to use Python 3.10 from the alternatives list: sudo update-alternatives --config python3 You will see a list of Python versions. It will look something like this (your exact list might vary): There are 2 choices for the alternative python3 (providing /usr/bin/python3). Selection Path Priority Status -
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
--- * 0 /usr/bin/python3.12 2 auto mode 1 /usr/bin/python3.10 1 manual mode 2 /usr/bin/python3.12 2 manual mode Press <enter> to keep the current choice[*], or type selection number: Type the number corresponding to /usr/bin/python3.10 (in the example above, it's 1) and press Enter. Confirm the change: python3 --version It must now show Python 3.10.x. If it still shows 3.12.x, something went wrong, and we need to troubleshoot this step before proceeding. After you have successfully verified that python3 --version outputs Python 3.10.x, then proceed to Step 26. Step 26: Re-create the Virtual Environment with Python 3.10 and Reinstall Dependencies Action: Deactivate your current virtual environment: deactivate Your prompt should go back to bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Delete the existing virtual environment: rm -rf .venv Create a new virtual environment using Python 3.10: python3.10 -m venv .venv Activate the new virtual environment: source .venv/bin/activate Your prompt should now show (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Re-install torch and torchvision (CPU version if you don't have a supported NVIDIA GPU or CUDA is not set up): pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu OR (if you have an NVIDIA GPU and CUDA is correctly set up in WSL2): pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 # Or cu121 if you have CUDA 12.1+ Again, if you're unsure about CUDA, stick with the CPU version for now. Getting Oobabooga to launch is the priority. Re-install other necessary dependencies (including the specific Gradio/Gradio Client and markdown): pip install -r requirements.txt pip install markdown pip install gradio==4.37.2 gradio_client==1.0.2 Remember that installing requirements.txt might try to bring in a newer Gradio. By explicitly installing gradio==4.37.2 gradio_client==1.0.2 after it, pip should correct the version if it was upgraded. Run the llama.cpp specific build (important for the --loader llama.cpp argument): pip install -r extensions/webui_llama_cpp/requirements.txt Finally, launch Oobabooga again: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2 This is a comprehensive set of steps, but it directly addresses the Python version incompatibility that's likely causing the TypeError. Please share the output of each command, especially the python3 --version check after updating alternatives and the final Oobabooga launch.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]