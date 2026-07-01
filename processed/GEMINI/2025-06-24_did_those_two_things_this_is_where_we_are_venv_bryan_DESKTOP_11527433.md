---
category: ai-tools
date: 2025-06-24
id: 11051
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: partial
sentiment: executing
source: GEMINI
summary: The user is installing PyTorch with CUDA 11.8 support in a virtual environment
  for the text-generation-webui project, having completed prior steps and now in the
  process of dependency installation.
tags:
- pytorch-installation
- text-generation-webui
- cuda-11-8
- python-virtual-environment
- gpu-acceleration
---
# did those two things, this is where we are: (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
Looking in indexes: https://download.pytorch.org/whl/cu118
Collecting torch
  Obtaining dependency information for torch from https://download.pytorch.org/whl/cu118/torch-2.7.1%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torch-2.7.1%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (28 kB)
Collecting torchvision
  Obtaining dependency information for torchvision from https://download.pytorch.org/whl/cu118/torchvision-0.22.1%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torchvision-0.22.1%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (6.1 kB)
Collecting torchaudio
  Obtaining dependency information for torchaudio from https://download.pytorch.org/whl/cu118/torchaudio-2.7.1%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torchaudio-2.7.1%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (6.6 kB)
Collecting nvidia-nvtx-cu11==11.8.86
  Using cached https://download.pytorch.org/whl/cu118/nvidia_nvtx_cu11-11.8.86-py3-none-manylinux1_x86_64.whl (99 kB)
Collecting networkx
  Obtaining dependency information for networkx from https://download.pytorch.org/whl/networkx-3.3-py3-none-any.whl.metadata
  Using cached https://download.pytorch.org/whl/networkx-3.3-py3-none-any.whl.metadata (5.1 kB)
Collecting sympy>=1.13.3
  Obtaining dependency information for sympy>=1.13.3 from https://download.pytorch.org/whl/sympy-1.13.3-py3-none-any.whl.metadata
  Using cached https://download.pytorch.org/whl/sympy-1.13.3-py3-none-any.whl.metadata (12 kB)
Collecting nvidia-cuda-runtime-cu11==11.8.89
  Using cached https://download.pytorch.org/whl/cu118/nvidia_cuda_runtime_cu11-11.8.89-py3-none-manylinux1_x86_64.whl (875 kB)
Collecting filelock
  Obtaining dependency information for filelock from https://download.pytorch.org/whl/filelock-3.13.1-py3-none-any.whl.metadata
  Using cached https://download.pytorch.org/whl/filelock-3.13.1-py3-none-any.whl.metadata (2.8 kB)
Collecting nvidia-cudnn-cu11==9.1.0.70
  Using cached https://download.pytorch.org/whl/cu118/nvidia_cudnn_cu11-9.1.0.70-py3-none-manylinux2014_x86_64.whl (663.9 MB)
Collecting nvidia-cuda-nvrtc-cu11==11.8.89
  Using cached https://download.pytorch.org/whl/cu118/nvidia_cuda_nvrtc_cu11-11.8.89-py3-none-manylinux1_x86_64.whl (23.2 MB)
Collecting fsspec
  Obtaining dependency information for fsspec from https://download.pytorch.org/whl/fsspec-2024.6.1-py3-none-any.whl.metadata
  Using cached https://download.pytorch.org/whl/fsspec-2024.6.1-py3-none-any.whl.metadata (11 kB)
Collecting nvidia-cufft-cu11==10.9.0.58
  Using cached https://download.pytorch.org/whl/cu118/nvidia_cufft_cu11-10.9.0.58-py3-none-manylinux1_x86_64.whl (168.4 MB)
Collecting nvidia-cusparse-cu11==11.7.5.86
  Using cached https://download.pytorch.org/whl/cu118/nvidia_cusparse_cu11-11.7.5.86-py3-none-manylinux1_x86_64.whl (204.1 MB)
Collecting nvidia-cusolver-cu11==11.4.1.48
  Using cached https://download.pytorch.org/whl/cu118/nvidia_cusolver_cu11-11.4.1.48-py3-none-manylinux1_x86_64.whl (128.2 MB)
Collecting triton==3.3.1
  Obtaining dependency information for triton==3.3.1 from https://download.pytorch.org/whl/triton-3.3.1-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/triton-3.3.1-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (1.5 kB)
Collecting nvidia-curand-cu11==10.3.0.86
  Using cached https://download.pytorch.org/whl/cu118/nvidia_curand_cu11-10.3.0.86-py3-none-manylinux1_x86_64.whl (58.1 MB)
Collecting jinja2
  Obtaining dependency information for jinja2 from https://download.pytorch.org/whl/Jinja2-3.1.4-py3-none-any.whl.metadata
  Using cached https://download.pytorch.org/whl/Jinja2-3.1.4-py3-none-any.whl.metadata (2.6 kB)
Discarding https://download.pytorch.org/whl/Jinja2-3.1.4-py3-none-any.whl#sha256=bc5dd2abb727a5319567b7a813e6a2e7318c39f4f487cfe6c89c6f9c7d25197d (from https://download.pytorch.org/whl/cu118/jinja2/): Requested jinja2 from https://download.pytorch.org/whl/Jinja2-3.1.4-py3-none-any.whl#sha256=bc5dd2abb727a5319567b7a813e6a2e7318c39f4f487cfe6c89c6f9c7d25197d (from torch) has inconsistent Name: expected 'jinja2', but metadata has 'Jinja2'
  Using cached https://download.pytorch.org/whl/Jinja2-3.1.3-py3-none-any.whl (133 kB)
Collecting nvidia-nccl-cu11==2.21.5
  Using cached https://download.pytorch.org/whl/cu118/nvidia_nccl_cu11-2.21.5-py3-none-manylinux2014_x86_64.whl (147.8 MB)
Collecting nvidia-cuda-cupti-cu11==11.8.87
  Using cached https://download.pytorch.org/whl/cu118/nvidia_cuda_cupti_cu11-11.8.87-py3-none-manylinux1_x86_64.whl (13.1 MB)
Collecting typing-extensions>=4.10.0
  Obtaining dependency information for typing-extensions>=4.10.0 from https://download.pytorch.org/whl/typing_extensions-4.12.2-py3-none-any.whl.metadata
  Using cached https://download.pytorch.org/whl/typing_extensions-4.12.2-py3-none-any.whl.metadata (3.0 kB)
Discarding https://download.pytorch.org/whl/typing_extensions-4.12.2-py3-none-any.whl#sha256=04e5ca0351e0f3f85c6853954072df659d0d13fac324d0072316b67d7794700d (from https://download.pytorch.org/whl/cu118/typing-extensions/): Requested typing-extensions>=4.10.0 from https://download.pytorch.org/whl/typing_extensions-4.12.2-py3-none-any.whl#sha256=04e5ca0351e0f3f85c6853954072df659d0d13fac324d0072316b67d7794700d (from torch) has inconsistent Name: expected 'typing-extensions', but metadata has 'typing_extensions'
Collecting torch
  Obtaining dependency information for torch from https://download.pytorch.org/whl/cu118/torch-2.7.0%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torch-2.7.0%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (28 kB)
Collecting triton==3.3.0
  Obtaining dependency information for triton==3.3.0 from https://download.pytorch.org/whl/triton-3.3.0-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/triton-3.3.0-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (1.5 kB)
Collecting torch
  Obtaining dependency information for torch from https://download.pytorch.org/whl/cu118/torch-2.6.0%2Bcu118-cp310-cp310-linux_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torch-2.6.0%2Bcu118-cp310-cp310-linux_x86_64.whl.metadata (27 kB)
Collecting sympy==1.13.1
  Using cached https://download.pytorch.org/whl/sympy-1.13.1-py3-none-any.whl (6.2 MB)
Collecting triton==3.2.0
  Obtaining dependency information for triton==3.2.0 from https://download.pytorch.org/whl/triton-3.2.0-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/triton-3.2.0-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (1.4 kB)
Collecting torch
  Using cached https://download.pytorch.org/whl/cu118/torch-2.5.1%2Bcu118-cp310-cp310-linux_x86_64.whl (838.3 MB)
Collecting triton==3.1.0
  Using cached https://download.pytorch.org/whl/triton-3.1.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (209.5 MB)
Collecting typing-extensions>=4.8.0
  Using cached https://download.pytorch.org/whl/typing_extensions-4.9.0-py3-none-any.whl (32 kB)
