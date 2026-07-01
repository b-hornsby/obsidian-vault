---
category: coding
date: 2025-09-07
id: 854159
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is confirming whether two specific Python libraries are the only dependencies
  needed before having Cursor scaffold the project.
tags:
- python-libraries
- cursor-scaffolding
- dependency-check
- crewai
- blender-api
---
# those two are the only libraries i need before i have cursor scaffold this?

### USER
those two are the only libraries i need before i have cursor scaffold this?

### GEMINI
For the initial scaffolding of the core AI agent and its ability to communicate with Blender, yes, crewai and bpy are the only two essential libraries you need right now. crewai will handle the orchestration of your agents and their tasks. bpy will allow your Python scripts to interact with Blender, acting as the bridge. As your project grows, you will likely need to install more libraries. For example: The Environment agent will likely need the requests library to make API calls to Skybox AI. The Assets agent might require a library to read or process different 3D file formats. But for your immediate task of generating the initial crew structure, you have everything you need.
