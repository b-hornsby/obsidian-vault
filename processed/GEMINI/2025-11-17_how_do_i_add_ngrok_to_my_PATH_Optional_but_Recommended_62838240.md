---
category: coding
date: 2025-11-17
id: 229646
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is asking for instructions on how to add ngrok to his system PATH,
  likely for local LLM development.
tags:
- ngrok
- environment-variables
- system-path
- local-llm-setup
---
# how do i add ngrok to my PATH (Optional but Recommended):

### USER
how do i add ngrok to my PATH (Optional but Recommended):

### GEMINI
Adding ngrok to your system's PATH is generally straightforward, though the exact steps depend on your operating system (Windows, macOS, or Linux) and shell (e.g., Bash, Zsh, PowerShell). Here's a breakdown for the most common systems. 💻 Step 1: Download and Extract ngrok First, you need to download the ngrok binary and place it in an accessible location. Download: Go to the official ngrok website and download the package for your operating system. Extract: Unzip or extract the downloaded file. It will contain a single executable file, usually named ngrok. Placement: Move the ngrok executable to a permanent, memorable location on your computer. Recommended Location: A common and good location is often a bin directory within your user folder (e.g., ~/bin/ on Linux/macOS or a dedicated C:\ngrok\ folder on Windows). Crucial: Note the full path to the directory where you placed the ngrok executable. You will need this for the next step. 📂 Step 2: Add the Directory to Your PATH The PATH is a list of directories that your operating system searches automatically when you type a command. By adding the directory where you placed the ngrok executable to the PATH, you can run ngrok from any terminal window, regardless of your current directory. For macOS / Linux (Using Bash or Zsh) Open the Shell Configuration File: You need to edit your shell's configuration file. This is usually: ~/.bashrc or ~/.bash_profile (for Bash) ~/.zshrc (for Zsh, the default on modern macOS) Use a text editor like nano or vi, or a GUI editor: nano ~/.zshrc # or nano ~/.bash_profile Add the Export Command: Add the following line to the end of the file, replacing /path/to/ngrok/directory with the actual path from Step 1 (e.g., ~/bin): export PATH="$PATH:/path/to/ngrok/directory" Example (if you used ~/bin): export PATH="$PATH:~/bin" Save and Reload: Save the file and exit the editor. Then, apply the changes by running the following command, or by simply closing and reopening your terminal: source ~/.zshrc # or source ~/.bash_profile For Windows (Modern Method: System Settings) Open Environment Variables: Search for "Edit the system environment variables" in the Windows Start menu and open it. In the System Properties window, click the "Environment Variables..." button. Edit the Path Variable: Under the "User variables for [Your Username]" section (recommended for just your account), select the "Path" variable and click "Edit...". If you want it available for all users, edit the "Path" variable in the "System variables" section. Add the Directory: In the "Edit environment variable" window, click "New". Paste the full path to the directory where you placed the ngrok.exe file (e.g., C:\ngrok). Click "OK" on all windows to save the changes. Restart Terminal: Close any open Command Prompt or PowerShell windows and open a new one for the change to take effect. ✅ Step 3: Verify the Installation To confirm that ngrok is correctly in your PATH, open a new terminal or command prompt window and run the command: ngrok help If it displays the ngrok help documentation, you have successfully added it to your PATH! You can now run the ngrok command from any location. Would you like me to find the ngrok download link for a specific operating system?
