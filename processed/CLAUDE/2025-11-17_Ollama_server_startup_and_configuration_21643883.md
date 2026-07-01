---
category: homelab
date: 2025-11-17
id: 169112
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: frustrated
source: CLAUDE
summary: The user is trying to get Ollama to utilize their NVIDIA RTX 3070's 8GB VRAM
  for running the qwen2.5-coder model, but the server config shows empty GPU environment
  variables, indicating the model isn't offloading to the GPU despite updated drivers.
tags:
- ollama
- gpu-acceleration
- nvidia-rtx-3070
- vram-utilization
- local-llm
---
# Ollama server startup and configuration

### HUMAN
what's happening here? PS C:\Users\Bryan> ollama list
NAME                                 ID              SIZE      MODIFIED
qwen2.5-coder:14b-instruct-q4_K_M    9ec8897f747e    9.0 GB    27 minutes ago
PS C:\Users\Bryan> ollama serve
time=2025-11-17T18:59:19.901-05:00 level=INFO source=routes.go:1544 msg="server config" env="map[CUDA_VISIBLE_DEVICES: GGML_VK_VISIBLE_DEVICES: GPU_DEVICE_ORDINAL: HIP_VISIBLE_DEVICES: HSA_OVERRIDE_GFX_VERSION: HTTPS_PROXY: HTTP_PROXY: NO_PROXY: OLLAMA_CONTEXT_LENGTH:4096 OLLAMA_DEBUG:INFO OLLAMA_FLASH_ATTENTION:false OLLAMA_GPU_OVERHEAD:0 OLLAMA_HOST:http://127.0.0.1:11434 OLLAMA_KEEP_ALIVE:5m0s OLLAMA_KV_CACHE_TYPE: OLLAMA_LLM_LIBRARY: OLLAMA_LOAD_TIMEOUT:5m0s OLLAMA_MAX_LOADED_MODELS:0 OLLAMA_MAX_QUEUE:512 OLLAMA_MODELS:C:\\Users\\Bryan\\.ollama\\models OLLAMA_MULTIUSER_CACHE:false OLLAMA_NEW_ENGINE:false OLLAMA_NOHISTORY:false OLLAMA_NOPRUNE:false OLLAMA_NUM_PARALLEL:1 OLLAMA_ORIGINS:[* http://localhost https://localhost http://localhost:* https://localhost:* http://127.0.0.1 https://127.0.0.1 http://127.0.0.1:* https://127.0.0.1:* http://0.0.0.0 https://0.0.0.0 http://0.0.0.0:* https://0.0.0.0:* app://* file://* tauri://* vscode-webview://* vscode-file://*] OLLAMA_REMOTES:[ollama.com] OLLAMA_SCHED_SPREAD:false OLLAMA_VULKAN:false ROCR_VISIBLE_DEVICES:]"
time=2025-11-17T18:59:19.903-05:00 level=INFO source=images.go:522 msg="total blobs: 5"
time=2025-11-17T18:59:19.903-05:00 level=INFO source=images.go:529 msg="total unused blobs removed: 0"
time=2025-11-17T18:59:19.904-05:00 level=INFO source=routes.go:1597 msg="Listening on 127.0.0.1:11434 (version 0.12.11)"
time=2025-11-17T18:59:19.904-05:00 level=INFO source=runner.go:67 msg="discovering available GPUs..."
time=2025-11-17T18:59:19.911-05:00 level=INFO source=server.go:392 msg="starting runner" cmd="C:\\Users\\Bryan\\AppData\\Local\\Programs\\Ollama\\ollama.exe runner --ollama-engine --port 64348"
time=2025-11-17T18:59:19.949-05:00 level=INFO source=types.go:60 msg="inference compute" id=cpu library=cpu compute="" name=cpu description=cpu libdirs=ollama driver="" pci_id="" type="" total="31.7 GiB" available="22.1 GiB"
time=2025-11-17T18:59:19.950-05:00 level=INFO source=routes.go:1638 msg="entering low vram mode" "total vram"="0 B" threshold="20.0 GiB"

### ASSISTANT
Based on your Ollama logs, here's what's happening:

## Current Status
You've successfully started the Ollama server, and it's running on your local machine at `127.0.0.1:11434`. You have the **Qwen2.5-Coder 14B** model installed (9 GB, quantized at Q4_K_M).

## Key Points from the Logs

**Good news:**
- Server is running properly (version 0.12.11)
- The model is installed and ready to use
- Server is listening on the correct port

