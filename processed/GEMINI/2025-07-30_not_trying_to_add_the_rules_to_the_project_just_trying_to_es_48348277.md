---
category: coding
date: 2025-07-30
id: 152611
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan is clarifying that he's trying to establish rules for the local LLM
  in Continue.dev to create a cursor-like experience, not add rules to a specific
  project.
tags:
- continue.dev
- local-llm-customization
- cursor-experience
---
# not trying to add the rules to the project just trying to establish the rules for the local llm via continue.dev so that it is as close to a cursor experience 

### USER
not trying to add the rules to the project just trying to establish the rules for the local llm via continue.dev so that it is as close to a cursor experience 

### GEMINI
Got it, thanks for the clarification! This is an important distinction. You are absolutely correct: The rules are established for the local LLM (via Continue.dev's configuration), not added "to the project" in a way that affects your actual code. They are configuration for the AI assistant itself. When I mentioned: "Create these folders at the root of your VS Code workspace (your project folder): .continue/, .continue/rules/, .continue/prompts/" "File Name: 01-general-coding-standards.md Location: YOUR_PROJECT_ROOT/.continue/rules/" My intention was to guide you to place the rule files (.md files) in a specific location that Continue.dev automatically scans for its own configuration, which then dictates how the AI behaves. These files are part of the Continue.dev configuration, not part of your actual Python project's source code. They are typically placed in a hidden directory (.continue) so they don't clutter your project's main codebase. To be crystal clear: You do NOT paste these rules directly into your Python files. You do NOT modify your Python project's build system or code to include these rules. These .md files in .continue/rules/ are configuration files for Continue.dev itself, telling Continue.dev's AI how to behave and what guidelines to follow when it interacts with your code. So, when you create those .md files in the specified .continue/rules/ directory, and update your config.yaml to point to them (or embed them as YAML as in the last complete config.yaml example), you are indeed: Establishing rules for the local LLM (via Continue.dev). Making the Continue.dev experience as close to Cursor as possible. My apologies if the phrasing implied they were part of your project's source code. They are strictly configuration for the Continue.dev extension to guide the AI's behavior within your workspace.
