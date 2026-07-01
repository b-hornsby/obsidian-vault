---
category: homelab
date: 2025-06-24
id: 362917
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: partial
sentiment: building
source: GEMINI
summary: The user is attempting to compile llama.cpp with CUDA GPU acceleration support
  on their local machine, indicating they are building a local LLM inference setup.
tags:
- llama.cpp
- CUDA
- local-llm
- compilation
- gpu-acceleration
---
# bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$ rm -rf *
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
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$ rm -rf *
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
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$ rm -rf *
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
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/repositories/llama.cpp/build$ rm -rf *
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
Okay, excellent! We are making progress. The previous issue is gone, and we have a new, clear error: -- Could not find nvcc, please set CUDAToolkit_ROOT. CMake Error at ggml/src/ggml-cuda/CMakeLists.txt:183 (message): CUDA Toolkit not found This message means that cmake is now correctly attempting to build llama.cpp with CUDA support (because of -DGGML_CUDA=ON), but it cannot find the NVIDIA CUDA Toolkit installed on your WSL2 system. The nvcc compiler (NVIDIA CUDA Compiler) is a key part of this toolkit. Even though you likely have NVIDIA drivers and possibly some CUDA runtime on your Windows host, for llama.cpp to compile with CUDA support inside WSL2, the CUDA Toolkit development libraries and compiler (nvcc) must be installed directly within your WSL2 distribution. Step 38: Install NVIDIA CUDA Toolkit in WSL2 You need to install the CUDA Toolkit within your Ubuntu/WSL2 environment. We'll use CUDA 11.8 since your PyTorch installation (cu118) is compatible with that version. Action: Ensure you are still in your WSL2 terminal. Run the following commands to install the CUDA Toolkit 11.8 for WSL-Ubuntu: # Remove any previous NVIDIA keyrings sudo rm /etc/apt/sources.list.d/cuda.list sudo apt autoremove --purge 'cuda*' 'nvidia*' sudo apt update sudo apt clean sudo apt autoclean # Download and add the NVIDIA GPG key wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600 wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb sudo dpkg -i cuda-keyring_1.1-1_all.deb # Update your package list and install CUDA Toolkit 11.8 sudo apt update sudo apt -y install cuda-toolkit-11-8 Pay attention to any prompts during sudo apt -y install cuda-toolkit-11-8 – it will download a significant amount of data and may take a while. Do not proceed until this installation completes successfully. After the installation, add CUDA to your PATH environment variable. This makes nvcc discoverable. echo 'export PATH=/usr/local/cuda-11.8/bin${PATH:+:${PATH}}' >> ~/.bashrc echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc source ~/.bashrc Verify the nvcc installation: nvcc --version This should output the CUDA compiler version. Once CUDA Toolkit is installed and verified, navigate back to your llama.cpp/build directory: cd ~/text-generation-webui/repositories/llama.cpp/build Clear the build directory again (important after installing new system dependencies): rm -rf * Re-run CMake to configure the build (this time it should find CUDA): cmake .. -DGGML_CUDA=ON Build the project: cmake --build . --config Release This is a multi-step process, but it's essential for enabling GPU support in llama.cpp. Please provide the full output of each command.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]