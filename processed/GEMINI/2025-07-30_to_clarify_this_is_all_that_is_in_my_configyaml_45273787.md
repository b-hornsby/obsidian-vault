---
id: 248234
source: GEMINI
date: 2025-07-30
tags: ['continue.dev', 'yaml-configuration', 'local-llm-setup']
category: coding
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan is clarifying the contents of his config.yaml file.
---
# to clarify this is all that is in my config.yaml: 

### USER
to clarify this is all that is in my config.yaml: 

### GEMINI
To clarify based on the image you provided, your config.yaml currently contains: name: llama3.1 8b version: 1.0.1 schema: v1 models: - name: llama3.1 8b provider: ollama model: llama3.1:8b-instruct-q4_K_M roles: - chat - edit - apply - tool_use defaultCompletionOptions: contextLength: 8192 - name: qwen2.5-coder 1.5b provider: ollama model: qwen2.5-coder:1.5b roles: - autocomplete defaultCompletionOptions: contextLength: 4096 This config.yaml only defines your models. To achieve a Cursor-like experience, you need to add the contextProviders and customRules sections, and potentially customPrompts. Here is the complete config.yaml you should use, incorporating all the elements for a well-rounded, Cursor-like AI assistant, including the contextProviders and the customRules that reference the .md files you'll create. Your ~/.continue/config.yaml should look exactly like this (replace your current content with this): name: My Well-Rounded Local LLM Setup version: 1.0.1 schema: v1 # --- MODELS SECTION (as we finalized previously and matching your image) --- models: - name: llama3.1 8b provider: ollama model: llama3.1:8b-instruct-q4_K_M roles: - chat - edit - apply - tool_use defaultCompletionOptions: contextLength: 8192 # Optimal for performance on 8GB VRAM and good context - name: qwen2.5-coder 1.5b provider: ollama model: qwen2.5-coder:1.5b roles: - autocomplete - chat # Keep chat role for Qwen if you want to use it sometimes defaultCompletionOptions: contextLength: 4096 # Optimal for autocomplete speed and sufficient context # --- CORE SETTINGS FOR AI BEHAVIOR --- temperature: 0.2 # Lower temperature for more consistent, less creative code completionParams: maxTokens: 2048 # Max tokens for AI response, balance with contextLength # --- CONTEXT PROVIDERS (MAXIMUM AWARENESS) --- contextProviders: # Essential for project-wide awareness and code search - name: codebase params: # Crucial for performance: Exclude large, irrelevant directories exclude: - "**/node_modules" - "**/build" - "**/.venv" - "**/dist" - "**/__pycache__" - "**/.git" - "**/*.log" - "**/*.lock" - "**/coverage" # maxContextTokens: 4000 # Uncomment and adjust if performance still an issue with very large codebases # To include explicitly selected files via @file - name: file # To include current VS Code problems/diagnostics - name: problems # To include the last executed terminal command and its output - name: terminal # To provide a high-level map of your repository structure - name: repo-map params: includeSignatures: true # Include function/class signatures for better map context # Include content from currently open files - name: open-files # --- FEATURES (ENSURE THESE ARE ENABLED/CONFIGURED) --- enablePowerButtons: true # Adds buttons for common tasks in the sidebar allowAnonymousTelemetry: false # Recommended for privacy highlighting: query: true # Highlight parts of your code related to the AI's query response: true # Highlight parts of your code changed by AI's response # --- RULES (Defined by referencing the .md files you will create) --- customRules: - name: Universal Code Quality filepath: .continue/rules/01-universal-code-quality.md alwaysApply: true # This means these rules will always be active for every AI request description: "Core coding guidelines for readability, comments, and structure applicable to any language." - name: Robust Error Handling Principles filepath: .continue/rules/02-error-handling-principles.md alwaysApply: true description: "Principles for implementing robust and specific error handling across any language." - name: Comprehensive Testing Principles filepath: .continue/rules/03-comprehensive-testing-principles.md alwaysApply: true description: "Universal guidelines for writing effective unit and integration tests." - name: Python Specific Conventions filepath: .continue/rules/04-python-specific-conventions.md alwaysApply: true globs: "**/*.py" # This rule only applies when the active file is a Python file description: "Specific style and best practices for Python development (e.g., PEP8, type hinting)." - name: JavaScript & TypeScript Best Practices filepath: .continue/rules/05-js-ts-best-practices.md alwaysApply: true globs: "**/*.{js,jsx,ts,tsx}" # This rule only applies to JS/TS files description: "Specific guidelines for JavaScript and TypeScript development." # --- PROMPTS (Defined by referencing the .md files in .continue/prompts/) --- # Make sure these prompt files exist in YOUR_PROJECT_ROOT/.continue/prompts/ customPrompts: - name: Generate Tests filepath: .continue/prompts/generate-tests.md - name: Refactor Code filepath: .continue/prompts/refactor-code.md - name: Explain Code filepath: .continue/prompts/explain-code.md


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
