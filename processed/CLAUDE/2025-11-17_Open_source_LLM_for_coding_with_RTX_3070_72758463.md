---
category: homelab
date: 2025-11-17
id: 972801
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/coding.md']
linked_projects:
- operation-immortal-agent
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: stuck
source: CLAUDE
summary: The user wants to run a local open-source LLM optimized for advanced coding
  and agentic tasks on their homelab hardware, integrated with Cursor IDE, but is
  stuck on configuring the OLLAMA_ORIGINS environment variable on Windows and concerned
  about security exposure.
tags:
- ollama
- cursor-integration
- local-llm
- CORS-configuration
- agentic-coding
---
# Open source LLM for coding with RTX 3070

### HUMAN
what is the best open source llm model for advanced coding tasks given my current specs: Cpu: Intel Core i7-12700KMotherboard: Asus Prime Z790-PCpu cooler: Noctua NH-U12SMemory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40Storage: 970 Evo Plus M.2 SSD 2TBGraphics card: PNY GeForce RTX™ 3070 8GB XLR8 Gaming REVEL EPIC-X RGBCase: Corsair 4000D AirflowPSU: Corsair CX750MOS: Windows 11

### ASSISTANT
Given your specs, particularly the **RTX 3070 with 8GB VRAM**, here are the best open source LLMs for advanced coding tasks:

## Top Recommendations

**1. DeepSeek Coder V2 Lite (16B)** - Best overall choice
- Excellent coding performance, especially for completion and debugging
- Can run quantized (4-bit) on your 8GB VRAM
- Supports 128K context window
- Strong at multiple programming languages

**2. CodeLlama 13B** - Most reliable option
- Purpose-built for coding by Meta
- Well-optimized, runs smoothly quantized on 8GB
- Great for code completion, debugging, and explanation
- Good balance of quality and speed on your hardware

**3. Qwen2.5-Coder 14B** - Strong alternative
- Recent model with excellent coding benchmarks
- Performs well on complex coding tasks
- Can run quantized on your setup

## Practical Setup

With 8GB VRAM, you'll want to run **4-bit quantized versions** (GGUF format) using:
- **Ollama** (easiest) - `ollama run deepseek-coder-v2:16b-lite-instruct-q4_K_M`
- **LM Studio** (user-friendly GUI)
- **llama.cpp** (most control)

Your 32GB system RAM is a great backup for offloading layers if needed, and your i7-12700K will handle inference well.

## For Maximum Quality

If you're willing to run slower with RAM offloading, you could try **DeepSeek Coder V2 (236B)** or **Qwen2.5-Coder 32B** quantized, but expect significantly slower inference times.

**My suggestion**: Start with **DeepSeek Coder V2 Lite 16B (4-bit)** via Ollama - it offers the best balance of coding capability and performance for your hardware.

### HUMAN
for more clarity i want senior engineer level code. i want it to be a well rounded model in terms of coding task and able to do agentic work as well, all while utilizing the specs i have given you: Cpu: Intel Core i7-12700KMotherboard: Asus Prime Z790-PCpu cooler: Noctua NH-U12SMemory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40Storage: 970 Evo Plus M.2 SSD 2TBGraphics card: PNY GeForce RTX™ 3070 8GB XLR8 Gaming REVEL EPIC-X RGBCase: Corsair 4000D AirflowPSU: Corsair CX750MOS: Windows 11

### ASSISTANT
<thinking>
The user is asking for a more specific recommendation - they want:
1. Senior engineer level code quality
2. Well-rounded coding capabilities
3. Agentic work capability (tool use, reasoning, multi-step tasks)
4. Optimized for their specs (8GB VRAM RTX 3070, 32GB RAM, i7-12700K)

For senior-level coding and agentic work, the key constraints are:
- 8GB VRAM is limiting - need quantized models
- 32GB RAM is good for offloading
- They need reasoning capability, not just code completion

