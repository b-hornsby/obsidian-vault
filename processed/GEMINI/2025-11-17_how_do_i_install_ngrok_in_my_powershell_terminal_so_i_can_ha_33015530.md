---
category: coding
date: 2025-11-17
id: 248430
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is asking for help installing ngrok in his PowerShell terminal to connect
  his Ollama model to Cursor IDE.
tags:
- ngrok-installation
- powershell
- ollama-integration
- cursor-ide
- local-llm-setup
---
# how do i install ngrok in my powershell terminal so i can have my model in ollama talk to cursor to plug my model in and use it? 

### USER
how do i install ngrok in my powershell terminal so i can have my model in ollama talk to cursor to plug my model in and use it? 

### GEMINI
Setting up ngrok to tunnel your Ollama model for use with Cursor in PowerShell involves three main phases: installing ngrok, configuring Ollama, and starting the ngrok tunnel. 1. Install and Configure ngrok in PowerShell 💻 The easiest way to install ngrok on Windows for use with PowerShell is by downloading the executable and configuring your account. Download ngrok: Go to the official ngrok download page and download the Windows ZIP file. Extract the contents of the ZIP file. A common location to extract the ngrok.exe file is a new folder like C:\ngrok. Sign up for an ngrok account: Visit the ngrok website and sign up for a free account to get your authtoken. Add ngrok to your PATH (Optional but Recommended): For ease of use, you can add the directory where you saved ngrok.exe (e.g., C:\ngrok) to your system's PATH environment variable. This lets you run the ngrok command from any PowerShell directory. Connect your ngrok account: Open your PowerShell terminal. Run the following command, replacing <your-token-here> with the authtoken you copied from the ngrok dashboard: ngrok config add-authtoken <your-token-here> 2. Configure Ollama for External Access 🌐 By default, Ollama only listens for connections on your local machine (localhost). You need to configure it to accept connections from other origins for ngrok to work. Set the CORS Environment Variable: Cursor needs the Cross-Origin Resource Sharing (CORS) setting enabled to connect through the ngrok URL. Open PowerShell as an Administrator. Run the following command to set the required environment variable for your user: [System.Environment]::SetEnvironmentVariable('OLLAMA_ORIGINS', '*', 'User') Restart Ollama: You must restart the Ollama service for the new environment variable to take effect. If Ollama is running in your system tray, right-click the icon and choose to quit, then relaunch it. If you run it via the command line, stop the process and restart it. A reliable way to restart is to stop the service and re-run the server: Stop the existing Ollama service/process. Run the Ollama server with the host set to listen on all interfaces: OLLAMA_HOST=0.0.0.0 ollama serve 3. Start the ngrok Tunnel and Connect to Cursor 🔗 Now you can create the secure public URL that Cursor needs. Ollama's default port is 11434. Start the ngrok tunnel: Open a new PowerShell window. Run the ngrok command to expose port 11434: ngrok http 11434 --host-header="localhost:11434" Note: The --host-header="localhost:11434" is critical as it ensures the correct header is forwarded, which Ollama often requires. Get the Public URL: The ngrok terminal will display a "Forwarding" section, providing a public HTTPS URL (e.g., https://73f1-92-233-157-239.ngrok-free.app). Copy this URL. Configure Cursor: Open the Cursor IDE and go to Settings $\rightarrow$ Models. Find the option to Add your custom model. Model Name: Enter the exact model name you pulled in Ollama (e.g., llama3:8b). API Key: Enter a placeholder like Ollama (no real key is needed). Base URL (or OpenAI Base URL): Paste the ngrok URL you copied, adding /v1 to the end to match the OpenAI-compatible API that Ollama exposes. Example: https://your-ngrok-url.ngrok-free.app/v1 Deselect all other non-local models (like GPT-4, Claude, etc.) to ensure Cursor only tries to use your local model. Click Verify or Save, and your Cursor IDE should now be using your local Ollama model via the ngrok tunnel. This video provides a visual guide on how to set up and use a local large language model within the Cursor IDE. How to Use a Local LLM within Cursor
