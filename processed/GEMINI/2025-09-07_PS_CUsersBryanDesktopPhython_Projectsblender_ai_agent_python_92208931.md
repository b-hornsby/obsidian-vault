---
id: 906711
source: GEMINI
date: 2025-09-07
tags: ['coding', 'ai', 'agent', 'gemini', 'short', 'python', 'script', 'package']
category: coding
sentiment: building
resolution: partial
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md']
---
# PS C:\Users\Bryan\Desktop\Phython Projects\blender ai agent> python --versionPython was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.PS C:\Users\Bryan\Desktop\Phython Projects\blender ai agent> 

### USER
PS C:\Users\Bryan\Desktop\Phython Projects\blender ai agent> python --versionPython was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.PS C:\Users\Bryan\Desktop\Phython Projects\blender ai agent> 

### GEMINI
It looks like you're trying to run the python command, but your terminal isn't recognizing it. This is a common issue on Windows when Python isn't in your system's PATH, or a different alias is in use. You need to use the full path to the Python executable within your virtual environment to ensure you're running the right version. How to Check the Version First, make sure your new virtual environment, blender_ai_env_311, is activated. Then, use the following command to check the version of Python specifically in that environment: blender_ai_env_311\Scripts\python.exe --version The output should be Python 3.11.9, which will confirm you're on the correct version and can move on to installing the packages.