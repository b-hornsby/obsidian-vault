---
id: 615073
source: GEMINI
date: 2025-06-25
tags: ['coding', 'llm', 'ai', 'gemini', 'model', 'oobabooga', 'llama.cpp', 'gguf']
category: coding
sentiment: executing
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# did everything up to load and got: Downloading Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf to user_data/models

Download of 1 files to user_data/models completed.
12:55:03-829386 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf"
12:55:03-834672 INFO     Using gpu_layers=17 | ctx_size=8192 | cache_type=fp16
/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/llama_cpp_binaries/bin/llama-server: /home/bryan_/miniconda3/envs/llm-assist/lib/libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/llama_cpp_binaries/bin/llama-server)
12:55:04-837477 ERROR    Error loading the model with llama.cpp: Server process terminated unexpectedly with exit code:
                         1
 

### USER
did everything up to load and got: Downloading Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf to user_data/models

Download of 1 files to user_data/models completed.
12:55:03-829386 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf"
12:55:03-834672 INFO     Using gpu_layers=17 | ctx_size=8192 | cache_type=fp16
/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/llama_cpp_binaries/bin/llama-server: /home/bryan_/miniconda3/envs/llm-assist/lib/libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/llama_cpp_binaries/bin/llama-server)
12:55:04-837477 ERROR    Error loading the model with llama.cpp: Server process terminated unexpectedly with exit code:
                         1
 

### GEMINI
Ah, it looks like we've hit a new error, but it's a very specific one: GLIBCXX_3.4.30' not found. This error indicates a mismatch or an outdated version of the C++ standard library (libstdc++.so.6) that llama-server (which is part of the llama-cpp-python installation within Oobabooga's environment) is trying to use. It's looking for a version of GLIBCXX that is newer than what it found in the specified path. The key part of the error is: /home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/llama_cpp_binaries/bin/llama-server: /home/bryan_/miniconda3/envs/llm-assist/lib/libstdc++.so.6: version GLIBCXX_3.4.30' not found (required by /home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/llama_cpp_binaries/bin/llama-server)` This suggests that llama-server (which Oobabooga just compiled in its new environment) is trying to link against a libstdc++.so.6 found in your old llm-assist environment (/home/bryan_/miniconda3/envs/llm-assist/lib/libstdc++.so.6), and that specific library doesn't have the required version GLIBCXX_3.4.30. This is exactly why we went through the "one-click installer" for Oobabooga – to avoid these kinds of cross-environment conflicts! It seems there might be an environment variable or path lingering that's causing llama-server to look outside its own dedicated environment. Let's try to resolve this by ensuring Oobabooga's environment is truly isolated. Here's the plan: Clean up potential lingering environment variables: Sometimes, previous export commands (like LD_LIBRARY_PATH from our llm-assist troubleshooting) can persist or interfere. We need to start fresh. Ensure Oobabooga's llama-cpp-python is correctly linked within its own environment. Steps to resolve: A. Terminate the current Oobabooga session and restart your WSL2 terminal: In the WSL2 terminal where Oobabooga is running: Press Ctrl + C multiple times until the process terminates and you get back to your prompt (e.g., (textgen) bryan_@DESKTOP-NG2I0P2:~$ or (base) bryan_@DESKTOP-NG2I0P2:~$). Close the current WSL2 terminal window completely. This is important to clear any lingering session-specific environment variables. Open a brand new WSL2 terminal window. B. Navigate back to Oobabooga and re-run the setup script (which also runs the server): In the new WSL2 terminal, navigate to the Oobabooga directory: cd ~/text-generation-webui Run the start_linux.sh script again. ./start_linux.sh This script will re-activate its internal Conda environment, run any updates if needed, and then attempt to launch the web UI again. By restarting the terminal and using start_linux.sh, we're giving the Oobabooga environment the best chance to self-correct its paths and linking. Wait for Oobabooga to start up fully and confirm the URL http://127.0.0.1:7860. Then, go back to your web browser and try to load the model again. This GLIBCXX error often happens when an executable compiled for a newer C++ standard tries to run with an older libstdc++. By restarting the terminal and using Oobabooga's start_linux.sh, we are attempting to ensure it uses the libstdc++ version that's compatible with its own compiled llama-server binary, which should reside within ~/text-generation-webui/installer_files/env/lib/.