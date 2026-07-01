---
id: 487814
source: GEMINI
date: 2025-06-24
tags: ['wsl2-setup', 'environment-separation', 'project-planning']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was trying to figure out the best plan of attack for keeping his WSL2 environment separate from his Windows setup.
---
# Well, if I'm trying to keep it separate from my window stuff, that's probably the the best way to go about it, but I just didn't know uh kind of like moving forward like what the best plan of attack is.

### USER
Well, if I'm trying to keep it separate from my window stuff, that's probably the the best way to go about it, but I just didn't know uh kind of like moving forward like what the best plan of attack is.

### GEMINI
Okay, so you want to keep your Oobabooga setup separate from your Windows environment. That's a smart move for organization and avoiding potential conflicts. Since you're using WSL2, the best approach is to treat it like a regular Linux installation. This means cloning the repository from GitHub directly into your WSL2 file system. Here's a general plan of attack: Open your WSL2 terminal: This is where you'll be working. Navigate to your desired directory: Use the cd command to move to the folder where you want to install Oobabooga. For example, cd ~ will take you to your home directory. Clone the repository: Use the git clone command to download the Oobabooga files. You'll find the exact command on the Oobabooga GitHub page. Navigate into the Oobabooga directory: Use cd again to enter the newly created folder. Run the installation script: Oobabooga has a script that automates most of the setup. You'll need to run this from your terminal. The exact command is usually something like ./start_linux.sh or ./install.sh. Follow the instructions: The script will guide you through the remaining steps, like installing dependencies and configuring any settings. This process might seem a bit more involved than the one-click installer, but it's the standard way to install Oobabooga on Linux and WSL2. It gives you more control over the installation and makes it easier to update in the future.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