Best options for this use case:
1. **Qwen2.5-Coder 32B** (quantized) - Best coding quality that fits their specs
2. **DeepSeek Coder V2 236B** (heavily quantized with offloading) - Highest quality but slower
3. **Codestral 22B** (Mistral's coding model)

For agentic work specifically, models need:
- Strong reasoning
- Tool use capability
- Multi-step problem solving
- Code understanding and generation

Actually, let me reconsider. For senior-level code AND agentic work, I should look at:
- **Qwen2.5-Coder 32B** - excellent coding, supports tool use
- **DeepSeek-V2.5** or **DeepSeek-V3** - but these are huge (236B+)
- **Codestral 22B** - Mistral's coding model

Given the 8GB VRAM constraint, the realistic options are:
1. Run 32B models in Q4 quantization (will fit in VRAM + RAM offloading)
2. Run larger models heavily quantized with significant RAM offloading (slower)

For senior-level + agentic:
- **Qwen2.5-Coder 32B Instruct** (Q4_K_M) - Best balance
- **DeepSeek Coder V2 236B** (Q2/Q3) - Highest quality but very slow

I should also mention that true agentic work might benefit from using these models with frameworks like:
- AutoGen
- LangChain
- CrewAI

Let me give a clear, actionable recommendation.
</thinking>

For **senior engineer-level code** and **agentic work** on your specs, here's my recommendation:

## Primary Recommendation: **Qwen2.5-Coder 32B Instruct**

This is your best bet because:
- **Top-tier coding quality** - Rivals GPT-4 on many coding benchmarks
- **Strong reasoning** - Can handle complex, multi-step problems
- **Tool use capable** - Supports function calling for agentic workflows
- **Fits your hardware** - Q4 quantization (~18GB) runs via VRAM + RAM offloading

**Setup**: 
```bash
# Using Ollama
ollama run qwen2.5-coder:32b-instruct-q4_K_M
```

With your 8GB VRAM + 32GB RAM, expect:
- ~8-12 tokens/second (usable for development)
- Layers split between GPU and CPU
- Quality far superior to smaller models

## Alternative: **DeepSeek-Coder-V2 236B** (Q2/Q3 quantization)

If you're willing to sacrifice speed (~2-4 tokens/sec) for **maximum quality**:
- Truly senior-level architectural thinking
- Better at complex refactoring and system design
- Requires aggressive quantization + heavy RAM offloading

## For Agentic Workflows

Pair your model with:
- **Aider** - AI pair programming with git integration
- **Continue.dev** - VSCode/JetBrains extension with agentic features
- **Open Interpreter** - Code execution and multi-step tasks

These tools add the agentic layer (planning, tool use, iterative problem-solving) on top of the base model.

## Reality Check

With 8GB VRAM, you're bandwidth-limited. For truly production-grade agentic work at scale, consider:
- Cloud API access (DeepSeek API is very cheap: $0.14/1M tokens)
- Upgrading to 16GB+ VRAM in the future

**Bottom line**: **Qwen2.5-Coder 32B-Instruct (Q4)** gives you the best quality-to-performance ratio for senior-level coding and agentic work on your current hardware.

### HUMAN
when i download ollama the windows app is more like a chat gpt type interface. i'm trying to plug this local model into cursor using this method: https://themeansquare.medium.com/running-local-ai-models-in-cursor-the-complete-guide-4290fe0383fa

### ASSISTANT
Ah, you want to use the model as a **backend for Cursor**, not chat with it directly. Here's how to properly set this up:

## Step 1: Install Ollama (CLI, not the chat app)

Download from: https://ollama.com/download/windows

After installation, Ollama runs as a **background service** on `localhost:11434` - you won't see a UI window.

## Step 2: Pull Your Model

Open **Command Prompt** or **PowerShell** and run:

```bash
# For Qwen2.5-Coder 32B (recommended)
ollama pull qwen2.5-coder:32b-instruct

# OR for DeepSeek Coder V2 Lite (faster, less VRAM)
ollama pull deepseek-coder-v2:16b-lite-instruct-q4_K_M

# OR for CodeLlama 13B (most efficient)
ollama pull codellama:13b-instruct
```

Verify it's running:
```bash
ollama list
```

## Step 3: Configure Cursor

1. Open **Cursor Settings** (Ctrl+,)
2. Search for "**Models**" or go to **Cursor Settings > Models**
3. Add custom model:
   - **Model Name**: `qwen2.5-coder:32b-instruct` (or whichever you pulled)
   - **API Base URL**: `http://localhost:11434/v1`
   - **API Key**: `ollama` (or leave blank - Ollama doesn't need auth locally)

4. In Cursor's model selector (usually Ctrl+L for chat or Ctrl+K for inline), choose your custom model

## Step 4: Test It

- Press **Ctrl+L** to open Cursor chat
- Select your local model from the dropdown
- Ask it something like: "Write a Python function to parse JSON"

## Troubleshooting

**If Cursor can't connect:**

1. Verify Ollama is running:
```bash
curl http://localhost:11434/api/tags
```

2. Check if the port is accessible:
```bash
netstat -an | findstr 11434
```

3. Make sure Windows Firewall isn't blocking localhost connections

**For better performance in Cursor:**
- Use the model for **completions/chat**, not for every keystroke autocomplete
- Consider using smaller models for autocomplete and larger for chat/refactoring

## Model Recommendations for Cursor

- **For Chat/Complex Tasks**: `qwen2.5-coder:32b-instruct`
- **For Fast Autocomplete**: `codellama:7b-code` or `deepseek-coder:6.7b-base`
- **Balanced**: `deepseek-coder-v2:16b-lite-instruct`

You can run multiple models and switch between them in Cursor depending on the task!

### HUMAN
how do i set the CORS Environment Variable? it says to  use export OLLAMA_ORIGINS=* but when i do it says: C:\Users\Bryan>export OLLAMA_ORIGINS=*
'export' is not recognized as an internal or external command,
operable program or batch file.
C:\Users\Bryan>

### ASSISTANT
You're on **Windows**, so `export` is a Linux/Mac command. Here's how to set it on Windows:

## Option 1: Set Permanently (Recommended)

**Using Command Prompt (as Administrator):**
```bash
setx OLLAMA_ORIGINS "*"
```

**Using PowerShell (as Administrator):**
```powershell
[System.Environment]::SetEnvironmentVariable('OLLAMA_ORIGINS', '*', 'User')
```

Then **restart Ollama** for changes to take effect:
1. Open Task Manager (Ctrl+Shift+Esc)
2. Find "Ollama" in processes and end it
3. Restart Ollama from Start Menu

## Option 2: Set Temporarily (Current Session Only)

**Command Prompt:**
```bash
set OLLAMA_ORIGINS=*
ollama serve
```

**PowerShell:**
```powershell
$env:OLLAMA_ORIGINS="*"
ollama serve
```

## Option 3: Set System-Wide via GUI

1. Press **Windows Key + R**
2. Type `sysdm.cpl` and press Enter
3. Go to **Advanced** tab → **Environment Variables**
4. Under **User variables**, click **New**
5. Variable name: `OLLAMA_ORIGINS`
6. Variable value: `*`
7. Click **OK**
8. **Restart Ollama**

## Verify It's Set

In Command Prompt or PowerShell:
```bash
echo %OLLAMA_ORIGINS%
```

Or PowerShell:
```powershell
$env:OLLAMA_ORIGINS
```

Should return `*`

## Important Note

Setting `OLLAMA_ORIGINS=*` allows **any website** to access your local Ollama instance. Since you're only using it with Cursor locally, this is fine. But don't expose Ollama to the internet with this setting.

After setting the variable and restarting Ollama, Cursor should connect without CORS issues!

### HUMAN
how can i ensure that i dont expose ollama to the internet after running the setx OLLMA_ORIGINS "*" ?

### ASSISTANT
Great security thinking! Here's how to ensure Ollama stays local-only:

## 1. Verify Ollama is Bound to Localhost Only

By default, Ollama binds to `127.0.0.1` (localhost), which means it's **not accessible from the internet**. Verify this:

**PowerShell:**
```powershell
netstat -an | findstr 11434
```

You should see:
```
TCP    127.0.0.1:11434        0.0.0.0:0              LISTENING
```

✅ **Safe** - Only accessible from your computer
❌ **Unsafe** - If you see `0.0.0.0:11434` (accessible from any network interface)

## 2. Set OLLAMA_HOST to Localhost (Extra Safety)

Explicitly tell Ollama to only listen on localhost:

```bash
setx OLLAMA_HOST "127.0.0.1:11434"
```

Then restart Ollama.

## 3. Check Your Windows Firewall

Ollama should **not** have inbound rules allowing external access:

1. Open **Windows Defender Firewall with Advanced Security**
2. Click **Inbound Rules**
3. Look for any "Ollama" rules
4. If found, ensure they're set to **Block** or only allow **Local subnet**

## 4. If You're Behind a Router (Most Home Users)

You're already protected by **NAT** (Network Address Translation). External requests can't reach your computer unless you:
- Set up port forwarding (don't do this for Ollama)
- Put your PC in DMZ mode (don't do this)

## 5. Test External Access (Optional)

From another device on your network (phone, laptop):
```bash
curl http://YOUR_PC_IP:11434/api/tags
```

Replace `YOUR_PC_IP` with your computer's local IP (find it with `ipconfig`).

- **Should fail/timeout** = ✅ Secure
- **Returns data** = ❌ Exposed on local network (may need to adjust firewall)

## What OLLAMA_ORIGINS Actually Does

`OLLAMA_ORIGINS=*` **only affects CORS** (Cross-Origin Resource Sharing), which is a **browser security feature**. It does NOT:
- Open ports to the internet
- Change network bindings
- Bypass firewalls

It just tells Ollama: "Accept requests from any web page origin" (like Cursor's webview).

## Summary: You're Safe If...

✅ Ollama binds to `127.0.0.1` (default behavior)  
✅ You haven't manually port-forwarded 11434 on your router  
✅ Windows Firewall is enabled  
✅ You're on a home network behind a router  

**Bottom line**: With default settings, `OLLAMA_ORIGINS=*` is safe. It only allows local applications (like Cursor) to make cross-origin requests to your local Ollama instance.

### HUMAN
when i run netstat -an | findstr 11434 it doesn't return anything

### ASSISTANT
If `netstat` returns nothing, it means **Ollama isn't running**. Let's get it started:

## Step 1: Start Ollama

**Option A: Start from Start Menu**
1. Press Windows Key
2. Type "Ollama"
3. Click on the Ollama app

**Option B: Start from Command Line**
Open PowerShell or Command Prompt and run:
```bash
ollama serve
```

This will start Ollama and keep the window open (you'll see logs).

## Step 2: Verify It's Running

Open a **new** Command Prompt/PowerShell window and run:
```bash
netstat -an | findstr 11434
```

Should now show:
```
TCP    127.0.0.1:11434        0.0.0.0:0              LISTENING
```

Or test with:
```bash
ollama list
```

Should show your downloaded models.

## Step 3: Make Sure Ollama Starts Automatically

If you want Ollama to run in the background automatically:

1. Check if it's in your system tray (bottom-right, near clock)
2. If not, you may need to reinstall Ollama and ensure "Start on login" is enabled
3. Or manually add it to startup:
   - Press `Win + R`
   - Type `shell:startup`
   - Create a shortcut to Ollama there

## Troubleshooting

**If Ollama won't start:**

Check if something else is using port 11434:
```bash
netstat -an | findstr 11434
```

Or check Task Manager to see if Ollama is already running but hung:
1. Open Task Manager (Ctrl+Shift+Esc)
2. Look for "Ollama" processes
3. End them and restart

**After setting the environment variables**, you need to restart Ollama for them to take effect, so make sure you:
1. Close all Ollama processes
2. Restart Ollama
3. Then check the port binding

Let me know what you see after starting Ollama!

### HUMAN
when i ran ollama serve i got: C:\Windows\System32>ollama serve
time=2025-11-16T21:18:48.202-05:00 level=INFO source=routes.go:1544 msg="server config" env="map[CUDA_VISIBLE_DEVICES: GGML_VK_VISIBLE_DEVICES: GPU_DEVICE_ORDINAL: HIP_VISIBLE_DEVICES: HSA_OVERRIDE_GFX_VERSION: HTTPS_PROXY: HTTP_PROXY: NO_PROXY: OLLAMA_CONTEXT_LENGTH:4096 OLLAMA_DEBUG:INFO OLLAMA_FLASH_ATTENTION:false OLLAMA_GPU_OVERHEAD:0 OLLAMA_HOST:http://127.0.0.1:11434 OLLAMA_KEEP_ALIVE:5m0s OLLAMA_KV_CACHE_TYPE: OLLAMA_LLM_LIBRARY: OLLAMA_LOAD_TIMEOUT:5m0s OLLAMA_MAX_LOADED_MODELS:0 OLLAMA_MAX_QUEUE:512 OLLAMA_MODELS:C:\\Users\\Bryan\\.ollama\\models OLLAMA_MULTIUSER_CACHE:false OLLAMA_NEW_ENGINE:false OLLAMA_NOHISTORY:false OLLAMA_NOPRUNE:false OLLAMA_NUM_PARALLEL:1 OLLAMA_ORIGINS:[* http://localhost https://localhost http://localhost:* https://localhost:* http://127.0.0.1 https://127.0.0.1 http://127.0.0.1:* https://127.0.0.1:* http://0.0.0.0 https://0.0.0.0 http://0.0.0.0:* https://0.0.0.0:* app://* file://* tauri://* vscode-webview://* vscode-file://*] OLLAMA_REMOTES:[ollama.com] OLLAMA_SCHED_SPREAD:false OLLAMA_VULKAN:false ROCR_VISIBLE_DEVICES:]"
time=2025-11-16T21:18:48.203-05:00 level=INFO source=images.go:522 msg="total blobs: 5"
time=2025-11-16T21:18:48.204-05:00 level=INFO source=images.go:529 msg="total unused blobs removed: 0"
time=2025-11-16T21:18:48.204-05:00 level=INFO source=routes.go:1597 msg="Listening on 127.0.0.1:11434 (version 0.12.11)"
time=2025-11-16T21:18:48.205-05:00 level=INFO source=runner.go:67 msg="discovering available GPUs..."
time=2025-11-16T21:18:48.211-05:00 level=INFO source=server.go:392 msg="starting runner" cmd="C:\\Users\\Bryan\\AppData\\Local\\Programs\\Ollama\\ollama.exe runner --ollama-engine --port 49544"
time=2025-11-16T21:18:48.266-05:00 level=INFO source=types.go:60 msg="inference compute" id=cpu library=cpu compute="" name=cpu description=cpu libdirs=ollama driver="" pci_id="" type="" total="31.7 GiB" available="19.8 GiB"
time=2025-11-16T21:18:48.266-05:00 level=INFO source=routes.go:1638 msg="entering low vram mode" "total vram"="0 B" threshold="20.0 GiB"

### ASSISTANT
Perfect! Ollama is running. I can see some important info here:

## ✅ Good News

1. **Ollama is listening on `127.0.0.1:11434`** - This means it's **localhost only** and NOT exposed to the internet
2. **OLLAMA_ORIGINS is set correctly** - I can see it includes `*` in the origins list
3. Your environment variables from earlier (`OLLAMA_ORIGINS=*`) are working

## ⚠️ Issue Detected: "Low VRAM Mode"

```
level=INFO source=routes.go:1638 msg="entering low vram mode" "total vram"="0 B"
```

Ollama isn't detecting your **RTX 3070's 8GB VRAM**. It's falling back to CPU-only mode, which will be **very slow**.

## Fix GPU Detection

This is usually a CUDA/driver issue. Let's fix it:

### Step 1: Verify Your NVIDIA Drivers

Open PowerShell and run:
```bash
nvidia-smi
```

Should show your RTX 3070 and CUDA version. If this command fails, you need to update your NVIDIA drivers from: https://www.nvidia.com/download/index.aspx

### Step 2: Restart Ollama

After confirming nvidia-smi works:
1. Press `Ctrl+C` in the window running `ollama serve`
2. Close any other Ollama processes in Task Manager
3. Run again:
```bash
ollama serve
```

You should now see:
```
level=INFO source=types.go:60 msg="inference compute" id=GPU-... library=cuda compute="8.6" name="NVIDIA GeForce RTX 3070"
```

### Step 3: If Still Not Detecting GPU

Reinstall Ollama to get the latest CUDA libraries:
1. Uninstall Ollama from Windows Settings
2. Download fresh from https://ollama.com/download/windows
3. Install and restart

## For Now: Test with Cursor

Even in CPU mode, you can test the Cursor connection:

**Keep `ollama serve` running in that window**, then:

1. Open **Cursor**
2. Go to **Settings → Models**
3. Add custom model:
   - **API Base**: `http://localhost:11434/v1`
   - **Model**: `qwen2.5-coder:32b-instruct` (or whatever you pulled)
4. Test it in Cursor chat (Ctrl+L)

It will work but be slow until we fix GPU detection. Let me know what `nvidia-smi` shows!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]