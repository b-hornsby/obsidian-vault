---
category: ai-tools
date: 2025-09-07
id: 095477
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- private-ai-consulting
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wants to create a prompt for Cursor to implement a Skybox AI API for
  his Environment Agent, which will generate 3D environments from text prompts.
tags:
- ai-agent-pipeline
- skybox-ai-api
- environment-generation
- cursor-prompt
---
# next tool same idea: Skybox AI API (for the Environment Agent): This tool will handle the communication with an external AI service. It would take a text prompt (e.g., "futuristic cityscape at night") and send it to Skybox AI to get a generated 3D environment or texture back.

### USER
next tool same idea: Skybox AI API (for the Environment Agent): This tool will handle the communication with an external AI service. It would take a text prompt (e.g., "futuristic cityscape at night") and send it to Skybox AI to get a generated 3D environment or texture back.

### GEMINI
Sounds good. The Skybox AI API is the next step. This tool is a great example of an agent needing to communicate with an external service, not just internal code. The requests library is the standard for this kind of work in Python. Here's the prompt to have Cursor generate the code for you. Prompt for Cursor "Create a Python class named SkyboxAITool inside the scripts/blender_tools.py file. Import the requests library. The class should have a name of 'Skybox AI Generator' and a description that explains its purpose: 'Useful for generating a 360-degree environment from a text prompt using the Skybox AI API.' The class should have a run method that takes a single string argument: text_prompt. Inside the run method, use the requests library to make a POST request to the Skybox AI API endpoint. The request body should include the text_prompt. The method should also handle the API response. If successful, it should save the generated image to your assets/environments/ directory. If there's an error, it should print the error message. Important: The code should include a placeholder for your API key, like api_key = 'YOUR_API_KEY_HERE', and a comment instructing the user to replace it with their actual key. Add comments throughout the code to explain what each section does." This prompt will create the skeleton for the Environment Agent's ability to generate a 3D environment, using an external API as the basis for its work. Here's a video on how to use AI to generate a skybox.


## Related

### Projects

- [[nodes/projects/private-ai-consulting|Private AI Consulting]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
