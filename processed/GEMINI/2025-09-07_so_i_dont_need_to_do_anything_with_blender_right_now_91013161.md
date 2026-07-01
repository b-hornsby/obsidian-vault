---
category: coding
date: 2025-09-07
id: 992172
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is confirming whether Blender itself needs to be configured at this
  stage or if the work is purely on the AI agent pipeline.
tags:
- blender-setup
- development-phases
- project-planning
---
# so i dont need to do anything with blender right now? 

### USER
so i dont need to do anything with blender right now? 

### GEMINI
That's correct. You don't need to be in the Blender GUI for now. Your immediate task is to write the Python code that will allow your AI agents to control Blender. The communication bridge we discussed—using the command line to execute scripts—means your agents will operate from your external Python environment. The actual Blender work will happen automatically in the background when your agents run the subprocess commands you write. The next step is to build the director.py file, which will serve as the entry point for your entire crew. It will be responsible for defining your agents and their tasks based on the context_profile.json file we've been working on.
