---
category: coding
date: 2025-06-24
id: 130572
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Test enrichment
tags:
- test
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cd ..
(.venv) bryan_@DESKTOP-NG2I0P2:~$ rm -rf text-generation-webui
(.venv) bryan_@DESKTOP-NG2I0P2:~$ git clone https://github.com/oobabooga/text-generation-webui.git --recursive
Cloning into 'text-generation-webui'...
remote: Enumerating objects: 23468, done.
remote: Counting objects: 100% (443/443), done.
remote: Compressing objects: 100% (77/77), done.
remote: Total 23468 (delta 413), reused 371 (delta 366), pack-reused 23025 (from 3)
Receiving objects: 100% (23468/23468), 30.01 MiB | 31.17 MiB/s, done.
Resolving deltas: 100% (16891/16891), done.
(.venv) bryan_@DESKTOP-NG2I0P2:~$ cd text-generation-webui
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cat .gitmodules
cat: .gitmodules: No such file or directory
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cd ..
(.venv) bryan_@DESKTOP-NG2I0P2:~$ rm -rf text-generation-webui
(.venv) bryan_@DESKTOP-NG2I0P2:~$ git clone https://github.com/oobabooga/text-generation-webui.git --recursive
Cloning into 'text-generation-webui'...
remote: Enumerating objects: 23468, done.
remote: Counting objects: 100% (443/443), done.
remote: Compressing objects: 100% (77/77), done.
remote: Total 23468 (delta 413), reused 371 (delta 366), pack-reused 23025 (from 3)
Receiving objects: 100% (23468/23468), 30.01 MiB | 31.17 MiB/s, done.
Resolving deltas: 100% (16891/16891), done.
(.venv) bryan_@DESKTOP-NG2I0P2:~$ cd text-generation-webui
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cat .gitmodules
cat: .gitmodules: No such file or directory
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
This is truly baffling. The output shows that your git clone --recursive command finished without errors, yet immediately after, cat .gitmodules still reports "No such file or directory". This is not how Git submodules are supposed to work. The .gitmodules file should definitely be present if the repository uses submodules and the clone was successful. This indicates a persistent and fundamental problem with Git's ability to clone the entire repository structure, specifically the submodules, in your environment (likely your WSL setup or network configuration). Since the .gitmodules file itself is missing, Git has no instructions on what submodules to download. Given that the text-generation-webui needs llama.cpp to use the --loader llama.cpp flag, and the automatic submodule cloning is failing, we will have to install llama.cpp manually. Step 36: Manually Clone and Build llama.cpp We will create the repositories directory (if it doesn't exist) and then clone llama.cpp directly into it, and build it, bypassing the main repository's submodule system. Action: Ensure your virtual environment is not active for these manual steps for a moment, as you're dealing with external binaries/compilation. (Your prompt (.venv) shows it is active, but for make commands it's less critical and you can keep it active). Create the repositories directory if it doesn't exist: mkdir -p repositories The -p flag ensures that if repositories already exists, it won't throw an error. Navigate into the repositories directory: cd repositories Clone the official llama.cpp repository into this directory: git clone https://github.com/ggerganov/llama.cpp.git This will create the llama.cpp directory inside repositories. Navigate into the newly cloned llama.cpp directory: cd llama.cpp Build llama.cpp with CUBLAS support (for GPU acceleration): make LLAMA_CUBLAS=1 This command will compile llama.cpp. This step might take a few minutes. You need to have make and a C/C++ compiler (like g++) installed on your system for this to work. If you encounter errors about make or g++ not found, you might need to install build-essential: sudo apt update && sudo apt install build-essential. Once make LLAMA_CUBLAS=1 completes successfully, the llama.cpp binaries will be compiled and ready. Then we can go back to the web UI root, recreate the virtual environment, and install Python dependencies. Please provide the full output of each of these commands.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]