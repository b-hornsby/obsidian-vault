---
category: coding
date: 2025-09-23
id: 262444
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- private-ai-consulting
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was trying to undo or uninstall changes made in Windsurf.
tags:
- windsurf
- undo-changes
- ide-cleanup
- project-reset
---
# so how do i uninstall what i did in windsurf? 

### USER
so how do i uninstall what i did in windsurf? 

### GEMINI
Even though the installation likely failed or was non-functional, the pip command did run and may have left behind a partial installation on your Windows system. The good news is that you can remove it using the same tool you used to install it. How to Uninstall vLLM in Windows To remove what you've installed, follow these steps in your Windows terminal (PowerShell or Command Prompt). Open your terminal. Run the uninstall command: This command will search for the vllm package and its dependencies and prompt you to confirm their removal. pip uninstall vllm Confirm the removal: If prompted, type Y and press Enter to confirm that you want to uninstall the listed files. This process should clean up the non-functional installation. You can also run the command with the -y flag to automatically confirm all prompts and save time: pip uninstall vllm -y This process will not affect the core Python installation on your machine. You will be able to proceed with the correct setup using WSL2. The video provided below offers a visual guide on how to uninstall Python packages from a Windows environment using the pip uninstall command. How to Uninstall Multiple Python Packages Using PIP (2024)


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