Collecting nvidia-cublas-cu11==11.11.3.6
  Using cached https://download.pytorch.org/whl/cu118/nvidia_cublas_cu11-11.11.3.6-py3-none-manylinux1_x86_64.whl (417.9 MB)
Collecting mpmath<1.4,>=1.1.0
  Using cached https://download.pytorch.org/whl/mpmath-1.3.0-py3-none-any.whl (536 kB)
Collecting pillow!=8.3.*,>=5.3.0
  Obtaining dependency information for pillow!=8.3.*,>=5.3.0 from https://download.pytorch.org/whl/pillow-11.0.0-cp310-cp310-manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/pillow-11.0.0-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (9.1 kB)
Collecting numpy
  Obtaining dependency information for numpy from https://download.pytorch.org/whl/numpy-2.1.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/numpy-2.1.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (60 kB)
INFO: pip is looking at multiple versions of torchvision to determine which version is compatible with other requirements. This could take a while.
Collecting torchvision
  Obtaining dependency information for torchvision from https://download.pytorch.org/whl/cu118/torchvision-0.22.0%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torchvision-0.22.0%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (6.1 kB)
  Obtaining dependency information for torchvision from https://download.pytorch.org/whl/cu118/torchvision-0.21.0%2Bcu118-cp310-cp310-linux_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torchvision-0.21.0%2Bcu118-cp310-cp310-linux_x86_64.whl.metadata (6.1 kB)
  Using cached https://download.pytorch.org/whl/cu118/torchvision-0.20.1%2Bcu118-cp310-cp310-linux_x86_64.whl (6.5 MB)
Collecting torchaudio
  Obtaining dependency information for torchaudio from https://download.pytorch.org/whl/cu118/torchaudio-2.7.0%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torchaudio-2.7.0%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (6.6 kB)
  Obtaining dependency information for torchaudio from https://download.pytorch.org/whl/cu118/torchaudio-2.6.0%2Bcu118-cp310-cp310-linux_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torchaudio-2.6.0%2Bcu118-cp310-cp310-linux_x86_64.whl.metadata (6.6 kB)
  Using cached https://download.pytorch.org/whl/cu118/torchaudio-2.5.1%2Bcu118-cp310-cp310-linux_x86_64.whl (3.3 MB)
Collecting MarkupSafe>=2.0
  Using cached https://download.pytorch.org/whl/MarkupSafe-2.1.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)
Using cached https://download.pytorch.org/whl/pillow-11.0.0-cp310-cp310-manylinux_2_28_x86_64.whl (4.4 MB)
Using cached https://download.pytorch.org/whl/filelock-3.13.1-py3-none-any.whl (11 kB)
Using cached https://download.pytorch.org/whl/fsspec-2024.6.1-py3-none-any.whl (177 kB)
Using cached https://download.pytorch.org/whl/networkx-3.3-py3-none-any.whl (1.7 MB)
Using cached https://download.pytorch.org/whl/numpy-2.1.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.3 MB)
Using cached https://download.pytorch.org/whl/pillow-11.0.0-cp310-cp310-manylinux_2_28_x86_64.whl (4.4 MB)
Using cached https://download.pytorch.org/whl/filelock-3.13.1-py3-none-any.whl (11 kB)
Using cached https://download.pytorch.org/whl/fsspec-2024.6.1-py3-none-any.whl (177 kB)
Using cached https://download.pytorch.org/whl/networkx-3.3-py3-none-any.whl (1.7 MB)
Using cached https://download.pytorch.org/whl/numpy-2.1.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.3 MB)
Installing collected packages: mpmath, typing-extensions, sympy, pillow, nvidia-nvtx-cu11, nvidia-nccl-cu11, nvidia-cusparse-cu11, nvidia-curand-cu11, nvidia-cufft-cu11, nvidia-cuda-runtime-cu11, nvidia-cuda-nvrtc-cu11, nvidia-cuda-cupti-cu11, nvidia-cublas-cu11, numpy, networkx, MarkupSafe, fsspec, filelock, triton, nvidia-cusolver-cu11, nvidia-cudnn-cu11, jinja2, torch, torchvision, torchaudio
Successfully installed MarkupSafe-2.1.5 filelock-3.13.1 fsspec-2024.6.1 jinja2-3.1.3 mpmath-1.3.0 networkx-3.3 numpy-2.1.2 nvidia-cublas-cu11-11.11.3.6 nvidia-cuda-cupti-cu11-11.8.87 nvidia-cuda-nvrtc-cu11-11.8.89 nvidia-cuda-runtime-cu11-11.8.89 nvidia-cudnn-cu11-9.1.0.70 nvidia-cufft-cu11-10.9.0.58 nvidia-curand-cu11-10.3.0.86 nvidia-cusolver-cu11-11.4.1.48 nvidia-cusparse-cu11-11.7.5.86 nvidia-nccl-cu11-2.21.5 nvidia-nvtx-cu11-11.8.86 pillow-11.0.0 sympy-1.13.1 torch-2.5.1+cu118 torchaudio-2.5.1+cu118 torchvision-0.20.1+cu118 triton-3.1.0 typing-extensions-4.9.0
WARNING: There was an error checking the latest version of pip.
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install -r requirements/full/requirements.txt
Ignoring llama-cpp-binaries: markers 'platform_system == "Windows" and python_version == "3.11"' don't match your environment
Ignoring llama-cpp-binaries: markers 'platform_system == "Linux" and platform_machine == "x86_64" and python_version == "3.11"' don't match your environment
Ignoring exllamav3: markers 'platform_system == "Windows" and python_version == "3.11"' don't match your environment
Ignoring exllamav3: markers 'platform_system == "Linux" and platform_machine == "x86_64" and python_version == "3.11"' don't match your environment
Ignoring exllamav2: markers 'platform_system == "Windows" and python_version == "3.11"' don't match your environment
Ignoring exllamav2: markers 'platform_system == "Linux" and platform_machine == "x86_64" and python_version == "3.11"' don't match your environment
Ignoring exllamav2: markers 'platform_system == "Linux" and platform_machine != "x86_64"' don't match your environment
Ignoring flash-attn: markers 'platform_system == "Windows" and python_version == "3.11"' don't match your environment
Ignoring flash-attn: markers 'platform_system == "Linux" and platform_machine == "x86_64" and python_version == "3.11"' don't match your environment
Collecting accelerate==1.5.*
  Using cached accelerate-1.5.2-py3-none-any.whl (345 kB)
Collecting bitsandbytes==0.45.*
  Using cached bitsandbytes-0.45.5-py3-none-manylinux_2_24_x86_64.whl (76.1 MB)
Collecting colorama
  Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Collecting datasets
  Using cached datasets-3.6.0-py3-none-any.whl (491 kB)
Collecting duckduckgo_search==8.0.2
  Using cached duckduckgo_search-8.0.2-py3-none-any.whl (18 kB)
Collecting einops
  Using cached einops-0.8.1-py3-none-any.whl (64 kB)
Collecting fastapi==0.112.4
  Using cached fastapi-0.112.4-py3-none-any.whl (93 kB)
Collecting gradio==4.37.*
  Using cached gradio-4.37.2-py3-none-any.whl (12.3 MB)
Collecting html2text==2025.4.15
  Using cached html2text-2025.4.15-py3-none-any.whl (34 kB)
Collecting jinja2==3.1.6
  Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Collecting markdown
  Using cached markdown-3.8.2-py3-none-any.whl (106 kB)
Collecting numpy==2.2.*
  Using cached numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
Collecting pandas
  Using cached pandas-2.3.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.3 MB)
Collecting peft==0.15.*
  Using cached peft-0.15.2-py3-none-any.whl (411 kB)
Requirement already satisfied: Pillow>=9.5.0 in ./.venv/lib/python3.10/site-packages (from -r requirements/full/requirements.txt (line 15)) (11.0.0)
Collecting psutil
  Using cached psutil-7.0.0-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (277 kB)
Collecting pydantic==2.8.2
  Using cached pydantic-2.8.2-py3-none-any.whl (423 kB)
Collecting PyPDF2==3.0.1
  Using cached pypdf2-3.0.1-py3-none-any.whl (232 kB)
Collecting python-docx==1.1.2
  Using cached python_docx-1.1.2-py3-none-any.whl (244 kB)
Collecting pyyaml
  Using cached PyYAML-6.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (751 kB)
