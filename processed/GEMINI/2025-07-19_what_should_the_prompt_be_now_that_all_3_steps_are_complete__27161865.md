---
category: ai-tools
date: 2025-07-19
id: 183567
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- private-ai-consulting
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan is asking for the appropriate prompt to use in Cursor to scaffold his
  AI helpdesk project.
tags:
- ai-helpdesk
- cursor-ide
- scaffolding
- prompt-engineering
---
# what should the prompt be now that all 3 steps are complete for cursor to scaffold this and bring this idea to life? ensure that the primary goal of the project is defined for maximum clarity and best results 

### USER
what should the prompt be now that all 3 steps are complete for cursor to scaffold this and bring this idea to life? ensure that the primary goal of the project is defined for maximum clarity and best results 

### GEMINI
Now that you've completed all three preparation steps (created .env, set up the data folder, and ensured Oobabooga is running), your project is ready for Cursor to scaffold the CrewAI application. To achieve the best results and ensure Cursor understands the full scope of your project, use the following prompt. It explicitly states the primary goal and references the context_profile.json for all the details. Cursor Prompt Here's the prompt you should use for Cursor: Using the detailed context and requirements provided in `context_profile.json`, please scaffold a CrewAI project. The **primary goal of this project is to create an AI-powered hybrid IT helpdesk that autonomously resolves common technical issues using a local LLM, a knowledge base, and real command execution (with safety protocols), and seamlessly escalates complex problems to human technicians.** Generate the necessary Python files for the agents, tasks, and tools as defined in `context_profile.json`. Ensure the setup correctly integrates with the local Oobabooga LLM as specified in the `llm_details` section, and that tools designed for real command execution include placeholder functions with clear safety warnings and instructions for implementation. Also, generate the main script to run the crew.
