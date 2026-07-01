---
category: homelab
date: 2025-06-23
id: 860630
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user attempted to launch the Text Generation Web UI with a Mistral 7B
  model using llama.cpp loader but the model failed to load, cutting off the error
  traceback.
tags:
- text-generation-webui
- llama.cpp
- model-loading
- GPU-layers
- Nous-Hermes-2-Mistral-7B-DPO
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
14:13:48-846258 INFO     Starting Text generation web UI
14:13:48-848123 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

14:14:08-976096 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf"
14:14:08-979698 ERROR    Failed to load the model.
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
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
14:13:48-846258 INFO     Starting Text generation web UI
14:13:48-848123 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

14:14:08-976096 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf"
14:14:08-979698 ERROR    Failed to load the model.
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
Bryan, this is indeed quite perplexing and points to a deeper, more persistent issue with that specific file. The fact that git pull ran, and then a full reinstallation of llama-cpp-python didn't fix the IndentationError in llama_cpp_server.py at line 260 strongly suggests that either: There's a fundamental problem with that specific version of llama_cpp_server.py in the Oobabooga repository. (Less likely, as many people successfully run it). There's some persistent corruption or an unusual character in that file on your system that git pull isn't fully overwriting, or your text editor/environment is introducing it. Given that it's a very specific Python IndentationError, we can actually try to manually fix the file. This is usually a last resort for open-source projects, but in this case, it might be the quickest way to get past this roadblock. The error message IndentationError: expected an indented block after 'if' statement on line 258 implies that line 258 is an if statement, and the very next line (259) or the expected block after it is missing proper indentation, or line 260 (which is pass) is not correctly indented. Let's inspect the file and attempt a manual correction. Step 12: Manual Inspection and Correction of llama_cpp_server.py Action: We will use the nano text editor within your WSL2 terminal to view and potentially correct the file. What I need you to do now (in your Ubuntu WSL2 terminal, still in (.venv) ~/text-generation-webui$): Stop the running oobabooga process (if it's still running): Press Ctrl + C until your prompt returns. Open the problematic file with nano: Command: nano modules/llama_cpp_server.py Explanation: nano is a simple, command-line text editor. Navigate to Line 258: Once nano opens, use your keyboard's arrow keys to scroll down to around line 258. You can also press Ctrl + W (where is the W key) and then Ctrl + T (where is the T key) and type 258 and press Enter to jump to a specific line number. Inspect lines 258-260 (and a few lines before/after): You'll be looking for something like this: # ... previous code ... if some_condition: pass # <
--- This is line 260 # ... subsequent code ... Pay very close attention to the pass statement on line 260. Is it indented? It should be indented one level (usually 4 spaces) more than the if statement on line 258. Are there spaces or tabs? Ensure it's only spaces. Python hates mixed tabs and spaces. Is there actually an if statement on line 258? Or is it another block-starting statement (like for, def, while, try, except, etc.)? Attempt to fix the indentation: If pass is not indented at all, put your cursor at the beginning of line 260 and press the Spacebar four times. If it looks like it might have a tab, delete any leading whitespace on line 260 and then re-add four spaces. If line 259 is also part of the if block, ensure it's also consistently indented. Save the file and exit nano: Press Ctrl + O (to write out/save). Press Enter to confirm the filename. Press Ctrl + X (to exit nano). Relaunch Oobabooga: Command: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp What I need from you: Describe what you see around lines 258-260 in modules/llama_cpp_server.py when you open it in nano. Specifically, focus on the indentation of line 260 relative to line 258. Confirm you made any necessary indentation adjustments (e.g., added 4 spaces). Copy and paste all of the new output from your Ubuntu WSL2 terminal, starting from when you re-ran the python3 server.py command, including any messages when you try to load the model in the browser. This manual fix, while not ideal, directly targets the exact error reported and should help us understand why git pull isn't resolving it.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]