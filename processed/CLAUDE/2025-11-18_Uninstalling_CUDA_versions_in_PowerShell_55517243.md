---
category: homelab
date: 2025-11-18
id: 842192
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: CLAUDE
summary: Bryan wanted to uninstall CUDA versions using PowerShell.
tags:
- cuda
- powershell
- gpu-drivers
- uninstallation
---
# Uninstalling CUDA versions in PowerShell

### HUMAN
how do i unistall cuda versions in powershell

### ASSISTANT
To uninstall CUDA versions in PowerShell, you have a few options:

## Option 1: Using Windows Settings (Recommended)
```powershell
# Open the uninstall programs interface
appwiz.cpl
```
Then look for NVIDIA CUDA entries and uninstall them one by one.

## Option 2: Using PowerShell with WMI
```powershell
# List all CUDA installations
Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -like "*CUDA*" }

# Uninstall a specific version (replace with exact name)
$cuda = Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -eq "NVIDIA CUDA Toolkit 11.8" }
$cuda.Uninstall()
```

## Option 3: Using winget (if available)
```powershell
# List installed CUDA versions
winget list | Select-String "CUDA"

# Uninstall specific version
winget uninstall "NVIDIA CUDA Toolkit 11.8"
```

## Option 4: Manual registry and file cleanup
After uninstalling through the above methods, you may want to clean up residual files:

```powershell
# Remove CUDA installation directories
Remove-Item -Path "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\*" -Recurse -Force

# Remove CUDA from environment variables
[Environment]::SetEnvironmentVariable("CUDA_PATH", $null, "Machine")
[Environment]::SetEnvironmentVariable("CUDA_PATH_V11_8", $null, "Machine")
```

**Note:** The WMI method (Option 2) can be slow. Option 1 or 3 are usually faster and more reliable. Always run PowerShell as Administrator for these operations.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
