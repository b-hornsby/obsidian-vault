---
category: ai-tools
date: 2025-07-02
id: 423597
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is reporting that adding the '--api' flag in nano didn't produce the
  expected API message when running Oobabooga, and other flags were missing.
tags:
- text-generation-webui
- oobabooga
- local-llm
- api-configuration
---
# so when i added --api to the nano and i ran oobabooga as normal the api message didn't pop up and these weren't in the nano when i added the -- api: --listen
--some-other-flag

### USER
so when i added --api to the nano and i ran oobabooga as normal the api message didn't pop up and these weren't in the nano when i added the -- api: --listen
--some-other-flag

### GEMINI
Ah, that's a common point of confusion with Oobabooga's flags! Thanks for letting me know. The reason you didn't see the API message after adding --api to CMD_FLAGS.txt is likely due to how start_linux.sh handles flags, especially if you have other flags or specific configurations. Let's try a different, more direct approach to ensure the API is enabled, and then we'll verify it. The most reliable way to force the API on for our purposes, especially if CMD_FLAGS.txt isn't behaving as expected, is to pass the flag directly to the server.py command within the start_linux.sh script. Here's how we'll do it: Revising Step 1: Directly Modify start_linux.sh (Safely) We'll edit the start_linux.sh script itself to ensure the --api flag is always included when Oobabooga launches. We'll be careful to only add one line. Open your Ubuntu WSL window. Navigate to your text-generation-webui directory: cd text-generation-webui Open the start_linux.sh script for editing using nano: nano start_linux.sh Inside nano, you'll see a script with many lines. You need to find the line that actually runs the server.py command. It usually looks something like this (it might have other flags, but python server.py will be there): python server.py --model "$model_name" --load-in-4bit --xformers $cmd_flags "$@" or python server.py --model "$model_name" --auto-devices $cmd_flags "$@" or even simpler: python server.py $cmd_flags "$@" Your goal is to add --api to the list of flags that are passed to server.py. Here's what you should change it to: Find the line that starts with python server.py and add --api right before $cmd_flags or "$@". Example: If you see: python server.py --model "$model_name" --load-in-4bit --xformers $cmd_flags "$@" Change it to: python server.py --model "$model_name" --load-in-4bit --xformers --api $cmd_flags "$@" If your python server.py line looks very different, please copy and paste that specific line here, and I'll tell you exactly where to put --api. Save and Exit nano: Press Ctrl + X (control key and 'x' key at the same time). It will ask if you want to "Save modified buffer?" Type Y for Yes, then press Enter. It will then ask for the "File Name to Write:" Just press Enter to confirm start_linux.sh. Now, start Oobabooga as you normally would: ./start_linux.sh Crucially, monitor the output carefully. You should now see a line like: API listening on: http://127.0.0.1:5000/ (or a different port if you've configured it). Please perform this modification to your start_linux.sh file. After you restart Oobabooga, paste the full output you see in your Ubuntu terminal, or at least the part that shows the API listening address. If you encounter any new errors, paste those as well.
