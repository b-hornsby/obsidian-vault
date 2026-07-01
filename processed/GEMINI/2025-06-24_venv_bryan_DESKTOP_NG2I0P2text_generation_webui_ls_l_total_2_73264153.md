---
id: 577870
source: GEMINI
date: 2025-06-24
tags: ['coding', 'module', 'docker', 'ai', 'gemini', 'model', 'text-generation', 'python']
category: coding
sentiment: building
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
---
# (venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -l
total 204
-rw-r--r--  1 bryan_ bryan_  4080 Jun 24 14:21 Colab-TextGen-GPU.ipynb
-rw-r--r--  1 bryan_ bryan_ 34523 Jun 24 14:21 LICENSE
-rw-r--r--  1 bryan_ bryan_ 24673 Jun 24 14:21 README.md
-rwxr-xr-x  1 bryan_ bryan_   728 Jun 24 14:21 cmd_linux.sh
-rwxr-xr-x  1 bryan_ bryan_   699 Jun 24 14:21 cmd_macos.sh
-rwxr-xr-x  1 bryan_ bryan_   938 Jun 24 14:21 cmd_windows.bat
drwxr-xr-x  6 bryan_ bryan_  4096 Jun 24 14:21 css
drwxr-xr-x  7 bryan_ bryan_  4096 Jun 24 14:21 docker
drwxr-xr-x  2 bryan_ bryan_  4096 Jun 24 14:21 docs
-rw-r--r--  1 bryan_ bryan_ 18192 Jun 24 14:21 download-model.py
drwxr-xr-x 18 bryan_ bryan_  4096 Jun 24 14:21 extensions
drwxr-xr-x  5 bryan_ bryan_  4096 Jun 24 14:21 js
drwxr-xr-x  4 bryan_ bryan_  4096 Jun 24 15:19 modules
-rw-r--r--  1 bryan_ bryan_ 20322 Jun 24 14:21 one_click.py
drwxr-xr-x  3 bryan_ bryan_  4096 Jun 24 14:24 repositories
drwxr-xr-x  4 bryan_ bryan_  4096 Jun 24 14:21 requirements
-rw-r--r--  1 bryan_ bryan_ 12231 Jun 24 14:21 server.py
-rw-r--r--  1 bryan_ bryan_    61 Jun 24 14:21 setup.cfg
-rwxr-xr-x  1 bryan_ bryan_  2516 Jun 24 14:21 start_linux.sh
-rwxr-xr-x  1 bryan_ bryan_  2505 Jun 24 14:21 start_macos.sh
-rwxr-xr-x  1 bryan_ bryan_  4233 Jun 24 14:21 start_windows.bat
-rwxr-xr-x  1 bryan_ bryan_   889 Jun 24 14:21 update_wizard_linux.sh
-rwxr-xr-x  1 bryan_ bryan_   881 Jun 24 14:21 update_wizard_macos.sh
-rwxr-xr-x  1 bryan_ bryan_  1017 Jun 24 14:21 update_wizard_windows.bat
drwxr-xr-x  9 bryan_ bryan_  4096 Jun 24 14:21 user_data
drwxr-xr-x  5 bryan_ bryan_  4096 Jun 24 15:21 venv
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -l
total 204
-rw-r--r--  1 bryan_ bryan_  4080 Jun 24 14:21 Colab-TextGen-GPU.ipynb
-rw-r--r--  1 bryan_ bryan_ 34523 Jun 24 14:21 LICENSE
-rw-r--r--  1 bryan_ bryan_ 24673 Jun 24 14:21 README.md
-rwxr-xr-x  1 bryan_ bryan_   728 Jun 24 14:21 cmd_linux.sh
-rwxr-xr-x  1 bryan_ bryan_   699 Jun 24 14:21 cmd_macos.sh
-rwxr-xr-x  1 bryan_ bryan_   938 Jun 24 14:21 cmd_windows.bat
drwxr-xr-x  6 bryan_ bryan_  4096 Jun 24 14:21 css
drwxr-xr-x  7 bryan_ bryan_  4096 Jun 24 14:21 docker
drwxr-xr-x  2 bryan_ bryan_  4096 Jun 24 14:21 docs
-rw-r--r--  1 bryan_ bryan_ 18192 Jun 24 14:21 download-model.py
drwxr-xr-x 18 bryan_ bryan_  4096 Jun 24 14:21 extensions
drwxr-xr-x  5 bryan_ bryan_  4096 Jun 24 14:21 js
drwxr-xr-x  4 bryan_ bryan_  4096 Jun 24 15:19 modules
-rw-r--r--  1 bryan_ bryan_ 20322 Jun 24 14:21 one_click.py
drwxr-xr-x  3 bryan_ bryan_  4096 Jun 24 14:24 repositories
drwxr-xr-x  4 bryan_ bryan_  4096 Jun 24 14:21 requirements
-rw-r--r--  1 bryan_ bryan_ 12231 Jun 24 14:21 server.py
-rw-r--r--  1 bryan_ bryan_    61 Jun 24 14:21 setup.cfg
-rwxr-xr-x  1 bryan_ bryan_  2516 Jun 24 14:21 start_linux.sh
-rwxr-xr-x  1 bryan_ bryan_  2505 Jun 24 14:21 start_macos.sh
-rwxr-xr-x  1 bryan_ bryan_  4233 Jun 24 14:21 start_windows.bat
-rwxr-xr-x  1 bryan_ bryan_   889 Jun 24 14:21 update_wizard_linux.sh
-rwxr-xr-x  1 bryan_ bryan_   881 Jun 24 14:21 update_wizard_macos.sh
-rwxr-xr-x  1 bryan_ bryan_  1017 Jun 24 14:21 update_wizard_windows.bat
drwxr-xr-x  9 bryan_ bryan_  4096 Jun 24 14:21 user_data
drwxr-xr-x  5 bryan_ bryan_  4096 Jun 24 15:21 venv
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Aha! I see the issue now, and it's not that the requirements file is missing entirely, but that it's located in a subdirectory. Your ls -l output shows a directory named requirements/: drwxr-xr-x 4 bryan_ bryan_ 4096 Jun 24 14:21 requirements This means that the actual requirements files are inside that requirements/ folder, not directly in the text-generation-webui root directory. This is a common structure for projects with many modular dependencies. The main requirements file that includes core dependencies is usually named requirements_base.txt. Action: Install from the correct requirements file path While still in your activated virtual environment ((venv) should be visible in your prompt) and in the ~/text-generation-webui directory, run this command: pip install -r requirements/requirements_base.txt This will tell pip to look inside the requirements directory for the requirements_base.txt file and install all the listed dependencies. This will include gradio and many other essential packages. This will take some time to download and install. After that command completes successfully, try starting the server again: python3 server.py --listen --model-menu This should finally get your text-generation-webui up and running!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/tech/homelab|Homelab]]