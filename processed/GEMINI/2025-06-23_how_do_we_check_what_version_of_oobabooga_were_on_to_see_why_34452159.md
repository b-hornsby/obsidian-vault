---
category: ai-tools
date: 2025-06-23
id: 338080
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user is trying to determine the version of Oobabooga they are running
  to troubleshoot why a specific setting is not appearing in the interface.
tags:
- oobabooga
- version-check
- troubleshooting
- local-ai
- configuration
---
# how do we check what version of oobabooga we're on to see why the setting isn't popping up? 

### USER
how do we check what version of oobabooga we're on to see why the setting isn't popping up? 

### GEMINI
You're asking a great question, Bryan! Oobabooga doesn't have a simple "About" menu that shows a version number like traditional software. For projects managed with Git (like Oobabooga), the "version" is typically identified by its Git commit hash. We actually already saw your current version's commit hash in your terminal output after you ran git reset --hard origin/main: HEAD is now at 17f9c188 Merge pull request #7092 from oobabooga/dev The commit hash 17f9c188 is your current version. This hash indicates you are on a very recent version of Oobabooga, specifically one where the dev branch was merged into main. Given how recent that commit is, it's actually quite puzzling that the dedicated RAG extensions (like rag_agent or document_loader) are not appearing in your "Available extensions" list under the "Settings" tab, nor is there a separate "Extensions" tab on your left sidebar. This suggests that the issue isn't that your Oobabooga is "too old" for RAG. Instead, it points to one of these possibilities: UI Anomaly/Specific Build: Your particular installation or a very specific minor revision of Oobabooga might have a different UI layout or simply doesn't expose those extensions in the usual way (even though the code for them might be present). Extension Not Activated in Your Setup: Perhaps a command-line flag is needed to activate the full extensions manager, or a certain prerequisite isn't met in your specific environment that prevents them from showing up. They've been moved/renamed to a less obvious place: We've checked the "Training" tab, but it's clearly for LoRA fine-tuning. Since your Oobabooga is updated to a very recent commit, it strongly suggests the RAG code should be there. The challenge is getting your UI to display and allow you to configure it. For now, the fact that you're on 17f9c188 tells us you're very up-to-date, which makes the absence of the RAG extension UI even more unusual.