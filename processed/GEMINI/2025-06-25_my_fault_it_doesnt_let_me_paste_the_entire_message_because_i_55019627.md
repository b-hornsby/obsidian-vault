---
id: 404860
source: GEMINI
date: 2025-06-25
tags: ['coding', 'llm', 'ai', 'gemini', 'defi', 'long', 'python', 'go']
category: coding
sentiment: frustrated
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/topics/personal/crypto-web3.md', 'nodes/people/dad.md']
---
# my fault. it doesn't let me paste the entire message because its too long but it ended with:    /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaStreamCreateWithFlags@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaDeviceCanAccessPeer@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaPeekAtLastError@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGraphLaunch@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `omp_get_num_threads@OMP_1.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMallocManaged@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `__cudaRegisterVar@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `__cudaUnregisterFatBinary@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `__cudaPopCallConfiguration@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGetDeviceProperties_v2@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGetLastError@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cuMemGetAllocationGranularity'
      collect2: error: ld returned 1 exit status
      ninja: build stopped: subcommand failed.


      *** CMake build failed
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for llama-cpp-python
Failed to build llama-cpp-python
ERROR: Failed to build installable wheels for some pyproject.toml based projects (llama-cpp-python)
(llm-assist) bryan_@DESKTOP-NG2I0P2:~$

### USER
my fault. it doesn't let me paste the entire message because its too long but it ended with:    /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaStreamCreateWithFlags@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaDeviceCanAccessPeer@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaPeekAtLastError@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGraphLaunch@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `omp_get_num_threads@OMP_1.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMallocManaged@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `__cudaRegisterVar@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `__cudaUnregisterFatBinary@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `__cudaPopCallConfiguration@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGetDeviceProperties_v2@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGetLastError@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cuMemGetAllocationGranularity'
      collect2: error: ld returned 1 exit status
      ninja: build stopped: subcommand failed.


      *** CMake build failed
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for llama-cpp-python
Failed to build llama-cpp-python
ERROR: Failed to build installable wheels for some pyproject.toml based projects (llama-cpp-python)
(llm-assist) bryan_@DESKTOP-NG2I0P2:~$

### GEMINI
Ah, thank you! This is the exact error output we needed. The crucial part is: /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaStreamCreateWithFlags@libcudart.so.12' ... /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGetDeviceProperties_v2@libcudart.so.12' /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGetLastError@libcudart.so.12' /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cuMemGetAllocationGranularity' collect2: error: ld returned 1 exit status ninja: build stopped: subcommand failed. This is a linking error. It means that the llama-cpp-python build process successfully compiled its CUDA and CPU code, but when it tried to link those compiled pieces into the final shared libraries (libggml-cuda.so and libggml-cpu.so), it couldn't find the definitions for various CUDA functions (like cudaStreamCreateWithFlags, cudaDeviceCanAccessPeer, cudaGetLastError, etc.) and some OpenMP functions (omp_get_num_threads). The @libcudart.so.12 part indicates that it expects these functions to come from libcudart.so.12, which is the CUDA Runtime Library version 12. Why is this happening? CUDA Toolkit Environment: Even though CMake found CUDA Toolkit 12.0.140, the linker (ld) either isn't looking in the correct directories for the CUDA libraries, or there's a conflict/mismatch in how your conda environment's compiler wrappers (compiler_compat) are interacting with the CUDA installation. Missing or Mismatched Libraries: The necessary CUDA libraries (specifically libcudart.so.12) might not be in a location discoverable by the linker, or there might be an issue with their versions. OpenMP Issue: The omp_get_num_threads@OMP_1.0 suggests a similar linking issue with OpenMP, which is used for CPU parallelization. Let's try a common fix for linking issues in Conda environments, which involves explicitly specifying the CUDA library paths and potentially ensuring OpenMP is correctly configured via Conda. Action: First, ensure your environment variables are correctly set for CUDA within your llm-assist environment. We'll try setting LD_LIBRARY_PATH explicitly. Then, we'll try installing libgomp (GNU OpenMP library) via conda to ensure it's properly linked for the OpenMP error. Run these commands one by one in your (llm-assist) terminal: conda install -c conda-forge libgomp -y (This should install or confirm libgomp is present.) Now, try the pip install command again with explicit library paths: export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib:$CUDA_HOME/lib64 CMAKE_ARGS="-DGGML_CUDA=on" FORCE_CMAKE=1 pip install llama-cpp-python --no-cache-dir export LD_LIBRARY_PATH=...: This temporarily adds your Conda environment's lib directory and the standard CUDA lib64 directory (assuming $CUDA_HOME is correctly set, which it seems to be from previous outputs) to the linker's search path. This should help ld find libcudart.so.12 and other necessary libraries. $CONDA_PREFIX/lib: This points to ~/miniconda3/envs/llm-assist/lib, where Conda-installed libraries reside. $CUDA_HOME/lib64: This points to where your CUDA Toolkit's main libraries are. While nvcc found /usr/include, the libraries are typically in /usr/local/cuda/lib64 or similar, which $CUDA_HOME should point to. IMPORTANT: The export command only sets the variable for the current terminal session. If you close and reopen the terminal, you'd need to re-run the export command before attempting any llama-cpp-python compilation. Please run these commands and share the full output of the pip install command again, especially the tail end if it fails.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]