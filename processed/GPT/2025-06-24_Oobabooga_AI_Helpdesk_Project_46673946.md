---
id: 099179
source: GPT
date: 2025-06-24
tags: ['oobabooga', 'wsl2', 'fresh-install', 'git-clone', 'setup-comparison']
category: homelab
sentiment: exploratory
resolution: resolved
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was considering wiping WSL2 and starting fresh, debating whether to download Oobabooga directly vs cloning via git.
---
# Oobabooga AI Helpdesk Project

### ASSISTANT
Great move starting fresh — sometimes a clean slate saves you hours of troubleshooting later. Let’s break this down:

### 📂 **How to Move a Downloaded Project into WSL2**

If you **download the .zip from GitHub**, here’s how to move it:

#### Option 1: Use Windows File Explorer to Move It
1. Download the `.zip` from [oobabooga's GitHub](https://github.com/oobabooga/text-generation-webui).
2. Unzip it in your `Downloads` folder.
3. Open your WSL2 home directory in Windows:
   - Type this in your WSL2 terminal:
     ```bash
     explorer.exe .
     ```
   - This opens your Linux home directory in Windows File Explorer.
4. Drag and drop the unzipped folder into the WSL2 window.

#### Option 2: Use the Linux `mv` Command (If File is in `/mnt/c`)
If the file is sitting in `C:\Users\<YourName>\Downloads`, you can move it like this:
```bash
cd ~
mv /mnt/c/Users/<YourName>/Downloads/text-generation-webui-main ./text-generation-webui
```

> Make sure to replace `<YourName>` with your actual Windows username.

Let me know if you want me to walk through the fresh install step-by-step again using Git, especially since you're aiming for performance and cleanliness.

### USER
So if I were to start from scratch, starting with oobabooga and downloading my model from there would probably result in less errors within wsl2?

### ASSISTANT
Of course — hit me with your question about oobabooga and your project. Just to recap, you're building a fully offline self-hosted AI Helpdesk Assistant using a local LLM (like Nous-Hermes-2 Mistral 7B) via oobabooga on WSL2, with plans to expand to .txt lookup, image generation, and voice input/output.

What do you need help with right now?

### USER
Just brainstorming for the time being but I completely wiped my wsl2 environment to have a fresh start and to try the whole process again to get everything running right. Would it make a difference downloading oobabooga from the website itself rather than trying to clone it with git? How would I get that over to my wsl2 environment if I chose to download it from the site itself?

### USER
Question about oobabooga and the project I’m working on

### USER
I was gonna say setting up oobabooga shouldn’t have been such a pain to set up from what I’ve seen in videos

### ASSISTANT
Yes — **starting from scratch and using `git clone` to get oobabooga** directly inside WSL2 is the *cleanest, most reliable method*, especially for your kind of project.

Here’s why that combo works best in WSL2:

### 🧼 Clean Fresh Start Process (Recommended)

Here’s your **step-by-step fresh start**:

```bash
# 1. Update WSL2 package list
sudo apt update && sudo apt upgrade -y

# 2. Install git (if not installed)
sudo apt install git -y

# 3. Clone oobabooga inside your home directory
cd ~
git clone https://github.com/oobabooga/text-generation-webui.git
cd text-generation-webui

# 4. (Optional but smart) Create a Python virtual environment
sudo apt install python3-venv -y
python3 -m venv venv
source venv/bin/activate

# 5. Install requirements
pip install --upgrade pip
pip install -r requirements.txt

# 6. Download your model using the built-in downloader
# Or manually drop your .gguf in the models folder later
```

Ready to go line-by-line when you are. Just say the word and I’ll walk you through the whole clean setup.

### ASSISTANT
You’re **100% right** — and honestly, it *shouldn’t* be that much of a pain. But here’s the truth behind why it **often is** (especially on Windows/WSL2), and why your experience isn’t just you "doing it wrong" — you're running into real, common gotchas:

### 🛠️ What Makes It Easier Now

Now that you've wiped everything and want to start from scratch the *right way*, here’s how we make it “just work” this time:

#### ✅ No more dragging files from Windows  
Everything stays inside the WSL2 Linux environment.

#### ✅ Use `git clone` to avoid zip/unzip chaos  
The repo stays clean, updateable, and correct.

#### ✅ Virtualenv prevents Python package conflicts  
No more “Torch won’t import” because of system-wide collisions.

#### ✅ Model download handled directly in the terminal  
No weird file path issues or permission problems.

Let me know if you want to do a **step-by-step clean install from the first command to the model launch** — we’ll make sure this time it’s smooth and solid.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]