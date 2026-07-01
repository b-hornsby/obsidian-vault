---
id: 442401
source: GEMINI
date: 2025-06-24
tags: ['coding', 'ai', 'gemini', 'model', 'oobabooga', 'llama.cpp', 'text-generation', 'defi']
category: coding
sentiment: frustrated
resolution: unresolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/topics/personal/crypto-web3.md']
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip uninstall flash-attn
Found existing installation: flash_attn 2.7.4.post1
Uninstalling flash_attn-2.7.4.post1:
  Would remove:
    /home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn-2.7.4.post1.dist-info/*
    /home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn/*
    /home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so
    /home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/hopper/*
Proceed (Y/n)? y
  Successfully uninstalled flash_attn-2.7.4.post1
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip uninstall flash-attn
Found existing installation: flash_attn 2.7.4.post1
Uninstalling flash_attn-2.7.4.post1:
  Would remove:
    /home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn-2.7.4.post1.dist-info/*
    /home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn/*
    /home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so
    /home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/hopper/*
Proceed (Y/n)? y
  Successfully uninstalled flash_attn-2.7.4.post1
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Excellent! That's exactly what we needed. You successfully uninstalled flash_attn-2.7.4.post1 and, crucially, the problematic flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so file. This removes the source of the "undefined symbol" error. Now, let's try launching Oobabooga again. Without flash_attn installed, transformers and sentence-transformers should fall back to standard (CPU or non-Flash-optimized GPU) attention mechanisms, allowing superboogav2 to load. Step 8: Re-launch Oobabooga and verify superboogav2 loading. Action: Ensure your virtual environment is active. (You should still see (.venv)). If not: cd ~/text-generation-webui source .venv/bin/activate Launch Oobabooga with the --extensions superboogav2 flag. We no longer need TRANSFORMERS_FLASH_ATTN_CUDA_HANDOFF=0 since flash-attn is removed, but keeping superboogav2 in the command line is good practice to ensure it loads. python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2 (Again, use your exact full command, including all the arguments you typically use). Carefully observe the terminal output. We are looking for the absence of the Failed to load the extension "superboogav2" error and, ideally, an INFO message that superboogav2 has loaded successfully. Once Oobabooga is running and you have the web UI accessible, confirm that the "SuperBooga" (or similar) tab now appears at the top. If it does, we are finally ready to start populating your knowledge base!