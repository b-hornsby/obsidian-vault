---
id: 732277
source: GEMINI
date: 2025-07-05
tags: ['ai-tools', 'ai', 'gemini', 'model', 'oobabooga', 'rag', 'gguf', 'hermes']
category: ai-tools
sentiment: building
resolution: abandoned
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# there's more to it but on the wsl2 environment where oobabooga was running, this popped up when i asked the question in  the other window: 11:29:16-460074 ERROR    No model is loaded. Please select one in the Model tab.
Exception in ASGI application
  + Exception Group Traceback (most recent call last):
  |   File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/starlette/_utils.py", line 77, in collapse_excgroups
  |     yield
  |   File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/starlette/middleware/base.py", line 186, in __call__
  |     async with anyio.create_task_group() as task_group:
  |   File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 772, in __aexit__
  |     raise BaseExceptionGroup(
  | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception)
  +-+
---
-
---
-
---
-
---
- 1 -
---
-
---
-
---
-
---
    | Traceback (most recent call last):
    |   File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/uvicorn/protocols/http/h11_impl.py", line 403, in run_asgi
    |     result = await app(  # type: ignore[func-returns-value]
    |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    |   File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
    |     return await self.app(scope, receive, send) 

### USER
there's more to it but on the wsl2 environment where oobabooga was running, this popped up when i asked the question in  the other window: 11:29:16-460074 ERROR    No model is loaded. Please select one in the Model tab.
Exception in ASGI application
  + Exception Group Traceback (most recent call last):
  |   File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/starlette/_utils.py", line 77, in collapse_excgroups
  |     yield
  |   File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/starlette/middleware/base.py", line 186, in __call__
  |     async with anyio.create_task_group() as task_group:
  |   File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 772, in __aexit__
  |     raise BaseExceptionGroup(
  | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception)
  +-+
---
-
---
-
---
-
---
- 1 -
---
-
---
-
---
-
---
    | Traceback (most recent call last):
    |   File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/uvicorn/protocols/http/h11_impl.py", line 403, in run_asgi
    |     result = await app(  # type: ignore[func-returns-value]
    |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    |   File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
    |     return await self.app(scope, receive, send) 

### GEMINI
Ah, that's the key! The error No model is loaded. Please select one in the Model tab. from Oobabooga's terminal is the root cause of the Internal Server Error you saw previously. This means that while Oobabooga's API server started up, it didn't actually load the AI model (Nous-Hermes-2 Mistral GGUF) into memory. This happens if the model name provided was incorrect or if you started it without specifying the model. Let's fix this immediately. Solution: Ensure Oobabooga Loads the Model You need to make sure you specify the correct model name when starting Oobabooga. Go to your second WSL2 terminal window (where Oobabooga is running). Stop Oobabooga. You can do this by pressing Ctrl + C in that terminal. You might need to press it a couple of times. Find the exact filename of your Nous-Hermes-2 Mistral GGUF model. It should be in your ~/text-generation-webui/models/ directory. In your Oobabooga terminal, type: ls models/ Look for the .gguf file (e.g., nous-hermes-2-mistral-7b-dpo.Q4_K_M.gguf). Make sure you get the full and exact filename, including capitalization and any Q4_K_M.gguf part. Restart Oobabooga, explicitly loading the model with --model and enabling the API with --api. Replace [YOUR_MODEL_FILENAME] with the exact filename you found in the previous step. python server.py --model [YOUR_MODEL_FILENAME] --api For example: python server.py --model nous-hermes-2-mistral-7b-dpo.Q4_K_M.gguf --api Wait for it to load completely. This step will take longer than before, as it's actually loading the large AI model into memory. You'll see progress bars and messages related to the model loading. It should eventually say: INFO: Started server process [xxxxx] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://127.0.0.1:5000 (Press CTRL+C to quit) Once you confirm that Oobabooga has fully loaded the model and is running the API at http://127.0.0.1:5000 in the second terminal, then switch back to your first terminal and try running rag_chat.py again. We can skip the CHUNK_SIZE and k adjustments for now, as the primary issue was Oobabooga not having a model loaded. If it still errors out after this, we can revisit those. Let me know the output from your Oobabooga terminal after you restart it with the model specified.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]