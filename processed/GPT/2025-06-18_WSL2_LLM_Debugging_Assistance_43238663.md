---
source: GPT
date: 2025-06-18
category: ai-tools
id: 43238663
linked_nodes: ['nodes/people/bryan.md']
---
### ✅ Fix: Use CMake to build `llama.cpp`

Here’s a **clean step-by-step fix** tailored for WSL2:

### 📁 2. Navigate to your `llama.cpp` folder:

You're already in:

```bash
cd ~/llama.cpp
```

### ⚙️ 4. Build the project:

```bash
cmake --build . --config Release
```

This compiles everything using CMake. The binaries like `main`, `llama`, or `server` will be placed in the `build/` directory.

Let me know:
- Which exact model file you plan to run
- Whether you want to use `main`, `server`, or the chat UI

And I’ll guide you from there.

### ASSISTANT
You got this error because you’re inside `~/llama.cpp/models` and trying to run `./main` — but `main` is **not** in the `models` folder; it’s in the `bin` folder (e.g., `~/llama.cpp/bin/main` or `~/llama.cpp/build/bin/main`).

### Summary:

- `./main` runs `main` from the **current folder** — which is wrong in your case  
- You need to specify where `main` actually lives (usually `bin/` or `build/bin/`)

If you want, run this to see what’s inside:

```bash
ls -lh
```

And if you want help with downloading or placing your model files here, just say so!

### USER
can you get me back into the model so i can start from scratch and test the capabilities it has so far before moving on to the oobabooga thing we were working on?

### USER
i asked what is the difference between nvme storage and hdd? and it said 3??

### ASSISTANT
Perfect — that means the build finished successfully! 🎉

Your executables are now in the `bin/` folder inside your build directory.

If you want, I can help you craft the exact command to run your model or help troubleshoot any runtime issues.

What’s the exact model file you want to load? And what prompt or setup do you want to try?

### USER
bryan_@DESKTOP-NG2I0P2:~/llama.cpp/models$ ./main -m models/mistral-7b-instruct-v0.1.Q4_K_M.gguf --threads 20 --ctx-size 4096
-bash: ./main: No such file or directory
bryan_@DESKTOP-NG2I0P2:~/llama.cpp/models$

### ASSISTANT
Got it — the error `No such file or directory` means that either:

1. The executable **is not in `../bin/`** from `models` folder  
2. Or the executable has a different name or location  
3. Or it might not have executable permissions

2. **If no `bin` folder, check `build` directly:**

```bash
ls -l ../build
```

Sometimes binaries are in `build` directly, or inside a `build/bin` folder depending on your cmake setup.

4. **If you find the executable file**, note its full path and try running it using that path.

Send me the output of the above commands, and I’ll help you figure out the exact run command!

### ASSISTANT
Awesome, you found your executables in `../build/bin/`!

There isn’t a `main` executable, but you do have several similarly named tools, like:

- `llama-cli`  
- `llama-run`  
- `llama-server`  
- `llama-simple`  
- `llama-simple-chat`

### Try this command from your current folder (`~/llama.cpp/models`):

```bash
../build/bin/llama-cli -m mistral-7b-instruct-v0.1.Q4_K_M.gguf --threads 20 --ctx-size 4096
```

Or if you want to provide a prompt directly:

```bash
../build/bin/llama-cli -m mistral-7b-instruct-v0.1.Q4_K_M.gguf --threads 20 --ctx-size 4096 -p "Hello, how are you?"
```

Try that and let me know if it starts up or if you get any errors!

### ASSISTANT
You’re currently in `~/llama.cpp/build`. To go back to the main `llama.cpp` folder from there, run:

```bash
cd ..
```

That will take you back one level, landing you in `~/llama.cpp`.

If you want to be absolutely sure where you are after, run:

```bash
pwd
```

to print your current directory.

### ASSISTANT
Thanks for the full output — this is a **clear model loading error**:

```
gguf_init_from_file: failed to open GGUF file './models/mistral-7b-instruct-v0.1.Q4_K_M.gguf'
```

### ✅ Fix: Verify or move the model file

#### 1. **Check if the file exists**

Run this to check the contents of your `models` directory:

```bash
ls -lh ./models
```

Do you see `mistral-7b-instruct-v0.1.Q4_K_M.gguf` there?

#### 3. **Once it’s in place, re-run:**

```bash
./build/bin/llama-cli -m ./models/mistral-7b-instruct-v0.1.Q4_K_M.gguf --threads 16 --ctx-size 4096 --interactive
```

### ✅ Step-by-step: Launch your local model in interactive mode

#### 1. **Open WSL2**

Launch Ubuntu from your Start menu or terminal.

#### 3. **Launch the model in interactive mode**

```bash
./build/bin/llama-cli -m ./models/mistral-7b-instruct-v0.1.Q4_K_M.gguf --threads 16 --ctx-size 4096 --interactive
```

