---
category: ai-tools
date: 2025-06-23
id: 658579
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
- homelab-stack
- private-ai-consulting
resolution: partial
sentiment: executing
source: GEMINI
summary: The user was updating their text-generation-webui to the latest dev branch,
  cleaning cache, and attempting to start the server with a custom model directory.
tags:
- text-generation-webui
- model-management
- git-update
- python-environment
- local-llm
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ deactivate
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ git reset --hard origin/dev
HEAD is now at 9a589648 Keep the last message visible when the input height changes
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ find . -name "__pycache__" -exec rm -rf {} +
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ source .venv/bin/activate
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
14:32:29-627010 INFO     Starting Text generation web UI
14:32:29-629042 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

14:32:44-537010 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf"
14:32:44-541075 ERROR    Failed to load the model.
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/modules/ui_model_menu.py", line 196, in load_model_wrapper
    shared.model, shared.tokenizer = load_model(selected_model, loader)
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/modules/models.py", line 42, in load_model
    output = load_func_map[loader](model_name)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/modules/models.py", line 65, in llama_cpp_server_loader
    from modules.llama_cpp_server import LlamaServer
  File "/home/bryan_/text-generation-webui/modules/llama_cpp_server.py", line 12, in <module>
    import llama_cpp_binaries
ModuleNotFoundError: No module named 'llama_cpp_binaries'

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ deactivate
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ git reset --hard origin/dev
HEAD is now at 9a589648 Keep the last message visible when the input height changes
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ find . -name "__pycache__" -exec rm -rf {} +
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ source .venv/bin/activate
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
14:32:29-627010 INFO     Starting Text generation web UI
14:32:29-629042 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

14:32:44-537010 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf"
14:32:44-541075 ERROR    Failed to load the model.
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/modules/ui_model_menu.py", line 196, in load_model_wrapper
    shared.model, shared.tokenizer = load_model(selected_model, loader)
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/modules/models.py", line 42, in load_model
    output = load_func_map[loader](model_name)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/modules/models.py", line 65, in llama_cpp_server_loader
    from modules.llama_cpp_server import LlamaServer
  File "/home/bryan_/text-generation-webui/modules/llama_cpp_server.py", line 12, in <module>
    import llama_cpp_binaries
ModuleNotFoundError: No module named 'llama_cpp_binaries'

### GEMINI
Okay, Bryan, this is progress! The IndentationError is definitely gone, which confirms that our forceful reset and cache clearing worked to get a clean set of files. However, we have a new ModuleNotFoundError: No module named 'llama_cpp_binaries'. This is a very specific error and it tells us that the Oobabooga codebase, after the git reset, has updated its requirements for how it finds the llama.cpp server executable. It no longer just relies on llama_cpp.get_binary_path(); it now expects a separate module called llama_cpp_binaries to handle that. This module is likely a new dependency or a component that needs to be specifically installed or built by Oobabooga's setup process. Step 20: Install the New llama_cpp_binaries Dependency Since git reset --hard pulled the latest code, it's highly probable that the requirements/full/requirements.txt file (which we successfully used before) has been updated to include this new dependency. We need to run the pip install command again to pick up any new requirements. Action: Re-install all dependencies from requirements/full/requirements.txt to ensure llama_cpp_binaries (or whatever pulls it in) is installed. What I need you to do now (in your Ubuntu WSL2 terminal, still in (.venv) ~/text-generation-webui$): Stop the running oobabooga process (if it's still running): Press Ctrl + C until your prompt returns. Re-install all dependencies from the full requirements file: Command: pip install -r requirements/full/requirements.txt Explanation: This will re-evaluate all dependencies in the full.txt file. pip is smart enough not to reinstall things that are already correctly installed, but it will install any new packages that have been added to that file since your last installation. llama_cpp_binaries is likely one of them. Relaunch Oobabooga: After the pip install completes, we'll try launching it again with the same command. Command: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp What I need from you: Confirm you stopped the server. Run the pip install -r requirements/full/requirements.txt command. Copy and paste the entire output of this command here. This might take a few moments if new packages are downloaded. After it finishes, run the python3 server.py ... command again. Copy and paste all of the new output from your Ubuntu WSL2 terminal, starting from the python3 server.py command, including any messages when you try to load the model in the browser. This should hopefully install the missing module and get us past this new error!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]