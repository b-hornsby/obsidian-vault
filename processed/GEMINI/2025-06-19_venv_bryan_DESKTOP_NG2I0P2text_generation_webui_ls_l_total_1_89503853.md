---
category: homelab
date: 2025-06-19
id: 214252
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- operation-immortal-agent
resolution: unresolved
sentiment: exploratory
source: GEMINI
summary: The user was exploring the directory structure of text-generation-webui in
  their home lab environment, likely setting up or investigating a local AI text generation
  deployment.
tags:
- text-generation-webui
- local-ai
- file-exploration
- linux-environment
- setup-investigation
---
# (venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -l
total 196
-rw-r--r--  1 bryan_ bryan_  4080 Jun 18 21:29 Colab-TextGen-GPU.ipynb
-rw-r--r--  1 bryan_ bryan_ 34523 Jun 18 21:29 LICENSE
-rw-r--r--  1 bryan_ bryan_ 23952 Jun 18 21:29 README.md
-rwxr-xr-x  1 bryan_ bryan_   728 Jun 18 21:29 cmd_linux.sh
-rwxr-xr-x  1 bryan_ bryan_   699 Jun 18 21:29 cmd_macos.sh
-rwxr-xr-x  1 bryan_ bryan_   938 Jun 18 21:29 cmd_windows.bat
drwxr-xr-x  6 bryan_ bryan_  4096 Jun 18 21:29 css
drwxr-xr-x  7 bryan_ bryan_  4096 Jun 18 21:29 docker
drwxr-xr-x  2 bryan_ bryan_  4096 Jun 18 21:29 docs
-rw-r--r--  1 bryan_ bryan_ 17776 Jun 18 21:29 download-model.py
drwxr-xr-x 18 bryan_ bryan_  4096 Jun 18 21:29 extensions
drwxr-xr-x  5 bryan_ bryan_  4096 Jun 18 21:29 js
drwxr-xr-x  3 bryan_ bryan_  4096 Jun 18 21:29 modules
-rw-r--r--  1 bryan_ bryan_ 20322 Jun 18 21:29 one_click.py
drwxr-xr-x  4 bryan_ bryan_  4096 Jun 18 21:29 requirements
-rw-r--r--  1 bryan_ bryan_ 12094 Jun 18 21:29 server.py
-rw-r--r--  1 bryan_ bryan_    61 Jun 18 21:29 setup.cfg
-rwxr-xr-x  1 bryan_ bryan_  2516 Jun 18 21:29 start_linux.sh
-rwxr-xr-x  1 bryan_ bryan_  2505 Jun 18 21:29 start_macos.sh
-rwxr-xr-x  1 bryan_ bryan_  4233 Jun 18 21:29 start_windows.bat
-rwxr-xr-x  1 bryan_ bryan_   889 Jun 18 21:29 update_wizard_linux.sh
-rwxr-xr-x  1 bryan_ bryan_   881 Jun 18 21:29 update_wizard_macos.sh
-rwxr-xr-x  1 bryan_ bryan_  1017 Jun 18 21:29 update_wizard_windows.bat
drwxr-xr-x 10 bryan_ bryan_  4096 Jun 18 21:29 user_data
drwxr-xr-x  5 bryan_ bryan_  4096 Jun 18 21:29 venv
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -l
total 196
-rw-r--r--  1 bryan_ bryan_  4080 Jun 18 21:29 Colab-TextGen-GPU.ipynb
-rw-r--r--  1 bryan_ bryan_ 34523 Jun 18 21:29 LICENSE
-rw-r--r--  1 bryan_ bryan_ 23952 Jun 18 21:29 README.md
-rwxr-xr-x  1 bryan_ bryan_   728 Jun 18 21:29 cmd_linux.sh
-rwxr-xr-x  1 bryan_ bryan_   699 Jun 18 21:29 cmd_macos.sh
-rwxr-xr-x  1 bryan_ bryan_   938 Jun 18 21:29 cmd_windows.bat
drwxr-xr-x  6 bryan_ bryan_  4096 Jun 18 21:29 css
drwxr-xr-x  7 bryan_ bryan_  4096 Jun 18 21:29 docker
drwxr-xr-x  2 bryan_ bryan_  4096 Jun 18 21:29 docs
-rw-r--r--  1 bryan_ bryan_ 17776 Jun 18 21:29 download-model.py
drwxr-xr-x 18 bryan_ bryan_  4096 Jun 18 21:29 extensions
drwxr-xr-x  5 bryan_ bryan_  4096 Jun 18 21:29 js
drwxr-xr-x  3 bryan_ bryan_  4096 Jun 18 21:29 modules
-rw-r--r--  1 bryan_ bryan_ 20322 Jun 18 21:29 one_click.py
drwxr-xr-x  4 bryan_ bryan_  4096 Jun 18 21:29 requirements
-rw-r--r--  1 bryan_ bryan_ 12094 Jun 18 21:29 server.py
-rw-r--r--  1 bryan_ bryan_    61 Jun 18 21:29 setup.cfg
-rwxr-xr-x  1 bryan_ bryan_  2516 Jun 18 21:29 start_linux.sh
-rwxr-xr-x  1 bryan_ bryan_  2505 Jun 18 21:29 start_macos.sh
-rwxr-xr-x  1 bryan_ bryan_  4233 Jun 18 21:29 start_windows.bat
-rwxr-xr-x  1 bryan_ bryan_   889 Jun 18 21:29 update_wizard_linux.sh
-rwxr-xr-x  1 bryan_ bryan_   881 Jun 18 21:29 update_wizard_macos.sh
-rwxr-xr-x  1 bryan_ bryan_  1017 Jun 18 21:29 update_wizard_windows.bat
drwxr-xr-x 10 bryan_ bryan_  4096 Jun 18 21:29 user_data
drwxr-xr-x  5 bryan_ bryan_  4096 Jun 18 21:29 venv
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Excellent! Thank you for providing the ls -l output. This changes everything and reveals the true problem. Looking at your ls -l output: drwxr-xr-x 4 bryan_ bryan_ 4096 Jun 18 21:29 requirements This line shows that requirements is not a file, but a directory! Inside that requirements directory, you will likely find requirements_linux.txt (and possibly requirements.txt or other platform-specific requirement files). The Solution: You need to tell pip to look inside the requirements directory for the requirements_linux.txt file. Try this command: pip install -r requirements/requirements_linux.txt Explanation: requirements/: This part tells the shell to look inside the requirements directory (which exists in your current directory). requirements_linux.txt: This is the name of the file you want pip to read. This should finally resolve the "No such file or directory" error! Let me know how it goes.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/homelab|Homelab]]