---
category: ai-tools
date: 2025-09-07
id: 724356
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wants to create a prompt for Cursor to implement a Delegation Tool
  for his AI agent pipeline, which breaks down high-level creative requests into smaller
  tasks.
tags:
- ai-agent-pipeline
- delegation-tool
- task-decomposition
- cursor-prompt
---
# let run down the list and get these working. start with this one and give me a prompt to feed cursor: Delegation Tool (for the Director Agent): This tool is more of an internal function. Its job is to help the Director agent break down a high-level creative request (like "make a crypto animation") into smaller, sequential tasks for the other agents (like "generate environment," "load assets," etc.).

### USER
let run down the list and get these working. start with this one and give me a prompt to feed cursor: Delegation Tool (for the Director Agent): This tool is more of an internal function. Its job is to help the Director agent break down a high-level creative request (like "make a crypto animation") into smaller, sequential tasks for the other agents (like "generate environment," "load assets," etc.).

### GEMINI
Let's do it. We'll start with the Delegation Tool. This tool is unique because it doesn't talk to an external service like an API. Instead, it's a special function that helps your Director Agent break down big ideas into a simple, ordered to-do list for the rest of the crew. Here is the code for the DelegationTool. The Code for the Delegation Tool Copy this code and paste it into your scripts/blender_tools.py file. from crewai import Tool class DelegationTool(Tool): """ This tool is used by the Director Agent to break down a high-level creative prompt into a detailed, sequential list of tasks for the other agents in the crew. """ name: str = "Delegation Tool" description: str = "Useful for analyzing a user's high-level request and breaking it down into a detailed list of sub-tasks for the Environment, Asset, Animation, and RenderAndPolish agents." def _run(self, prompt: str) -> str: """ Analyzes the user's creative prompt and creates a structured list of tasks with clear instructions and dependencies for each agent. """ task_list = f""" Creative Request: {prompt} Detailed Task List for the Crew: 1. **Environment Agent:** Generate a background and environment based on the prompt. This includes setting the skybox and lighting mood. 2. **Asset Agent:** Generate or fetch all necessary 3D models and textures. This includes the primary subject (e.g., the crypto coin) and any secondary props. 3. **Animation Agent:** Create the keyframe animations, camera movements, and object interactions based on the plan. 4. **RenderAndPolish Agent:** Finalize lighting, render the animation, and perform any necessary post-processing effects. This list is a complete workflow. Each agent should work sequentially and pass its output to the next. """ return task_list # Note: You'll also need to add this tool to the Director Agent in your crew.py file. # We'll get to that in the next step. What This Code Does class DelegationTool(Tool):: This line creates a new "tool" for your crew. The Tool part tells CrewAI that this is something an agent can use to perform a job. name and description: This is how the AI "knows" when to use this tool. The description tells the Director Agent that this tool's job is to break down a big prompt. def _run(self, prompt: str): This is the core of the tool. It's the action the tool performs. It takes the prompt from the user and turns it into the structured list of tasks you see in the code. return task_list: The tool finishes its job and gives the detailed list back to the Director Agent. After you've copied this code, the Director Agent will now have the ability to create a plan for the other agents. What would you like to work on next?
