---
category: homelab
date: 2025-06-23
id: 844876
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: unresolved
sentiment: curious
source: GEMINI
summary: The user was attempting to load a quantized Mistral model via text-generation-webui
  but encountered an error during model loading, indicating a failure in initializing
  the Nous-Hermes-2-Mistral-7B-DPO model.
tags:
- local-ai
- model-loading
- text-generation
- troubleshooting
- gguf
---
# 14:21:24-003826 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf"
14:21:24-006235 ERROR    Failed to load the model.
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
        ^
IndentationError: unindent does not match any outer indentation level

### USER
14:21:24-003826 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf"
14:21:24-006235 ERROR    Failed to load the model.
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
        ^
IndentationError: unindent does not match any outer indentation level

### GEMINI
This is incredibly stubborn! My apologies, Bryan. The IndentationError: unindent does not match any outer indentation level is Python's way of saying "the spacing on this line is messed up compared to the lines above it." This means that even after our previous fix attempts, the indentation on line 260 (which was the pass statement, or now the line where the pass statement was) is still not perfectly aligned, or there's a mix of tabs and spaces, or some other invisible character. Let's be extremely meticulous about this specific line. We're going to try to delete it entirely and re-add it with known good spacing. Step 14: Thoroughly Fix Indentation on Line 260 of llama_cpp_server.py Action: We will manually correct the line, ensuring perfect indentation with spaces. What I need you to do now (in your Ubuntu WSL2 terminal, still in (.venv) ~/text-generation-webui$): Stop the running oobabooga process (if it's still running): Press Ctrl + C until your prompt returns. Open modules/llama_cpp_server.py with nano: Command: nano modules/llama_cpp_server.py Navigate to the relevant section (around line 258-260). You should see something like this now (with or without the pass): if self.server_path is None: self.server_path = llama_cpp.get_binary_path() pass # Or this line might be gone, if you removed it. Focus on the line self.server_path = llama_cpp.get_binary_path(). The Fix - Extreme Indentation Cleanup: Go to the very beginning of the line: self.server_path = llama_cpp.get_binary_path() Press your Left Arrow key all the way to the very first character on that line. Press the Backspace key repeatedly until the line is completely against the left edge of the editor (no leading spaces or tabs at all). Now, from the very left edge, add exactly eight (8) spaces (four spaces for the if block, and another four for the content inside the if). So, you will transform: if self.server_path is None: self.server_path = llama_cpp.get_binary_path() # <
--- focus here into: if self.server_path is None: self.server_path = llama_cpp.get_binary_path() # <
--- after backspacing and adding 8 spaces (Note: nano will likely auto-indent the if and pass/self.server_path lines based on what's before it, so be precise with how many spaces you are adding to that specific line after clearing it.) Verify the indentation of the if statement itself. The if statement on line 258 should have 4 spaces before it. The line self.server_path = llama_cpp.get_binary_path() (what was line 259/260 depending on if pass was removed) needs to be 4 spaces further in than the if statement. So, if the if is at 4 spaces, the self.server_path line needs to be at 8 spaces. Final check of the block: # ... code above ... def _start_server(self): # This line likely has 4 spaces of indentation """Start the llama.cpp server and wait until it's ready.""" # This line likely has 8 spaces of indentation # Determine the server path if self.server_path is None: # This line should have 8 spaces of indentation self.server_path = llama_cpp.get_binary_path() # THIS LINE MUST HAVE 12 SPACES OF INDENTATION # If you still have 'pass' after this, it should also have 12 spaces. # ... subsequent code ... Let's aim for this exact structure, where _start_server is at 4, if is at 8, and self.server_path is at 12 spaces. Save the file and exit nano: Press Ctrl + O (to write out/save). Press Enter to confirm the filename. Press Ctrl + X (to exit nano). Relaunch Oobabooga: Command: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp What I need from you: Confirm you have manually aligned the self.server_path = llama_cpp.get_binary_path() line with 12 spaces of indentation (relative to the file start) and saved the file. Copy and paste all of the new output from your Ubuntu WSL2 terminal, starting from when you re-ran the python3 server.py command, including any messages when you try to load the model in the browser. This is the most precise we can be about indentation. If this fails, we might need to consider a fresh install of the oobabooga repository itself. But let's try this surgical fix first.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]