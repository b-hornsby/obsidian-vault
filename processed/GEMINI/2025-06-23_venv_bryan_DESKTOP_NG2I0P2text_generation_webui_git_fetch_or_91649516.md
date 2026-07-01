---
category: ai-tools
date: 2025-06-23
id: 648112
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: partial
sentiment: executing
source: GEMINI
summary: The user was updating their local text-generation-webui installation by fetching
  the latest code from the main branch and preparing to install dependencies via pip.
tags:
- text-generation-webui
- git-update
- dependency-installation
- local-ai
- oobabooga
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ git fetch origin main
From https://github.com/oobabooga/text-generation-webui
 * branch              main       -> FETCH_HEAD
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ git reset --hard origin/main
HEAD is now at 17f9c188 Merge pull request #7092 from oobabooga/dev
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ git pull
Already up to date.
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install -r requirements.txt --upgrade
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'

[notice] A new release of pip is available: 24.0 -> 25.1.1
[notice] To update, run: pip install --upgrade pip
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
16:47:38-925727 INFO     Starting Text generation web UI
16:47:38-927565 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ git fetch origin main
From https://github.com/oobabooga/text-generation-webui
 * branch              main       -> FETCH_HEAD
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ git reset --hard origin/main
HEAD is now at 17f9c188 Merge pull request #7092 from oobabooga/dev
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ git pull
Already up to date.
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install -r requirements.txt --upgrade
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'

[notice] A new release of pip is available: 24.0 -> 25.1.1
[notice] To update, run: pip install --upgrade pip
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
16:47:38-925727 INFO     Starting Text generation web UI
16:47:38-927565 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

### GEMINI
You're so close, Bryan! The git fetch, git reset --hard, and git pull commands all worked perfectly, meaning your Oobabooga codebase is now fully up to date with the latest version. That's a big hurdle cleared! The error you're seeing: ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt' means that for some reason, when pip tried to run, it couldn't find the requirements.txt file in your current directory. This is very unusual after a git reset --hard origin/main because that file should definitely be there in the root of the text-generation-webui directory in the latest version. Let's quickly check if the file is actually there. Make sure you are still in the text-generation-webui directory in your WSL2 terminal. Your prompt (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ confirms you are. List the contents of your directory: Type the following command and press Enter: ls -la This command will list all files and folders in your current directory, including hidden ones. Please share the output of that ls -la command. We need to confirm if requirements.txt is present and visible in that list. Based on that, we'll figure out why pip couldn't find it.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]