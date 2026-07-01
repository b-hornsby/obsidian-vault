---
category: homelab
date: 2025-06-23
id: 552752
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user attempted to set up text-generation-webui in a Python virtual environment
  but encountered an error because the requirements.txt file was missing, halting
  the installation process.
tags:
- local-ai
- text-generation-webui
- python-venv
- dependency-installation
- setup-error
---
# bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 -m venv .venv
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ source .venv/bin/activate
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install -r requirements.txt
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 -m venv .venv
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ source .venv/bin/activate
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install -r requirements.txt
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
You're doing great with the commands, and hitting these errors is a normal part of the process when setting up complex software like this! The error ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt' is super clear. It means that while you're in the text-generation-webui directory, the requirements.txt file itself isn't directly in that folder. Oobabooga recently reorganized its repository, and the requirements.txt files are now located in a requirements subdirectory. Step 6: Install Missing Python Dependencies (Corrected Path) Action: We need to specify the correct path to the requirements.txt file. Based on the oobabooga repository structure, it's typically within a requirements/ subfolder. We also need to pick the correct requirements file for NVIDIA GPUs and an AVX2-capable CPU (which your i7-12700K definitely is). What I need you to do now (in your Ubuntu WSL2 terminal, still in (.venv) ~/text-generation-webui$): Install the dependencies with the correct path: Command: pip install -r requirements/requirements.txt Explanation of the change: requirements/requirements.txt: This specifies that pip should look for the requirements.txt file inside the requirements subdirectory. This is the standard file for NVIDIA GPUs with AVX2 support (which your i7-12700K has). What I need from you: Run the pip install -r requirements/requirements.txt command. Copy and paste the entire output here. This step will download and install a significant number of packages and will take several minutes (could be 5-15 minutes or more depending on your internet speed and system performance). You'll see a lot of lines scrolling by indicating download progress and installation. Let's get those dependencies installed!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]