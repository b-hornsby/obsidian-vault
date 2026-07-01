---
category: ai-tools
date: 2025-11-18
id: 801542
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan configured Cursor with a custom base URL and model name but was getting
  'message too long' errors and wasn't sure if the local model was actually being
  used.
tags:
- cursor-ide
- ollama
- ngrok
- base-url
- local-llm-integration
---
# i did the placeholder, i changed the base url and i made the name of the model gpt-4. now it says message too long when i type hi but i'm still not sure if its even working with my model

### USER
i did the placeholder, i changed the base url and i made the name of the model gpt-4. now it says message too long when i type hi but i'm still not sure if its even working with my model

### GEMINI
That is fantastic news! The fact that you received the error "message too long" (instead of the previous "does not work with current plan or api key") confirms two vital things: ✅ The ngrok tunnel is working. ✅ Cursor is successfully sending the request to your LM Studio server. ✅ The LM Studio server is receiving the request and attempting to process it. The new error, "message too long," is a sign of a misconfigured context window limit on the LM Studio server, a common issue when using models in an OpenAI-compatible API wrapper. Here is how to fix this and get your model working: 🔧 Step 5: Fix the Context Window Limit in LM Studio The "message too long" error on a simple prompt like "hi" indicates that the context window (the model's "memory" size, $n_{ctx}$) in LM Studio is set too small, or the model's internal prompt template is using a lot of tokens. The Qwen2.5-Coder-14B-Instruct model natively supports a large context (up to 32,768 tokens, or even 128K with specific configurations), so the limit is almost certainly set incorrectly in LM Studio. Go to the LM Studio Application. Navigate to the "${\ldots}$ Local Server" tab. Look for the "Model Settings" panel (usually on the right side). Find the setting labeled "Context Length (n_ctx)" or "Max Context Size". The default value is sometimes very small (like 512 or 2048) or simply wrong after a fresh load. Set this value much higher. A safe and robust value for your model is its native context size. Recommended Value: Set $n_{ctx}$ to 16384 (16K tokens) or 32768 (32K tokens). This is the native size for Qwen2.5-Coder. Restart the Server: After changing the setting, click the "Stop Server" button and then the "Start Server" button to apply the new context length. Check ngrok: Make sure your ngrok http 1234 session is still running and the forwarding URL is the same. Why this happens with Cursor: When you use $\text{Cmd+K}$ or chat in Cursor, it sends your entire codebase context (the file you are focused on, related files, etc.) plus the system prompt and your actual message, all in one large prompt. Even if you type "hi," that hidden context is what is causing the prompt to exceed the tiny, misconfigured $n_{ctx}$ limit in LM Studio. Setting it to 16K or 32K will give Cursor the space it needs to include the codebase context. ✅ Step 6: Verify in Cursor Go back to Cursor. Start a new chat just to be safe (old chats might have bad context history). Type a small, clear prompt like: Explain the difference between a list and a tuple in Python. Question: What does the LM Studio log window show when you send this new, small prompt? You should see a successful API call followed by token generation logs (numbers flying across the screen) and the model responding in Cursor. Let me know the result!
