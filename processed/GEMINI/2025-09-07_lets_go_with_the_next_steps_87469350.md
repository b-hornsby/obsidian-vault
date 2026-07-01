---
category: coding
date: 2025-09-07
id: 644704
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan is requesting guidance on the next steps to take in his project.
tags:
- workflow-guidance
- ai-assisted-development
---
# lets go with the next steps 

### USER
lets go with the next steps 

### GEMINI
Sounds good. Now that your old environment is gone, we can create the new one and get the libraries installed. 1. Create and Activate the New Virtual Environment Open your terminal in the blender ai agent project folder and create a new virtual environment using the Python 3.11.9 version you just installed. py -3.11 -m venv blender_ai_env_311 blender_ai_env_311\Scripts\activate 2. Install the Required Libraries With the new environment active, install the bpy (Blender Python API) and crewai libraries. The bpy package will now install correctly because you're using a compatible Python version. pip install bpy --extra-index-url https://download.blender.org/pypi/bpy/ pip install crewai Once these commands finish without errors, your development environment will be fully set up. We can then use the Cursor prompt we discussed earlier to generate the code for your director.py file.
