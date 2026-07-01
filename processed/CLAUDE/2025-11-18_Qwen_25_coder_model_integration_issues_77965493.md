---
id: 607888
source: CLAUDE
date: 2025-11-18
tags: ['qwen-2.5-coder', 'cursor-integration', 'lm-studio', 'local-llm']
category: ai-tools
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is experiencing issues integrating the Qwen 2.5 coder model into Cursor, even after switching to LM Studio for ease of use.
---
# Qwen 2.5 coder model integration issues

### HUMAN
why isn't my qwen 2.5 coder model not working in cursor? i switched to lm studio for ease of use but still no luck

### ASSISTANT
I can help troubleshoot your Qwen 2.5 Coder setup with Cursor and LM Studio. Here are the most common issues and solutions:

## Common Issues & Fixes

**1. API Endpoint Configuration**
- In Cursor, go to Settings → Models → Add Model
- Make sure the base URL matches LM Studio's server (usually `http://localhost:1234/v1`)
- Check that LM Studio's server is actually running (look for "Server Started" in LM Studio)

**2. Model Loading in LM Studio**
- Ensure the Qwen 2.5 Coder model is fully loaded in LM Studio before trying to use it
- Check the model name in LM Studio matches what you're entering in Cursor
- Try clicking "Start Server" in LM Studio if it's not already running

**3. Cursor API Configuration**
- In Cursor settings, select "OpenAI Compatible" as the provider
- Set the API key field (can be dummy text like "lm-studio" since LM Studio doesn't require auth)
- Model name should match exactly what LM Studio shows (e.g., `qwen2.5-coder-7b-instruct`)

**4. Firewall/Port Issues**
- Verify nothing else is using port 1234
- Check if your firewall is blocking local connections
- Try `http://127.0.0.1:1234/v1` instead of localhost

**Quick Test**: Open `http://localhost:1234` in your browser - you should see LM Studio's server page if it's running properly.

**What specific error are you seeing?** That would help me pinpoint the exact issue - for example:
- Connection errors?
- Model not responding?
- Authentication errors?
- Something else?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
