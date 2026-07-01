---
category: homelab
date: 2025-06-23
id: 299439
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/coding.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user is trying to install dependencies for text-generation-webui but
  is encountering environment marker mismatches for llama-cpp-binaries and exllamav3
  packages that don't match their current platform/Python version configuration.
tags:
- text-generation-webui
- python
- pip
- requirements
- llama-cpp
- exllamav3
- environment-mismatch
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install -r requirements/full/requirements.txt
Ignoring llama-cpp-binaries: markers 'platform_system == "Windows" and python_version == "3.11"' don't match your environment
Ignoring llama-cpp-binaries: markers 'platform_system == "Linux" and platform_machine == "x86_64" and python_version == "3.11"' don't match your environment
Ignoring exllamav3: markers 'platform_system == "Windows" and python_version == "3.11"' don't match your environment
Ignoring exllamav3: markers 'platform_system == "Linux" and platform_machine == "x86_64" and python_version == "3.11"' don't match your environment
Ignoring exllamav2: markers 'platform_system == "Windows" and python_version == "3.11"' don't match your environment
Ignoring exllamav2: markers 'platform_system == "Linux" and platform_machine == "x86_64" and python_version == "3.11"' don't match your environment
Ignoring exllamav2: markers 'platform_system == "Linux" and platform_machine != "x86_64"' don't match your environment
Ignoring flash-attn: markers 'platform_system == "Windows" and python_version == "3.11"' don't match your environment
Ignoring flash-attn: markers 'platform_system == "Linux" and platform_machine == "x86_64" and python_version == "3.11"' don't match your environment
Requirement already satisfied: accelerate==1.5.* in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 1)) (1.5.2)
Requirement already satisfied: bitsandbytes==0.45.* in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 2)) (0.45.5)
Requirement already satisfied: colorama in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 3)) (0.4.6)
Requirement already satisfied: datasets in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 4)) (3.6.0)
Requirement already satisfied: duckduckgo_search==8.0.2 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 5)) (8.0.2)
Requirement already satisfied: einops in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 6)) (0.8.1)
Requirement already satisfied: fastapi==0.112.4 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 7)) (0.112.4)
Requirement already satisfied: gradio==4.37.* in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 8)) (4.37.2)
Requirement already satisfied: html2text==2025.4.15 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 9)) (2025.4.15)
Requirement already satisfied: jinja2==3.1.6 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 10)) (3.1.6)
Requirement already satisfied: markdown in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 11)) (3.8.2)
Collecting numpy==2.2.* (from -r requirements/full/requirements.txt (line 12))
  Using cached numpy-2.2.6-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (62 kB)
Requirement already satisfied: pandas in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 13)) (2.3.0)
Requirement already satisfied: peft==0.15.* in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 14)) (0.15.2)
Requirement already satisfied: Pillow>=9.5.0 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 15)) (10.4.0)
Requirement already satisfied: psutil in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 16)) (7.0.0)
Requirement already satisfied: pydantic==2.8.2 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 17)) (2.8.2)
Requirement already satisfied: PyPDF2==3.0.1 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 18)) (3.0.1)
Requirement already satisfied: python-docx==1.1.2 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 19)) (1.1.2)
Requirement already satisfied: pyyaml in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 20)) (6.0.2)
Requirement already satisfied: requests in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 21)) (2.32.4)
Requirement already satisfied: rich in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 22)) (14.0.0)
Requirement already satisfied: safetensors==0.5.* in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 23)) (0.5.3)
Requirement already satisfied: scipy in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 24)) (1.16.0)
Requirement already satisfied: sentencepiece in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 25)) (0.2.0)
Requirement already satisfied: tensorboard in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 26)) (2.19.0)
Requirement already satisfied: transformers==4.50.* in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 27)) (4.50.3)
Requirement already satisfied: tqdm in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 28)) (4.67.1)
Requirement already satisfied: wandb in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 29)) (0.20.1)
Requirement already satisfied: flask_cloudflared==0.0.14 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 32)) (0.0.14)
Requirement already satisfied: sse-starlette==1.6.5 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 33)) (1.6.5)
Requirement already satisfied: tiktoken in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 34)) (0.9.0)
Requirement already satisfied: packaging>=20.0 in ./.venv/lib/python3.12/site-packages (from accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (25.0)
Requirement already satisfied: torch>=2.0.0 in ./.venv/lib/python3.12/site-packages (from accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (2.7.1)
Requirement already satisfied: huggingface-hub>=0.21.0 in ./.venv/lib/python3.12/site-packages (from accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (0.33.0)
Requirement already satisfied: click>=8.1.8 in ./.venv/lib/python3.12/site-packages (from duckduckgo_search==8.0.2->-r requirements/full/requirements.txt (line 5)) (8.2.1)
Requirement already satisfied: primp>=0.15.0 in ./.venv/lib/python3.12/site-packages (from duckduckgo_search==8.0.2->-r requirements/full/requirements.txt (line 5)) (0.15.0)
Requirement already satisfied: lxml>=5.3.0 in ./.venv/lib/python3.12/site-packages (from duckduckgo_search==8.0.2->-r requirements/full/requirements.txt (line 5)) (5.4.0)
Requirement already satisfied: starlette<0.39.0,>=0.37.2 in ./.venv/lib/python3.12/site-packages (from fastapi==0.112.4->-r requirements/full/requirements.txt (line 7)) (0.38.6)
Requirement already satisfied: typing-extensions>=4.8.0 in ./.venv/lib/python3.12/site-packages (from fastapi==0.112.4->-r requirements/full/requirements.txt (line 7)) (4.14.0)
Requirement already satisfied: aiofiles<24.0,>=22.0 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (23.2.1)
Requirement already satisfied: altair<6.0,>=4.2.0 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (5.5.0)
Requirement already satisfied: ffmpy in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.6.0)
Requirement already satisfied: gradio-client==1.0.2 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (1.0.2)
Requirement already satisfied: httpx>=0.24.1 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.28.1)
Requirement already satisfied: importlib-resources<7.0,>=1.3 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (6.5.2)
Collecting markupsafe~=2.0 (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8))
  Using cached MarkupSafe-2.1.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.0 kB)
