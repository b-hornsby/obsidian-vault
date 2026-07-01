---
category: homelab
date: 2025-06-24
id: 873029
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: partial
sentiment: stuck
source: GEMINI
summary: The user is trying to build llama.cpp with CUDA support on their local machine
  but encountered a deprecated Makefile build system and is transitioning to the CMake
  build process.
tags:
- llama.cpp
- CUDA
- CMake
- build-errors
- local-llm
---
# bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories$ cd llama.cpp
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp$ make LLAMA_CUBLAS=1
Makefile:2: *** The Makefile build is deprecated. Use the CMake build instead. For more details, see https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md.  Stop.
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp$ mkdir build
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp$ cd build
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$ cmake .. -DLLAMA_CUBLAS=ON
-- The C compiler identification is GNU 13.3.0
-- The CXX compiler identification is GNU 13.3.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found Git: /usr/bin/git (found version "2.43.0")
CMake Error at CMakeLists.txt:116 (message):
  LLAMA_CUBLAS is deprecated and will be removed in the future.

  Use GGML_CUDA instead

Call Stack (most recent call first):
  CMakeLists.txt:121 (llama_option_depr)


-- Configuring incomplete, errors occurred!
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$

### USER
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories$ cd llama.cpp
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp$ make LLAMA_CUBLAS=1
Makefile:2: *** The Makefile build is deprecated. Use the CMake build instead. For more details, see https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md.  Stop.
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp$ mkdir build
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp$ cd build
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$ cmake .. -DLLAMA_CUBLAS=ON
-- The C compiler identification is GNU 13.3.0
-- The CXX compiler identification is GNU 13.3.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found Git: /usr/bin/git (found version "2.43.0")
CMake Error at CMakeLists.txt:116 (message):
  LLAMA_CUBLAS is deprecated and will be removed in the future.

  Use GGML_CUDA instead

Call Stack (most recent call first):
  CMakeLists.txt:121 (llama_option_depr)


-- Configuring incomplete, errors occurred!
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$

### GEMINI
You're getting excellent, precise error messages, which helps a lot! The cmake command failed because LLAMA_CUBLAS is now a deprecated flag for enabling CUDA. The message explicitly tells you: Use GGML_CUDA instead. This means llama.cpp has updated its build options for GPU support. Step 37 (Revised): Configure llama.cpp build with CMake using GGML_CUDA Action: Ensure you are still in the ~/text-generation-webui/repositories/llama.cpp/build directory. (Your prompt confirms this). Re-run CMake with the correct flag -DGGML_CUDA=ON: cmake .. -DGGML_CUDA=ON This should now successfully configure the build. Build the project (if CMake configuration is successful): cmake --build . --config Release This step will compile llama.cpp. It might still take several minutes. Please provide the full output of both these commands. If the cmake .. -DGGML_CUDA=ON step completes without errors, the build should then proceed.