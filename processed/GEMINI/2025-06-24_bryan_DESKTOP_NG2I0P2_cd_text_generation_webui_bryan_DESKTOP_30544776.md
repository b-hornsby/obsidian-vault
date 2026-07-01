---
category: ai-tools
date: 2025-06-24
id: 661176
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: partial
sentiment: building
source: GEMINI
summary: The user is setting up a local AI environment by cloning the llama.cpp repository
  within the text-generation-webui project structure, indicating early-stage deployment
  of a local language model infrastructure.
tags:
- llama.cpp
- text-generation-webui
- local-ai
- model-deployment
- homelab
---
# bryan_@DESKTOP-NG2I0P2:~$ cd text-generation-webui
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ mkdir -p repositories
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cd repositories
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories$ git clone https://github.com/ggerganov/llama.cpp.git
Cloning into 'llama.cpp'...
remote: Enumerating objects: 54590, done.
remote: Counting objects: 100% (83/83), done.
remote: Compressing objects: 100% (69/69), done.
remote: Total 54590 (delta 47), reused 16 (delta 14), pack-reused 54507 (from 4)
Receiving objects: 100% (54590/54590), 129.99 MiB | 57.37 MiB/s, done.
Resolving deltas: 100% (39687/39687), done.
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories$ cd llama.cpp
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp$ make LLAMA_CUBLAS=1
Makefile:2: *** The Makefile build is deprecated. Use the CMake build instead. For more details, see https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md.  Stop.
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp$

### USER
bryan_@DESKTOP-NG2I0P2:~$ cd text-generation-webui
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ mkdir -p repositories
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cd repositories
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories$ git clone https://github.com/ggerganov/llama.cpp.git
Cloning into 'llama.cpp'...
remote: Enumerating objects: 54590, done.
remote: Counting objects: 100% (83/83), done.
remote: Compressing objects: 100% (69/69), done.
remote: Total 54590 (delta 47), reused 16 (delta 14), pack-reused 54507 (from 4)
Receiving objects: 100% (54590/54590), 129.99 MiB | 57.37 MiB/s, done.
Resolving deltas: 100% (39687/39687), done.
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories$ cd llama.cpp
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp$ make LLAMA_CUBLAS=1
Makefile:2: *** The Makefile build is deprecated. Use the CMake build instead. For more details, see https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md.  Stop.
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp$

### GEMINI
Excellent! You have successfully manually cloned llama.cpp into the repositories directory. This is a significant step forward, as llama.cpp is now present in the expected location. The make LLAMA_CUBLAS=1 command failed, but it gave us a very clear and helpful message: Makefile:2: *** The Makefile build is deprecated. Use the CMake build instead. This means that the llama.cpp project has updated its build system. We need to use CMake instead of make directly for compilation. Step 37: Build llama.cpp using CMake (with CUBLAS) We will now use the correct CMake commands to build llama.cpp with GPU (CUBLAS) acceleration. Action: Ensure you are in the ~/text-generation-webui/repositories/llama.cpp directory. (Your prompt confirms this). Create a build directory (standard practice for CMake projects): mkdir build Navigate into the build directory: cd build Configure the build with CMake, enabling CUBLAS: cmake .. -DLLAMA_CUBLAS=ON The .. tells CMake to look for the CMakeLists.txt file in the parent directory (llama.cpp). -DLLAMA_CUBLAS=ON explicitly enables GPU acceleration. Build the project: cmake --build . --config Release cmake --build . tells CMake to build the project in the current directory. --config Release builds an optimized release version. This step will compile llama.cpp and might take several minutes. Please provide the full output of each of these commands. This build process is crucial for llama.cpp to function.