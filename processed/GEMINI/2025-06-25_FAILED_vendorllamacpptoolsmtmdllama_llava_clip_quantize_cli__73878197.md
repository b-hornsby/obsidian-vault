---
id: 602806
source: GEMINI
date: 2025-06-25
tags: ['coding', 'llm', 'ai', 'gemini', 'llama.cpp', 'defi', 'dex', 'python']
category: coding
sentiment: frustrated
resolution: unresolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/topics/personal/crypto-web3.md']
---
#       FAILED: vendor/llama.cpp/tools/mtmd/llama-llava-clip-quantize-cli
      : && /usr/bin/g++  -pthread -B /home/bryan_/miniconda3/envs/llm-assist/compiler_compat -O3 -DNDEBUG  vendor/llama.cpp/tools/mtmd/CMakeFiles/llava.dir/llava.cpp.o vendor/llama.cpp/tools/mtmd/CMakeFiles/llava.dir/clip.cpp.o vendor/llama.cpp/tools/mtmd/CMakeFiles/llama-llava-clip-quantize-cli.dir/clip-quantize-cli.cpp.o -o vendor/llama.cpp/tools/mtmd/llama-llava-clip-quantize-cli  -Wl,-rpath,/tmp/tmp3gtpgtcv/build/bin:  vendor/llama.cpp/common/libcommon.a  bin/libllama.so  bin/libggml.so  bin/libggml-cpu.so  bin/libggml-base.so && :
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: warning: libgomp.so.1, needed by bin/libggml-cpu.so, not found (try using -rpath or -rpath-link)
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `GOMP_barrier@GOMP_1.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `GOMP_parallel@GOMP_4.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `omp_get_thread_num@OMP_1.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `GOMP_single_start@GOMP_1.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `omp_get_num_threads@OMP_1.0'
      collect2: error: ld returned 1 exit status
      [79/79] : && /usr/bin/g++  -pthread -B /home/bryan_/miniconda3/envs/llm-assist/compiler_compat -O3 -DNDEBUG  vendor/llama.cpp/tools/mtmd/CMakeFiles/mtmd.dir/mtmd.cpp.o vendor/llama.cpp/tools/mtmd/CMakeFiles/mtmd.dir/clip.cpp.o vendor/llama.cpp/tools/mtmd/CMakeFiles/llama-mtmd-cli.dir/mtmd-cli.cpp.o -o vendor/llama.cpp/tools/mtmd/llama-mtmd-cli  -Wl,-rpath,/tmp/tmp3gtpgtcv/build/bin:  vendor/llama.cpp/common/libcommon.a  bin/libllama.so  bin/libggml.so  bin/libggml-cpu.so  bin/libggml-base.so && :
      FAILED: vendor/llama.cpp/tools/mtmd/llama-mtmd-cli
      : && /usr/bin/g++  -pthread -B /home/bryan_/miniconda3/envs/llm-assist/compiler_compat -O3 -DNDEBUG  vendor/llama.cpp/tools/mtmd/CMakeFiles/mtmd.dir/mtmd.cpp.o vendor/llama.cpp/tools/mtmd/CMakeFiles/mtmd.dir/clip.cpp.o vendor/llama.cpp/tools/mtmd/CMakeFiles/llama-mtmd-cli.dir/mtmd-cli.cpp.o -o vendor/llama.cpp/tools/mtmd/llama-mtmd-cli  -Wl,-rpath,/tmp/tmp3gtpgtcv/build/bin:  vendor/llama.cpp/common/libcommon.a  bin/libllama.so  bin/libggml.so  bin/libggml-cpu.so  bin/libggml-base.so && :
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: warning: libgomp.so.1, needed by bin/libggml-cpu.so, not found (try using -rpath or -rpath-link)
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `GOMP_barrier@GOMP_1.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `GOMP_parallel@GOMP_4.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `omp_get_thread_num@OMP_1.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `GOMP_single_start@GOMP_1.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `omp_get_num_threads@OMP_1.0'
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
      FAILED: vendor/llama.cpp/tools/mtmd/llama-llava-clip-quantize-cli
      : && /usr/bin/g++  -pthread -B /home/bryan_/miniconda3/envs/llm-assist/compiler_compat -O3 -DNDEBUG  vendor/llama.cpp/tools/mtmd/CMakeFiles/llava.dir/llava.cpp.o vendor/llama.cpp/tools/mtmd/CMakeFiles/llava.dir/clip.cpp.o vendor/llama.cpp/tools/mtmd/CMakeFiles/llama-llava-clip-quantize-cli.dir/clip-quantize-cli.cpp.o -o vendor/llama.cpp/tools/mtmd/llama-llava-clip-quantize-cli  -Wl,-rpath,/tmp/tmp3gtpgtcv/build/bin:  vendor/llama.cpp/common/libcommon.a  bin/libllama.so  bin/libggml.so  bin/libggml-cpu.so  bin/libggml-base.so && :
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: warning: libgomp.so.1, needed by bin/libggml-cpu.so, not found (try using -rpath or -rpath-link)
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `GOMP_barrier@GOMP_1.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `GOMP_parallel@GOMP_4.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `omp_get_thread_num@OMP_1.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `GOMP_single_start@GOMP_1.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `omp_get_num_threads@OMP_1.0'
      collect2: error: ld returned 1 exit status
      [79/79] : && /usr/bin/g++  -pthread -B /home/bryan_/miniconda3/envs/llm-assist/compiler_compat -O3 -DNDEBUG  vendor/llama.cpp/tools/mtmd/CMakeFiles/mtmd.dir/mtmd.cpp.o vendor/llama.cpp/tools/mtmd/CMakeFiles/mtmd.dir/clip.cpp.o vendor/llama.cpp/tools/mtmd/CMakeFiles/llama-mtmd-cli.dir/mtmd-cli.cpp.o -o vendor/llama.cpp/tools/mtmd/llama-mtmd-cli  -Wl,-rpath,/tmp/tmp3gtpgtcv/build/bin:  vendor/llama.cpp/common/libcommon.a  bin/libllama.so  bin/libggml.so  bin/libggml-cpu.so  bin/libggml-base.so && :
      FAILED: vendor/llama.cpp/tools/mtmd/llama-mtmd-cli
      : && /usr/bin/g++  -pthread -B /home/bryan_/miniconda3/envs/llm-assist/compiler_compat -O3 -DNDEBUG  vendor/llama.cpp/tools/mtmd/CMakeFiles/mtmd.dir/mtmd.cpp.o vendor/llama.cpp/tools/mtmd/CMakeFiles/mtmd.dir/clip.cpp.o vendor/llama.cpp/tools/mtmd/CMakeFiles/llama-mtmd-cli.dir/mtmd-cli.cpp.o -o vendor/llama.cpp/tools/mtmd/llama-mtmd-cli  -Wl,-rpath,/tmp/tmp3gtpgtcv/build/bin:  vendor/llama.cpp/common/libcommon.a  bin/libllama.so  bin/libggml.so  bin/libggml-cpu.so  bin/libggml-base.so && :
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: warning: libgomp.so.1, needed by bin/libggml-cpu.so, not found (try using -rpath or -rpath-link)
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `GOMP_barrier@GOMP_1.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `GOMP_parallel@GOMP_4.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `omp_get_thread_num@OMP_1.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `GOMP_single_start@GOMP_1.0'
      /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `omp_get_num_threads@OMP_1.0'
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
You've hit a common compilation issue when building llama-cpp-python from source, especially in certain environments! The core of the problem is indicated by these lines: /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: warning: libgomp.so.1, needed by bin/libggml-cpu.so, not found (try using -rpath or -rpath-link) ... /home/bryan_/miniconda3/envs/llm-assist/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `GOMP_barrier@GOMP_1.0' ... collect2: error: ld returned 1 exit status This means the linker (ld) couldn't find libgomp.so.1, which is the GNU OpenMP (Open Multi-Processing) library. This library is crucial for parallel processing on the CPU, and even when you're targeting the GPU, llama.cpp's underlying ggml library still uses OpenMP for some CPU-related operations. The "undefined reference" errors confirm that essential functions from libgomp are missing. This usually happens when the compiler environment (which Conda tries to manage with compiler_compat) doesn't have the necessary runtime libraries immediately accessible, or they're not installed in a standard location. Let's try to resolve this by explicitly installing the libgomp1 package and possibly reinstalling build-essential to ensure all compiler dependencies are met within your WSL environment. Action: First, ensure your package lists are up to date within your llm-assist environment (though this is more for system-wide packages, it doesn't hurt). sudo apt update Next, explicitly install the libgomp1 package. This provides the missing library. sudo apt install libgomp1 -y It's also a good idea to ensure build-essential is fully reconciled after the Conda environment setup, as llama-cpp-python builds C++ components. sudo apt install build-essential -y After these system-level packages are installed, we will retry the llama-cpp-python installation. pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/wheels/cu121 Please run these commands one by one. Let me know the full output of the pip install command after you retry it.