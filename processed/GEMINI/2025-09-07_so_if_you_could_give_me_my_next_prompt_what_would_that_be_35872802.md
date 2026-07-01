---
category: coding
date: 2025-09-07
id: 425607
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking for the next prompt to use in Cursor to continue scaffolding
  the Blender AI agent project.
tags:
- next-prompt
- cursor-ide
- vibe-coding
- development-guidance
---
# so if you could give me my next prompt, what would that be 

### USER
so if you could give me my next prompt, what would that be 

### GEMINI
Your next prompt would be for creating the core tool that allows your agents to communicate with Blender. This is the BlenderScriptRunner tool. This tool acts as the crucial bridge between your AI agent's "thoughts" and the actual actions performed inside Blender. It will take a Python script and execute it using Blender's command-line interface. The Cursor Prompt You'll need to use this prompt to generate the code for your blender_tools.py file. Prompt for Cursor: "Create a Python class named BlenderScriptRunner inside scripts/blender_tools.py. Import the subprocess module to run external commands. The class should have a run method that accepts a single argument: blender_script_path (the path to the Python script to be run inside Blender). Inside the run method, use subprocess.run() to call the Blender executable. Use the --background flag and the --python flag to execute the script in headless mode. The method should also accept an optional args parameter to pass additional arguments to the Blender script. Add a clear print statement to indicate when the script is being executed. Include a comment explaining what each part of the subprocess command does." This prompt will generate the most important piece of code for your project's functionality. Once you have this, you can move on to defining the other tools and refining your agent's tasks.
