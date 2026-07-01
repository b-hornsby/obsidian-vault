---
category: coding
date: 2025-07-17
id: 835836
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan is clarifying whether he needs to change oobabooga settings or just
  his workflow code.
tags:
- oobabooga
- crewai
- workflow-code
- configuration
---
# so i don't need to change anything on the oobabooga side but the code for the workflow itself?

### USER
so i don't need to change anything on the oobabooga side but the code for the workflow itself?

### GEMINI
Yes, that's correct! Assuming you have already completed these one-time setup steps on the Oobabooga side: Oobabooga text-generation-webui is running. The openai extension is enabled in Oobabooga's "Session" tab (and you've restarted the UI after enabling it). Your "Phi-3-mini-4k-instruct-q4" model is loaded in Oobabooga's "Model" tab. If those three conditions are met, then you do not need to make any further changes within the Oobabooga web UI or its configuration files. All the "aliasing" and redirection for your CrewAI workflow happens by setting the OPENAI_API_BASE and OPENAI_MODEL_NAME environment variables (or directly configuring the OpenAI client if you're using it directly) within your Python code, as shown in the example. Your CrewAI application will then send requests to your local Oobabooga server, presenting itself as if it's talking to gpt-3.5-turbo.