Requirement already satisfied: matplotlib~=3.0 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (3.10.3)
Requirement already satisfied: orjson~=3.0 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (3.10.18)
Requirement already satisfied: pydub in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.25.1)
Requirement already satisfied: python-multipart>=0.0.9 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.0.20)
Requirement already satisfied: ruff>=0.2.2 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.12.0)
Requirement already satisfied: semantic-version~=2.0 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (2.10.0)
Requirement already satisfied: tomlkit==0.12.0 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.12.0)
Requirement already satisfied: typer<1.0,>=0.12 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.16.0)
Requirement already satisfied: urllib3~=2.0 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (2.5.0)
Requirement already satisfied: uvicorn>=0.14.0 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.34.3)
Requirement already satisfied: annotated-types>=0.4.0 in ./.venv/lib/python3.12/site-packages (from pydantic==2.8.2->-r requirements/full/requirements.txt (line 17)) (0.7.0)
Requirement already satisfied: pydantic-core==2.20.1 in ./.venv/lib/python3.12/site-packages (from pydantic==2.8.2->-r requirements/full/requirements.txt (line 17)) (2.20.1)
Requirement already satisfied: filelock in ./.venv/lib/python3.12/site-packages (from transformers==4.50.*->-r requirements/full/requirements.txt (line 27)) (3.18.0)
Requirement already satisfied: regex!=2019.12.17 in ./.venv/lib/python3.12/site-packages (from transformers==4.50.*->-r requirements/full/requirements.txt (line 27)) (2024.11.6)
Requirement already satisfied: tokenizers<0.22,>=0.21 in ./.venv/lib/python3.12/site-packages (from transformers==4.50.*->-r requirements/full/requirements.txt (line 27)) (0.21.1)
Requirement already satisfied: Flask>=0.8 in ./.venv/lib/python3.12/site-packages (from flask_cloudflared==0.0.14->-r requirements/full/requirements.txt (line 32)) (3.1.1)
Requirement already satisfied: fsspec in ./.venv/lib/python3.12/site-packages (from gradio-client==1.0.2->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (2025.3.0)
Requirement already satisfied: websockets<12.0,>=10.0 in ./.venv/lib/python3.12/site-packages (from gradio-client==1.0.2->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (11.0.3)
Requirement already satisfied: pyarrow>=15.0.0 in ./.venv/lib/python3.12/site-packages (from datasets->-r requirements/full/requirements.txt (line 4)) (20.0.0)
Requirement already satisfied: dill<0.3.9,>=0.3.0 in ./.venv/lib/python3.12/site-packages (from datasets->-r requirements/full/requirements.txt (line 4)) (0.3.8)
Requirement already satisfied: xxhash in ./.venv/lib/python3.12/site-packages (from datasets->-r requirements/full/requirements.txt (line 4)) (3.5.0)
Requirement already satisfied: multiprocess<0.70.17 in ./.venv/lib/python3.12/site-packages (from datasets->-r requirements/full/requirements.txt (line 4)) (0.70.16)
Requirement already satisfied: python-dateutil>=2.8.2 in ./.venv/lib/python3.12/site-packages (from pandas->-r requirements/full/requirements.txt (line 13)) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in ./.venv/lib/python3.12/site-packages (from pandas->-r requirements/full/requirements.txt (line 13)) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in ./.venv/lib/python3.12/site-packages (from pandas->-r requirements/full/requirements.txt (line 13)) (2025.2)
Requirement already satisfied: charset_normalizer<4,>=2 in ./.venv/lib/python3.12/site-packages (from requests->-r requirements/full/requirements.txt (line 21)) (3.4.2)
Requirement already satisfied: idna<4,>=2.5 in ./.venv/lib/python3.12/site-packages (from requests->-r requirements/full/requirements.txt (line 21)) (3.10)
Requirement already satisfied: certifi>=2017.4.17 in ./.venv/lib/python3.12/site-packages (from requests->-r requirements/full/requirements.txt (line 21)) (2025.6.15)
Requirement already satisfied: markdown-it-py>=2.2.0 in ./.venv/lib/python3.12/site-packages (from rich->-r requirements/full/requirements.txt (line 22)) (3.0.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in ./.venv/lib/python3.12/site-packages (from rich->-r requirements/full/requirements.txt (line 22)) (2.19.2)
Requirement already satisfied: absl-py>=0.4 in ./.venv/lib/python3.12/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (2.3.0)
Requirement already satisfied: grpcio>=1.48.2 in ./.venv/lib/python3.12/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (1.73.0)
Requirement already satisfied: protobuf!=4.24.0,>=3.19.6 in ./.venv/lib/python3.12/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (6.31.1)
Requirement already satisfied: setuptools>=41.0.0 in ./.venv/lib/python3.12/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (80.9.0)
Requirement already satisfied: six>1.9 in ./.venv/lib/python3.12/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (1.17.0)
Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in ./.venv/lib/python3.12/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (0.7.2)
Requirement already satisfied: werkzeug>=1.0.1 in ./.venv/lib/python3.12/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (3.1.3)
Requirement already satisfied: gitpython!=3.1.29,>=1.0.0 in ./.venv/lib/python3.12/site-packages (from wandb->-r requirements/full/requirements.txt (line 29)) (3.1.44)
Requirement already satisfied: platformdirs in ./.venv/lib/python3.12/site-packages (from wandb->-r requirements/full/requirements.txt (line 29)) (4.3.8)
Requirement already satisfied: sentry-sdk>=2.0.0 in ./.venv/lib/python3.12/site-packages (from wandb->-r requirements/full/requirements.txt (line 29)) (2.30.0)
Requirement already satisfied: setproctitle in ./.venv/lib/python3.12/site-packages (from wandb->-r requirements/full/requirements.txt (line 29)) (1.3.6)
Requirement already satisfied: jsonschema>=3.0 in ./.venv/lib/python3.12/site-packages (from altair<6.0,>=4.2.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (4.24.0)
Requirement already satisfied: narwhals>=1.14.2 in ./.venv/lib/python3.12/site-packages (from altair<6.0,>=4.2.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (1.44.0)
Requirement already satisfied: blinker>=1.9.0 in ./.venv/lib/python3.12/site-packages (from Flask>=0.8->flask_cloudflared==0.0.14->-r requirements/full/requirements.txt (line 32)) (1.9.0)
Requirement already satisfied: itsdangerous>=2.2.0 in ./.venv/lib/python3.12/site-packages (from Flask>=0.8->flask_cloudflared==0.0.14->-r requirements/full/requirements.txt (line 32)) (2.2.0)
Requirement already satisfied: aiohttp!=4.0.0a0,!=4.0.0a1 in ./.venv/lib/python3.12/site-packages (from fsspec[http]<=2025.3.0,>=2023.1.0->datasets->-r requirements/full/requirements.txt (line 4)) (3.12.13)
Requirement already satisfied: gitdb<5,>=4.0.1 in ./.venv/lib/python3.12/site-packages (from gitpython!=3.1.29,>=1.0.0->wandb->-r requirements/full/requirements.txt (line 29)) (4.0.12)
Requirement already satisfied: anyio in ./.venv/lib/python3.12/site-packages (from httpx>=0.24.1->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (4.9.0)
Requirement already satisfied: httpcore==1.* in ./.venv/lib/python3.12/site-packages (from httpx>=0.24.1->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (1.0.9)
Requirement already satisfied: h11>=0.16 in ./.venv/lib/python3.12/site-packages (from httpcore==1.*->httpx>=0.24.1->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.16.0)
Requirement already satisfied: hf-xet<2.0.0,>=1.1.2 in ./.venv/lib/python3.12/site-packages (from huggingface-hub>=0.21.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (1.1.5)
Requirement already satisfied: mdurl~=0.1 in ./.venv/lib/python3.12/site-packages (from markdown-it-py>=2.2.0->rich->-r requirements/full/requirements.txt (line 22)) (0.1.2)
Requirement already satisfied: contourpy>=1.0.1 in ./.venv/lib/python3.12/site-packages (from matplotlib~=3.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (1.3.2)
Requirement already satisfied: cycler>=0.10 in ./.venv/lib/python3.12/site-packages (from matplotlib~=3.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in ./.venv/lib/python3.12/site-packages (from matplotlib~=3.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (4.58.4)
Requirement already satisfied: kiwisolver>=1.3.1 in ./.venv/lib/python3.12/site-packages (from matplotlib~=3.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (1.4.8)
Requirement already satisfied: pyparsing>=2.3.1 in ./.venv/lib/python3.12/site-packages (from matplotlib~=3.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (3.2.3)
Requirement already satisfied: sympy>=1.13.3 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (1.14.0)
Requirement already satisfied: networkx in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (3.5)
Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.6.77 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (12.6.77)
Requirement already satisfied: nvidia-cuda-runtime-cu12==12.6.77 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (12.6.77)
Requirement already satisfied: nvidia-cuda-cupti-cu12==12.6.80 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (12.6.80)
Requirement already satisfied: nvidia-cudnn-cu12==9.5.1.17 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (9.5.1.17)
Requirement already satisfied: nvidia-cublas-cu12==12.6.4.1 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (12.6.4.1)
Requirement already satisfied: nvidia-cufft-cu12==11.3.0.4 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.3.0.4)
Requirement already satisfied: nvidia-curand-cu12==10.3.7.77 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (10.3.7.77)
Requirement already satisfied: nvidia-cusolver-cu12==11.7.1.2 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.7.1.2)
Requirement already satisfied: nvidia-cusparse-cu12==12.5.4.2 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (12.5.4.2)
Requirement already satisfied: nvidia-cusparselt-cu12==0.6.3 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (0.6.3)
Requirement already satisfied: nvidia-nccl-cu12==2.26.2 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (2.26.2)
Requirement already satisfied: nvidia-nvtx-cu12==12.6.77 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (12.6.77)
Requirement already satisfied: nvidia-nvjitlink-cu12==12.6.85 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (12.6.85)
Requirement already satisfied: nvidia-cufile-cu12==1.11.1.6 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (1.11.1.6)
Requirement already satisfied: triton==3.3.1 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (3.3.1)
Requirement already satisfied: shellingham>=1.3.0 in ./.venv/lib/python3.12/site-packages (from typer<1.0,>=0.12->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (1.5.4)
Requirement already satisfied: aiohappyeyeballs>=2.5.0 in ./.venv/lib/python3.12/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.3.0,>=2023.1.0->datasets->-r requirements/full/requirements.txt (line 4)) (2.6.1)
Requirement already satisfied: aiosignal>=1.1.2 in ./.venv/lib/python3.12/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.3.0,>=2023.1.0->datasets->-r requirements/full/requirements.txt (line 4)) (1.3.2)
Requirement already satisfied: attrs>=17.3.0 in ./.venv/lib/python3.12/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.3.0,>=2023.1.0->datasets->-r requirements/full/requirements.txt (line 4)) (25.3.0)
Requirement already satisfied: frozenlist>=1.1.1 in ./.venv/lib/python3.12/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.3.0,>=2023.1.0->datasets->-r requirements/full/requirements.txt (line 4)) (1.7.0)
Requirement already satisfied: multidict<7.0,>=4.5 in ./.venv/lib/python3.12/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.3.0,>=2023.1.0->datasets->-r requirements/full/requirements.txt (line 4)) (6.5.0)
Requirement already satisfied: propcache>=0.2.0 in ./.venv/lib/python3.12/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.3.0,>=2023.1.0->datasets->-r requirements/full/requirements.txt (line 4)) (0.3.2)
Requirement already satisfied: yarl<2.0,>=1.17.0 in ./.venv/lib/python3.12/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.3.0,>=2023.1.0->datasets->-r requirements/full/requirements.txt (line 4)) (1.20.1)
Requirement already satisfied: sniffio>=1.1 in ./.venv/lib/python3.12/site-packages (from anyio->httpx>=0.24.1->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (1.3.1)
Requirement already satisfied: smmap<6,>=3.0.1 in ./.venv/lib/python3.12/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.29,>=1.0.0->wandb->-r requirements/full/requirements.txt (line 29)) (5.0.2)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in ./.venv/lib/python3.12/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (2025.4.1)
Requirement already satisfied: referencing>=0.28.4 in ./.venv/lib/python3.12/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.36.2)
Requirement already satisfied: rpds-py>=0.7.1 in ./.venv/lib/python3.12/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.25.1)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in ./.venv/lib/python3.12/site-packages (from sympy>=1.13.3->torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (1.3.0)
Using cached numpy-2.2.6-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.5 MB)
Using cached MarkupSafe-2.1.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (28 kB)
Installing collected packages: numpy, markupsafe
  Attempting uninstall: numpy
    Found existing installation: numpy 2.3.1
    Uninstalling numpy-2.3.1:
      Successfully uninstalled numpy-2.3.1
  Attempting uninstall: markupsafe
    Found existing installation: MarkupSafe 3.0.2
    Uninstalling MarkupSafe-3.0.2:
      Successfully uninstalled MarkupSafe-3.0.2
Successfully installed markupsafe-2.1.5 numpy-2.2.6
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
14:34:23-917428 INFO     Starting Text generation web UI
14:34:23-919603 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

14:34:35-182523 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf"
14:34:35-185270 ERROR    Failed to load the model.
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/modules/ui_model_menu.py", line 196, in load_model_wrapper
    shared.model, shared.tokenizer = load_model(selected_model, loader)
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/modules/models.py", line 42, in load_model
    output = load_func_map[loader](model_name)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/modules/models.py", line 65, in llama_cpp_server_loader
    from modules.llama_cpp_server import LlamaServer
  File "/home/bryan_/text-generation-webui/modules/llama_cpp_server.py", line 12, in <module>
    import llama_cpp_binaries
ModuleNotFoundError: No module named 'llama_cpp_binaries'

### USER
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
Requirement already satisfied: accelerate==1.5.* in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 1)) (1.5.2)
Requirement already satisfied: bitsandbytes==0.45.* in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 2)) (0.45.5)
Requirement already satisfied: colorama in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 3)) (0.4.6)
Requirement already satisfied: datasets in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 4)) (3.6.0)
Requirement already satisfied: duckduckgo_search==8.0.2 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 5)) (8.0.2)
Requirement already satisfied: einops in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 6)) (0.8.1)
Requirement already satisfied: fastapi==0.112.4 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 7)) (0.112.4)
Requirement already satisfied: gradio==4.37.* in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 8)) (4.37.2)
Requirement already satisfied: html2text==2025.4.15 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 9)) (2025.4.15)
Requirement already satisfied: jinja2==3.1.6 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 10)) (3.1.6)
Requirement already satisfied: markdown in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 11)) (3.8.2)
Collecting numpy==2.2.* (from -r requirements/full/requirements.txt (line 12))
  Using cached numpy-2.2.6-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (62 kB)
