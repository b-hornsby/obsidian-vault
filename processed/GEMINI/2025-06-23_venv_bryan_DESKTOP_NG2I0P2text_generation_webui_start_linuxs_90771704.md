---
category: homelab
date: 2025-06-23
id: 140108
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user is trying to load a quantized GGUF model in text-generation-webui
  with GPU offloading but encountering a model loading failure, likely due to configuration
  or compatibility issues with the llama.cpp backend.
tags:
- text-generation-webui
- llama.cpp
- model-loading
- gpu-configuration
- local-llm
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ./start_linux.sh --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
14:27:45-444845 INFO     Starting Text generation web UI
14:27:45-446603 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

14:28:19-619363 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf"
14:28:19-624726 ERROR    Failed to load the model.
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
    import llama_cpp
ModuleNotFoundError: No module named 'llama_cpp'

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ./start_linux.sh --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
14:27:45-444845 INFO     Starting Text generation web UI
14:27:45-446603 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

14:28:19-619363 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf"
14:28:19-624726 ERROR    Failed to load the model.
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
    import llama_cpp
ModuleNotFoundError: No module named 'llama_cpp'

### GEMINI
Bryan, this is a very confusing and frustrating turn of events, and I sincerely apologize for the back-and-forth. The error ModuleNotFoundError: No module named 'llama_cpp' is directly contradictory to our previous step where pip install --force-reinstall --no-cache-dir llama-cpp-python successfully completed. This kind of error, appearing after a successful installation, often points to: A virtual environment issue: Something is preventing the Python interpreter from finding the installed llama_cpp module within the active virtual environment. An issue with start_linux.sh: The script might be deactivating/reactivating the virtual environment in a way that causes this, or it's not correctly passing the environment. A deeper system-level Python path problem: Less likely given we're in a venv, but possible. Let's try a very specific diagnostic step. We need to confirm that llama_cpp is indeed installed within your active virtual environment and that the Python interpreter can find it. Step 18: Verify llama_cpp Installation and Path Action: We will manually check the Python environment. What I need you to do now (in your Ubuntu WSL2 terminal): Stop the running oobabooga process (if it's still running): Press Ctrl + C until your prompt returns. Confirm your virtual environment is active: Your prompt must still be (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. If it's not, reactivate it with source .venv/bin/activate. Launch a Python interpreter within the virtual environment: Command: python3 You should see a prompt like >>>. Attempt to import llama_cpp: Command (inside the >>> prompt): import llama_cpp Press Enter. If the import works (no error): Command (inside the >>> prompt): llama_cpp.__version__ Press Enter. Command (inside the >>> prompt): llama_cpp.__file__ Press Enter. Then exit the Python interpreter: exit() Press Enter. If the import fails (gives ModuleNotFoundError): Then type exit() and press Enter to leave the Python interpreter. This would indicate a very serious issue with the pip installation within the virtual environment. What I need from you: Copy and paste the entire output of the steps above (starting from python3, including the import attempt and __version__/__file__ if it works, or the ModuleNotFoundError if it fails, and the exit()). This will tell us definitively if the llama_cpp module is correctly installed and discoverable by Python within that virtual environment. Depending on the outcome, our next steps will be much clearer.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]