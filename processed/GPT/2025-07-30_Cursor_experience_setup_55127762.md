---
id: 216112
source: GPT
date: 2025-07-30
tags: ['continue-dev', 'config-yaml', 'ollama', 'cursor-alternative', 'local-llm', 'model-setup']
category: ai-tools
sentiment: building
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan was configuring Continue.dev with Ollama models and YAML config to replicate a Cursor-like experience locally and for free.
---
# Cursor experience setup

### ASSISTANT
Great question — and it’s **a key piece** of making Continue.dev behave more like Cursor.dev.

### 🔍 Breakdown of Each Context Provider

| Context Provider | What It Injects Into the Prompt | Why It Matters (Cursor Comparison) |
|
---
-
---
-
---
-
---
---|
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
---|
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-|
| `code`           | The open file or selected code   | Matches Cursor’s “Ask AI” on a file or code block |
| `folder`         | Folder structure, file list      | Like Cursor’s project-level awareness (helps with file references) |
| `terminal`       | Recent terminal output or commands | Lets model “see” command-line context (useful in full-stack/code-heavy workflows) |
| `docs`           | Related documentation (comments, docstrings, or markdown) | Helps answer questions about APIs or internal tools |
| `diff`           | Recent changes to the file/codebase | Simulates Cursor’s inline change tracking and smart suggestions |
| `problems`       | VS Code problem panel (linting, errors, warnings) | Like Cursor noticing compiler errors or TypeScript red squiggles |

## ✅ Example

Let’s say you highlight a function and say:

> “Refactor this into a more efficient async version.”

Here’s what happens with context enabled:

- `code` gives it the exact function
- `folder` gives it awareness of imports/files it may need to modify
- `docs` provides comments above the function
- `diff` lets it know what you just changed
- `problems` alerts it if your current version has an error

Without context, you’re flying blind — the model only sees **your selected text or message**, with no understanding of the bigger picture.

## 🔧 Recommended `config.yaml` Additions

### 💡 Model Assignments
```yaml
models:
  - name: LLaMA 3.1 Instruct
    model: llama3.1:8b-instruct-q4_K_M
    provider: ollama
  - name: Qwen Coder Autocomplete
    model: qwen2.5-coder:1.5b
    provider: ollama
    mode: autocomplete
```

### 🧠 Rules: Cursor-Inspired Prompt Behavior

```yaml
rules:
  - mode: chat
    prompt: >
      You are a helpful AI pair programmer. Respond clearly and directly. 
      Prefer concise explanations and relevant code examples when asked.
      If clarification is needed, ask brief follow-up questions.

  - mode: edit
    prompt: >
      Act as a code assistant. Make minimal, surgical edits to the selected code 
      based on the user's request. If the change is risky, ask first.

  - mode: apply
    prompt: >
      Implement the given instructions by modifying the relevant code. Do not
      add unrelated changes. Maintain consistent coding style with the project.

  - mode: plan
    prompt: >
      Create a concise, step-by-step plan to implement the requested feature or fix.
      Focus on logical sequencing and avoid unnecessary elaboration.

  - mode: autocomplete
    prompt: >
      Predict the most likely code continuation. Keep suggestions short and context-aware.
```

Want me to generate a complete `config.yaml` for you with everything above pre-filled?

### ASSISTANT
User is using `llama3.1:8b-instruct-q4_K_M` for chat, edit, and apply modes, and `qwen2.5-coder:1.5b` for autocomplete in Continue.dev.

### USER
so all that's left is editing the config.yaml?

### ASSISTANT
Thanks for the heads-up — it looks like Continue.dev is a bit strict with its YAML schema, especially the difference between `roles:` (which you correctly used) vs `modes:` (which I had accidentally swapped in my suggestion). Let's fix this cleanly.

name: llama3.1 8b
version: 1.0.1
schema: v1

