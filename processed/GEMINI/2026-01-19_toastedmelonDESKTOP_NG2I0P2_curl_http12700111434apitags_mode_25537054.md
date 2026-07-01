---
id: 809686
source: GEMINI
date: 2026-01-19
tags: ['ollama', 'local-llm', 'llama2', 'api-request', 'model-inspection']
category: ai-tools
sentiment: curious
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is checking the available models in his local Ollama setup using a curl request to the API.
---
# toastedmelon@DESKTOP-NG2I0P2:~$ curl http://127.0.0.1:11434/api/tags
{"models":[{"name":"llama2:latest","model":"llama2:latest","modified_at":"2026-01-19T12:44:03.210681932-05:00","size":3826793677,"digest":"78e26419b4469263f75331927a00a0284ef6544c1975b826b15abdaef17bb962","details":{"parent_model":"","format":"gguf","family":"llama","families":["llama"],"parameter_size":"7B","quantization_level":"Q4_0"}}]}toastedmelon@DESKTOP-NG2I0P2:~$

### USER
toastedmelon@DESKTOP-NG2I0P2:~$ curl http://127.0.0.1:11434/api/tags
{"models":[{"name":"llama2:latest","model":"llama2:latest","modified_at":"2026-01-19T12:44:03.210681932-05:00","size":3826793677,"digest":"78e26419b4469263f75331927a00a0284ef6544c1975b826b15abdaef17bb962","details":{"parent_model":"","format":"gguf","family":"llama","families":["llama"],"parameter_size":"7B","quantization_level":"Q4_0"}}]}toastedmelon@DESKTOP-NG2I0P2:~$

### GEMINI
Good. You've confirmed Ollama is alive, it’s listening on the local interface, and it has llama2 ready to go. You’ve cleared the biggest hurdle. Because you used --network=host in your previous step, the Open WebUI container is essentially "plugged in" to the same internal network as that Ollama instance. They are currently standing in the same room. The Moment of Truth Open your browser in Windows and go to: http://localhost:8080 What to Look For (The "No Fluff" Check) The Login Screen: It will ask you to create an account. This is a local account stored only on your machine. The first account created is the Admin. The Model Dropdown: Once logged in, click the "Select a model" dropdown at the top center/left. The Verification: If you see llama2:latest in that list, you have successfully bridged the gap. Potential "Failure at the Finish Line" Scenarios If the page doesn't load or the model isn't there, here is the objective list of what you likely messed up: Port Conflict: If you have something else running on port 8080 in Windows, Docker might be "up" but the traffic is blocked. If http://localhost:8080 fails, try http://127.0.0.1:8080. The Container Died: Use sudo docker ps. If the list is empty, the container crashed. Use sudo docker logs open-webui to see why it committed suicide. Ollama is "Local Only": Sometimes Ollama binds so tightly to the host that even the container can't see it. If the UI loads but shows no models, you need to restart Ollama with the binding variable: OLLAMA_HOST=0.0.0.0 ollama serve Strategic Optimization Once you confirm it's working, your next "level up" is to stop running this manually every time you reboot. Are you able to see the Open WebUI login page in your browser right now?
