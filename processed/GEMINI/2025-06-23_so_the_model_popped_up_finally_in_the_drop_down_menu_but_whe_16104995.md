---
category: homelab
date: 2025-06-23
id: 840191
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
- second-brain-vault
- streaming-rig
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user successfully loaded a model in text-generation-webui but encountered
  an error when pressing 'load' in WSL2, with the process stopping mid-log during
  model loading of 'Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf'.
tags:
- text-generation-webui
- llama.cpp
- WSL2
- model-loading
- GPU-layers
---
# so the model popped up finally in the drop down menu but when i press load, this pops up in wsl2: (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
14:03:54-851020 INFO     Starting Text generation web UI
14:03:54-853053 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

14:05:07-458801 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf"
14:05:07-463400 ERROR    Failed to load the model.
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
so the model popped up finally in the drop down menu but when i press load, this pops up in wsl2: (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
14:03:54-851020 INFO     Starting Text generation web UI
14:03:54-853053 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

14:05:07-458801 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf"
14:05:07-463400 ERROR    Failed to load the model.
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
Aha! Okay, this is a new type of error, but it's a Python error, not a setup or missing dependency error. That's good news, it means we're past the installation phase. The error: IndentationError: expected an indented block after 'if' statement on line 258 means there's a syntax error in one of Oobabooga's Python files (llama_cpp_server.py). Python is very strict about indentation. This usually happens for one of two reasons: A recent update to oobabooga's code introduced a bug. This is less likely but possible. A partial or corrupted update/pull of the repository. Sometimes, if a git pull or update didn't complete cleanly, a file can be left in an inconsistent state. Given that you just installed all the dependencies, it's possible that the core text-generation-webui code itself might need to be refreshed or updated. Step 9: Update Oobabooga's Text Generation WebUI Repository The best way to fix potential code inconsistencies is to pull the latest changes from the oobabooga GitHub repository. This will ensure you have the most up-to-date and hopefully bug-free version of the code. Action: We will use git pull to update your text-generation-webui directory. What I need you to do now (in your Ubuntu WSL2 terminal, you should still be in (.venv) ~/text-generation-webui$): Stop the running oobabooga process: You need to stop the current process before you can update the files. Go to your Ubuntu WSL2 terminal where oobabooga is running. Press Ctrl + C (hold down Ctrl and press C). You might need to press it once or twice. You should see output indicating the server is shutting down, and your prompt (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ should return. Update the repository: Command: git pull Explanation: git pull: This command fetches new commits from the remote repository (where oobabooga's code lives) and merges them into your local branch. This will update all the Python scripts and other files to their latest versions. Relaunch Oobabooga: After the git pull completes, we'll try launching it again with the same command. Command: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp What I need from you: Confirm you've stopped the server (Ctrl+C). Run the git pull command. Copy and paste the entire output of the git pull command here. (It will show which files were updated, if any). After git pull finishes, run the python3 server.py ... command again. Copy and paste all of the new output from your Ubuntu WSL2 terminal after trying to launch oobabooga (and then attempting to load the model in the browser again). This update should fix any minor code inconsistencies that could lead to an IndentationError. Let's get this resolved!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]