Collecting requests
  Using cached requests-2.32.4-py3-none-any.whl (64 kB)
Collecting rich
  Using cached rich-14.0.0-py3-none-any.whl (243 kB)
Collecting safetensors==0.5.*
  Using cached safetensors-0.5.3-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (471 kB)
Collecting scipy
  Using cached scipy-1.15.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (37.7 MB)
Collecting sentencepiece
  Using cached sentencepiece-0.2.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.3 MB)
Collecting tensorboard
  Using cached tensorboard-2.19.0-py3-none-any.whl (5.5 MB)
Collecting transformers==4.50.*
  Using cached transformers-4.50.3-py3-none-any.whl (10.2 MB)
Collecting tqdm
  Using cached tqdm-4.67.1-py3-none-any.whl (78 kB)
Collecting wandb
  Using cached wandb-0.20.1-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23.2 MB)
Collecting flask_cloudflared==0.0.14
  Using cached flask_cloudflared-0.0.14-py3-none-any.whl (6.4 kB)
Collecting sse-starlette==1.6.5
  Using cached sse_starlette-1.6.5-py3-none-any.whl (9.6 kB)
Collecting tiktoken
  Using cached tiktoken-0.9.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.2 MB)
Collecting packaging>=20.0
  Using cached packaging-25.0-py3-none-any.whl (66 kB)
Requirement already satisfied: torch>=2.0.0 in ./.venv/lib/python3.10/site-packages (from accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (2.5.1+cu118)
Collecting huggingface-hub>=0.21.0
  Using cached huggingface_hub-0.33.0-py3-none-any.whl (514 kB)
Collecting click>=8.1.8
  Using cached click-8.2.1-py3-none-any.whl (102 kB)
Collecting lxml>=5.3.0
  Using cached lxml-5.4.0-cp310-cp310-manylinux_2_28_x86_64.whl (5.1 MB)
Collecting primp>=0.15.0
  Using cached primp-0.15.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.3 MB)
Collecting starlette<0.39.0,>=0.37.2
  Using cached starlette-0.38.6-py3-none-any.whl (71 kB)
Requirement already satisfied: typing-extensions>=4.8.0 in ./.venv/lib/python3.10/site-packages (from fastapi==0.112.4->-r requirements/full/requirements.txt (line 7)) (4.9.0)
Collecting ffmpy
  Using cached ffmpy-0.6.0-py3-none-any.whl (5.5 kB)
Collecting altair<6.0,>=4.2.0
  Using cached altair-5.5.0-py3-none-any.whl (731 kB)
Collecting pydub
  Using cached pydub-0.25.1-py2.py3-none-any.whl (32 kB)
Collecting Pillow>=9.5.0
  Using cached pillow-10.4.0-cp310-cp310-manylinux_2_28_x86_64.whl (4.5 MB)
Collecting semantic-version~=2.0
  Using cached semantic_version-2.10.0-py2.py3-none-any.whl (15 kB)
Collecting aiofiles<24.0,>=22.0
  Using cached aiofiles-23.2.1-py3-none-any.whl (15 kB)
Collecting matplotlib~=3.0
  Using cached matplotlib-3.10.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (8.6 MB)
Collecting importlib-resources<7.0,>=1.3
  Using cached importlib_resources-6.5.2-py3-none-any.whl (37 kB)
Requirement already satisfied: markupsafe~=2.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (2.1.5)
Collecting uvicorn>=0.14.0
  Using cached uvicorn-0.34.3-py3-none-any.whl (62 kB)
Collecting ruff>=0.2.2
  Using cached ruff-0.12.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.6 MB)
Collecting gradio-client==1.0.2
  Using cached gradio_client-1.0.2-py3-none-any.whl (318 kB)
Collecting python-multipart>=0.0.9
  Using cached python_multipart-0.0.20-py3-none-any.whl (24 kB)
Collecting orjson~=3.0
  Using cached orjson-3.10.18-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (132 kB)
Collecting httpx>=0.24.1
  Using cached httpx-0.28.1-py3-none-any.whl (73 kB)
Collecting tomlkit==0.12.0
  Using cached tomlkit-0.12.0-py3-none-any.whl (37 kB)
Collecting typer<1.0,>=0.12
  Using cached typer-0.16.0-py3-none-any.whl (46 kB)
Collecting urllib3~=2.0
  Using cached urllib3-2.5.0-py3-none-any.whl (129 kB)
Collecting pydantic-core==2.20.1
  Using cached pydantic_core-2.20.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
Collecting annotated-types>=0.4.0
  Using cached annotated_types-0.7.0-py3-none-any.whl (13 kB)
Requirement already satisfied: filelock in ./.venv/lib/python3.10/site-packages (from transformers==4.50.*->-r requirements/full/requirements.txt (line 27)) (3.13.1)
Collecting regex!=2019.12.17
  Using cached regex-2024.11.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (781 kB)
Collecting tokenizers<0.22,>=0.21
  Using cached tokenizers-0.21.2-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
Collecting Flask>=0.8
  Using cached flask-3.1.1-py3-none-any.whl (103 kB)
Requirement already satisfied: fsspec in ./.venv/lib/python3.10/site-packages (from gradio-client==1.0.2->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (2024.6.1)
Collecting websockets<12.0,>=10.0
  Using cached websockets-11.0.3-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (129 kB)
Collecting dill<0.3.9,>=0.3.0
  Using cached dill-0.3.8-py3-none-any.whl (116 kB)
Collecting multiprocess<0.70.17
  Using cached multiprocess-0.70.16-py310-none-any.whl (134 kB)
Collecting pyarrow>=15.0.0
  Using cached pyarrow-20.0.0-cp310-cp310-manylinux_2_28_x86_64.whl (42.3 MB)
Collecting xxhash
  Using cached xxhash-3.5.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (194 kB)
Collecting python-dateutil>=2.8.2
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Collecting pytz>=2020.1
  Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Collecting tzdata>=2022.7
  Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Collecting certifi>=2017.4.17
  Using cached certifi-2025.6.15-py3-none-any.whl (157 kB)
Collecting charset_normalizer<4,>=2
  Using cached charset_normalizer-3.4.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (149 kB)
Collecting idna<4,>=2.5
  Using cached idna-3.10-py3-none-any.whl (70 kB)
Collecting pygments<3.0.0,>=2.13.0
  Using cached pygments-2.19.2-py3-none-any.whl (1.2 MB)
Collecting markdown-it-py>=2.2.0
  Using cached markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
Collecting absl-py>=0.4
  Using cached absl_py-2.3.0-py3-none-any.whl (135 kB)
Collecting grpcio>=1.48.2
  Using cached grpcio-1.73.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (6.0 MB)
Collecting tensorboard-data-server<0.8.0,>=0.7.0
  Using cached tensorboard_data_server-0.7.2-py3-none-manylinux_2_31_x86_64.whl (6.6 MB)
Collecting six>1.9
  Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Requirement already satisfied: setuptools>=41.0.0 in ./.venv/lib/python3.10/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (65.5.0)
Collecting werkzeug>=1.0.1
  Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
Collecting protobuf!=4.24.0,>=3.19.6
  Using cached protobuf-6.31.1-cp39-abi3-manylinux2014_x86_64.whl (321 kB)
Collecting gitpython!=3.1.29,>=1.0.0
  Using cached GitPython-3.1.44-py3-none-any.whl (207 kB)
Collecting sentry-sdk>=2.0.0
  Using cached sentry_sdk-2.31.0-py2.py3-none-any.whl (355 kB)
Collecting setproctitle
  Using cached setproctitle-1.3.6-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (30 kB)
Collecting platformdirs
  Using cached platformdirs-4.3.8-py3-none-any.whl (18 kB)
Collecting narwhals>=1.14.2
  Using cached narwhals-1.44.0-py3-none-any.whl (365 kB)
Collecting typing-extensions>=4.8.0
  Using cached typing_extensions-4.14.0-py3-none-any.whl (43 kB)
Collecting jsonschema>=3.0
  Using cached jsonschema-4.24.0-py3-none-any.whl (88 kB)
Collecting blinker>=1.9.0
  Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Collecting itsdangerous>=2.2.0
  Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Collecting aiohttp!=4.0.0a0,!=4.0.0a1
  Using cached aiohttp-3.12.13-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.6 MB)
Collecting gitdb<5,>=4.0.1
  Using cached gitdb-4.0.12-py3-none-any.whl (62 kB)
