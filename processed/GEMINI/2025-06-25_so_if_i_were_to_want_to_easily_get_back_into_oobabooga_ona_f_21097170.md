---
id: 251016
source: GEMINI
date: 2025-06-25
tags: ['oobabooga', 'startup-script', 'wsl2-shortcut', 'persistent-access']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
summary: Bryan wanted to know how to easily relaunch oobabooga after a fresh WSL2 boot without going through the full setup process again.
---
# so if i were to want to easily get back into oobabooga ona  fresh bootup, what would i do? 

### USER
so if i were to want to easily get back into oobabooga ona  fresh bootup, what would i do? 

### GEMINI
To easily get back into Oobabooga on a fresh bootup of your Windows machine (and thus WSL2), you would follow these steps: Open your WSL2 terminal. You can do this by searching for "Ubuntu" (or whatever your WSL2 distribution is named) in the Windows Start Menu and opening the application. Navigate to the text-generation-webui directory. This is the folder where you cloned Oobabooga's repository. If you followed the previous instructions, it should be in your home directory: cd ~/text-generation-webui Run the start_linux.sh script. This script will activate Oobabooga's dedicated Conda environment, ensure all its dependencies are up-to-date, and then launch the web UI. ./start_linux.sh Wait for the "Running on local URL" message. In the WSL2 terminal, you'll see output indicating that the server is starting and then it will display the URL, typically http://127.0.0.1:7860. Open your web browser on your Windows machine and go to the displayed URL (http://127.0.0.1:7860). That's it! This sequence of commands will consistently get you back into the Oobabooga web UI, ready to load models and interact with them.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
