---
id: 639087
source: GEMINI
date: 2025-07-29
tags: ['coding', 'ai', 'gemini', 'model', 'long', 'go', 'code', 'import']
category: coding
sentiment: building
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# when i look in the .continue folder on my pc this is what i see 

### USER
when i look in the .continue folder on my pc this is what i see 

### GEMINI
You've provided a screenshot (image_a52227.png) of your .continue folder, and it appears to contain: config.yaml config.json A history folder This is important! The presence of config.json alongside config.yaml is a potential source of conflict. According to continue.dev documentation, if both config.yaml and config.json are present in the ~/.continue (or %USERPROFILE%\.continue on Windows) folder, config.yaml will be loaded instead of config.json. However, in your scenario, where the extension is not even initializing enough to create its output channel or read any configuration, having both might be causing an unexpected issue during its very early startup phase. Even though the documentation says config.yaml takes precedence, if there's an older, perhaps malformed or empty config.json from a previous installation or a default creation, it might be confusing the extension's initial loading process, before it even gets to the point of properly parsing the YAML. Here's the next step, which is a very simple cleanup: Close VS Code. Go to your .continue folder: C:\Users\Bryan\.continue\ Delete the config.json file. Only keep config.yaml and the history folder. Open VS Code. Reload VS Code (Ctrl+Shift+P -> "Developer: Reload Window"). Check the Output tab again for "Continue". Check the continue.dev sidebar for your model. While continue.dev is supposed to prioritize config.yaml, completely removing the config.json ensures there's absolutely no ambiguity or potential for an older/conflicting JSON file to interfere with the startup process after your fresh install. This is a quick and harmless check to make.