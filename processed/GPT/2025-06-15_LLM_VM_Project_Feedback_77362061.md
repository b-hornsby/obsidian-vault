---
id: 576981
source: GPT
date: 2025-06-15
tags: ['local-llm', 'virtual-machine', 'career-project', 'resume-building']
category: career
sentiment: exploratory
resolution: resolved
linked_projects: ['nodes/projects/operation-immortal-agent.md', 'nodes/projects/it-certification.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/it-certification.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan was seeking unbiased feedback on his idea to build a local LLM project using a VM to help land a tech job.
---
### What this means for your project:

- You can comfortably run medium-sized quantized LLMs locally — like llama.cpp with a 7B or maybe 13B parameter model if properly quantized.
- You have the option to experiment with GPU acceleration, speeding up inference if you want to go deeper.
- VM or WSL2 should have no problem running smoothly with this hardware, but I recommend allocating enough resources to your virtual environment — at least 4-8 cores and 16GB RAM reserved for it depending on your model size.

### Next steps

Since you’re preparing to run a local LLM, here’s what usually comes next:

1. **Clone the LLM repository you want to use**  
For example, if you’re using [llama.cpp](https://github.com/ggerganov/llama.cpp), which is a popular lightweight C++ implementation for running LLaMA models locally, you would run:

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
```

2. **Build the project**  
Once inside the repo folder, compile the code:

```bash
make
```

This builds the executable you’ll use to run the model.

3. **Download a compatible model file**  
You’ll need to download a quantized LLaMA model file (like 7B) from a trusted source or convert a model yourself. This step is crucial but depends on where you get your model.

4. **Run inference**  
After you have the model file, you can run commands to interact with the model locally.

### Step 1: Set up your virtual environment (VM or WSL2)

- Decide whether you want to use a full Linux virtual machine (e.g., via VirtualBox, VMware, or Hyper-V) or the Windows Subsystem for Linux 2 (WSL2).
- I recommend **WSL2** for simplicity and better integration with your Windows system.
- If you want a full VM instead, we can do that too—just let me know.

### Step 3: Clone and build the llama.cpp project

- Get the code from GitHub
- Compile it locally

### Step 5: Run your first local LLM inference test

- Run the basic command to chat or generate text

### Step 7: Document everything

- Write step-by-step notes, tips, troubleshooting
- Capture screenshots or terminal outputs
- Prepare your project for GitHub or blog post

**Check if you already have WSL2 installed:**

Open PowerShell (Admin) and run:

```powershell
wsl --list --verbose
```

If you see a Linux distro with version 2, you’re set.

If not, you’ll want to install WSL2.

**After installation:**

- Launch Ubuntu from the Start menu
- It will prompt you to create a Linux user account and password — go ahead and do that

### Here’s my constructive take:

**Pros:**

- **Technical depth & relevance:** Running an LLM locally is definitely a hot, bleeding-edge topic. It shows initiative, comfort with virtualization, Linux environments, and even machine learning concepts.
- **Portfolio value:** If you document it well—setup steps, troubleshooting, performance tuning, networking, integration with a helpdesk interface—it’s a real stand-out project that can impress hiring managers or recruiters.
- **Practical skills:** You’ll gain hands-on skills in Linux, virtualization, model deployment, command line, scripting, resource management — all transferable to many IT and DevOps roles.
- **Safe experimentation:** Using a VM or WSL to isolate the environment is smart. It reduces risk to your daily-use machine.

**Cons / Risks:**

- **Complexity:** This is a relatively advanced project. It might take longer than expected, especially if you hit hardware or software setup issues. You need patience and troubleshooting skills.
- **Hardware limitations:** Running large models locally requires good CPU/GPU and RAM. You’ll likely be limited to smaller quantized models unless you have a beefy setup.
- **Certification gap:** While this project shows technical skill, some entry-level roles might value formal certifications or practical IT support experience more than bleeding-edge AI projects.
- **Focus:** If your immediate goal is to land an entry-level IT or help desk job, you might want to balance this project with more foundational skills or certifications.

If you want, I can help you break down the setup and coding steps one-by-one, review your progress, or help with writing documentation and the project’s narrative.

Sound good?

### USER
do you remember this project?: "i have an idea for a project i need help working through that i think will help me stand out to maybe land a tech gig and finally get out of warehousing. i have that certificate from tiffin university for the A+ and Net+ course they offer and although that isn't the same as having the actual certification, it coming form a university itself i feel like could still help me. anyway, i was thinking about working on running LLM locally and documenting that as a project for that but i want to do it using a virtual machine sort of thing to avoid any issues with my actual system. good idea? be unbias here i need constructive criticism to make sure i'm using my time wisely here"

### USER
i have an idea for a project i need help working through that i think will help me stand out to maybe land a tech gig and finally get out of warehousing. i have that certificate from tiffin university for the A+ and Net+ course they offer and although that isn't the same as having the actual certification, it coming form a university itself i feel like could still help me. anyway, i was thinking about working on running LLM locally and documenting that as a project for that but i want to do it using a virtual machine sort of thing to avoid any issues with my actual system. good idea? be unbias here i need constructive criticism to make sure i'm using my time wisely here"

### ASSISTANT
Yep, I remember you shared that idea! You’re aiming to run a local LLM inside a virtual machine (or something like WSL2) to safely experiment and build a project that will help you stand out and eventually land a tech job beyond warehousing.

Here’s my straightforward, unbiased take:

### Potential downsides or risks:

- **Complexity:** Setting up and running LLMs locally isn’t trivial. It can be time-consuming, especially if you hit errors or hardware limits.
- **Hardware limits:** Big LLMs require powerful GPUs and tons of RAM; you may need to stick with smaller or quantized models.
- **Certifications vs projects:** Entry-level IT roles sometimes prioritize certifications and troubleshooting skills over advanced AI projects. So balance this with learning/practicing core IT skills.
- **Focus:** Make sure you don’t get lost in the complexity of AI and lose sight of your immediate goal to land a tech role.

If you want, I can help you plan and execute each step so you don’t get stuck or waste time.

Sound like a plan?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/it-certification|IT Certification]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]