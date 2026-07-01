---
id: 955423
source: GEMINI
date: 2025-09-07
tags: ['json-context-profile', 'cursor-scaffolding', 'project-structure', 'placeholder-files']
category: coding
sentiment: building
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan has generated a JSON context profile and placeholder files/folders to give Cursor AI maximum project context for scaffolding.
---
# okay so i ran those two, we have the .json context profile and these are my placeholder files/folders so cursor has as much context as possible: 

### USER
okay so i ran those two, we have the .json context profile and these are my placeholder files/folders so cursor has as much context as possible: 

### GEMINI
With those libraries installed and your project structure in place, you are now ready to have Cursor scaffold the core code for your AI crew. The key is to provide a very specific and detailed prompt that leverages the context_profile.json file you have already created. The Cursor Prompt You'll need to use Cursor's ability to read and understand your project files. By referencing the context_profile.json file, you can instruct Cursor to parse the data and use it to build your agents. This process is often called "prompt stacking" or providing "context bundling." Here is a breakdown of the prompt you should use: Prompt for Cursor: "Based on the context_profile.json file in my project's root directory, create the director.py file inside the agents/ folder. Import the necessary Agent, Task, and Crew classes from crewai. Import json to load the context_profile.json file. Read and parse the context_profile.json file to get the agent definitions (role, goal, backstory). Define the Director agent using its attributes from the JSON data. Define a simple Task for the Director that instructs it to "create a 30-second futuristic crypto animation." Instantiate the Crew with the Director agent and its task. Add a main execution block (if __name__ == "__main__":) to kick off the crew's work. Add comments explaining what each part of the code does." This prompt tells Cursor exactly what to do and where to find the information, which will result in the most accurate code generation. The video below explains how to get started with CrewAI, including how to define agents with roles, goals, and backstories. CrewAI Tutorial: Build AI Agents in less than 40 lines of Python!
