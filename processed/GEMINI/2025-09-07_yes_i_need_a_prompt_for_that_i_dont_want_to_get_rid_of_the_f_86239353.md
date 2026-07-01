---
id: 718394
source: GEMINI
date: 2025-09-07
tags: ['ai-agent', 'skybox-generation', 'prompt-engineering', 'image-upload']
category: ai-tools
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan needs a prompt for his AI agent to generate skyboxes, but wants to retain some functionality despite limited funds, planning to use image uploads.
---
# yes i need a prompt for that. i dont want to get rid of the functionality to be able to have the ai agent go and make worlds for me in skybox BUT since i dont have the funds right now i still want SOME functionality (will most likely upload picture files in)

### USER
yes i need a prompt for that. i dont want to get rid of the functionality to be able to have the ai agent go and make worlds for me in skybox BUT since i dont have the funds right now i still want SOME functionality (will most likely upload picture files in)

### GEMINI
Yes, I have a prompt for that. We can modify the SkyboxAITool to have a fallback option. This is a common and practical approach when dealing with paid APIs. The new functionality will allow the tool to check for a valid API key. If it doesn't find one, it will automatically use a local image file from your assets/environments/ folder instead of trying to make a paid API call. This keeps the core functionality intact while letting your crew continue to work. The Cursor Prompt "Open and modify the SkyboxAITool class in scripts/blender_tools.py. Add a new boolean parameter to the run method called use_local_file, which defaults to False. Inside the run method, add an if-else statement. If use_local_file is True, the method should search your assets/environments/ directory for a file that matches the provided text_prompt and return the path to that file. Else (if use_local_file is False), the method should proceed with the original requests.post() API call logic. Add a clear comment in the run method explaining the new fallback functionality. Ensure the tool's description is updated to reflect its ability to use either the API or a local file."
