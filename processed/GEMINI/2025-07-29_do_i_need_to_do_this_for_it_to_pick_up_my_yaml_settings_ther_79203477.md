---
category: ai-tools
date: 2025-07-29
id: 543969
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is trying to figure out if he needs to take specific steps to make
  VS Code recognize his YAML settings for the Continue.dev extension.
tags:
- vscode-intellisense
- yaml-configuration
- continue-dev-setup
- local-llm-integration
---
# do i need to do this for it to pick up my yaml settings? there was an option to download the YAML ext for intellisense?

### USER
do i need to do this for it to pick up my yaml settings? there was an option to download the YAML ext for intellisense?

### GEMINI
Yes, that's a very good observation and question! The prompt to "Download XML extension for Intellisense" and then specifically showing the "Do you trust the publisher 'Red Hat'?" dialog for a YAML extension is relevant. While the YAML extension itself (published by Red Hat) isn't strictly required for continue.dev to read your config.yaml, it's an important diagnostic clue and potentially a missing dependency for VS Code's internal YAML parsing. Here's why it's important: YAML Parsing: continue.dev relies on VS Code's environment to correctly parse the config.yaml file. If the underlying YAML parser that VS Code uses is encountering issues (or is not fully installed/trusted), it could prevent continue.dev from successfully reading its configuration. Publisher Trust: The "Do you trust the publisher 'Red Hat'?" dialog is a security measure. If you don't "Trust Publisher & Install", then VS Code might not fully activate or integrate extensions from that publisher, even if they're nominally installed. It's possible this is indirectly affecting how continue.dev interacts with the YAML file. IntelliSense: While Intellisense (code completion, syntax highlighting, validation) is a user convenience, the fact that VS Code is prompting for a YAML extension specifically for Intellisense indicates that it's dealing with a YAML file and might be missing core components for it. Therefore, yes, you should absolutely "Trust Publisher & install" the Red Hat YAML extension. Here's the plan: Click "Trust Publisher & install" in that dialog box. This will install the YAML extension. Reload VS Code. (It might prompt you, or do it manually via Command Palette: Ctrl+Shift+P -> "Developer: Reload Window"). Confirm ollama serve is still running in your PowerShell window. (It needs to be continuously running). Check the VS Code Output tab again: Go to View -> Output. Click the dropdown. Look for "Continue" again. If it appears, select it and check the logs. Check the continue.dev sidebar (the AI icon): Does your "Llama 3.1 8B Local (Ollama)" model now appear in the "Select model" dropdown? It's possible that this missing YAML extension, or the publisher trust issue, was a subtle underlying problem preventing continue.dev from properly parsing its configuration file during startup. This is a very promising lead.
