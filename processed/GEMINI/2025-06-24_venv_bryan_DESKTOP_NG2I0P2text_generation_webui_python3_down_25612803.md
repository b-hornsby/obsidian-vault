---
id: 806113
source: GEMINI
date: 2025-06-24
tags: ['coding', 'module', 'ai', 'gemini', 'model', 'oobabooga', 'llama.cpp', 'text-generation']
category: coding
sentiment: building
resolution: partial
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 download-model.py --llama-cpp
usage: download-model.py [-h] [--branch BRANCH] [--threads THREADS] [--text-only] [--specific-file SPECIFIC_FILE]
                         [--exclude-pattern EXCLUDE_PATTERN] [--output OUTPUT] [--model-dir MODEL_DIR] [--clean]
                         [--check] [--max-retries MAX_RETRIES]
                         [MODEL]
download-model.py: error: unrecognized arguments: --llama-cpp
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 download-model.py --llama-cpp
usage: download-model.py [-h] [--branch BRANCH] [--threads THREADS] [--text-only] [--specific-file SPECIFIC_FILE]
                         [--exclude-pattern EXCLUDE_PATTERN] [--output OUTPUT] [--model-dir MODEL_DIR] [--clean]
                         [--check] [--max-retries MAX_RETRIES]
                         [MODEL]
download-model.py: error: unrecognized arguments: --llama-cpp
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
You are absolutely right to point this out, and my apologies again for these path issues! The error download-model.py: error: unrecognized arguments: --llama-cpp indicates that the download-model.py script in your current text-generation-webui version does not support the --llama-cpp argument. This means llama.cpp is handled differently in your specific version of the web UI. Given that: llama.cpp/ does not exist at the root. extensions/webui_llama_cpp/ does not exist. download-model.py doesn't have the --llama-cpp flag. It's highly likely that llama.cpp is intended to be integrated differently in your version of Oobabooga's web UI. Often, it's included as a Git submodule or its build process is part of a more general setup script that you might have bypassed by manually creating the virtual environment. Let's check for the most common location for llama.cpp in newer versions of the web UI when it's integrated as a submodule. Step 32: Check for llama.cpp in the repositories directory Action: List the contents of the repositories directory: ls -l repositories/ If llama.cpp is a submodule, it's usually cloned into this directory. Please provide the output of ls -l repositories/. This will help us determine the next steps for getting llama.cpp set up, or if we need to consider alternative loaders for now.