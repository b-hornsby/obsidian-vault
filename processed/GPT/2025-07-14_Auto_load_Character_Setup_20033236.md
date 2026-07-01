---
id: 694572
source: GPT
date: 2025-07-14
tags: ['oobabooga', 'auto-load-character', 'start-script', 'nano-editor', 'wsl2']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was trying to configure Oobabooga to automatically load a character when starting the web UI.
---
# Auto-load Character Setup

### ASSISTANT
Yes, you *can* set a default character to automatically load when you run `./start_linux.sh` in **oobabooga** or similar local LLM UIs. You just need to predefine it in the **launch options** or **configuration file** depending on how your setup works.

### ✅ Edit `start_linux.sh`

Open it with a text editor, then find the line that starts the server (usually `python server.py` or similar), and add:

```bash
--character "Your Character Name"
```

**Example modified line:**

```bash
python server.py --character "HelpfulAgent" --model "phi-3-mini-q4"
```

If the model is also not loading by default, you can add the `--model` flag too.

### 📝 Pro Tip:
Make sure:
- Your character is saved in the correct `/characters` folder.
- The name is exact (case-sensitive).
- The model is already downloaded or points to the right path.

### ✅ Step-by-step: Set Default Model in `start_linux.sh`

1. **Open the file for editing:**
   ```bash
   nano start_linux.sh
   ```

2. **Look for the line near the bottom** that starts with:
   ```bash
   python server.py
   ```
   or:
   ```bash
   python3 server.py
   ```

3. **Add the model flag like this**:
   ```bash
   python3 server.py --model "phi-3-mini-q4"
   ```

   Full example:
   ```bash
   python3 server.py --model "phi-3-mini-q4" --character "HelpfulAgent"
   ```

   You can include any other flags you want here too, like:
   - `--extensions` for specific UI features
   - `--load-in-4bit` or `--load-in-8bit` for memory optimization

4. **Save and exit nano:**
   - Press `Ctrl + O` to save
   - Press `Enter` to confirm
   - Press `Ctrl + X` to exit

Want to also default to a certain **preset**, **GPU config**, or **UI extension**? I can help tailor those into your `start_linux.sh` too.

### USER
what nano file did i have to edit to have it know to run the model automatically when i run ./start_linux.sh

### USER
can i set the character built in so when i run ./start_linux.sh it just knows to run that character along with the model?