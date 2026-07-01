---
id: 842046
source: GEMINI
date: 2025-07-06
tags: ['coding', 'gemini', 'model', 'oobabooga', 'embedding', 'text-generation', 'python', 'go']
category: coding
sentiment: frustrated
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# (base) bryan_@DESKTOP-NG2I0P2:~/.cache/huggingface/hub$ # List contents to identify
ls

# Example: To delete a specific model cache
rm -rf models--sentence-transformers--all-MiniLM-L6-v2

# Or to delete everything (more aggressive, forces re-download of all HF models)
# rm -rf *
models--sentence-transformers--all-MiniLM-L6-v2  models--sentence-transformers--all-mpnet-base-v2  version.txt
(base) bryan_@DESKTOP-NG2I0P2:~/.cache/huggingface/hub$

### USER
(base) bryan_@DESKTOP-NG2I0P2:~/.cache/huggingface/hub$ # List contents to identify
ls

# Example: To delete a specific model cache
rm -rf models--sentence-transformers--all-MiniLM-L6-v2

# Or to delete everything (more aggressive, forces re-download of all HF models)
# rm -rf *
models--sentence-transformers--all-MiniLM-L6-v2  models--sentence-transformers--all-mpnet-base-v2  version.txt
(base) bryan_@DESKTOP-NG2I0P2:~/.cache/huggingface/hub$

### GEMINI
It looks like you've successfully listed the contents of your Hugging Face cache! From your output, you have two sentence-transformers models cached: models--sentence-transformers--all-MiniLM-L6-v2 models--sentence-transformers--all-mpnet-base-v2 The superboogav2 extension typically uses all-MiniLM-L6-v2 by default. To fix the recurring NameResolutionError for superboogav2, you should delete the models--sentence-transformers--all-MiniLM-L6-v2 cache folder and then restart Oobabooga with an active internet connection. This will force superboogav2 to redownload and properly re-cache the necessary embedding model. Here's the command to do that based on your ls output: rm -rf models--sentence-transformers--all-MiniLM-L6-v2 After running this: Ensure you have an active internet connection in your WSL2 terminal (ping google.com to check). Go back to your text-generation-webui directory. Run Oobabooga: ./installer_files/env/bin/python server.py This process should resolve the persistent loading issue for superboogav2.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]