---
id: 860524
source: CLAUDE
date: 2025-09-10
tags: ['blender-ai-agent', 'local-llm-integration', 'oobabooga-setup', 'wsl2-environment', 'cursor-integration', 'skybox-ai']
category: ai-tools
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is setting up an AI-powered Blender agent workflow using local LLMs and Skybox AI, and needs help with WSL2 environment setup and connecting Oobabooga to Cursor.
---
# AI-Powered Blender Agent Workflow

### HUMAN
working on getting oobabooga setup so i can have my local llm talk to cursor for this blender ai agent framework i'm working on. the entire point is this: You are building an **AI-powered Blender agent workflow** to create 3D visualizations for a **crypto project or content generation**, where Blender automatically generates and manipulates 3D scenes based on AI guidance. The project uses:
* **Blender 4.5** for 3D modeling, animation, and rendering.
* **AI agents** like CrewAI or local LLMs (Nous-Hermes or similar) to provide instructions for scene creation, object placement, animation, materials, or camera setups.
* **Skybox AI** to generate environment assets or backgrounds (skies, landscapes, space scenes, etc.), which Blender then integrates into the scene automatically.

### ASSISTANT
This sounds like a fascinating project! You're building a really innovative pipeline that combines local AI control with automated 3D content generation. Let me break down some key considerations and suggestions for your oobabooga + Cursor + Blender AI agent setup:

## Architecture Overview
Your workflow seems to follow this pattern:
**Local LLM (oobabooga)** → **Cursor IDE** → **Blender Python Scripts** → **3D Scene Generation** → **Skybox AI Integration**

## Key Integration Points

### 1. Oobabooga → Cursor Connection
- Use oobabooga's API server mode to expose your local LLM
- Cursor can connect via HTTP requests to localhost
- Consider using OpenAI-compatible API format for easier integration
- You might want to set up a custom Cursor extension or use existing AI code completion features

### 2. Blender Python API Strategy
- Leverage `bpy` (Blender Python API) for all scene manipulation
- Create modular functions for: object creation, material assignment, animation keyframes, camera positioning, lighting setup
- Consider using Blender's addon system for persistent functionality
- Set up proper error handling since Blender operations can fail silently

### 3. AI Agent Framework Integration
- **CrewAI**: Great for multi-agent workflows (one agent for modeling, another for materials, etc.)
- **Local LLM considerations**: Nous-Hermes 2 or CodeLlama variants work well for code generation
- Structure your prompts to output valid Python/Blender code directly

### 4. Skybox AI Integration
- Develop API wrapper for Skybox AI calls
- Implement automatic texture downloading and HDRI setup in Blender
- Consider caching generated assets to avoid API rate limits

## Recommended Technical Stack

```python
# Example structure for your Blender agent
class BlenderAIAgent:
    def __init__(self):
        self.llm_client = OobaboogaClient()
        self.skybox_client = SkyboxClient()
        
    def generate_scene(self, prompt):
        # AI generates Blender script
        script = self.llm_client.generate_blender_code(prompt)
        
        # Execute in Blender
        self.execute_blender_script(script)
        
        # Add environment
        hdri = self.skybox_client.generate_environment(prompt)
        self.apply_hdri(hdri)
```

## Potential Challenges & Solutions

**Challenge**: LLM generating invalid Blender code
**Solution**: Fine-tune prompts with working examples, implement code validation

**Challenge**: Skybox API rate limits
**Solution**: Asset caching system, batch processing

**Challenge**: Blender crashes from AI-generated scripts
**Solution**: Sandboxed execution, gradual scene building

## Crypto/Content Generation Applications
This setup could be perfect for:
- Automated NFT artwork generation
- Crypto project visualization (tokenomics, roadmaps)
- Dynamic content for social media
- Procedural game asset creation

Would you like me to help you with any specific part of this integration? I could help you set up the oobabooga API connection, create Blender Python templates, or design the agent communication protocol.

### HUMAN
okay so i've gotten the code all connected and i think we're good on that front (trying to connect a model to test this workflow out) but i need help getting rid of my old wsl2 environment and starting fresh so i can have oobabooga setup. currently using ubuntu 22.04.4.5 LTS

### ASSISTANT
Great! Let's get you a clean WSL2 environment for your oobabooga setup. Here's how to properly wipe your current Ubuntu installation and start fresh:

## Step 1: Check Current WSL Distributions
First, let's see what you have installed:
```powershell
wsl --list --verbose
```

