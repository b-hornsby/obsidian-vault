---
category: ai-tools
date: 2025-07-05
id: 937035
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: executing
source: GEMINI
summary: Bryan is agreeing to fix a problem, indicating that an issue has been identified
  and he's ready to address it.
tags:
- local-llm
- debugging
- issue-resolution
---
# yeah lets fix it please ;)

### USER
yeah lets fix it please ;)

### GEMINI
No problem at all! Let's get that minor UI issue fixed for whisper_stt so your spoken input shows up in the chat box. Here are the steps to modify the script.py file for the whisper_stt extension: Step 1: Stop Oobabooga If your Oobabooga server is currently running, go to your WSL2 terminal and press Ctrl+C to stop it. Step 2: Edit the whisper_stt Script File Navigate to the correct directory: cd ~/text-generation-webui/extensions/whisper_stt/ Open the script.py file using nano: nano script.py Locate the auto_transcribe function: Once the file opens in nano, use your arrow keys to scroll down. Look for a line that starts with def auto_transcribe(. Inside this function, you'll need to find the line that currently returns the transcription string. It will likely look like this: return transcription Modify the return statement: Change the return transcription line to the following: return {"text": transcription, "files": []} This change wraps the transcribed text in a dictionary format that the Gradio MultimodalTextbox component expects, allowing it to display your spoken input in the chat box. Save and Exit nano: Press Ctrl+O (to write out/save the changes). Press Enter to confirm the filename. Press Ctrl+X (to exit the nano editor). Step 3: Restart Oobabooga Go back to the Oobabooga root directory: cd ~/text-generation-webui/ Restart the Oobabooga server: ./installer_files/env/bin/python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf Step 4: Test Voice Input in the UI Once Oobabooga is fully loaded, open your web browser and go to http://127.0.0.1:7860. Navigate to the "Chat" tab. Click the microphone icon to record your voice. Now, after you speak and the transcription completes, your spoken words should appear in the input text box of the chat UI, in addition to being processed by the AI. Let me know if you successfully make the edit and if the input text appears as expected!
