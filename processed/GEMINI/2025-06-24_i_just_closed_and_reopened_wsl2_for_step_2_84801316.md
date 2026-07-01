---
id: 405206
source: GEMINI
date: 2025-06-24
tags: ['wsl2', 'restart', 'environment-reset']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was restarting WSL2 as part of a step in the setup process.
---
# i just closed and reopened wsl2 for step 2

### USER
i just closed and reopened wsl2 for step 2

### GEMINI
Okay, good. Closing and reopening WSL2 gives us a fresh start. Since you've re-opened WSL2, you're likely in your home directory (~). We need to get back into the text-generation-webui directory first, and then proceed with manually setting up llama.cpp. Let's pick up from the beginning of Step 36: Manually Clone and Build llama.cpp, assuming you are now in your home directory (~). Action (restarting from a fresh WSL session): Navigate back into your text-generation-webui directory: cd text-generation-webui Create the repositories directory if it doesn't exist: mkdir -p repositories Navigate into the repositories directory: cd repositories Clone the official llama.cpp repository into this directory: git clone https://github.com/ggerganov/llama.cpp.git This will create the llama.cpp directory inside repositories. Navigate into the newly cloned llama.cpp directory: cd llama.cpp Build llama.cpp with CUBLAS support (for GPU acceleration): make LLAMA_CUBLAS=1 This command will compile llama.cpp. This step might take a few minutes. Important: If make or g++ (a C++ compiler) is not found, you might need to install build-essential first: sudo apt update sudo apt install build-essential Then retry make LLAMA_CUBLAS=1. Please provide the full output of each of these commands as you execute them. This is a critical manual step to get llama.cpp working.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