## Step 2: Backup Any Important Data
Before nuking everything, make sure you've backed up:
- Any code/projects you want to keep
- SSH keys (`~/.ssh/`)
- Custom configs (`.bashrc`, `.zshrc`, etc.)
- Any model files or datasets

## Step 3: Unregister the Old Ubuntu Installation
```powershell
wsl --unregister Ubuntu-22.04
```
This completely removes the distribution and all its data.

## Step 4: Install Fresh Ubuntu
You have a few options:

### Option A: Latest Ubuntu from Microsoft Store
- Install "Ubuntu" (gets you the latest LTS)
- Or install "Ubuntu 22.04.3 LTS" if you want to stick with 22.04

### Option B: Command Line Installation
```powershell
wsl --install -d Ubuntu
```

## Step 5: Initial Setup After Fresh Install
Once you launch your new Ubuntu:

```bash
# Update everything first
sudo apt update && sudo apt upgrade -y

# Install essential development tools
sudo apt install -y git curl wget build-essential python3-pip python3-venv

# Optional: Install conda/miniconda for better Python environment management
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

## Step 6: Set Up for Oobabooga
```bash
# Create a dedicated directory
mkdir ~/ai-projects
cd ~/ai-projects

# Clone oobabooga
git clone https://github.com/oobabooga/text-generation-webui.git
cd text-generation-webui

# Run the installation script
./start_linux.sh
```

## Pro Tips for Your Setup:

**WSL2 Performance Optimization:**
```bash
# Add to ~/.bashrc for better performance
export CUDA_VISIBLE_DEVICES=0  # if you have GPU
export OMP_NUM_THREADS=$(nproc)
```

**Memory Management:**
Create `.wslconfig` in your Windows user directory (`C:\Users\YourName\.wslconfig`):
```ini
[wsl2]
memory=16GB  # Adjust based on your RAM
processors=8  # Adjust based on your CPU cores
swap=8GB
```

**For Your Blender AI Agent Workflow:**
Consider creating separate conda environments:
```bash
# Environment for oobabooga
conda create -n oobabooga python=3.10
conda activate oobabooga

# Environment for Blender scripting (if needed)
conda create -n blender-ai python=3.10
```

## Quick Verification Commands:
After setup, verify everything works:
```bash
# Check Python
python3 --version

# Check pip
pip3 --version

# Check CUDA (if GPU setup)
nvidia-smi

# Test oobabooga installation
cd ~/ai-projects/text-generation-webui
python server.py --help
```

Would you like me to walk you through any specific part of this process, or do you have questions about optimizing the setup for your particular hardware configuration?

### HUMAN
well i unregistered the old ubuntu but i dont know where to go from there

### ASSISTANT
Perfect! Now let's get you a fresh Ubuntu installation. Here's exactly what to do next:

## Install Fresh Ubuntu

### Option 1: Microsoft Store (Recommended)
1. Open Microsoft Store
2. Search for "Ubuntu"
3. Install either:
   - **"Ubuntu"** (gets you the latest LTS - currently 24.04)
   - **"Ubuntu 22.04.3 LTS"** (if you want to stick with 22.04 specifically)

### Option 2: Command Line (Faster)
Open PowerShell as Administrator and run:
```powershell
wsl --install -d Ubuntu
```

## First Launch Setup
After installation, launch Ubuntu from:
- Start Menu → Ubuntu
- Or type `ubuntu` in PowerShell

You'll see something like:
```
Installing, this may take a few minutes...
Please create a default UNIX user account...
Enter new UNIX username: [enter your username]
New password: [enter password]
Retype new password: [confirm password]
```

## Verify Installation
Once you're in the Ubuntu terminal, check everything is working:
```bash
# Check your Ubuntu version
cat /etc/os-release

# Check WSL version
wsl.exe --status
```

## Quick Initial Setup
Run these commands to get your system ready:
```bash
# Update package lists and upgrade
sudo apt update && sudo apt upgrade -y

# Install essential tools
sudo apt install -y git curl wget build-essential python3-pip python3-venv
```

Let me know when you've got Ubuntu installed and running - then we can move on to setting up oobabooga! Which installation method are you going with?

### HUMAN
ubuntu is up and running.. now what?

### ASSISTANT
Awesome! Now let's get oobabooga set up. Here's the step-by-step process:

## Step 1: Initial System Setup
```bash
# Make sure everything is up to date
sudo apt update && sudo apt upgrade -y