**Important notice:**
- **"entering low vram mode"** - This is the critical message. Ollama detected that you have **no dedicated GPU VRAM** (`"total vram"="0 B"`)
- Your system is using **CPU-only inference** with 31.7 GB of system RAM (22.1 GB available)
- The threshold for low VRAM mode is 20 GB, so it's defaulting to CPU mode

## What This Means
Your Ollama installation will run the model using your **CPU instead of a GPU**. This means:
- ✅ It will work fine
- ⚠️ Inference will be **significantly slower** than with a GPU
- ✅ The Q4_K_M quantization you chose is appropriate for CPU usage (smaller and faster than full precision)

## To Use It
In another PowerShell window or terminal, you can now run:
```bash
ollama run qwen2.5-coder:14b-instruct-q4_K_M
```

The model should load and you can start chatting with it. Just expect slower response times due to CPU-only processing.

### HUMAN
so you're saying its not currently using any of my 8gb of vram?

### ASSISTANT
Exactly right! According to the logs, Ollama is reporting `"total vram"="0 B"` - meaning it's **not detecting your GPU at all**, so your 8GB of VRAM isn't being used.

## Why This Might Be Happening

1. **GPU drivers not installed/updated** - Ollama needs proper GPU drivers (NVIDIA CUDA, AMD ROCm, or Intel OneAPI depending on your GPU)

2. **GPU not compatible** - Ollama may not support your specific GPU model

3. **Environment variables not set** - Sometimes GPU visibility needs to be configured

## To Fix This

**First, identify your GPU:**
```powershell
wmic path win32_VideoController get name
```

Then depending on what you have:
- **NVIDIA GPU**: Install CUDA drivers from NVIDIA
- **AMD GPU**: Install ROCm (limited Windows support)
- **Intel GPU**: May need specific configuration

Once you have the right drivers installed, restart Ollama and it should detect your GPU. You'll see messages about GPU compute instead of just CPU, and it should use your 8GB VRAM instead of system RAM.

Would you like help figuring out which GPU you have and getting it working with Ollama?

### HUMAN
when i run that command i get this: PS C:\Users\Bryan> wmic path win32_VideoController get name
Name
NVIDIA GeForce RTX 3070
PS C:\Users\Bryan>

### ASSISTANT
Perfect! You have an **NVIDIA GeForce RTX 3070** with 8GB of VRAM - that's a great GPU for running LLMs and should work excellently with Ollama.

## The Problem
Ollama isn't detecting your GPU, which means you likely need to install or update your **NVIDIA CUDA drivers**.

## Solution

1. **Check if you have CUDA installed:**
   ```powershell
   nvidia-smi
   ```
   If this command works, it will show your GPU and driver info. If it doesn't work or shows an error, you need to install CUDA.

