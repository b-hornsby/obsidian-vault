---
id: 566981
source: GEMINI
date: 2025-09-07
tags: ['cursor-ide', 'prompt-engineering', 'ai-assisted-coding']
category: coding
sentiment: executing
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan is stating that he is using Cursor IDE for all of his coding and is working from a prompt.
---
# i said a prompt. i'm doing ALL coding in cursor 

### USER
i said a prompt. i'm doing ALL coding in cursor 

### GEMINI
My apologies. You are absolutely right. I should be providing the prompts for Cursor, not the code itself. My previous response was off-track. Let's get back on track. Here is the correct prompt to generate the Delegation Tool. Prompt for Cursor: "Create a Python class named DelegationTool inside scripts/blender_tools.py. Import the Tool class from crewai. The tool's name should be 'Delegation Tool' and its description should be 'Useful for analyzing a user's high-level request and breaking it down into a detailed list of sub-tasks for the other agents in the crew.' The class should have a _run method that takes a high_level_prompt as a string argument. Inside the _run method, generate a structured, sequential list of tasks for the other agents. The list should be formatted clearly and should be based on the high_level_prompt. The method should return this structured task list as a string. Add clear comments explaining what the class and its methods do." This prompt will create the tool your Director agent needs to break down a project into a clear plan. Once you have this code generated, let me know, and we can move on to the next tool.
