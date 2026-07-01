---
category: coding
date: 2025-06-23
id: 881673
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- operation-immortal-agent
- homelab-stack
resolution: unresolved
sentiment: exploratory
source: GEMINI
summary: The user was exploring the directory structure of the text-generation-webui
  project in their local environment, likely setting up or checking dependencies for
  a local LLM deployment as part of their homelab infrastructure.
tags:
- text-generation-webui
- llm-deployment
- file-system-exploration
- python-environment
- homelab
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -la requirements/
total 16
drwxr-xr-x  4 bryan_ bryan_ 4096 Jun 18 21:29 .
drwxr-xr-x 17 bryan_ bryan_ 4096 Jun 23 15:50 ..
drwxr-xr-x  2 bryan_ bryan_ 4096 Jun 22 18:00 full
drwxr-xr-x  2 bryan_ bryan_ 4096 Jun 22 18:00 portable
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -la requirements/
total 16
drwxr-xr-x  4 bryan_ bryan_ 4096 Jun 18 21:29 .
drwxr-xr-x 17 bryan_ bryan_ 4096 Jun 23 15:50 ..
drwxr-xr-x  2 bryan_ bryan_ 4096 Jun 22 18:00 full
drwxr-xr-x  2 bryan_ bryan_ 4096 Jun 22 18:00 portable
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Okay, this is very helpful! The ls -la requirements/ output shows that there isn't a requirements.txt file directly in the requirements folder. Instead, it contains two subdirectories: full/ and portable/. This indicates that Oobabooga has indeed changed how it structures its dependencies in recent versions, likely to offer different installation options. For a full-featured setup like yours, we'll typically want the "full" set of requirements. Now, let's look inside that full directory to find the actual requirements file. Please run this command: ls -la requirements/full/ Press Enter. This should show us the .txt file that contains the dependencies for the full Oobabooga experience.