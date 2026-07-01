---
id: 710393
source: CLAUDE
date: 2025-11-17
tags: ['ngrok', 'path-environment-variable', 'system-administration']
category: homelab
sentiment: curious
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is asking for instructions on how to add ngrok to the PATH environment variable.
---
# Adding ngrok to PATH environment variable

### HUMAN
how do i add ngrok to my PATH (Optional but Recommended):

### ASSISTANT
I'll help you add ngrok to your PATH. The steps vary depending on your operating system:

## **Windows**

1. **Find where ngrok is installed** (e.g., `C:\Users\YourName\ngrok`)

2. **Add to PATH:**
   - Press `Win + X` and select "System"
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "System variables" (or "User variables"), find and select "Path"
   - Click "Edit"
   - Click "New"
   - Add the full path to the folder containing `ngrok.exe`
   - Click "OK" on all dialogs

3. **Verify:** Open a new Command Prompt and type `ngrok version`

## **macOS/Linux**

**Option 1: Move to a directory already in PATH**
```bash
sudo mv ngrok /usr/local/bin
```

**Option 2: Add ngrok's current location to PATH**

1. Find where ngrok is located:
   ```bash
   which ngrok
   # or if you just downloaded it
   pwd
   ```

2. Add to your shell config file (`~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`):
   ```bash
   export PATH="$PATH:/path/to/ngrok/folder"
   ```

3. Reload your shell config:
   ```bash
   source ~/.bashrc  # or ~/.zshrc
   ```

4. **Verify:** Type `ngrok version` in a new terminal

After adding to PATH, you can run `ngrok` from any directory instead of typing the full path!
