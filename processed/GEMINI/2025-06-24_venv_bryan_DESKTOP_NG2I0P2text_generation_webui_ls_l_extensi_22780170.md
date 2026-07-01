---
id: 172502
source: GEMINI
date: 2025-06-24
tags: ['coding', 'module', 'ai', 'gemini', 'grok', 'model', 'oobabooga', 'openai']
category: coding
sentiment: curious
resolution: partial
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -l extensions/
total 64
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 Training_PRO
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 character_bias
drwxr-xr-x 3 bryan_ bryan_ 4096 Jun 18 21:29 coqui_tts
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 example
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 gallery
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 google_translate
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 long_replies
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 ngrok
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 22 18:00 openai
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 perplexity_colors
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 sd_api_pictures
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 send_pictures
drwxr-xr-x 3 bryan_ bryan_ 4096 Jun 18 21:29 silero_tts
drwxr-xr-x 3 bryan_ bryan_ 4096 Jun 23 16:54 superbooga
drwxr-xr-x 5 bryan_ bryan_ 4096 Jun 24 13:04 superboogav2
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 whisper_stt
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -l extensions/
total 64
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 Training_PRO
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 character_bias
drwxr-xr-x 3 bryan_ bryan_ 4096 Jun 18 21:29 coqui_tts
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 example
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 gallery
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 google_translate
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 long_replies
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 ngrok
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 22 18:00 openai
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 perplexity_colors
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 sd_api_pictures
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 send_pictures
drwxr-xr-x 3 bryan_ bryan_ 4096 Jun 18 21:29 silero_tts
drwxr-xr-x 3 bryan_ bryan_ 4096 Jun 23 16:54 superbooga
drwxr-xr-x 5 bryan_ bryan_ 4096 Jun 24 13:04 superboogav2
drwxr-xr-x 2 bryan_ bryan_ 4096 Jun 18 21:29 whisper_stt
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Aha! The problem is clear now. The ls -l extensions/ output shows that there is no webui_llama_cpp directory within your extensions/ folder. This means the llama.cpp integration is either not present, or it's named something else, or it's handled differently in your specific clone of Oobabooga's web UI. You have superbooga and superboogav2 directories, which are extensions, but nothing explicitly named llama_cpp or webui_llama_cpp. This explains why pip couldn't find the requirements.txt file in that path. This is a significant discovery. If the llama.cpp extension isn't in that directory structure, then the --loader llama.cpp argument will not work as expected because the necessary backend code for llama.cpp won't be found by the web UI. What we need to do: You need to ensure that the llama.cpp specific components are present in your Oobabooga installation. They are usually handled by download-model.py or specific installation instructions for llama.cpp itself. Let's check if the core llama.cpp library is even intended to be installed as an "extension" in your current version of the web UI, or if it's expected to be a top-level installation. Step 30: Verify llama.cpp Installation Method for Your Web UI Version I need you to tell me how you originally installed the llama.cpp backend for Oobabooga, or if you ever did. For example, did you: Run a download-model.py --llama-cpp command? Follow instructions to compile llama.cpp separately? Just assume it would work with --loader llama.cpp? If you're unsure, let's try a common way Oobabooga handles llama.cpp. Often, llama.cpp is built and managed via the oobabooga project's own tools rather than being a standard "extension" with a requirements.txt in that specific path. Action: Check for a llama.cpp directory at the root of your text-generation-webui folder: ls -l llama.cpp/ This would be the case if it's a sub-module or downloaded separately. If that doesn't exist, let's try to run the main installation script with the llama.cpp option, if one exists for your version. Please provide the output of ls -l llama.cpp/. This will help us confirm if it's located elsewhere.