models:
  - name: llama3.1 8b
    provider: ollama
    model: llama3.1:8b-instruct-q4_K_M 
    roles:
      - chat
      - edit
      - apply
    capabilities:
      - tool_use
    defaultCompletionOptions:
      contextLength: 8192

  - name: qwen2.5-coder 1.5b
    provider: ollama
    model: qwen2.5-coder:1.5b
    roles:
      - autocomplete
    defaultCompletionOptions:
      contextLength: 4096

context:
  - provider: code
  - provider: folder
  - provider: terminal
  - provider: docs
  - provider: diff
  - provider: problems

rules:
  - role: chat
    prompt: >
      You are a helpful, concise AI pair programmer. Answer clearly and include code when relevant.
      If unsure, ask clarifying questions. Be direct and practical.

  - role: edit
    prompt: >
      You are a precise coding assistant. Make minimal edits to the selected code as requested.
      Follow the project's style. Do not add anything unrelated.

  - role: apply
    prompt: >
      Implement the requested changes cleanly and efficiently. Maintain code structure and style.
      Avoid unnecessary changes. Use correct syntax.

  - role: plan
    prompt: >
      Output a step-by-step plan to implement the user's request. Be concise and logical.
```

## Final Step

After replacing your `config.yaml` with this version:

1. **Save the file**
2. **Restart VS Code**
3. **Open Continue sidebar → Confirm models show up**
4. **Try a chat/edit/apply action** to verify behavior

Let me know if you want me to walk through adding *custom tools*, *project indexing*, or *shortcuts* next.

### ASSISTANT
Yes — if this updated `config.yaml` works **and** you already have your **rules set up in the proper location**, then yes — you’re solid. You’ve now got a **local, offline Cursor-like experience** with:

### 🧠 What You’re *Effectively Getting Now*

- Smart contextual edits like Cursor’s “Edit with AI”
- Chat that understands your file and folder context
- Code-aware autocomplete suggestions (though not as powerful as GPT-4-Turbo — but fast and local)
- Minimal, intentional code edits (if your rules are tuned right)
- Plan and Apply mode support (if rules are configured there too)

### ✅ TL;DR: You're Good to Go

You’ve got the Continue.dev + Ollama setup configured properly to simulate the Cursor.dev experience **as close as possible offline** with your current models.

If you ever want to:
- Optimize the prompt rules
- Add auto-reply agents or scripted flows
- Or integrate local document lookups...

Let me know — but for now?  
**You’re officially Cursor-ing offline.**

### ASSISTANT
Great — your `config.yaml` is already well-structured! You're **90% of the way there**. To finish making Continue.dev behave like Cursor, you just need to:

### 2. **Add Context Providers** (so your model gets file + folder info like Cursor)

Add this section **below** your `models:` block (but before `rules:`):

```yaml
context:
  - provider: code
  - provider: folder
  - provider: terminal
  - provider: docs
  - provider: diff
  - provider: problems
```

name: llama3.1 8b
version: 1.0.1
schema: v1

models:
  - name: llama3.1 8b
    provider: ollama
    model: llama3.1:8b-instruct-q4_K_M 
    roles:
      - chat
      - edit
      - apply
    capabilities:
      - tool_use
    defaultCompletionOptions:
      contextLength: 8192

  - name: qwen2.5-coder 1.5b
    provider: ollama
    model: qwen2.5-coder:1.5b
    roles:
      - autocomplete
    defaultCompletionOptions:
      contextLength: 4096

context:
  - provider: code
  - provider: folder
  - provider: terminal
  - provider: docs
  - provider: diff
  - provider: problems

rules:
  - mode: chat
    prompt: >
      You are a helpful, concise AI pair programmer. Answer clearly and include code when relevant.
      If unsure, ask clarifying questions. Be direct and practical.

  - mode: edit
    prompt: >
      You are a precise coding assistant. Make minimal edits to the selected code as requested.
      Follow the project's style. Do not add anything unrelated.

  - mode: apply
    prompt: >
      Implement the requested changes cleanly and efficiently. Maintain code structure and style.
      Avoid unnecessary changes. Use correct syntax.

  - mode: plan
    prompt: >
      Output a step-by-step plan to implement the user's request. Be concise and logical.
```

