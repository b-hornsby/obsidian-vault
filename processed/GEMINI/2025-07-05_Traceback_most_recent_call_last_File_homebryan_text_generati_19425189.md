---
id: 085833
source: GEMINI
date: 2025-07-05
tags: ['coding', 'ai', 'gemini', 'model', 'oobabooga', 'gguf', 'embedding', 'hermes']
category: coding
sentiment: executing
resolution: unresolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md']
---
# Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/queueing.py", line 541, in process_events
    response = await route_utils.call_process_api(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/route_utils.py", line 276, in call_process_api
    output = await app.get_blocks().process_api(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/blocks.py", line 1938, in process_api
    data = await self.postprocess_data(block_fn, result["prediction"], state)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/blocks.py", line 1761, in postprocess_data
    prediction_value = block.postprocess(prediction_value)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/components/multimodal_textbox.py", line 166, in postprocess
    raise ValueError(
ValueError: MultimodalTextbox expects a dictionary with optional keys 'text' and 'files'. Received str
13:47:17-728425 INFO     Adding 5 new embeddings.
/home/bryan_/text-generation-webui/extensions/superboogav2/chromadb.py:195: RuntimeWarning: invalid value encountered in scalar divide
  weights = weights * (time_power / max(weights))
prompt processing progress, n_past = 379, n_tokens = 123, progress = 1.000000
prompt eval time =     892.95 ms /   379 tokens (    2.36 ms per token,   424.44 tokens per second)
       eval time =   10935.76 ms /   270 tokens (   40.50 ms per token,    24.69 tokens per second)
      total time =   11828.71 ms /   649 tokens
13:47:29-589580 INFO     Output generated in 11.83 seconds (22.90 tokens/s, 271 tokens, context 379, seed 2142622427)

### USER
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/queueing.py", line 541, in process_events
    response = await route_utils.call_process_api(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/route_utils.py", line 276, in call_process_api
    output = await app.get_blocks().process_api(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/blocks.py", line 1938, in process_api
    data = await self.postprocess_data(block_fn, result["prediction"], state)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/blocks.py", line 1761, in postprocess_data
    prediction_value = block.postprocess(prediction_value)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/components/multimodal_textbox.py", line 166, in postprocess
    raise ValueError(
ValueError: MultimodalTextbox expects a dictionary with optional keys 'text' and 'files'. Received str
13:47:17-728425 INFO     Adding 5 new embeddings.
/home/bryan_/text-generation-webui/extensions/superboogav2/chromadb.py:195: RuntimeWarning: invalid value encountered in scalar divide
  weights = weights * (time_power / max(weights))
prompt processing progress, n_past = 379, n_tokens = 123, progress = 1.000000
prompt eval time =     892.95 ms /   379 tokens (    2.36 ms per token,   424.44 tokens per second)
       eval time =   10935.76 ms /   270 tokens (   40.50 ms per token,    24.69 tokens per second)
      total time =   11828.71 ms /   649 tokens
13:47:29-589580 INFO     Output generated in 11.83 seconds (22.90 tokens/s, 271 tokens, context 379, seed 2142622427)

### GEMINI
The new error you're encountering is: ValueError: MultimodalTextbox expects a dictionary with optional keys 'text' and 'files'. Received str This error indicates a mismatch in what the Gradio interface (which Oobabooga uses) expects as an output format from a component (likely whisper_stt) and what it's actually receiving. It's expecting a complex data structure (a dictionary with text and/or file information) but is getting a simple string. This is often caused by a recent update to Gradio or a specific extension not fully catching up with a new Gradio format. Solution: Adjust Whisper STT's Output Format This issue typically needs a small modification within the whisper_stt extension's script.py file to make its output compatible with the MultimodalTextbox Gradio component. Stop Oobabooga: If Oobabooga is still running, press Ctrl+C in your WSL2 terminal to stop it. Edit the script.py file for whisper_stt: nano ~/text-generation-webui/extensions/whisper_stt/script.py Locate the auto_transcribe function: Scroll down or use Ctrl+W to search for def auto_transcribe(. Modify the return statement: Inside this function, you'll likely find a line that looks something like: return transcription You need to change this line to return a dictionary in the format Gradio expects: return {"text": transcription, "files": []} Explanation: This wraps the transcription string into a dictionary with a "text" key, and adds an empty "files" list, satisfying the MultimodalTextbox's requirements. Save and Exit nano: Press Ctrl+O (to write out/save), then Enter to confirm the filename. Press Ctrl+X (to exit). Step 2: Restart Oobabooga After saving the modified script.py file, restart the Oobabooga server: ./installer_files/env/bin/python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf Step 3: Test Voice Input Again Go back to the Oobabooga web UI (http://127.0.0.1:7860). Navigate to the "Chat" tab. Click the microphone icon to record your voice. This change should resolve the ValueError and allow your spoken input to be transcribed and appear in the chat textbox. Let me know if you hit any issues with editing the file or after restarting!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]