Collecting anyio
  Using cached anyio-4.9.0-py3-none-any.whl (100 kB)
Collecting httpcore==1.*
  Using cached httpcore-1.0.9-py3-none-any.whl (78 kB)
Collecting h11>=0.16
  Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Collecting hf-xet<2.0.0,>=1.1.2
  Using cached hf_xet-1.1.5-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
Collecting mdurl~=0.1
  Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Collecting kiwisolver>=1.3.1
  Using cached kiwisolver-1.4.8-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.6 MB)
Collecting contourpy>=1.0.1
  Using cached contourpy-1.3.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (325 kB)
Collecting cycler>=0.10
  Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
Collecting pyparsing>=2.3.1
  Using cached pyparsing-3.2.3-py3-none-any.whl (111 kB)
Collecting fonttools>=4.22.0
  Using cached fonttools-4.58.4-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.8 MB)
Requirement already satisfied: nvidia-cudnn-cu11==9.1.0.70 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (9.1.0.70)
Requirement already satisfied: nvidia-nccl-cu11==2.21.5 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (2.21.5)
Requirement already satisfied: nvidia-cuda-nvrtc-cu11==11.8.89 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.8.89)
Requirement already satisfied: nvidia-cublas-cu11==11.11.3.6 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.11.3.6)
Requirement already satisfied: nvidia-cusparse-cu11==11.7.5.86 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.7.5.86)
Requirement already satisfied: nvidia-nvtx-cu11==11.8.86 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.8.86)
Requirement already satisfied: triton==3.1.0 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (3.1.0)
Requirement already satisfied: nvidia-cusolver-cu11==11.4.1.48 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.4.1.48)
Requirement already satisfied: sympy==1.13.1 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (1.13.1)
Requirement already satisfied: networkx in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (3.3)
Requirement already satisfied: nvidia-cufft-cu11==10.9.0.58 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (10.9.0.58)
Requirement already satisfied: nvidia-curand-cu11==10.3.0.86 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (10.3.0.86)
Requirement already satisfied: nvidia-cuda-runtime-cu11==11.8.89 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.8.89)
Requirement already satisfied: nvidia-cuda-cupti-cu11==11.8.87 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.8.87)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in ./.venv/lib/python3.10/site-packages (from sympy==1.13.1->torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (1.3.0)
Collecting shellingham>=1.3.0
  Using cached shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
Collecting multidict<7.0,>=4.5
  Using cached multidict-6.4.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (219 kB)
Collecting async-timeout<6.0,>=4.0
  Using cached async_timeout-5.0.1-py3-none-any.whl (6.2 kB)
Collecting propcache>=0.2.0
  Using cached propcache-0.3.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (198 kB)
Collecting frozenlist>=1.1.1
  Using cached frozenlist-1.7.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (222 kB)
Collecting attrs>=17.3.0
  Using cached attrs-25.3.0-py3-none-any.whl (63 kB)
Collecting aiosignal>=1.1.2
  Using cached aiosignal-1.3.2-py2.py3-none-any.whl (7.6 kB)
Collecting yarl<2.0,>=1.17.0
  Using cached yarl-1.20.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (326 kB)
Collecting aiohappyeyeballs>=2.5.0
  Using cached aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
Collecting sniffio>=1.1
  Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
Collecting exceptiongroup>=1.0.2
  Using cached exceptiongroup-1.3.0-py3-none-any.whl (16 kB)
Collecting smmap<6,>=3.0.1
  Using cached smmap-5.0.2-py3-none-any.whl (24 kB)
Collecting jsonschema-specifications>=2023.03.6
  Using cached jsonschema_specifications-2025.4.1-py3-none-any.whl (18 kB)
Collecting referencing>=0.28.4
  Using cached referencing-0.36.2-py3-none-any.whl (26 kB)
Collecting rpds-py>=0.7.1
  Using cached rpds_py-0.25.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (386 kB)
Installing collected packages: sentencepiece, pytz, pydub, xxhash, werkzeug, websockets, urllib3, tzdata, typing-extensions, tqdm, tomlkit, tensorboard-data-server, sniffio, smmap, six, shellingham, setproctitle, semantic-version, safetensors, ruff, rpds-py, regex, pyyaml, python-multipart, PyPDF2, pyparsing, pygments, pyarrow, psutil, protobuf, propcache, primp, platformdirs, Pillow, packaging, orjson, numpy, narwhals, mdurl, markdown, lxml, kiwisolver, jinja2, itsdangerous, importlib-resources, idna, html2text, hf-xet, h11, grpcio, frozenlist, fonttools, ffmpy, einops, dill, cycler, colorama, click, charset_normalizer, certifi, blinker, attrs, async-timeout, annotated-types, aiohappyeyeballs, aiofiles, absl-py, uvicorn, tensorboard, sentry-sdk, scipy, requests, referencing, python-docx, python-dateutil, pydantic-core, multiprocess, multidict, markdown-it-py, httpcore, gitdb, Flask, exceptiongroup, duckduckgo_search, contourpy, aiosignal, yarl, tiktoken, rich, pydantic, pandas, matplotlib, jsonschema-specifications, huggingface-hub, gitpython, flask_cloudflared, bitsandbytes, anyio, wandb, typer, tokenizers, starlette, jsonschema, httpx, aiohttp, accelerate, transformers, sse-starlette, gradio-client, fastapi, altair, peft, gradio, datasets
  Attempting uninstall: typing-extensions
    Found existing installation: typing_extensions 4.9.0
    Uninstalling typing_extensions-4.9.0:
      Successfully uninstalled typing_extensions-4.9.0
  Attempting uninstall: Pillow
    Found existing installation: pillow 11.0.0
    Uninstalling pillow-11.0.0:
      Successfully uninstalled pillow-11.0.0
  Attempting uninstall: numpy
    Found existing installation: numpy 2.1.2
    Uninstalling numpy-2.1.2:
      Successfully uninstalled numpy-2.1.2
  Attempting uninstall: jinja2
    Found existing installation: Jinja2 3.1.3
    Uninstalling Jinja2-3.1.3:
      Successfully uninstalled Jinja2-3.1.3
Successfully installed Flask-3.1.1 Pillow-10.4.0 PyPDF2-3.0.1 absl-py-2.3.0 accelerate-1.5.2 aiofiles-23.2.1 aiohappyeyeballs-2.6.1 aiohttp-3.12.13 aiosignal-1.3.2 altair-5.5.0 annotated-types-0.7.0 anyio-4.9.0 async-timeout-5.0.1 attrs-25.3.0 bitsandbytes-0.45.5 blinker-1.9.0 certifi-2025.6.15 charset_normalizer-3.4.2 click-8.2.1 colorama-0.4.6 contourpy-1.3.2 cycler-0.12.1 datasets-3.6.0 dill-0.3.8 duckduckgo_search-8.0.2 einops-0.8.1 exceptiongroup-1.3.0 fastapi-0.112.4 ffmpy-0.6.0 flask_cloudflared-0.0.14 fonttools-4.58.4 frozenlist-1.7.0 gitdb-4.0.12 gitpython-3.1.44 gradio-4.37.2 gradio-client-1.0.2 grpcio-1.73.0 h11-0.16.0 hf-xet-1.1.5 html2text-2025.4.15 httpcore-1.0.9 httpx-0.28.1 huggingface-hub-0.33.0 idna-3.10 importlib-resources-6.5.2 itsdangerous-2.2.0 jinja2-3.1.6 jsonschema-4.24.0 jsonschema-specifications-2025.4.1 kiwisolver-1.4.8 lxml-5.4.0 markdown-3.8.2 markdown-it-py-3.0.0 matplotlib-3.10.3 mdurl-0.1.2 multidict-6.4.4 multiprocess-0.70.16 narwhals-1.44.0 numpy-2.2.6 orjson-3.10.18 packaging-25.0 pandas-2.3.0 peft-0.15.2 platformdirs-4.3.8 primp-0.15.0 propcache-0.3.2 protobuf-6.31.1 psutil-7.0.0 pyarrow-20.0.0 pydantic-

### USER
did those two things, this is where we are: (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
Looking in indexes: https://download.pytorch.org/whl/cu118
Collecting torch
  Obtaining dependency information for torch from https://download.pytorch.org/whl/cu118/torch-2.7.1%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torch-2.7.1%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (28 kB)
Collecting torchvision
  Obtaining dependency information for torchvision from https://download.pytorch.org/whl/cu118/torchvision-0.22.1%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torchvision-0.22.1%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (6.1 kB)
Collecting torchaudio
  Obtaining dependency information for torchaudio from https://download.pytorch.org/whl/cu118/torchaudio-2.7.1%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torchaudio-2.7.1%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (6.6 kB)
Collecting nvidia-nvtx-cu11==11.8.86
  Using cached https://download.pytorch.org/whl/cu118/nvidia_nvtx_cu11-11.8.86-py3-none-manylinux1_x86_64.whl (99 kB)
Collecting networkx
  Obtaining dependency information for networkx from https://download.pytorch.org/whl/networkx-3.3-py3-none-any.whl.metadata
  Using cached https://download.pytorch.org/whl/networkx-3.3-py3-none-any.whl.metadata (5.1 kB)
Collecting sympy>=1.13.3
  Obtaining dependency information for sympy>=1.13.3 from https://download.pytorch.org/whl/sympy-1.13.3-py3-none-any.whl.metadata
  Using cached https://download.pytorch.org/whl/sympy-1.13.3-py3-none-any.whl.metadata (12 kB)
Collecting nvidia-cuda-runtime-cu11==11.8.89
  Using cached https://download.pytorch.org/whl/cu118/nvidia_cuda_runtime_cu11-11.8.89-py3-none-manylinux1_x86_64.whl (875 kB)
Collecting filelock
  Obtaining dependency information for filelock from https://download.pytorch.org/whl/filelock-3.13.1-py3-none-any.whl.metadata
  Using cached https://download.pytorch.org/whl/filelock-3.13.1-py3-none-any.whl.metadata (2.8 kB)
Collecting nvidia-cudnn-cu11==9.1.0.70
  Using cached https://download.pytorch.org/whl/cu118/nvidia_cudnn_cu11-9.1.0.70-py3-none-manylinux2014_x86_64.whl (663.9 MB)
Collecting nvidia-cuda-nvrtc-cu11==11.8.89
  Using cached https://download.pytorch.org/whl/cu118/nvidia_cuda_nvrtc_cu11-11.8.89-py3-none-manylinux1_x86_64.whl (23.2 MB)
Collecting fsspec
  Obtaining dependency information for fsspec from https://download.pytorch.org/whl/fsspec-2024.6.1-py3-none-any.whl.metadata
  Using cached https://download.pytorch.org/whl/fsspec-2024.6.1-py3-none-any.whl.metadata (11 kB)
Collecting nvidia-cufft-cu11==10.9.0.58
  Using cached https://download.pytorch.org/whl/cu118/nvidia_cufft_cu11-10.9.0.58-py3-none-manylinux1_x86_64.whl (168.4 MB)
Collecting nvidia-cusparse-cu11==11.7.5.86
  Using cached https://download.pytorch.org/whl/cu118/nvidia_cusparse_cu11-11.7.5.86-py3-none-manylinux1_x86_64.whl (204.1 MB)
Collecting nvidia-cusolver-cu11==11.4.1.48
  Using cached https://download.pytorch.org/whl/cu118/nvidia_cusolver_cu11-11.4.1.48-py3-none-manylinux1_x86_64.whl (128.2 MB)
Collecting triton==3.3.1
  Obtaining dependency information for triton==3.3.1 from https://download.pytorch.org/whl/triton-3.3.1-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/triton-3.3.1-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (1.5 kB)
Collecting nvidia-curand-cu11==10.3.0.86
  Using cached https://download.pytorch.org/whl/cu118/nvidia_curand_cu11-10.3.0.86-py3-none-manylinux1_x86_64.whl (58.1 MB)
Collecting jinja2
  Obtaining dependency information for jinja2 from https://download.pytorch.org/whl/Jinja2-3.1.4-py3-none-any.whl.metadata
  Using cached https://download.pytorch.org/whl/Jinja2-3.1.4-py3-none-any.whl.metadata (2.6 kB)
Discarding https://download.pytorch.org/whl/Jinja2-3.1.4-py3-none-any.whl#sha256=bc5dd2abb727a5319567b7a813e6a2e7318c39f4f487cfe6c89c6f9c7d25197d (from https://download.pytorch.org/whl/cu118/jinja2/): Requested jinja2 from https://download.pytorch.org/whl/Jinja2-3.1.4-py3-none-any.whl#sha256=bc5dd2abb727a5319567b7a813e6a2e7318c39f4f487cfe6c89c6f9c7d25197d (from torch) has inconsistent Name: expected 'jinja2', but metadata has 'Jinja2'
  Using cached https://download.pytorch.org/whl/Jinja2-3.1.3-py3-none-any.whl (133 kB)
Collecting nvidia-nccl-cu11==2.21.5
  Using cached https://download.pytorch.org/whl/cu118/nvidia_nccl_cu11-2.21.5-py3-none-manylinux2014_x86_64.whl (147.8 MB)
Collecting nvidia-cuda-cupti-cu11==11.8.87
  Using cached https://download.pytorch.org/whl/cu118/nvidia_cuda_cupti_cu11-11.8.87-py3-none-manylinux1_x86_64.whl (13.1 MB)
Collecting typing-extensions>=4.10.0
  Obtaining dependency information for typing-extensions>=4.10.0 from https://download.pytorch.org/whl/typing_extensions-4.12.2-py3-none-any.whl.metadata
  Using cached https://download.pytorch.org/whl/typing_extensions-4.12.2-py3-none-any.whl.metadata (3.0 kB)
Discarding https://download.pytorch.org/whl/typing_extensions-4.12.2-py3-none-any.whl#sha256=04e5ca0351e0f3f85c6853954072df659d0d13fac324d0072316b67d7794700d (from https://download.pytorch.org/whl/cu118/typing-extensions/): Requested typing-extensions>=4.10.0 from https://download.pytorch.org/whl/typing_extensions-4.12.2-py3-none-any.whl#sha256=04e5ca0351e0f3f85c6853954072df659d0d13fac324d0072316b67d7794700d (from torch) has inconsistent Name: expected 'typing-extensions', but metadata has 'typing_extensions'
Collecting torch
  Obtaining dependency information for torch from https://download.pytorch.org/whl/cu118/torch-2.7.0%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torch-2.7.0%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (28 kB)
Collecting triton==3.3.0
  Obtaining dependency information for triton==3.3.0 from https://download.pytorch.org/whl/triton-3.3.0-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/triton-3.3.0-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (1.5 kB)
Collecting torch
  Obtaining dependency information for torch from https://download.pytorch.org/whl/cu118/torch-2.6.0%2Bcu118-cp310-cp310-linux_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torch-2.6.0%2Bcu118-cp310-cp310-linux_x86_64.whl.metadata (27 kB)
Collecting sympy==1.13.1
  Using cached https://download.pytorch.org/whl/sympy-1.13.1-py3-none-any.whl (6.2 MB)
Collecting triton==3.2.0
  Obtaining dependency information for triton==3.2.0 from https://download.pytorch.org/whl/triton-3.2.0-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/triton-3.2.0-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (1.4 kB)
Collecting torch
  Using cached https://download.pytorch.org/whl/cu118/torch-2.5.1%2Bcu118-cp310-cp310-linux_x86_64.whl (838.3 MB)
Collecting triton==3.1.0
  Using cached https://download.pytorch.org/whl/triton-3.1.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (209.5 MB)
Collecting typing-extensions>=4.8.0
  Using cached https://download.pytorch.org/whl/typing_extensions-4.9.0-py3-none-any.whl (32 kB)
Collecting nvidia-cublas-cu11==11.11.3.6
  Using cached https://download.pytorch.org/whl/cu118/nvidia_cublas_cu11-11.11.3.6-py3-none-manylinux1_x86_64.whl (417.9 MB)
Collecting mpmath<1.4,>=1.1.0
  Using cached https://download.pytorch.org/whl/mpmath-1.3.0-py3-none-any.whl (536 kB)
Collecting pillow!=8.3.*,>=5.3.0
  Obtaining dependency information for pillow!=8.3.*,>=5.3.0 from https://download.pytorch.org/whl/pillow-11.0.0-cp310-cp310-manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/pillow-11.0.0-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (9.1 kB)
Collecting numpy
  Obtaining dependency information for numpy from https://download.pytorch.org/whl/numpy-2.1.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/numpy-2.1.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (60 kB)
INFO: pip is looking at multiple versions of torchvision to determine which version is compatible with other requirements. This could take a while.
Collecting torchvision
  Obtaining dependency information for torchvision from https://download.pytorch.org/whl/cu118/torchvision-0.22.0%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torchvision-0.22.0%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (6.1 kB)
  Obtaining dependency information for torchvision from https://download.pytorch.org/whl/cu118/torchvision-0.21.0%2Bcu118-cp310-cp310-linux_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torchvision-0.21.0%2Bcu118-cp310-cp310-linux_x86_64.whl.metadata (6.1 kB)
  Using cached https://download.pytorch.org/whl/cu118/torchvision-0.20.1%2Bcu118-cp310-cp310-linux_x86_64.whl (6.5 MB)
Collecting torchaudio
  Obtaining dependency information for torchaudio from https://download.pytorch.org/whl/cu118/torchaudio-2.7.0%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torchaudio-2.7.0%2Bcu118-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (6.6 kB)
  Obtaining dependency information for torchaudio from https://download.pytorch.org/whl/cu118/torchaudio-2.6.0%2Bcu118-cp310-cp310-linux_x86_64.whl.metadata
  Using cached https://download.pytorch.org/whl/cu118/torchaudio-2.6.0%2Bcu118-cp310-cp310-linux_x86_64.whl.metadata (6.6 kB)
  Using cached https://download.pytorch.org/whl/cu118/torchaudio-2.5.1%2Bcu118-cp310-cp310-linux_x86_64.whl (3.3 MB)
Collecting MarkupSafe>=2.0
  Using cached https://download.pytorch.org/whl/MarkupSafe-2.1.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)
Using cached https://download.pytorch.org/whl/pillow-11.0.0-cp310-cp310-manylinux_2_28_x86_64.whl (4.4 MB)
Using cached https://download.pytorch.org/whl/filelock-3.13.1-py3-none-any.whl (11 kB)
Using cached https://download.pytorch.org/whl/fsspec-2024.6.1-py3-none-any.whl (177 kB)
Using cached https://download.pytorch.org/whl/networkx-3.3-py3-none-any.whl (1.7 MB)
Using cached https://download.pytorch.org/whl/numpy-2.1.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.3 MB)
Using cached https://download.pytorch.org/whl/pillow-11.0.0-cp310-cp310-manylinux_2_28_x86_64.whl (4.4 MB)
Using cached https://download.pytorch.org/whl/filelock-3.13.1-py3-none-any.whl (11 kB)
Using cached https://download.pytorch.org/whl/fsspec-2024.6.1-py3-none-any.whl (177 kB)
Using cached https://download.pytorch.org/whl/networkx-3.3-py3-none-any.whl (1.7 MB)
Using cached https://download.pytorch.org/whl/numpy-2.1.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.3 MB)
Installing collected packages: mpmath, typing-extensions, sympy, pillow, nvidia-nvtx-cu11, nvidia-nccl-cu11, nvidia-cusparse-cu11, nvidia-curand-cu11, nvidia-cufft-cu11, nvidia-cuda-runtime-cu11, nvidia-cuda-nvrtc-cu11, nvidia-cuda-cupti-cu11, nvidia-cublas-cu11, numpy, networkx, MarkupSafe, fsspec, filelock, triton, nvidia-cusolver-cu11, nvidia-cudnn-cu11, jinja2, torch, torchvision, torchaudio
Successfully installed MarkupSafe-2.1.5 filelock-3.13.1 fsspec-2024.6.1 jinja2-3.1.3 mpmath-1.3.0 networkx-3.3 numpy-2.1.2 nvidia-cublas-cu11-11.11.3.6 nvidia-cuda-cupti-cu11-11.8.87 nvidia-cuda-nvrtc-cu11-11.8.89 nvidia-cuda-runtime-cu11-11.8.89 nvidia-cudnn-cu11-9.1.0.70 nvidia-cufft-cu11-10.9.0.58 nvidia-curand-cu11-10.3.0.86 nvidia-cusolver-cu11-11.4.1.48 nvidia-cusparse-cu11-11.7.5.86 nvidia-nccl-cu11-2.21.5 nvidia-nvtx-cu11-11.8.86 pillow-11.0.0 sympy-1.13.1 torch-2.5.1+cu118 torchaudio-2.5.1+cu118 torchvision-0.20.1+cu118 triton-3.1.0 typing-extensions-4.9.0
WARNING: There was an error checking the latest version of pip.
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install -r requirements/full/requirements.txt
Ignoring llama-cpp-binaries: markers 'platform_system == "Windows" and python_version == "3.11"' don't match your environment
Ignoring llama-cpp-binaries: markers 'platform_system == "Linux" and platform_machine == "x86_64" and python_version == "3.11"' don't match your environment
Ignoring exllamav3: markers 'platform_system == "Windows" and python_version == "3.11"' don't match your environment
Ignoring exllamav3: markers 'platform_system == "Linux" and platform_machine == "x86_64" and python_version == "3.11"' don't match your environment
Ignoring exllamav2: markers 'platform_system == "Windows" and python_version == "3.11"' don't match your environment
Ignoring exllamav2: markers 'platform_system == "Linux" and platform_machine == "x86_64" and python_version == "3.11"' don't match your environment
Ignoring exllamav2: markers 'platform_system == "Linux" and platform_machine != "x86_64"' don't match your environment
Ignoring flash-attn: markers 'platform_system == "Windows" and python_version == "3.11"' don't match your environment
Ignoring flash-attn: markers 'platform_system == "Linux" and platform_machine == "x86_64" and python_version == "3.11"' don't match your environment
Collecting accelerate==1.5.*
  Using cached accelerate-1.5.2-py3-none-any.whl (345 kB)
Collecting bitsandbytes==0.45.*
  Using cached bitsandbytes-0.45.5-py3-none-manylinux_2_24_x86_64.whl (76.1 MB)
Collecting colorama
  Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Collecting datasets
  Using cached datasets-3.6.0-py3-none-any.whl (491 kB)
Collecting duckduckgo_search==8.0.2
  Using cached duckduckgo_search-8.0.2-py3-none-any.whl (18 kB)
Collecting einops
  Using cached einops-0.8.1-py3-none-any.whl (64 kB)
Collecting fastapi==0.112.4
  Using cached fastapi-0.112.4-py3-none-any.whl (93 kB)
Collecting gradio==4.37.*
  Using cached gradio-4.37.2-py3-none-any.whl (12.3 MB)
Collecting html2text==2025.4.15
  Using cached html2text-2025.4.15-py3-none-any.whl (34 kB)
Collecting jinja2==3.1.6
  Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Collecting markdown
  Using cached markdown-3.8.2-py3-none-any.whl (106 kB)
Collecting numpy==2.2.*
  Using cached numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
Collecting pandas
  Using cached pandas-2.3.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.3 MB)
Collecting peft==0.15.*
  Using cached peft-0.15.2-py3-none-any.whl (411 kB)
Requirement already satisfied: Pillow>=9.5.0 in ./.venv/lib/python3.10/site-packages (from -r requirements/full/requirements.txt (line 15)) (11.0.0)
Collecting psutil
  Using cached psutil-7.0.0-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (277 kB)
Collecting pydantic==2.8.2
  Using cached pydantic-2.8.2-py3-none-any.whl (423 kB)
Collecting PyPDF2==3.0.1
  Using cached pypdf2-3.0.1-py3-none-any.whl (232 kB)
Collecting python-docx==1.1.2
  Using cached python_docx-1.1.2-py3-none-any.whl (244 kB)
Collecting pyyaml
  Using cached PyYAML-6.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (751 kB)
Collecting requests
  Using cached requests-2.32.4-py3-none-any.whl (64 kB)
Collecting rich
  Using cached rich-14.0.0-py3-none-any.whl (243 kB)
Collecting safetensors==0.5.*
  Using cached safetensors-0.5.3-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (471 kB)
Collecting scipy
  Using cached scipy-1.15.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (37.7 MB)
Collecting sentencepiece
  Using cached sentencepiece-0.2.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.3 MB)
