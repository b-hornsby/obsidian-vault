---
category: homelab
date: 2025-06-24
id: 858109
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user was trying to set up text-generation-webui in a Python virtual environment
  but failed because the requirements.txt file was missing from the directory.
tags:
- text-generation-webui
- python-venv
- dependency-installation
- setup-error
- requirements-missing
---
# bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cd ~/text-generation-webui
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 -m venv venv
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ source venv/bin/activate
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install -r requirements.txt
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cd ~/text-generation-webui
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 -m venv venv
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ source venv/bin/activate
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install -r requirements.txt
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
You've activated the virtual environment successfully, which is great! You can tell by (venv) at the beginning of your prompt. However, it looks like pip couldn't find the requirements.txt file: ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'. This file should definitely be present in the main text-generation-webui directory if it was cloned correctly. Let's verify its existence. While still in your ~/text-generation-webui directory, please run: ls -l requirements.txt And also list the general contents of the directory to confirm: ls -l Possible outcomes: If ls -l requirements.txt shows the file: This would be very odd, as pip should have found it. We'd investigate further. If ls -l requirements.txt shows No such file or directory: This means the file is indeed missing. If ls -l shows a file with a similar name (e.g., requirements-wsl.txt or install_requirements.txt), then we'll use that. Please share the output of those ls -l commands. If requirements.txt is truly missing, we might have a problem with the initial clone of text-generation-webui.