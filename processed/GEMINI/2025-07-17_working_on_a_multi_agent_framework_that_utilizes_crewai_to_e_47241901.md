---
category: coding
date: 2025-07-17
id: 598227
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is troubleshooting a LiteLLM provider error preventing CrewAI from
  recognizing his oobabooga model.
tags:
- crewai
- multi-agent-framework
- oobabooga
- litellm
- llm-provider-error
---
# working on a multi agent framework that utilizes crewai to emulate a real helpdesk team and i'm using my model (Phi-3-mini-4k-instruct-q4) running in wsl2 via oobabooga to power the brains of the workflow. ran my main.py and this is the summary of my issue:  CrewAI (via LiteLLM) fails to recognize the custom model name (Phi-3-mini-4k-instruct-q4) as belonging to a valid provider, even when the provider is set via environment variables. This results in a "LLM Provider NOT provided" error, blocking all LLM completions and preventing the workflow from running with oobabooga as the backend.

### USER
working on a multi agent framework that utilizes crewai to emulate a real helpdesk team and i'm using my model (Phi-3-mini-4k-instruct-q4) running in wsl2 via oobabooga to power the brains of the workflow. ran my main.py and this is the summary of my issue:  CrewAI (via LiteLLM) fails to recognize the custom model name (Phi-3-mini-4k-instruct-q4) as belonging to a valid provider, even when the provider is set via environment variables. This results in a "LLM Provider NOT provided" error, blocking all LLM completions and preventing the workflow from running with oobabooga as the backend.

### GEMINI
Decoding the "LLM Provider NOT Provided" Error: A Guide to Integrating Custom Models with CrewAI and Oobabooga You're encountering a common stumbling block when venturing into the exciting world of multi-agent frameworks with locally hosted models. The "LLM Provider NOT provided" error from CrewAI (via LiteLLM) is essentially a breakdown in communication. Your CrewAI agents, powered by LiteLLM, are unable to identify which language model provider to use for your custom model, in this case, Phi-3-mini-4k-instruct-q4 running on Oobabooga. This guide will walk you through the necessary configurations to resolve this issue and get your helpdesk team simulation up and running. The Root of the Problem: Missing Identification At its core, the issue lies in how LiteLLM, the library CrewAI uses to communicate with a vast array of language models, recognizes and categorizes them. When you provide a model name, LiteLLM attempts to match it with a known provider (like OpenAI, Cohere, etc.). For custom-hosted models, you need to explicitly tell LiteLLM two crucial pieces of information: The Provider: You must specify that you are using a custom, Oobabooga-hosted model. The Endpoint: LiteLLM needs the URL of your Oobabooga server to send requests. Without this information, LiteLLM is lost and throws the "LLM Provider NOT provided" error. The Solution: Proper Configuration in Your CrewAI Project To fix this, you need to correctly configure your environment variables and how you instantiate your ChatOllama (or a similar class) in your Python script. Here’s a step-by-step breakdown: Step 1: Setting the Correct Environment Variables The most robust way to configure CrewAI and LiteLLM is through environment variables. This keeps your credentials and endpoints separate from your main codebase. You'll need to set the following: OPENAI_API_BASE: This variable must point to your Oobabooga server's API endpoint. Typically, this will be http://<your-wsl2-ip>:5000/v1. The /v1 at the end is crucial for the OpenAI-compatible endpoint of Oobabooga. OPENAI_MODEL_NAME: This is where you specify your custom model. To signify that it's a custom model for Oobabooga, you should prefix it with oobabooga/. So, for your model, the value should be oobabooga/Phi-3-mini-4k-instruct-q4. OPENAI_API_KEY: Even though you are running a local model that may not require an API key for authentication, the LiteLLM library often expects a value for this variable. You can typically set this to a dummy string like "NA". You can set these in a .env file in your project's root directory and use a library like python-dotenv to load them. .env file example: OPENAI_API_BASE="http://localhost:5000/v1" OPENAI_MODEL_NAME="oobabooga/Phi-3-mini-4k-instruct-q4" OPENAI_API_KEY="NA" Note: Replace localhost with the actual IP address of your WSL2 instance if you are running your Python script from outside of it. Step 2: Updating Your Python Code In your main.py or wherever you are defining your CrewAI agents, you need to instantiate the language model object correctly. When using a custom OpenAI-compatible endpoint like Oobabooga's, you can leverage the ChatOllama class from crewai.llms or directly use ChatOpenAI from langchain_openai. Here's an example of how to define your LLM in your Python script: import os from dotenv import load_dotenv from crewai import Agent, Task, Crew from crewai.llms import ChatOllama # Load environment variables from .env file load_dotenv() # Define the custom LLM # The model name will be picked up from the OPENAI_MODEL_NAME environment variable. # The api_base will be picked up from the OPENAI_API_BASE environment variable. llm = ChatOllama( model=os.getenv("OPENAI_MODEL_NAME"), base_url=os.getenv("OPENAI_API_BASE") ) # Now you can define your agents and tasks using this `llm` instance helpdesk_agent = Agent( role='Helpdesk Specialist', goal='Provide excellent first-line technical support.', backstory='An experienced and patient helpdesk specialist.', llm=llm, allow_delegation=False ) # ... your other agents and tasks By explicitly passing the model and base_url to the ChatOllama constructor, you are directly telling CrewAI and LiteLLM how to connect to your custom model on Oobabooga. The oobabooga/ prefix in the model name acts as the provider identifier for LiteLLM. By following these steps, you should be able to resolve the "LLM Provider NOT provided" error and successfully integrate your custom Phi-3 model running on Oobabooga with your CrewAI framework, paving the way for your multi-agent helpdesk team to start solving problems. 🤖💻


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/it-certification|IT Certification]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
