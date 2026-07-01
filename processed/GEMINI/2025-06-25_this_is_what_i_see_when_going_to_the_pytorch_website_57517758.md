---
id: 432093
source: GEMINI
date: 2025-06-25
tags: ['pytorch-install', 'cuda-compatibility', 'pytorch-website']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan was looking at the PyTorch website to determine the correct installation command for his CUDA setup.
---
# this is what i see when going to the pytorch website

### USER
this is what i see when going to the pytorch website

### GEMINI
Thanks for sharing the screenshot! That helps me understand what you're seeing. It looks like you've scrolled down a bit on the PyTorch page. The section we need is an interactive selector higher up on that same page. Please scroll up on the Pyotics website until you see a section that looks like this: It will have dropdown menus for: PyTorch Build: Your OS: Package: Compute Platform: Make sure you select these options in those dropdowns: PyTorch Build: Stable (2.3.1) (or whatever the latest stable version is, e.g., 2.4.0) Your OS: Linux Package: Pip Compute Platform: CUDA 12.1 (or the highest CUDA 12.x version available, as your nvidia-smi showed CUDA 12.9, which is compatible). Once you've selected those, the "Run this Command:" box below those selectors will show you the exact pip install command you need. Copy that entire command and paste it into your (llm-assist) Ubuntu terminal. Let me know when you've found the selector, run the command, and are ready for the verification step.
