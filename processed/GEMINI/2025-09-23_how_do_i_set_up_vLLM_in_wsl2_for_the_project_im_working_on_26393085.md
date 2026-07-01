---
category: ai-tools
date: 2025-09-23
id: 935329
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking for instructions on how to set up vLLM within WSL2 for his
  current project.
tags:
- vllm
- wsl2
- local-llm-deployment
- development-environment
---
# how do i set up vLLM in wsl2 for the project i'm working on? 

### USER
how do i set up vLLM in wsl2 for the project i'm working on? 

### GEMINI
Setting up vLLM in WSL2 involves a few key steps to ensure compatibility between Windows, the Linux environment, and your NVIDIA GPU. Here's a concise guide: 💻 1. Prerequisites and Environment Setup First, ensure you have the necessary components installed and configured correctly: WSL2: You must be using WSL2, as it provides a full Linux kernel and GPU passthrough capabilities, which are essential for vLLM. WSL1 does not support this. NVIDIA Drivers: Install the NVIDIA GPU drivers for Windows. These drivers are designed to work with WSL2 and enable your Linux environment to access the GPU. You can download them directly from the NVIDIA website. CUDA Toolkit (in WSL2): Inside your WSL2 Ubuntu environment, you need to install the CUDA Toolkit for WSL. Be careful not to overwrite your Windows drivers with the Linux CUDA package. The CUDA Toolkit for WSL is specifically designed to work with your Windows NVIDIA drivers. You can verify the installation by running nvcc --version inside your WSL terminal. Python and Conda: It is highly recommended to use a virtual environment, such as a Conda environment, to manage your dependencies. This helps prevent conflicts with other Python projects. Create a new environment with a compatible Python version (3.8-3.12). 2. Installing vLLM Once your environment is set up, you can install vLLM. The most straightforward method is using pip. Conda: If you're using Conda, create and activate an environment: conda create -n myenv python=3.10 -y conda activate myenv Installation: Install vLLM using pip. The vLLM binaries are typically compiled with a specific CUDA version (e.g., CUDA 12.1 or 12.6), and you should ensure it matches your setup. pip install vllm Building from source (if necessary): If you run into compatibility issues or need a specific configuration, you may have to build vLLM from source. This process can take a significant amount of time as it compiles CUDA kernels. 3. Running a vLLM Server After installation, you can run an OpenAI-compatible API server to use vLLM for inference. Start the server: Run the following command, replacing MODELTORUN with the Hugging Face model you want to use. vllm serve --model MODELTORUN Additional flags: You can add flags to configure the server, such as specifying the host and port (--host and --port) or using a specific data type (--dtype). How-to Install vLLM and Serve AI Models Locally This video is a comprehensive guide to installing vLLM and running AI models locally, which is directly relevant to setting up vLLM in a WSL2 environment.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
