---
category: ai-tools
date: 2025-06-23
id: 417114
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- text-generation-webui
- homelab-stack
- private-ai-consulting
- second-brain-vault
- streaming-rig
- it-certification
- flappy-meme-bird
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user was trying to launch text-generation-webui with llama.cpp backend
  but encountered a 'python' command not found error, indicating a Python environment
  configuration issue on their homelab setup.
tags:
- text-generation-webui
- python-environment
- llama.cpp
- gpu-configuration
- command-not-found
---
# bryan_@DESKTOP-NG2I0P2:~$ cd text-generation-webui
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
Command 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
bryan_@DESKTOP-NG2I0P2:~$ cd text-generation-webui
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
Command 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Ah, excellent catch! This is a very common scenario in Linux environments. The error Command 'python' not found, did you mean: command 'python3' from deb python3 command 'python' from deb python-is-python3 means that your system doesn't have a direct python command set up, but it does have python3 (which is the modern, current version). Many Linux distributions, especially Ubuntu, explicitly distinguish between python (which historically often pointed to Python 2) and python3. The fix is simple: We just need to use python3 instead of python in our command. Step 3 (Continued): Launching Oobabooga with GPU Acceleration (Corrected Command) Action: We will rerun the previous command, simply replacing python with python3. What I need you to do now (in your Ubuntu WSL2 terminal): Rerun the launch command with python3: Command: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp Explanation of the change: python3: Explicitly calls the Python 3 interpreter. All other arguments remain the same and are crucial for pointing to your model and leveraging your GPU. What I need from you: Paste the corrected command above into your Ubuntu WSL2 terminal and press Enter. Crucially, copy and paste any and all output you see in the terminal after running this command. This output is vital for diagnosing the next steps. I'll be waiting for that output! This should get us much further along.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]