---
category: ai-tools
date: 2025-06-23
id: 743528
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: curious
source: GEMINI
summary: The user is asking for a quick way to easily boot up and get started with
  Oobabooga (a web UI for running LLMs) without going through complex setup steps.
tags:
- oobabooga
- text-generation-webui
- local-llm
- quick-start
- setup
---
# is there a way to easily boot straight up and get going in oobabooga? 

### USER
is there a way to easily boot straight up and get going in oobabooga? 

### GEMINI
Yes, absolutely! The best way to "easily boot straight up and get going" with Oobabooga in your WSL2 environment is to create a simple shell script. This script will handle activating your virtual environment and launching the server with all the necessary arguments in one go. Here's how to set it up: Step 1: Create the Startup Script Open your Ubuntu WSL2 terminal. Navigate to your text-generation-webui directory: cd ~/text-generation-webui Create a new file called start_ooba.sh (or any name you prefer, like run.sh): nano start_ooba.sh (If nano isn't installed, you can use vi or vim or code . if you have VS Code integrated.) Paste the following content into the nano editor: #!/bin/bash echo "Starting Oobabooga text-generation-webui..." # Navigate to the correct directory (if not already there) # cd /home/bryan_/text-generation-webui # Uncomment if you run the script from somewhere else # Activate the Python virtual environment source .venv/bin/activate # Start the Oobabooga server with your preferred model and GPU settings # The --model flag can be added if you always want to load a specific model by name # e.g., --model "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf" python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --listen --port 53767 & # Give the server a moment to start up echo "Waiting for server to start..." sleep 10 # Adjust this if the model takes longer to load (e.g., 20 or 30 seconds) # Open the Oobabooga Web UI in your default Windows browser echo "Opening Oobabooga Web UI in browser..." wslview http://127.0.0.1:53767 echo "Oobabooga started. Check your browser." echo "To stop the server, return to this terminal and press Ctrl+C repeatedly." Explanation of additions: --listen: This makes the server accessible from outside localhost (not strictly necessary if you're only using 127.0.0.1, but good practice). --port 53767: Ensures it always tries to use this specific port. &: This runs the python3 server.py command in the background, so the script can continue to the sleep and wslview commands. sleep 10: Pauses the script for 10 seconds. This is crucial to give the Oobabooga server enough time to fully load the model and start listening before the browser tries to connect. You might need to increase this value if your model takes longer to load (e.g., sleep 20 or sleep 30). wslview http://127.0.0.1:53767: This is a WSL2 utility that will automatically open the specified URL in your default Windows web browser. This is the "boot straight up" part! Save the file and exit nano: Press Ctrl + O (to write out) Press Enter (to confirm filename) Press Ctrl + X (to exit) Step 2: Make the Script Executable You need to give the script permission to run as a program: chmod +x start_ooba.sh Step 3: Run Your Startup Script Now, whenever you want to start Oobabooga, all you have to do is: Open your Ubuntu WSL2 terminal. Navigate to your text-generation-webui directory: cd ~/text-generation-webui Run the script: ./start_ooba.sh The script will: Print status messages. Activate the virtual environment. Start the Oobabooga server. Wait for 10 seconds. Automatically open the Oobabooga Web UI in your default Windows browser! To Stop the Server Later: After the script runs, the terminal will still be active. To stop the Oobabooga server: Return to that same WSL2 terminal. Press Ctrl + C repeatedly until you see your command prompt return. This shell script makes launching Oobabooga a one-command process, automating all the setup steps for you!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]