Collecting tensorboard
  Using cached tensorboard-2.19.0-py3-none-any.whl (5.5 MB)
Collecting transformers==4.50.*
  Using cached transformers-4.50.3-py3-none-any.whl (10.2 MB)
Collecting tqdm
  Using cached tqdm-4.67.1-py3-none-any.whl (78 kB)
Collecting wandb
  Using cached wandb-0.20.1-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23.2 MB)
Collecting flask_cloudflared==0.0.14
  Using cached flask_cloudflared-0.0.14-py3-none-any.whl (6.4 kB)
Collecting sse-starlette==1.6.5
  Using cached sse_starlette-1.6.5-py3-none-any.whl (9.6 kB)
Collecting tiktoken
  Using cached tiktoken-0.9.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.2 MB)
Collecting packaging>=20.0
  Using cached packaging-25.0-py3-none-any.whl (66 kB)
Requirement already satisfied: torch>=2.0.0 in ./.venv/lib/python3.10/site-packages (from accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (2.5.1+cu118)
Collecting huggingface-hub>=0.21.0
  Using cached huggingface_hub-0.33.0-py3-none-any.whl (514 kB)
Collecting click>=8.1.8
  Using cached click-8.2.1-py3-none-any.whl (102 kB)
Collecting lxml>=5.3.0
  Using cached lxml-5.4.0-cp310-cp310-manylinux_2_28_x86_64.whl (5.1 MB)
Collecting primp>=0.15.0
  Using cached primp-0.15.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.3 MB)
