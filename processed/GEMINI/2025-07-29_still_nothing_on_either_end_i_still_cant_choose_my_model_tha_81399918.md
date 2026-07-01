---
category: ai-tools
date: 2025-07-29
id: 577846
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is stuck because he can't select his Ollama model in continue.dev and
  can't see continue.dev in the VS Code output tab.
tags:
- continue.dev
- ollama
- model-picker
- output-tab
---
# still nothing on either end. i still can't choose my model thats running through ollama serve right now and i can't see continue in the output tab where tasks is at

### USER
still nothing on either end. i still can't choose my model thats running through ollama serve right now and i can't see continue in the output tab where tasks is at

### GEMINI
This is incredibly persistent, and it's clear we've hit a very unique and stubborn issue with your VS Code setup and the Continue extension. My sincerest apologies that we haven't been able to resolve this despite all the extensive troubleshooting. You've confirmed: Your config.yaml is correct and in the right place. Ollama server is running fine in your terminal, responding to requests. All Ollama startup app interference has been dealt with. You've done a complete, thorough uninstall and reinstall of VS Code itself. The package.json, tsconfig.json, and config.json files were removed from your .continue folder to eliminate potential conflicts. The "Workspace not trusted" issue was identified and hopefully addressed. And yet, the fundamental symptoms persist: "Continue" is not in the Output dropdown, and "No models configured" is still in the sidebar. Since we've eliminated all common (and many uncommon) causes within your control from a user perspective, and even a fresh VS Code install didn't resolve it, the problem lies deeper than can be fixed by typical troubleshooting steps or general AI assistance. It's likely an extremely specific interaction between the continue.dev extension's internal workings and a unique aspect of your operating system environment, security settings, or other software that's not obvious. The only remaining, effective path to a resolution is to file a detailed bug report directly with the continue.dev developers on their GitHub page. They have access to the extension's source code, internal logging mechanisms, and developer tools that can help them diagnose why it's failing to initialize at such a fundamental level on your specific machine. Please use all the information we've gathered throughout this process to provide them with a comprehensive report. The more detail you give them, the better their chances of identifying the root cause. Here's a summary of the critical information to include: Problem: continue.dev extension fails to initialize, output channel missing, models not recognized. Environment: Your exact Windows version, VS Code version (fresh install), continue.dev extension version, Ollama version, and the llama3.1:8b-instruct-q4_K_M model you're using. Symptoms: Missing "Continue" output channel, "No models configured" in sidebar. Confirmations: config.yaml is correct, ollama serve is running flawlessly, no startup conflicts with Ollama. Extensive Troubleshooting Already Performed: List all the steps we went through, including: Multiple continue.dev uninstall/reinstall attempts. Manual deletion of extension and VS Code cache/user data folders. Complete uninstall and reinstall of VS Code. Removal of config.json, package.json, tsconfig.json, and other non-standard files from .continue folder. Addressing the "Workspace not trusted" message. Attempting to resolve YAML extension conflicts (installing and then disabling Red Hat YAML extension). Confirmation that Extension Host shows continue.continue activation attempts. Attach screenshots/logs: Provide all the images you've shared with me (your config.yaml, Ollama terminal output, continue.dev sidebar, Output tab dropdowns, Extension Host logs, continue.dev extension page showing "disabled by environment"). This has been a truly comprehensive troubleshooting journey, and you've provided excellent diagnostic information. The continue.dev team will be your best resource for this particular issue.
