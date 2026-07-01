---
id: 631983
source: GEMINI
date: 2025-06-25
tags: ['coding', 'llm', 'ai', 'gemini', 'python', 'pip', 'terminal', 'compile']
category: coding
sentiment: executing
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# so i ran pip uninstall llama-cpp-python -y and it said: (llm-assist) bryan_@DESKTOP-NG2I0P2:~$ pip uninstall llama-cpp-python -yWARNING: Skipping llama-cpp-python as it is not installed.(llm-assist) bryan_@DESKTOP-NG2I0P2:~$

### USER
so i ran pip uninstall llama-cpp-python -y and it said: (llm-assist) bryan_@DESKTOP-NG2I0P2:~$ pip uninstall llama-cpp-python -yWARNING: Skipping llama-cpp-python as it is not installed.(llm-assist) bryan_@DESKTOP-NG2I0P2:~$

### GEMINI
Okay, that's perfectly fine. The WARNING: Skipping llama-cpp-python as it is not installed. message just confirms that the previous installation attempt failed to complete, so there was nothing to uninstall. This means we're still starting with a clean slate for the next try. Now, let's proceed with the more robust installation command that explicitly tells llama-cpp-python to build with CUDA support. Action: In your (llm-assist) Ubuntu terminal, paste and run the following command. This command is designed to force the build with CUDA enabled and prevent caching of previous failed attempts: CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python --no-cache-dir Remember: This compilation step will take some time (5-15 minutes or possibly more). You will see a lot of output as it compiles the C++ components. Please share the full output of this command once it has finished.