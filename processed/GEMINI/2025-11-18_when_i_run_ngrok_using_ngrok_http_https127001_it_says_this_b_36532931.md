---
category: homelab
date: 2025-11-18
id: 763353
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was trying to connect Cursor IDE through an ngrok tunnel but hit a
  plan/API key limitation.
tags:
- ngrok
- cursor-ide
- api-key
- tunneling
---
# when i run ngrok using: ngrok http https:127.0.0.1 it says this but when i try to connect to cursor it says it doesnt work with current plan or api key: �  Decouple policy and sensitive data with vaults: https://ngrok.com/r/secrets

Session Status                online
Account                       bryh4m@gmail.com (Plan: Free)
Update                        update available (version 3.33.0, Ctrl-U to update)
Version                       3.22.1
Region                        United States (us)
Latency                       17ms
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://delena-ungrinned-lemuel.ngrok-free.dev -> http://127.0.0.1:1234

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00

### USER
when i run ngrok using: ngrok http https:127.0.0.1 it says this but when i try to connect to cursor it says it doesnt work with current plan or api key: �  Decouple policy and sensitive data with vaults: https://ngrok.com/r/secrets

Session Status                online
Account                       bryh4m@gmail.com (Plan: Free)
Update                        update available (version 3.33.0, Ctrl-U to update)
Version                       3.22.1
Region                        United States (us)
Latency                       17ms
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://delena-ungrinned-lemuel.ngrok-free.dev -> http://127.0.0.1:1234

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00

### GEMINI
This is a critical piece of information and a very common hurdle when connecting local models to Cursor! What Your Terminal Output Tells Us Successful ngrok Tunnel: Your terminal shows that the ngrok tunnel is working perfectly and is forwarding to the correct local address: Forwarding URL: https://delena-ungrinned-lemuel.ngrok-free.dev Local Target: http://127.0.0.1:1234 This means any request sent to the ngrok URL is successfully being passed to your LM Studio server. The Cursor Error: The error "The model does not work with your current plan or api key" is the standard, generic error Cursor gives when it successfully connects to the overridden base URL (your ngrok link) but then encounters an issue with the API call itself. This usually means one of two things: The API endpoint URL is wrong. (The most common reason). The Model Name is wrong (LM Studio has a specific name it uses). Cursor is rejecting the connection because of a check it performs on its side. Let's troubleshoot the Base URL and Model Name first. 🛠️ Step 4: Correct the Cursor Configuration The most likely issue is that you did not append the necessary path to your ngrok URL in Cursor's settings. The OpenAI API standard requires the path to end in /v1. LM Studio implements this standard. 1. Re-check the Base URL Go back to Cursor Settings ($\text{Cmd+,}$ or $\text{Ctrl+,}$) > Models section: Override OpenAI Base URL: You must append /v1 to your ngrok URL. Current ngrok URL: https://delena-ungrinned-lemuel.ngrok-free.dev Correct Base URL to use in Cursor: https://delena-ungrinned-lemuel.ngrok-free.dev/v1 2. Verify the Model Name Cursor requires the model name you use to match exactly what your LM Studio server is broadcasting. Find the Model Name in LM Studio: Go to the "${\ldots}$ Local Server" tab in LM Studio. The model you loaded, Qwen2.5-Coder-14B-Instruct-Q4_K_M.gguf, will have a short API identifier. Look for it in the server logs or the configuration panel. Sometimes, it uses the filename (e.g., Qwen2.5-Coder-14B-Instruct-Q4_K_M) or a simplified version. Update the Model Name in Cursor: In Cursor Settings > Models, in the list of models (where you might have entered gpt-4o as a placeholder), add the exact model name you found in LM Studio. Crucially: If you still see the error, try using the standard OpenAI model name workaround: gpt-4 or gpt-3.5-turbo instead of your local model's actual name. Sometimes Cursor forces a model check on its own servers, and using one of their expected names bypasses this check while still routing the request through your overridden URL. 3. Final Check in Cursor Use a placeholder API Key (e.g., lm-studio-key). The Base URL is https://delena-ungrinned-lemuel.ngrok-free.dev/v1. Ensure only your custom model is selected in the list (or the workaround model like gpt-4). Deselecting official cloud models can help. Try to start a new chat or use $\text{Cmd+K}$ to initiate a prompt. Question: After you have changed the Base URL in Cursor to include the /v1 path, and ensured the model name is correct (either the LM Studio name or the gpt-4 workaround), what happens when you try to use the AI? Do you still get the same error, or do you see a different error in the Cursor UI, or perhaps even in the LM Studio log window?
