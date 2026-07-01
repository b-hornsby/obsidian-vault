---
id: 988418
source: GEMINI
date: 2025-06-25
tags: ['oobabooga', 'Nous-Hermes-2-Mistral-7B', 'llama-cpp-loader', 'model-loaded']
category: ai-tools
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan confirmed that oobabooga successfully loaded the Nous-Hermes-2-Mistral-7B-DPO model via llama.cpp in his WSL2 environment.
---
# this happened in wsl2: main: server is listening on http://127.0.0.1:60851 - starting the main loop
12:57:34-609670 INFO     Loaded "Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf" in 4.01 seconds.
12:57:34-610377 INFO     LOADER: "llama.cpp"
12:57:34-610917 INFO     TRUNCATION LENGTH: 8192
12:57:34-611345 INFO     INSTRUCTION TEMPLATE: "Custom (obtained from model metadata)"
 

### USER
this happened in wsl2: main: server is listening on http://127.0.0.1:60851 - starting the main loop
12:57:34-609670 INFO     Loaded "Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf" in 4.01 seconds.
12:57:34-610377 INFO     LOADER: "llama.cpp"
12:57:34-610917 INFO     TRUNCATION LENGTH: 8192
12:57:34-611345 INFO     INSTRUCTION TEMPLATE: "Custom (obtained from model metadata)"
 

### GEMINI
This is fantastic news! The output 12:57:34-609670 INFO Loaded "Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf" in 4.01 seconds. confirms that the Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf model has been successfully loaded by Oobabooga's llama.cpp backend, and it only took 4.01 seconds. The GLIBCXX_3.4.30' not found error is gone, which means restarting the terminal and letting start_linux.sh handle the environment properly fixed the linking issue. What to do now: Go to your web browser where Oobabooga's UI is open (http://127.0.0.1:7860). Navigate to the "Chat" tab. You should now be able to type your questions into the input box and interact with the Nous-Hermes-2-Mistral-7B-DPO model! Congratulations! You have successfully set up a local large language model with GPU acceleration in your WSL2 environment.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
