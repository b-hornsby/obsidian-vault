---
id: 187579
source: GEMINI
date: 2025-06-24
tags: ['coding', 'ai', 'gemini', 'model', 'oobabooga', 'llama.cpp', 'lora', 'text-generation']
category: coding
sentiment: building
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
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
Collecting accelerate==1.5.*
  Downloading accelerate-1.5.2-py3-none-any.whl (345 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 345.1/345.1 kB 6.4 MB/s eta 0:00:00
Collecting bitsandbytes==0.45.*
  Downloading bitsandbytes-0.45.5-py3-none-manylinux_2_24_x86_64.whl (76.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 76.1/76.1 MB 18.4 MB/s eta 0:00:00
Collecting colorama
  Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Collecting datasets
  Downloading datasets-3.6.0-py3-none-any.whl (491 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 491.5/491.5 kB 28.9 MB/s eta 0:00:00
Collecting duckduckgo_search==8.0.2
  Downloading duckduckgo_search-8.0.2-py3-none-any.whl (18 kB)
Collecting einops
  Downloading einops-0.8.1-py3-none-any.whl (64 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.4/64.4 kB 5.7 MB/s eta 0:00:00
Collecting fastapi==0.112.4
  Downloading fastapi-0.112.4-py3-none-any.whl (93 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 93.9/93.9 kB 10.5 MB/s eta 0:00:00
Collecting gradio==4.37.*
  Downloading gradio-4.37.2-py3-none-any.whl (12.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.3/12.3 MB 81.8 MB/s eta 0:00:00
Collecting html2text==2025.4.15
  Downloading html2text-2025.4.15-py3-none-any.whl (34 kB)
Collecting jinja2==3.1.6
  Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 134.9/134.9 kB 12.6 MB/s eta 0:00:00
Collecting markdown
  Downloading markdown-3.8.2-py3-none-any.whl (106 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 106.8/106.8 kB 16.1 MB/s eta 0:00:00
Collecting numpy==2.2.*
  Downloading numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.8/16.8 MB 78.5 MB/s eta 0:00:00
Collecting pandas
  Downloading pandas-2.3.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.3/12.3 MB 74.6 MB/s eta 0:00:00
Collecting peft==0.15.*
  Downloading peft-0.15.2-py3-none-any.whl (411 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 411.1/411.1 kB 27.6 MB/s eta 0:00:00
Requirement already satisfied: Pillow>=9.5.0 in ./.venv/lib/python3.10/site-packages (from -r requirements/full/requirements.txt (line 15)) (11.0.0)
Collecting psutil
  Downloading psutil-7.0.0-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (277 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 278.0/278.0 kB 29.9 MB/s eta 0:00:00
Collecting pydantic==2.8.2
  Downloading pydantic-2.8.2-py3-none-any.whl (423 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 423.9/423.9 kB 24.6 MB/s eta 0:00:00
Collecting PyPDF2==3.0.1
  Downloading pypdf2-3.0.1-py3-none-any.whl (232 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 232.6/232.6 kB 22.3 MB/s eta 0:00:00
Collecting python-docx==1.1.2
  Downloading python_docx-1.1.2-py3-none-any.whl (244 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 244.3/244.3 kB 15.7 MB/s eta 0:00:00
Collecting pyyaml
  Downloading PyYAML-6.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (751 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 751.2/751.2 kB 28.3 MB/s eta 0:00:00
Collecting requests
  Downloading requests-2.32.4-py3-none-any.whl (64 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.8/64.8 kB 7.5 MB/s eta 0:00:00
Collecting rich
  Downloading rich-14.0.0-py3-none-any.whl (243 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 243.2/243.2 kB 25.7 MB/s eta 0:00:00
Collecting safetensors==0.5.*
  Downloading safetensors-0.5.3-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (471 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 471.6/471.6 kB 37.1 MB/s eta 0:00:00
Collecting scipy
  Downloading scipy-1.15.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (37.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 37.7/37.7 MB 57.5 MB/s eta 0:00:00
Collecting sentencepiece
  Downloading sentencepiece-0.2.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 53.8 MB/s eta 0:00:00
Collecting tensorboard
  Downloading tensorboard-2.19.0-py3-none-any.whl (5.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 77.5 MB/s eta 0:00:00
Collecting transformers==4.50.*
  Downloading transformers-4.50.3-py3-none-any.whl (10.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.2/10.2 MB 87.9 MB/s eta 0:00:00
Collecting tqdm
  Downloading tqdm-4.67.1-py3-none-any.whl (78 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.5/78.5 kB 11.4 MB/s eta 0:00:00
Collecting wandb
  Downloading wandb-0.20.1-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 23.2/23.2 MB 59.5 MB/s eta 0:00:00
Collecting flask_cloudflared==0.0.14
  Downloading flask_cloudflared-0.0.14-py3-none-any.whl (6.4 kB)
Collecting sse-starlette==1.6.5
  Downloading sse_starlette-1.6.5-py3-none-any.whl (9.6 kB)
Collecting tiktoken
  Downloading tiktoken-0.9.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 53.6 MB/s eta 0:00:00
Collecting huggingface-hub>=0.21.0
  Downloading huggingface_hub-0.33.0-py3-none-any.whl (514 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 514.8/514.8 kB 58.3 MB/s eta 0:00:00
Requirement already satisfied: torch>=2.0.0 in ./.venv/lib/python3.10/site-packages (from accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (2.5.1+cu118)
Collecting packaging>=20.0
  Downloading packaging-25.0-py3-none-any.whl (66 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.5/66.5 kB 10.7 MB/s eta 0:00:00
Collecting lxml>=5.3.0
  Downloading lxml-5.4.0-cp310-cp310-manylinux_2_28_x86_64.whl (5.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.1/5.1 MB 68.9 MB/s eta 0:00:00
Collecting primp>=0.15.0
  Downloading primp-0.15.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 60.6 MB/s eta 0:00:00
Collecting click>=8.1.8
  Downloading click-8.2.1-py3-none-any.whl (102 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 102.2/102.2 kB 17.2 MB/s eta 0:00:00
Collecting starlette<0.39.0,>=0.37.2
  Downloading starlette-0.38.6-py3-none-any.whl (71 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 71.5/71.5 kB 11.3 MB/s eta 0:00:00
Requirement already satisfied: typing-extensions>=4.8.0 in ./.venv/lib/python3.10/site-packages (from fastapi==0.112.4->-r requirements/full/requirements.txt (line 7)) (4.9.0)
Collecting python-multipart>=0.0.9
  Downloading python_multipart-0.0.20-py3-none-any.whl (24 kB)
Collecting ruff>=0.2.2
  Downloading ruff-0.12.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.6/11.6 MB 77.2 MB/s eta 0:00:00
Requirement already satisfied: markupsafe~=2.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (2.1.5)
Collecting importlib-resources<7.0,>=1.3
  Downloading importlib_resources-6.5.2-py3-none-any.whl (37 kB)
Collecting Pillow>=9.5.0
  Downloading pillow-10.4.0-cp310-cp310-manylinux_2_28_x86_64.whl (4.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 69.2 MB/s eta 0:00:00
Collecting matplotlib~=3.0
  Downloading matplotlib-3.10.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (8.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.6/8.6 MB 75.9 MB/s eta 0:00:00
Collecting typer<1.0,>=0.12
  Downloading typer-0.16.0-py3-none-any.whl (46 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 46.3/46.3 kB 6.8 MB/s eta 0:00:00
Collecting tomlkit==0.12.0
  Downloading tomlkit-0.12.0-py3-none-any.whl (37 kB)
Collecting pydub
  Downloading pydub-0.25.1-py2.py3-none-any.whl (32 kB)
Collecting altair<6.0,>=4.2.0
  Downloading altair-5.5.0-py3-none-any.whl (731 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 731.2/731.2 kB 36.0 MB/s eta 0:00:00
Collecting aiofiles<24.0,>=22.0
  Downloading aiofiles-23.2.1-py3-none-any.whl (15 kB)
Collecting httpx>=0.24.1
  Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.5/73.5 kB 8.0 MB/s eta 0:00:00
Collecting semantic-version~=2.0
  Downloading semantic_version-2.10.0-py2.py3-none-any.whl (15 kB)
Collecting ffmpy
  Downloading ffmpy-0.6.0-py3-none-any.whl (5.5 kB)
Collecting gradio-client==1.0.2
  Downloading gradio_client-1.0.2-py3-none-any.whl (318 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 318.2/318.2 kB 23.0 MB/s eta 0:00:00
Collecting urllib3~=2.0
  Downloading urllib3-2.5.0-py3-none-any.whl (129 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 129.8/129.8 kB 16.2 MB/s eta 0:00:00
Collecting orjson~=3.0
  Downloading orjson-3.10.18-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (132 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 132.8/132.8 kB 12.5 MB/s eta 0:00:00
Collecting uvicorn>=0.14.0
  Downloading uvicorn-0.34.3-py3-none-any.whl (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.4/62.4 kB 8.7 MB/s eta 0:00:00
Collecting annotated-types>=0.4.0
  Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
Collecting pydantic-core==2.20.1
  Downloading pydantic_core-2.20.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 85.3 MB/s eta 0:00:00
Requirement already satisfied: filelock in ./.venv/lib/python3.10/site-packages (from transformers==4.50.*->-r requirements/full/requirements.txt (line 27)) (3.13.1)
Collecting tokenizers<0.22,>=0.21
  Downloading tokenizers-0.21.2-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 76.9 MB/s eta 0:00:00
Collecting regex!=2019.12.17
  Downloading regex-2024.11.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (781 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 781.7/781.7 kB 55.7 MB/s eta 0:00:00
Collecting Flask>=0.8
  Downloading flask-3.1.1-py3-none-any.whl (103 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.3/103.3 kB 12.3 MB/s eta 0:00:00
Requirement already satisfied: fsspec in ./.venv/lib/python3.10/site-packages (from gradio-client==1.0.2->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (2024.6.1)
Collecting websockets<12.0,>=10.0
  Downloading websockets-11.0.3-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (129 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 129.9/129.9 kB 14.3 MB/s eta 0:00:00
Collecting dill<0.3.9,>=0.3.0
  Downloading dill-0.3.8-py3-none-any.whl (116 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 116.3/116.3 kB 12.0 MB/s eta 0:00:00
Collecting multiprocess<0.70.17
  Downloading multiprocess-0.70.16-py310-none-any.whl (134 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 134.8/134.8 kB 19.5 MB/s eta 0:00:00
Collecting pyarrow>=15.0.0
  Downloading pyarrow-20.0.0-cp310-cp310-manylinux_2_28_x86_64.whl (42.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.3/42.3 MB 18.7 MB/s eta 0:00:00
Collecting xxhash
  Downloading xxhash-3.5.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (194 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 194.1/194.1 kB 27.4 MB/s eta 0:00:00
Collecting pytz>=2020.1
  Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 509.2/509.2 kB 47.2 MB/s eta 0:00:00
Collecting tzdata>=2022.7
  Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 347.8/347.8 kB 31.2 MB/s eta 0:00:00
Collecting python-dateutil>=2.8.2
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.9/229.9 kB 30.0 MB/s eta 0:00:00
Collecting charset_normalizer<4,>=2
  Downloading charset_normalizer-3.4.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (149 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 149.5/149.5 kB 21.9 MB/s eta 0:00:00
Collecting certifi>=2017.4.17
  Downloading certifi-2025.6.15-py3-none-any.whl (157 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 157.7/157.7 kB 15.4 MB/s eta 0:00:00
Collecting idna<4,>=2.5
  Downloading idna-3.10-py3-none-any.whl (70 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 70.4/70.4 kB 6.1 MB/s eta 0:00:00
Collecting markdown-it-py>=2.2.0
  Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 87.5/87.5 kB 8.4 MB/s eta 0:00:00
Collecting pygments<3.0.0,>=2.13.0
  Downloading pygments-2.19.2-py3-none-any.whl (1.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 52.1 MB/s eta 0:00:00
Collecting grpcio>=1.48.2
  Downloading grpcio-1.73.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (6.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.0/6.0 MB 81.9 MB/s eta 0:00:00
Collecting six>1.9
  Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Collecting protobuf!=4.24.0,>=3.19.6
  Downloading protobuf-6.31.1-cp39-abi3-manylinux2014_x86_64.whl (321 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 321.1/321.1 kB 36.4 MB/s eta 0:00:00
Collecting absl-py>=0.4
  Downloading absl_py-2.3.0-py3-none-any.whl (135 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 135.7/135.7 kB 19.3 MB/s eta 0:00:00
Collecting tensorboard-data-server<0.8.0,>=0.7.0
  Downloading tensorboard_data_server-0.7.2-py3-none-manylinux_2_31_x86_64.whl (6.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.6/6.6 MB 85.7 MB/s eta 0:00:00
Requirement already satisfied: setuptools>=41.0.0 in ./.venv/lib/python3.10/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (65.5.0)
Collecting werkzeug>=1.0.1
  Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 224.5/224.5 kB 27.0 MB/s eta 0:00:00
Collecting sentry-sdk>=2.0.0
  Downloading sentry_sdk-2.31.0-py2.py3-none-any.whl (355 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 355.6/355.6 kB 38.1 MB/s eta 0:00:00
Collecting gitpython!=3.1.29,>=1.0.0
  Downloading GitPython-3.1.44-py3-none-any.whl (207 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 207.6/207.6 kB 25.0 MB/s eta 0:00:00
Collecting setproctitle
  Downloading setproctitle-1.3.6-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (30 kB)
Collecting platformdirs
  Downloading platformdirs-4.3.8-py3-none-any.whl (18 kB)
Collecting narwhals>=1.14.2
  Downloading narwhals-1.44.0-py3-none-any.whl (365 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 365.2/365.2 kB 39.8 MB/s eta 0:00:00
Collecting jsonschema>=3.0
  Downloading jsonschema-4.24.0-py3-none-any.whl (88 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 88.7/88.7 kB 8.1 MB/s eta 0:00:00
Collecting typing-extensions>=4.8.0
  Downloading typing_extensions-4.14.0-py3-none-any.whl (43 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.8/43.8 kB 5.9 MB/s eta 0:00:00
Collecting blinker>=1.9.0
  Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Collecting itsdangerous>=2.2.0
  Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Collecting aiohttp!=4.0.0a0,!=4.0.0a1
  Downloading aiohttp-3.12.13-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 59.1 MB/s eta 0:00:00
Collecting gitdb<5,>=4.0.1
  Downloading gitdb-4.0.12-py3-none-any.whl (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.8/62.8 kB 9.1 MB/s eta 0:00:00
Collecting httpcore==1.*
  Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.8/78.8 kB 12.8 MB/s eta 0:00:00
Collecting anyio
  Downloading anyio-4.9.0-py3-none-any.whl (100 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.9/100.9 kB 16.3 MB/s eta 0:00:00
Collecting h11>=0.16
  Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Collecting hf-xet<2.0.0,>=1.1.2
  Downloading hf_xet-1.1.5-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 20.0 MB/s eta 0:00:00
Collecting mdurl~=0.1
  Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Collecting cycler>=0.10
  Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Collecting fonttools>=4.22.0
  Downloading fonttools-4.58.4-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.8/4.8 MB 43.4 MB/s eta 0:00:00
Collecting kiwisolver>=1.3.1
  Downloading kiwisolver-1.4.8-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 63.8 MB/s eta 0:00:00
Collecting contourpy>=1.0.1
  Downloading contourpy-1.3.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (325 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 325.0/325.0 kB 23.1 MB/s eta 0:00:00
Collecting pyparsing>=2.3.1
  Downloading pyparsing-3.2.3-py3-none-any.whl (111 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 111.1/111.1 kB 17.0 MB/s eta 0:00:00
Requirement already satisfied: nvidia-cuda-runtime-cu11==11.8.89 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.8.89)
Requirement already satisfied: nvidia-nccl-cu11==2.21.5 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (2.21.5)
Requirement already satisfied: sympy==1.13.1 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (1.13.1)
Requirement already satisfied: nvidia-cudnn-cu11==9.1.0.70 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (9.1.0.70)
Requirement already satisfied: nvidia-cuda-nvrtc-cu11==11.8.89 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.8.89)
Requirement already satisfied: nvidia-cufft-cu11==10.9.0.58 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (10.9.0.58)
Requirement already satisfied: networkx in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (3.3)
Requirement already satisfied: nvidia-cuda-cupti-cu11==11.8.87 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.8.87)
Requirement already satisfied: nvidia-curand-cu11==10.3.0.86 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (10.3.0.86)
Requirement already satisfied: nvidia-cublas-cu11==11.11.3.6 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.11.3.6)
Requirement already satisfied: nvidia-cusolver-cu11==11.4.1.48 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.4.1.48)
Requirement already satisfied: nvidia-nvtx-cu11==11.8.86 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.8.86)
Requirement already satisfied: nvidia-cusparse-cu11==11.7.5.86 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.7.5.86)
Requirement already satisfied: triton==3.1.0 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (3.1.0)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in ./.venv/lib/python3.10/site-packages (from sympy==1.13.1->torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (1.3.0)
Collecting shellingham>=1.3.0
  Downloading shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
Collecting frozenlist>=1.1.1
  Downloading frozenlist-1.7.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (222 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 222.9/222.9 kB 17.4 MB/s eta 0:00:00
Collecting multidict<7.0,>=4.5
  Downloading multidict-6.4.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (219 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 219.1/219.1 kB 24.0 MB/s eta 0:00:00
Collecting propcache>=0.2.0
  Downloading propcache-0.3.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (198 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 198.3/198.3 kB 20.3 MB/s eta 0:00:00
Collecting attrs>=17.3.0
  Downloading attrs-25.3.0-py3-none-any.whl (63 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.8/63.8 kB 9.7 MB/s eta 0:00:00
Collecting async-timeout<6.0,>=4.0
  Downloading async_timeout-5.0.1-py3-none-any.whl (6.2 kB)
Collecting aiosignal>=1.1.2
  Downloading aiosignal-1.3.2-py2.py3-none-any.whl (7.6 kB)
Collecting aiohappyeyeballs>=2.5.0
  Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
Collecting yarl<2.0,>=1.17.0
  Downloading yarl-1.20.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (326 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 326.1/326.1 kB 21.1 MB/s eta 0:00:00
Collecting exceptiongroup>=1.0.2
  Downloading exceptiongroup-1.3.0-py3-none-any.whl (16 kB)
Collecting sniffio>=1.1
  Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
Collecting smmap<6,>=3.0.1
  Downloading smmap-5.0.2-py3-none-any.whl (24 kB)
Collecting referencing>=0.28.4
  Downloading referencing-0.36.2-py3-none-any.whl (26 kB)
Collecting rpds-py>=0.7.1
  Downloading rpds_py-0.25.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (386 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 387.0/387.0 kB 28.1 MB/s eta 0:00:00
Collecting jsonschema-specifications>=2023.03.6
  Downloading jsonschema_specifications-2025.4.1-py3-none-any.whl (18 kB)
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
Successfully installed Flask-3.1.1 Pillow-10.4.0 PyPDF2-3.0.1 absl-py-2.3.0 accelerate-1.5.2 aiofiles-23.2.1 aiohappyeyeballs-2.6.1 aiohttp-3.12.13 aiosignal-1.3.2 altair-5.5.0 annotated-types-0.7.0 anyio-4.9.0 async-timeout-5.0.1 attrs-25.3.0 bitsandbytes-0.45.5 blinker-1.9.0 certifi-2025.6.15 charset_normalizer-3.4.2 click-8.2.1 colorama-0.4.6 contourpy-1.3.2 cycler-0.12.1 datasets-3.6.0 dill-0.3.8 duckduckgo_search-8.0.2 einops-0.8.1 exceptiongroup-1.3.0 fastapi-0.112.4 ffmpy-0.6.0 flask_cloudflared-0.0.14 fonttools-4.58.4 frozenlist-1.7.0 gitdb-4.0.12 gitpython-3.1.44 gradio-4.37.2 gradio-client-1.0.2 grpcio-1.73.0 h11-0.16.0 hf-xet-1.1.5 html2text-2025.4.15 httpcore-1.0.9 httpx-0.28.1 huggingface-hub-0.33.0 idna-3.10 importlib-resources-6.5.2 itsdangerous-2.2.0 jinja2-3.1.6 jsonschema-4.24.0 jsonschema-specifications-2025.4.1 kiwisolver-1.4.8 lxml-5.4.0 markdown-3.8.2 markdown-it-py-3.0.0 matplotlib-3.10.3 mdurl-0.1.2 multidict-6.4.4 multiprocess-0.70.16 narwhals-1.44.0 numpy-2.2.6 orjson-3.10.18 packaging-25.0 pandas-2.3.0 peft-0.15.2 platformdirs-4.3.8 primp-0.15.0 propcache-0.3.2 protobuf-6.31.1 psutil-7.0.0 pyarrow-20.0.0 pydantic-2.8.2 pydantic-core-2.20.1 pydub-0.25.1 pygments-2.19.2 pyparsing-3.2.3 python-dateutil-2.9.0.post0 python-docx-1.1.2 python-multipart-0.0.20 pytz-2025.2 pyyaml-6.0.2 referencing-0.36.2 regex-2024.11.6 requests-2.32.4 rich-14.0.0 rpds-py-0.25.1 ruff-0.12.0 safetensors-0.5.3 scipy-1.15.3 semantic-version-2.10.0 sentencepiece-0.2.0 sentry-sdk-2.31.0 setproctitle-1.3.6 shellingham-1.5.4 six-1.17.0 smmap-5.0.2 sniffio-1.3.1 sse-starlette-1.6.5 starlette-0.38.6 tensorboard-2.19.0 tensorboard-data-server-0.7.2 tiktoken-0.9.0 tokenizers-0.21.2 tomlkit-0.12.0 tqdm-4.67.1 transformers-4.50.3 typer-0.16.0 typing-extensions-4.14.0 tzdata-2025.2 urllib3-2.5.0 uvicorn-0.34.3 wandb-0.20.1 websockets-11.0.3 werkzeug-3.1.3 xxhash-3.5.0 yarl-1.20.1
WARNING: There was an error checking the latest version of pip.
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

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
Collecting accelerate==1.5.*
  Downloading accelerate-1.5.2-py3-none-any.whl (345 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 345.1/345.1 kB 6.4 MB/s eta 0:00:00
Collecting bitsandbytes==0.45.*
  Downloading bitsandbytes-0.45.5-py3-none-manylinux_2_24_x86_64.whl (76.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 76.1/76.1 MB 18.4 MB/s eta 0:00:00
Collecting colorama
  Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Collecting datasets
  Downloading datasets-3.6.0-py3-none-any.whl (491 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 491.5/491.5 kB 28.9 MB/s eta 0:00:00
Collecting duckduckgo_search==8.0.2
  Downloading duckduckgo_search-8.0.2-py3-none-any.whl (18 kB)
Collecting einops
  Downloading einops-0.8.1-py3-none-any.whl (64 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.4/64.4 kB 5.7 MB/s eta 0:00:00
Collecting fastapi==0.112.4
  Downloading fastapi-0.112.4-py3-none-any.whl (93 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 93.9/93.9 kB 10.5 MB/s eta 0:00:00
Collecting gradio==4.37.*
  Downloading gradio-4.37.2-py3-none-any.whl (12.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.3/12.3 MB 81.8 MB/s eta 0:00:00
Collecting html2text==2025.4.15
  Downloading html2text-2025.4.15-py3-none-any.whl (34 kB)
Collecting jinja2==3.1.6
  Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 134.9/134.9 kB 12.6 MB/s eta 0:00:00
Collecting markdown
  Downloading markdown-3.8.2-py3-none-any.whl (106 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 106.8/106.8 kB 16.1 MB/s eta 0:00:00
Collecting numpy==2.2.*
  Downloading numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.8/16.8 MB 78.5 MB/s eta 0:00:00
Collecting pandas
  Downloading pandas-2.3.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.3/12.3 MB 74.6 MB/s eta 0:00:00
Collecting peft==0.15.*
  Downloading peft-0.15.2-py3-none-any.whl (411 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 411.1/411.1 kB 27.6 MB/s eta 0:00:00
Requirement already satisfied: Pillow>=9.5.0 in ./.venv/lib/python3.10/site-packages (from -r requirements/full/requirements.txt (line 15)) (11.0.0)
Collecting psutil
  Downloading psutil-7.0.0-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (277 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 278.0/278.0 kB 29.9 MB/s eta 0:00:00
Collecting pydantic==2.8.2
  Downloading pydantic-2.8.2-py3-none-any.whl (423 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 423.9/423.9 kB 24.6 MB/s eta 0:00:00
Collecting PyPDF2==3.0.1
  Downloading pypdf2-3.0.1-py3-none-any.whl (232 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 232.6/232.6 kB 22.3 MB/s eta 0:00:00
Collecting python-docx==1.1.2
  Downloading python_docx-1.1.2-py3-none-any.whl (244 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 244.3/244.3 kB 15.7 MB/s eta 0:00:00
Collecting pyyaml
  Downloading PyYAML-6.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (751 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 751.2/751.2 kB 28.3 MB/s eta 0:00:00
Collecting requests
  Downloading requests-2.32.4-py3-none-any.whl (64 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.8/64.8 kB 7.5 MB/s eta 0:00:00
Collecting rich
  Downloading rich-14.0.0-py3-none-any.whl (243 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 243.2/243.2 kB 25.7 MB/s eta 0:00:00
Collecting safetensors==0.5.*
  Downloading safetensors-0.5.3-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (471 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 471.6/471.6 kB 37.1 MB/s eta 0:00:00
Collecting scipy
  Downloading scipy-1.15.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (37.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 37.7/37.7 MB 57.5 MB/s eta 0:00:00
Collecting sentencepiece
  Downloading sentencepiece-0.2.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 53.8 MB/s eta 0:00:00
Collecting tensorboard
  Downloading tensorboard-2.19.0-py3-none-any.whl (5.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 77.5 MB/s eta 0:00:00
Collecting transformers==4.50.*
  Downloading transformers-4.50.3-py3-none-any.whl (10.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.2/10.2 MB 87.9 MB/s eta 0:00:00
Collecting tqdm
  Downloading tqdm-4.67.1-py3-none-any.whl (78 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.5/78.5 kB 11.4 MB/s eta 0:00:00
Collecting wandb
  Downloading wandb-0.20.1-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 23.2/23.2 MB 59.5 MB/s eta 0:00:00
Collecting flask_cloudflared==0.0.14
  Downloading flask_cloudflared-0.0.14-py3-none-any.whl (6.4 kB)
Collecting sse-starlette==1.6.5
  Downloading sse_starlette-1.6.5-py3-none-any.whl (9.6 kB)
Collecting tiktoken
  Downloading tiktoken-0.9.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 53.6 MB/s eta 0:00:00
Collecting huggingface-hub>=0.21.0
  Downloading huggingface_hub-0.33.0-py3-none-any.whl (514 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 514.8/514.8 kB 58.3 MB/s eta 0:00:00
Requirement already satisfied: torch>=2.0.0 in ./.venv/lib/python3.10/site-packages (from accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (2.5.1+cu118)
Collecting packaging>=20.0
  Downloading packaging-25.0-py3-none-any.whl (66 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.5/66.5 kB 10.7 MB/s eta 0:00:00
Collecting lxml>=5.3.0
  Downloading lxml-5.4.0-cp310-cp310-manylinux_2_28_x86_64.whl (5.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.1/5.1 MB 68.9 MB/s eta 0:00:00
Collecting primp>=0.15.0
  Downloading primp-0.15.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 60.6 MB/s eta 0:00:00
Collecting click>=8.1.8
  Downloading click-8.2.1-py3-none-any.whl (102 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 102.2/102.2 kB 17.2 MB/s eta 0:00:00
Collecting starlette<0.39.0,>=0.37.2
  Downloading starlette-0.38.6-py3-none-any.whl (71 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 71.5/71.5 kB 11.3 MB/s eta 0:00:00
Requirement already satisfied: typing-extensions>=4.8.0 in ./.venv/lib/python3.10/site-packages (from fastapi==0.112.4->-r requirements/full/requirements.txt (line 7)) (4.9.0)
Collecting python-multipart>=0.0.9
  Downloading python_multipart-0.0.20-py3-none-any.whl (24 kB)
Collecting ruff>=0.2.2
  Downloading ruff-0.12.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.6/11.6 MB 77.2 MB/s eta 0:00:00
Requirement already satisfied: markupsafe~=2.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (2.1.5)
Collecting importlib-resources<7.0,>=1.3
  Downloading importlib_resources-6.5.2-py3-none-any.whl (37 kB)
Collecting Pillow>=9.5.0
  Downloading pillow-10.4.0-cp310-cp310-manylinux_2_28_x86_64.whl (4.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 69.2 MB/s eta 0:00:00
Collecting matplotlib~=3.0
  Downloading matplotlib-3.10.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (8.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.6/8.6 MB 75.9 MB/s eta 0:00:00
Collecting typer<1.0,>=0.12
  Downloading typer-0.16.0-py3-none-any.whl (46 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 46.3/46.3 kB 6.8 MB/s eta 0:00:00
Collecting tomlkit==0.12.0
  Downloading tomlkit-0.12.0-py3-none-any.whl (37 kB)
Collecting pydub
  Downloading pydub-0.25.1-py2.py3-none-any.whl (32 kB)
Collecting altair<6.0,>=4.2.0
  Downloading altair-5.5.0-py3-none-any.whl (731 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 731.2/731.2 kB 36.0 MB/s eta 0:00:00
Collecting aiofiles<24.0,>=22.0
  Downloading aiofiles-23.2.1-py3-none-any.whl (15 kB)
Collecting httpx>=0.24.1
  Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.5/73.5 kB 8.0 MB/s eta 0:00:00
Collecting semantic-version~=2.0
  Downloading semantic_version-2.10.0-py2.py3-none-any.whl (15 kB)
Collecting ffmpy
  Downloading ffmpy-0.6.0-py3-none-any.whl (5.5 kB)
Collecting gradio-client==1.0.2
  Downloading gradio_client-1.0.2-py3-none-any.whl (318 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 318.2/318.2 kB 23.0 MB/s eta 0:00:00
Collecting urllib3~=2.0
  Downloading urllib3-2.5.0-py3-none-any.whl (129 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 129.8/129.8 kB 16.2 MB/s eta 0:00:00
Collecting orjson~=3.0
  Downloading orjson-3.10.18-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (132 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 132.8/132.8 kB 12.5 MB/s eta 0:00:00
Collecting uvicorn>=0.14.0
  Downloading uvicorn-0.34.3-py3-none-any.whl (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.4/62.4 kB 8.7 MB/s eta 0:00:00
Collecting annotated-types>=0.4.0
  Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
Collecting pydantic-core==2.20.1
  Downloading pydantic_core-2.20.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 85.3 MB/s eta 0:00:00
Requirement already satisfied: filelock in ./.venv/lib/python3.10/site-packages (from transformers==4.50.*->-r requirements/full/requirements.txt (line 27)) (3.13.1)
Collecting tokenizers<0.22,>=0.21
  Downloading tokenizers-0.21.2-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 76.9 MB/s eta 0:00:00
Collecting regex!=2019.12.17
  Downloading regex-2024.11.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (781 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 781.7/781.7 kB 55.7 MB/s eta 0:00:00
Collecting Flask>=0.8
  Downloading flask-3.1.1-py3-none-any.whl (103 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.3/103.3 kB 12.3 MB/s eta 0:00:00
Requirement already satisfied: fsspec in ./.venv/lib/python3.10/site-packages (from gradio-client==1.0.2->gradio==4.37.*->-r requirements/full/requirements.txt (line 8)) (2024.6.1)
Collecting websockets<12.0,>=10.0
  Downloading websockets-11.0.3-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (129 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 129.9/129.9 kB 14.3 MB/s eta 0:00:00
Collecting dill<0.3.9,>=0.3.0
  Downloading dill-0.3.8-py3-none-any.whl (116 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 116.3/116.3 kB 12.0 MB/s eta 0:00:00
Collecting multiprocess<0.70.17
  Downloading multiprocess-0.70.16-py310-none-any.whl (134 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 134.8/134.8 kB 19.5 MB/s eta 0:00:00
Collecting pyarrow>=15.0.0
  Downloading pyarrow-20.0.0-cp310-cp310-manylinux_2_28_x86_64.whl (42.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.3/42.3 MB 18.7 MB/s eta 0:00:00
Collecting xxhash
  Downloading xxhash-3.5.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (194 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 194.1/194.1 kB 27.4 MB/s eta 0:00:00
Collecting pytz>=2020.1
  Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 509.2/509.2 kB 47.2 MB/s eta 0:00:00
Collecting tzdata>=2022.7
  Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 347.8/347.8 kB 31.2 MB/s eta 0:00:00
Collecting python-dateutil>=2.8.2
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.9/229.9 kB 30.0 MB/s eta 0:00:00
Collecting charset_normalizer<4,>=2
  Downloading charset_normalizer-3.4.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (149 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 149.5/149.5 kB 21.9 MB/s eta 0:00:00
Collecting certifi>=2017.4.17
  Downloading certifi-2025.6.15-py3-none-any.whl (157 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 157.7/157.7 kB 15.4 MB/s eta 0:00:00
Collecting idna<4,>=2.5
  Downloading idna-3.10-py3-none-any.whl (70 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 70.4/70.4 kB 6.1 MB/s eta 0:00:00
Collecting markdown-it-py>=2.2.0
  Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 87.5/87.5 kB 8.4 MB/s eta 0:00:00
Collecting pygments<3.0.0,>=2.13.0
  Downloading pygments-2.19.2-py3-none-any.whl (1.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 52.1 MB/s eta 0:00:00
Collecting grpcio>=1.48.2
  Downloading grpcio-1.73.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (6.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.0/6.0 MB 81.9 MB/s eta 0:00:00
Collecting six>1.9
  Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Collecting protobuf!=4.24.0,>=3.19.6
  Downloading protobuf-6.31.1-cp39-abi3-manylinux2014_x86_64.whl (321 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 321.1/321.1 kB 36.4 MB/s eta 0:00:00
Collecting absl-py>=0.4
  Downloading absl_py-2.3.0-py3-none-any.whl (135 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 135.7/135.7 kB 19.3 MB/s eta 0:00:00
Collecting tensorboard-data-server<0.8.0,>=0.7.0
  Downloading tensorboard_data_server-0.7.2-py3-none-manylinux_2_31_x86_64.whl (6.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.6/6.6 MB 85.7 MB/s eta 0:00:00
Requirement already satisfied: setuptools>=41.0.0 in ./.venv/lib/python3.10/site-packages (from tensorboard->-r requirements/full/requirements.txt (line 26)) (65.5.0)
Collecting werkzeug>=1.0.1
  Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 224.5/224.5 kB 27.0 MB/s eta 0:00:00
Collecting sentry-sdk>=2.0.0
  Downloading sentry_sdk-2.31.0-py2.py3-none-any.whl (355 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 355.6/355.6 kB 38.1 MB/s eta 0:00:00
Collecting gitpython!=3.1.29,>=1.0.0
  Downloading GitPython-3.1.44-py3-none-any.whl (207 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 207.6/207.6 kB 25.0 MB/s eta 0:00:00
Collecting setproctitle
  Downloading setproctitle-1.3.6-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (30 kB)
Collecting platformdirs
  Downloading platformdirs-4.3.8-py3-none-any.whl (18 kB)
Collecting narwhals>=1.14.2
  Downloading narwhals-1.44.0-py3-none-any.whl (365 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 365.2/365.2 kB 39.8 MB/s eta 0:00:00
Collecting jsonschema>=3.0
  Downloading jsonschema-4.24.0-py3-none-any.whl (88 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 88.7/88.7 kB 8.1 MB/s eta 0:00:00
Collecting typing-extensions>=4.8.0
  Downloading typing_extensions-4.14.0-py3-none-any.whl (43 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.8/43.8 kB 5.9 MB/s eta 0:00:00
Collecting blinker>=1.9.0
  Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Collecting itsdangerous>=2.2.0
  Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Collecting aiohttp!=4.0.0a0,!=4.0.0a1
  Downloading aiohttp-3.12.13-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 59.1 MB/s eta 0:00:00
Collecting gitdb<5,>=4.0.1
  Downloading gitdb-4.0.12-py3-none-any.whl (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.8/62.8 kB 9.1 MB/s eta 0:00:00
Collecting httpcore==1.*
  Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.8/78.8 kB 12.8 MB/s eta 0:00:00
Collecting anyio
  Downloading anyio-4.9.0-py3-none-any.whl (100 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.9/100.9 kB 16.3 MB/s eta 0:00:00
Collecting h11>=0.16
  Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Collecting hf-xet<2.0.0,>=1.1.2
  Downloading hf_xet-1.1.5-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 20.0 MB/s eta 0:00:00
Collecting mdurl~=0.1
  Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Collecting cycler>=0.10
  Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Collecting fonttools>=4.22.0
  Downloading fonttools-4.58.4-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.8/4.8 MB 43.4 MB/s eta 0:00:00
Collecting kiwisolver>=1.3.1
  Downloading kiwisolver-1.4.8-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 63.8 MB/s eta 0:00:00
Collecting contourpy>=1.0.1
  Downloading contourpy-1.3.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (325 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 325.0/325.0 kB 23.1 MB/s eta 0:00:00
Collecting pyparsing>=2.3.1
  Downloading pyparsing-3.2.3-py3-none-any.whl (111 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 111.1/111.1 kB 17.0 MB/s eta 0:00:00
Requirement already satisfied: nvidia-cuda-runtime-cu11==11.8.89 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.8.89)
Requirement already satisfied: nvidia-nccl-cu11==2.21.5 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (2.21.5)
Requirement already satisfied: sympy==1.13.1 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (1.13.1)
Requirement already satisfied: nvidia-cudnn-cu11==9.1.0.70 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (9.1.0.70)
Requirement already satisfied: nvidia-cuda-nvrtc-cu11==11.8.89 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.8.89)
Requirement already satisfied: nvidia-cufft-cu11==10.9.0.58 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (10.9.0.58)
Requirement already satisfied: networkx in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (3.3)
Requirement already satisfied: nvidia-cuda-cupti-cu11==11.8.87 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.8.87)
Requirement already satisfied: nvidia-curand-cu11==10.3.0.86 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (10.3.0.86)
Requirement already satisfied: nvidia-cublas-cu11==11.11.3.6 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.11.3.6)
Requirement already satisfied: nvidia-cusolver-cu11==11.4.1.48 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.4.1.48)
Requirement already satisfied: nvidia-nvtx-cu11==11.8.86 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.8.86)
Requirement already satisfied: nvidia-cusparse-cu11==11.7.5.86 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (11.7.5.86)
Requirement already satisfied: triton==3.1.0 in ./.venv/lib/python3.10/site-packages (from torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (3.1.0)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in ./.venv/lib/python3.10/site-packages (from sympy==1.13.1->torch>=2.0.0->accelerate==1.5.*->-r requirements/full/requirements.txt (line 1)) (1.3.0)
Collecting shellingham>=1.3.0
  Downloading shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
Collecting frozenlist>=1.1.1
  Downloading frozenlist-1.7.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (222 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 222.9/222.9 kB 17.4 MB/s eta 0:00:00
Collecting multidict<7.0,>=4.5
  Downloading multidict-6.4.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (219 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 219.1/219.1 kB 24.0 MB/s eta 0:00:00
Collecting propcache>=0.2.0
  Downloading propcache-0.3.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (198 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 198.3/198.3 kB 20.3 MB/s eta 0:00:00
Collecting attrs>=17.3.0
  Downloading attrs-25.3.0-py3-none-any.whl (63 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.8/63.8 kB 9.7 MB/s eta 0:00:00
Collecting async-timeout<6.0,>=4.0
  Downloading async_timeout-5.0.1-py3-none-any.whl (6.2 kB)
Collecting aiosignal>=1.1.2
  Downloading aiosignal-1.3.2-py2.py3-none-any.whl (7.6 kB)
Collecting aiohappyeyeballs>=2.5.0
  Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
Collecting yarl<2.0,>=1.17.0
  Downloading yarl-1.20.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (326 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 326.1/326.1 kB 21.1 MB/s eta 0:00:00
Collecting exceptiongroup>=1.0.2
  Downloading exceptiongroup-1.3.0-py3-none-any.whl (16 kB)
Collecting sniffio>=1.1
  Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
Collecting smmap<6,>=3.0.1
  Downloading smmap-5.0.2-py3-none-any.whl (24 kB)
Collecting referencing>=0.28.4
  Downloading referencing-0.36.2-py3-none-any.whl (26 kB)
Collecting rpds-py>=0.7.1
  Downloading rpds_py-0.25.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (386 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 387.0/387.0 kB 28.1 MB/s eta 0:00:00
Collecting jsonschema-specifications>=2023.03.6
  Downloading jsonschema_specifications-2025.4.1-py3-none-any.whl (18 kB)
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
Successfully installed Flask-3.1.1 Pillow-10.4.0 PyPDF2-3.0.1 absl-py-2.3.0 accelerate-1.5.2 aiofiles-23.2.1 aiohappyeyeballs-2.6.1 aiohttp-3.12.13 aiosignal-1.3.2 altair-5.5.0 annotated-types-0.7.0 anyio-4.9.0 async-timeout-5.0.1 attrs-25.3.0 bitsandbytes-0.45.5 blinker-1.9.0 certifi-2025.6.15 charset_normalizer-3.4.2 click-8.2.1 colorama-0.4.6 contourpy-1.3.2 cycler-0.12.1 datasets-3.6.0 dill-0.3.8 duckduckgo_search-8.0.2 einops-0.8.1 exceptiongroup-1.3.0 fastapi-0.112.4 ffmpy-0.6.0 flask_cloudflared-0.0.14 fonttools-4.58.4 frozenlist-1.7.0 gitdb-4.0.12 gitpython-3.1.44 gradio-4.37.2 gradio-client-1.0.2 grpcio-1.73.0 h11-0.16.0 hf-xet-1.1.5 html2text-2025.4.15 httpcore-1.0.9 httpx-0.28.1 huggingface-hub-0.33.0 idna-3.10 importlib-resources-6.5.2 itsdangerous-2.2.0 jinja2-3.1.6 jsonschema-4.24.0 jsonschema-specifications-2025.4.1 kiwisolver-1.4.8 lxml-5.4.0 markdown-3.8.2 markdown-it-py-3.0.0 matplotlib-3.10.3 mdurl-0.1.2 multidict-6.4.4 multiprocess-0.70.16 narwhals-1.44.0 numpy-2.2.6 orjson-3.10.18 packaging-25.0 pandas-2.3.0 peft-0.15.2 platformdirs-4.3.8 primp-0.15.0 propcache-0.3.2 protobuf-6.31.1 psutil-7.0.0 pyarrow-20.0.0 pydantic-2.8.2 pydantic-core-2.20.1 pydub-0.25.1 pygments-2.19.2 pyparsing-3.2.3 python-dateutil-2.9.0.post0 python-docx-1.1.2 python-multipart-0.0.20 pytz-2025.2 pyyaml-6.0.2 referencing-0.36.2 regex-2024.11.6 requests-2.32.4 rich-14.0.0 rpds-py-0.25.1 ruff-0.12.0 safetensors-0.5.3 scipy-1.15.3 semantic-version-2.10.0 sentencepiece-0.2.0 sentry-sdk-2.31.0 setproctitle-1.3.6 shellingham-1.5.4 six-1.17.0 smmap-5.0.2 sniffio-1.3.1 sse-starlette-1.6.5 starlette-0.38.6 tensorboard-2.19.0 tensorboard-data-server-0.7.2 tiktoken-0.9.0 tokenizers-0.21.2 tomlkit-0.12.0 tqdm-4.67.1 transformers-4.50.3 typer-0.16.0 typing-extensions-4.14.0 tzdata-2025.2 urllib3-2.5.0 uvicorn-0.34.3 wandb-0.20.1 websockets-11.0.3 werkzeug-3.1.3 xxhash-3.5.0 yarl-1.20.1
WARNING: There was an error checking the latest version of pip.
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Fantastic! That was a massive success! You can see pip downloaded and installed a huge list of dependencies, including gradio-4.37.2 and gradio-client-1.0.2, which are the versions we specifically targeted. The "Ignoring" messages at the beginning are perfectly normal; they just mean those specific packages (like llama-cpp-binaries, exllamav3, flash-attn) have specific Python or OS requirements that don't match your current Python 3.10 setup, so pip skips them. This is expected and fine, especially since we're using --loader llama.cpp which often has its own compilation process. Now, let's complete the dependency installation. Action: Run the pip install markdown command (even though markdown seems to have been installed by the previous step, it's good to ensure): pip install markdown Run the explicit gradio and gradio_client installation again (this is a safeguard to ensure the versions stay correct): pip install gradio==4.37.2 gradio_client==1.0.2 Run the llama.cpp specific build (important for the --loader llama.cpp argument): pip install -r extensions/webui_llama_cpp/requirements.txt Finally, launch Oobabooga: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2 Please provide the output of each of these commands. We are now at the most promising point to see Oobabooga launch successfully!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]