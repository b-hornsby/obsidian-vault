---
category: ai-tools
date: 2025-09-07
id: 647492
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wants to create a prompt for Cursor to implement a Local 3D Library
  API for his Asset Agent, which will find and load 3D models and textures from his
  local library.
tags:
- ai-agent-pipeline
- 3d-asset-management
- local-library-api
- cursor-prompt
---
# new tool same idea: Local 3D Library API (for the Asset Agent): This tool will be your bridge to your assets/ folder. Its purpose is to find and load the correct 3D models and textures from your local library so they can be prepared for the scene.

### USER
new tool same idea: Local 3D Library API (for the Asset Agent): This tool will be your bridge to your assets/ folder. Its purpose is to find and load the correct 3D models and textures from your local library so they can be prepared for the scene.

### GEMINI
The next tool on your list is the Local 3D Library API, which is your bridge to your assets/ folder. Think of this tool as a digital librarian for your 3D models and textures. Here is the prompt for Cursor to create the code for this tool. Prompt for Cursor "Create a Python class named Local3DLibraryTool inside the scripts/blender_tools.py file. Import the os and glob modules. The class should have a name of 'Local 3D Library' and a description that explains its purpose: 'Useful for searching the local file system for 3D models or texture files.' The class should have a run method that takes a string argument named asset_name. The run method should search your local assets/ directory for any file that matches the asset_name using glob. If a file is found, the method should return the full path to that file. If no matching file is found, it should return a clear error message like 'Asset not found.' Add comments throughout the code to explain what each part does."
