---
category: coding
date: 2025-07-17
id: 850389
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/coding.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wants to make API calls to oobabooga using gpt-3.5-turbo alias for
  his CrewAI multi-agent workflow.
tags:
- oobabooga
- api-calls
- crewai
- gpt-3.5-turbo-alias
- multi-agent
---
# thats what i'm trying to do. how do i make API Calls to Oobabooga using "gpt-3.5-turbo" as the model name so that my multi agent workflow using crewai will pick my model up 

### USER
thats what i'm trying to do. how do i make API Calls to Oobabooga using "gpt-3.5-turbo" as the model name so that my multi agent workflow using crewai will pick my model up 

### GEMINI
To make API calls to Oobabooga using "gpt-3.5-turbo" as the model name for your CrewAI multi-agent workflow, you'll configure CrewAI to point to your Oobabooga instance's OpenAI-compatible API. Here's how you can set it up: Step 1: Ensure Oobabooga is Running with OpenAI API Enabled First, make sure your Oobabooga text-generation-webui is running and has its OpenAI API extension enabled: Start Oobabooga: Launch your start_windows.bat (or equivalent) script. Enable OpenAI Extension: In the Oobabooga web UI, navigate to the "Session" tab. Find the openai extension and check its box. Click "Apply and restart UI". Verify API Endpoint: Look at the console output of Oobabooga. You should see a line like: OpenAI compatible API ready at: OPENAI_API_BASE=http://0.0.0.0:5001/v1 Note the IP address and port (e.g., http://127.0.0.1:5000 or http://localhost:5000). This is the base_url you'll use. Load your Model: Go to the "Model" tab and ensure your "Phi-3-mini-4k-instruct-q4" model is loaded. Oobabooga will use this loaded model regardless of the model name sent in the API request. Step 2: Configure CrewAI to Use Oobabooga CrewAI uses the OPENAI_API_BASE and OPENAI_MODEL_NAME environment variables (or direct configuration) to determine where to send its API requests and what model name to use. Here's a Python script demonstrating how to set this up for your CrewAI workflow: Explanation: os.environ["OPENAI_API_BASE"] = "http://localhost:5000/v1": This is the most critical line. It tells any openai library calls (which CrewAI uses under the hood) to direct requests to your local Oobabooga server instead of OpenAI's official API. Adjust the port (5000 in this example) if your Oobabooga instance is running on a different one. os.environ["OPENAI_API_KEY"] = "sk-not-needed-for-local": While Oobabooga's local OpenAI API doesn't authenticate with a real OpenAI key, the openai Python library often expects this environment variable to be set. A dummy string is usually sufficient. If you configured Oobabooga with --api-key, you'd put that key here. os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo": This sets the model name that CrewAI will request. As discussed, Oobabooga's OpenAI compatibility layer will typically receive this but then use whatever model (your Phi-3-mini-4k-instruct-q4) is currently loaded in its backend to generate the response. By setting these environment variables before initializing your CrewAI agents and tasks, CrewAI will automatically route its requests to your Oobabooga instance, effectively "aliasing" your loaded Phi-3 model as "gpt-3.5-turbo" for your multi-agent workflow.