# Install essential development tools
sudo apt install -y git curl wget build-essential python3-pip python3-venv python3-dev
```

## Step 2: Create Project Directory and Clone Oobabooga
```bash
# Create a dedicated directory for your AI projects
mkdir ~/ai-projects
cd ~/ai-projects

# Clone the text-generation-webui (oobabooga)
git clone https://github.com/oobabooga/text-generation-webui.git
cd text-generation-webui
```

## Step 3: Run the Installation Script
```bash
# This will install all dependencies and set up the environment
./start_linux.sh
```

The installer will ask you some questions:
- **GPU acceleration**: Choose based on your hardware (NVIDIA = CUDA, AMD = ROCm, None = CPU only)
- **Installation type**: Choose the default options for most cases

## What to Expect
The installation process will:
- Download and install conda/miniconda if not present
- Create a Python environment
- Install PyTorch and other dependencies
- Set up the web interface

## After Installation
Once it's done, you should see the web interface start up and it will give you a local URL like:
```
Running on local URL:  http://127.0.0.1:7860
```

## Test the Setup
1. Open that URL in your Windows browser
2. You should see the oobabooga web interface
3. From there you can download and test models

**Quick question**: Do you have a dedicated GPU (NVIDIA/AMD) or will you be running on CPU? This will affect which installation options to choose.

Go ahead and start with the installation script - let me know if you run into any issues or questions during the process!

### HUMAN
okay its working and now i cant get into the webui. how do i get my model to work within oobabooga and how do i connect that to whats going on in  cursor

### ASSISTANT
Great! Let's get your model loaded and connected to Cursor. Here's the step-by-step process:

## Step 1: Access the WebUI

If you can't get to the web interface, let's troubleshoot:

```bash
cd ~/ai-projects/text-generation-webui

# Start the server manually
python server.py --listen --api
```

The `--listen` flag makes it accessible from Windows, and `--api` enables the API for Cursor.

You should see something like:
```
Running on local URL:  http://127.0.0.1:7860
Running on public URL:  http://0.0.0.0:7860
```

Try accessing it at: `http://localhost:7860` in your Windows browser.

## Step 2: Download a Model

Once you're in the WebUI:

1. Go to the **"Model"** tab
2. In the **"Download model"** section, enter a model name like:
   - `microsoft/DialoGPT-medium` (lightweight for testing)
   - `NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO` (if you have good hardware)
   - `TheBloke/CodeLlama-7B-Instruct-GGML` (good for code generation)

3. Click **"Download"**
4. Once downloaded, select it from the **"Model"** dropdown
5. Click **"Load"**

## Step 3: Enable API Mode

Make sure you're running with API enabled:
```bash
python server.py --listen --api --api-blocking-port 5000
```

This creates:
- WebUI at `http://localhost:7860`
- API at `http://localhost:5000`

## Step 4: Connect to Cursor

In Cursor, you need to configure it to use your local API:

### Option A: Using Cursor's AI Settings
1. Open Cursor Settings (Ctrl+,)
2. Look for AI/LLM settings
3. Add custom endpoint: `http://localhost:5000`

### Option B: Using Code/Extensions
Create a simple API client in your project:

```python
# api_client.py
import requests
import json

class LocalLLMClient:
    def __init__(self, base_url="http://localhost:5000"):
        self.base_url = base_url
    
    def generate(self, prompt, max_tokens=500):
        payload = {
            "prompt": prompt,
            "max_new_tokens": max_tokens,
            "temperature": 0.7,
            "top_p": 0.9,
            "do_sample": True
        }
        
        response = requests.post(f"{self.base_url}/api/v1/generate", json=payload)
        return response.json()

# Test it
client = LocalLLMClient()
result = client.generate("Write a Python function to create a cube in Blender:")
print(result)
```

## Step 5: Test the Connection

```bash
# Test API directly with curl
curl -X POST http://localhost:5000/api/v1/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Hello, how are you?",
    "max_new_tokens": 50
  }'
```

## Quick Troubleshooting:

**Can't access WebUI?**
- Try `http://localhost:7860` instead of `127.0.0.1:7860`
- Make sure Windows Firewall isn't blocking it
- Check if the process is actually running: `ps aux | grep python`

**Model won't load?**
- Check available RAM/VRAM
- Try a smaller model first
- Look at the console output for error messages

Let me know what happens when you try to access the WebUI and which model you want to use for your Blender AI agent!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
