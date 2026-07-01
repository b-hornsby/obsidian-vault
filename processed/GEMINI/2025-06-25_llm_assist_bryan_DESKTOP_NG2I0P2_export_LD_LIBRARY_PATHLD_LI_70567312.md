---
id: 878005
source: GEMINI
date: 2025-06-25
tags: ['ai-tools', 'llm', 'ai', 'gemini', 'model', 'rag', 'gguf', 'leverage']
category: ai-tools
sentiment: building
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# (llm-assist) bryan_@DESKTOP-NG2I0P2:~$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib:$CUDA_HOME/lib64
CMAKE_ARGS="-DGGML_CUDA=on" FORCE_CMAKE=1 pip install llama-cpp-python --no-cache-dir
Collecting llama-cpp-python
  Downloading llama_cpp_python-0.3.9.tar.gz (67.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 67.9/67.9 MB 89.9 MB/s eta 0:00:00
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
  Building wheel for llama-cpp-python (pyproject.toml) ... done
  Created wheel for llama-cpp-python: filename=llama_cpp_python-0.3.9-cp311-cp311-linux_x86_64.whl size=47496150 sha256=d05bfccbaecdf990f7709fedf551c0aadedb487321d19c32cd97877bc46eae37
  Stored in directory: /tmp/pip-ephem-wheel-cache-sr47ynuh/wheels/9e/8f/bf/148c8eb7d69021eccd6eae6444f3accd48347587054ffd24e5
Successfully built llama-cpp-python
Installing collected packages: diskcache, llama-cpp-python
Successfully installed diskcache-5.6.3 llama-cpp-python-0.3.9
(llm-assist) bryan_@DESKTOP-NG2I0P2:~$

### USER
(llm-assist) bryan_@DESKTOP-NG2I0P2:~$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib:$CUDA_HOME/lib64
CMAKE_ARGS="-DGGML_CUDA=on" FORCE_CMAKE=1 pip install llama-cpp-python --no-cache-dir
Collecting llama-cpp-python
  Downloading llama_cpp_python-0.3.9.tar.gz (67.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 67.9/67.9 MB 89.9 MB/s eta 0:00:00
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
  Building wheel for llama-cpp-python (pyproject.toml) ... done
  Created wheel for llama-cpp-python: filename=llama_cpp_python-0.3.9-cp311-cp311-linux_x86_64.whl size=47496150 sha256=d05bfccbaecdf990f7709fedf551c0aadedb487321d19c32cd97877bc46eae37
  Stored in directory: /tmp/pip-ephem-wheel-cache-sr47ynuh/wheels/9e/8f/bf/148c8eb7d69021eccd6eae6444f3accd48347587054ffd24e5
Successfully built llama-cpp-python
Installing collected packages: diskcache, llama-cpp-python
Successfully installed diskcache-5.6.3 llama-cpp-python-0.3.9
(llm-assist) bryan_@DESKTOP-NG2I0P2:~$

### GEMINI
Oh, this is FANTASTIC NEWS! Look at these lines: Building wheels for collected packages: llama-cpp-python Building wheel for llama-cpp-python (pyproject.toml) ... done Created wheel for llama-cpp-python: filename=llama_cpp_python-0.3.9-cp311-cp311-linux_x86_64.whl size=47496150 sha256=d05bfccbaecdf990f7709fedf551c0aadedb487321d19c32cd97877bc46eae37 Stored in directory: /tmp/pip-ephem-wheel-cache-sr47ynuh/wheels/9e/8f/bf/148c8eb7d69021eccd6eae6444f3accd48347587054ffd24e5 Successfully built llama-cpp-python Installing collected packages: diskcache, llama-cpp-python Successfully installed diskcache-5.6.3 llama-cpp-python-0.3.9 llama-cpp-python has successfully built and installed with CUDA support! The conda install cuda-toolkit step, combined with setting LD_LIBRARY_PATH, provided the necessary CUDA and cuBLAS libraries in a way that the llama-cpp-python build system (which uses CMake and Ninja) could find and link against. You have overcome the most difficult part of setting this up. What's next? You should now be able to use llama-cpp-python within your llm-assist Conda environment, and it should leverage your GPU for acceleration. You can now proceed with following the instructions for using llama-cpp-python to download a GGUF model and run it. Remember to activate your llm-assist environment (conda activate llm-assist) whenever you want to use it. Congratulations! This was a challenging one, but we got there.