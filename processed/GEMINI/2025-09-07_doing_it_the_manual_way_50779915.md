---
id: 550848
source: GEMINI
date: 2025-09-07
tags: ['coding', 'module', 'ai', 'agent', 'gemini', 'cursor', 'python', 'go']
category: coding
sentiment: building
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md']
---
# doing it the manual way: 

### USER
doing it the manual way: 

### GEMINI
Excellent. You are in the correct location. That's the site-packages directory inside your Blender installation's Python environment. To do this the manual way, you need to copy a few key files and folders from this directory into your project's virtual environment. The Files You Need to Copy The most crucial modules are bpy and mathutils. Look for these in the list of files and folders in your image. Find the bpy folder and the _bpy.pyd file (the C-extension that makes the API work). Find the mathutils folder. For good measure, you can also copy bl_ui and gpu related files if your agents might use them later for more advanced rendering features. Copy these specific files and folders from your Blender site-packages: bpy (folder) _bpy.pyd (or _bpy.so on Linux/macOS) mathutils (folder) bl_ui (folder) gpu (folder) _gpu.pyd (or _gpu.so) bgl (folder) _bgl.pyd (or _bgl.so) The Destination Now, paste all of those files and folders into your project's virtual environment site-packages directory. Based on your terminal output, that path is: C:\Users\Bryan\Desktop\Phython Projects\blender ai agent\blender_ai_env\Lib\site-packages Once you've copied those files, you can open a Python terminal within your virtual environment and test it with import bpy. If there are no errors, you've successfully bridged the two environments, and your agents can now use Blender's API. After this is complete, you can use the Cursor prompt we discussed earlier to generate the code for your director.py file.