Collecting starlette<0.39.0,>=0.37.2
  Using cached starlette-0.38.6-py3-none-any.whl (71 kB)
Requirement already satisfied: typing-extensions>=4.8.0 in ./.venv/lib/python3.10/site-packages (from fastapi==0.112.4->-r requirements/full/requirements.txt (line 7)) (4.9.0)
Collecting ffmpy
  Using cached ffmpy-0.6.0-py3-none-any.whl (5.5 kB)
Collecting altair<6.0,>=4.2.0
  Using cached altair-5.5.0-py3-none-any.whl (731 kB)
Collecting pydub
  Using cached pydub-0.25.1-py2.py3-none-any.whl (32 kB)
Collecting Pillow>=9.5.0
  Using cached pillow-10.4.0-cp310-cp310-manylinux_2_28_x86_64.whl (4.5 MB)
Collecting semantic-version~=2.0
  Using cached semantic_version-2.10.0-py2.py3-none-any.whl (15 kB)
Collecting aiofiles<24.0,>=22.0
  Using cached aiofiles-23.2.1-py3-none-any.whl (15 kB)
Collecting matplotlib~=3.0
  Using cached matplotlib-3.10.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (8.6 MB)
Collecting importlib-resources<7.0,>=1.3
  Using cached importlib_resources-6.5.2-py3-none-any.whl (37 kB)
