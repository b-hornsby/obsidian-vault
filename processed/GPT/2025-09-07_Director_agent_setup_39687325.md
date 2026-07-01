---
source: GPT
date: 2025-09-07
category: ai-tools
id: 39687325
linked_nodes: ['nodes/people/bryan.md']
---
# Director agent setup

### USER
got gemini to help me get everything setup with the blender stuff i think. this is the prompt it gave me for cursor: Based on the context_profile.json file in my project's root directory, create the director.py file inside the agents/ folder.

    Import the necessary Agent, Task, and Crew classes from crewai.

    Import json to load the context_profile.json file.

    Read and parse the context_profile.json file to get the agent definitions (role, goal, backstory).

    Define the Director agent using its attributes from the JSON data.

    Define a simple Task for the Director that instructs it to "create a 30-second futuristic crypto animation."

    Instantiate the Crew with the Director agent and its task.

    Add a main execution block (if __name__ == "__main__":) to kick off the crew's work.

    Add comments explaining what each part of the code does."

### ASSISTANT
Absolutely — we can make the Gemini prompt much more detailed and “Cursor-friendly,” so it doesn’t leave anything vague. Here’s a fully fleshed-out version you can feed directly to Cursor:  

If you want, I can also **write the exact Python file that Cursor should produce** from this prompt so you don’t have to guess if it got everything right. That usually saves a ton of headaches.  

Do you want me to do that next?

### USER
can you just rewrite the prompt gemini gave in a detailed way so that cursor gets this right?

### ASSISTANT
Perfect! That Gemini prompt is basically a step-by-step blueprint for creating a `director.py` script that will act as the “brain” of your Blender AI agent workflow using CrewAI. Here’s a clear breakdown of what’s happening and how to approach it:

### **Step-by-Step Explanation**

1. **Imports**
```python
from crewai import Agent, Task, Crew
import json
```
- `Agent`: Defines a single AI agent with a role and abilities.
- `Task`: Encapsulates a specific instruction or goal for an agent.
- `Crew`: Groups agents and manages task execution.
- `json`: Reads your `context_profile.json` for the agent’s setup.

3. **Define the Director agent**
```python
director_info = profile_data["agents"]["Director"]

director = Agent(
    name="Director",
    role=director_info["role"],
    goal=director_info["goal"],
    backstory=director_info.get("backstory", "")
)
```
- Pulls the Director’s info from the JSON.
- `backstory` is optional (defaults to empty string if missing).

5. **Instantiate the Crew**
```python
crew = Crew(agents=[director], tasks=[task])
```
- Groups the Director agent and its task into a “crew.”
- CrewAI will manage the workflow for executing the task.

7. **Add comments**
Make it clear what each block does, e.g.:
```python
# Load agent definitions from JSON
# Define the Director agent using JSON data
# Create a Task for the Director
# Group the agent and task in a Crew
# Run the Crew to execute tasks
```
---
## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/crypto-web3|Crypto Web3]]