🔧 Adjust:
- `--threads 16` — change based on your CPU (you have 20 logical cores, so this is fine)
- `--ctx-size 4096` — higher context for longer prompts/responses
- `--interactive` — lets you chat with the model line by line

### ⚠️ If you get weird or short answers again:

Try re-running like this to give it a clean, deterministic prompt:

```bash
./build/bin/llama-cli -m ./models/mistral-7b-instruct-v0.1.Q4_K_M.gguf -p "What is the difference between NVMe and HDD?" --threads 16 --ctx-size 4096 --repeat_penalty 1.2 --temp 0.7
```

That sets better sampling parameters and gives you a one-shot reply.

## Step 1: Install required packages

```bash
sudo apt update
sudo apt install -y git build-essential cmake libcurl4-openssl-dev
```

## Step 3: Build with CMake

```bash
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

## Step 5: Run model interactively

From the `llama.cpp` root folder:

```bash
./build/bin/llama-cli -m ./models/mistral-7b-instruct-v0.1.Q4_K_M.gguf --threads 20 --ctx-size 4096 --interactive
```

If you want to test a one-off prompt instead of interactive mode, just add `-p "Your question here"` instead of `--interactive`:

```bash
./build/bin/llama-cli -m ./models/mistral-7b-instruct-v0.1.Q4_K_M.gguf --threads 20 --ctx-size 4096 -p "Hello, how are you?"
```

### Possible reasons for weird or wrong answers:

1. **Model isn’t fully loaded or initialized properly.** Sometimes the prompt gets truncated or the model state isn’t ready.

2. **Prompt formatting issues.** The CLI might expect specific prompt syntax or commands to trigger the generation correctly.

3. **Model or tokenizer mismatch.** If the model file or tokenizer config is corrupted, incomplete, or incompatible, output can be garbage.

4. **Insufficient context or parameters.** Context size, thread count, or other parameters might be misconfigured, causing incomplete or corrupted output.

### Quick explanation of NVMe vs HDD in case you want the answer now:

- **HDD (Hard Disk Drive):** Uses spinning magnetic disks to store data; slower read/write speeds; mechanical parts; cheaper per GB.

- **NVMe (Non-Volatile Memory Express) SSD:** Uses PCIe bus with flash memory; extremely fast read/write speeds; no moving parts; more expensive but way faster.

If you want to double-check your path at any time, use:

```bash
pwd
```

to see exactly where you are.

### ASSISTANT
Nice, you got it launching — good progress! 🎉

If the model starts but then says `command not found` or something similar **when you type a question**, it usually means the interactive input mode isn't working as expected, or the CLI expects a different input method.

#### 2. **If you want interactive mode, confirm the CLI expects it**

Some llama.cpp forks or versions have different behavior for interactive mode.

Try running:

```bash
../build/bin/llama-cli -m mistral-7b-instruct-v0.1.Q4_K_M.gguf --threads 20 --ctx-size 4096 --interactive
```

and then type your question.

#### 4. **Alternative: Use `llama-simple` or `llama-simple-chat`**

Try:

```bash
../build/bin/llama-simple -m mistral-7b-instruct-v0.1.Q4_K_M.gguf --threads 20 --ctx-size 4096
```

This binary is often a simpler interactive shell where you can type questions and get answers.

Try these and let me know exactly what you type and what the response or error is!

### ASSISTANT
Ah, gotcha! You want the exact command to **start the model interactively after reopening WSL2**, assuming everything is already built and your model files are in place.

### Quick explanation:

- `cd ~/llama.cpp` — go to the project folder  
- `./build/bin/llama-cli` — run the built executable  
- `-m ./models/...` — point to your model file  
- `--threads 20` — use 20 CPU threads (adjust to your CPU)  
- `--ctx-size 4096` — set the context size  
- `--interactive` — start interactive chat mode

If you want me to help make a simple script or alias to make this easier, just ask!

### ASSISTANT
Right, the key takeaway: **Makefile build is deprecated** — you must switch to CMake entirely.

The `make -j` command won’t work anymore in this repo version. So your next steps are:

1. **Don’t use `make` anymore here.**  
2. Use the CMake commands instead, as we discussed:
   - `mkdir build && cd build`  
   - `cmake ..` (with optional `-DLLAMA_CURL=OFF` if you want to skip CURL)  
   - `cmake --build . --config Release`

### How to fix the CURL error?

You have two options:

### Option 2: Disable CURL support if you don’t need it

If you want to **skip CURL support**, run:

```bash
cd ~/llama.cpp/build
cmake .. -DLLAMA_CURL=OFF
cmake --build . --config Release
```

This tells the build system not to look for CURL and just disables that feature.
---
### What do you want?

- Want to **install CURL** and build with it?  
- Or want to **skip CURL** entirely?  

Just let me know, I’ll help you finish the build and run your LLM.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]