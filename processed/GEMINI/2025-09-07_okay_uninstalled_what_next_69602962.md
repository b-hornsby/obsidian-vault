---
category: coding
date: 2025-09-07
id: 101834
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: executing
source: GEMINI
summary: Bryan has uninstalled an old Python version and is asking what the next step
  should be.
tags:
- python-uninstall
- next-steps
- environment-setup
- cleanup
---
# okay uninstalled. what next? 

### USER
okay uninstalled. what next? 

### GEMINI
Start by installing the correct version of Python and creating a new virtual environment. Based on the Blender version you're using (4.5), the compatible Python version is 3.11. Your old environment was using Python 3.12, which caused the error. Step-by-Step Guide Install Python 3.11 Make sure you have a fresh installation of Python 3.11. You can download it directly from the official Python website. Create and Activate a New Virtual Environment Open your terminal in the blender ai agent project folder and run the following commands. This will create a new, clean virtual environment with the correct Python version. py -3.11 -m venv blender_ai_env_311 blender_ai_env_311\Scripts\activate Install the Necessary Libraries With the new environment active, install bpy (the Blender Python API) and crewai using the commands below. The first command will install the correct version of bpy that is compatible with your Blender 4.5. pip install bpy --extra-index-url https://download.blender.org/pypi/bpy/ pip install crewai Once these commands finish without errors, you will have successfully set up your development environment. You can then move on to writing the code for your agents. The next step will be to use the Cursor prompt we discussed earlier to generate the code for your director.py file.