## ✅ 1. Keep Your Working `models:` Block (as-is)

No changes here — this is solid and fully compatible:
```yaml
models:
  - name: llama3.1 8b
    provider: ollama
    model: llama3.1:8b-instruct-q4_K_M 
    roles:
      - chat
      - edit
      - apply
    capabilities:
      - tool_use
    defaultCompletionOptions:
      contextLength: 8192

  - name: qwen2.5-coder 1.5b
    provider: ollama
    model: qwen2.5-coder:1.5b
    roles:
      - autocomplete
    defaultCompletionOptions:
      contextLength: 4096
```

## ⚠️ 3. Skip `rules:` Section for Now

Unfortunately, it looks like Continue **might not currently support `rules:` in `config.yaml`**, or it needs to be defined elsewhere (like in a separate `prompt_rules.yaml` or in the extension settings GUI).

So:  
🛑 **Do not include the `rules:` section** in the YAML file for now — it's what's breaking model detection.

name: llama3.1 8b
version: 1.0.1
schema: v1

models:
  - name: llama3.1 8b
    provider: ollama
    model: llama3.1:8b-instruct-q4_K_M 
    roles:
      - chat
      - edit
      - apply
    capabilities:
      - tool_use
    defaultCompletionOptions:
      contextLength: 8192

  - name: qwen2.5-coder 1.5b
    provider: ollama
    model: qwen2.5-coder:1.5b
    roles:
      - autocomplete
    defaultCompletionOptions:
      contextLength: 4096

context:
  - provider: code
  - provider: folder
  - provider: terminal
  - provider: docs
  - provider: diff
  - provider: problems
```

## ✅ If You Do These Three Things in `config.yaml`, You’ll Be Very Close to Cursor:

### 1. **Model Assignments**
Tell Continue which model to use for each mode.

```yaml
models:
  - name: llama3.1
    provider: ollama
    model: llama3.1:8b-instruct-q4_K_M
    modes: [chat, edit, apply, plan]

  - name: qwen2.5-coder
    provider: ollama
    model: qwen2.5-coder:1.5b
    modes: [autocomplete]
```

### 3. **Enable All Relevant Context Providers**
These inject live coding context (like open files, diffs, folder structure, etc.).

```yaml
context:
  - provider: code
  - provider: folder
  - provider: terminal
  - provider: problems
  - provider: docs
  - provider: diff
```

Would you like me to generate the **full `config.yaml` file** for you so you can copy-paste it directly?

### TOOL
Model set context updated.

### ASSISTANT
Not quite — **just selecting the model and adding rules is a good start**, but it’s **not enough** to fully replicate the Cursor.dev experience. Cursor is more than just a model with some rules. It also tightly integrates contextual awareness, live indexing, diff tracking, and multi-modal context injection (terminal, docs, git, file system, etc). Here's a breakdown of **what’s missing and what you can do to get closer**:

## ❌ What You’re *Still Missing* vs Cursor
- **Live Indexing**: Cursor indexes your entire codebase and offers real-time semantic search. Continue does not yet replicate this fully offline.
- **Inline Autocomplete + Suggestions**: Continue doesn’t provide GPT-powered autocomplete like Cursor (this is being worked on).
- **Inline Edits + Diff Previews**: Cursor offers smarter code edits with inline previews. Continue’s edit mode is simpler.
- **Project-aware memory / embeddings**: Cursor can "remember" across multiple chats and files much better using cloud vector embeddings. Continue does not yet support persistent local memory or RAG.

## TL;DR
No — selecting the model and adding rules is a *good start*, but Cursor’s full experience depends on:
- Smart context injection
- Semantic indexing
- Inline editing/autocomplete
- Persistent memory

To get closer, use **full context providers**, **custom rules for each mode**, and consider integrating **local RAG or scripting tools** to simulate Cursor’s behavior. I can help you write a complete `config.yaml` + rule set tailored to your local model if you want.