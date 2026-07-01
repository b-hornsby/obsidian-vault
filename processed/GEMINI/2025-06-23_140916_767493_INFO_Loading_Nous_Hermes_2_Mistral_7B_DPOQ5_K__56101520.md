---
category: homelab
date: 2025-06-23
id: 065582
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user encountered an error while trying to load the Nous-Hermes-2-Mistral-7B-DPO
  model in text-generation-webui, with the model failing to load due to an incomplete
  traceback error.
tags:
- local-ai
- model-loading
- text-generation-webui
- mistral-model
- gguf
---
# 14:09:16-767493 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf"
14:09:16-770839 ERROR    Failed to load the model.
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/modules/ui_model_menu.py", line 196, in load_model_wrapper
    shared.model, shared.tokenizer = load_model(selected_model, loader)
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/modules/models.py", line 42, in load_model
    output = load_func_map[loader](model_name)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/modules/models.py", line 65, in llama_cpp_server_loader
    from modules.llama_cpp_server import LlamaServer
  File "/home/bryan_/text-generation-webui/modules/llama_cpp_server.py", line 260
    pass
    ^^^^
IndentationError: expected an indented block after 'if' statement on line 258

### USER
14:09:16-767493 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf"
14:09:16-770839 ERROR    Failed to load the model.
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/modules/ui_model_menu.py", line 196, in load_model_wrapper
    shared.model, shared.tokenizer = load_model(selected_model, loader)
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/modules/models.py", line 42, in load_model
    output = load_func_map[loader](model_name)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/modules/models.py", line 65, in llama_cpp_server_loader
    from modules.llama_cpp_server import LlamaServer
  File "/home/bryan_/text-generation-webui/modules/llama_cpp_server.py", line 260
    pass
    ^^^^
IndentationError: expected an indented block after 'if' statement on line 258

### GEMINI
Alright, Bryan. This is frustrating, I agree. We've hit the exact same IndentationError again, even after the git pull. This strongly suggests one of two things: The git pull didn't fully resolve the specific file's state. Sometimes, local changes or permissions issues can prevent a perfect merge. There might be a lingering issue with the Python environment, or a specific version dependency conflict that git pull doesn't address. Given that git pull reported fetching objects and then "Already up to date.", it implies it tried to update. However, an IndentationError is purely a syntax issue. Let's try a more aggressive but standard approach: recompiling the llama.cpp bindings and making absolutely sure the environment is clean. Step 10: Rebuild Llama.cpp Bindings and Clean Environment The llama.cpp part of oobabooga relies on Python bindings that are often compiled. If there's an issue there, or with the Python environment's understanding of the compiled components, it can lead to weird issues. We'll also try forcing a clean reinstallation of llama-cpp-python. Action: We will first manually remove and then reinstall the llama-cpp-python library, and then attempt to re-launch. What I need you to do now (in your Ubuntu WSL2 terminal, you should still be in (.venv) ~/text-generation-webui$): Stop the running oobabooga process (if it's still running): Go to your Ubuntu WSL2 terminal. Press Ctrl + C (you might need to press it once or twice). Ensure your prompt (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ is back. Deactivate the virtual environment: Command: deactivate Explanation: This will exit your virtual environment. Your prompt should change back to bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. We do this to ensure no lingering processes are tied to the old environment. Clean out old llama_cpp_python components (optional but recommended for stubborn issues): Command: rm -rf .venv/lib/python*/site-packages/llama_cpp_python* Explanation: This command is a bit more aggressive. It uses rm -rf (remove recursively and forcefully) to delete any existing llama_cpp_python installations or related files from your virtual environment's site-packages directory. The * is a wildcard for your Python version (e.g., python3.10). This ensures a fresh install. Reactivate the virtual environment: Command: source .venv/bin/activate Your prompt should now show (.venv) again. Reinstall llama-cpp-python with CUDA support: We need to ensure it's specifically built to use your GPU. Command: pip install --force-reinstall --no-cache-dir llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/wheels/cu118 Explanation: --force-reinstall: Forces pip to uninstall and then reinstall the package. --no-cache-dir: Prevents pip from using cached versions, ensuring a fresh download. llama-cpp-python: The package itself. --extra-index-url https://abetlen.github.io/llama-cpp-python/wheels/cu118: This is crucial! It tells pip to look for pre-compiled wheels (binaries) of llama-cpp-python that are built with CUDA 11.8 support. This is the most common CUDA version for NVIDIA GPUs in WSL2. This should ensure it uses your RTX 3070. Relaunch Oobabooga: Command: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp What I need from you: Confirm you stopped the server and deactivated the environment. Run the rm -rf command (and confirm it ran without output or errors). Reactivate the virtual environment and confirm the prompt change. Run the pip install --force-reinstall ... command. Copy and paste the entire output of this command here. This will take a few minutes. After it finishes, run the python3 server.py ... command. Copy and paste all of the new output from your Ubuntu WSL2 terminal, starting from the python3 server.py command, including any messages when you try to load the model in the browser. This is a more thorough reset of the llama.cpp part, which is the most likely culprit for that specific Python error when loading the model.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]