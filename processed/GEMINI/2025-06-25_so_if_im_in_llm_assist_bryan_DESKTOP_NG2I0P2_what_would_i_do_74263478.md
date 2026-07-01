---
id: 698331
source: GEMINI
date: 2025-06-25
tags: ['coding', 'llm', 'ai', 'gemini', 'grok', 'oobabooga', 'rag', 'text-generation']
category: coding
sentiment: building
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md']
---
# so if i'm in: (llm-assist) bryan_@DESKTOP-NG2I0P2:~$ what would i do to get oobabooga officially up and running? 

### USER
so if i'm in: (llm-assist) bryan_@DESKTOP-NG2I0P2:~$ what would i do to get oobabooga officially up and running? 

### GEMINI
Here's exactly what you would do, step-by-step, from your current prompt (llm-assist) bryan_@DESKTOP-NG2I0P2:~$ to get Oobabooga's text-generation-webui officially up and running using its recommended "one-click" method: Goal: Install Oobabooga into its own separate Conda environment, leaving your llm-assist environment as is. Exit the llm-assist Conda environment. It's best practice to deactivate your current environment before letting Oobabooga's script create its own. conda deactivate Your prompt should change from (llm-assist) to (base) or just bryan_@DESKTOP-NG2I0P2:~$. Navigate to your desired installation directory. This is where the text-generation-webui folder will be created. Your home directory (~) is a common and usually good choice. cd ~ (You are likely already in your home directory, but cd ~ ensures it.) Clone the text-generation-webui repository. This downloads all the necessary files for Oobabooga. git clone https://github.com/oobabooga/text-generation-webui.git Change into the newly created directory. cd text-generation-webui Run the start_linux.sh script. This is the "one-click installer" part. It will automatically set up the Conda environment, install dependencies, and then launch the web UI. ./start_linux.sh What to expect after running ./start_linux.sh: Initial Setup (Longest Part): The script will first check for Conda, then create a new Conda environment (usually named textgen). It will then download and install a large number of packages, including: PyTorch (configured for your CUDA 12.x setup). llama-cpp-python (it will compile its own version of this, leveraging your system's CUDA Toolkit and the PyTorch it just installed). Various other Python libraries required by Oobabooga. Potentially some system tools like ffmpeg. This step can take anywhere from 15 minutes to an hour or more, depending on your internet speed and system resources, as it's downloading multiple gigabytes of data and compiling code. Progress Messages: You will see a lot of text scrolling by, indicating package downloads, installations, and compilation steps. Success Message: If successful, it will eventually print messages indicating that the web UI is running and provide you with a URL, typically something like: Running on local URL: http://127.0.0.1:7860 It might also show a public URL if you have ngrok set up, but the local one is what you need. Opening the UI: Copy and paste the http://127.0.0.1:7860 URL into your Windows web browser (not your WSL2 terminal browser). Key point to remember: This process is designed to be self-contained and should avoid conflicts with your llm-assist environment because it sets up its own dedicated environment. Good luck! This is the standard and most reliable way to get Oobabooga running.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]