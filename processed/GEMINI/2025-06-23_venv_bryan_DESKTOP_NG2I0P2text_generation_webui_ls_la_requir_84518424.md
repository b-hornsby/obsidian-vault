---
category: homelab
date: 2025-06-23
id: 518974
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: exploratory
source: GEMINI
summary: The user is exploring the dependency structure of text-generation-webui,
  likely trying to understand or set up the project requirements for their local environment.
tags:
- text-generation-webui
- local-ai
- requirements
- dependency-management
- linux-setup
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -la requirements/full/
total 52
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 22 18:00 .
drwxr-xr-x 4 bryan_ bryan_ 4096 Jun 18 21:29 ..
-rw-r--r-- 1 bryan_ bryan_ 2282 Jun 22 18:00 requirements.txt
-rw-r--r-- 1 bryan_ bryan_ 1169 Jun 22 18:00 requirements_amd.txt
-rw-r--r-- 1 bryan_ bryan_ 1175 Jun 22 18:00 requirements_amd_noavx2.txt
-rw-r--r-- 1 bryan_ bryan_ 1136 Jun 22 18:00 requirements_apple_intel.txt
-rw-r--r-- 1 bryan_ bryan_ 1388 Jun 22 18:00 requirements_apple_silicon.txt
-rw-r--r-- 1 bryan_ bryan_  858 Jun 22 18:00 requirements_cpu_only.txt
-rw-r--r-- 1 bryan_ bryan_  859 Jun 22 18:00 requirements_cpu_only_noavx2.txt
-rw-r--r-- 1 bryan_ bryan_ 2292 Jun 22 18:00 requirements_cuda128.txt
-rw-r--r-- 1 bryan_ bryan_ 2298 Jun 22 18:00 requirements_cuda128_noavx2.txt
-rw-r--r-- 1 bryan_ bryan_ 2288 Jun 22 18:00 requirements_noavx2.txt
-rw-r--r-- 1 bryan_ bryan_  414 Jun 22 18:00 requirements_nowheels.txt

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -la requirements/full/
total 52
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 22 18:00 .
drwxr-xr-x 4 bryan_ bryan_ 4096 Jun 18 21:29 ..
-rw-r--r-- 1 bryan_ bryan_ 2282 Jun 22 18:00 requirements.txt
-rw-r--r-- 1 bryan_ bryan_ 1169 Jun 22 18:00 requirements_amd.txt
-rw-r--r-- 1 bryan_ bryan_ 1175 Jun 22 18:00 requirements_amd_noavx2.txt
-rw-r--r-- 1 bryan_ bryan_ 1136 Jun 22 18:00 requirements_apple_intel.txt
-rw-r--r-- 1 bryan_ bryan_ 1388 Jun 22 18:00 requirements_apple_silicon.txt
-rw-r--r-- 1 bryan_ bryan_  858 Jun 22 18:00 requirements_cpu_only.txt
-rw-r--r-- 1 bryan_ bryan_  859 Jun 22 18:00 requirements_cpu_only_noavx2.txt
-rw-r--r-- 1 bryan_ bryan_ 2292 Jun 22 18:00 requirements_cuda128.txt
-rw-r--r-- 1 bryan_ bryan_ 2298 Jun 22 18:00 requirements_cuda128_noavx2.txt
-rw-r--r-- 1 bryan_ bryan_ 2288 Jun 22 18:00 requirements_noavx2.txt
-rw-r--r-- 1 bryan_ bryan_  414 Jun 22 18:00 requirements_nowheels.txt

### GEMINI
Excellent! We found it! The output of ls -la requirements/full/ clearly shows: -rw-r--r-- 1 bryan_ bryan_ 2282 Jun 22 18:00 requirements.txt This means the main requirements.txt file is indeed inside the requirements/full/ directory. Now, we can finally tell pip the correct path to update all the necessary Python libraries for your Oobabooga setup. Here's the final command to update your dependencies: Ensure Oobabooga is still stopped (if it's running, press Ctrl + C in the terminal). Run the pip install command with the correct path: pip install -r requirements/full/requirements.txt --upgrade Press Enter. This command will now correctly find the requirements.txt file and proceed with installing or upgrading all the necessary Python packages. This might take several minutes as it downloads and installs libraries, so please be patient. Once that command finishes and you see your prompt (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ return, you can then restart Oobabooga using your manual command: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp Press Enter. After Oobabooga fully loads in your browser, go back to the "Settings" tab (or look for a new "Extensions" tab on the left if it appears). You should now see the dedicated RAG extensions (like rag_agent or document_loader) in the "Available extensions" list, and we can proceed with setting up RAG!