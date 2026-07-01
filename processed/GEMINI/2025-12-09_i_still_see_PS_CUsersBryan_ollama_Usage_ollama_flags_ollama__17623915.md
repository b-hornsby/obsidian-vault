---
id: 863035
source: GEMINI
date: 2025-12-09
tags: ['ai-tools', 'ollama', 'ai', 'gemini', 'model', 'defi', 'go', 'shell']
category: ai-tools
sentiment: frustrated
resolution: unresolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md', 'nodes/topics/personal/crypto-web3.md']
---
# i still see: PS C:\Users\Bryan> ollama
Usage:
  ollama [flags]
  ollama [command]

Available Commands:
  serve       Start ollama
  create      Create a model
  show        Show information for a model
  run         Run a model
  stop        Stop a running model
  pull        Pull a model from a registry
  push        Push a model to a registry
  signin      Sign in to ollama.com
  signout     Sign out from ollama.com
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command

Flags:
  -h, --help      help for ollama
  -v, --version   Show version information

Use "ollama [command] --help" for more information about a command.
PS C:\Users\Bryan>

### USER
i still see: PS C:\Users\Bryan> ollama
Usage:
  ollama [flags]
  ollama [command]

Available Commands:
  serve       Start ollama
  create      Create a model
  show        Show information for a model
  run         Run a model
  stop        Stop a running model
  pull        Pull a model from a registry
  push        Push a model to a registry
  signin      Sign in to ollama.com
  signout     Sign out from ollama.com
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command

Flags:
  -h, --help      help for ollama
  -v, --version   Show version information

Use "ollama [command] --help" for more information about a command.
PS C:\Users\Bryan>

### GEMINI
This output is a clear indicator that you missed a crucial step: The Ollama executable is still in your system's PATH environment variables. The program binary (ollama.exe) itself was not removed from a location that your terminal is configured to search, or the terminal session has not been refreshed. This is a classic lingering artifact. Here is the diagnosis and the precise plan to eliminate it: Diagnosis & Plan Problem: The core executable file (ollama.exe) still exists in a directory listed in your Path variable, or the Path variable itself was not properly cleaned up by the uninstaller. Your current PowerShell session is also holding a cached reference to the old command. Action Plan: Locate the remaining executable. Manually delete the file and/or the parent folder. Clean up the PATH variable (if necessary). Confirm the removal in a fresh session. Step-by-Step Fix 1. Locate and Delete the Executable First, ask the operating system where it is finding the command. In that same PowerShell window, type: Get-Command ollama | Select-Object -ExpandProperty Definition This command will output the full file path to the ollama.exe file that PowerShell is finding (e.g., C:\Program Files\Ollama\ollama.exe or similar). Go to that location in File Explorer. Delete the ollama.exe file. If the entire parent folder (e.g., C:\Program Files\Ollama) is empty or contains only the executable, delete the entire parent folder. 2. Verify PATH Cleanup The standard uninstaller should remove the entry for this folder from your PATH. Let's verify and manually remove it if it's still there. Press the Win key and type "env". Select "Edit environment variables for your account". In the bottom section, under "System variables", find the variable named Path. Click Edit.... Scan the list of directory entries for anything related to Ollama, such as: C:\Program Files\Ollama %ProgramFiles%\Ollama Select any Ollama-related entry and click Delete. Click OK on all windows to save the changes. 3. Final Verification (Crucial) Your existing PowerShell session is likely caching the old command. You must start fresh. Close your current PowerShell window. Open a brand-new PowerShell window. Type: ollama You should now finally see the expected error: "'ollama' is not recognized..." If you still see the usage text, the executable is still on your machine in a folder listed in the PATH, and you need to repeat Step 1 with the new path shown by Get-Command.