---
category: ai-tools
date: 2025-07-02
id: 19990
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is asking if he needs to remove previously added content from a nano
  configuration file.
tags:
- text-generation-webui
- oobabooga
- local-llm
- configuration
---
# so do i need to delete what we put in that nano?

### USER
so do i need to delete what we put in that nano?

### GEMINI
You hit on a very good question! And yes, you are absolutely right to ask about it. Yes, it is a good idea to delete the --api line from your CMD_FLAGS.txt file. Here's why: Avoids Redundancy and Potential Conflicts: If you add --api directly into start_linux.sh (which is what we're aiming for now), having it also in CMD_FLAGS.txt is redundant. While it usually won't cause an error, it's cleaner and reduces the chance of unexpected behavior if Oobabooga's flag parsing changes in the future. Clearer Source of Truth: By putting it directly in start_linux.sh, you know exactly where that flag is being applied every time. If CMD_FLAGS.txt was empty and not seemingly being picked up, then it's better to rely on the direct script modification. So, let's refine the steps: Revised Phase 1: Ensuring API is Enabled and Clean-Up Step 1: Remove --api from CMD_FLAGS.txt Open your Ubuntu WSL window. Navigate to your text-generation-webui directory: cd text-generation-webui Open the CMD_FLAGS.txt file for editing: nano CMD_FLAGS.txt Delete the line that says --api. If it's the only line, just make the file completely empty. Save and Exit nano: Press Ctrl + X. Type Y for Yes, then press Enter. Press Enter again to confirm the file name. Step 2: Directly Modify start_linux.sh (as previously instructed) This is the step we discussed before, to put --api directly into the line that executes server.py. Open your Ubuntu WSL window. Navigate to your text-generation-webui directory (if not already there): cd text-generation-webui Open the start_linux.sh script for editing: nano start_linux.sh Find the line that starts with python server.py. It's crucial to identify this line correctly. Common pattern: python server.py ... $cmd_flags "$@" Add --api right before $cmd_flags or "$@". For example, if your line is: python server.py --model "$model_name" --load-in-4bit --xformers $cmd_flags "$@" Change it to: python server.py --model "$model_name" --load-in-4bit --xformers --api $cmd_flags "$@" Again, if your python server.py line looks very different, please copy and paste that specific line here, and I'll tell you exactly where to put --api. Save and Exit nano: Press Ctrl + X. Type Y for Yes, then press Enter. Press Enter again to confirm the file name. Step 3: Run Oobabooga and Verify API Start Oobabooga as you normally would: ./start_linux.sh Carefully observe the output. You are looking for a line similar to: API listening on: http://127.0.0.1:5000/ Please go through these revised steps. After you've done this, paste the full output you see in your Ubuntu terminal when Oobabooga starts, or at least the part that shows the API listening address. If you encounter any errors or don't see the API listening message, please paste all relevant output.
