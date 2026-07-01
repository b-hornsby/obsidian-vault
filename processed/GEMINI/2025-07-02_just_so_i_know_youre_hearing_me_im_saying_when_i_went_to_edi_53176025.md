---
category: ai-tools
date: 2025-07-02
id: 533464
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is clarifying that certain flags were missing when he edited a configuration
  file, and he's unsure if they are necessary.
tags:
- text-generation-webui
- oobabooga
- local-llm
- configuration
---
# just so i know you're hearing me, i'm saying when i went to edit the nano, the other flags weren't there when i opened it. i wasn't sure if i needed them to 

### USER
just so i know you're hearing me, i'm saying when i went to edit the nano, the other flags weren't there when i opened it. i wasn't sure if i needed them to 

### GEMINI
Yes, I'm absolutely hearing you clearly! Thank you for clarifying that the CMD_FLAGS.txt file was empty for you. That's a very important piece of information. You are correct – you absolutely do not need to manually add --listen or --some-other-flag to CMD_FLAGS.txt if they weren't there originally. I just used those as examples of what might be in someone's CMD_FLAGS.txt file. My apologies if that caused confusion. The core issue was that --api wasn't being picked up, and editing start_linux.sh directly is a more reliable way to ensure it's always included. So, to reiterate: You were right not to add those extra flags. The previous instruction to modify start_linux.sh directly is the correct path forward now, as it bypasses any potential issues with CMD_FLAGS.txt not being read or processed as expected by your specific start_linux.sh script. Let's proceed with that change to start_linux.sh. Have you had a chance to perform the steps from my previous message, specifically editing the start_linux.sh file to add --api directly to the python server.py line, and then restarting Oobabooga? Please paste the output you see after starting Oobabooga with the modified start_linux.sh script.
