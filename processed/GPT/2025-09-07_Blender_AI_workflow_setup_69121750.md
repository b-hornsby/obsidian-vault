---
source: GPT
date: 2025-09-07
category: ai-tools
id: 69121750
linked_nodes: ['nodes/people/bryan.md']
---
# Blender AI workflow setup

### ASSISTANT
Got it — let’s break it down clearly so Gemini (or anyone you hand this to) can immediately understand the project, the goal, and your current roadblocks. Here’s a thorough summary you can use:  

If you want, I can now **write a ready-to-go prompt for Gemini that includes all of this**, so it knows the project, your goal, and the exact blockers — basically a “catch-up” injection so you can start working there immediately.  

Do you want me to do that?

### USER
yeah can you explain what the project is, the goal and what it is that i'm trying to build. explain what i'm having trouble with as well so i can solve this please

### USER
can you bring up the last steps we were working on? trying to get blender connected to this whole workflow

### USER
you're missing the skybox details and what it is that this is for

### ASSISTANT
Ah! Perfect — let’s incorporate **Skybox AI** and clarify the **purpose of the project** so Gemini can fully understand. Here’s the updated summary:  

If you want, I can now **turn all of this into a single, concise Gemini prompt** that immediately catches it up to speed so you can start building/test scripts over there.  

Do you want me to do that next?

### ASSISTANT
Absolutely — here’s a concise but detailed prompt you can drop into Gemini to bring it up to speed on your Blender AI agent project:  

If you want, I can also **make a “super condensed” 3–4 sentence version** for Gemini that’s even faster to process but still catches it up fully. Do you want me to do that?

### USER
scratch that can you give me a prompt that catched gemini up to speed so i can work through this over there real fast? just trying

### ASSISTANT
Got it! Let’s pick up where you left off with connecting Blender to your AI workflow. From our last threads, the key points were:  

1. **Blender Python Environment**  
   - You confirmed that Blender 4.5 is installed and its Python executable is at:  
     ```
     C:\Program Files\Blender Foundation\Blender 4.5\4.5\python\bin\python.exe
     ```
   - You ran `--version` and it’s Python 3.11.11, so we’re good on the version side.  

2. **Installing Packages**  
   - You tried `pip install blender-python` but got errors — that’s expected because there’s no package called `blender-python` on PyPI. Blender uses its **bundled Python**, and you install packages into it by pointing `pip` directly to Blender’s Python.  

3. **Next Steps to Connect Blender to Your AI Agent Workflow**  
   Here’s what we need to do next:

   **Step 1: Ensure pip works inside Blender’s Python**  
   Open PowerShell and run:
   ```powershell
   & "C:\Program Files\Blender Foundation\Blender 4.5\4.5\python\bin\python.exe" -m ensurepip
   & "C:\Program Files\Blender Foundation\Blender 4.5\4.5\python\bin\python.exe" -m pip install --upgrade pip
   ```
   This ensures pip is up-to-date in Blender’s environment.  

   **Step 2: Install required Python packages**  
   Depending on your workflow, at minimum you’ll need packages like `requests` (for API calls), `numpy`, and possibly `crewai` if you’re connecting agents:
   ```powershell
   & "C:\Program Files\Blender Foundation\Blender 4.5\4.5\python\bin\python.exe" -m pip install requests numpy crewai
   ```

   **Step 3: Make Blender scripts communicate with your AI agents**  
   - You’ll likely have a Python script inside Blender that can call your local AI models or API endpoints.  
   - Example template inside Blender:
   ```python
   import requests

   # Example call to your AI agent
   response = requests.post("http://localhost:5000/query", json={"prompt": "Generate 3D scene setup"})
   print(response.json())
   ```
   - You can expand this to trigger Blender operations like adding objects, running simulations, or generating renders based on AI output.  

   **Step 4: Optional – Add a “Blender Agent Module”**  
   - Create a dedicated `.py` file for Blender automation that interacts with your AI workflow.  
   - Import it in Blender’s scripting editor and run it whenever you need AI-driven automation.
---

If you want, I can **write a concrete example of a Blender Python script that hooks directly into your CrewAI/LM workflow** so you can immediately test it inside Blender. This would effectively plug Blender into your AI agent ecosystem.  

Do you want me to do that next?