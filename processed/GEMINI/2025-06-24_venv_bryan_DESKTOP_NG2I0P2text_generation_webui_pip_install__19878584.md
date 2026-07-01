---
id: 412432
source: GEMINI
date: 2025-06-24
tags: ['coding', 'ai', 'gemini', 'oobabooga', 'text-generation', 'go', 'script', 'error']
category: coding
sentiment: executing
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install -r requirements/requirements.txt --upgrade
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements/requirements.txt'

[notice] A new release of pip is available: 24.0 -> 25.1.1
[notice] To update, run: pip install --upgrade pip
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install -r requirements/requirements.txt --upgrade
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements/requirements.txt'

[notice] A new release of pip is available: 24.0 -> 25.1.1
[notice] To update, run: pip install --upgrade pip
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
This is an unexpected twist! You're right, I also missed a detail here. My apologies. You are seeing: ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements/requirements.txt' This means that while there is a requirements/ directory, the actual requirements.txt file is not inside it. Instead, the ls -l output you provided earlier shows a requirements directory and then several other files at the top level of text-generation-webui. Let's re-examine that ls -l output very carefully, looking for a file that is a requirements file. Looking back at your output from ls -l in ~/text-generation-webui: drwxr-xr-x 4 bryan_ bryan_ 4096 Jun 18 21:29 requirements This line shows requirements as a directory (d at the beginning). However, I now see the issue. Oobabooga's repository structure has changed over time. Many older guides (and my previous assumptions) might point to requirements.txt being at the root. In newer versions, it seems the dependencies are often managed directly by the start_linux.sh script or other installer scripts, or the dependencies are listed in a different file. It's clear there's no requirements.txt directly at the root, nor in a requirements/requirements.txt path. Given this, trying to pip install -r a non-existent file will never work. What this means: Oobabooga likely has its dependencies handled differently in your version of the repo, or the main start_linux.sh script is the intended way to install/update dependencies. Let's go back to the most common and robust way Oobabooga manages its dependencies, which is through its start_linux.sh script. This script is designed to set up the environment and install necessary packages. Step 18: Use start_linux.sh to Repair/Update Dependencies The start_linux.sh script usually handles creating the virtual environment and installing all required packages. Running it again should ensure all dependencies are correctly installed and updated. Action: Stop Oobabooga completely. (If it's running). Press Ctrl + C repeatedly in your WSL2 terminal until you see your prompt. Ensure you are in the top-level text-generation-webui directory: cd ~/text-generation-webui Run the start_linux.sh script: ./start_linux.sh This script will check your environment, potentially activate the virtual environment, and then install/update all necessary dependencies. It might ask you some questions (e.g., if you want to update). Answer y if prompted for updates. This process can take a significant amount of time, as it will likely download and compile various packages. Let it run to completion. Once the start_linux.sh script finishes and successfully launches the web UI (it should open automatically or give you the URL), open a new incognito/private browser window and go to http://127.0.0.1:7860. Carefully check all tabs again for "SuperBooga". This is the most "official" way to ensure Oobabooga's dependencies are correctly set up for your specific version. This should fix any underlying dependency issues that might be preventing the UI from rendering the extension tab. Please share the full output from running ./start_linux.sh and whether the tab appears after it finishes.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]