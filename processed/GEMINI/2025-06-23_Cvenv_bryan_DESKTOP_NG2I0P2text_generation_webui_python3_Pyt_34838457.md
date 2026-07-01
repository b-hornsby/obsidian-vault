---
category: homelab
date: 2025-06-23
id: 998449
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/coding.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: resolved
sentiment: exploratory
source: GEMINI
summary: The user was verifying that llama-cpp is properly installed in their Python
  virtual environment by checking its version (0.3.9) within the text-generation-webui
  project directory.
tags:
- llama-cpp
- python-environment
- local-ai
- version-check
- text-generation
---
# ^C(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3
Python 3.12.3 (main, Jun 18 2025, 17:59:45) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import llama_cpp
>>> llama_cpp.__version__
'0.3.9'
>>> exit()
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
^C(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3
Python 3.12.3 (main, Jun 18 2025, 17:59:45) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import llama_cpp
>>> llama_cpp.__version__
'0.3.9'
>>> exit()
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Okay, Bryan, this is critical information and it changes our diagnostic path significantly! Your output: >>> import llama_cpp >>> llama_cpp.__version__ '0.3.9' >>> exit() CONFIRMS that llama_cpp IS installed and accessible within your (.venv) virtual environment! This completely contradicts the ModuleNotFoundError you get when launching oobabooga. This situation (module imports fine in interpreter, but not when running the application) points to a more subtle issue, often related to: File corruption/encoding: Even after manual fixes, a very stubborn hidden character or encoding problem in modules/llama_cpp_server.py could still be present, causing the import to fail when that specific file is being processed by the main application. Conflicting environment variables or paths: Though less likely in a clean virtual environment. Python interpreter caching: Sometimes Python caches compiled .pyc files in __pycache__ directories, and if these are stale or corrupted, they can interfere. Given the history of the IndentationError in that exact file, let's try a forceful reset of your local oobabooga repository and clear Python caches. This is more aggressive than a simple git pull and ensures your files are pristine. Step 19: Forceful Repository Reset and Cache Clearing Action: We will reset your local oobabooga repository to match the remote, and then clear Python's internal caches to ensure no stale files are interfering. What I need you to do now (in your Ubuntu WSL2 terminal, still in (.venv) ~/text-generation-webui$): Stop the running oobabooga process (if it's still running): Press Ctrl + C until your prompt returns. Deactivate the virtual environment (important for clean reset): Command: deactivate Your prompt should change back to bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Forcefully reset your repository to the latest remote version: Command: git reset --hard origin/dev Explanation: This command is powerful. It will discard any and all local changes you've made to the files in the text-generation-webui directory and force them to exactly match the latest version available on the origin/dev branch. This will overwrite your manual fixes, but if they were the cause of a subtle problem (like a hidden character), this will eliminate it. Clean Python's __pycache__ directories: Command: find . -name "__pycache__" -exec rm -rf {} + Explanation: This command searches for all directories named __pycache__ within your current directory (.) and its subdirectories, then forcefully removes them. This ensures Python recompiles its bytecode files fresh. Reactivate the virtual environment: Command: source .venv/bin/activate Your prompt should now show (.venv) again. Re-launch Oobabooga (using python3 server.py directly, as start_linux.sh seemed to introduce new issues): Command: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp What I need from you: Confirm you stopped the server and deactivated the venv. Run the git reset --hard origin/dev command. Copy and paste its output. Run the find . -name "__pycache__" -exec rm -rf {} + command. (It usually has no output if successful). Reactivate the virtual environment and confirm the prompt change. Run the python3 server.py ... command. Copy and paste all of the new output from your Ubuntu WSL2 terminal, starting from the python3 server.py command, including any messages when you try to load the model in the browser. This is a very comprehensive cleanup. If this doesn't resolve the ModuleNotFoundError for llama_cpp, it suggests a much deeper, more unusual problem with your specific WSL2 installation or how Python is interacting with compiled libraries, which might require a full reinstall of WSL2 or Ubuntu itself, but let's not go there yet!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]