---
id: 134049
source: GEMINI
date: 2025-06-25
tags: ['coding', 'llm', 'ai', 'gemini', 'llama.cpp', 'python', 'go', 'code']
category: coding
sentiment: frustrated
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# (llm-assist) bryan_@DESKTOP-NG2I0P2:~$ CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python --no-cache-dir
Collecting llama-cpp-python
  Downloading llama_cpp_python-0.3.9.tar.gz (67.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 67.9/67.9 MB 97.2 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: typing-extensions>=4.5.0 in ./miniconda3/envs/llm-assist/lib/python3.11/site-packages (from llama-cpp-python) (4.12.2)
Requirement already satisfied: numpy>=1.20.0 in ./miniconda3/envs/llm-assist/lib/python3.11/site-packages (from llama-cpp-python) (2.1.2)
Collecting diskcache>=5.6.1 (from llama-cpp-python)
  Downloading diskcache-5.6.3-py3-none-any.whl.metadata (20 kB)
Requirement already satisfied: jinja2>=2.11.3 in ./miniconda3/envs/llm-assist/lib/python3.11/site-packages (from llama-cpp-python) (3.1.4)
Requirement already satisfied: MarkupSafe>=2.0 in ./miniconda3/envs/llm-assist/lib/python3.11/site-packages (from jinja2>=2.11.3->llama-cpp-python) (2.1.5)
Downloading diskcache-5.6.3-py3-none-any.whl (45 kB)
Building wheels for collected packages: llama-cpp-python
  Building wheel for llama-cpp-python (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Building wheel for llama-cpp-python (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [28 lines of output]
      *** scikit-build-core 0.11.4 using CMake 4.0.3 (wheel)
      *** Configuring CMake...
      loading initial cache file /tmp/tmp1mioabeb/build/CMakeInit.txt
      -- The C compiler identification is GNU 13.3.0
      -- The CXX compiler identification is GNU 13.3.0
      -- Detecting C compiler ABI info
      -- Detecting C compiler ABI info - done
      -- Check for working C compiler: /usr/bin/gcc - skipped
      -- Detecting C compile features
      -- Detecting C compile features - done
      -- Detecting CXX compiler ABI info
      -- Detecting CXX compiler ABI info - done
      -- Check for working CXX compiler: /usr/bin/g++ - skipped
      -- Detecting CXX compile features
      -- Detecting CXX compile features - done
      -- Found Git: /usr/bin/git (found version "2.43.0")
      CMake Error at vendor/llama.cpp/CMakeLists.txt:108 (message):
        LLAMA_CUBLAS is deprecated and will be removed in the future.

        Use GGML_CUDA instead

      Call Stack (most recent call first):
        vendor/llama.cpp/CMakeLists.txt:113 (llama_option_depr)


      -- Configuring incomplete, errors occurred!

      *** CMake configuration failed
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for llama-cpp-python
Failed to build llama-cpp-python
ERROR: Failed to build installable wheels for some pyproject.toml based projects (llama-cpp-python)
(llm-assist) bryan_@DESKTOP-NG2I0P2:~$

### USER
(llm-assist) bryan_@DESKTOP-NG2I0P2:~$ CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python --no-cache-dir
Collecting llama-cpp-python
  Downloading llama_cpp_python-0.3.9.tar.gz (67.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 67.9/67.9 MB 97.2 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: typing-extensions>=4.5.0 in ./miniconda3/envs/llm-assist/lib/python3.11/site-packages (from llama-cpp-python) (4.12.2)
Requirement already satisfied: numpy>=1.20.0 in ./miniconda3/envs/llm-assist/lib/python3.11/site-packages (from llama-cpp-python) (2.1.2)
Collecting diskcache>=5.6.1 (from llama-cpp-python)
  Downloading diskcache-5.6.3-py3-none-any.whl.metadata (20 kB)
Requirement already satisfied: jinja2>=2.11.3 in ./miniconda3/envs/llm-assist/lib/python3.11/site-packages (from llama-cpp-python) (3.1.4)
Requirement already satisfied: MarkupSafe>=2.0 in ./miniconda3/envs/llm-assist/lib/python3.11/site-packages (from jinja2>=2.11.3->llama-cpp-python) (2.1.5)
Downloading diskcache-5.6.3-py3-none-any.whl (45 kB)
Building wheels for collected packages: llama-cpp-python
  Building wheel for llama-cpp-python (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Building wheel for llama-cpp-python (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [28 lines of output]
      *** scikit-build-core 0.11.4 using CMake 4.0.3 (wheel)
      *** Configuring CMake...
      loading initial cache file /tmp/tmp1mioabeb/build/CMakeInit.txt
      -- The C compiler identification is GNU 13.3.0
      -- The CXX compiler identification is GNU 13.3.0
      -- Detecting C compiler ABI info
      -- Detecting C compiler ABI info - done
      -- Check for working C compiler: /usr/bin/gcc - skipped
      -- Detecting C compile features
      -- Detecting C compile features - done
      -- Detecting CXX compiler ABI info
      -- Detecting CXX compiler ABI info - done
      -- Check for working CXX compiler: /usr/bin/g++ - skipped
      -- Detecting CXX compile features
      -- Detecting CXX compile features - done
      -- Found Git: /usr/bin/git (found version "2.43.0")
      CMake Error at vendor/llama.cpp/CMakeLists.txt:108 (message):
        LLAMA_CUBLAS is deprecated and will be removed in the future.

        Use GGML_CUDA instead

      Call Stack (most recent call first):
        vendor/llama.cpp/CMakeLists.txt:113 (llama_option_depr)


      -- Configuring incomplete, errors occurred!

      *** CMake configuration failed
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for llama-cpp-python
Failed to build llama-cpp-python
ERROR: Failed to build installable wheels for some pyproject.toml based projects (llama-cpp-python)
(llm-assist) bryan_@DESKTOP-NG2I0P2:~$

### GEMINI
Okay, this is a different and actually more helpful error! The key lines are: CMake Error at vendor/llama.cpp/CMakeLists.txt:108 (message): LLAMA_CUBLAS is deprecated and will be removed in the future. Use GGML_CUDA instead This tells us that the build flag LLAMA_CUBLAS (which we used to enable CUDA) is now deprecated by llama.cpp itself, and they want us to use GGML_CUDA instead. This is a recent change in llama.cpp (the underlying C++ library) that llama-cpp-python relies on. This is a good sign because it means your compiler environment is now working well enough to get to the point where llama.cpp's CMake configuration is running, and it's explicitly telling you what's wrong with the build flag. Let's adjust the CMAKE_ARGS to use the new, recommended flag. Action: We don't need to uninstall again, as the previous attempt failed cleanly. Run the installation command again, but with the updated CMAKE_ARGS: CMAKE_ARGS="-DGGML_CUDA=on" FORCE_CMAKE=1 pip install llama-cpp-python --no-cache-dir Change: LLAMA_CUBLAS has been replaced with GGML_CUDA. Keep FORCE_CMAKE=1 and --no-cache-dir. Remember: This compilation will still take a significant amount of time. Please run this updated command and share the full output again. This should hopefully get us past this compilation hurdle!