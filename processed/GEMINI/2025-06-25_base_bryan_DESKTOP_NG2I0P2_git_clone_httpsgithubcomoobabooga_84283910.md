---
id: 630337
source: GEMINI
date: 2025-06-25
tags: ['coding', 'gemini', 'oobabooga', 'text-generation', 'python', 'script', 'git', 'github']
category: coding
sentiment: executing
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# (base) bryan_@DESKTOP-NG2I0P2:~$ git clone https://github.com/oobabooga/text-generation-webui.git
Cloning into 'text-generation-webui'...
remote: Enumerating objects: 23468, done.
remote: Counting objects: 100% (443/443), done.
remote: Compressing objects: 100% (79/79), done.
remote: Total 23468 (delta 413), reused 369 (delta 364), pack-reused 23025 (from 3)
Receiving objects: 100% (23468/23468), 30.00 MiB | 41.91 MiB/s, done.
Resolving deltas: 100% (16903/16903), done.
(base) bryan_@DESKTOP-NG2I0P2:~$

### USER
(base) bryan_@DESKTOP-NG2I0P2:~$ git clone https://github.com/oobabooga/text-generation-webui.git
Cloning into 'text-generation-webui'...
remote: Enumerating objects: 23468, done.
remote: Counting objects: 100% (443/443), done.
remote: Compressing objects: 100% (79/79), done.
remote: Total 23468 (delta 413), reused 369 (delta 364), pack-reused 23025 (from 3)
Receiving objects: 100% (23468/23468), 30.00 MiB | 41.91 MiB/s, done.
Resolving deltas: 100% (16903/16903), done.
(base) bryan_@DESKTOP-NG2I0P2:~$

### GEMINI
Great! You've successfully cloned the text-generation-webui repository. Now, you just need to cd into that directory and run the start_linux.sh script. Next Step: cd text-generation-webui ./start_linux.sh This command will initiate the "one-click" installation process, setting up Oobabooga's dedicated Conda environment and installing all its dependencies, including a CUDA-enabled llama-cpp-python within that new environment. Remember this step will take a significant amount of time due to large downloads and compilation.