Requirement already satisfied: pandas in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 13)) (2.3.0)
Requirement already satisfied: peft==0.15.* in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 14)) (0.15.2)
Requirement already satisfied: Pillow>=9.5.0 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 15)) (10.4.0)
Requirement already satisfied: psutil in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 16)) (7.0.0)
Requirement already satisfied: pydantic==2.8.2 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 17)) (2.8.2)
Requirement already satisfied: PyPDF2==3.0.1 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 18)) (3.0.1)
Requirement already satisfied: python-docx==1.1.2 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 19)) (1.1.2)
Requirement already satisfied: pyyaml in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 20)) (6.0.2)
Requirement already satisfied: requests in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 21)) (2.32.4)
Requirement already satisfied: rich in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 22)) (14.0.0)
Requirement already satisfied: safetensors==0.5.* in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 23)) (0.5.3)
Requirement already satisfied: scipy in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 24)) (1.16.0)
Requirement already satisfied: sentencepiece in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 25)) (0.2.0)
Requirement already satisfied: tensorboard in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 26)) (2.19.0)
Requirement already satisfied: transformers==4.50.* in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 27)) (4.50.3)
Requirement already satisfied: tqdm in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 28)) (4.67.1)
Requirement already satisfied: wandb in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 29)) (0.20.1)
Requirement already satisfied: flask_cloudflared==0.0.14 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 32)) (0.0.14)
Requirement already satisfied: sse-starlette==1.6.5 in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 33)) (1.6.5)
Requirement already satisfied: tiktoken in ./.venv/lib/python3.12/site-packages (from -r requirements/full/requirements.txt (line 34)) (0.9.0)
Requirement already satisfied: packaging>=20.0 in ./.venv/lib/python3.12/site-packages (from accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (25.0)
Requirement already satisfied: torch>=2.0.0 in ./.venv/lib/python3.12/site-packages (from accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (2.7.1)
Requirement already satisfied: huggingface-hub>=0.21.0 in ./.venv/lib/python3.12/site-packages (from accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (0.33.0)
Requirement already satisfied: click>=8.1.8 in ./.venv/lib/python3.12/site-packages (from duckduckgo_search==8.0.2->-r requirements/full/requirements.txt (line 5)) (8.2.1)
Requirement already satisfied: primp>=0.15.0 in ./.venv/lib/python3.12/site-packages (from duckduckgo_search==8.0.2->-r requirements/full/requirements.txt (line 5)) (0.15.0)
Requirement already satisfied: lxml>=5.3.0 in ./.venv/lib/python3.12/site-packages (from duckduckgo_search==8.0.2->-r requirements/full/requirements.txt (line 5)) (5.4.0)
Requirement already satisfied: starlette<0.39.0,>=0.37.2 in ./.venv/lib/python3.12/site-packages (from fastapi==0.112.4->-r requirements/full/requirements.txt (line 7)) (0.38.6)
Requirement already satisfied: typing-extensions>=4.8.0 in ./.venv/lib/python3.12/site-packages (from fastapi==0.112.4->-r requirements/full/requirements.txt (line 7)) (4.14.0)
Requirement already satisfied: aiofiles<24.0,>=22.0 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (23.2.1)
Requirement already satisfied: altair<6.0,>=4.2.0 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (5.5.0)
Requirement already satisfied: ffmpy in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.6.0)
Requirement already satisfied: gradio-client==1.0.2 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (1.0.2)
Requirement already satisfied: httpx>=0.24.1 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.28.1)
Requirement already satisfied: importlib-resources<7.0,>=1.3 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (6.5.2)
Collecting markupsafe~=2.0 (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8))
  Using cached MarkupSafe-2.1.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.0 kB)