Requirement already satisfied: markupsafe~=2.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (2.1.5)
Collecting uvicorn>=0.14.0
  Using cached uvicorn-0.34.3-py3-none-any.whl (62 kB)
Collecting ruff>=0.2.2
  Using cached ruff-0.12.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.6 MB)
Collecting gradio-client==1.0.2
  Using cached gradio_client-1.0.2-py3-none-any.whl (318 kB)
Collecting python-multipart>=0.0.9
  Using cached python_multipart-0.0.20-py3-none-any.whl (24 kB)
Collecting orjson~=3.0
  Using cached orjson-3.10.18-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (132 kB)
Collecting httpx>=0.24.1
  Using cached httpx-0.28.1-py3-none-any.whl (73 kB)
Collecting tomlkit==0.12.0
  Using cached tomlkit-0.12.0-py3-none-any.whl (37 kB)
Collecting typer<1.0,>=0.12
  Using cached typer-0.16.0-py3-none-any.whl (46 kB)
Collecting urllib3~=2.0
  Using cached urllib3-2.5.0-py3-none-any.whl (129 kB)
Collecting pydantic-core==2.20.1
  Using cached pydantic_core-2.20.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
Collecting annotated-types>=0.4.0
  Using cached annotated_types-0.7.0-py3-none-any.whl (13 kB)
Requirement already satisfied: filelock in ./.venv/lib/python3.10/site-packages (from transformers==4.50.*->-r requirements/full/requirements.txt (line 27)) (3.13.1)
Collecting regex!=2019.12.17
  Using cached regex-2024.11.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (781 kB)
Collecting tokenizers<0.22,>=0.21
  Using cached tokenizers-0.21.2-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
Collecting Flask>=0.8
  Using cached flask-3.1.1-py3-none-any.whl (103 kB)
Requirement already satisfied: fsspec in ./.venv/lib/python3.10/site-packages (from gradio-client==1.0.2->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (2024.6.1)
Collecting websockets<12.0,>=10.0
  Using cached websockets-11.0.3-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (129 kB)
Collecting dill<0.3.9,>=0.3.0
  Using cached dill-0.3.8-py3-none-any.whl (116 kB)
Collecting multiprocess<0.70.17
  Using cached multiprocess-0.70.16-py310-none-any.whl (134 kB)
Collecting pyarrow>=15.0.0
  Using cached pyarrow-20.0.0-cp310-cp310-manylinux_2_28_x86_64.whl (42.3 MB)
Collecting xxhash
  Using cached xxhash-3.5.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (194 kB)
Collecting python-dateutil>=2.8.2
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Collecting pytz>=2020.1
  Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Collecting tzdata>=2022.7
  Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Collecting certifi>=2017.4.17
  Using cached certifi-2025.6.15-py3-none-any.whl (157 kB)
Collecting charset_normalizer<4,>=2
  Using cached charset_normalizer-3.4.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (149 kB)
Collecting idna<4,>=2.5
  Using cached idna-3.10-py3-none-any.whl (70 kB)
Collecting pygments<3.0.0,>=2.13.0
  Using cached pygments-2.19.2-py3-none-any.whl (1.2 MB)
Collecting markdown-it-py>=2.2.0
  Using cached markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
Collecting absl-py>=0.4
  Using cached absl_py-2.3.0-py3-none-any.whl (135 kB)
Collecting grpcio>=1.48.2
  Using cached grpcio-1.73.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (6.0 MB)
Collecting tensorboard-data-server<0.8.0,>=0.7.0
  Using cached tensorboard_data_server-0.7.2-py3-none-manylinux_2_31_x86_64.whl (6.6 MB)
Collecting six>1.9
  Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Requirement already satisfied: setuptools>=41.0.0 in ./.venv/lib/python3.10/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (65.5.0)
Collecting werkzeug>=1.0.1
  Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
Collecting protobuf!=4.24.0,>=3.19.6
  Using cached protobuf-6.31.1-cp39-abi3-manylinux2014_x86_64.whl (321 kB)
Collecting gitpython!=3.1.29,>=1.0.0
  Using cached GitPython-3.1.44-py3-none-any.whl (207 kB)
Collecting sentry-sdk>=2.0.0
  Using cached sentry_sdk-2.31.0-py2.py3-none-any.whl (355 kB)
Collecting setproctitle
  Using cached setproctitle-1.3.6-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (30 kB)
Collecting platformdirs
  Using cached platformdirs-4.3.8-py3-none-any.whl (18 kB)
Collecting narwhals>=1.14.2
  Using cached narwhals-1.44.0-py3-none-any.whl (365 kB)
Collecting typing-extensions>=4.8.0
  Using cached typing_extensions-4.14.0-py3-none-any.whl (43 kB)
Collecting jsonschema>=3.0
  Using cached jsonschema-4.24.0-py3-none-any.whl (88 kB)
Collecting blinker>=1.9.0
  Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Collecting itsdangerous>=2.2.0
  Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Collecting aiohttp!=4.0.0a0,!=4.0.0a1
  Using cached aiohttp-3.12.13-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.6 MB)
Collecting gitdb<5,>=4.0.1
  Using cached gitdb-4.0.12-py3-none-any.whl (62 kB)
Collecting anyio
  Using cached anyio-4.9.0-py3-none-any.whl (100 kB)
Collecting httpcore==1.*
  Using cached httpcore-1.0.9-py3-none-any.whl (78 kB)
Collecting h11>=0.16
  Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Collecting hf-xet<2.0.0,>=1.1.2
  Using cached hf_xet-1.1.5-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
Collecting mdurl~=0.1
  Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Collecting kiwisolver>=1.3.1
  Using cached kiwisolver-1.4.8-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.6 MB)
Collecting contourpy>=1.0.1
  Using cached contourpy-1.3.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (325 kB)
Collecting cycler>=0.10
  Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
Collecting pyparsing>=2.3.1
  Using cached pyparsing-3.2.3-py3-none-any.whl (111 kB)
