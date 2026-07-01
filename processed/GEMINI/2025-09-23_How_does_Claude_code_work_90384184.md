---
id: 048958
source: GEMINI
date: 2025-09-23
tags: ['claude-code', 'ai-coding-tools']
category: coding
sentiment: curious
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan was asking how Claude Code works as an AI coding tool.
---
# How does Claude code work? 

### USER
How does Claude code work? 

### GEMINI
Claude Code is an agentic coding assistant that uses Anthropic's large language models, like Sonnet 4 and Opus 4.1, to write and manage code. It works through a command-line interface (CLI) where you give it instructions in natural language. It then takes a series of steps to fulfill your request, acting as an AI "agent" that can perform actions and get feedback from its environment. How it Works Instruction & Context: You start by giving Claude Code a command in your terminal, such as "create a Python script that scrapes a website." It automatically gathers context from your project directory, including files like CLAUDE.md, which you can use to give it specific instructions, style guides, and other important information about the codebase. This context-gathering process is a key part of its functionality, allowing it to understand and interact with your specific project. Planning and Execution: After understanding the task, Claude Code forms a plan. It will often ask for permission before taking any action that could modify your system, like writing a file or running a bash command. This is a safety feature designed to prevent unwanted changes. It can execute bash commands and leverage various tools to perform its tasks. Iterative Process: Coding isn't a one-and-done process. Claude Code operates in an iterative loop. For example, if you ask it to write a feature, it might: Write the initial code. Run tests to check its work. Receive feedback from the tests (e.g., a test failed). Correct the code based on the feedback. Rerun the tests. This cycle continues until the code works correctly or until you provide new instructions. Advanced Features: Claude Code can handle complex tasks by breaking them down and even using multiple "subagents" to tackle different parts of a problem simultaneously. It can also manage version control systems like Git, writing commit messages and pushing changes to a repository. Key Features and Concepts 🤖 Agentic Coding: Instead of just generating a block of code, Claude Code acts as a coding agent that can observe, plan, and execute actions. It can navigate your codebase, run commands, and correct its own mistakes, much like a human developer would. CLAUDE.md: These are special markdown files that Claude Code automatically pulls into its context. You can use them to give it project-specific guidance, such as coding conventions, common commands, or a project's architecture. This is a powerful way to make the tool more effective for your specific workflow. Safety and Control: Claude Code is designed to be a power tool with a strong emphasis on safety. By default, it requests permission for most actions that modify your system, giving you control over what it does. Unopinionated Design: It doesn't force you into a specific workflow. This flexibility allows you to use it for various tasks, from generating new features and writing documentation to creating tests and performing code reviews.