2. **Install/Update NVIDIA Drivers:**
   - Download the latest **Game Ready Driver** or **Studio Driver** from [NVIDIA's website](https://www.nvidia.com/download/index.aspx)
   - Or use GeForce Experience to update

3. **After installing drivers, restart your computer**

4. **Restart Ollama:**
   ```powershell
   ollama serve
   ```

Once the drivers are properly installed, you should see something like this in the logs instead:
```
level=INFO msg="inference compute" id=GPU-xxx name="NVIDIA GeForce RTX 3070" total="8.0 GiB"
```

And your model will run **much faster** using your GPU instead of CPU!

Try running `nvidia-smi` first and let me know what you see - that will tell us if your drivers are installed.

### HUMAN
so i updated my drivers and ran ollama serve again and got this?: PS C:\Users\Bryan> ollama serve
time=2025-11-17T19:08:52.523-05:00 level=INFO source=routes.go:1544 msg="server config" env="map[CUDA_VISIBLE_DEVICES: GGML_VK_VISIBLE_DEVICES: GPU_DEVICE_ORDINAL: HIP_VISIBLE_DEVICES: HSA_OVERRIDE_GFX_VERSION: HTTPS_PROXY: HTTP_PROXY: NO_PROXY: OLLAMA_CONTEXT_LENGTH:4096 OLLAMA_DEBUG:INFO OLLAMA_FLASH_ATTENTION:false OLLAMA_GPU_OVERHEAD:0 OLLAMA_HOST:http://127.0.0.1:11434 OLLAMA_KEEP_ALIVE:5m0s OLLAMA_KV_CACHE_TYPE: OLLAMA_LLM_LIBRARY: OLLAMA_LOAD_TIMEOUT:5m0s OLLAMA_MAX_LOADED_MODELS:0 OLLAMA_MAX_QUEUE:512 OLLAMA_MODELS:C:\\Users\\Bryan\\.ollama\\models OLLAMA_MULTIUSER_CACHE:false OLLAMA_NEW_ENGINE:false OLLAMA_NOHISTORY:false OLLAMA_NOPRUNE:false OLLAMA_NUM_PARALLEL:1 OLLAMA_ORIGINS:[* http://localhost https://localhost http://localhost:* https://localhost:* http://127.0.0.1 https://127.0.0.1 http://127.0.0.1:* https://127.0.0.1:* http://0.0.0.0 https://0.0.0.0 http://0.0.0.0:* https://0.0.0.0:* app://* file://* tauri://* vscode-webview://* vscode-file://*] OLLAMA_REMOTES:[ollama.com] OLLAMA_SCHED_SPREAD:false OLLAMA_VULKAN:false ROCR_VISIBLE_DEVICES:]"
time=2025-11-17T19:08:52.525-05:00 level=INFO source=images.go:522 msg="total blobs: 5"
time=2025-11-17T19:08:52.525-05:00 level=INFO source=images.go:529 msg="total unused blobs removed: 0"
time=2025-11-17T19:08:52.526-05:00 level=INFO source=routes.go:1597 msg="Listening on 127.0.0.1:11434 (version 0.12.11)"
time=2025-11-17T19:08:52.527-05:00 level=INFO source=runner.go:67 msg="discovering available GPUs..."
time=2025-11-17T19:08:52.533-05:00 level=INFO source=server.go:392 msg="starting runner" cmd="C:\\Users\\Bryan\\AppData\\Local\\Programs\\Ollama\\ollama.exe runner --ollama-engine --port 65200"
time=2025-11-17T19:08:52.571-05:00 level=INFO source=types.go:60 msg="inference compute" id=cpu library=cpu compute="" name=cpu description=cpu libdirs=ollama driver="" pci_id="" type="" total="31.7 GiB" available="21.4 GiB"
time=2025-11-17T19:08:52.571-05:00 level=INFO source=routes.go:1638 msg="entering low vram mode" "total vram"="0 B" threshold="20.0 GiB"

### ASSISTANT
Unfortunately, it's **still not detecting your GPU** - same issue as before (`"total vram"="0 B"`).

## Let's troubleshoot:

**1. First, verify your NVIDIA driver is actually working:**
```powershell
nvidia-smi
```
This should show your RTX 3070 and driver version. If this command fails, the driver didn't install correctly.

**2. Check if you restarted your computer** after installing the drivers - this is usually required for GPU drivers to fully initialize.

**3. If `nvidia-smi` works but Ollama still doesn't see the GPU:**

You might need to install **CUDA Toolkit** separately (the driver alone sometimes isn't enough for compute applications):
- Download from: https://developer.nvidia.com/cuda-downloads
- Choose Windows > x86_64 > your Windows version > exe (local)
- Install it, then restart your computer

**4. After restart, try Ollama again:**
```powershell
ollama serve
```

Let me know what `nvidia-smi` shows - that will tell us if the problem is with the driver installation or with Ollama detecting the driver.

### HUMAN
PS C:\Users\Bryan> nvidia-smi
Mon Nov 17 19:09:55 2025
+
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
--+
| NVIDIA-SMI 581.80                 Driver Version: 581.80         CUDA Version: 13.0     |
+
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
-
---
--+
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
-+
---
-
---
-
---
-
---
-
---
---+
| GPU  Name                  Driver-Model | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 3070      WDDM  |   00000000:01:00.0  On |                  N/A |
|  0%   41C    P5             45W /  220W |    1293MiB /   8192MiB |     14%      Default |
|                                         |                        |                  N/A |
+
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
-
---
--+
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
-+
---
-
---
-
---
-
---
-
---
---+
+
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
--+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            6260    C+G   ...ato\StreamDeck\StreamDeck.exe      N/A      |
|    0   N/A  N/A           10800    C+G   C:\Windows\explorer.exe               N/A      |
|    0   N/A  N/A           11292    C+G   ...indows\System32\ShellHost.exe      N/A      |
|    0   N/A  N/A           11876    C+G   ...2txyewy\CrossDeviceResume.exe      N/A      |
|    0   N/A  N/A           12808    C+G   ...IA App\CEF\NVIDIA Overlay.exe      N/A      |
|    0   N/A  N/A           13356    C+G   ...IA App\CEF\NVIDIA Overlay.exe      N/A      |
|    0   N/A  N/A           14420    C+G   ..._cw5n1h2txyewy\SearchHost.exe      N/A      |
|    0   N/A  N/A           14428    C+G   ...y\StartMenuExperienceHost.exe      N/A      |
|    0   N/A  N/A           16456    C+G   ....0.3595.80\msedgewebview2.exe      N/A      |
|    0   N/A  N/A           16828    C+G   ...8bbwe\PhoneExperienceHost.exe      N/A      |
|    0   N/A  N/A           17208    C+G   ...s\Mozilla Firefox\firefox.exe      N/A      |
|    0   N/A  N/A           18092    C+G   ...s\Mozilla Firefox\firefox.exe      N/A      |
|    0   N/A  N/A           18176    C+G   ...cord\app-1.0.9214\Discord.exe      N/A      |
|    0   N/A  N/A           21340    C+G   ...5n1h2txyewy\TextInputHost.exe      N/A      |
|    0   N/A  N/A           23976    C+G   ...ef.win7x64\steamwebhelper.exe      N/A      |
|    0   N/A  N/A           25132    C+G   ...roadcast\NVIDIA Broadcast.exe      N/A      |
|    0   N/A  N/A           26900    C+G   ...lpaper_engine\wallpaper64.exe      N/A      |
|    0   N/A  N/A           27044    C+G   ...rsair iCUE5 Software\iCUE.exe      N/A      |
|    0   N/A  N/A           28164    C+G   ...yb3d8bbwe\WindowsTerminal.exe      N/A      |
|    0   N/A  N/A           28480    C+G   ...26wp6bftszj\TranslucentTB.exe      N/A      |
|    0   N/A  N/A           28520    C+G   ...CUE5 Software\QmlRenderer.exe      N/A      |
+
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
--+
PS C:\Users\Bryan>

### ASSISTANT
Great! Your NVIDIA driver is working perfectly - **CUDA Version 13.0** is showing, and your GPU is active. The issue is that Ollama still isn't detecting it.

## The Problem
Ollama needs the **CUDA Toolkit** installed separately. Having the driver (which you have) isn't enough - you need the actual CUDA development libraries.

## Solution

**1. Download and install CUDA Toolkit 12.x:**
- Go to: https://developer.nvidia.com/cuda-downloads
- Select: **Windows > x86_64 > 11 > exe (local)**
- Download and run the installer (~3GB)
- Choose "Express" installation

**Note:** Even though `nvidia-smi` shows "CUDA Version: 13.0", that's just the maximum version your driver supports. You still need to install the actual toolkit. CUDA 12.x is the current stable version for Ollama.

**2. After installation, restart your computer** (important!)

**3. Verify CUDA is installed:**
```powershell
nvcc --version
```

**4. Start Ollama again:**
```powershell
ollama serve
```

After this, you should see your RTX 3070 detected with "8.0 GiB" VRAM, and your models will run **much faster** on the GPU instead of CPU!

### HUMAN
how do i uninstall the cuda version 13.0 so i can start fresh?

### ASSISTANT
Good thinking! Here's how to cleanly uninstall CUDA:

## Uninstall CUDA

**1. Open Windows Settings:**
```powershell
# Or just press Windows key and type "Add or remove programs"
```

**2. Search for and uninstall ALL NVIDIA CUDA components:**
Look for entries like:
- NVIDIA CUDA Toolkit (any version)
- NVIDIA CUDA Development
- NVIDIA CUDA Runtime
- NVIDIA CUDA Documentation
- NVIDIA CUDA Samples
- NVIDIA CUDA Visual Studio Integration

Uninstall **all of them**.

**3. Optionally, you can also use the NVIDIA uninstaller:**
- Go to: `C:\Program Files\NVIDIA Corporation\Installer2\`
- Look for an uninstaller executable related to CUDA

**4. After uninstalling, restart your computer**

## Important Note
The "CUDA Version: 13.0" shown in `nvidia-smi` is **not actually installed** - it just indicates the maximum CUDA version your driver *supports*. So you likely don't have CUDA Toolkit installed yet, which is why Ollama can't use your GPU.

You can verify by running:
```powershell
nvcc --version
```
If this gives an error saying `nvcc` is not recognized, then CUDA Toolkit was never installed.

**After confirming it's not installed (or after uninstalling), proceed with installing CUDA Toolkit 12.x** as I mentioned in my previous message.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]