Collecting fonttools>=4.22.0
  Using cached fonttools-4.58.4-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.8 MB)
Requirement already satisfied: nvidia-cudnn-cu11==9.1.0.70 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (9.1.0.70)
Requirement already satisfied: nvidia-nccl-cu11==2.21.5 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (2.21.5)
Requirement already satisfied: nvidia-cuda-nvrtc-cu11==11.8.89 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.8.89)
Requirement already satisfied: nvidia-cublas-cu11==11.11.3.6 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.11.3.6)
Requirement already satisfied: nvidia-cusparse-cu11==11.7.5.86 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.7.5.86)
Requirement already satisfied: nvidia-nvtx-cu11==11.8.86 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.8.86)
Requirement already satisfied: triton==3.1.0 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (3.1.0)
Requirement already satisfied: nvidia-cusolver-cu11==11.4.1.48 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.4.1.48)
Requirement already satisfied: sympy==1.13.1 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (1.13.1)
Requirement already satisfied: networkx in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (3.3)
Requirement already satisfied: nvidia-cufft-cu11==10.9.0.58 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (10.9.0.58)
Requirement already satisfied: nvidia-curand-cu11==10.3.0.86 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (10.3.0.86)
Requirement already satisfied: nvidia-cuda-runtime-cu11==11.8.89 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.8.89)
Requirement already satisfied: nvidia-cuda-cupti-cu11==11.8.87 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.8.87)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in ./.venv/lib/python3.10/site-packages (from sympy==1.13.1->torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (1.3.0)
Collecting shellingham>=1.3.0
  Using cached shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
Collecting multidict<7.0,>=4.5
  Using cached multidict-6.4.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (219 kB)
Collecting async-timeout<6.0,>=4.0
  Using cached async_timeout-5.0.1-py3-none-any.whl (6.2 kB)
Collecting propcache>=0.2.0
  Using cached propcache-0.3.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (198 kB)
Collecting frozenlist>=1.1.1
  Using cached frozenlist-1.7.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (222 kB)
Collecting attrs>=17.3.0
  Using cached attrs-25.3.0-py3-none-any.whl (63 kB)
Collecting aiosignal>=1.1.2
  Using cached aiosignal-1.3.2-py2.py3-none-any.whl (7.6 kB)
Collecting yarl<2.0,>=1.17.0
  Using cached yarl-1.20.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (326 kB)
Collecting aiohappyeyeballs>=2.5.0
  Using cached aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
Collecting sniffio>=1.1
  Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
Collecting exceptiongroup>=1.0.2
  Using cached exceptiongroup-1.3.0-py3-none-any.whl (16 kB)
Collecting smmap<6,>=3.0.1
  Using cached smmap-5.0.2-py3-none-any.whl (24 kB)
Collecting jsonschema-specifications>=2023.03.6
  Using cached jsonschema_specifications-2025.4.1-py3-none-any.whl (18 kB)
Collecting referencing>=0.28.4
  Using cached referencing-0.36.2-py3-none-any.whl (26 kB)
Collecting rpds-py>=0.7.1
  Using cached rpds_py-0.25.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (386 kB)
Installing collected packages: sentencepiece, pytz, pydub, xxhash, werkzeug, websockets, urllib3, tzdata, typing-extensions, tqdm, tomlkit, tensorboard-data-server, sniffio, smmap, six, shellingham, setproctitle, semantic-version, safetensors, ruff, rpds-py, regex, pyyaml, python-multipart, PyPDF2, pyparsing, pygments, pyarrow, psutil, protobuf, propcache, primp, platformdirs, Pillow, packaging, orjson, numpy, narwhals, mdurl, markdown, lxml, kiwisolver, jinja2, itsdangerous, importlib-resources, idna, html2text, hf-xet, h11, grpcio, frozenlist, fonttools, ffmpy, einops, dill, cycler, colorama, click, charset_normalizer, certifi, blinker, attrs, async-timeout, annotated-types, aiohappyeyeballs, aiofiles, absl-py, uvicorn, tensorboard, sentry-sdk, scipy, requests, referencing, python-docx, python-dateutil, pydantic-core, multiprocess, multidict, markdown-it-py, httpcore, gitdb, Flask, exceptiongroup, duckduckgo_search, contourpy, aiosignal, yarl, tiktoken, rich, pydantic, pandas, matplotlib, jsonschema-specifications, huggingface-hub, gitpython, flask_cloudflared, bitsandbytes, anyio, wandb, typer, tokenizers, starlette, jsonschema, httpx, aiohttp, accelerate, transformers, sse-starlette, gradio-client, fastapi, altair, peft, gradio, datasets
  Attempting uninstall: typing-extensions
    Found existing installation: typing_extensions 4.9.0
    Uninstalling typing_extensions-4.9.0:
      Successfully uninstalled typing_extensions-4.9.0
  Attempting uninstall: Pillow
    Found existing installation: pillow 11.0.0
    Uninstalling pillow-11.0.0:
      Successfully uninstalled pillow-11.0.0
  Attempting uninstall: numpy
    Found existing installation: numpy 2.1.2
    Uninstalling numpy-2.1.2:
      Successfully uninstalled numpy-2.1.2
  Attempting uninstall: jinja2
    Found existing installation: Jinja2 3.1.3
    Uninstalling Jinja2-3.1.3:
      Successfully uninstalled Jinja2-3.1.3
Successfully installed Flask-3.1.1 Pillow-10.4.0 PyPDF2-3.0.1 absl-py-2.3.0 accelerate-1.5.2 aiofiles-23.2.1 aiohappyeyeballs-2.6.1 aiohttp-3.12.13 aiosignal-1.3.2 altair-5.5.0 annotated-types-0.7.0 anyio-4.9.0 async-timeout-5.0.1 attrs-25.3.0 bitsandbytes-0.45.5 blinker-1.9.0 certifi-2025.6.15 charset_normalizer-3.4.2 click-8.2.1 colorama-0.4.6 contourpy-1.3.2 cycler-0.12.1 datasets-3.6.0 dill-0.3.8 duckduckgo_search-8.0.2 einops-0.8.1 exceptiongroup-1.3.0 fastapi-0.112.4 ffmpy-0.6.0 flask_cloudflared-0.0.14 fonttools-4.58.4 frozenlist-1.7.0 gitdb-4.0.12 gitpython-3.1.44 gradio-4.37.2 gradio-client-1.0.2 grpcio-1.73.0 h11-0.16.0 hf-xet-1.1.5 html2text-2025.4.15 httpcore-1.0.9 httpx-0.28.1 huggingface-hub-0.33.0 idna-3.10 importlib-resources-6.5.2 itsdangerous-2.2.0 jinja2-3.1.6 jsonschema-4.24.0 jsonschema-specifications-2025.4.1 kiwisolver-1.4.8 lxml-5.4.0 markdown-3.8.2 markdown-it-py-3.0.0 matplotlib-3.10.3 mdurl-0.1.2 multidict-6.4.4 multiprocess-0.70.16 narwhals-1.44.0 numpy-2.2.6 orjson-3.10.18 packaging-25.0 pandas-2.3.0 peft-0.15.2 platformdirs-4.3.8 primp-0.15.0 propcache-0.3.2 protobuf-6.31.1 psutil-7.0.0 pyarrow-20.0.0 pydantic-

### GEMINI
Excellent! You've successfully installed all the core requirements for text-generation-webui. The output you provided for pip install -r requirements/full/requirements.txt shows that: A vast number of packages, including accelerate, bitsandbytes, fastapi, gradio, transformers, pydantic, and many others, were successfully installed. The Ignoring messages for llama-cpp-binaries, exllamav3, exllamav2, and flash-attn are expected and completely fine. These are typically alternative or platform-specific builds that are not needed when llama.cpp is integrated as a submodule, which your --recursive clone has now enabled. It seems you might have pasted the PyTorch installation output again (the pip install torch torchvision torchaudio... part) just before the pip install -r requirements/full/requirements.txt output, but the key is that the requirements file installation did run and completed successfully. Now that the Python dependencies are handled, the next crucial step is to verify that llama.cpp itself is in the correct place, as it should have been pulled in by the --recursive clone. Action: Verify the llama.cpp submodule is present: ls -l repositories/llama.cpp/ This should show you the contents of the llama.cpp source code directory. If that command runs successfully and shows files, then we can proceed to launch the web UI. Please provide the output of ls -l repositories/llama.cpp/.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]