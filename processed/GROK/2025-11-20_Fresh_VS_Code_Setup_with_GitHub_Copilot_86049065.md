---
id: 357716
source: GROK
date: 2025-11-20
tags: ['vs-code', 'github-copilot', 'fresh-install', 'setup-guide']
category: coding
sentiment: building
resolution: resolved
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan wanted a step-by-step guide to uninstall his old VS Code, do a fresh install, and set up GitHub Copilot.
---
# Fresh VS Code Setup with GitHub Copilot

### HUMAN
looking to start fresh with vs code. walk me through the steps to uninstall my old instance, install a fresh new one and guide me through how to plug in github copilot so i can try it out please

### ASSISTANT
Here's a complete, step-by-step guide to starting completely fresh with Visual Studio Code (VS Code) as of late 2025. I'll cover a **true clean uninstall** (removing the app + all settings/extensions/cache), a fresh install, and then setting up **GitHub Copilot** (including the free tier option so you can try it immediately).

Since you didn't specify your operating system, I'll provide instructions for **Windows**, **macOS**, and **Linux** (Ubuntu/Debian-based; adjust for other distros like Fedora).

### 1. Completely Uninstall Your Current VS Code (Clean Slate)
This removes the app **and** all user data (settings, extensions, caches) so your new install feels 100% fresh.

#### **Windows**
1. Go to **Settings > Apps > Installed apps** (or search "Add or remove programs").
2. Find **Visual Studio Code** → Click the three dots → Uninstall (follow prompts).
   - If it was a .zip/portable install, just delete the folder where you extracted it.
3. Delete user data folders (this is the "fresh start" part):
   - Press Win + R → Type `%APPDATA%\Code` → Delete the entire **Code** folder.
   - Type `%USERPROFILE%\.vscode` → Delete the **.vscode** folder.
   - (Optional but thorough) Type `%USERPROFILE%\AppData\Local\Programs\Microsoft VS Code` if anything remains.

#### **macOS**
1. Quit VS Code completely.
2. Open **Finder > Applications** → Drag **Visual Studio Code.app** to the Trash → Empty Trash.
3. Delete user data (open Terminal and run these commands one by one):
   ```
   rm -rf ~/Library/Application\ Support/Code
   rm -rf ~/.vscode
   rm -rf ~/Library/Caches/com microsoft.VSCode*
   rm -rf ~/Library/Saved\ Application\ State/com.microsoft.VSCode.savedState
   ```
   (You might need `sudo` for some if permissions are weird.)

#### **Linux** (Debian/Ubuntu example; adjust for your distro)
1. Uninstall the package:
   ```
   sudo apt purge code   # or "code-insiders" if you use that
   sudo apt autoremove
   ```
   - Snap install? `sudo snap remove code`
   - Flatpak? `flatpak uninstall com.visualstudio.code`
2. Delete user data:
   ```
   rm -rf ~/.config/Code
   rm -rf ~/.vscode
   ```

After this, restart your computer for good measure — now you're truly starting from zero.

### 2. Install a Fresh Copy of VS Code
Go to the official site: **https://code.visualstudio.com/** → Click **Download** for your OS (it auto-detects).

#### **Windows**
- Run the downloaded `.exe` (choose **User installer** or **System installer** — System adds "code" to PATH globally).
- Accept defaults (adds to PATH, creates desktop/start menu shortcuts).

#### **macOS**
- Open the downloaded `.zip` → Drag **Visual Studio Code.app** to your Applications folder.
- First launch: Right-click → Open (to bypass Gatekeeper if needed).

#### **Linux** (recommended .deb or .rpm)
- Debian/Ubuntu: Download `.deb` → Double-click or `sudo dpkg -i code_*.deb`
- Or add Microsoft's repo for auto-updates (recommended):
  ```
  wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
  sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
  sudo sh -c 'echo "deb [arch=amd64,arm64,armhf] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
  sudo apt update && sudo apt install code
  ```

Launch VS Code — it should feel brand new (no old themes/extensions/settings).

### 3. Set Up GitHub Copilot (Free Tier Available — You Can Try It Right Now!)
GitHub Copilot now has a **free plan** with monthly limits on completions and chat — perfect for trying it out without paying. (Paid plans remove limits and add more features.)

1. In VS Code, open the **Extensions view** (Ctrl+Shift+X or Cmd+Shift+X on Mac, or the square icon on the sidebar).
2. Search for **GitHub Copilot** (publisher: GitHub).
3. Install the main extension — it will automatically prompt to install **GitHub Copilot Chat** too (do it — that's the inline chat/agent features).
4. After install, you'll see a prompt in the status bar or a pop-up: **"Sign in to use Copilot"**.
   - Click it → Choose **Sign in with GitHub**.
   - A browser window opens → Log in to your GitHub account → Authorize VS Code.
   - If you don't have a paid Copilot subscription yet, it will automatically put you on the **Copilot Free** plan.
5. Done! Look for the Copilot icon in the status bar (bottom-right) — it should say "Copilot: Ready" or similar.

#### Quick Test
- Open any file (e.g., create a new `test.py` or `index.js`).
- Start typing a comment like `// function to sort an array of numbers` or `# fetch data from an API and parse JSON`.
- Gray "ghost text" suggestions appear → Press **Tab** to accept.
- For chat: Press **Ctrl+Enter** (or Cmd+Enter on Mac) in the editor, or open the Chat view (icon in sidebar) and ask something like "Explain this code" or "Write a React component for a todo list".

#### Tips & Shortcuts
- Cycle multiple suggestions: **Alt+] / Alt+[** (or Option on Mac).
- Open inline chat: **Ctrl+I** (Cmd+I on Mac).
- If you later want unlimited/full features: Go to https://github.com/settings/copilot (or inside VS Code: Copilot status bar icon → Manage subscription).

That's it — you now have a completely fresh VS Code with GitHub Copilot ready to go! If anything feels off (e.g., proxy issues behind a corporate network), let me know your OS and exact error, and I'll troubleshoot. Happy coding! 🚀
