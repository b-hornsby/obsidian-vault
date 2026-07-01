---
category: ai-tools
date: 2025-07-06
id: 992642
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is requesting instructions on how to complete a specific step (step
  4) in a process, indicating he's stuck or unsure how to proceed.
tags:
- local-llm
- troubleshooting
- step-by-step-guide
- technical-assistance
---
# can you show me how to do step 4 

### USER
can you show me how to do step 4 

### GEMINI
Certainly! Let's get that .wslconfig file set up for you. Step 4: Manually Configure DNS in WSL2 This step involves creating or editing a specific configuration file for WSL2 in your Windows user profile. This file tells WSL2 to consistently use a reliable DNS server, which should prevent the "Temporary failure in name resolution" errors. Here's how to do it: Close All WSL2 Terminals: Make sure no WSL2 windows are open. This is crucial for .wslconfig changes to take effect. Open PowerShell or Command Prompt as an Administrator: Click the Windows Start button. Type powershell or cmd. Right-click on "Windows PowerShell" or "Command Prompt" in the search results. Select "Run as administrator." Confirm any User Account Control prompts. Shut Down WSL2: In the Administrator PowerShell/Command Prompt window, run this command: wsl --shutdown This ensures WSL2 completely restarts and picks up the new configuration. Open Notepad (or any text editor) with Administrator Privileges: Click the Windows Start button. Type notepad. Right-click on "Notepad" in the search results. Select "Run as administrator." Confirm any User Account Control prompts. Navigate to Your User Profile Folder and Open/Create .wslconfig: In Notepad, go to File > Open... In the "File name:" box, type the exact path to your user profile folder, followed by .wslconfig. For example: C:\Users\YourUserName\.wslconfig Replace YourUserName with your actual Windows username. Important: By default, Notepad might only show .txt files. In the "File name:" box, type the full .wslconfig name including the dot, then press Enter or click "Open." If it asks if you want to create a new file, say Yes. Add/Edit Content in .wslconfig: Ensure the file contains only these lines: [wsl2] dns=8.8.8.8 This tells WSL2 to use Google's Public DNS (8.8.8.8) for all name resolution. Save the file: Go to File > Save. Make sure it's saved as .wslconfig in your C:\Users\YourUserName\ directory. Close Notepad and the Administrator PowerShell/Command Prompt. Restart WSL2: Just open a new WSL2 terminal (e.g., by searching for "Ubuntu" or "WSL"). Verify DNS in WSL2 (Optional, but Recommended): In your new WSL2 terminal, run: cat /etc/resolv.conf The output should show nameserver 8.8.8.8 (or something very similar) near the top. This confirms your .wslconfig change is working. Now, try running Oobabooga again. With the consistent DNS setting, superboogav2 should be able to reach Hugging Face Hub, download its embedding model, and then function as expected.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
