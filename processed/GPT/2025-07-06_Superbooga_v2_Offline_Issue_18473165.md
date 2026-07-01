---
source: GPT
date: 2025-07-06
category: ai-tools
id: 18473165
linked_nodes: ['nodes/people/bryan.md']
---
# Superbooga v2 Offline Issue

### ASSISTANT
Got it — since you're using **Superbooga v2** locally *for RAG with .txt files*, and not calling external APIs or tools, the WebUI **should not** need an internet connection just to boot. If it does, that usually means **something in the frontend or backend is trying to reach the internet anyway**. Here are the most likely culprits based on your setup:

#### ✅ 2. **`--listen` or `--host` Bind Confusion**
- If Superbooga is launched with `--listen` or `--host 0.0.0.0`, it may rely on proper DNS resolution or network stack behavior, which can break when offline — especially if your machine tries to resolve local routes using Wi-Fi or VPN routing tables.

**Fix:**
Launch Superbooga with explicit loopback:
```bash
python server.py --host 127.0.0.1 --port 7860
```
(or the equivalent for your version)

#### ✅ 4. **Embedded Tool or Extension That Auto-Calls Out**
- If Superbooga has any **tools** or **extensions** enabled by default (e.g. web search tool, Wolfram Alpha, or even whisper STT cloud integrations), they might be initialized on boot even if unused.

**Fix:**
Check your `extensions/` or `config.json` and disable/remove unnecessary tools:
```json
"enable_tool_calling": false,
"use_remote_tools": false
```

### 🛠️ What You Can Do

- ✅ Try starting the project **completely offline**, then open DevTools (F12) in your browser to see what fails to load.
- ✅ Make sure you're not accidentally triggering extensions/tools that expect an API call.
- ✅ Post your launch command and `config.json` (sanitized) if you want a deeper dive.

Would you like help modifying your Superbooga setup to run **completely offline**, including UI assets? I can walk you through patching that.

### ASSISTANT
Yes, there are a few reasons why **Superbooga v2** (a custom oobabooga-based UI) might **require an internet connection to access the WebUI**, even if you're running it locally. Here are the most common ones:

### 🔐 2. **Auth or API Hooks (like HuggingFace/Google)**
Some custom builds check:
- **License/authentication** with an external server.
- Or auto-connect to **Hugging Face** or **OpenAI APIs** by default (even if you don’t want them to).

Check your `config.json`, `.env`, or command-line flags for anything like:
```bash
--api-key
--use-hf-api
--auth
```

### 🌐 4. **Misconfigured Network Bindings**
Sometimes it appears that you "need to be online," but the real issue is:
- You're **binding the server to a public IP** or `0.0.0.0` without proper routing.
- Your browser tries to resolve `localhost` or the port through your **DNS/internet stack** if you're offline.

You can try launching it with:
```bash
python server.py --listen --host 127.0.0.1
```
or
```bash
--listen --listen-port 7860
```

### ✅ How to Debug It

1. **Open DevTools (F12)** in your browser → Go to **Network tab** → See if anything’s trying to load from the web.
2. Run with the `--no-internet` or `--offline` flags (if supported) to see if it boots.
3. Try **disabling agent/tool integrations** or editing config files to remove web features.
---
### USER
I was using superboogav2 for RAG in this project and I made the .txt files for it to look through so I’m confused why it would require internet to boot into the webui?

### USER
Would there be a particular reason why superboogav2 requires being online in order to access the webui?