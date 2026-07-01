---
id: 012298
source: GEMINI
date: 2025-06-25
tags: ['wsl2', 'ubuntu', 'linux-distribution', 'windows-subsystem-for-linux']
category: homelab
sentiment: exploratory
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is listing the installed WSL2 distributions, finding Ubuntu in a stopped state.
---
# PS C:\WINDOWS\system32> wsl --list --verbose                                                                              NAME      STATE           VERSION                                                                                     * Ubuntu    Stopped         2                                                                                           PS C:\WINDOWS\system32>     

### USER
PS C:\WINDOWS\system32> wsl --list --verbose                                                                              NAME      STATE           VERSION                                                                                     * Ubuntu    Stopped         2                                                                                           PS C:\WINDOWS\system32>     

### GEMINI
Perfect! That's exactly what we needed to see. You have one WSL2 distribution named Ubuntu and it's currently Stopped and using Version 2 (which is good!). Now, let's unregister it to achieve that clean slate. This will completely delete the Ubuntu installation and all its files. Step 2: Unregistering the WSL2 Distribution Action: In the same PowerShell (Administrator) window, type the following command exactly as shown, and then press Enter: wsl --unregister Ubuntu Explanation: wsl: This is the command-line tool for managing WSL. --unregister: This option tells WSL to delete a distribution. Ubuntu: This is the exact name of the distribution we found in the previous step. It's case-sensitive, so Ubuntu with a capital 'U' is important. What to expect: PowerShell will process the command, and after a moment, you should just get a new prompt (PS C:\WINDOWS\system32>) with no specific success message. This is normal for unregistration. Once you've run this command, just let me know, and we'll confirm that it's gone.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
