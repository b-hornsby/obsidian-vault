---
category: coding
date: 2025-07-13
id: 612775
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- second-brain-vault
resolution: partial
sentiment: executing
source: GEMINI
summary: Bryan wants specific prompts to use in Cursor to scan his codebase for potential
  bottlenecks and adjust accordingly.
tags:
- cursor-ide
- code-scanning
- bottleneck-detection
- prompt-engineering
---
# if i were to check for each of these potential bottlenecks, can you write each prompt that i can put into cursor so i can have it scan my codebase and adjust if need be? make these concise and extremely clear in instruction please  

### USER
if i were to check for each of these potential bottlenecks, can you write each prompt that i can put into cursor so i can have it scan my codebase and adjust if need be? make these concise and extremely clear in instruction please  

### GEMINI
Here are concise and clear Cursor prompts to check for each potential bottleneck: Cursor Prompts for Bottleneck Analysis 🚀 LLM Manager Concurrency Analyze 'llm_manager.py' for potential concurrency bottlenecks when handling multiple agent requests. Suggest async/queuing mechanisms if not present. Config Manager Efficiency Evaluate 'config_manager.py' for efficiency. Identify potential performance bottlenecks with large configurations or frequent read/write operations. Tool Error Handling Scan all files in the 'tools/' directory. For each tool, check for robust error handling and input validation. Knowledge Base Scalability Assess 'knowledge_base_search.py' for scalability issues with a growing knowledge base. Propose efficient indexing/retrieval methods for offline use (e.g., local vector database integration). Agent Communication & Coordination Examine 'agents/' and 'tasks/' for complex multi-agent interaction patterns. Identify potential deadlocks or unexpected behaviors in handoffs. Log Collection Volume Analyze 'log_collection.py'. Suggest strategies for managing large volumes of logs and implementing retention policies.