Requirement already satisfied: matplotlib~=3.0 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (3.10.3)
Requirement already satisfied: orjson~=3.0 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (3.10.18)
Requirement already satisfied: pydub in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.25.1)
Requirement already satisfied: python-multipart>=0.0.9 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.0.20)
Requirement already satisfied: ruff>=0.2.2 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.12.0)
Requirement already satisfied: semantic-version~=2.0 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (2.10.0)
Requirement already satisfied: tomlkit==0.12.0 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.12.0)
Requirement already satisfied: typer<1.0,>=0.12 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.16.0)
Requirement already satisfied: urllib3~=2.0 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (2.5.0)
Requirement already satisfied: uvicorn>=0.14.0 in ./.venv/lib/python3.12/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.34.3)
Requirement already satisfied: annotated-types>=0.4.0 in ./.venv/lib/python3.12/site-packages (from pydantic==2.8.2->-r requirements/full/requirements.txt (line 17)) (0.7.0)
Requirement already satisfied: pydantic-core==2.20.1 in ./.venv/lib/python3.12/site-packages (from pydantic==2.8.2->-r requirements/full/requirements.txt (line 17)) (2.20.1)
Requirement already satisfied: filelock in ./.venv/lib/python3.12/site-packages (from transformers==4.50.*->-r requirements/full/requirements.txt (line 27)) (3.18.0)
Requirement already satisfied: regex!=2019.12.17 in ./.venv/lib/python3.12/site-packages (from transformers==4.50.*->-r requirements/full/requirements.txt (line 27)) (2024.11.6)
Requirement already satisfied: tokenizers<0.22,>=0.21 in ./.venv/lib/python3.12/site-packages (from transformers==4.50.*->-r requirements/full/requirements.txt (line 27)) (0.21.1)
Requirement already satisfied: Flask>=0.8 in ./.venv/lib/python3.12/site-packages (from flask_cloudflared==0.0.14->-r requirements/full/requirements.txt (line 32)) (3.1.1)
Requirement already satisfied: fsspec in ./.venv/lib/python3.12/site-packages (from gradio-client==1.0.2->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (2025.3.0)
Requirement already satisfied: websockets<12.0,>=10.0 in ./.venv/lib/python3.12/site-packages (from gradio-client==1.0.2->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (11.0.3)
Requirement already satisfied: pyarrow>=15.0.0 in ./.venv/lib/python3.12/site-packages (from datasets->-r requirements/full/requirements.txt (line 4)) (20.0.0)
Requirement already satisfied: dill<0.3.9,>=0.3.0 in ./.venv/lib/python3.12/site-packages (from datasets->-r requirements/full/requirements.txt (line 4)) (0.3.8)
Requirement already satisfied: xxhash in ./.venv/lib/python3.12/site-packages (from datasets->-r requirements/full/requirements.txt (line 4)) (3.5.0)
Requirement already satisfied: multiprocess<0.70.17 in ./.venv/lib/python3.12/site-packages (from datasets->-r requirements/full/requirements.txt (line 4)) (0.70.16)
Requirement already satisfied: python-dateutil>=2.8.2 in ./.venv/lib/python3.12/site-packages (from pandas->-r requirements/full/requirements.txt (line 13)) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in ./.venv/lib/python3.12/site-packages (from pandas->-r requirements/full/requirements.txt (line 13)) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in ./.venv/lib/python3.12/site-packages (from pandas->-r requirements/full/requirements.txt (line 13)) (2025.2)
Requirement already satisfied: charset_normalizer<4,>=2 in ./.venv/lib/python3.12/site-packages (from requests->-r requirements/full/requirements.txt (line 21)) (3.4.2)
Requirement already satisfied: idna<4,>=2.5 in ./.venv/lib/python3.12/site-packages (from requests->-r requirements/full/requirements.txt (line 21)) (3.10)
Requirement already satisfied: certifi>=2017.4.17 in ./.venv/lib/python3.12/site-packages (from requests->-r requirements/full/requirements.txt (line 21)) (2025.6.15)
Requirement already satisfied: markdown-it-py>=2.2.0 in ./.venv/lib/python3.12/site-packages (from rich->-r requirements/full/requirements.txt (line 22)) (3.0.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in ./.venv/lib/python3.12/site-packages (from rich->-r requirements/full/requirements.txt (line 22)) (2.19.2)
Requirement already satisfied: absl-py>=0.4 in ./.venv/lib/python3.12/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (2.3.0)
Requirement already satisfied: grpcio>=1.48.2 in ./.venv/lib/python3.12/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (1.73.0)
Requirement already satisfied: protobuf!=4.24.0,>=3.19.6 in ./.venv/lib/python3.12/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (6.31.1)
Requirement already satisfied: setuptools>=41.0.0 in ./.venv/lib/python3.12/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (80.9.0)
Requirement already satisfied: six>1.9 in ./.venv/lib/python3.12/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (1.17.0)
Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in ./.venv/lib/python3.12/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (0.7.2)
Requirement already satisfied: werkzeug>=1.0.1 in ./.venv/lib/python3.12/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (3.1.3)
Requirement already satisfied: gitpython!=3.1.29,>=1.0.0 in ./.venv/lib/python3.12/site-packages (from wandb->-r requirements/full/requirements.txt (line 29)) (3.1.44)
Requirement already satisfied: platformdirs in ./.venv/lib/python3.12/site-packages (from wandb->-r requirements/full/requirements.txt (line 29)) (4.3.8)
Requirement already satisfied: sentry-sdk>=2.0.0 in ./.venv/lib/python3.12/site-packages (from wandb->-r requirements/full/requirements.txt (line 29)) (2.30.0)
Requirement already satisfied: setproctitle in ./.venv/lib/python3.12/site-packages (from wandb->-r requirements/full/requirements.txt (line 29)) (1.3.6)
Requirement already satisfied: jsonschema>=3.0 in ./.venv/lib/python3.12/site-packages (from altair<6.0,>=4.2.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (4.24.0)
Requirement already satisfied: narwhals>=1.14.2 in ./.venv/lib/python3.12/site-packages (from altair<6.0,>=4.2.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (1.44.0)
Requirement already satisfied: blinker>=1.9.0 in ./.venv/lib/python3.12/site-packages (from Flask>=0.8->flask_cloudflared==0.0.14->-r requirements/full/requirements.txt (line 32)) (1.9.0)
Requirement already satisfied: itsdangerous>=2.2.0 in ./.venv/lib/python3.12/site-packages (from Flask>=0.8->flask_cloudflared==0.0.14->-r requirements/full/requirements.txt (line 32)) (2.2.0)
Requirement already satisfied: aiohttp!=4.0.0a0,!=4.0.0a1 in ./.venv/lib/python3.12/site-packages (from fsspec[http]<=2025.3.0,>=2023.1.0->datasets->-r requirements/full/requirements.txt (line 4)) (3.12.13)
Requirement already satisfied: gitdb<5,>=4.0.1 in ./.venv/lib/python3.12/site-packages (from gitpython!=3.1.29,>=1.0.0->wandb->-r requirements/full/requirements.txt (line 29)) (4.0.12)
Requirement already satisfied: anyio in ./.venv/lib/python3.12/site-packages (from httpx>=0.24.1->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (4.9.0)
Requirement already satisfied: httpcore==1.* in ./.venv/lib/python3.12/site-packages (from httpx>=0.24.1->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (1.0.9)
Requirement already satisfied: h11>=0.16 in ./.venv/lib/python3.12/site-packages (from httpcore==1.*->httpx>=0.24.1->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.16.0)
Requirement already satisfied: hf-xet<2.0.0,>=1.1.2 in ./.venv/lib/python3.12/site-packages (from huggingface-hub>=0.21.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (1.1.5)
Requirement already satisfied: mdurl~=0.1 in ./.venv/lib/python3.12/site-packages (from markdown-it-py>=2.2.0->rich->-r requirements/full/requirements.txt (line 22)) (0.1.2)
Requirement already satisfied: contourpy>=1.0.1 in ./.venv/lib/python3.12/site-packages (from matplotlib~=3.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (1.3.2)
Requirement already satisfied: cycler>=0.10 in ./.venv/lib/python3.12/site-packages (from matplotlib~=3.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in ./.venv/lib/python3.12/site-packages (from matplotlib~=3.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (4.58.4)
Requirement already satisfied: kiwisolver>=1.3.1 in ./.venv/lib/python3.12/site-packages (from matplotlib~=3.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (1.4.8)
Requirement already satisfied: pyparsing>=2.3.1 in ./.venv/lib/python3.12/site-packages (from matplotlib~=3.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (3.2.3)
Requirement already satisfied: sympy>=1.13.3 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (1.14.0)
Requirement already satisfied: networkx in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (3.5)
Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.6.77 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (12.6.77)
Requirement already satisfied: nvidia-cuda-runtime-cu12==12.6.77 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (12.6.77)
Requirement already satisfied: nvidia-cuda-cupti-cu12==12.6.80 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (12.6.80)
Requirement already satisfied: nvidia-cudnn-cu12==9.5.1.17 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (9.5.1.17)
Requirement already satisfied: nvidia-cublas-cu12==12.6.4.1 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (12.6.4.1)
Requirement already satisfied: nvidia-cufft-cu12==11.3.0.4 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.3.0.4)
Requirement already satisfied: nvidia-curand-cu12==10.3.7.77 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (10.3.7.77)
Requirement already satisfied: nvidia-cusolver-cu12==11.7.1.2 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.7.1.2)
Requirement already satisfied: nvidia-cusparse-cu12==12.5.4.2 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (12.5.4.2)
Requirement already satisfied: nvidia-cusparselt-cu12==0.6.3 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (0.6.3)
Requirement already satisfied: nvidia-nccl-cu12==2.26.2 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (2.26.2)
Requirement already satisfied: nvidia-nvtx-cu12==12.6.77 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (12.6.77)
Requirement already satisfied: nvidia-nvjitlink-cu12==12.6.85 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (12.6.85)
Requirement already satisfied: nvidia-cufile-cu12==1.11.1.6 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (1.11.1.6)
Requirement already satisfied: triton==3.3.1 in ./.venv/lib/python3.12/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (3.3.1)
Requirement already satisfied: shellingham>=1.3.0 in ./.venv/lib/python3.12/site-packages (from typer<1.0,>=0.12->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (1.5.4)
Requirement already satisfied: aiohappyeyeballs>=2.5.0 in ./.venv/lib/python3.12/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.3.0,>=2023.1.0->datasets->-r requirements/full/requirements.txt (line 4)) (2.6.1)
Requirement already satisfied: aiosignal>=1.1.2 in ./.venv/lib/python3.12/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.3.0,>=2023.1.0->datasets->-r requirements/full/requirements.txt (line 4)) (1.3.2)
Requirement already satisfied: attrs>=17.3.0 in ./.venv/lib/python3.12/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.3.0,>=2023.1.0->datasets->-r requirements/full/requirements.txt (line 4)) (25.3.0)
Requirement already satisfied: frozenlist>=1.1.1 in ./.venv/lib/python3.12/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.3.0,>=2023.1.0->datasets->-r requirements/full/requirements.txt (line 4)) (1.7.0)
Requirement already satisfied: multidict<7.0,>=4.5 in ./.venv/lib/python3.12/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.3.0,>=2023.1.0->datasets->-r requirements/full/requirements.txt (line 4)) (6.5.0)
Requirement already satisfied: propcache>=0.2.0 in ./.venv/lib/python3.12/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.3.0,>=2023.1.0->datasets->-r requirements/full/requirements.txt (line 4)) (0.3.2)
Requirement already satisfied: yarl<2.0,>=1.17.0 in ./.venv/lib/python3.12/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.3.0,>=2023.1.0->datasets->-r requirements/full/requirements.txt (line 4)) (1.20.1)
Requirement already satisfied: sniffio>=1.1 in ./.venv/lib/python3.12/site-packages (from anyio->httpx>=0.24.1->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (1.3.1)
Requirement already satisfied: smmap<6,>=3.0.1 in ./.venv/lib/python3.12/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.29,>=1.0.0->wandb->-r requirements/full/requirements.txt (line 29)) (5.0.2)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in ./.venv/lib/python3.12/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (2025.4.1)
Requirement already satisfied: referencing>=0.28.4 in ./.venv/lib/python3.12/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.36.2)
Requirement already satisfied: rpds-py>=0.7.1 in ./.venv/lib/python3.12/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (0.25.1)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in ./.venv/lib/python3.12/site-packages (from sympy>=1.13.3->torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (1.3.0)
Using cached numpy-2.2.6-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.5 MB)
Using cached MarkupSafe-2.1.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (28 kB)
Installing collected packages: numpy, markupsafe
  Attempting uninstall: numpy
    Found existing installation: numpy 2.3.1
    Uninstalling numpy-2.3.1:
      Successfully uninstalled numpy-2.3.1
  Attempting uninstall: markupsafe
    Found existing installation: MarkupSafe 3.0.2
    Uninstalling MarkupSafe-3.0.2:
      Successfully uninstalled MarkupSafe-3.0.2
Successfully installed markupsafe-2.1.5 numpy-2.2.6
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
14:34:23-917428 INFO     Starting Text generation web UI
14:34:23-919603 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

14:34:35-182523 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf"
14:34:35-185270 ERROR    Failed to load the model.
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/modules/ui_model_menu.py", line 196, in load_model_wrapper
    shared.model, shared.tokenizer = load_model(selected_model, loader)
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/modules/models.py", line 42, in load_model
    output = load_func_map[loader](model_name)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/modules/models.py", line 65, in llama_cpp_server_loader
    from modules.llama_cpp_server import LlamaServer
  File "/home/bryan_/text-generation-webui/modules/llama_cpp_server.py", line 12, in <module>
    import llama_cpp_binaries
ModuleNotFoundError: No module named 'llama_cpp_binaries'

### GEMINI
Bryan, thank you for providing the output. This is very insightful and helps us narrow down the problem significantly. The output from pip install -r requirements/full/requirements.txt shows something critical at the very top: Ignoring llama-cpp-binaries: markers 'platform_system == "Windows" and python_version == "3.11"' don't match your environment Ignoring llama-cpp-binaries: markers 'platform_system == "Linux" and platform_machine == "x86_64" and python_version == "3.11"' don't match your environment This means that the requirements/full/requirements.txt file does contain llama-cpp-binaries, but it has specific markers (conditions) that tell pip to only install it if the system is Windows and Python 3.11, or Linux x86_64 and Python 3.11. You are running Python 3.12.3 (Python 3.12.3 (main, Jun 18 2025, 17:59:45) [GCC 13.3.0] on linux as seen in your previous python3 command output). Because your Python version is 3.12, pip is explicitly ignoring the llama-cpp-binaries installation requirement. This is the direct cause of your ModuleNotFoundError: No module named 'llama_cpp_binaries'. The git reset --hard pulled code that expects llama_cpp_binaries, but your Python environment isn't set up to install it due to the version mismatch specified in the requirements.txt file. This is a common issue when a project has strict Python version requirements for certain dependencies. Step 21: Align Python Version or Manually Install llama_cpp_binaries We have two primary options to fix this: Option 1: (Recommended) Try to downgrade your Python version to 3.11 within WSL2. This is often the cleanest solution, as it aligns your environment with what the requirements.txt expects. However, it can be a bit more involved to manage Python versions in WSL2 if you haven't done it before. Option 2: (Faster, but potentially less robust long-term) Manually install a compatible llama_cpp_binaries package if one exists for Python 3.12, or remove the version check in the requirements file. Modifying the requirements.txt is generally not recommended as it could cause issues if the maintainers specifically intended this, but it might get you running. Let's try a direct installation of llama_cpp_binaries for your environment first, as sometimes pip markers can be overly restrictive if there's a compatible wheel available. If that fails, we can look into Python version management. Step 21 (Action): Attempt Direct Installation of llama_cpp_binaries We will explicitly try to install llama-cpp-binaries while ignoring the Python version check. What I need you to do now (in your Ubuntu WSL2 terminal, still in (.venv) ~/text-generation-webui$): Stop the running oobabooga process (if it's still running): Press Ctrl + C until your prompt returns. Attempt to install llama-cpp-binaries directly, ignoring platform/version markers: Command: pip install --no-deps --no-index --find-links https://abetlen.github.io/llama-cpp-python/wheels/cu118 llama-cpp-binaries Explanation: --no-deps: Tells pip not to install any dependencies of llama-cpp-binaries itself, as many common ones should already be present. --no-index: Tells pip to only look at the provided --find-links URL, not PyPI. --find-links https://abetlen.github.io/llama-cpp-python/wheels/cu118: This is the same URL we used for llama-cpp-python, which hosts pre-built wheels including CUDA support. There's a chance llama-cpp-binaries might be hosted there too, or a compatible wheel is present. llama-cpp-binaries: The specific package we want to install. If the above command fails or prints "Cannot find a version...": It likely means there isn't a pre-built wheel for Python 3.12 on that specific index, or it needs to be built from source (which is more complex). In that case, we might need to resort to editing the requirements.txt as a quick test, or consider changing your Python version. Relaunch Oobabooga: Command: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp What I need from you: Confirm you stopped the server. Run the pip install --no-deps --no-index --find-links ... command. Copy and paste the entire output of this command here. After it finishes, run the python3 server.py ... command. Copy and paste all of the new output from your Ubuntu WSL2 terminal, starting from the python3 server.py command, including any messages when you try to load the model in the browser. Let's see if we can force this specific binary to install!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]