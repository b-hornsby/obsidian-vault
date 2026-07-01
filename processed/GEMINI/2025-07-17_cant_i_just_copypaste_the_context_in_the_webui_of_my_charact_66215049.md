---
category: ai-tools
date: 2025-07-17
id: 778842
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan wants to copy/paste character context from oobabooga into Cursor for
  codebase integration.
tags:
- oobabooga
- character-prompt
- cursor-ide
- workflow-integration
---
# can't i just copy/paste the context in the webui of my character and have cursor put that in the codebase?

### USER
can't i just copy/paste the context in the webui of my character and have cursor put that in the codebase?

### GEMINI
Yes, absolutely! That's actually the most direct and easiest way to do it. You can simply: Go to the "Character" tab in your Oobabooga web UI. Select your character. Locate the large text area labeled "Context" (or sometimes "Description" or "Persona"). Copy the entire content of that text area. Then, you can feed that copied text directly into a prompt for Cursor. Here's how you'd phrase that for Cursor: Cursor Prompt: "I have copied the system prompt (context) for my character from the Oobabooga web UI. Please insert this text into the Python script as the value for the character_system_prompt variable. Here is the copied text: [PASTE YOUR COPIED OOBABOOGA CHARACTER CONTEXT HERE] Ensure the text is enclosed within triple quotes ("""...""") to handle multi-line content correctly. The variable should look like this after the change: character_system_prompt = """ [PASTE YOUR COPIED OOBABOOGA CHARACTER CONTEXT HERE] """ "
