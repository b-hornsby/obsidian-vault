---
id: 776515
source: GEMINI
date: 2025-06-24
tags: ['coding', 'ai', 'gemini', 'model', 'oobabooga', 'llama.cpp', 'text-generation', 'python']
category: coding
sentiment: building
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install markdown
Requirement already satisfied: markdown in ./.venv/lib/python3.10/site-packages (3.8.2)
WARNING: There was an error checking the latest version of pip.
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install gradio==4.37.2 gradio_client==1.0.2
Requirement already satisfied: gradio==4.37.2 in ./.venv/lib/python3.10/site-packages (4.37.2)
Requirement already satisfied: gradio_client==1.0.2 in ./.venv/lib/python3.10/site-packages (1.0.2)
Requirement already satisfied: fastapi in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.112.4)
Requirement already satisfied: ruff>=0.2.2 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.12.0)
Requirement already satisfied: pandas<3.0,>=1.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (2.3.0)
Requirement already satisfied: aiofiles<24.0,>=22.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (23.2.1)
Requirement already satisfied: uvicorn>=0.14.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.34.3)
Requirement already satisfied: matplotlib~=3.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (3.10.3)
Requirement already satisfied: tomlkit==0.12.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.12.0)
Requirement already satisfied: huggingface-hub>=0.19.3 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.33.0)
Requirement already satisfied: orjson~=3.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (3.10.18)
Requirement already satisfied: pillow<11.0,>=8.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (10.4.0)
Requirement already satisfied: typing-extensions~=4.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (4.14.0)
Requirement already satisfied: python-multipart>=0.0.9 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.0.20)
Requirement already satisfied: pyyaml<7.0,>=5.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (6.0.2)
Requirement already satisfied: pydub in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.25.1)
Requirement already satisfied: httpx>=0.24.1 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.28.1)
Requirement already satisfied: typer<1.0,>=0.12 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.16.0)
Requirement already satisfied: pydantic>=2.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (2.8.2)
Requirement already satisfied: importlib-resources<7.0,>=1.3 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (6.5.2)
Requirement already satisfied: semantic-version~=2.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (2.10.0)
Requirement already satisfied: ffmpy in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.6.0)
Requirement already satisfied: urllib3~=2.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (2.5.0)
Requirement already satisfied: altair<6.0,>=4.2.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (5.5.0)
Requirement already satisfied: jinja2<4.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (3.1.6)
Requirement already satisfied: markupsafe~=2.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (2.1.5)
Requirement already satisfied: packaging in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (25.0)
Requirement already satisfied: numpy<3.0,>=1.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (2.2.6)
Requirement already satisfied: fsspec in ./.venv/lib/python3.10/site-packages (from gradio_client==1.0.2) (2024.6.1)
Requirement already satisfied: websockets<12.0,>=10.0 in ./.venv/lib/python3.10/site-packages (from gradio_client==1.0.2) (11.0.3)
Requirement already satisfied: narwhals>=1.14.2 in ./.venv/lib/python3.10/site-packages (from altair<6.0,>=4.2.0->gradio==4.37.2) (1.44.0)
Requirement already satisfied: jsonschema>=3.0 in ./.venv/lib/python3.10/site-packages (from altair<6.0,>=4.2.0->gradio==4.37.2) (4.24.0)
Requirement already satisfied: anyio in ./.venv/lib/python3.10/site-packages (from httpx>=0.24.1->gradio==4.37.2) (4.9.0)
Requirement already satisfied: idna in ./.venv/lib/python3.10/site-packages (from httpx>=0.24.1->gradio==4.37.2) (3.10)
Requirement already satisfied: certifi in ./.venv/lib/python3.10/site-packages (from httpx>=0.24.1->gradio==4.37.2) (2025.6.15)
Requirement already satisfied: httpcore==1.* in ./.venv/lib/python3.10/site-packages (from httpx>=0.24.1->gradio==4.37.2) (1.0.9)
Requirement already satisfied: h11>=0.16 in ./.venv/lib/python3.10/site-packages (from httpcore==1.*->httpx>=0.24.1->gradio==4.37.2) (0.16.0)
Requirement already satisfied: hf-xet<2.0.0,>=1.1.2 in ./.venv/lib/python3.10/site-packages (from huggingface-hub>=0.19.3->gradio==4.37.2) (1.1.5)
Requirement already satisfied: tqdm>=4.42.1 in ./.venv/lib/python3.10/site-packages (from huggingface-hub>=0.19.3->gradio==4.37.2) (4.67.1)
Requirement already satisfied: filelock in ./.venv/lib/python3.10/site-packages (from huggingface-hub>=0.19.3->gradio==4.37.2) (3.13.1)
Requirement already satisfied: requests in ./.venv/lib/python3.10/site-packages (from huggingface-hub>=0.19.3->gradio==4.37.2) (2.32.4)
Requirement already satisfied: contourpy>=1.0.1 in ./.venv/lib/python3.10/site-packages (from matplotlib~=3.0->gradio==4.37.2) (1.3.2)
Requirement already satisfied: cycler>=0.10 in ./.venv/lib/python3.10/site-packages (from matplotlib~=3.0->gradio==4.37.2) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in ./.venv/lib/python3.10/site-packages (from matplotlib~=3.0->gradio==4.37.2) (4.58.4)
Requirement already satisfied: pyparsing>=2.3.1 in ./.venv/lib/python3.10/site-packages (from matplotlib~=3.0->gradio==4.37.2) (3.2.3)
Requirement already satisfied: python-dateutil>=2.7 in ./.venv/lib/python3.10/site-packages (from matplotlib~=3.0->gradio==4.37.2) (2.9.0.post0)
Requirement already satisfied: kiwisolver>=1.3.1 in ./.venv/lib/python3.10/site-packages (from matplotlib~=3.0->gradio==4.37.2) (1.4.8)
Requirement already satisfied: pytz>=2020.1 in ./.venv/lib/python3.10/site-packages (from pandas<3.0,>=1.0->gradio==4.37.2) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in ./.venv/lib/python3.10/site-packages (from pandas<3.0,>=1.0->gradio==4.37.2) (2025.2)
Requirement already satisfied: annotated-types>=0.4.0 in ./.venv/lib/python3.10/site-packages (from pydantic>=2.0->gradio==4.37.2) (0.7.0)
Requirement already satisfied: pydantic-core==2.20.1 in ./.venv/lib/python3.10/site-packages (from pydantic>=2.0->gradio==4.37.2) (2.20.1)
Requirement already satisfied: click>=8.0.0 in ./.venv/lib/python3.10/site-packages (from typer<1.0,>=0.12->gradio==4.37.2) (8.2.1)
Requirement already satisfied: shellingham>=1.3.0 in ./.venv/lib/python3.10/site-packages (from typer<1.0,>=0.12->gradio==4.37.2) (1.5.4)
Requirement already satisfied: rich>=10.11.0 in ./.venv/lib/python3.10/site-packages (from typer<1.0,>=0.12->gradio==4.37.2) (14.0.0)
Requirement already satisfied: starlette<0.39.0,>=0.37.2 in ./.venv/lib/python3.10/site-packages (from fastapi->gradio==4.37.2) (0.38.6)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in ./.venv/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio==4.37.2) (2025.4.1)
Requirement already satisfied: attrs>=22.2.0 in ./.venv/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio==4.37.2) (25.3.0)
Requirement already satisfied: referencing>=0.28.4 in ./.venv/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio==4.37.2) (0.36.2)
Requirement already satisfied: rpds-py>=0.7.1 in ./.venv/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio==4.37.2) (0.25.1)
Requirement already satisfied: six>=1.5 in ./.venv/lib/python3.10/site-packages (from python-dateutil>=2.7->matplotlib~=3.0->gradio==4.37.2) (1.17.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in ./.venv/lib/python3.10/site-packages (from rich>=10.11.0->typer<1.0,>=0.12->gradio==4.37.2) (2.19.2)
Requirement already satisfied: markdown-it-py>=2.2.0 in ./.venv/lib/python3.10/site-packages (from rich>=10.11.0->typer<1.0,>=0.12->gradio==4.37.2) (3.0.0)
Requirement already satisfied: exceptiongroup>=1.0.2 in ./.venv/lib/python3.10/site-packages (from anyio->httpx>=0.24.1->gradio==4.37.2) (1.3.0)
Requirement already satisfied: sniffio>=1.1 in ./.venv/lib/python3.10/site-packages (from anyio->httpx>=0.24.1->gradio==4.37.2) (1.3.1)
Requirement already satisfied: charset_normalizer<4,>=2 in ./.venv/lib/python3.10/site-packages (from requests->huggingface-hub>=0.19.3->gradio==4.37.2) (3.4.2)
Requirement already satisfied: mdurl~=0.1 in ./.venv/lib/python3.10/site-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0,>=0.12->gradio==4.37.2) (0.1.2)
WARNING: There was an error checking the latest version of pip.
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install markdown
Requirement already satisfied: markdown in ./.venv/lib/python3.10/site-packages (3.8.2)
WARNING: There was an error checking the latest version of pip.
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install gradio==4.37.2 gradio_client==1.0.2
Requirement already satisfied: gradio==4.37.2 in ./.venv/lib/python3.10/site-packages (4.37.2)
Requirement already satisfied: gradio_client==1.0.2 in ./.venv/lib/python3.10/site-packages (1.0.2)
Requirement already satisfied: fastapi in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.112.4)
Requirement already satisfied: ruff>=0.2.2 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.12.0)
Requirement already satisfied: pandas<3.0,>=1.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (2.3.0)
Requirement already satisfied: aiofiles<24.0,>=22.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (23.2.1)
Requirement already satisfied: uvicorn>=0.14.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.34.3)
Requirement already satisfied: matplotlib~=3.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (3.10.3)
Requirement already satisfied: tomlkit==0.12.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.12.0)
Requirement already satisfied: huggingface-hub>=0.19.3 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.33.0)
Requirement already satisfied: orjson~=3.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (3.10.18)
Requirement already satisfied: pillow<11.0,>=8.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (10.4.0)
Requirement already satisfied: typing-extensions~=4.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (4.14.0)
Requirement already satisfied: python-multipart>=0.0.9 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.0.20)
Requirement already satisfied: pyyaml<7.0,>=5.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (6.0.2)
Requirement already satisfied: pydub in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.25.1)
Requirement already satisfied: httpx>=0.24.1 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.28.1)
Requirement already satisfied: typer<1.0,>=0.12 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.16.0)
Requirement already satisfied: pydantic>=2.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (2.8.2)
Requirement already satisfied: importlib-resources<7.0,>=1.3 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (6.5.2)
Requirement already satisfied: semantic-version~=2.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (2.10.0)
Requirement already satisfied: ffmpy in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (0.6.0)
Requirement already satisfied: urllib3~=2.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (2.5.0)
Requirement already satisfied: altair<6.0,>=4.2.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (5.5.0)
Requirement already satisfied: jinja2<4.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (3.1.6)
Requirement already satisfied: markupsafe~=2.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (2.1.5)
Requirement already satisfied: packaging in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (25.0)
Requirement already satisfied: numpy<3.0,>=1.0 in ./.venv/lib/python3.10/site-packages (from gradio==4.37.2) (2.2.6)
Requirement already satisfied: fsspec in ./.venv/lib/python3.10/site-packages (from gradio_client==1.0.2) (2024.6.1)
Requirement already satisfied: websockets<12.0,>=10.0 in ./.venv/lib/python3.10/site-packages (from gradio_client==1.0.2) (11.0.3)
Requirement already satisfied: narwhals>=1.14.2 in ./.venv/lib/python3.10/site-packages (from altair<6.0,>=4.2.0->gradio==4.37.2) (1.44.0)
Requirement already satisfied: jsonschema>=3.0 in ./.venv/lib/python3.10/site-packages (from altair<6.0,>=4.2.0->gradio==4.37.2) (4.24.0)
Requirement already satisfied: anyio in ./.venv/lib/python3.10/site-packages (from httpx>=0.24.1->gradio==4.37.2) (4.9.0)
Requirement already satisfied: idna in ./.venv/lib/python3.10/site-packages (from httpx>=0.24.1->gradio==4.37.2) (3.10)
Requirement already satisfied: certifi in ./.venv/lib/python3.10/site-packages (from httpx>=0.24.1->gradio==4.37.2) (2025.6.15)
Requirement already satisfied: httpcore==1.* in ./.venv/lib/python3.10/site-packages (from httpx>=0.24.1->gradio==4.37.2) (1.0.9)
Requirement already satisfied: h11>=0.16 in ./.venv/lib/python3.10/site-packages (from httpcore==1.*->httpx>=0.24.1->gradio==4.37.2) (0.16.0)
Requirement already satisfied: hf-xet<2.0.0,>=1.1.2 in ./.venv/lib/python3.10/site-packages (from huggingface-hub>=0.19.3->gradio==4.37.2) (1.1.5)
Requirement already satisfied: tqdm>=4.42.1 in ./.venv/lib/python3.10/site-packages (from huggingface-hub>=0.19.3->gradio==4.37.2) (4.67.1)
Requirement already satisfied: filelock in ./.venv/lib/python3.10/site-packages (from huggingface-hub>=0.19.3->gradio==4.37.2) (3.13.1)
Requirement already satisfied: requests in ./.venv/lib/python3.10/site-packages (from huggingface-hub>=0.19.3->gradio==4.37.2) (2.32.4)
Requirement already satisfied: contourpy>=1.0.1 in ./.venv/lib/python3.10/site-packages (from matplotlib~=3.0->gradio==4.37.2) (1.3.2)
Requirement already satisfied: cycler>=0.10 in ./.venv/lib/python3.10/site-packages (from matplotlib~=3.0->gradio==4.37.2) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in ./.venv/lib/python3.10/site-packages (from matplotlib~=3.0->gradio==4.37.2) (4.58.4)
Requirement already satisfied: pyparsing>=2.3.1 in ./.venv/lib/python3.10/site-packages (from matplotlib~=3.0->gradio==4.37.2) (3.2.3)
Requirement already satisfied: python-dateutil>=2.7 in ./.venv/lib/python3.10/site-packages (from matplotlib~=3.0->gradio==4.37.2) (2.9.0.post0)
Requirement already satisfied: kiwisolver>=1.3.1 in ./.venv/lib/python3.10/site-packages (from matplotlib~=3.0->gradio==4.37.2) (1.4.8)
Requirement already satisfied: pytz>=2020.1 in ./.venv/lib/python3.10/site-packages (from pandas<3.0,>=1.0->gradio==4.37.2) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in ./.venv/lib/python3.10/site-packages (from pandas<3.0,>=1.0->gradio==4.37.2) (2025.2)
Requirement already satisfied: annotated-types>=0.4.0 in ./.venv/lib/python3.10/site-packages (from pydantic>=2.0->gradio==4.37.2) (0.7.0)
Requirement already satisfied: pydantic-core==2.20.1 in ./.venv/lib/python3.10/site-packages (from pydantic>=2.0->gradio==4.37.2) (2.20.1)
Requirement already satisfied: click>=8.0.0 in ./.venv/lib/python3.10/site-packages (from typer<1.0,>=0.12->gradio==4.37.2) (8.2.1)
Requirement already satisfied: shellingham>=1.3.0 in ./.venv/lib/python3.10/site-packages (from typer<1.0,>=0.12->gradio==4.37.2) (1.5.4)
Requirement already satisfied: rich>=10.11.0 in ./.venv/lib/python3.10/site-packages (from typer<1.0,>=0.12->gradio==4.37.2) (14.0.0)
Requirement already satisfied: starlette<0.39.0,>=0.37.2 in ./.venv/lib/python3.10/site-packages (from fastapi->gradio==4.37.2) (0.38.6)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in ./.venv/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio==4.37.2) (2025.4.1)
Requirement already satisfied: attrs>=22.2.0 in ./.venv/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio==4.37.2) (25.3.0)
Requirement already satisfied: referencing>=0.28.4 in ./.venv/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio==4.37.2) (0.36.2)
Requirement already satisfied: rpds-py>=0.7.1 in ./.venv/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio==4.37.2) (0.25.1)
Requirement already satisfied: six>=1.5 in ./.venv/lib/python3.10/site-packages (from python-dateutil>=2.7->matplotlib~=3.0->gradio==4.37.2) (1.17.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in ./.venv/lib/python3.10/site-packages (from rich>=10.11.0->typer<1.0,>=0.12->gradio==4.37.2) (2.19.2)
Requirement already satisfied: markdown-it-py>=2.2.0 in ./.venv/lib/python3.10/site-packages (from rich>=10.11.0->typer<1.0,>=0.12->gradio==4.37.2) (3.0.0)
Requirement already satisfied: exceptiongroup>=1.0.2 in ./.venv/lib/python3.10/site-packages (from anyio->httpx>=0.24.1->gradio==4.37.2) (1.3.0)
Requirement already satisfied: sniffio>=1.1 in ./.venv/lib/python3.10/site-packages (from anyio->httpx>=0.24.1->gradio==4.37.2) (1.3.1)
Requirement already satisfied: charset_normalizer<4,>=2 in ./.venv/lib/python3.10/site-packages (from requests->huggingface-hub>=0.19.3->gradio==4.37.2) (3.4.2)
Requirement already satisfied: mdurl~=0.1 in ./.venv/lib/python3.10/site-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0,>=0.12->gradio==4.37.2) (0.1.2)
WARNING: There was an error checking the latest version of pip.
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Excellent! Both pip install markdown and pip install gradio==4.37.2 gradio_client==1.0.2 show "Requirement already satisfied," which is exactly what we want. This confirms that these crucial packages are installed at the correct versions within your new Python 3.10 virtual environment. Now, let's install the specific requirements for the llama.cpp extension. Action: Execute the llama.cpp specific build: pip install -r extensions/webui_llama_cpp/requirements.txt This command will install any Python dependencies specific to the llama.cpp integration. Finally, if that completes successfully, launch Oobabooga: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2 Please share the full output of pip install -r extensions/webui_llama_cpp/requirements.txt. Then, if that's good, try running server.py and let me know if it launches correctly or if you encounter any new errors. We are incredibly close!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]