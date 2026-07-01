---
id: 548923
source: GEMINI
date: 2025-07-29
tags: ['vs-code', 'output-tab', 'continue.dev', 'troubleshooting']
category: ai-tools
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is showing what appears in his VS Code output tab to troubleshoot why continue.dev isn't listed.
---
# this is all i see in the output tab

### USER
this is all i see in the output tab

### GEMINI
Okay, that's incredibly helpful! The second screenshot shows the Output tab, but it's currently showing Tasks in the dropdown. The reason you're not seeing any Continue logs is because you haven't selected Continue from that dropdown. Here's exactly what you need to do: Look at the Output tab in your VS Code window. Locate the dropdown menu on the right side of the Output tab (it currently says "Tasks" in your screenshot). Click on "Tasks" to open the dropdown list. Select "Continue" from the list of available output channels. Once you select "Continue", that panel should then display the logs from the Continue extension. After you've selected it, perform another "Developer: Reload Window" (Ctrl+Shift+P / Cmd+Shift+P -> "Reload Window") to ensure continue.dev re-initializes and outputs its startup logs to that channel. Please share whatever appears in the "Continue" output channel after you do this. That will finally give us the clues we need to understand why your model isn't appearing.
