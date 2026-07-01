---
id: 073291
source: GEMINI
date: 2025-12-07
tags: ['wsl', 'ubuntu', 'fresh-install', 'windows-subsystem-linux']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan wanted to set up a fresh WSL/Ubuntu instance and needed guidance on the process.
---
# so now to get a fresh instance of wsl/ubuntu, what do i need to do? 

### USER
so now to get a fresh instance of wsl/ubuntu, what do i need to do? 

### GEMINI
You are pivoting directly to reinstallation—a clean start is an aggressive and strategic move. Given that you have already initiated the destruction of the old instance, getting a fresh installation is extremely simple. There are two effective methods to achieve a fresh Ubuntu instance on WSL, depending on whether you completely disabled the core WSL feature (Step 3 in the previous response). ⚡ Method 1: The Single, Automatic Command (Recommended) If you followed the full deletion plan and completely disabled the Windows features (WSL and Virtual Machine Platform), this command will re-enable everything and install the latest Ubuntu distribution in one shot. Open PowerShell or Command Prompt as an administrator. Run the single install command: wsl --install This command automatically enables the necessary Windows components (WSL and Virtual Machine Platform). It installs the latest Linux kernel. It downloads and installs the default Ubuntu distribution (usually the latest LTS version). You will be prompted to restart your computer. You must do this to complete the installation of the Windows components. After the reboot, the new Ubuntu terminal will automatically open, prompting you to create your new UNIX username and password. This is your fresh instance. ⚙️ Method 2: Install Only the Distribution (If WSL Core is Enabled) If you only ran wsl --unregister Ubuntu but did not disable the core Windows features, the core WSL platform is still active. In this case, you only need to install a new distribution. Open PowerShell or Command Prompt as an administrator. Run the command to install the latest Ubuntu LTS: wsl --install -d Ubuntu Note: You can use wsl --list --online to see all available distribution names (like Ubuntu-24.04, Debian, etc.) if you want a specific version or different distro. The system will download and install the new image, and the Ubuntu terminal will open to prompt for your new username and password. The key takeaway is that the days of complex, multi-step manual setup for WSL are over. You need only one command for a total fresh start. To see the available distributions you can install with the command line, check out this video. Windows 11, 10: Install WSL – The right way, avoiding errors (Command & GUI)


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
