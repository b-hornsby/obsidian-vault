---
id: 938126
source: GEMINI
date: 2025-07-05
tags: ['coding', 'ai', 'gemini', 'model', 'oobabooga', 'rag', 'gguf', 'hermes']
category: coding
sentiment: frustrated
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md']
---
# (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -F installer_files/env/
bin/    compiler_compat/  etc/      lib/      man/   share/  x86_64-conda-linux-gnu/
cmake/  conda-meta/       include/  libexec/  sbin/  ssl/    x86_64-conda_cos7-linux-gnu/
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -F installer_files/env/
bin/    compiler_compat/  etc/      lib/      man/   share/  x86_64-conda-linux-gnu/
cmake/  conda-meta/       include/  libexec/  sbin/  ssl/    x86_64-conda_cos7-linux-gnu/
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Perfect! We found it. 👍 The output bin/ inside installer_files/env/ confirms that the activation script is indeed located at installer_files/env/bin/activate. The reason the previous command failed was likely due to a subtle shell issue or a cached path. Let's try activating it again, ensuring the correct syntax. Final Attempt to Fix Oobabooga Dependencies Ensure you're still in your ~/text-generation-webui directory in the second WSL2 terminal. Your prompt should be: (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ Explicitly activate Oobabooga's virtual environment. Use this exact command: source ./installer_files/env/bin/activate The ./ at the beginning ensures that source looks for the script relative to your current directory. After this, your terminal prompt should change to include (env) or (base) with (env) in front (e.g., (env) (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$). This change is critical as it indicates you're now operating within Oobabooga's isolated Python environment. Install all required packages from Oobabooga's requirements.txt file. Since you are now in the correct environment, this command will install gradio and any other missing dependencies precisely where they need to be. pip install -r requirements.txt Let this command run completely. It will display a lot of output as it downloads and installs packages. It might take several minutes depending on what's missing. Once the pip install command finishes, deactivate the virtual environment. deactivate Your prompt should revert to (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Now, restart Oobabooga with your model and API. python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf --api Crucially, watch this terminal window. This time, you should see messages indicating the model is actually being loaded. This is the big file (several GBs) being loaded into RAM or VRAM, so it will take a moment, with progress indicators (e.g., percentages, kv cache details). Wait patiently for the model to fully load. You will eventually see the familiar Uvicorn running on http://127.0.0.1:5000 message. This confirms the API is ready and the model is loaded. Next Action Please perform these steps in your second WSL2 terminal and paste the complete output, especially from the source command, the pip install command, and the final python server.py command showing the model loading. This is the last hurdle before we can test your RAG system!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]