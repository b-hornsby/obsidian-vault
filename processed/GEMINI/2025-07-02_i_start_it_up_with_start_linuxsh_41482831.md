---
id: 194574
source: GEMINI
date: 2025-07-02
tags: ['text-generation-webui', 'oobabooga', 'local-llm']
category: ai-tools
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan confirms he's using the start_linux.sh script to launch Oobabooga.
---
# i start it up with: ./start_linux.sh 

### USER
i start it up with: ./start_linux.sh 

### GEMINI
No problem at all, thanks for clarifying! Using ./start_linux.sh is a common way to run Oobabooga. To enable the --api flag when using the start_linux.sh script, you have two primary options: Option 1: Edit the CMD_FLAGS.txt file (Recommended for persistent flags) Oobabooga provides a special file where you can put command-line flags that you want to be applied every time you run the start_linux.sh script. This is generally the cleanest way to do it. Open your Ubuntu WSL window. Navigate to your text-generation-webui directory. cd text-generation-webui (Make sure you are in the main text-generation-webui folder, where start_linux.sh is located.) Open the CMD_FLAGS.txt file for editing. We'll use a simple text editor called nano, which is usually pre-installed in Ubuntu. nano CMD_FLAGS.txt If CMD_FLAGS.txt doesn't exist, that's okay! nano will create it for you when you save. Inside the nano editor, you'll see a blank file or possibly some commented-out examples (lines starting with #). Add --api on a new line. If there are existing flags you want to keep, make sure --api is on its own line or separated by spaces. For example, if the file is empty, just type: --api If it has other flags, ensure --api is added: --listen --api --some-other-flag (You might see --listen already there, which means it listens for connections from other computers on your network, which can be useful later, but --api is what we strictly need for RAG integration). Save and Exit nano: Press Ctrl + X (control key and 'x' key at the same time). It will ask if you want to "Save modified buffer?" Type Y for Yes, then press Enter. It will then ask for the "File Name to Write:" Just press Enter to confirm CMD_FLAGS.txt. Now, start Oobabooga as you normally would: ./start_linux.sh Look for the API message: As Oobabooga starts up, you should see output indicating that the API is active, something like: API listening on: http://127.0.0.1:5000/ Option 2: Pass the flag directly when starting (Temporary or for quick tests) You can also pass flags directly to the script, which is useful if you only want the API enabled for a single session and don't want to modify CMD_FLAGS.txt. Open your Ubuntu WSL window. Navigate to your text-generation-webui directory. cd text-generation-webui Run the script with the --api flag: ./start_linux.sh --api Look for the API message: Again, watch the output for the line indicating the API is listening. Please perform Option 1 (editing CMD_FLAGS.txt) as it's the more robust approach for our project. Once you've done that, start Oobabooga with ./start_linux.sh and paste the line that shows the API listening address and port (e.g., API listening on: http://127.0.0.1:5000/). If you encounter any errors or don't see the API listening message, please paste the relevant output.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
