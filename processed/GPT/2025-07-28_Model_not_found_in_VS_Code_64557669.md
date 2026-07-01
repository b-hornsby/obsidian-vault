---
category: ai-tools
date: 2025-07-28
id: 981066
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GPT
summary: Bryan was troubleshooting a 'model not found' error in VS Code's Continue.dev
  extension despite having the model installed in Ollama.
tags:
- ollama
- continue-dev
- vs-code
- codellama
- model-not-found
---
### ⚠️ Why it sometimes fails:

Even if the model is **already installed**, Continue might:

- Not detect it due to a config mismatch (`codellama` vs `codellama:7b-instruct`)
- Attempt to install a **different model variant** (e.g. base vs instruct version)
- Not be syncing with the Ollama CLI properly

### If pressing "Install" doesn’t work:
Then you’re dealing with a **model name mismatch or config issue**, and we’d want to:

1. Open your `.continue/config.json`
2. Manually insert the correct model block (like in my previous message)
3. Reload VS Code

If you want, I can help you troubleshoot step-by-step:

- What OS are you on?  
- What exact VS Code extension or setup are you using to connect to Ollama?  
- What commands or UI flow are you using when it says “model not found”?  
- Can you share the output of `ollama list` in VS Code terminal?

That way, we can pinpoint why VS Code can’t “see” the model you have running in Ollama.

### ASSISTANT
Perfect — that output confirms:

- ✅ The **Ollama daemon is running**
- ✅ The **`codellama:7b-instruct` model is installed locally**
- ✅ The **Ollama CLI works** from PowerShell

So the issue is most likely with how **VS Code (and Continue)** is trying to connect to Ollama or reference the model.

#### 2. **Restart Continue + VS Code**
Sometimes Continue doesn’t immediately pick up new models:
- Reload VS Code (`Ctrl + Shift + P` → "Reload Window")
- Or close and reopen VS Code completely

#### 🧠 If the issue persists:
Try these quick checks:

- ✅ Run this in the terminal to see if Ollama responds:
  ```bash
  ollama run codellama:7b-instruct
  ```

- ✅ Check for errors in the `Continue` output:
  - Go to `Output` tab in VS Code (bottom panel)
  - Select "Continue" in the dropdown — see if there’s an error like "Model not found", "Ollama not running", etc.

### ✅ Fix the model name in `config.yaml`

Just change this line:

```yaml
model: codellama-7b
```

To the **correct Ollama model name**:

```yaml
model: codellama:7b-instruct
```

Full corrected section:
```yaml
models:
  - name: CodeLlama Instruct
    provider: ollama
    model: codellama:7b-instruct
```

> ⚠️ Important: The colon (`:`) is required — Ollama uses it to separate the model name from its variant/tag.

Let me know if it works — or if you want to add multiple models to switch between!

### USER
it says that the model isn't found in ollama and that i need to install it (in vs code via continue) even though i have the model running in ollama?

### ASSISTANT
Thanks — that error tells us **exactly** what the issue is:

> ❌ **Model "codellama:7b" is not found in Ollama.**

But your installed model is:

> ✅ **codellama:7b-instruct**

### ✅ How to fix it (2-minute fix):

1. Press `Ctrl + Shift + P` → `Continue: Open Config`
2. In your `.continue/config.json`, **replace or edit** the model block like this:

```json
{
  "models": [
    {
      "title": "Code Llama 7B Instruct",
      "provider": "ollama",
      "model": "codellama:7b-instruct"
    }
  ]
}
```

> 🔁 If there’s already a `codellama:7b` entry, just change it to `codellama:7b-instruct`.

3. Save the file.
4. Reload VS Code (or just run `Reload Window` from the command palette).

Let me know if you want help editing your `config.json`. You can paste the contents here and I’ll adjust it for you.

### USER
can't i just press the install tab from the error that says that it can't be found?

### USER
PS C:\Users\Bryan> ollama list
NAME                     ID              SIZE      MODIFIED
codellama:7b-instruct    8fdf8f752f6e    3.8 GB    55 minutes ago
PS C:\Users\Bryan>