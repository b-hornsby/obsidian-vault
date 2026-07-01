---
category: ai-tools
date: 2025-07-17
id: 520617
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan wants to alias his model as gpt-3.5-turbo in oobabooga for CrewAI compatibility.
tags:
- oobabooga
- model-aliasing
- openai-compatible-api
- crewai-integration
---
# how do i alias my model as "gpt-3.5-turbo" in oobabooga? I heard that most Open AI-compatible servers will accept any model name and just use the loaded model (Phi-3-mini-4k-instruct-q4)

### USER
how do i alias my model as "gpt-3.5-turbo" in oobabooga? I heard that most Open AI-compatible servers will accept any model name and just use the loaded model (Phi-3-mini-4k-instruct-q4)

### GEMINI
You're right! Many OpenAI-compatible servers, including Oobabooga's text-generation-webui, are designed to accept a model parameter in API calls, but they'll typically just use the model that's currently loaded in the backend, regardless of what name you send. This is incredibly useful for compatibility with various frontends and tools that expect an OpenAI-style API. How to "alias" your loaded model (Phi-3-mini-4k-instruct-q4) as "gpt-3.5-turbo" in Oobabooga: You don't really "alias" it within Oobabooga's UI in a specific setting. Instead, you achieve this by leveraging Oobabooga's OpenAI-compatible API. Here's the breakdown: Enable the OpenAI API Extension in Oobabooga: Start Oobabooga's text-generation-webui. Go to the "Session" tab (or "Interface" on older versions). Find and check the box for the "openai" extension. Click "Apply and restart UI" (or whatever the equivalent button is to apply changes and restart the server). You should see a message in your Oobabooga console indicating that the OpenAI compatible API is ready, usually at http://0.0.0.0:5001/v1 or http://127.0.0.1:5000/v1. Load your desired model (Phi-3-mini-4k-instruct-q4): Go to the "Model" tab in Oobabooga. Load your "Phi-3-mini-4k-instruct-q4" model as you normally would. Make API Calls to Oobabooga using "gpt-3.5-turbo" as the model name: Now, when you use a tool or application that wants to connect to an OpenAI API (like a custom script, a frontend like SillyTavern, etc.), you'll configure it to point to your Oobabooga API endpoint and specify "gpt-3.5-turbo" as the model name. Example (Python using the openai library): from openai import OpenAI # Point to your Oobabooga API client = OpenAI( base_url="http://localhost:5000/v1", # Or whatever port your Oobabooga API is running on api_key="sk-whatever", # A dummy key is often sufficient, or use a real one if you set --api-key in Oobabooga ) response = client.chat.completions.create( model="gpt-3.5-turbo", # This is the "alias" you're using messages=[ {"role": "system", "content": "You are a helpful assistant."}, {"role == "user", "content": "Tell me a joke."}, ] ) print(response.choices[0].message.content) Key Points: base_url: This is crucial. It tells your application to send API requests to your local Oobabooga instance instead of OpenAI's servers. model="gpt-3.5-turbo": This is where you specify the "alias." Oobabooga's OpenAI API compatibility layer will typically ignore this model name and simply use the model you have loaded in the UI. api_key: While Oobabooga doesn't require a valid OpenAI API key for its local API, some applications or libraries might still expect one. You can provide a dummy string like "sk-whatever" or set a real API key in Oobabooga's startup flags (--api-key yourkey) if you want to enforce authentication. In summary: Oobabooga's OpenAI API extension acts as a translator. It receives requests formatted for the OpenAI API, ignores the specific model name in many cases, and then processes the request using the model you've loaded in its own UI. This allows you to effectively "alias" your local models for external applications.
