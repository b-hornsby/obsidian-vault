---
category: homelab
date: 2025-06-24
id: 744703
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user is trying to compile llama.cpp with CUDA support in their local
  LLM setup but encountered a build error during the cmake configuration step and
  is seeking help diagnosing the issue.
tags:
- llama.cpp
- CUDA
- compilation
- build-errors
- local-llm
---
# so from: bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$ what do i need to fix this error: bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$ rm -rf *
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$ cmake .. -DGGML_CUDA=ON
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
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
-- Warning: ccache not found - consider installing it for faster compilation or disable this warning with GGML_CCACHE=OFF
-- CMAKE_SYSTEM_PROCESSOR: x86_64
-- GGML_SYSTEM_ARCH: x86
-- Including CPU backend
-- Found OpenMP_C: -fopenmp (found version "4.5")
-- Found OpenMP_CXX: -fopenmp (found version "4.5")
-- Found OpenMP: TRUE (found version "4.5")
-- x86 detected
-- Adding CPU backend variant ggml-cpu: -march=native
-- Could not find nvcc, please set CUDAToolkit_ROOT.
CMake Error at ggml/src/ggml-cuda/CMakeLists.txt:183 (message):
  CUDA Toolkit not found


-- Configuring incomplete, errors occurred!
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$

### USER
so from: bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$ what do i need to fix this error: bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$ rm -rf *
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$ cmake .. -DGGML_CUDA=ON
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
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
-- Warning: ccache not found - consider installing it for faster compilation or disable this warning with GGML_CCACHE=OFF
-- CMAKE_SYSTEM_PROCESSOR: x86_64
-- GGML_SYSTEM_ARCH: x86
-- Including CPU backend
-- Found OpenMP_C: -fopenmp (found version "4.5")
-- Found OpenMP_CXX: -fopenmp (found version "4.5")
-- Found OpenMP: TRUE (found version "4.5")
-- x86 detected
-- Adding CPU backend variant ggml-cpu: -march=native
-- Could not find nvcc, please set CUDAToolkit_ROOT.
CMake Error at ggml/src/ggml-cuda/CMakeLists.txt:183 (message):
  CUDA Toolkit not found


-- Configuring incomplete, errors occurred!
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$

### GEMINI
You are at bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$. The error CUDA Toolkit not found means that even though you're trying to build llama.cpp with GPU support (-DGGML_CUDA=ON), CMake cannot find the necessary NVIDIA CUDA development tools (like the nvcc compiler) installed within your WSL2 environment. To fix this, you need to install the NVIDIA CUDA Toolkit directly into your WSL2 Ubuntu distribution. Here are the steps you need to follow from your current position, which largely repeat and consolidate the instructions from my previous message for clarity: Step to Fix: Install NVIDIA CUDA Toolkit in WSL2 Navigate out of the build directory and then out of the llama.cpp directory: cd ../../.. This should take you back to your home directory: bryan_@DESKTOP-NG2I0P2:~/$. (Alternatively, you could use cd ~.) Install the CUDA Toolkit 11.8 for WSL-Ubuntu. First, clean up any old NVIDIA repository configurations and update apt: sudo rm -f /etc/apt/sources.list.d/cuda.list sudo apt update sudo apt autoremove --purge 'cuda*' 'nvidia*' # This removes old CUDA/NVIDIA packages sudo apt clean sudo apt autoclean sudo apt update # Update again after cleaning Next, download and add the NVIDIA GPG key and repository: wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600 wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb sudo dpkg -i cuda-keyring_1.1-1_all.deb Finally, install the CUDA Toolkit 11.8: sudo apt update sudo apt -y install cuda-toolkit-11-8 This command will download a lot of data and take a while. Please be patient and let it complete. Add CUDA to your system's PATH environment variable. This makes the nvcc compiler discoverable. echo 'export PATH=/usr/local/cuda-11.8/bin${PATH:+:${PATH}}' >> ~/.bashrc echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc source ~/.bashrc Verify the nvcc (CUDA Compiler) installation: nvcc --version You should see output indicating CUDA compilation tools and a version like V11.8.XX. If you see "command not found," something went wrong with the installation or PATH setup. Once nvcc --version works, navigate back to your llama.cpp/build directory: cd ~/text-generation-webui/repositories/llama.cpp/build Clear the build directory again (important after installing new system dependencies): rm -rf * Re-run CMake to configure the build (this time it should find CUDA): cmake .. -DGGML_CUDA=ON Build the project (if CMake configuration is successful): cmake --build . --config Release Please execute these steps carefully and provide the full output for each command. The nvcc --version output is particularly important to confirm the CUDA Toolkit is correctly installed.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]