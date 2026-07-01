---
id: 590236
source: GEMINI
date: 2025-06-25
tags: ['coding', 'llm', 'ai', 'gemini', 'mcp', 'defi', 'dex', 'python']
category: coding
sentiment: frustrated
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/topics/personal/crypto-web3.md', 'nodes/projects/operation-immortal-agent.md']
---
# this is what it spat out:       /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `__cudaRegisterFunction@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaStreamEndCapture@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMalloc@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaHostRegister@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGetDeviceCount@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGraphInstantiate@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGetErrorString@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaEventRecord@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGraphDestroy@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGraphExecDestroy@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaFreeHost@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaStreamDestroy@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cublasSetStream_v2@libcublas.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cublasGemmBatchedEx@libcublas.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGetDevice@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `__cudaRegisterFatBinary@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaStreamSynchronize@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cuMemAddressFree'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaEventCreateWithFlags@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaLaunchKernel@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaFuncSetAttribute@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMemcpyPeerAsync@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMemcpy3DPeerAsync@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cublasDestroy_v2@libcublas.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaFuncGetAttributes@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cublasGemmEx@libcublas.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cuGetErrorString'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cublasGemmStridedBatchedEx@libcublas.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cublasCreate_v2@libcublas.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMemGetInfo@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMemsetAsync@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cublasSetMathMode@libcublas.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `__cudaPushCallConfiguration@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cuDeviceGetAttribute'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaDeviceEnablePeerAccess@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cuMemMap'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMemcpyAsync@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGraphExecUpdate@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMemcpy2DAsync@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMemset@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cuMemRelease'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cublasGetStatusString@libcublas.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaDeviceDisablePeerAccess@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaHostUnregister@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaStreamCreateWithFlags@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaDeviceCanAccessPeer@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaPeekAtLastError@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGraphLaunch@libcudart.so.12'
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
this is what it spat out:       /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `__cudaRegisterFunction@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaStreamEndCapture@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMalloc@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaHostRegister@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGetDeviceCount@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGraphInstantiate@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGetErrorString@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaEventRecord@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGraphDestroy@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGraphExecDestroy@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaFreeHost@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaStreamDestroy@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cublasSetStream_v2@libcublas.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cublasGemmBatchedEx@libcublas.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGetDevice@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `__cudaRegisterFatBinary@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaStreamSynchronize@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cuMemAddressFree'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaEventCreateWithFlags@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaLaunchKernel@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaFuncSetAttribute@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMemcpyPeerAsync@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMemcpy3DPeerAsync@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cublasDestroy_v2@libcublas.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaFuncGetAttributes@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cublasGemmEx@libcublas.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cuGetErrorString'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cublasGemmStridedBatchedEx@libcublas.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cublasCreate_v2@libcublas.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMemGetInfo@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMemsetAsync@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cublasSetMathMode@libcublas.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `__cudaPushCallConfiguration@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cuDeviceGetAttribute'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaDeviceEnablePeerAccess@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cuMemMap'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMemcpyAsync@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGraphExecUpdate@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMemcpy2DAsync@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaMemset@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cuMemRelease'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cublasGetStatusString@libcublas.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaDeviceDisablePeerAccess@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaHostUnregister@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaStreamCreateWithFlags@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaDeviceCanAccessPeer@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaPeekAtLastError@libcudart.so.12'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cuda.so: undefined reference to `cudaGraphLaunch@libcudart.so.12'
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
Got it. Thanks for providing the end of the output. This is still a linking error, and it specifically mentions libcudart.so.12 and libcublas.so.12. This is quite persistent. The undefined reference errors mean that the linker (part of the compiler toolchain) cannot find the actual code for these CUDA and cuBLAS functions, even though the header files were found during compilation. This often indicates: Libraries are not in the linker's search path: We tried LD_LIBRARY_PATH, but it might not be picking it up correctly or there's another path interfering. Incorrect CUDA Toolkit installation/environment setup: While nvcc is found, the actual .so files might not be where the build expects them. Conflict with Conda's compiler_compat: Conda's environment attempts to provide a consistent compiler toolchain. Sometimes, this can conflict with external installations like the CUDA Toolkit if not managed carefully. Missing cuda-toolkit conda package: Even if you have CUDA installed system-wide, llama-cpp-python often works best when the CUDA libraries are also available via a conda-forge cuda-toolkit package. This ensures all components are consistent within the conda environment. Let's try the most robust approach for Conda environments: installing the CUDA Toolkit components directly via Conda. This often resolves these deep linking issues by ensuring all necessary CUDA libraries are properly integrated into your llm-assist environment and known to its linker. Action: Install the CUDA Toolkit (Base) and cuBLAS through Conda. This will pull in the necessary libcudart and libcublas libraries into your Conda environment's lib directory, which compiler_compat should then correctly pick up. Run this in your (llm-assist) terminal: conda install -c "nvidia/label/cuda-12.0" cuda-toolkit -y conda install -c "nvidia/label/cuda-12.0" cublas -y We're specifying the nvidia/label/cuda-12.0 channel because your nvcc reported version 12.0.140. It's crucial to match the CUDA version as closely as possible. This step might download and install a significant number of packages. This is expected as it brings CUDA components into your Conda env. After the conda install commands complete, try installing llama-cpp-python again. We will still include the LD_LIBRARY_PATH export as a belt-and-suspenders approach, but the Conda-installed packages should be the primary fix. export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib:$CUDA_HOME/lib64 CMAKE_ARGS="-DGGML_CUDA=on" FORCE_CMAKE=1 pip install llama-cpp-python --no-cache-dir Please execute these conda install commands first, then the pip install command. Share the full output of all commands. This is our best shot at resolving the linker errors.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/private-ai-consulting|Private AI Consulting]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]