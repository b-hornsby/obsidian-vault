---
category: ai-tools
date: 2025-07-29
id: 669712
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is reporting problems that appeared after installing the continue.dev
  extension in VS Code.
tags:
- continue.dev
- vs-code
- installation-errors
---
# now when i installed that these problems popped up? 

### USER
now when i installed that these problems popped up? 

### GEMINI
You've hit on a new, important piece of information! The "Problems" tab showing errors related to your config.yaml (like Missing property "name", Missing property "title", and Property 'title' is not allowed) indicates that the newly installed Red Hat YAML extension is trying to validate your config.yaml against a schema that doesn't match what continue.dev expects. This is a conflict in schema validation, not an error in your config.yaml itself (which we previously confirmed looked correct for continue.dev). The YAML extension is trying to be helpful but is applying the wrong rules for this specific file. While these errors aren't directly from continue.dev, it's possible they are confusing VS Code's internal file parsing or indirectly preventing continue.dev from loading its configuration correctly. Let's temporarily remove this new variable from the equation: Temporarily Disable the Red Hat YAML Extension: Go to the Extensions view in VS Code (Ctrl + Shift + X). In the search bar, type YAML. Find the "YAML Language Support by Red Hat" extension. Click the "Disable" button for this extension. (You can re-enable it later if needed for other YAML files). Reload VS Code: Open the Command Palette (Ctrl + Shift + P or Cmd + Shift + P). Type Reload Window and select "Developer: Reload Window". Confirm Ollama Server is Running: Make sure your PowerShell window with ollama serve is still open and the server is running without any "bind" errors. Check the VS Code Output Tab again: Go to View -> Output. Click the dropdown. Look for "Continue" again. If it appears, select it and check its logs for any messages about loading config.yaml or connecting to Ollama. Check the continue.dev Sidebar: Go to the continue.dev sidebar (the AI icon). See if your "Llama 3.1 8B Local (Ollama)" model now appears in the "Select model" dropdown. By disabling the YAML extension, we are hoping to allow continue.dev to process its config.yaml without interference from external schema validation. If this works, then we know the YAML extension was indeed causing a conflict.
