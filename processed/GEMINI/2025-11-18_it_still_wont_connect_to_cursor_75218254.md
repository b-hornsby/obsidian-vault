---
category: ai-tools
date: 2025-11-18
id: 730481
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was still unable to connect his local Ollama model to Cursor IDE despite
  troubleshooting efforts.
tags:
- cursor-ide
- ollama
- ngrok
- connection-issue
- local-llm
---
# it still wont connect to cursor

### USER
it still wont connect to cursor

### GEMINI
That's frustrating! It sounds like we have covered the most common issues (CORS, /v1 endpoint, model isolation), but one final detail is likely causing the failure. The "The model does not work with your current plan or API key" error is incredibly common with Cursor and local LLMs, and often points to a mismatch in the request being sent. Let's go through the definitive three checks and one verification step to pinpoint the failure. 🔎 Three Critical Checks (Double-Check Everything) Check 1: Ollama Server Status (The CORS Restart) You said you ran the PowerShell command, which is good for persistence, but the running ollama serve process needs to be aware of the new environment variable. Go to the terminal running ollama serve and press Ctrl+C to stop it. Restart the server by running: ollama serve If you still get the error, the CORS setting is the most likely culprit, as the request is being blocked before it even hits the model. Check 2: Cursor Model Isolation This is the most frequent cause of that specific error message. Open Cursor Settings (Ctrl+, or Cmd+,) and go to "Models." Scroll down to the list of models. ABSOLUTELY CONFIRM that only qwen2.5-coder:14b-instruct-q4_K_M is toggled ON. If you leave any other model (like GPT-4, Claude, etc.) toggled on, Cursor tries to check if that model works at your ngrok URL, which causes the failure. Check 3: API Key/URL Entry The URL must be perfectly formatted. In the "OpenAI API Key" section: API Key: Must be a placeholder, e.g., Ollama Override OpenAI Base URL: Must be your ngrok HTTPS address + /v1. Your ngrok URL was: https://delena-ungrinned-lemuel.ngrok-free.dev The required Base URL is: https://delena-ungrinned-lemuel.ngrok-free.dev/v1 ✅ Verification Step: Check the Logs If you have confirmed all three checks above, we need to see where the request is dying. Make sure the ngrok terminal and the Ollama server terminal are both open and running. In Cursor, go to the chat panel (Cmd+L / Ctrl+L) and send a simple prompt (e.g., "Hello"). Check the ngrok terminal first: Do you see any activity (like POST /v1/chat/completions 200 OK or 404 Not Found)? Check the Ollama terminal second: Do you see a request being logged by Ollama? If the request made it past ngrok, Ollama should log that it received a request for qwen2.5-coder:14b-instruct-q4_K_M. If you see no activity in either log when you send a prompt in Cursor, the problem is likely an aggressive setting in Cursor blocking the request from leaving, or a fundamental CORS block. If you see a 4xx or 5xx error in the ngrok log, copy the exact error and let me know. That will tell us exactly what's failing. What do the logs show when you try to prompt the model in Cursor?
