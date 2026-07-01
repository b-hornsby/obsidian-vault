---
category: homelab
date: 2025-06-24
id: 193014
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: User encountered a CMake deprecation error when trying to build llama.cpp
  with CUDA support, indicating a configuration issue with the build setup.
tags:
- llama.cpp
- CUDA
- build-error
- CMake
- GPU-acceleration
---
# bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$ cmake .. -DGGML_CUDA=ON
CMake Error at CMakeLists.txt:116 (message):
  LLAMA_CUBLAS is deprecated and will be removed in the future.

  Use GGML_CUDA instead

Call Stack (most recent call first):
  CMakeLists.txt:121 (llama_option_depr)


-- Configuring incomplete, errors occurred!
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$

### USER
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$ cmake .. -DGGML_CUDA=ON
CMake Error at CMakeLists.txt:116 (message):
  LLAMA_CUBLAS is deprecated and will be removed in the future.

  Use GGML_CUDA instead

Call Stack (most recent call first):
  CMakeLists.txt:121 (llama_option_depr)


-- Configuring incomplete, errors occurred!
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$

### GEMINI
This is incredibly stubborn! It's very unusual for cmake to keep giving the exact same error about LLAMA_CUBLAS even after you've explicitly provided -DGGML_CUDA=ON. This suggests that CMake's internal cache or temporary files in the build directory might be "stuck" on the old configuration. To fix this, we need to completely clear the build directory's contents and then try the cmake command again. This will ensure CMake starts from a clean slate. Step 37 (Revised Again): Clear CMake Cache and Re-configure Build Action: Ensure you are still in the ~/text-generation-webui/repositories/llama.cpp/build directory. (Your prompt confirms this). Remove all contents of the build directory: rm -rf * This command will delete CMakeCache.txt and the CMakeFiles directory, which are CMake's cached configuration files. Re-run CMake with the correct flag -DGGML_CUDA=ON: cmake .. -DGGML_CUDA=ON This should now successfully configure the build. Build the project (if CMake configuration is successful): cmake --build . --config Release This step will compile llama.cpp. It might still take several minutes. Please provide the full output of each of these commands. Clearing the cache should resolve this persistent issue.

### GEMINI
It seems like the command you just ran cmake .. -DGGML_CUDA=ON produced the exact same error as before, still mentioning LLAMA_CUBLAS being deprecated. This is very strange, as the command you typed should have corrected that. It makes me suspect one of two things: You might have accidentally pasted the previous output again. There might be a very subtle typo, or an issue where CMake's cache isn't clearing properly, causing it to re-evaluate based on a previous state. Please, carefully re-type the command manually to ensure there are no hidden characters or typos, and then provide the full output. Action: Ensure you are still in the ~/text-generation-webui/repositories/llama.cpp/build directory. Manually type this exact command and press Enter: cmake .. -DGGML_CUDA=ON Provide the complete output you see after running this command. This is crucial for us to confirm the new flag is being correctly recognized.